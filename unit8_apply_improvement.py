#!/usr/bin/env python3
"""Optional ONE-FILE, ONE-SETTING improvement after evaluating Unit 8 baseline.

Only use if baseline diagnoses point to high-confidence AI false positives.
It widens the uncertainty region by changing AI_THRESHOLD from .78 to .85.
"""
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--apply',action='store_true',help='Actually change config.py')
    a=ap.parse_args()
    p=ROOT/'config.py'
    old='AI_THRESHOLD = 0.78'
    new='AI_THRESHOLD = 0.85'
    base_e=ROOT/'results'/'unit8_criteria_before.json'
    attack=sorted((ROOT/'results').glob('attack_run_*_before.md'))
    if not base_e.exists() or not attack:
        raise SystemExit('First run the real baseline: python run_eval.py --label before AND python run_attacks.py --set <folder> --label before')
    if not a.apply:
        print('PROPOSAL ONLY — no files changed. If false-positive diagnoses support it, run:')
        print('python unit8_apply_improvement.py --apply')
        print('This changes exactly ONE threshold 0.78 -> 0.85. It can miss more AI content.')
        return
    src=p.read_text(encoding='utf-8')
    if new in src and old not in src:
        print('Improvement already applied; no changes.')
        return
    if src.count(old)!=1:raise SystemExit('Expected 0.78 config threshold not found uniquely; nothing changed.')
    p.write_text(src.replace(old,new,1),encoding='utf-8')
    print('Applied one change: AI_THRESHOLD 0.78 -> 0.85')
    print('Now re-run the full attack set and 3-trial evaluation. Report both wins AND losses.')

if __name__=='__main__':main()
