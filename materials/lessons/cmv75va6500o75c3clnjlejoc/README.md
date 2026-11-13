# Ask for Formulas You Can Explain — lesson 147

Emmanuel Corels Academy. Fictional event-cost estimates and actuals; no purchases or real private data. This kit supplies a genuine OOXML spreadsheet and source-matching practice exercises. Formula cells deliberately contain no manufactured cached result; the workbook requests calculation on opening. The supplied expected results are independent arithmetic expectations, not claims of observed spreadsheet or assistant output.

## Files and workflow

Keep the original `formula-practice.xlsx` unchanged. For this lesson’s native demonstration, use the authenticated workbook as the source for a separate Academy working copy in genuine Google Sheets in the authorized browser. Record the actual application and version observations honestly; do not label Sheets as Excel or claim a Copilot interface. A learner may also do the independent arithmetic manually. `event-costs.csv` is an accessible source-data counterpart.

The `Event` sheet has A1 Item, B1 Estimated cost and C1 Actual cost. Room is 120/125, food85/90, printingblank/0 and transport40/35. The estimate total belongs in B6; the actual total belongs in C6. B4 is genuinely absent, not an empty string or a numeric zero. A7 labels the average estimate in B7.

1. Record the intended result, destination, source range and blank rule in `worksheet.md`. Use `formula-request.txt` with an available assistant, or write the simple formula manually. Assistant text is generated material, not proof; save its real output separately.
2. Inspect `=SUM(B2:B5)` in B6. Read both endpoints and verify that estimates—not actuals, headers or the result cell—are included. Compare the spreadsheet’s actual result with mental arithmetic.
3. Inspect `OmittedTransport`, where `=SUM(B2:B4)` omits transport. Compare a plausible result with the full intended range; syntactically valid does not mean correct.
4. In `KnownTest`, E2:E5 contain10,20,blank,5. Inspect E6 and compare its full-range formula with the intentionally incomplete H6 formula. Check both against your predicted answer.
5. Compare B7 in `Event` and `BlankZero`. `AVERAGE(B2:B5)` ignores a genuinely blank B4 but includes a numeric0. Explain why the divisor changes. Do not pretend an unknown estimate is known to be zero.
6. Copy the estimate formula from B6 to C6 in a working copy. Verify that it becomes `=SUM(C2:C5)`. `WrongCopiedColumn` deliberately keeps B-column references in C6 as a counterexample. Labels never control the referenced cells.
7. `ManualAddition` uses `=B2+B3+B4+B5`, the simple alternate total in the lesson. Explain each part; compare it with SUM.
8. In `FreshPractice`, describe the calculation before writing the F6 formula for F2:F5. Predict the total, then change F5 from10 to1 and predict again. Only after your attempt inspect `FreshChecked` and `answer-key.json`.
9. Compare intention, actual formula and a separately checked small example. Ask for a simpler formula if you cannot explain every function/operator/reference. `reusable-request.txt` includes the general request and the blank-versus-zero average rule.

Use `python3 check_workbook.py` for local structural/source/arithmetic checks. These do not replace genuine Google Sheets observation of formula edit/range outline, copy behavior, recalculation and independent review. Record actual browser/application observations separately. Save any genuine assistant response with its actual provenance; authored requests and hypothetical explanation errors must be labelled as authored examples, never observed assistant output.

No macro, external link or network connection is embedded. The workbook has eight separate source-matching scenario sheets; copying formulas or changing input values affects only your working copy. No automated edits are sent to an account or cloud sheet.
