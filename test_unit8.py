"""Local Unit 8 tests: no model download, no HTTP server required.

Run after installing the Unit 8 baseline: python -m unittest -v test_unit8.py
"""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import config
import app as appmod
import detector
import stylometry

TEXT='This is a sufficiently long written text that should pass the minimum word-count validation check.'
FIELDS={'timestamp','content_id','creator_id','guess','model_score','style_score','combined_score','label','status'}

class Unit8Tests(unittest.TestCase):
    def test_rate_limiter_and_rejection_audit(self):
        self.assertTrue(config.RATE_LIMITING_ENABLED,'Enable rate limits in config.py and restart.')
        with tempfile.TemporaryDirectory() as t, \
             patch.object(config,'LOG_DIR',Path(t)), \
             patch.object(config,'AUDIT_LOG',Path(t)/'test_audit.jsonl'), \
             patch.object(detector,'model_signal',return_value=0.4), \
             patch.object(stylometry,'style_signal',return_value=0.5):
            c=appmod.app.test_client()
            statuses=[]
            for i in range(config.RATE_LIMIT_PER_MINUTE+1):
                response=c.post('/submit',json={'text':TEXT,'creator_id':'unit8_test_unique'})
                statuses.append(response.status_code)
            self.assertEqual(statuses[:-1],[200]*config.RATE_LIMIT_PER_MINUTE)
            self.assertEqual(statuses[-1],429)
            new_creator=c.post('/submit',json={'text':TEXT,'creator_id':'unit8_test_other'})
            self.assertEqual(new_creator.status_code,200,'Limiter should be keyed to creator, not shared IP')
            lines=Path(t,'test_audit.jsonl').read_text(encoding='utf-8').splitlines()
            import json
            entries=[json.loads(line) for line in lines]
            self.assertEqual(len(entries),config.RATE_LIMIT_PER_MINUTE+2)
            rejection=[x for x in entries if x.get('event')=='rejected']
            self.assertEqual(len(rejection),1)
            self.assertTrue(FIELDS.issubset(rejection[0]))
            self.assertEqual(rejection[0]['reason'],'rate_limited')
            self.assertIsNone(rejection[0]['content_id'])

    def test_acceptance_scenarios_well_formed(self):
        import scenarios
        self.assertEqual(len(scenarios.get_scenarios()),5)
        self.assertEqual(len(scenarios.INVALID_BODIES),5)
        self.assertEqual(len(scenarios.AI_TEXTS),5)

if __name__=='__main__':unittest.main()
