# Summarize and Compare Data
Emmanuel Corels Academy · Practical AI for Everyday People · Lesson 148.

These are self-created fictional Academy practice records, not private records or observed real events. The supplied workbook (including five actual assistant formula drafts in Original K2:K6) was executed in genuine LibreOffice Calc 24.2.7.2. See `native-observations.json` for the observed checks. Your own workbook still needs independent checking.

Start with `Academy_Event_Summary.ods` or build the same exercise from the CSV files. Its Original, Analysis Copy, Duplicate Review, Monthly Summary, Checks, Pivot Summary, Assistant Draft and Final Checklist sheets retain the different analysis states; label them carefully. The pivot uses the original eight rows and total 118; the cleaned analysis copy totals 100.

1. Preserve `events-original.csv` unchanged. Open/import it in LibreOffice Calc, with real dates and numeric amounts. Verify headers A1:E1 and eight rows A2:E9; inspect all original records together.
2. Define one row and its identity meaning. There are two blank Groups and two blank Amounts. Keep them visible and unresolved; do not silently replace blanks with zeros.
3. Use `assistant-prompt.txt` optionally with permitted fictional input, or work manually from `formula-reference.md`. `assistant-response.json` records the actual generic assistant formula draft used for this exercise; inspect its assumptions and do not treat it as an owner decision. Inspect every formula range, criterion and assumption. Do not supply private data or editing access.
4. Independently add entered values: 30+12+25+18+18+15=118. Group sums are A42/B43/C18/blank15. Counts are A2/B3/C1/blank2, total8 records. Count/total checks do not explain missing values or authorize duplicate removal.
5. Compare both EVT-104 records in a review copy before doing anything. Only after reading the explicit fictional author decision in `data-owner-decision.md`, exclude original row7 from the analysis copy. Original remains unchanged. The supplied `analysis-copy.csv` is the reference outcome for that decision only.
6. Reconcile entered total100 against retained original rows2,3,4,5,8. A42+B43+blank15=100, C's only record was excluded. Missing Amounts remain missing and numeric totals are incomplete real-world evidence.
7. Make a pivot-style summary in Calc, with Group as rows and Amount as summed values. Check actual source range, blank label and whether you used Original or the analysis copy. Compare against formula/reference arithmetic before presenting it.
8. Test the true whole-month conditional sum using a real date interval, not equality to a month-start date. Label no matches and unknowns honestly. Dates stored as text need fixing in a permitted copy, not assumed correct.
9. Use `reconciliation-expected.csv` after doing your independent work; note original row numbers remain audit references after analysis rows move. No check marks claim a human has already reviewed your workbook.

The exercise remains useful without an AI feature: use Calc formulas, filters/sorting of the whole table, a pivot-style summary, and hand arithmetic. The optional Python verifier checks structure/arithmetic only, not whether a real dataset's owner decisions are justified.

All files are fictional/self-created, no macros/private files/external links. Academy practice materials: CC0-1.0.
