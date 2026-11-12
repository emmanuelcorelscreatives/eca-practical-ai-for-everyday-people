# Lesson 132 — Build a Monthly Admin Routine

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 22

Practice collect → extract → verify → file, keeping uncertain items visible. Every document in this kit is self-authored fictional training data. No real organization, purchase, payment, deadline, or external action is represented. Dates, totals, references and filenames match the saved authored scene prompts and the spoken values. They are fictional practice particulars, not facts about real documents.

## Start locally

Unzip the complete kit into a writable folder. Open `Admin Routine/Monthly_Admin_Register.xlsx` in your spreadsheet application, or import `starter-register.csv`. Keep `Originals` untouched. `01_Inbox` starts with four copies: three ordinary documents and one intentionally incomplete notice. Folder names 02_Reviewed, 03_Filed and 04_Exceptions may be created if your ZIP extractor omits empty folders. The expected workbook is a separate answer key, not the starter.

Read each original before extracting. Confirm permission and tool suitability before any upload; this exercise works entirely locally. If OCR is unavailable, type fields manually. `ocr-draft-fixtures.json` is an intentionally authored practice draft, not an observed model result. Keep draft text separate from evidence.

## Exercise

1. Record one row per inbox item and mark it Unverified. Include its filename, document date, type, organization, total where relevant, requested action/deadline, reference, status and notes.
2. Compare Northlight's 2026-09-03, 48.60 and NS-1042 directly with the JPG. Mark Verified only after this comparison.
3. Read Cedar's PDF, including the exception paragraph. Record issue date 2026-09-11, response due 2026-10-18, reference CHA-2048 and action Confirm attendance preference. Leave Total blank with a note 'not applicable'; do not invent zero. The original course's exception wording was unavailable: this kit supplies a clearly labelled NEW fictional exercise paragraph about not duplicating an existing confirmation. It is not recovered course evidence.
4. Compare Riverbend's draft with its original: correct 78.20 to 73.20 and RR-771g to RR-7719. Keep both corrections in Notes. Preserve the original scan.
5. Preview descriptive names for copies: `2026-09-03_Receipt_Northlight-Stationery_NS-1042.jpg`, `2026-09-11_Notice_Cedar-House_CHA-2048.pdf`, `2026-09-27_Receipt_Riverbend-Repairs_RR-7719.jpg`. Use 02_Reviewed for working copies, then 03_Filed/2026/2026-09/Receipts or Notices. Adapt names only for actual storage restrictions; preserve traceability.
6. Update each source link to the actual filed copy, open it, compare the document and row, and record the test. The answer-key workbook contains source filenames as text, not pretested clickable links. Add links to your actual copy locations; no path test is claimed.
7. Do not guess the cropped deadline in Unclear_Notice_Scan.jpg. Record Deadline missing, status Exception, next action Obtain complete page, review date empty; move its working copy to 04_Exceptions.
8. Finish only when 01_Inbox is empty and each of the four items is either verified/filed or an explicit exception with next action. Do not mark an uncertain record verified to empty the inbox.

## Check your result

See `expected-register.csv`, `expected-register.xlsx`, `CHECKLIST.md`, and `ANSWER-KEY.md`. `verify-kit.py` checks selected exact CSV/draft values, expected/starter XLSX agreement with those CSVs, source-file existence and inbox/original duplicate hashes. It does not read the images or PDF, perform OCR, or test filed paths. It does not certify your OCR, your link tests, or your personal documents. Your own review is essential.

Keep records according to your applicable rules and actual needs; no fixed retention period is prescribed. Do not upload real private records merely to complete this exercise.
