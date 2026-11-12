# Answers and expected checks

These are deterministic worked expectations for the fictional source, not captured software results.

Entry A matches 12.50; Entry B matches 8.40. Entry C in the teaching extraction is a mismatch: 14.70 versus source AR-055 version 1, Entry C, 14.10. Mark unresolved while rereading; after confirming the original, record “14.70 changed to 14.10 after checking AR-055 v1 Entry C.” All three labels and values must be checked.

Correct calculator expression: `12.50 + 8.40 + 14.10 = 35.00`.

Spreadsheet: A2 Entry A/B2 12.50; A3 Entry B/B3 8.40; A4 Entry C/B4 14.10; A5 Total/B5 `=SUM(B2:B4)`. Expected numeric result 35, displayed as 35.00 with two-decimal formatting. Select B5 and inspect the actual formula; confirm the range includes exactly the intended three rows. Decimal separators and formula separators may vary by locale; keep values unambiguous and use your spreadsheet's accepted syntax.

A. `12.50 + 8.40 + 14.70 = 35.60`. Two tools can agree on a wrong total from the same wrong input. Their agreement checks arithmetic, not the truth of the copied values.

B. A and B alone total 20.90. You may explicitly report “Partial sum of verified Entries A and B only: 20.90; Entry C unresolved and excluded; complete total unavailable.” Do not present 20.90 as the total of all three or substitute zero, 14.10 from memory, or a guessed amount.

C. `=SUM(B2:B3)` omits Entry C and yields 20.90. Check labels, range highlights and the formula bar against the verified table; use `=SUM(B2:B4)` only when all three inputs are verified.

D. A typed 35.00 contains no inspectable calculation. Enter the explicit formula and inspect it; a plausible answer alone is insufficient.

E. Swapping A and B preserves 35.00, so the total does not detect the shifted labels. A row-by-row label/value comparison catches it.

Completion check: original source retained; every label/value compared; gaps explicit; old and corrected values preserved; expression checked; spreadsheet formula/range visible if used; independent entry check recorded; no fabricated AI or app evidence.
