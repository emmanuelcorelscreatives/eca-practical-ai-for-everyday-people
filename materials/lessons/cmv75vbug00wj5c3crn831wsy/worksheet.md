# Lesson 197 — Test with Sample Records
Emmanuel Corels Academy · Practical AI for Everyday People

## What you will test
Follow a fictional form record through trigger input, mapped transformation input, structured draft and a safe review record. Inspect content at every boundary. Two successful samples are not evidence about untested cases. Keep the real trigger OFF and unpublished throughout.

All names, events and values in this kit are fictional. No real Zapier, Google Forms, AI or Airtable action has been performed by this offline kit. Example drafts below are human-authored simulation fixtures, never claimed model outputs. The runnable check validates the supplied data and expectations only.

## Files
- `fictional-records.json` and `.csv`: identical two source records; empty strings/cells mean genuinely unanswered, not an answer.
- `expected-checks.json`: expectations to write down BEFORE testing; no invented values allowed.
- `mapping-card.csv`: field-by-field mapping to inspect, not an importable vendor configuration.
- `simulation-fixtures.json`: deliberately labeled manual examples with proposed review rows.
- `test-log.csv`: blank observation log; enter what actually happened.
- `validate_samples.py`: optional Python 3 consistency check; no dependencies/network/account required.

## Prepare a safe destination
Use only a new course-owned test area. In a supported connected platform, create an Airtable base named **Draft Review Table — TEST ONLY** with Source ID, Draft title, Draft summary, Safety note and Missing information columns. Verify account, permissions, destination and field mappings before any test. A test button can write real data. Do not use a live customer base, shared publication queue or messaging app. Never import credentials or existing personal records. Keep the real trigger disabled; do not publish this workflow.

The narrated example uses a Google Forms trigger, an existing AI transformation and an Airtable test action in Zapier. Interface labels and availability vary by account. Use the actual visible test control to load your fictional sample; if the connection/test feature is unavailable, STOP and use the manual route below. Do not invent a platform result or substitute a screenshot-shaped imitation.

## Test 1: normal record
1. Read TEST-197-001 in the source file. Expect the identifier, Community Garden Orientation, 22 October 2026, Cedar Room, New volunteers and Bring closed-toe shoes unchanged in meaning. Accessibility remains explicitly unanswered.
2. Load that exact sample in the trigger test. Inspect the retrieved input: Location must contain Cedar Room, not the date or notes. A success status alone is insufficient. Stop at the first missing, stale or misplaced value.
3. Compare every transformation input mapping with `mapping-card.csv`. Do not rewrite the existing AI instruction in this lesson.
4. Run only the transformation step. Read every output line against the fictional source. A new summary is allowed; unsupported claims are not. Accessibility must say it was not provided, not infer an answer.
5. Inspect the safe action destination and mapped fields, then run that test only if safe. Open the actual destination and find Source ID TEST-197-001. Check title, date, location, safety note and missing information in the STORED row. A green platform status is only evidence of the request status, not content correctness.
6. Record the source, actual transformation output and actual stored row separately. Mark pass only if all three agree on all required details.

## Test 2: incomplete record
TEST-197-002 is Seed Swap Table, for Neighbours, with Label seed packets. Date, location and accessibility are deliberately empty. Set expectations first, load this exact second record and check for stale values from sample 001. Inspect mapped input, run only the transformation and read output BEFORE any final action. Date, location and accessibility must remain explicit gaps. If a date/venue is invented, mark FAIL and STOP before creating a record. Record a correction note, then retest the affected boundary with the same fictional input. Do not erase the failed observation.

The lesson does not require creating a final action for sample 002. Log it as NOT RUN if you only inspected transformation. Never mark a nonexistent stored record as observed.

## Manual simulation fallback (complete route without accounts)
Open the source files in a text editor or spreadsheet. Use `simulation-fixtures.json` as HUMAN-AUTHORED EXAMPLES, not evidence of a real AI run. For each sample, copy source input into Step 1 received; inspect mapped Step 2 input; write a proposed draft and proposed review row. Label every output **SIMULATED / PROPOSED — NO EXTERNAL ACTION**. Compare with expected checks and record your actual manual result. Do not claim Airtable was updated. A passing manual simulation is limited to that manual exercise, and does not prove any external workflow works. Leave an external-result field NOT RUN.

## Optional local check
With Python 3 installed, open a terminal in this folder and run `python3 validate_samples.py` (on Windows, `py -3 validate_samples.py` if that is your installed launcher). Expected output: `PASS: 2 fictional inputs, expected gaps and manual fixtures; no external action performed.` This checks fixture consistency, not AI output, vendor accounts, mappings or live delivery. The manual route needs no Python.

## Learner exercise and completion
Complete the blank log from your own controlled tests or clearly labeled manual simulation. Keep raw input and every intermediate result. Show the ACTUAL test destination if a real action ran; otherwise explicitly show the proposed row and NOT RUN external action. Check every required value, safety note and unresolved question; write a pass/fail decision with reasons. Keep failures and correction notes, not just polished drafts. Reconfirm trigger OFF. Save both records and the log for Lesson 198 — Build the First Draft-Only Automation.
