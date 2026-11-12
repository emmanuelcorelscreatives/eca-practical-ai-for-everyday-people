# Check Citations Against the Original Page — lesson 105

Emmanuel Corels Academy. These are self-authored fictional practice materials, not an actual garden policy or recorded assistant session. The kit matches the saved lesson example; no account, subscription or network access is required to complete the manual fallback.

## What to open

- `Community Garden Access Notes.pdf`: original, searchable 12-page source. The exact garden quotation is on **viewer page 2**. Viewer position 6 has the separate **printed Page 5** example.
- `source-record.json`: exact filename, origin, received date, version and page-location facts.
- `worksheet.csv`: fillable source-check table with a separate Interpretation field; do not place interpretation inside the quotation field.
- `numbering-check.csv` and `numbering-answer.csv`: separate location-record exercise and expected viewer-position/printed-page result.
- `Community Garden Access Notes - scan.pdf` and `scan-page.png`: the same access paragraph as image-only practice evidence.
- `ocr-draft.txt`: deliberately introduced `hours` → `ours` mistake, not actual OCR output.
- `answer-key.csv`: expected judgments; consult after doing the checks.
- `source-text.txt`: accessible text counterpart for this authored source. For the OCR exercise, inspect the image rather than trusting this companion.

## Exercise

1. Record the file origin, received date and version. Add only the original searchable PDF to a source notebook or document-capable assistant if one is available. Never upload private files for this exercise.
2. Use this exact instruction: **Answer only from Community Garden Access Notes.pdf. Quote the relevant passage exactly, give its page location, and label any explanation as interpretation. If the file does not answer, say so.** Ask what the note says about access.
3. Keep the actual response separate from the source. A practice answer may contain `Claim`, `Quotation`, `Location` and `Interpretation`, but do not pretend that a supplied example is an actual model response. The expected exact quotation is: **The garden welcomes residents during scheduled volunteer hours.** An interpretation such as “This suggests access is not unrestricted” is not another source quotation.
4. Open viewer page 2 of the original. Search `scheduled volunteer hours`, compare the quotation word by word and read the whole surrounding paragraph. Record that hours are scheduled, some activities are supervised and the statement is a committee recommendation.
5. Evaluate the deliberately overbroad claim **The garden is open to all residents every day.** Mark it unsupported as written. Correct it using the exact narrower source sentence; do not invent the schedule.
6. Evaluate **The city requires this schedule.** Mark that stronger attribution unsupported. The note identifies a committee recommendation, not a city requirement.
7. Open viewer position 6. Confirm the footer says **Page 5**. Record both numbering systems, filename and a distinctive phrase in `numbering-check.csv`; compare with `numbering-answer.csv`. This is a separate numbering demonstration; do not move the page-2 quotation to page 6.
8. Open the image-only scan. Searching may return no match. Inspect the image or thumbnails; absence from text search is not absence from the page. Compare `ocr-draft.txt` against the image and correct **ours** to **hours**. Treat the draft as a controlled error example; if you run OCR yourself, record the real output separately.
9. Fill all rows of `worksheet.csv`, then compare with `answer-key.csv`. Leave unresolved claims explicit.

## Manual fallback and expected completion

If no assistant is available, write the claims from steps 5–6 directly into the worksheet and inspect the supplied original. Complete exactly the same evidence checks. A successful worksheet separates document evidence from interpretation, preserves the scheduled/supervised qualifications, rejects every-day and city-requirement additions, records page 2 correctly, records viewer 6 / printed 5 separately and corrects the OCR draft against the image. The activity does not require a confidence score or an invented live result.

Run `python3 check_materials.py` from this folder for source/inventory checks; Python standard library only. The builder requires ReportLab and Pillow only if you choose to regenerate the authored PDFs. No exercise command contacts an external service.
