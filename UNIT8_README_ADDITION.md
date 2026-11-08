# Unit 8 — Provenance Guard, Part 2: Testing

> Generated from local result files, not from fabricated responses. Review before pasting into README.

## Rate Limiting

- **Limits:** 10 requests/minute and 200 requests/day per `creator_id`.
- **Why:** A legitimate writer can send several drafts without being blocked, while sustained repeated submissions from one creator account are throttled. This is per creator, not per IP; it cannot stop someone rotating accounts.
- **429 logging:** rate-limited requests are logged as `rejected` with the standard audit fields and a `rate_limited` reason.

### Recorded flood — exact status codes

# Rate limit check

- Produced by: `run_attacks.py::run_flood`
- 15 submissions as `flood_tester` · 2026-11-08 13:55
- Rate limited: **5**

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```


## Attack Run — Before

> **NOT YET RUN:** get the teaching fellow attack_set folder and run `python run_attacks.py --set .\attack_set --label before`.


### Audit evidence — at least 10 lines, including a rate-limited request

```json
[
  {
    "timestamp": "2026-11-08T18:55:17+00:00",
    "content_id": "ae249c18f4ba",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:17+00:00",
    "content_id": "8f6d835d56b5",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:17+00:00",
    "content_id": "a0a3f718e8bc",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": "266e563e8934",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": "dad630755f09",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": "3acc9f1017f6",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": "fcf477968335",
    "creator_id": "flood_tester",
    "guess": "unsure",
    "model_score": 0.2587,
    "style_score": 0.5,
    "combined_score": 0.3552,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": null,
    "creator_id": "flood_tester",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "10 per 1 minute"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": null,
    "creator_id": "flood_tester",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "10 per 1 minute"
  },
  {
    "timestamp": "2026-11-08T18:55:18+00:00",
    "content_id": null,
    "creator_id": "flood_tester",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "10 per 1 minute"
  }
]
```

Audit extract status: 10 entries included

## Run Log and Verdicts — Before

Not yet run.

> **NOT YET RUN:** run `python run_eval.py --label before`.


## Diagnoses

> **TO COMPLETE FROM REAL OUTPUT:** For every attack marked BROKE and each MISSED criterion, identify which stage failed (route, model signal, style signal, combining rule, or label mapping), plus the exact mechanism. A response alone does not establish a cause.

## The Improvement

> **NOT YET VERIFIED:** Choose one change after diagnosing the baseline. Example ONLY if false AI accusations dominate: raise `AI_THRESHOLD` from `0.78` to `0.85`, widening the unsure band. That protects some human writers at the cost of missed AI text. Do not state it helped unless the after-results support that claim.

### Attack Run — After

> **NOT YET RUN:** make exactly one improvement then rerun the full attack set with `--label after`.


### Run Log and Verdicts — After

Not yet run.

> **NOT YET RUN:** run `python run_eval.py --label after`.


## What's Still Broken

> **TO COMPLETE FROM AFTER RESULTS:** Identify remaining failed attacks and missed criteria, why you stopped, and who bears the consequences of the production tradeoff.
