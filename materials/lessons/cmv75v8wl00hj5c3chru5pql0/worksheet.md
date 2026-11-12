# Handle Scans, Tables and Poor OCR

Emmanuel Corels Academy • Lesson 107

This kit contains self-authored, fictional, permission-cleared practice records. It contains no private documents. The three-page original-scan.pdf is image-only; it deliberately has no selectable text layer. Keep it unchanged. PNG page images and their SVG authoring sources are supplied so the exercise remains inspectable without any vendor account.

## Practice

1. Record the SHA256 of original-scan.pdf with Python's hashlib or your platform's file-hashing utility. Copy it to a working directory; never overwrite the original. Try selecting a sentence in your PDF reader and compare with the PNG image. An OCR text layer in another document can still be wrong.
2. If your reader offers text recognition, run it on the working copy. Names vary by tool. Alternatively use the supplied actual Tesseract output in actual-ocr/. The file practice/deliberately-flawed-extraction.txt is separately labeled seeded teaching material; it is NOT claimed to be an OCR engine's observed output. No confidence score guarantees correctness.
3. Compare page 2 in small sections. Inspect B17 versus 817, the minus sign in -3.50, the omitted instruction, punctuation and note order. Preserve page/line references. The literal 4?7 is intentionally uncertain source content: do not resolve it to 477 from context.
4. On page 3, trace each value across its row and up to its header. Paper must have Units 12 and Rate 3.50; Folders must have Units 8 and Rate 4.00. The flawed practice extraction says Paper 3.80. Its cause is not proven by the value alone: inspect characters and structure rather than assuming a column shift. Keep meaningful blank cells blank in any future table.
5. Fill practice/correction-log-template.csv. Record page, field, extracted value, source value, status, reason and exact source location. Log confirmed values as well as errors. Keep your corrected organization separate from the original scan. Compare with answers/correction-log.csv only after completing your own review.
6. Use manual fallback for important fields when recognition is poor. Zoom in, transcribe only needed fields, and retain uncertainty. A source that cannot settle a character needs a clearer copy or the document owner, not a guess.
7. Only after verifying source values, calculate 12 × 3.50 = 42.00 and 8 × 4.00 = 32.00; total 74.00. Compare with the printed total on page 3. This is a separate arithmetic check, not proof that extraction was correct. Run python3 tools/check-practice.py to check the supplied references and PDF image-only structure.

## Completion checklist

- Original unchanged; working copy clearly identified.
- Page references retained for every important item.
- Names, dates, signs, units and row/column relationships compared directly.
- Unclear source items remain explicitly uncertain.
- Source verification and calculations documented separately.

Passing arithmetic alone is insufficient. The original image remains the evidence; this kit makes no claim of universal OCR accuracy.
