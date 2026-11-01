"""Provenance Guard settings. Defaults only expose service on localhost."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', '5000'))
DEBUG = os.getenv('AI201_DEBUG', '0') == '1' and HOST in ('127.0.0.1', 'localhost')

# Keep model local. Do not replace GPT-2 output with an invented score.
DETECTOR_MODEL = os.getenv('AI201_DETECTOR_MODEL', 'gpt2')
DETECTOR_MAX_TOKENS = 400

# Unit 7: favor not falsely accusing a real writer.
WEIGHT_MODEL_SIGNAL = 0.60
WEIGHT_STYLE_SIGNAL = 0.40
HUMAN_THRESHOLD = 0.30
AI_THRESHOLD = 0.78
SIGNAL_DISAGREEMENT_LIMIT = 0.42

# Unit 8 functionality is deliberately off until the next unit.
RATE_LIMITING_ENABLED = os.getenv('AI201_RATE_LIMITS', '0') == '1'
RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200
RATE_LIMIT_STORAGE = 'memory://'

# Local persistence: the append-only audit records are a submission artifact.
LOG_DIR = ROOT / 'logs'
AUDIT_LOG = LOG_DIR / 'audit.jsonl'
RESULTS_DIR = ROOT / 'results'
MAX_TEXT_CHARS = 20000
MAX_CREATOR_CHARS = 100
MAX_REASONING_CHARS = 4000
