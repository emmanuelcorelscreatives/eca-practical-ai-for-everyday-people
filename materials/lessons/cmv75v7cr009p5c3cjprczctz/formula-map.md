# Spreadsheet cell plan

Use a blank worksheet named Quantity Check. Import quantity-check-template.csv with comma separator and decimal point. Confirm A1=Quantity, B1=Unit price, C1=Total; A2=48, B2=19.75; rows 2–6 are exactly five records. Avoid importing a whole line into one cell. The supplied completed CSV is an answer fixture with numeric totals, not a workbook with formulas.

For the initial single-record check, leave C2 empty, select C2, type `=A2*B2`, inspect the referenced source cells and confirm. Expected C2 is 948. This is a manual exercise; no application execution is claimed by the kit.

For the five-record extension, enter the same multiplication in C3 through C6 using each row's own references: `=A3*B3`, `=A4*B4`, `=A5*B5`, `=A6*B6`. C7 should first contain the deliberately incomplete `=SUM(C2:C5)`. Observe and record 1,438. It includes only four records and omits C6=48. Correct C7 to `=SUM(C2:C6)` and record 1,486. Inspect all five records, not only the currently visible selection. A quick coarse estimate of 1,500 would not reliably expose the omitted 48; row counting and range inspection are still required.

For the mean exercise, put 12,15,18,20,25 in A2:A6 on a separate sheet. `=SUM(A2:A6)` gives 90, `=COUNT(A2:A6)` gives 5, `=AVERAGE(A2:A6)` gives 18. Bounds 12 and 25 reject 31 before an exact mean is needed. These formulas use numeric cells without blanks or text. Missing values and zeros have different meanings; investigate rather than substitute.

On paper the same table can be checked with five products followed by addition. No software is required to complete the worksheet.
