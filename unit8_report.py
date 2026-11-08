#!/usr/bin/env python3
"""Build a truthful Unit 8 README section from evidence collected on YOUR PC.

Does not invent missing results, classify unclear attacks, or claim an improvement.
Writes UNIT8_README_ADDITION.md; paste into README after reviewing.
"""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent
RESULTS=ROOT/'results'


def latest(pattern):
    options=sorted(RESULTS.glob(pattern)) if RESULTS.exists() else []
    return options[-1] if options else None


def body(path,missing):
    if path is None:return f'> **NOT YET RUN:** {missing}.\n'
    return path.read_text(encoding='utf-8')


def summary(label):
    path=RESULTS/f'unit8_criteria_{label}.json'
    if not path.exists(): return 'Not yet run.'
    x=json.loads(path.read_text(encoding='utf-8'))
    s=[]
    for i in range(1,6):
        trials=x['results'].get(str(i),[])
        result='MET' if len(trials)==3 and all(t.get('met') for t in trials) else 'MISSED'
        s.append(f"- Criterion {i}: **{result}** — "+'; '.join(t.get('value','n/a') for t in trials))
    return '\n'.join(s)


def main():
    before=latest('attack_run_*_before.md')
    after=latest('attack_run_*_after.md')
    flood=latest('flood_*.md')
    js=ROOT/'logs'/'audit.jsonl'
    if js.exists():
        entries=[]
        for line in js.read_text(encoding='utf-8').splitlines():
            try:entries.append(json.loads(line))
            except ValueError:pass
    else:entries=[]
    rejects=[e for e in entries if e.get('status')=='rejected']
    chosen=(rejects[-3:]+[e for e in entries if e.get('status')=='decided'][-7:])
    # Deduplicate selected records, retain original order within the final extract.
    chosen=sorted(chosen,key=lambda e:entries.index(e))
    actual_ten=len(chosen)==10
    lines=[
      '# Unit 8 — Provenance Guard, Part 2: Testing','',
      '> Generated from local result files, not from fabricated responses. Review before pasting into README.','',
      '## Rate Limiting','',
      '- **Limits:** 10 requests/minute and 200 requests/day per `creator_id`.','- **Why:** A legitimate writer can send several drafts without being blocked, while sustained repeated submissions from one creator account are throttled. This is per creator, not per IP; it cannot stop someone rotating accounts.','- **429 logging:** rate-limited requests are logged as `rejected` with the standard audit fields and a `rate_limited` reason.','',
      '### Recorded flood — exact status codes','', body(flood,'run `python run_attacks.py --flood 15`'),'',
      '## Attack Run — Before','', body(before,'get the teaching fellow attack_set folder and run `python run_attacks.py --set .\\attack_set --label before`'),'',
      '### Audit evidence — at least 10 lines, including a rate-limited request','',
      '```json',json.dumps(chosen,indent=2,ensure_ascii=False),'```','',
      'Audit extract status: '+('10 entries included' if actual_ten else f'Only {len(chosen)} suitable entries found; gather 10, including a 429.'),'',
      '## Run Log and Verdicts — Before','',summary('before'),'',
      body((RESULTS/'unit8_criteria_before.md') if (RESULTS/'unit8_criteria_before.md').exists() else None,'run `python run_eval.py --label before`'),'',
      '## Diagnoses','',
      '> **TO COMPLETE FROM REAL OUTPUT:** For every attack marked BROKE and each MISSED criterion, identify which stage failed (route, model signal, style signal, combining rule, or label mapping), plus the exact mechanism. A response alone does not establish a cause.','',
      '## The Improvement','',
      '> **NOT YET VERIFIED:** Choose one change after diagnosing the baseline. Example ONLY if false AI accusations dominate: raise `AI_THRESHOLD` from `0.78` to `0.85`, widening the unsure band. That protects some human writers at the cost of missed AI text. Do not state it helped unless the after-results support that claim.','',
      '### Attack Run — After','',body(after,'make exactly one improvement then rerun the full attack set with `--label after`'),'',
      '### Run Log and Verdicts — After','',summary('after'),'',
      body((RESULTS/'unit8_criteria_after.md') if (RESULTS/'unit8_criteria_after.md').exists() else None,'run `python run_eval.py --label after`'),'',
      '## What\'s Still Broken','',
      '> **TO COMPLETE FROM AFTER RESULTS:** Identify remaining failed attacks and missed criteria, why you stopped, and who bears the consequences of the production tradeoff.','',
    ]
    output=ROOT/'UNIT8_README_ADDITION.md'
    output.write_text('\n'.join(lines),encoding='utf-8')
    print(f'Wrote {output.name}. DO NOT claim completion until all results and diagnoses are genuine.')
    print('Copy the finished Unit 8 sections into README.md and commit it.')

if __name__=='__main__':main()
