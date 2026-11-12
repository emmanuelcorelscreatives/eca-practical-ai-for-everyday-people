# Lesson150 — Keep Original Data and Check Results

Emmanuel Corels Academy · Practical AI for Everyday People · Stage25

Use fictional expense records, preserve originals and check calculations independently. This kit works in an ordinary spreadsheet; an AI feature is optional. No real household data, account, purchase or cloud upload is needed. No named application execution or live assistant output is claimed.

## Three separate fixtures — do not mix their ranges

The authored demonstration contains three distinct ranges: five records with `=SUM(D2:D6)`; a missing-last-row example whose last expense is row7; and a seven-amount comparison with `=SUM(D3:D9)` yielding730. The kit makes those separate exercises explicit. It does not claim that five records total730, silently edit the lesson or overwrite original data.

1. **Five-row starter:** `Original-do-not-edit.xlsx` and `original-five.csv`. Headers are row1 and expenses rows2–6. Make your own copy named Working Copy — practice. `Working-Copy-practice.xlsx` is a separate prepared worked example; its formula sums the five amounts to615.00. It is not your own completed verification.
2. **Six-row range check:** `Range-check-six.xlsx` and `range-check-six.csv`. Headers row1, expenses rows2–7. The intended total includes the last35.00 record. `SUM(D2:D6)` omits that row; `SUM(D2:D7)` includes it and yields650.00. Keep the missing category blank; do not guess a category. The visual teaching example can show the bad range and a correction note without presenting its partial numeric total as a valid answer.
3. **Seven-row independent comparison:** `Independent-comparison-seven.xlsx` and `comparison-seven.csv`. Workbook title is row1, headers row2, expenses rows3–9. Values185.50,96.00,210.00,75.00,48.50,35.00,80.00 total730.00. The title/header offset is why this separate formula usesD3:D9. CSV has no title row: when importing CSV alone its seven expenses occupyD2:D8; adapt the formula to actual rows instead of copying the workbook range blindly.

## Practice workflow

Open the original, make a copy and confirm its rows/columns match before editing. Keep the original open for comparison. Do not assume connections, permissions or special features copy identically. This beginner exercise needs only a readable copy with the source untouched.

Ask an available assistant only for a formula suggestion and its exact cells: “Using the Amount column, suggest a formula for the total. State the cells or range you used.” This is an example instruction, not a claimed assistant response. Alternatively enter the explicit formula manually. Inspect the formula bar and every intended row, excluding headers and unrelated/subtotal rows.

Re-add the same fixture's visible amounts using a separate calculator, paper scratch sum or explicit independent method. Do not ask another AI to certify the first answer. If values differ, do not average or pick one: inspect missing/duplicated/filtered rows, ranges, values and units. Record the actual cause and correction. For consequential totals check all records. Category summaries must include uncategorized records separately; a blank is uncertainty, not a reason to invent a category.

Use `VERIFICATION.md` to record your check and `expected-results.json` for separately labelled answers. Save checked work separately; keep original file bytes unchanged. Run `python3 verify-kit.py` for fixture arithmetic, workbook XML/CRC, exact formula ranges and CSV agreement. This is not a claim that your own spreadsheet or copy was checked. Cached XLSX formula values are deterministic prepared examples; the workbook requests recalculation when opened.

The app has a separate **Download verification record JSON** button. Save that record alongside your working-copy CSV; it includes the fixture, source/working data, formula, independently typed operands and results, match status, correction note, and actual download time. Alternatively fill and save VERIFICATION.md manually. Nothing is retained after reload unless you export/copy it.
