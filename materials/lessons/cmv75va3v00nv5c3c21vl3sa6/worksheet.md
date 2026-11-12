# Build the clean table
## 1. Define the record
Open Source Notes and state: one record = one expense. Count six purchases. Do not split one purchase merely because it has several fields. Separate combined purchases only when the original source supplies each purchase's details.

## 2. Inspect the deliberately messy sheet
The Messy sheet has vague headers, mixed fields, two purchases combined in one row, an internal blank row and an embedded estimate. It is a deliberate teaching defect. Do not copy its estimate as a seventh expense or infer values from its layout.

## 3. Build clear columns
Use Headers Only as a start. Create exactly Date, Item, Category, Quantity, Unit Cost, Paid and Source Note. Put the paper-cup purchase in row 2: 2026-10-12 | Paper cups | Supplies | 3 | 2.40 | Yes | Note 1. Do not mix fruit with cups. Transfer the other five original notes into rows 3–7; use Clean Table only after attempting the transfer.

## 4. Inspect range and meaning
Keep A1:G7 contiguous: no internal blank rows/columns, no totals, comments or planning notes among records. Place a planning note outside the source table. Date holds dates, Quantity counts, Unit Cost a per-unit local value, Paid Yes/No. Formatting alone proves no accuracy.

## 5. Verify directly
Count six records. Compare all six notes, including every Paid value. Spot-check Paper cups 3 at 2.40 and Room hire 1 at 45.00. Do not deduplicate cups/name badges simply because they are both Supplies; compare full records and original notes first.

## 6. Optional structural assistant review
Use the exact bounded instruction in `assistant-prompt.md`. Do not request spending analysis or changed values. Record the actual response and compare its advice to your own source inspection. Never treat agreement as independent evidence.

## 7. Check one multiplication
In separate scratch cells J5=3 and K5=2.40, enter =J5*K5 in L5. Open the actual formula bar and referenced cells. Expected mathematical value: 7.20. Verify both source inputs, not just the displayed number. The workbook has no cached Excel result; opening it must recalculate.

## 8. Preserve uncertainty
Read `uncertainty-example.md`. Do not append the ambiguous note to the clean six-record dataset. Leave unconfirmed quantity, cost and payment status empty, or clearly mark for confirmation outside the numeric fields.

## Manual fallback
Use `manual-checklist.md` with no AI. Keep your original notes, practice workbook and record definition together. Structure comes before analysis.
