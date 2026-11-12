# Lesson 130 — Organize Files with Clear Naming Rules

These are self-created fictional Academy practice records. No real person, business, account or payment is represented. Work only on these supplied practice copies. This lesson teaches review and recovery, not automated renaming scripts.

## Practice setup

Put the four supplied records in Documents/Filing Practice/Originals: scan_001.pdf, IMG_0042.jpg, document(7).pdf and receipt-final.pdf. The receipt JPEG is exported from the included self-created receipt-source.svg, with no OCR added to the source image. Keep all four original names intact. Import review-sheet.csv into your spreadsheet; preserve filename strings as text.

## Inspect before suggesting

Open every record. The library notice was issued 30 September 2026; its 20 October deadline is not the issue date. The booking confirmation was issued 2 October; 18 November is the event date. The two bicycle records share 3 October but one is a paid receipt and the other an estimate. Do not invent identifying numbers or customer details.

Use YYYY-MM-DD_Category_Description and the original extension. Categories are Notice, Receipt, Booking and Other. Underscores divide fields; hyphens join description words. Avoid quotation marks, asterisks, colons, angle brackets, question marks, forward/back slashes and vertical bars. Check your actual storage service's current naming and length rules.

Use assistant-instruction.txt only with appropriate documents and permitted services. A generated suggestion remains separate from opened evidence. A changed filename does not remove sensitive contents or metadata. Leave unknown values CHECK, and leave approval blank until a person reviews them.

## Find and correct defects

ocr-deliberate-error.txt is an explicitly constructed error example, not an assertion about an OCR engine. Compare 08 with the visible 03. Record why you corrected it. In collision-example.csv the extensions differ, so these are not identical full filenames, but their ambiguous base names are misleading. Resolve using truthful Paid and Estimate descriptions, as in review-sheet.csv. Keep the booking on hold pending its date review.

## Preserve and preview

Before any rename, copy all four untouched records to Backup-Before-Rename. Verify four files, original names and a document that opens. Create a separate Working folder; do not rename the backup. Review the complete old-to-new mapping, sorted proposed names, extensions, unsupported characters and conflicts. Approve only the notice and paid receipt as in approved-small-batch.csv.

PowerRename is optional. Open it on working copies and inspect the actual current controls. These two different mappings may require separate exact-match operations; never use a common replacement rule that changes both to the same name. For each preview compare source, replacement and extension behavior with the approved row. Do not click Rename if any preview differs. Manual one-file-at-a-time renaming remains the safe fallback.

## Apply the small approved batch

Only the notice and paid receipt may change. The booking and estimate retain their original filenames. Open the two renamed files, verify their contents and only then record Completed and verified open. completed-small-batch.csv shows the expected record after this manual verification; it is an answer key, not proof that you executed anything. Stop on a mismatch and restore from the preserved copy before trying a corrected plan.

## Expected checks

- Library: 2026-09-30_Notice_Library-Renewal.pdf.
- Paid receipt: 2026-10-03_Receipt_Bicycle-Repair-Paid.jpg.
- Booking stays document(7).pdf during this approved pair, despite its reviewed proposal.
- Estimate stays receipt-final.pdf during this approved pair.
- Backup retains exactly the original four names and unchanged file contents.
- No rename changes a document's text or validates its meaning.

Describe how you would recover after an interruption without renaming a row twice. Explain why the two dates in the booking require a recorded rule and review. Never replace CHECK with an invented value.
