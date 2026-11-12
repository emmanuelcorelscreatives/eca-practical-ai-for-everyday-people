# Lesson 170 — Read Text from an Image

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 29

Practice extracting printed text and checking digits, dates and small print against the original. This kit matches the saved lesson's exact **self-created fictional Community Workshop notice**. It does not announce a real event or invite payment. All sample content is Academy-authored and contains no private data.

## Start

1. Open `notice-original.png` or print `notice-original.pdf`. Keep the original unchanged. The text-only `notice-original.txt` is a reference, not a replacement for inspecting the image.
2. Use a supported camera/gallery/OCR option on your device. Names and availability vary: Text, Copy text, Scan or Live Text. The lecture illustrates Google Photos/Lens; these supplied files do not claim to be captures of that app or to reproduce an Android session.
3. If photographing the print, flatten it, light evenly, avoid glare, keep the camera parallel and focus. Inspect all edges and the complete small print before extracting.
4. Paste the result into an editable note, preserving line order. Save this raw version separately.
5. Complete `worksheet.csv` using the exercise below. Keep the source image beside the note and compare each critical detail directly.
6. Compare your result with `answer-key.csv` and `corrected-checked-note.txt` only after your own check.

## Files and evidence

- `notice-original.png`, `.pdf`, `.txt`: the unchanged fictional source.
- `notice-small-print.png`: exact crop of the original, not newly invented wording.
- `notice-blurred-training.png`: deliberately degraded derivative for input-quality discussion; not a photograph or failed device result.
- `intentionally-faulty-extraction.txt`: **deliberately authored error fixture**, not measured OCR output. It contains the two exact near-miss types discussed in the lesson.
- `tesseract-actual-output.txt`, `ocr-execution.json`: actual local Linux Tesseract extraction of the exact original PNG, with engine, command and hashes. This is a separate reproducibility example, not Google Lens output and not a promise every engine will agree.
- `worksheet.csv`, `answer-key.csv`: editable learner table and checked expected details.
- `EXERCISE.md`, `ANSWER-GUIDE.md`: tasks, check order, limits and manual fallback.

No additional software or account is required to complete the manual comparison. A text editor, image viewer and magnification are enough. Use only material you own or have permission to process. Check app access and service handling before uploading any private image.
