"""Fast deterministic endpoint and math tests — no GPU or download needed.

Real GPT-2 signals are intentionally mocked only in HTTP route tests.
A passing test does NOT assert detector accuracy.
"""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import config
import scoring
import stylometry


class MathTests(unittest.TestCase):
    def test_three_reachable_labels(self):
        self.assertEqual(scoring.score_to_label(0.15)[0], 'human')
        self.assertEqual(scoring.score_to_label(0.55)[0], 'unsure')
        self.assertEqual(scoring.score_to_label(0.96)[0], 'ai')

    def test_disagreement_cannot_accuse(self):
        value = scoring.combine_signals(1.0, 0.1)
        self.assertLess(value, config.AI_THRESHOLD)

    def test_score_is_not_constant(self):
        self.assertNotEqual(scoring.combine_signals(0.1, 0.1),
                            scoring.combine_signals(0.95, 0.95))

    def test_style_bounds_and_variation(self):
        examples = [
            'Tiny text',
            'I went to the corner and saw a pigeon sitting on an old red sign. '
            'After that, unexpectedly, I crossed the very busy street without watching the light. '
            'I waited at the station for a long time, but the bus did not come. '
            'I ended up walking home alone, completely drenched after the sudden storm.',
            'The process has several steps and a simple expected result. '
            'The process has several steps and a simple expected result. '
            'The process has several steps and a simple expected result. '
            'The process has several steps and a simple expected result. '
            'The process has several steps and a simple expected result.',
        ]
        scores = [stylometry.style_signal(t) for t in examples]
        self.assertTrue(all(0 <= s <= 1 for s in scores))
        self.assertGreater(len(set(scores)), 1)

    def test_empty_style_metrics(self):
        self.assertEqual(stylometry.type_token_ratio(''), 0.0)
        self.assertEqual(stylometry.punctuation_density(''), 0.0)


class EndPointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import app
        except ImportError as exc:
            raise unittest.SkipTest(f'Flask is not installed: {exc}')
        cls.application = app.app

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.log_path = Path(self.temp.name) / 'audit.jsonl'
        self.log_path_patch = patch.object(config, 'AUDIT_LOG', self.log_path)
        self.log_path_patch.start()
        self.client = self.application.test_client()

    def tearDown(self):
        self.log_path_patch.stop()
        self.temp.cleanup()

    def test_bad_requests(self):
        self.assertEqual(self.client.post('/submit', json={'text': 'Hello'}).status_code, 400)
        self.assertEqual(self.client.post('/submit', json={'creator_id': 'u', 'text': ''}).status_code, 400)
        self.assertEqual(self.client.post('/appeal', json={'content_id': 'bad', 'reasoning': 'Mine'}).status_code, 404)

    def test_submission_appeal_and_immutable_decision(self):
        import audit
        content = 'I wrote about my day yesterday. It was a difficult trip on the bus. I finally arrived at work.'
        with patch('detector.model_signal', return_value=0.58):
            response = self.client.post('/submit', json={'text': content, 'creator_id': 'writer1'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        for key in ('content_id', 'guess', 'confidence', 'label', 'model_score', 'style_score'):
            self.assertIn(key, data)
        self.assertEqual(self.client.post('/appeal', json={
            'content_id': data['content_id'], 'reasoning': 'This is my original writing.'
        }).status_code, 200)
        events = audit.entries_for(data['content_id'])
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]['status'], 'decided')
        self.assertEqual(events[1]['status'], 'under_review')
        self.assertEqual(events[0]['model_score'], 0.58)
        self.assertEqual(self.client.get('/content/' + data['content_id']).get_json()['status'], 'under_review')


if __name__ == '__main__':
    unittest.main(verbosity=2)
