# Build the Claim-and-Evidence Table
Use this offline fictional evidence pack to practice the exact six-column routine from Lesson 68. Allow 20–30 minutes. A spreadsheet is convenient; a document or paper and a calculator work too. No account, AI subscription or coding is required.

1. Open material-to-check.md. Mark it material under review, not evidence.
2. Open claim-table-blank.csv in any spreadsheet, choosing UTF-8, comma separation and quoted text. It contains eight rows: the original facilities promise has been split into accessibility and refreshments because the results differ. The six headers are a course convention, not an official standard. Save your copy separately. A blank CSV has no formulas or hidden evidence.
3. Explain the consequence of error in each row. Begin with date/time, venue, access and deadline; finish every row. Keep each independently checkable assertion separate.
4. Open Event brief.odt (or identical event-brief.md), Registration list.ods (or identical registrations.csv), and Facilities note.odt (or identical facilities-note.md). These are self-created practice originals, not real-world authoritative records. Count the 36 records yourself; exclude the header and total row. Do not use the draft total as proof.
5. Fill Source opened and Evidence found. Record exact date, time, location, quantity and scope, not just the file name. Check capacity and registrations before arithmetic.
6. On a calculator enter 36 ÷ 48, then multiply by 100, or enter =36/48 in a spare spreadsheet cell and apply percentage formatting. You should obtain 0.75 or 75%. Record both inputs and their sources. A cached spreadsheet result is not independent execution proof; perform the calculation yourself.
7. Choose Supported, Corrected, Unsupported or Unresolved. Write the exact repair, removal or clarification request in the final column. None is a valid action for an unchanged supported claim.
8. Rebuild the final paragraph from the correction column and save it alongside your table. Keep step-free access pending; remove the refreshments promise. Compare with claim-table-answers.csv and checked-revision.md only after attempting the work.

Supported means opened evidence matches. Corrected means a replacement is documented. Unsupported means no adequate support is provided. Unresolved means evidence is incomplete or inconclusive; it does not mean false. In this fixed exercise, accessibility is Unresolved and refreshments Unsupported because those are the distinct decision labels taught in the source lesson.

Checks: eight independent rows; every row has an inspected source, precise evidence, result and action; totals Supported 3, Corrected 3, Unsupported 1, Unresolved 1; 36/48 = 75%; no Riverside Room, 70%, 22 October deadline or refreshments promise in your checked revision. Pending access stays explicit.

Manual fallback: copy the six headers onto landscape paper. Open or print the three evidence records, count registrations and use any calculator. Show the calculation and cross-references. Save the table with the checked artifact. No completed venue check is implied.

Optional maintainer check: with Python 3 installed, run `python3 check_pack.py` from this extracted kit directory. It checks supplied fixture consistency only, never your judgement or actual app display. Expected output is a JSON object with passed true, registrations 36, capacity 48, percentage 75 and the four result counts. The learner exercise does not depend on this command.
