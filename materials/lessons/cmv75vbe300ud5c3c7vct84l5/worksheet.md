# Check Each Transformation — Lesson 184
Emmanuel Corels Academy · Practical AI for Everyday People

All records, source references and deliberately faulty outputs in this kit are self-authored fictional training data. The output CSVs reproduce the lesson's failure modes; they are not claimed to be responses actually obtained from an AI provider. No delivery or event has occurred. Use only these new files, not private records.

## Files and authoritative input
Open `source.csv` in your spreadsheet application. Keep it unchanged, preferably as a separate Source sheet. Use comma separation, UTF-8, and a text Record ID column; display dates as YYYY-MM-DD. SRC-A1 through SRC-C2 are fictional source locators within this training table, not external evidence links. Their meaning is simply the corresponding row of source.csv.

The six rows are EV-101 through EV-106. Record four controls: 6 rows, earliest 2026-11-03, latest 2026-11-18, total quantity 53. EV-104 is 2026-11-12. EV-105 is 2026-11-18 and its delivery status is missing. EV-106 also has date 2026-11-18. Do not infer safety approval from “Electrical review required”, sign wording from “Wording pending”, placement from “Placement pending”, or delivery confirmation from a quantity.

## Practice: two handoffs
1. Compare `output-1-omitted.csv` with source. Count first, then match stable IDs rather than row positions. Log the missing record in `discrepancy-log-blank.csv`. A count match alone can hide a missing ID replaced by a duplicate.
2. Compare `output-2-date-error.csv`. It has six rows and still the same minimum and maximum dates. Identify the changed field by Record ID. Check names/items, dates, quantities, notes and source references rather than trusting summaries.
3. Read `unsupported-prose.txt`. Separate the copied quantity, changed date and unsupported confirmation. Use `classification.csv` to distinguish copied/calculated/generated/assumed/unsupported statements. Remove unsupported assertions, or obtain actual independent evidence if the task genuinely needs them. Missing information stays missing.
4. Write a precise correction instruction naming EV-104, the EV-105 source date and the missing delivery status. If using a real assistant, paste only this fictional table and preserve a copy of its actual response separately. Do not assume it will reproduce our deliberately faulty fixtures.
5. After checking, compare your result with `checked-transformation.csv`. Notes are preserved exactly; “Delivery status missing” and the narration's “Delivery status: missing” express the same missing fact, but this reference CSV retains the exact source spelling so comparison is literal.
6. Import/paste the checked table into a separate sheet/file and compare at the destination again. `destination.csv` is the provided correct second-handoff reference. Keep Source and Checked transformation separate and log any actual paste/import discrepancy you introduce; do not invent one.
7. Recalculate all controls, check unique IDs and every source field, and review the discrepancy log before accepting the result. `discrepancy-log-answer.csv` supplies the three demonstration corrections, not evidence that a learner has completed them.

## Optional prompt
Create a concise preparation table. Preserve every Record ID, date, item, quantity, note and source reference. Do not infer missing details. Label any generated wording. Return the table only.

## Manual fallback
Use two spreadsheet windows side by side or split-screen phone views. Tick IDs, compare each field and sum quantities with a calculator or spreadsheet. For CSVs imported with headers in row 1, quantities in D2:D7 can be summed with `=SUM(D2:D7)`; locale separators and imported date types vary. Count six visible data rows and compare YYYY-MM-DD text directly. Version history helps locate edits where available; it does not prove an added statement came from the source. Screen/whiteboard illustrations are preferable to photographed paper for this course.

## Answer key and acceptance
Output 1 omits EV-104 (quantity 4), leaving 5 rows and quantity 49. Output 2 changes EV-105 from 2026-11-18 to 2026-11-08; it retains 6 rows, total 53 and earliest/latest 2026-11-03/2026-11-18 because EV-106 retains the latest date. The unsupported sentence falsely confirms delivery and carries the wrong date. Correct and destination references match every source field, contain 6 unique IDs and quantity 53, and preserve all pending/missing notes.

Optional local verification: with Python 3 run `python3 check_transformation.py` from this extracted folder. It uses only the standard library, reads the bundled files, writes nothing and makes no network calls. It tests both known failures and corrected references. Coding is not needed for the manual exercise. `verification.txt` records the kit author's actual local execution, not learner completion.

For consequential schedules, payments, public notices or safety instructions, use stronger comparison and human review; stop to obtain genuinely missing facts. This exercise checks a handoff only. Workflow automation belongs to the following lesson.

## Model correction instruction
EV-104 was omitted. Restore this complete row: EV-104 | 2026-11-12 | Extension leads | 4 | Electrical review required | SRC-B2. Restore EV-105 date to 2026-11-18; its item is Water containers, quantity 6, note Delivery status missing, reference SRC-C1. Remove the unsupported delivery confirmation. Preserve all six Record IDs and every other original source field exactly; do not infer missing facts. Return only the six-row table.

## Suggested 13-minute practice schedule
This optional student practice plan totals 13:00; it is not a measured claim about the narrated video's native duration. 00:00–02:00 open source and calculate controls; 02:00–04:00 compare omitted-output IDs; 04:00–06:00 compare dates and summary limitations; 06:00–08:00 classify the unsupported claim and write corrections; 08:00–10:00 check every corrected field and second destination handoff; 10:00–12:00 complete discrepancy log and manual fallback; 12:00–13:00 reconcile controls and review acceptance. Actual video duration follows complete native narration under the course renderer, not this worksheet's schedule.
