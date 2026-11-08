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
