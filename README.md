
## Unit 8 — Provenance Guard Testing

### Rate Limiting

I implemented rate limiting using Flask-Limiter with a limit of 10 submissions per minute and 200 per day per creator.

My flood test sent 15 requests. The first 10 returned HTTP 200, while the final 5 returned HTTP 429. This confirmed that rate limiting works and rejected requests are recorded in the audit log.

### Attack Run — Before

I tested the system using all 56 instructor-provided attacks.

- Evasion: 9 of 10 avoided the AI label.
- False positives: All 8 human samples avoided an AI accusation.
- Prompt injection: All 6 returned valid responses, but response validity alone does not prove resistance.
- Malformed requests: All 20 were rejected with HTTP 400 or 413.
- Flood attacks: The final 2 requests returned HTTP 429.
- Server crashes: 0.

The biggest weakness was detecting modified AI-generated writing. Typos, unusual vocabulary, sentence changes, and human editing caused the model or style signal to produce lower AI-likeness scores.

Full results: `results/attack_run_2026-11-08_1502_before.md`

### Run Log and Verdicts

I evaluated all five acceptance criteria three times before and after the improvement.

| Criterion | Before | After | Verdict |
|---|---|---|---|
| C1: False positives | 0/10 AI flags | 0/10 AI flags | MET |
| C2: Score separation | +0.3330 | +0.3330 | MET |
| C3: Label coverage | 3/3 | 3/3 | MET |
| C4: Appeal handling | 5/5 | 5/5 | MET |
| C5: Invalid input | 5/5 | 5/5 | MET |

All five criteria passed in all three trials before and after.

The original acceptance targets were not changed.

### The Improvement

I changed `HUMAN_THRESHOLD` in `config.py` from 0.30 to 0.15.

This was based on EV05, where heavily edited AI-generated text was incorrectly classified as human.

Before the improvement, EV05 received a score of 0.233 and the label `human`.

After the improvement, its score remained 0.233, but its label became `unsure`.

PI02 also changed from `human` to `unsure`.

This reduced overconfident human classifications but did not increase the number of evasion attacks detected as AI.

### Attack Run — After

I reran the same 56 attacks after the threshold adjustment.

- All 56 attacks executed.
- EV05 and PI02 changed from human to unsure.
- Nine evasion attacks still avoided the AI label.
- All eight false-positive tests remained unsure.
- All 20 malformed requests were rejected.
- Rate limiting continued working.
- No server crashes occurred.

Full results: `results/attack_run_2026-11-08_1507_after.md`

### What's Still Broken

The detector still struggles with AI-generated text that has been edited to resemble human writing.

**Model signal:** Unusual vocabulary can increase perplexity and reduce the AI-likeness score.

**Style signal:** Changes to sentence length, punctuation, and vocabulary can manipulate the structural features.

**Label mapping:** Conservative thresholds protect human writers from false accusations but leave some AI-generated content undetected.

Future improvements should include larger evaluation datasets, improved signal calibration, multilingual testing, and more reliable identity-based rate limiting.

For production, I would prioritize avoiding false accusations and providing human review for uncertain decisions.

### Conclusion

Unit 8 demonstrated that Provenance Guard can handle malformed requests, enforce submission limits, record audit evidence, and preserve appeals.

All five acceptance criteria passed across three trials. However, the adversarial tests revealed significant weaknesses in identifying edited AI-generated writing.

The improvement reduced overconfident human labels, but overall AI detection did not improve.
