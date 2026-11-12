# Lesson 179 — Prepare Simple Operational Summaries
Emmanuel Corels Academy · Practical AI for Everyday People

All records are self-authored fictional practice data; no private people or actual service outcomes are represented. Workbook values and generated cached formulas are teaching data, not evidence of a software execution or real event.

## Practice
1. Keep the raw September CSV unchanged. Inspect REP-094 and document why its identical duplicate is one request, not a second visit.
2. Count 51 raw rows and 50 unique IDs; reconcile 42 completed plus 8 unresolved with 50. Reconcile August 35 plus 9 with 44.
3. Calculate (42−35)/35 = 0.20, a 20% increase relative to August completions. Both periods are full calendar months; do not claim identical length (31 versus 30 days).
4. Sum only complete volunteer shifts: 19 × 4 = 76 confirmed hours. SH-20 has no end time; never invent it. State “at least 76 confirmed hours”, not the complete monthly total.
5. Transfer only Approved Facts to an approved assistant. Do not include raw records, names or contacts. Use the prompt and classify every sentence in its returned draft. If unavailable, write manually using the same template.
6. Remove the deliberately unsupported causal sentence in generated-draft-example.md. A reminder date is recorded, but attribution is not. A cautious possible explanation belongs under investigation, not findings.
7. Recheck every number and claim; retain the final update, raw sources, calculations and review checklist together. The practice answer remains a draft requiring human permission before external sharing.

## Formula compatibility
The saved visual prompt mentions `COUNTUNIQUE`, a Google Sheets function. Desktop Excel does not implement that function. For Excel 365 use `=ROWS(UNIQUE('Request Register'!B2:B52))`; for the supplied workbook the Checks sheet uses a compatible SUMPRODUCT/COUNTIF uniqueness calculation. This documents a demonstration compatibility issue without changing lecture narration. Do not display a fake COUNTUNIQUE result in Excel.

## Files
CSV sources, data-dictionary.md, August_Volunteer_Log.csv, Repair_Event_Records.xlsx, assistant-prompt.txt, generated-draft-example.md, reviewed-update.md, review-checklist.md and verify.py. Run `python3 verify.py` in this folder; no packages or network required. The workbook contains source data and formulas with expected cached results; recalculate with your own trusted spreadsheet application. CSV files are portable independently of Excel licensing.
