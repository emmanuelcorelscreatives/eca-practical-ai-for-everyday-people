# Lesson 207 — Set Timeouts, Retries and Stop Conditions

This Emmanuel Corels Academy practice kit accompanies the authored lesson. It uses self-created fictional requests only. It is an offline **simulation**, not evidence from a live provider, a no-code vendor account, or an external delivery. No credentials, messages, purchases, paid calls, or network connections are needed. Python 3 runs the optional simulator; the supplied actual execution evidence is Linux only, and the Windows `py` launcher alternative is provided but not executed here; spreadsheet work can be done manually in your preferred tool.

## The training policy

Use a 30-second per-attempt timeout, **three total attempts including the first**, and delays of 10 seconds before attempt 2 and 30 seconds before attempt 3. These are training values, not universal recommendations. In a real tool, confirm whether attempts includes the first try and whether the timeout applies to one step or the whole run. Never assume a timeout proves that an external action did not happen. Inspect the destination and use duplicate protection before repeating a real action.

Open `simulator.html` in a browser for an interactive, self-created offline app. Its settings, test execution, bounded attempts, virtual delay advancement, history, draft downloads and error queue work locally. It is not a vendor interface or a real service run. Download results before resetting.

## Three practice cases

Open `Automation_Test_Log.ods` in Calc (or another compatible spreadsheet). It contains Test Inputs, an empty Error Log, a prediction/observation Test Summary and Read Me. Keep the observation cells blank until you inspect an actual practice run. CSV files provide a simple fallback.

Open `inputs.csv`: REQ-101 is Normal / Practice request A; REQ-102 is Temporary failure / Practice request B; REQ-103 is Persistent failure / Practice request C. All content is fictional. Do not put passwords, access tokens, full private messages or unrelated personal details into the error log.

1. Predict each result before running. REQ-101 should finish on attempt 1 (8 simulated seconds), REQ-102 should fail once, wait 10 simulated seconds, then succeed on attempt 2 (9 simulated seconds). REQ-103 should fail three times, wait 10 and then 30 simulated seconds, and stop. No fourth attempt is allowed.
2. Optionally run `python3 check_simulator.py` (on Windows: `py check_simulator.py`). Then run `python3 simulator.py --out generated` (Windows: `py simulator.py --out generated`). Choose a fresh output directory for another run; existing output is deliberately refused to avoid stale evidence.
3. Compare **three places**: `generated/run-history.json`, `generated/Review Drafts`, and `generated/Error Log.csv`. Only REQ-101 and REQ-102 drafts should exist. REQ-103 must have exactly one error row and no draft. The date/time is a fictional training clock; durations/delays are virtual, not measured service performance or actual waiting.
4. Open `generated/Test Summary.csv` in a spreadsheet. Its observed column records only the executed simulator result. Add your own observation notes only after actually inspecting the files; never treat a green status as sufficient proof.

## Human-readable error record

The error row includes input ID, fictional local time, failed step `Create draft`, three attempts, `Service unavailable after three attempts`, safe reference `Practice request C`, status `Needs human review`, and `Check service access; then create draft manually if appropriate`. Keep the original failure and both retry results. In real work use the actual local timestamp and safe reference; do not copy a sample date as observed evidence.

## Manual fallback and decision exercise

Pause further attempts. Open the safe reference; check access and the destination; create the needed draft manually only if appropriate, then record the human outcome. The simulator creates no external effects and does not claim to implement general duplicate protection.

Decide: (a) brief connection outage, (b) missing permission, (c) request timed out but may have been accepted, (d) malformed input. Expected answers: (a) bounded retry only if repeating is safe; (b) stop for human correction; (c) inspect/reconcile destination and confirmation before any repeat; (d) correct input instead of looping. The check script also proves that synthetic permission and ambiguous-timeout cases stop after one attempt.

## Reuse checklist

Confirm normal success, temporary recovery, persistent stop, destination/error/history agreement, no secrets in logs, finite usage, and a workable manual route. Check actual account controls, connector limits, permissions, interface and plan availability before unattended use. The next lesson addresses output structure; this kit does not replace that lesson.
