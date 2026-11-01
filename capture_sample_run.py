"""Run AFTER `python app.py` in another terminal; capture real service evidence.
No model values are mocked and the log entries are returned by the real server.
"""
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = 'http://127.0.0.1:5000'


def call(method, path, payload=None):
    raw = json.dumps(payload).encode('utf-8') if payload is not None else None
    req = Request(BASE + path, data=raw, method=method,
                  headers={'Content-Type': 'application/json'} if raw else {})
    try:
        with urlopen(req, timeout=180) as response:
            return response.status, json.loads(response.read().decode('utf-8'))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode('utf-8'))


def fmt(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


def main():
    sample = {
        'creator_id': 'writer-1',
        'text': ('Yesterday I missed the early train. The platform was wet and '
                 'I was carrying two heavy bags. I walked to work instead. '
                 'By the time I arrived, the sky had cleared, and I was laughing '
                 'about how much trouble I had made for myself.'),
    }
    try:
        status, body = call('POST', '/submit', sample)
    except URLError as exc:
        raise SystemExit(f'Start the service first with python app.py: {exc}') from exc
    if status != 200:
        raise SystemExit(f'Submission returned HTTP {status}: {fmt(body)}')

    appeal_body = {'content_id': body['content_id'],
                   'reasoning': 'I wrote this from my own firsthand experience.'}
    appeal_status, appeal_resp = call('POST', '/appeal', appeal_body)
    log_status, log_resp = call('GET', '/log?limit=10')
    status_code, item = call('GET', '/content/' + body['content_id'])
    lines = [
        '# Unit 7 Sample Run — real local HTTP evidence',
        '',
        'These values came from the locally running service, not a mock.',
        '',
        '## POST /submit',
        '',
        'Request:', '```json', fmt(sample), '```',
        f'Response — HTTP {status}:', '```json', fmt(body), '```',
        '## POST /appeal', 'Request:', '```json', fmt(appeal_body), '```',
        f'Response — HTTP {appeal_status}:', '```json', fmt(appeal_resp), '```',
        '## GET /log?limit=10', f'Response — HTTP {log_status}:',
        '```json', fmt(log_resp), '```',
        '## GET /content/<id>', f'Response — HTTP {status_code}:',
        '```json', fmt(item), '```',
    ]
    Path('SAMPLE_RUN.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('Wrote SAMPLE_RUN.md (real requests/responses)')
    print('Submit id:', body['content_id'])
    print('Appeal status:', appeal_resp.get('status'))


if __name__ == '__main__':
    main()
