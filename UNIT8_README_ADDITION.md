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

# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 15:02
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `92fa1f56c372` | unsure | 0.303 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `46d4e227c651` | unsure | 0.418 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cd41998e923d` | unsure | 0.514 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `35b6c15f8eaa` | unsure | 0.562 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `a0417f748b85` | human | 0.233 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0c9553ddd152` | unsure | 0.412 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `f94b3d5c2aac` | unsure | 0.552 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `ef570a73fa11` | unsure | 0.347 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b71bc70cd751` | unsure | 0.527 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c9af3ca77b5d` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6a4865fac77f` | unsure | 0.508 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a6d41a2ad8a1` | unsure | 0.679 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `98348c9d551f` | unsure | 0.683 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `9907a8e962f3` | unsure | 0.684 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `5076d71cb552` | unsure | 0.740 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f91a880423fe` | unsure | 0.675 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `3eb1b42249fe` | unsure | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `dbf80138424c` | unsure | 0.393 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `db7c6b85e9f2` | unsure | 0.357 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `058a6b6d10e3` | human | 0.181 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `6e700e2c1a4b` | unsure | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `231bcf707b23` | unsure | 0.455 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `0f43a399b5a1` | unsure | 0.584 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `dff5463113cb` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `661be74defbd` | human | 0.217 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a011cd2724bb` | human | 0.217 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `16fc2f937912` | human | 0.217 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dc1b6c90101` | human | 0.217 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `010956d164ce` | human | 0.217 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ec1f168a0ae8` | human | 0.217 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bb383d235fd6` | human | 0.217 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a16f32470f91` | human | 0.217 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `38cde96aa269` | human | 0.217 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `db4d512a81f2` | human | 0.217 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "92fa1f56c372",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3034,
  "model_score": 0.1635,
  "style_score": 0.5132,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "46d4e227c651",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4185,
  "model_score": 0.5943,
  "style_score": 0.1547,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "cd41998e923d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5136,
  "model_score": 0.6662,
  "style_score": 0.2848,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "35b6c15f8eaa",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5622,
  "model_score": 0.6114,
  "style_score": 0.4883,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "a0417f748b85",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2325,
  "model_score": 0.3212,
  "style_score": 0.0995,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "0c9553ddd152",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4116,
  "model_score": 0.5727,
  "style_score": 0.1699,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "f94b3d5c2aac",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5517,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "ef570a73fa11",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3471,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b71bc70cd751",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5267,
  "model_score": 0.7042,
  "style_score": 0.2605,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c9af3ca77b5d",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8605,
  "model_score": 0.9792,
  "style_score": 0.6824,
  "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6a4865fac77f",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5081,
  "model_score": 0.6175,
  "style_score": 0.3441,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a6d41a2ad8a1",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6793,
  "model_score": 0.7387,
  "style_score": 0.5903,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "98348c9d551f",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6831,
  "model_score": 0.8051,
  "style_score": 0.5002,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "9907a8e962f3",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6842,
  "model_score": 0.8329,
  "style_score": 0.4612,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "5076d71cb552",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7396,
  "model_score": 0.8005,
  "style_score": 0.6483,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "f91a880423fe",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6746,
  "model_score": 0.8814,
  "style_score": 0.3643,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "3eb1b42249fe",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6976,
  "model_score": 0.8816,
  "style_score": 0.4215,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "dbf80138424c",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3934,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "db7c6b85e9f2",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3575,
  "model_score": 0.4625,
  "style_score": 0.2,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "058a6b6d10e3",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1806,
  "model_score": 0.2044,
  "style_score": 0.145,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "6e700e2c1a4b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5279,
  "model_score": 0.5943,
  "style_score": 0.4282,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "231bcf707b23",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4551,
  "model_score": 0.4998,
  "style_score": 0.3881,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "0f43a399b5a1",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5841,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "dff5463113cb",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4815,
  "model_score": 0.5583,
  "style_score": 0.3664,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "661be74defbd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "a011cd2724bb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "16fc2f937912",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "6dc1b6c90101",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "010956d164ce",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "ec1f168a0ae8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "bb383d235fd6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "a16f32470f91",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "38cde96aa269",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "db4d512a81f2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```


### Audit evidence — at least 10 lines, including a rate-limited request

```json
[
  {
    "timestamp": "2026-11-08T20:08:07+00:00",
    "content_id": "f9c89d9fde9a",
    "creator_id": "eval8_separation_ai_68b9e2f6_4",
    "guess": "unsure",
    "model_score": 0.5821,
    "style_score": 0.5724,
    "combined_score": 0.5782,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:07+00:00",
    "content_id": "7173355e04ef",
    "creator_id": "eval8_separation_ai_68b9e2f6_5",
    "guess": "unsure",
    "model_score": 0.6794,
    "style_score": 0.4073,
    "combined_score": 0.5706,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:08+00:00",
    "content_id": "48cdaf2934fc",
    "creator_id": "eval8_appeal_68b9e2f6_1",
    "guess": "unsure",
    "model_score": 0.0482,
    "style_score": 0.5,
    "combined_score": 0.2289,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:08+00:00",
    "content_id": "0d9eabb868a1",
    "creator_id": "eval8_appeal_68b9e2f6_2",
    "guess": "unsure",
    "model_score": 0.0193,
    "style_score": 0.5,
    "combined_score": 0.2116,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:08+00:00",
    "content_id": "1231ec298bdd",
    "creator_id": "eval8_appeal_68b9e2f6_3",
    "guess": "unsure",
    "model_score": 0.0196,
    "style_score": 0.5,
    "combined_score": 0.2118,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:08+00:00",
    "content_id": "5c05f11120f3",
    "creator_id": "eval8_appeal_68b9e2f6_4",
    "guess": "unsure",
    "model_score": 0.0139,
    "style_score": 0.5,
    "combined_score": 0.2083,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:08+00:00",
    "content_id": "b42e767ab72e",
    "creator_id": "eval8_appeal_68b9e2f6_5",
    "guess": "unsure",
    "model_score": 0.0615,
    "style_score": 0.5,
    "combined_score": 0.2369,
    "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T20:08:09+00:00",
    "content_id": null,
    "creator_id": "eval8_invalid_68b9e2f6_3",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "invalid_text"
  },
  {
    "timestamp": "2026-11-08T20:08:09+00:00",
    "content_id": null,
    "creator_id": "unknown",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "invalid_creator_id"
  },
  {
    "timestamp": "2026-11-08T20:08:09+00:00",
    "content_id": null,
    "creator_id": "eval8_invalid_68b9e2f6_5",
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "event": "rejected",
    "status": "rejected",
    "reason": "text_too_long"
  }
]
```

Audit extract status: 10 entries included

## Run Log and Verdicts — Before

- Criterion 1: **MET** — 0/10 AI flags; 0/10 AI flags; 0/10 AI flags
- Criterion 2: **MET** — AI median 0.5448 - human median 0.2118 = +0.3330; AI median 0.5448 - human median 0.2118 = +0.3330; AI median 0.5448 - human median 0.2118 = +0.3330
- Criterion 3: **MET** — 3/3 labels; 3/3 labels; 3/3 labels
- Criterion 4: **MET** — 5/5 preserved appeal flows; 5/5 preserved appeal flows; 5/5 preserved appeal flows
- Criterion 5: **MET** — 5/5 4xx; rejection audit: yes; 5/5 4xx; rejection audit: yes; 5/5 4xx; rejection audit: yes

# Unit 8 acceptance criteria — before

Actual runs produced by `run_eval.py`; all non-direct scores came from POST /submit.
Timestamp (UTC): 2026-11-08T19:31:23.861591+00:00

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human false positives | At most 1/10 human samples classified ai per trial | 0/10 AI flags | 0/10 AI flags | 0/10 AI flags | MET |
| 2. Score spread | AI median minus human median >= 0.12 per trial | AI median 0.5448 - human median 0.2118 = +0.3330 | AI median 0.5448 - human median 0.2118 = +0.3330 | AI median 0.5448 - human median 0.2118 = +0.3330 | MET |
| 3. Label coverage | Direct label checks at 0.15, 0.55, 0.95 yield human, unsure, ai (3/3) | 3/3 labels | 3/3 labels | 3/3 labels | MET |
| 4. Appeal auditability | 5/5 appeals become under_review, original verdict and scores unchanged | 5/5 preserved appeal flows | 5/5 preserved appeal flows | 5/5 preserved appeal flows | MET |
| 5. Invalid requests | 5/5 malformed requests return 4xx with no attribution decision | 5/5 4xx; rejection audit: yes | 5/5 4xx; rejection audit: yes | 5/5 4xx; rejection audit: yes | MET |

## Real responses / traces

The values below are observed, not predictions. All trials remain visible even if they are identical.

### 1. Human false positives

#### Trial 1: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "18bf1127b8f7",
        "creator_id": "eval8_human_70c54315_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "3cc358fefd40",
        "creator_id": "eval8_human_70c54315_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "f556b01ea67f",
        "creator_id": "eval8_human_70c54315_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "d39b9c3286ea",
        "creator_id": "eval8_human_70c54315_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "fa1567bf5f19",
        "creator_id": "eval8_human_70c54315_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "51a58ac2a45d",
        "creator_id": "eval8_human_70c54315_6",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "1701c719c749",
        "creator_id": "eval8_human_70c54315_7",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "55ea55fc2c00",
        "creator_id": "eval8_human_70c54315_8",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "e6f96a876785",
        "creator_id": "eval8_human_70c54315_9",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "b9681eef2180",
        "creator_id": "eval8_human_70c54315_10",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

#### Trial 2: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "33bff88bf494",
        "creator_id": "eval8_human_8176a098_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "c75184d3ec88",
        "creator_id": "eval8_human_8176a098_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "1e83e93b3c21",
        "creator_id": "eval8_human_8176a098_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "c420be56294d",
        "creator_id": "eval8_human_8176a098_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "1f8cb763e56a",
        "creator_id": "eval8_human_8176a098_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "dfb61cd64a4b",
        "creator_id": "eval8_human_8176a098_6",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "83c7d21bfe39",
        "creator_id": "eval8_human_8176a098_7",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "0f21a8b65da4",
        "creator_id": "eval8_human_8176a098_8",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "ba130d87e1fa",
        "creator_id": "eval8_human_8176a098_9",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "f9ef719bcaea",
        "creator_id": "eval8_human_8176a098_10",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

#### Trial 3: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "31a73467d628",
        "creator_id": "eval8_human_43d3d6a9_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "9507cb0f8341",
        "creator_id": "eval8_human_43d3d6a9_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "59716e26e373",
        "creator_id": "eval8_human_43d3d6a9_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "b1b2bfb2f7b4",
        "creator_id": "eval8_human_43d3d6a9_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "ab732e2dd1e5",
        "creator_id": "eval8_human_43d3d6a9_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "0ef5baaa38c4",
        "creator_id": "eval8_human_43d3d6a9_6",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "b8032245ce4d",
        "creator_id": "eval8_human_43d3d6a9_7",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "0b92df897039",
        "creator_id": "eval8_human_43d3d6a9_8",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "203b7328a95f",
        "creator_id": "eval8_human_43d3d6a9_9",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "6bb37cd6ad2e",
        "creator_id": "eval8_human_43d3d6a9_10",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

### 2. Score spread

#### Trial 1: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "5678134282bf",
          "creator_id": "eval8_separation_h_70c54315_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "2645cf5b1762",
          "creator_id": "eval8_separation_h_70c54315_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "c60a7cb3b9ee",
          "creator_id": "eval8_separation_h_70c54315_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "6b1c1428b298",
          "creator_id": "eval8_separation_h_70c54315_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "4a54eebb1d8e",
          "creator_id": "eval8_separation_h_70c54315_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "54a44d8674d3",
          "creator_id": "eval8_separation_ai_70c54315_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "571f072a2895",
          "creator_id": "eval8_separation_ai_70c54315_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "ea6da402bcef",
          "creator_id": "eval8_separation_ai_70c54315_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "586e6cc2305c",
          "creator_id": "eval8_separation_ai_70c54315_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "f5bfcc07fa7e",
          "creator_id": "eval8_separation_ai_70c54315_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

#### Trial 2: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "649e1dc7d183",
          "creator_id": "eval8_separation_h_8176a098_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "9c7414ecde4b",
          "creator_id": "eval8_separation_h_8176a098_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "ee5beba0831d",
          "creator_id": "eval8_separation_h_8176a098_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "df48efa7b540",
          "creator_id": "eval8_separation_h_8176a098_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "15670bf1e8fb",
          "creator_id": "eval8_separation_h_8176a098_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "9c0c192a5a99",
          "creator_id": "eval8_separation_ai_8176a098_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "3765b4abeafa",
          "creator_id": "eval8_separation_ai_8176a098_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "dc85cd8ba34d",
          "creator_id": "eval8_separation_ai_8176a098_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "750ceec3a428",
          "creator_id": "eval8_separation_ai_8176a098_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "36d203b0231b",
          "creator_id": "eval8_separation_ai_8176a098_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

#### Trial 3: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "c5ae67d66067",
          "creator_id": "eval8_separation_h_43d3d6a9_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "d77d71f93997",
          "creator_id": "eval8_separation_h_43d3d6a9_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "a054bad212bb",
          "creator_id": "eval8_separation_h_43d3d6a9_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "030e5d7dfe36",
          "creator_id": "eval8_separation_h_43d3d6a9_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "c8486a198d40",
          "creator_id": "eval8_separation_h_43d3d6a9_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "7699ab4d730d",
          "creator_id": "eval8_separation_ai_43d3d6a9_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "01611c8cfabf",
          "creator_id": "eval8_separation_ai_43d3d6a9_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "9111d9d4655d",
          "creator_id": "eval8_separation_ai_43d3d6a9_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "2907b232c03a",
          "creator_id": "eval8_separation_ai_43d3d6a9_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "7c15f10d1498",
          "creator_id": "eval8_separation_ai_43d3d6a9_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

### 3. Label coverage

#### Trial 1: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

#### Trial 2: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

#### Trial 3: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

### 4. Appeal auditability

#### Trial 1: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "e1d51b327bcd",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "e1d51b327bcd",
          "creator_id": "eval8_appeal_70c54315_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "e1d51b327bcd",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "e1d51b327bcd",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "e1d51b327bcd",
        "creator_id": "eval8_appeal_70c54315_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:31:56+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "e1d51b327bcd",
        "creator_id": "eval8_appeal_70c54315_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:31:56+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "89049e34cda2",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "89049e34cda2",
          "creator_id": "eval8_appeal_70c54315_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "89049e34cda2",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "89049e34cda2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "89049e34cda2",
        "creator_id": "eval8_appeal_70c54315_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:31:56+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "89049e34cda2",
        "creator_id": "eval8_appeal_70c54315_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:31:56+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "205fa4d664d9",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "205fa4d664d9",
          "creator_id": "eval8_appeal_70c54315_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "205fa4d664d9",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "205fa4d664d9",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "205fa4d664d9",
        "creator_id": "eval8_appeal_70c54315_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "205fa4d664d9",
        "creator_id": "eval8_appeal_70c54315_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "2f86fc99e456",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "2f86fc99e456",
          "creator_id": "eval8_appeal_70c54315_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "2f86fc99e456",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "2f86fc99e456",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "2f86fc99e456",
        "creator_id": "eval8_appeal_70c54315_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "2f86fc99e456",
        "creator_id": "eval8_appeal_70c54315_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "1c255369cdcb",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "1c255369cdcb",
          "creator_id": "eval8_appeal_70c54315_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "1c255369cdcb",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "1c255369cdcb",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "1c255369cdcb",
        "creator_id": "eval8_appeal_70c54315_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "1c255369cdcb",
        "creator_id": "eval8_appeal_70c54315_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:31:57+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

#### Trial 2: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "3df783491bbe",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "3df783491bbe",
          "creator_id": "eval8_appeal_8176a098_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "3df783491bbe",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "3df783491bbe",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "3df783491bbe",
        "creator_id": "eval8_appeal_8176a098_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:03+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "3df783491bbe",
        "creator_id": "eval8_appeal_8176a098_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:03+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "0e24189cedaf",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "0e24189cedaf",
          "creator_id": "eval8_appeal_8176a098_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "0e24189cedaf",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "0e24189cedaf",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "0e24189cedaf",
        "creator_id": "eval8_appeal_8176a098_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:03+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "0e24189cedaf",
        "creator_id": "eval8_appeal_8176a098_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:03+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "41ae21723650",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "41ae21723650",
          "creator_id": "eval8_appeal_8176a098_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "41ae21723650",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "41ae21723650",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "41ae21723650",
        "creator_id": "eval8_appeal_8176a098_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:04+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "41ae21723650",
        "creator_id": "eval8_appeal_8176a098_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:04+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "a10f4ce36c32",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "a10f4ce36c32",
          "creator_id": "eval8_appeal_8176a098_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "a10f4ce36c32",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "a10f4ce36c32",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "a10f4ce36c32",
        "creator_id": "eval8_appeal_8176a098_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:04+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "a10f4ce36c32",
        "creator_id": "eval8_appeal_8176a098_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:04+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "76bfc3413110",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "76bfc3413110",
          "creator_id": "eval8_appeal_8176a098_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "76bfc3413110",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "76bfc3413110",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "76bfc3413110",
        "creator_id": "eval8_appeal_8176a098_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:05+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "76bfc3413110",
        "creator_id": "eval8_appeal_8176a098_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:05+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

#### Trial 3: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "28762a38a315",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "28762a38a315",
          "creator_id": "eval8_appeal_43d3d6a9_1",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "28762a38a315",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "28762a38a315",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "28762a38a315",
        "creator_id": "eval8_appeal_43d3d6a9_1",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:10+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "28762a38a315",
        "creator_id": "eval8_appeal_43d3d6a9_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:10+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "3d95321d5b7f",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "3d95321d5b7f",
          "creator_id": "eval8_appeal_43d3d6a9_2",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "3d95321d5b7f",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "3d95321d5b7f",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "3d95321d5b7f",
        "creator_id": "eval8_appeal_43d3d6a9_2",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "3d95321d5b7f",
        "creator_id": "eval8_appeal_43d3d6a9_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "6c785ac9f034",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "6c785ac9f034",
          "creator_id": "eval8_appeal_43d3d6a9_3",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "6c785ac9f034",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "6c785ac9f034",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "6c785ac9f034",
        "creator_id": "eval8_appeal_43d3d6a9_3",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "6c785ac9f034",
        "creator_id": "eval8_appeal_43d3d6a9_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "3741a9a404a8",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "3741a9a404a8",
          "creator_id": "eval8_appeal_43d3d6a9_4",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "3741a9a404a8",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "3741a9a404a8",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "3741a9a404a8",
        "creator_id": "eval8_appeal_43d3d6a9_4",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "3741a9a404a8",
        "creator_id": "eval8_appeal_43d3d6a9_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "646f3fa21918",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "646f3fa21918",
          "creator_id": "eval8_appeal_43d3d6a9_5",
          "guess": "human",
          "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "646f3fa21918",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "646f3fa21918",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "646f3fa21918",
        "creator_id": "eval8_appeal_43d3d6a9_5",
        "guess": "human",
        "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "646f3fa21918",
        "creator_id": "eval8_appeal_43d3d6a9_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T19:32:11+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

### 5. Invalid requests

#### Trial 1: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_70c54315_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:31:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_70c54315_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:31:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_70c54315_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:31:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:31:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_70c54315_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:31:57+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

#### Trial 2: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_8176a098_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:05+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_8176a098_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:05+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_8176a098_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:05+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:05+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_8176a098_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:05+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

#### Trial 3: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_43d3d6a9_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:12+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_43d3d6a9_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:12+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_43d3d6a9_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:12+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:12+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_43d3d6a9_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T19:32:12+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

## Diagnoses (fill after examining misses)

For each MISSED criterion: name the **stage** (route, model signal, style signal, combining rule, label mapping) and the **mechanism**. Do not invent a cause.


## Diagnoses

> **TO COMPLETE FROM REAL OUTPUT:** For every attack marked BROKE and each MISSED criterion, identify which stage failed (route, model signal, style signal, combining rule, or label mapping), plus the exact mechanism. A response alone does not establish a cause.

## The Improvement

> **NOT YET VERIFIED:** Choose one change after diagnosing the baseline. Example ONLY if false AI accusations dominate: raise `AI_THRESHOLD` from `0.78` to `0.85`, widening the unsure band. That protects some human writers at the cost of missed AI text. Do not state it helped unless the after-results support that claim.

### Attack Run — After

# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 15:07
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `02bfd0c5aa50` | unsure | 0.303 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8d502e8b5b3d` | unsure | 0.418 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a7fac4f907b2` | unsure | 0.514 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `7defc5ec9e1a` | unsure | 0.562 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c3539b1dec8a` | unsure | 0.233 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b56f246fe2b8` | unsure | 0.412 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bbb70e444d60` | unsure | 0.552 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `9164f63c212c` | unsure | 0.347 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3abad838a3ea` | unsure | 0.527 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `654a3e6c1741` | ai | 0.861 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6423b46e0117` | unsure | 0.508 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `6faed18da2b1` | unsure | 0.679 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1513aed9ea82` | unsure | 0.683 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4ef586a604b7` | unsure | 0.684 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `cee6ad97bfbb` | unsure | 0.740 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `aeefe1ea9f3c` | unsure | 0.675 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6be785e6729f` | unsure | 0.698 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `07e67cbe3134` | unsure | 0.393 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f23b7f43e000` | unsure | 0.357 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d7edc9e4a9f3` | unsure | 0.181 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0b43852a9553` | unsure | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4a69db1bc7f0` | unsure | 0.455 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b4afd1e28c2f` | unsure | 0.584 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `091a9ca4fce2` | unsure | 0.481 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7b2ae439cbc9` | unsure | 0.217 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0d0dea9940d6` | unsure | 0.217 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `087605ed88f3` | unsure | 0.217 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ac2e6c73074b` | unsure | 0.217 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bd541cac4595` | unsure | 0.217 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4e9472da237e` | unsure | 0.217 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a31270baaa3d` | unsure | 0.217 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `149c58ed922b` | unsure | 0.217 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `775d97101659` | unsure | 0.217 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c66fc24a86c6` | unsure | 0.217 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "02bfd0c5aa50",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3034,
  "model_score": 0.1635,
  "style_score": 0.5132,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "8d502e8b5b3d",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4185,
  "model_score": 0.5943,
  "style_score": 0.1547,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "a7fac4f907b2",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5136,
  "model_score": 0.6662,
  "style_score": 0.2848,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "7defc5ec9e1a",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5622,
  "model_score": 0.6114,
  "style_score": 0.4883,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c3539b1dec8a",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.2325,
  "model_score": 0.3212,
  "style_score": 0.0995,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "b56f246fe2b8",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4116,
  "model_score": 0.5727,
  "style_score": 0.1699,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bbb70e444d60",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5517,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "9164f63c212c",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3471,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "3abad838a3ea",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5267,
  "model_score": 0.7042,
  "style_score": 0.2605,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "654a3e6c1741",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8605,
  "model_score": 0.9792,
  "style_score": 0.6824,
  "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6423b46e0117",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5081,
  "model_score": 0.6175,
  "style_score": 0.3441,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "6faed18da2b1",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6793,
  "model_score": 0.7387,
  "style_score": 0.5903,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "1513aed9ea82",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6831,
  "model_score": 0.8051,
  "style_score": 0.5002,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "4ef586a604b7",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6842,
  "model_score": 0.8329,
  "style_score": 0.4612,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "cee6ad97bfbb",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7396,
  "model_score": 0.8005,
  "style_score": 0.6483,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "aeefe1ea9f3c",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6746,
  "model_score": 0.8814,
  "style_score": 0.3643,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "6be785e6729f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6976,
  "model_score": 0.8816,
  "style_score": 0.4215,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "07e67cbe3134",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3934,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f23b7f43e000",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3575,
  "model_score": 0.4625,
  "style_score": 0.2,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d7edc9e4a9f3",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.1806,
  "model_score": 0.2044,
  "style_score": 0.145,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0b43852a9553",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5279,
  "model_score": 0.5943,
  "style_score": 0.4282,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4a69db1bc7f0",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4551,
  "model_score": 0.4998,
  "style_score": 0.3881,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "b4afd1e28c2f",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5841,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "091a9ca4fce2",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4815,
  "model_score": 0.5583,
  "style_score": 0.3664,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "7b2ae439cbc9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0d0dea9940d6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "087605ed88f3",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "ac2e6c73074b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "bd541cac4595",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "4e9472da237e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "a31270baaa3d",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "149c58ed922b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "775d97101659",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "c66fc24a86c6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```


### Run Log and Verdicts — After

- Criterion 1: **MET** — 0/10 AI flags; 0/10 AI flags; 0/10 AI flags
- Criterion 2: **MET** — AI median 0.5448 - human median 0.2118 = +0.3330; AI median 0.5448 - human median 0.2118 = +0.3330; AI median 0.5448 - human median 0.2118 = +0.3330
- Criterion 3: **MET** — 3/3 labels; 3/3 labels; 3/3 labels
- Criterion 4: **MET** — 5/5 preserved appeal flows; 5/5 preserved appeal flows; 5/5 preserved appeal flows
- Criterion 5: **MET** — 5/5 4xx; rejection audit: yes; 5/5 4xx; rejection audit: yes; 5/5 4xx; rejection audit: yes

# Unit 8 acceptance criteria — after

Actual runs produced by `run_eval.py`; all non-direct scores came from POST /submit.
Timestamp (UTC): 2026-11-08T20:07:52.608124+00:00

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human false positives | At most 1/10 human samples classified ai per trial | 0/10 AI flags | 0/10 AI flags | 0/10 AI flags | MET |
| 2. Score spread | AI median minus human median >= 0.12 per trial | AI median 0.5448 - human median 0.2118 = +0.3330 | AI median 0.5448 - human median 0.2118 = +0.3330 | AI median 0.5448 - human median 0.2118 = +0.3330 | MET |
| 3. Label coverage | Direct label checks at 0.15, 0.55, 0.95 yield human, unsure, ai (3/3) | 3/3 labels | 3/3 labels | 3/3 labels | MET |
| 4. Appeal auditability | 5/5 appeals become under_review, original verdict and scores unchanged | 5/5 preserved appeal flows | 5/5 preserved appeal flows | 5/5 preserved appeal flows | MET |
| 5. Invalid requests | 5/5 malformed requests return 4xx with no attribution decision | 5/5 4xx; rejection audit: yes | 5/5 4xx; rejection audit: yes | 5/5 4xx; rejection audit: yes | MET |

## Real responses / traces

The values below are observed, not predictions. All trials remain visible even if they are identical.

### 1. Human false positives

#### Trial 1: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "c43ab6063355",
        "creator_id": "eval8_human_5d2a6a5e_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "3d9b86ed9e57",
        "creator_id": "eval8_human_5d2a6a5e_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "47afd9dcd05f",
        "creator_id": "eval8_human_5d2a6a5e_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "63c3641602c1",
        "creator_id": "eval8_human_5d2a6a5e_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "86047ae0349b",
        "creator_id": "eval8_human_5d2a6a5e_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "27876a534569",
        "creator_id": "eval8_human_5d2a6a5e_6",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "ee5643de7cfa",
        "creator_id": "eval8_human_5d2a6a5e_7",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "5379397ffd30",
        "creator_id": "eval8_human_5d2a6a5e_8",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "bd7efe96444f",
        "creator_id": "eval8_human_5d2a6a5e_9",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "f1b78b061224",
        "creator_id": "eval8_human_5d2a6a5e_10",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

#### Trial 2: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "e70817d02b6e",
        "creator_id": "eval8_human_2f907821_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "728f2f8136ab",
        "creator_id": "eval8_human_2f907821_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "89751409fbbd",
        "creator_id": "eval8_human_2f907821_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "d0674a0b0465",
        "creator_id": "eval8_human_2f907821_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "1cda55649f94",
        "creator_id": "eval8_human_2f907821_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "5fd8a7f46f0b",
        "creator_id": "eval8_human_2f907821_6",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "8c224ad347d5",
        "creator_id": "eval8_human_2f907821_7",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "b0aecc6aa873",
        "creator_id": "eval8_human_2f907821_8",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "e359bab926ec",
        "creator_id": "eval8_human_2f907821_9",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "0be585592123",
        "creator_id": "eval8_human_2f907821_10",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

#### Trial 3: MET

Observation: 0/10 AI flags

```json
{
  "met": true,
  "value": "0/10 AI flags",
  "detail": [
    {
      "status": 200,
      "json": {
        "confidence": 0.2289,
        "content_id": "7849681d9d42",
        "creator_id": "eval8_human_68b9e2f6_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_1"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2116,
        "content_id": "6535eae4b94e",
        "creator_id": "eval8_human_68b9e2f6_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_2"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2118,
        "content_id": "a6b089e183db",
        "creator_id": "eval8_human_68b9e2f6_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_3"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2083,
        "content_id": "f6bdea8978a8",
        "creator_id": "eval8_human_68b9e2f6_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_4"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2369,
        "content_id": "01bd2a502ebc",
        "creator_id": "eval8_human_68b9e2f6_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_5"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2042,
        "content_id": "9e535a5ca91b",
        "creator_id": "eval8_human_68b9e2f6_6",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.007,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_6"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2067,
        "content_id": "7dec1a8adf40",
        "creator_id": "eval8_human_68b9e2f6_7",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0111,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_7"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2449,
        "content_id": "0ddba7dbbfe6",
        "creator_id": "eval8_human_68b9e2f6_8",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0749,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_8"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2043,
        "content_id": "7f88ba52f72f",
        "creator_id": "eval8_human_68b9e2f6_9",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0071,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_9"
    },
    {
      "status": 200,
      "json": {
        "confidence": 0.2008,
        "content_id": "98f9905f9257",
        "creator_id": "eval8_human_68b9e2f6_10",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0014,
        "status": "decided",
        "style_score": 0.5
      },
      "sample": "human_10"
    }
  ],
  "note": "A failed HTTP response also counts as a miss."
}
```

### 2. Score spread

#### Trial 1: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "841c2803aaee",
          "creator_id": "eval8_separation_h_5d2a6a5e_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "c58e740b15eb",
          "creator_id": "eval8_separation_h_5d2a6a5e_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "a7b755b5c0e6",
          "creator_id": "eval8_separation_h_5d2a6a5e_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "29364910d95d",
          "creator_id": "eval8_separation_h_5d2a6a5e_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "41bce72a7119",
          "creator_id": "eval8_separation_h_5d2a6a5e_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "79abc19acd2f",
          "creator_id": "eval8_separation_ai_5d2a6a5e_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "0b6f358da016",
          "creator_id": "eval8_separation_ai_5d2a6a5e_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "19cc033bd69b",
          "creator_id": "eval8_separation_ai_5d2a6a5e_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "206794856670",
          "creator_id": "eval8_separation_ai_5d2a6a5e_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "dde3e594af17",
          "creator_id": "eval8_separation_ai_5d2a6a5e_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

#### Trial 2: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "a422c1a5dd25",
          "creator_id": "eval8_separation_h_2f907821_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "35047b39e853",
          "creator_id": "eval8_separation_h_2f907821_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "b215e60761da",
          "creator_id": "eval8_separation_h_2f907821_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "0f4ed95259ff",
          "creator_id": "eval8_separation_h_2f907821_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "e09e5a07f200",
          "creator_id": "eval8_separation_h_2f907821_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "7e5ef3d82c8e",
          "creator_id": "eval8_separation_ai_2f907821_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "bb0d76a257c2",
          "creator_id": "eval8_separation_ai_2f907821_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "c21f6280fc7a",
          "creator_id": "eval8_separation_ai_2f907821_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "311bc41990c8",
          "creator_id": "eval8_separation_ai_2f907821_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "c0a34c229958",
          "creator_id": "eval8_separation_ai_2f907821_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

#### Trial 3: MET

Observation: AI median 0.5448 - human median 0.2118 = +0.3330

```json
{
  "met": true,
  "value": "AI median 0.5448 - human median 0.2118 = +0.3330",
  "gap": 0.333,
  "detail": {
    "human": [
      {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "0152a9d4990b",
          "creator_id": "eval8_separation_h_68b9e2f6_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "4c53e7619010",
          "creator_id": "eval8_separation_h_68b9e2f6_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "42f3250b8fe1",
          "creator_id": "eval8_separation_h_68b9e2f6_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "080c417fcb92",
          "creator_id": "eval8_separation_h_68b9e2f6_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "e0644dfeec7d",
          "creator_id": "eval8_separation_h_68b9e2f6_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        },
        "sample": "separation_h_5"
      }
    ],
    "ai": [
      {
        "status": 200,
        "json": {
          "confidence": 0.5023,
          "content_id": "8325527a4723",
          "creator_id": "eval8_separation_ai_68b9e2f6_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4905,
          "status": "decided",
          "style_score": 0.52
        },
        "sample": "separation_ai_1"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5448,
          "content_id": "a9e9b7072088",
          "creator_id": "eval8_separation_ai_68b9e2f6_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6312,
          "status": "decided",
          "style_score": 0.4151
        },
        "sample": "separation_ai_2"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.47,
          "content_id": "0017b303fb4c",
          "creator_id": "eval8_separation_ai_68b9e2f6_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.4814,
          "status": "decided",
          "style_score": 0.453
        },
        "sample": "separation_ai_3"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5782,
          "content_id": "f9c89d9fde9a",
          "creator_id": "eval8_separation_ai_68b9e2f6_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.5821,
          "status": "decided",
          "style_score": 0.5724
        },
        "sample": "separation_ai_4"
      },
      {
        "status": 200,
        "json": {
          "confidence": 0.5706,
          "content_id": "7173355e04ef",
          "creator_id": "eval8_separation_ai_68b9e2f6_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.6794,
          "status": "decided",
          "style_score": 0.4073
        },
        "sample": "separation_ai_5"
      }
    ]
  }
}
```

### 3. Label coverage

#### Trial 1: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

#### Trial 2: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

#### Trial 3: MET

Observation: 3/3 labels

```json
{
  "met": true,
  "value": "3/3 labels",
  "detail": [
    {
      "score": 0.15,
      "guess": "human",
      "label": "This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship."
    },
    {
      "score": 0.55,
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made."
    },
    {
      "score": 0.95,
      "guess": "ai",
      "label": "This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment."
    }
  ],
  "note": "Direct function checks measure label mapping, not model accuracy."
}
```

### 4. Appeal auditability

#### Trial 1: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "42bcd06fb143",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "42bcd06fb143",
          "creator_id": "eval8_appeal_5d2a6a5e_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "42bcd06fb143",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "42bcd06fb143",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "42bcd06fb143",
        "creator_id": "eval8_appeal_5d2a6a5e_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:07:56+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "42bcd06fb143",
        "creator_id": "eval8_appeal_5d2a6a5e_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:07:56+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "7acd6aa6d8aa",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "7acd6aa6d8aa",
          "creator_id": "eval8_appeal_5d2a6a5e_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "7acd6aa6d8aa",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "7acd6aa6d8aa",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "7acd6aa6d8aa",
        "creator_id": "eval8_appeal_5d2a6a5e_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "7acd6aa6d8aa",
        "creator_id": "eval8_appeal_5d2a6a5e_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "b24a0a4d2343",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "b24a0a4d2343",
          "creator_id": "eval8_appeal_5d2a6a5e_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "b24a0a4d2343",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "b24a0a4d2343",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "b24a0a4d2343",
        "creator_id": "eval8_appeal_5d2a6a5e_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "b24a0a4d2343",
        "creator_id": "eval8_appeal_5d2a6a5e_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "80f666b84fbd",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "80f666b84fbd",
          "creator_id": "eval8_appeal_5d2a6a5e_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "80f666b84fbd",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "80f666b84fbd",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "80f666b84fbd",
        "creator_id": "eval8_appeal_5d2a6a5e_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "80f666b84fbd",
        "creator_id": "eval8_appeal_5d2a6a5e_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "13869edeea99",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "13869edeea99",
          "creator_id": "eval8_appeal_5d2a6a5e_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "13869edeea99",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "13869edeea99",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "13869edeea99",
        "creator_id": "eval8_appeal_5d2a6a5e_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "13869edeea99",
        "creator_id": "eval8_appeal_5d2a6a5e_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:07:57+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

#### Trial 2: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "a69d17cfc33a",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "a69d17cfc33a",
          "creator_id": "eval8_appeal_2f907821_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "a69d17cfc33a",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "a69d17cfc33a",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "a69d17cfc33a",
        "creator_id": "eval8_appeal_2f907821_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:02+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "a69d17cfc33a",
        "creator_id": "eval8_appeal_2f907821_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:02+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "3b820f368375",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "3b820f368375",
          "creator_id": "eval8_appeal_2f907821_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "3b820f368375",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "3b820f368375",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "3b820f368375",
        "creator_id": "eval8_appeal_2f907821_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:02+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "3b820f368375",
        "creator_id": "eval8_appeal_2f907821_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:02+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "b78ed8510e54",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "b78ed8510e54",
          "creator_id": "eval8_appeal_2f907821_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "b78ed8510e54",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "b78ed8510e54",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "b78ed8510e54",
        "creator_id": "eval8_appeal_2f907821_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "b78ed8510e54",
        "creator_id": "eval8_appeal_2f907821_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "26c2a89902ee",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "26c2a89902ee",
          "creator_id": "eval8_appeal_2f907821_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "26c2a89902ee",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "26c2a89902ee",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "26c2a89902ee",
        "creator_id": "eval8_appeal_2f907821_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "26c2a89902ee",
        "creator_id": "eval8_appeal_2f907821_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "a99c83b5fc60",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "a99c83b5fc60",
          "creator_id": "eval8_appeal_2f907821_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "a99c83b5fc60",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "a99c83b5fc60",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "a99c83b5fc60",
        "creator_id": "eval8_appeal_2f907821_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "a99c83b5fc60",
        "creator_id": "eval8_appeal_2f907821_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:03+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

#### Trial 3: MET

Observation: 5/5 preserved appeal flows

```json
{
  "met": true,
  "value": "5/5 preserved appeal flows",
  "detail": [
    {
      "i": 1,
      "content_id": "48cdaf2934fc",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2289,
          "content_id": "48cdaf2934fc",
          "creator_id": "eval8_appeal_68b9e2f6_1",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0482,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "48cdaf2934fc",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2289,
        "content_id": "48cdaf2934fc",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2289,
        "content_id": "48cdaf2934fc",
        "creator_id": "eval8_appeal_68b9e2f6_1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0482,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "48cdaf2934fc",
        "creator_id": "eval8_appeal_68b9e2f6_1",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 2,
      "content_id": "0d9eabb868a1",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2116,
          "content_id": "0d9eabb868a1",
          "creator_id": "eval8_appeal_68b9e2f6_2",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0193,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "0d9eabb868a1",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2116,
        "content_id": "0d9eabb868a1",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2116,
        "content_id": "0d9eabb868a1",
        "creator_id": "eval8_appeal_68b9e2f6_2",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0193,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "0d9eabb868a1",
        "creator_id": "eval8_appeal_68b9e2f6_2",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 3,
      "content_id": "1231ec298bdd",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2118,
          "content_id": "1231ec298bdd",
          "creator_id": "eval8_appeal_68b9e2f6_3",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0196,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "1231ec298bdd",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2118,
        "content_id": "1231ec298bdd",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2118,
        "content_id": "1231ec298bdd",
        "creator_id": "eval8_appeal_68b9e2f6_3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0196,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "1231ec298bdd",
        "creator_id": "eval8_appeal_68b9e2f6_3",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 4,
      "content_id": "5c05f11120f3",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2083,
          "content_id": "5c05f11120f3",
          "creator_id": "eval8_appeal_68b9e2f6_4",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0139,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "5c05f11120f3",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2083,
        "content_id": "5c05f11120f3",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2083,
        "content_id": "5c05f11120f3",
        "creator_id": "eval8_appeal_68b9e2f6_4",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0139,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "5c05f11120f3",
        "creator_id": "eval8_appeal_68b9e2f6_4",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "original_fields_unchanged": true
    },
    {
      "i": 5,
      "content_id": "b42e767ab72e",
      "passed": true,
      "submit": {
        "status": 200,
        "json": {
          "confidence": 0.2369,
          "content_id": "b42e767ab72e",
          "creator_id": "eval8_appeal_68b9e2f6_5",
          "guess": "unsure",
          "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
          "model_score": 0.0615,
          "status": "decided",
          "style_score": 0.5
        }
      },
      "appeal": {
        "status": 200,
        "json": {
          "content_id": "b42e767ab72e",
          "message": "Your appeal has been recorded for human review.",
          "status": "under_review"
        }
      },
      "status_response": {
        "confidence": 0.2369,
        "content_id": "b42e767ab72e",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "under_review",
        "style_score": 0.5
      },
      "original_decision": {
        "combined_score": 0.2369,
        "content_id": "b42e767ab72e",
        "creator_id": "eval8_appeal_68b9e2f6_5",
        "guess": "unsure",
        "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
        "model_score": 0.0615,
        "status": "decided",
        "style_score": 0.5,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "appeal_event": {
        "combined_score": null,
        "content_id": "b42e767ab72e",
        "creator_id": "eval8_appeal_68b9e2f6_5",
        "event": "appeal",
        "guess": null,
        "label": null,
        "model_score": null,
        "reasoning": "I wrote this personally and I request a human review of the detection score.",
        "status": "under_review",
        "style_score": null,
        "timestamp": "2026-11-08T20:08:08+00:00"
      },
      "original_fields_unchanged": true
    }
  ]
}
```

### 5. Invalid requests

#### Trial 1: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_5d2a6a5e_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:07:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_5d2a6a5e_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:07:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_5d2a6a5e_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:07:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:07:57+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_5d2a6a5e_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:07:57+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

#### Trial 2: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_2f907821_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_2f907821_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_2f907821_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_2f907821_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:03+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

#### Trial 3: MET

Observation: 5/5 4xx; rejection audit: yes

```json
{
  "met": true,
  "value": "5/5 4xx; rejection audit: yes",
  "detail": [
    {
      "case": 1,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 2,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 3,
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "passed": true
    },
    {
      "case": 4,
      "status": 400,
      "response": {
        "error": "invalid_creator_id",
        "message": "creator_id must be nonempty text."
      },
      "passed": true
    },
    {
      "case": 5,
      "status": 413,
      "response": {
        "error": "text_too_long",
        "message": "text exceeds 20000 characters."
      },
      "passed": true
    }
  ],
  "audit_rejections": [
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_68b9e2f6_1",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:09+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_68b9e2f6_2",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:09+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_68b9e2f6_3",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_text",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:09+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "unknown",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "invalid_creator_id",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:09+00:00"
    },
    {
      "combined_score": null,
      "content_id": null,
      "creator_id": "eval8_invalid_68b9e2f6_5",
      "event": "rejected",
      "guess": null,
      "label": null,
      "model_score": null,
      "reason": "text_too_long",
      "status": "rejected",
      "style_score": null,
      "timestamp": "2026-11-08T20:08:09+00:00"
    }
  ],
  "note": "Last five log entries should be rejections; run with no concurrent writers."
}
```

## Diagnoses (fill after examining misses)

For each MISSED criterion: name the **stage** (route, model signal, style signal, combining rule, label mapping) and the **mechanism**. Do not invent a cause.


## What's Still Broken

> **TO COMPLETE FROM AFTER RESULTS:** Identify remaining failed attacks and missed criteria, why you stopped, and who bears the consequences of the production tradeoff.
