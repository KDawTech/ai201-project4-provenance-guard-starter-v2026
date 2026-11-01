
# Provenance Guard

**CodePath AI201 — Project 4, Unit 7**  
**Repository:** https://github.com/KDawTech/ai201-project4-provenance-guard-starter-v2026

Provenance Guard is a local Flask API that helps a writing platform determine whether text resembles human or AI-generated writing. It combines two imperfect detection signals and communicates uncertainty instead of claiming to prove authorship.

Writers can challenge a decision through an appeal endpoint. An append-only audit log preserves both the original judgment and the appeal.

> **Important:** An AI-likeness score is not proof that AI authored a text. Automated labels should never be the sole basis for penalizing a writer.

**Getting started:** See [RUNNING.md](RUNNING.md). The application runs locally at `http://127.0.0.1:5000` and requires no API key.

---

## What This Does

A submission passes through seven steps:

1. A writer sends JSON containing `text` and `creator_id` to `POST /submit`.
2. `app.py` validates the submitted information and rejects invalid, missing, or excessively long input.
3. `detector.py::model_signal` uses a local GPT-2 model to measure text predictability through perplexity.
4. `stylometry.py::style_signal` examines sentence length variation, vocabulary diversity, and punctuation patterns.
5. `scoring.py::combine_signals` combines both scores into a 0–1 AI-likeness score.
6. `scoring.py::score_to_label` assigns `human`, `unsure`, or `ai`. The application generates a `content_id`, records the decision, and returns JSON containing both signal scores.
7. If the writer disagrees, `POST /appeal` records their reasoning and marks the submission as `under_review` without deleting the original decision.

Additional endpoints include:

| Endpoint | Method | Purpose |
|---|---|---|
| `/ping` | POST | Check whether the API responds |
| `/submit` | POST | Analyze submitted text |
| `/appeal` | POST | Request a review |
| `/log` | GET | View audit records |
| `/health` | GET | Check service status |
| `/content/<content_id>` | GET | Check a particular submission's status |

Invalid requests receive descriptive HTTP errors rather than fabricated model scores.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:**

The first signal uses GPT-2 to measure how predictable the submitted text is.

This measurement is called *perplexity*. Lower perplexity means the language model finds the writing easier to predict.

The result is transformed into a score between 0 and 1, where higher values indicate stronger AI-like characteristics.

**Why that might differ between human and AI writing:**

AI-generated writing sometimes uses common word sequences, predictable sentence structures, and familiar phrasing. Human writing may include more unexpected choices.

**What it can't see:**

Predictability does not prove authorship. A person writing in plain language or using a second language may produce highly predictable text. AI-generated writing may also contain unusual or unpredictable wording.

This creates a risk of false accusations against legitimate writers.

### Signal two — the style signal

**What it measures:**

The second signal analyzes writing style without interpreting the meaning of the text.

It examines three measurements:

| Measurement | Description |
|---|---|
| Sentence length spread | Measures variation in sentence lengths |
| Type-token ratio | Measures vocabulary diversity by comparing unique words with total words |
| Punctuation density | Measures the frequency of punctuation such as commas, semicolons, and dashes |

The style score is calculated using:

- 50% sentence regularity
- 30% vocabulary repetition
- 20% punctuation patterns

Short submissions with insufficient stylistic evidence receive a neutral style score of `0.50`.

**Why that might differ between human and AI writing:**

Human writing can contain irregular sentence lengths, varied vocabulary, and less predictable punctuation.

Some AI-generated writing is more consistent and structured.

**What it can't see:**

Writing style does not reveal who wrote something.

A human can write consistently, while AI can imitate irregular writing. Adding typos, changing punctuation, or rewriting sentences may also affect the score without changing the actual author.

### The combining rule

**The rule:**

The detector combines both measurements through a weighted average.

The model signal contributes 60%, while the style signal contributes 40%.

```python
combined_score = (
    0.60 * model_score
    + 0.40 * style_score
)
```

If the signals disagree substantially, the scoring system limits the combined result to avoid making an unsupported high-confidence AI accusation.

```python
if abs(model_score - style_score) >= 0.42:
    combined_score = min(combined_score, 0.77)
```

**The numbers:**

| Signal | Weight |
|---|---|
| Model signal | 60% |
| Style signal | 40% |

**Where it lives:** `scoring.py::combine_signals`

The weights and label thresholds are configured in `config.py`.

**A case where my two signals split, and what my rule does with it:**

During my real local test:

```text
model_score = 0.8117
style_score = 0.5000
```

The two signals differed by `0.3117`.

The weighted score was:

```text
(0.60 × 0.8117) + (0.40 × 0.50)

= 0.68702

≈ 0.687
```

The final decision was `unsure`.

The model considered the sample relatively predictable, but the style signal was neutral because the submitted text was short.

Rather than declaring AI authorship based on one strong signal, the system communicated uncertainty.

**Trade-off:**

Conservative thresholds reduce the chance of falsely accusing human writers. However, they may also allow more AI-generated writing to go unflagged.

I prioritize protecting legitimate writers over producing an aggressive but unreliable detection result.

---

## Label Variants

The system supports three reader-facing labels.

| Label | Score range | Exact text shown to the reader |
|---|---|---|
| High-confidence human | 0.00–0.30 | This writing appears likely to be human-written based on limited automated signals. This is not proof of authorship. |
| Unsure | Above 0.30 and below 0.78 | We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made. |
| High-confidence AI | 0.78–1.00 | This writing shows signals sometimes associated with AI-generated text. Automated judgments can be wrong. The writer can appeal this assessment. |

**Why I worded the "unsure" one this way:**

The system should not make writers feel accused when the evidence is inconclusive.

The unsure label clearly explains that the detector cannot reliably determine authorship.

It avoids implying wrongdoing and acknowledges that the person may have written the entire submission themselves.

All three labels have defined score ranges. Further real-world testing is necessary to determine how reliably different texts reach each label.

---

## Sample Run

The following results were recorded from my local Provenance Guard service on **November 1, 2026**.

The Python environment check returned:

```text
9 passed, 0 failed, 0 to look at, 0 skipped
```

The Flask server returned HTTP 200 for the submission, appeal, and audit-log requests.

### A submission

**Request:**

```http
POST http://127.0.0.1:5000/submit
Content-Type: application/json
```

```json
{
  "text": "The morning was beautiful. I walked through the park and enjoyed the fresh air. It was a peaceful and wonderful day.",
  "creator_id": "kevontest"
}
```

**Actual response — HTTP 200:**

```json
{
  "confidence": 0.687,
  "content_id": "af9a86e74084",
  "creator_id": "kevontest",
  "guess": "unsure",
  "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
  "model_score": 0.8117,
  "status": "decided",
  "style_score": 0.5
}
```

**Interpretation:**

The detector returned an AI-likeness score of `0.687`, but did not classify the text as high-confidence AI.

The result was `unsure`, showing the system's ability to communicate uncertainty.

### An appeal

**Request:**

```http
POST http://127.0.0.1:5000/appeal
Content-Type: application/json
```

```json
{
  "content_id": "af9a86e74084",
  "reasoning": "I wrote this text myself and request a review."
}
```

The server returned HTTP 200, confirming the request was processed successfully.

The audit log verified that the appeal had been recorded with the status:

```text
under_review
```

### What the log shows afterwards

**Actual audit-log response:**

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.687,
      "content_id": "af9a86e74084",
      "creator_id": "kevontest",
      "guess": "unsure",
      "label": "We cannot reliably determine who wrote this text from the available signals. No claim of AI authorship is being made.",
      "model_score": 0.8117,
      "status": "decided",
      "style_score": 0.5,
      "timestamp": "2026-11-01T21:21:11+00:00"
    },
    {
      "content_id": "af9a86e74084",
      "creator_id": "kevontest",
      "event": "appeal",
      "reasoning": "I wrote this text myself and request a review.",
      "status": "under_review",
      "timestamp": "2026-11-01T21:22:24+00:00"
    }
  ]
}
```

**What this demonstrates:**

The original decision remains in the audit history with the status `decided`.

The appeal creates a separate record with the status `under_review`.

The system does not overwrite the original decision, making its actions traceable and accountable.

Additional local testing successfully returned HTTP 200 for:

```text
POST /submit
POST /appeal
GET /log?limit=10
GET /content/04a7dd6b6119
```

---

## How I Used AI

### Moment 1 — Building the application

**What I asked for:**

I used ChatGPT to help implement the CodePath AI201 Unit 7 Provenance Guard assignment using the official Flask starter project.

**What came back:**

ChatGPT provided implementation suggestions for input validation, combining model and writing-style signals, defining labels, processing appeals, and documenting the application.

**What I changed or checked:**

I installed the application code in my project and tested the local API.

Initially, `/submit` returned a `not_implemented` error because the starter implementation was still active.

After installing the implementation and restarting Flask, I submitted real text and confirmed that the service returned a content ID, model score, style score, and label.

### Moment 2 — Fixing Python and verifying the API

**What I asked for:**

I asked ChatGPT to help resolve Python installation issues, PowerShell execution-policy errors, and problems running my local development environment.

**What came back:**

ChatGPT provided commands for activating my Python virtual environment, checking dependencies, running the Flask application, and testing endpoints.

**What I changed or checked:**

I successfully activated Python 3.11.9 and ran the project's environment check.

The results were:

```text
9 passed
0 failed
0 warnings
0 skipped
```

I then tested `/submit`, `/appeal`, and `/log`.

I verified that the original decision was preserved and the appeal was recorded separately.

**AI assistance disclosure:**

AI assisted with the implementation suggestions and README wording. The final service behavior was checked using real requests to the local Flask application.

The environment check verifies setup and dependencies; it does not measure the accuracy of the AI detector.

---

## Running the Project

### Requirements

- Python 3.11–3.13
- Flask
- PyTorch
- Hugging Face Transformers
- Local GPT-2 model
- Approximately 550 MB for the downloaded model

No external API key is required.

### Installation

Clone the repository:

```powershell
git clone https://github.com/KDawTech/ai201-project4-provenance-guard-starter-v2026.git
cd ai201-project4-provenance-guard-starter-v2026
```

Create and activate the virtual environment:

```powershell
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Check the environment:

```powershell
python test.py
```

Download or load the detector:

```powershell
python detector.py
```

Start the server:

```powershell
python app.py
```

The service runs at:

```text
http://127.0.0.1:5000
```

### Testing the API

In a second PowerShell terminal:

```powershell
$body = @{
    text = "The morning was beautiful. I walked through the park and enjoyed the fresh air. It was a peaceful and wonderful day."
    creator_id = "kevontest"
} | ConvertTo-Json

$result = Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/submit" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body

$result
```

Test the appeal system:

```powershell
$appeal = @{
    content_id = $result.content_id
    reasoning = "I wrote this text myself and request a review."
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/appeal" `
    -Method Post `
    -ContentType "application/json" `
    -Body $appeal
```

View the audit log:

```powershell
Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/log" |
    ConvertTo-Json -Depth 10
```

### Limitations

This is an educational prototype, not a production-ready authorship verification system.

- No automated detector can reliably prove authorship.
- Human writing may be incorrectly identified as AI-like.
- Generated text may be classified as human-like.
- Short writing samples provide limited stylistic evidence.
- The appeal endpoint records disputes but does not automatically resolve them.
- The local API does not provide user authentication.
- Rate limiting is reserved for Unit 8.

The application should not be used to automatically punish or penalize writers.

---

## Unit 8 — Future Work

Unit 8 builds on this same repository.

### Rate Limiting

Not yet enabled or evaluated for Unit 8.

### Attack Run — Before

The full adversarial attack suite has not yet been completed for Unit 8.

### Run Log and Verdicts

The five acceptance criteria must be evaluated across three separate trials.

### The Improvement

A measurable improvement will be selected after analyzing the Unit 8 attack results.

### What's Still Broken

Remaining weaknesses and trade-offs will be documented after the adversarial evaluation and improvement.

---

## Conclusion

Provenance Guard demonstrates how a local AI-assisted detection service can combine language-model predictability with structural writing characteristics.

The system supports a complete workflow:

**Submit → Validate → Analyze → Combine Scores → Label → Audit → Appeal**

The most important design principle is that an automated detection score should not be treated as definitive proof of authorship.

By returning uncertainty-aware labels and allowing appeals, the project emphasizes transparency, accountability, and fairness.

---

**GitHub Repository:** https://github.com/KDawTech/ai201-project4-provenance-guard-starter-v2026

**Setup Instructions:** [RUNNING.md](RUNNING.md)
