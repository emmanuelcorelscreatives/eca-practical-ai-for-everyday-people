# Add Logging and Duplicate Protection

Emmanuel Corels Academy · Lesson 214 · Fictional Community Workshop Requests

This offline practice kit matches the lesson's REQ-1047, TASK-031 and two-run demonstration. It is a teaching simulation, not a connection to an external task service or a copy of Google Sheets. No notices are sent and nothing is published. Only fictional room-setup data is included.

## The rule

**One source record ID may create no more than one review task.** Check the stable source identifier before creating anything. Do not identify duplicates from names, request text or timestamps. Identical text with different IDs is not automatically the same source record. Changed text under the same ID needs human review rather than an automatic replacement.

## Manual spreadsheet practice

1. Create a new practice spreadsheet named Decision Log. Import `decision-log-empty.csv`; freeze its header row. Its six fields are Source ID, Checked at, Run reference, Decision, Reason and Output reference. Set all identifier columns to plain text. Use the clearly labelled UTC check times supplied here.
2. Read `source-request.csv`. Search the Source ID column for REQ-1047. With no existing row, create exactly one fictional review task: TASK-031, title Review room-setup request, details Arrange twelve chairs., status Awaiting review. Inspect that destination task before accepting the run.
3. Record RUN-001 at 2026-10-15 13:10 UTC: New — sent for review / No existing Source ID found / TASK-031.
4. Submit the same source record again. Find its earlier row **before** the creation action. Do not create another task. Record RUN-002 at 2026-10-15 13:14 UTC: Duplicate — no new output / Existing Source ID found / TASK-031.
5. Compare all six cells of each row with `decision-log-expected.csv`. There should be one destination task and two log rows. Neither row says a human approved the task.
6. For manual fallback, find or filter REQ-1047. Inspect both matching rows and TASK-031. Record a new manual decision using the actual time and an unmistakable manual run reference; do not pretend the supplied fictional timestamps were observed live.

A counting formula such as `=COUNTIF(A2:A,"REQ-1047")` can help in Google Sheets, but inspect the actual rows and destination. Separator syntax can vary by locale. The formula is not a replacement for checking what happened.

## Use the browser practice

Open `workflow-practice.html` locally in a modern browser. It is an actual working Academy practice app, visibly not Google Sheets. Click Find Source ID in log, then Create review task. Run the lookup again, then Record duplicate decision. Inspect one task and two log rows. Edit the same ID to changed details and look it up: it holds for human review. The browser practice is in-memory only; closing or resetting it loses its data. It is sequential and not a durable production log. Use the real spreadsheet steps above for spreadsheet practice.

## Run the small offline practice simulator

Python 3, standard library only: `python3 duplicate_practice.py --demo`. It prints the six-column log and the one-task count using the lesson's fictional check times. It writes no external records. Run `python3 check_practice.py` to execute the new/repeat, changed-content, separate-ID, failed-lookup and missing-ID checks. Learners do not need to program to complete the manual exercise.

## Extend and inspect

Use `practice-cases.csv` in order, resetting your fictional worksheet when needed. Before each case, predict the decision, destination count and reason. A missing log row is not proof that nothing happened: if creation succeeded but logging failed, inspect the destination and platform history before retrying. Never blindly create a second task to recover a partial run.

This simple sequential teaching simulation is not a concurrency-safe production system: two simultaneous first runs need a platform-supported unique key, atomic claim or equivalent idempotency mechanism. Production destinations and log writes can fail independently. Stop and reconcile unknown outcomes before retrying. The lesson's manual inspection remains essential.

## Privacy and review

Restrict the log to reviewers/maintainers. Store identifiers, check times, decisions and references rather than whole messages or credentials. Platform history retention varies. Check permissions and limits in the platform you actually use. Nothing in this kit asserts a paid plan feature or claims a real external action occurred.

## Success criteria

- Stable REQ-1047 retained across both runs; check precedes creation.
- Exactly one TASK-031, awaiting human review, with the correct mapped fields.
- Two decision rows, both linked to TASK-031 and their own run reference.
- Changed content is not silently overwritten; uncertainty stops creation.
- Manual fallback checks the log and destination, preserving evidence.
