# CodePath AI201 — Unit 8 Provenance Guard Testing

**Use the same repository as Unit 7. Do not fork a new repository.**

The assignment deadline in the uploaded PDF is **Monday, Nov 9, 2026 at 2:59 AM EST**.

## 0. Before anything

From the VS Code project folder, with `(.venv)`:

```powershell
git status --short
git pull origin main
python test.py
```

If `git pull` reports conflicting local changes, **do not reset or delete anything**. Commit your local work or resolve the conflict before continuing.

## 1. Install the Unit 8 baseline

Unzip the pack downloaded from ChatGPT. From inside the existing repository:

```powershell
python "$HOME\Downloads\ProvenanceGuard_Unit8_Patch\unit8_install.py" --repo .
python -m unittest -v test_unit8.py
```

The installer does not delete `logs/audit.jsonl`, results, README or `criteria.md`. It switches rate limiting **on** by default, per creator ID: 10/minute and 200/day. Existing `run_eval.py` and `scenarios.py` are backed up to `*.unit7-backup`.

Make **two separate commits before running your baseline**:

```powershell
git add app.py audit.py config.py test_unit8.py
git commit -m "Unit 8: enable per-creator rate limits and log rejections"
git add scenarios.py run_eval.py unit8_*.py UNIT8_START_HERE.md
git commit -m "Unit 8: implement five-criterion three-trial evaluator"
```

## 2. First start Flask, then flood test

Terminal A:

```powershell
python app.py
```

Leave it running. In terminal B (with the virtual environment):

```powershell
Invoke-RestMethod http://127.0.0.1:5000/health
python run_attacks.py --flood 15
```

You should see `200` followed by `429`. The actual status list is saved to `results/flood_<date>.md` and rejected requests are logged.

## 3. Get staff attack-set files from teaching fellow

Unit 8's rubric requires a specific ZIP supplied **by the teaching fellow**. It is not included in this patch; fabricating an attack set is not the same assignment.

Unzip `attack_set.zip` in the project root such that this path exists:

```text
attack_set/attacks.csv
attack_set/attacks_malformed_requests.csv
```

Then run **the complete set** (no `--family` filtering):

```powershell
python run_attacks.py --set .\attack_set --label before
```

Review the resulting `results/attack_run_*_before.md`. Mark each row as **HELD** or **BROKE** using the stated attack goal; the runner only labels outright crashes automatically. Keep the **original raw report** as well if you want a trace of the initial blank verdicts.

## 4. Supply your own 10 human writing samples

Criterion 1 is expressly about **your** writing. Neither the AI nor this patch can honestly manufacture that evidence. Run:

```powershell
python unit8_add_human.py
```

Paste 10 short but genuinely user-authored excerpts (8+ words each). Your progress is saved in `data/unit8_human_samples.json`. Do not use AI-generated examples as human reference texts.

Run your five criteria across three trials (actual API requests):

```powershell
python run_eval.py --label before
```

This writes `results/unit8_criteria_before.json` and `.md` with 3 runs, targets, verdicts and real output. Do not edit `criteria.md` to weaken missed targets. Use original non-sensitive writing only: this assignment requires the scenario file to be submitted in a GitHub repository that may be public.

Make your **third Unit 8 commit** after the baseline:

```powershell
git add results/ logs/audit.jsonl data/unit8_human_samples.json
git commit -m "Unit 8: record flood, full attack baseline and three criterion trials"
```

## 5. Diagnose one issue, make ONE measured improvement

Look for patterns among the BROKE attacks and MISSED criteria. Each miss needs a stage and mechanism. **Only if the evidence points to false positive AI accusations**, the supplied optional improvement widens the unsure band:

```powershell
python unit8_apply_improvement.py
python unit8_apply_improvement.py --apply
```

The second command changes only `config.py`'s `AI_THRESHOLD` from 0.78 to 0.85. It can let more AI text go undetected; that must be acknowledged. **If your baseline shows a different dominant failure, choose a different one-change improvement and explain it instead.**

Commit the change (**fourth Unit 8 commit**), restart Flask (Ctrl+C in Terminal A, then `python app.py` again), and run both full datasets **again**:

```powershell
git add config.py
git commit -m "Unit 8: widen uncertain label after baseline analysis"
python run_attacks.py --set .\attack_set --label after
python run_eval.py --label after
```

## 6. Build honest README evidence and submit

```powershell
python unit8_report.py
code UNIT8_README_ADDITION.md
```

It collects actual attack reports, all three trials, ten log entries when available, and points out missing diagnoses. Copy its sections into `README.md`; replace the `TO COMPLETE` markers with **your observations, actual results, and mechanism-based diagnoses**. Verify the attack tables have per-row HELD or BROKE outcomes.

```powershell
git add README.md UNIT8_README_ADDITION.md results/ scenarios.py logs/audit.jsonl data/unit8_human_samples.json
git commit -m "Unit 8: document real before and after tests"
git push origin main
git log --oneline -5
```

Your assignment calls for **at least four NEW commits in Unit 8**. The example workflow makes at least five: limiter, criteria runner, before-evidence, improvement, and after-evidence/README.

Submit your **existing** repo URL, not CodePath's starter:

https://github.com/KDawTech/ai201-project4-provenance-guard-starter-v2026

**Do not say a test was run if it was not. Missed criteria and unsuccessful improvements can earn full credit with honest diagnoses.**
