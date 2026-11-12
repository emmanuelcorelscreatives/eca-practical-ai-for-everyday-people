# Formula drafts to inspect in LibreOffice Calc
The native lesson application is LibreOffice Calc. These are inspected reference formulas. `assistant-response.json` separately preserves the actual recorded formula-draft interaction with its stated assumptions. The reference and interaction are not claims of a particular commercial assistant interface. The accompanying workbook executed these formulas in genuine LibreOffice Calc 24.2.7.2; observed results are recorded in `native-observations.json`. Recheck your own ranges and results. English Calc formulas normally use semicolon separators; account for your locale.

Import `events-original.csv` with UTF-8, comma separator, a header row and Date as a genuine date (YMD). Keep Amount numeric and its two blanks truly blank. Verify A1:E9: ID, Date, Group, Item, Amount. A string that looks like a date is not sufficient.

- Entered numeric total: `=SUM(E2:E9)` → expected 118.
- Put `Group A` in G2: `=SUMIF($C$2:$C$9;G2;$E$2:$E$9)` → expected 42. Repeat for Group B/C.
- Blank-group entered total: `=SUMIF($C$2:$C$9;"";$E$2:$E$9)` → expected 15.
- Group row count: `=COUNTIF($C$2:$C$9;G2)`; expected A 2, B 3, C 1.
- Blank Group count: `=COUNTIF($C$2:$C$9;"")` → expected 2. Group counts sum to eight records; Amount count is six, not eight.
- For a whole-month Group A total, keep G2 as Group A and put an actual month-start date `2026-10-01` in H2 (display format YYYY-MM if desired): `=SUMIFS($E$2:$E$9;$C$2:$C$9;G2;$B$2:$B$9;">="&H2;$B$2:$B$9;"<"&EDATE(H2;1))` → expected 42. Lower bound inclusive, next-month bound exclusive. `Date=H2` alone matches a date rather than a whole month. A different selected month with no rows must be labeled as no matching supplied rows, not proof that no real event occurred.

The original duplicate-review copy retains all eight rows. After reading the explicit fictional owner decision, the analysis copy excludes only original row 7: seven retained records, five numeric Amounts, entered total 100, A 42, B 43, C 0, blank-group 15. The two missing Amounts remain missing. Any pivot-style summary must identify its source range and whether the exclusion has occurred; it must include/label the blank Group rather than silently lose those rows.
