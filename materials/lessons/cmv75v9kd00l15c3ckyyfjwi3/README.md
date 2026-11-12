# Turn Receipts into a Checked Register — lesson 128

Emmanuel Corels Academy. All receipts are self-authored fictional examples, not actual purchases. No real vendor, address, payment identifier or private record is used. Source SVGs are authored masters. The three JPG exports are the fictional original receipt images for this exercise; all edges and printed fields remain visible.

## Practice files

- `original-source/`: untouched source masters, one per fictional receipt. Preserve these and the exported originals.
- `receipt-facts.json`: teaching-example facts and provenance, including printed/normalized dates and separate currencies.
- `register-blank.csv`: eight exact authored lesson fields, with one row per receipt.
- `register-candidate.csv`: deliberately authored candidate errors from the lesson. These are NOT claimed as actual output from Google Docs or any live OCR product.
- `register-checked.csv`: expected result after comparing every field to its own receipt image; no aggregate sum.
- `check_materials.py`: standard-library validation of dates, labels, source references and arithmetic.

## Complete the check

1. Preserve every original. Inspect working copies for upright orientation, sharp digits, complete edges, even light and absence of unnecessary identifiers. If you practice with your own receipts later, redact only working copies and protect originals according to their purpose and applicable policy.
2. If using Google Drive/Docs, upload only these fictional practice images into a newly created private `Receipt practice` folder. Open an image with **Open with → Google Docs** when that function is actually available. Interface/account requirements can change. Real product screenshots require the real signed-in product; never imitate its UI.
3. Save your actual OCR output separately. It may differ from these deliberately authored error cases. Phone text recognition, a PDF/document tool or manual entry are valid alternatives. Request only the printed transaction date and final total; do not infer missing characters or labels.
4. For the controlled lesson exercise, open `register-candidate.csv`. The first candidate is **13.30 EUR**, but the original says **TOTAL €18.80**. Compare image → extracted text → cell. Preserve `14/10/2026`, normalize to `2026-10-14`, correct the total and note **OCR read 8 as 3.** Mark **Checked and corrected** only after both date and total have been checked.
5. Receipt two has **SUBTOTAL CAD 24.00**, **TAX CAD 2.40** and **TOTAL CAD 26.40**. Select the final TOTAL, not the cleanest-looking amount. Preserve the candidate result separately. The printed **DATES: DD/MM/YYYY** resolves `03/04/2026` as **3 April 2026**, normalized **2026-04-03**. Without reliable order evidence, leave the normalized date blank and mark it ambiguous.
6. Receipt three's candidate date is uncertain. Initially leave both date fields blank; keep the clear total **1240.00** and currency **INR**, with **Needs review**. Enlarge the original without editing it. The printed date **08 OCT 2026** can be read manually; preserve it, normalize to **2026-10-08**, note **OCR date unreadable; entered from enlarged image.**, and mark **Checked manually**. If still unclear, leave it unresolved.
7. Audit all three rows against their own originals. Read the exact amount/currency pairs **18.80 EUR**, **26.40 CAD**, **1240.00 INR**. Use numeric totals with two decimal places, dates in resolved year-month-day order and a separate text currency column. Do not sum different currencies. This exercise checks records, not accounting or financial decisions.
8. Confirm every source filename matches an existing original. Keep correction notes and actual OCR output. Compare your result with `register-checked.csv` only after your check.
9. Review cloud access and temporary copies. No material here asserts that a cloud copy was deleted or a real purchase occurred. Remove temporary copies only when no longer needed and authorized. There is no universal receipt retention period.

## Manual fallback

Enter printed dates and TOTAL amounts directly from the fictional images. Keep candidate/error examples clearly labeled; do not pretend a model produced them. Leave uncertain values blank until actual evidence resolves them. Every status is a record of your own verification, not proof merely because OCR returned text.

Run `python3 check_materials.py`. The complete kit includes all three JPG originals; the check verifies their presence. Source facts and candidate-stage assertions can be checked independently without a browser or account.
