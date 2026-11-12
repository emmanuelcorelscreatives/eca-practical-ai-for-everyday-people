# Inspect Formulas and Cell Ranges — Lesson 58
Use the fictional Community Workshop Expenses data to distinguish a short range, a blank amount and a missing record. No paid account or AI assistant is required. Use any spreadsheet you already have; Google Sheets is the authored visual example. This offline kit contains CSV data, not a simulated Google interface or screenshots.

## Set up the faulty sheet
Keep the source notes separate. Import faulty-sheet.csv into a new sheet at A1 with comma separator and the first row as headers. A is Date, B is Item, C is Amount. Dates intentionally remain blank. If import inserts extra columns or shifts rows, correct that before continuing. The data occupy rows 2–8; Transport is B5 with empty C5; Volunteer meals is B8 with C8=60. Enter Total in B9 and =SUM(C2:C7) in C9. Use a formula bar or edit view to inspect references. CSV files contain data only and do not include the total formula.

1. Record the displayed total, formula, first cell, last cell, and next populated cell outside the range. Explain why correct arithmetic can describe an incomplete range.
2. Compare the source notes with the sheet, matching each label and amount. Identify the blank amount and absent record separately. Do not replace blanks with zero without evidence.
3. In an unused area enter =COUNT(C2:C8) and =COUNTA(B2:B8). Record both results and the number of source records. Explain why matching row counts alone would not prove completeness.
4. In a separate sheet enter 10, an empty cell, and 20 in A1:A3. Use =SUM(A1:A3) and =AVERAGE(A1:A3). Replace the empty cell with numeric 0 and compare. Restore a true empty cell by deleting its contents, not by entering a space or an empty-text formula. Other cell types are outside this exercise.
5. Copy Transport 35 from the source into C5. Insert a row before Volunteer meals and enter Accessibility materials 50. Verify the resulting labels: Accessibility at B8 and Volunteer meals at B9. The total moves to row 10. Inspect its actual formula after insertion; record what your spreadsheet did. Automatic range updates differ; do not claim a particular intermediate behavior without observing it.
6. Set C10 explicitly to =SUM(C2:C9). Confirm that the range begins at the first expense and ends at Volunteer meals. Compare your eight labels and amounts against corrected-sheet.csv and the source, row by row.
7. Recalculate 120+45+80+35+20+90+50+60 in a separate calculator. Record the actual displayed result. Then run =COUNT(C2:C9) and =COUNTA(B2:B9). Reveal or account for filters and hidden rows before explaining the table. No SUBTOTAL behavior is prescribed here; check the spreadsheet's actual behavior if using one.
8. Optional AI prompt: “Explain what =SUM(C2:C9) includes and list what I should inspect. This formula and table are supplied by me. Do not claim that you opened the sheet or verified the source.” Treat any reply as explanation, then check it against the source and opened sheet. Do not submit private data.

## Manual fallback
Write C2 and C7 as the faulty endpoints, then C2 and C9 as the corrected endpoints. Tick all eight source labels against spreadsheet records. Mark a blank amount unresolved unless evidence supplies its value. Re-add verified amounts with a calculator. Use audit-record.csv for your observations; distinguish actual observations from the worked expectations in answers.md.

## Optional local fixture check
With Python 3 installed, open a terminal in this extracted kit and run `python3 check-fixtures.py`. It uses only the standard library and verifies the supplied CSV fixtures and expected arithmetic. It does not open your spreadsheet, evaluate its formulas, inspect filters or certify your own repaired workbook. Without Python, complete the same checks by hand using answers.md. Keep answers closed until you attempt the exercises.
