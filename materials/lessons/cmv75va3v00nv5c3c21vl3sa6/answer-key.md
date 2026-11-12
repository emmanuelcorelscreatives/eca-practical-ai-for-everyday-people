# Expected checks, not application execution proof
The exact clean range is A1:G7: seven unique nonblank headers plus six expenses. The table is in `clean-table.csv`; compare it to `source-notes.csv`.

- Record1: Paper cups, 2026-10-12, Supplies, quantity3, unitcost2.40, paidYes, Note1.
- Record6: Room hire, 2026-10-14, Venue, quantity1, unitcost45.00, paidNo, Note6.
- Paid sequence: Yes, Yes, No, Yes, Yes, No.
- Paper cups and name badges are distinct purchases even though both are Supplies. Shared date/category alone is no duplicate proof.
- Spot check: 3×2.40 =7.20. Inspect =J5*K5 and both input cells in the actual spreadsheet; this mathematical expectation is not a claimed screenshot or native recalculation receipt.
- The inserted blank row interrupts a contiguous range; remove the gap, not any purchase. Move the planning estimate outside the data rather than counting it as an expense.
- The separate ambiguous refreshments note is not part of the six known purchases and supplies no exact quantity, unitcost or payment status.
- A structural assistant response is generated advice, never an independent source verification. No spending analysis belongs in this exercise.
