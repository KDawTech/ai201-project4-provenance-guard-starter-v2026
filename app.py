#!/usr/bin/env python3
"""Provenance Guard — CodePath AI201 Unit 7 Flask API.

Routes: POST /ping, POST /submit, POST /appeal, GET /log, GET /health.
Optional GET /content/<id> reports latest status from append-only audit events.
"""
import uuid
from flask import Flask, jsonify, request

import audit
import config
import detector
import scoring
import stylometry

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 128


class _LimiterOff:
    def limit(self, *args, **kwargs):
        return lambda func: func


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        payload = request.get_json(silent=True)
        if isinstance(payload, dict):
            creator = payload.get('creator_id')
            if isinstance(creator, str) and creator.strip():
                return creator.strip()
        return get_remote_address()

    limiter = Limiter(key_func=rate_limit_key, app=app,
                      storage_uri=config.RATE_LIMIT_STORAGE, default_limits=[])

    @app.errorhandler(429)
    def rate_limited(exc):
        payload = request.get_json(silent=True)
        payload = payload if isinstance(payload, dict) else {}
        audit.log_rejection(creator_id=str(payload.get('creator_id', 'unknown')),
                            reason='rate_limited', limit=str(exc.description))
        return jsonify(error='rate_limited', message='Try again later.'), 429


@app.errorhandler(413)
def too_large(exc):
    return jsonify(error='payload_too_large', message='Request body is too large.'), 413


@app.post('/ping')
def ping():
    payload = request.get_json(silent=True)
    payload = payload if isinstance(payload, dict) else {}
    return jsonify(ok=True, you_sent=payload.get('message'), service='provenance-guard')


@app.get('/health')
def health():
    return jsonify(ok=True, detector_model=config.DETECTOR_MODEL,
                   detector_loaded=detector._model is not None,
                   rate_limiting=config.RATE_LIMITING_ENABLED,
                   log_entries=len(audit.read_entries()))


def _invalid(creator_id, reason, message, status=400):
    audit.log_rejection(creator_id=str(creator_id or 'unknown'), reason=reason)
    return jsonify(error=reason, message=message), status


@app.post('/submit')
@limiter.limit(f'{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day')
def submit():
    """Accept text, collect two independent signals, log and return verdict."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _invalid(None, 'invalid_json', 'Send a JSON object with text and creator_id.')

    text = payload.get('text')
    creator_id = payload.get('creator_id')
    if not isinstance(creator_id, str) or not creator_id.strip():
        return _invalid(creator_id, 'invalid_creator_id', 'creator_id must be nonempty text.')
    creator_id = creator_id.strip()
    if len(creator_id) > config.MAX_CREATOR_CHARS:
        return _invalid(creator_id, 'invalid_creator_id', 'creator_id is too long.')
    if not isinstance(text, str) or not text.strip():
        return _invalid(creator_id, 'invalid_text', 'text must be a nonempty string.')
    if len(text) > config.MAX_TEXT_CHARS:
        return _invalid(creator_id, 'text_too_long', f'text exceeds {config.MAX_TEXT_CHARS} characters.', 413)
    # The language model cannot estimate perplexity from a token or two.
    if len(stylometry.words(text)) < 8:
        return _invalid(creator_id, 'text_too_short', 'Provide at least eight words.')

    try:
        model_score = detector.model_signal(text)
        style_score = stylometry.style_signal(text)
        confidence = scoring.combine_signals(model_score, style_score)
        guess, label = scoring.score_to_label(confidence)
    except detector.DetectorUnavailable:
        # Do not silently fabricate a score when the real model is missing.
        audit.log_rejection(creator_id=creator_id, reason='detector_unavailable')
        return jsonify(error='detector_unavailable',
                       message='Local GPT-2 model could not be loaded; run python detector.py.'), 503
    except (ValueError, OverflowError):
        audit.log_rejection(creator_id=creator_id, reason='unscorable_text')
        return jsonify(error='unscorable_text', message='The text could not be scored.'), 422

    content_id = uuid.uuid4().hex[:12]
    audit.log_decision(content_id=content_id, creator_id=creator_id, guess=guess,
                       model_score=model_score, style_score=style_score,
                       combined_score=confidence, label=label, status='decided')
    return jsonify(content_id=content_id, creator_id=creator_id,
                   guess=guess, confidence=confidence, label=label,
                   model_score=model_score, style_score=style_score,
                   status='decided'), 200


@app.post('/appeal')
def appeal():
    """Append a creator's challenge without rewriting the original verdict."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error='invalid_json', message='Send a JSON object.'), 400
    content_id = payload.get('content_id')
    reasoning = payload.get('reasoning')
    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify(error='invalid_content_id', message='content_id is required.'), 400
    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify(error='invalid_reasoning', message='reasoning must be nonempty text.'), 400
    if len(reasoning) > config.MAX_REASONING_CHARS:
        return jsonify(error='invalid_reasoning', message='reasoning is too long.'), 400

    content_id = content_id.strip()
    events = audit.entries_for(content_id)
    original = next((e for e in events if e.get('status') == 'decided'), None)
    if original is None:
        return jsonify(error='not_found', message='No submission has this content_id.'), 404
    if any(e.get('event') == 'appeal' for e in events):
        return jsonify(error='already_appealed', message='This submission is already under review.'), 409

    audit.log_appeal(content_id=content_id, creator_id=original['creator_id'],
                     reasoning=reasoning.strip())
    return jsonify(content_id=content_id, status='under_review',
                   message='Your appeal has been recorded for human review.'), 200


@app.get('/log')
def get_log():
    limit = request.args.get('limit', default=None, type=int)
    if limit is not None:
        limit = max(1, min(limit, 500))
    entries = audit.read_entries(limit=limit)
    return jsonify(count=len(entries), entries=entries), 200


@app.get('/content/<content_id>')
def content_status(content_id):
    """Optional extension: one item's latest status from the full event trail."""
    events = audit.entries_for(content_id)
    original = next((e for e in events if e.get('status') == 'decided'), None)
    if original is None:
        return jsonify(error='not_found'), 404
    status = 'under_review' if any(e.get('event') == 'appeal' for e in events) else 'decided'
    return jsonify(content_id=content_id, status=status, guess=original['guess'],
                   confidence=original['combined_score'], label=original['label'],
                   model_score=original['model_score'], style_score=original['style_score']), 200


if __name__ == '__main__':
    print(f'Provenance Guard: http://{config.HOST}:{config.PORT}')
    print('No API key needed. Run python detector.py once to download the local model.')
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
