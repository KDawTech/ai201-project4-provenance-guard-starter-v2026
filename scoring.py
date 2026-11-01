"""Confidence and reader-facing transparency labels for Provenance Guard."""
import math
import config


def combine_signals(model_score: float, style_score: float) -> float:
    """Weighted score with a false-accusation guard for signal disagreement.

    Both inputs and output are on the same 0..1 AI-likeness axis.
    If the two signals differ by >= 0.42, cap the AI-likeness score inside the
    unsure band, rather than assigning the AI label on contradictory evidence.
    """
    for name, value in [('model_score', model_score), ('style_score', style_score)]:
        if not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(f'{name} must be a finite number between 0 and 1')
    value = (config.WEIGHT_MODEL_SIGNAL * model_score
             + config.WEIGHT_STYLE_SIGNAL * style_score)
    if abs(model_score - style_score) >= config.SIGNAL_DISAGREEMENT_LIMIT:
        value = min(value, config.AI_THRESHOLD - 0.01)
    return round(max(0.0, min(1.0, value)), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """Three *reachable* labels; the unsure version avoids accusations."""
    if not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 1:
        raise ValueError('score must be a finite number between 0 and 1')
    if score <= config.HUMAN_THRESHOLD:
        return 'human', (
            'This writing appears likely to be human-written based on limited automated '
            'signals. This is not proof of authorship.'
        )
    if score >= config.AI_THRESHOLD:
        return 'ai', (
            'This writing shows signals sometimes associated with AI-generated text. '
            'Automated judgments can be wrong. The writer can appeal this assessment.'
        )
    return 'unsure', (
        'We cannot reliably determine who wrote this text from the available signals. '
        'No claim of AI authorship is being made.'
    )


def label_ranges() -> list[tuple[str, str]]:
    return [
        ('high-confidence human', f'0.00 - {config.HUMAN_THRESHOLD:.2f} (inclusive)'),
        ('unsure', f'>{config.HUMAN_THRESHOLD:.2f} and <{config.AI_THRESHOLD:.2f}'),
        ('high-confidence AI', f'{config.AI_THRESHOLD:.2f} - 1.00 (inclusive)'),
    ]
