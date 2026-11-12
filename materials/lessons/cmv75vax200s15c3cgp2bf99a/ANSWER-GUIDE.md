# Expected checks and answers

The source reads:

- COMMUNITY WORKSHOP
- 18 November 2026
- 14:30
- Room B07
- Fee: €12.50
- Reference: OCR-8B01
- Bring photo identification.
- Cancellations accepted until 12 November 2026.

The authored error fixture changes `OCR-8B01` into `OCR-8801`: B has become 8. Both are orderly-looking strings, but only the original identifies this fictional record. It also deletes `until` from the cancellation sentence. A visible date alone does not preserve that condition. Restore each only by pointing to the matching source image text.

Keep 18, November and 2026 separate while checking the date. Check `14`, the colon and `30` for time. Room B07 contains B, zero, seven. The fee is twelve euros and fifty cents; preserve the euro symbol, decimal point and both decimal digits. The reference is uppercase OCR, a hyphen, eight, B, zero, one. Preserve source notation before any regional formatting changes.

A completed worksheet must include all seven fields and both small-print sentences, with the original image retained and raw output separated from corrections. The supplied actual Tesseract extraction is evidence only of that engine on that PNG; it is neither a phone workflow screenshot nor an endorsement. There is no universal exact OCR output to assume for a different device.

The notice is Academy-created fiction. Its dates, price and condition are pedagogical source values, not a real appointment, purchase or legal/financial instruction. A checked transcription does not verify the notice's authority or freshness.

## Measured local OCR disagreements

The retained Tesseract run read Room `BO7` instead of source `B07`, and `OCR-8BO1` instead of source `OCR-8B01`: those are letter O in the zero positions. This measured result differs from the deliberately authored B-to-8 error fixture. Compare both directly with the unchanged source; do not treat either fixture or an engine result as ground truth.
