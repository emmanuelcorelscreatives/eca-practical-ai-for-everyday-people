# Lesson 127 — Read and Summarize Routine Documents
Emmanuel Corels Academy · Practical AI for Everyday People

These original fictional practice materials preserve the lecture’s Maple Court example. They are not a real notice, real resident data, legal advice or evidence from an external AI system. All model/OCR error examples are deliberately seeded training fixtures, never claimed live observations.

## Run the exercise
1. Open `Maple-Court-Notice.pdf` and confirm both pages are present. The authoritative text is also in `source-pages.json`.
2. Compare `ocr-unverified.txt` with both originals; locate the deliberately incorrect deadline and closure time. Correct only against the source.
3. Open `Training-Workspace.html` in a modern browser. Use Source/Previous/Next, Capture Check, OCR, Privacy, Assistant, Checked extraction, Summary and Register. Its prepared fixtures illustrate review; it does not call an AI/OCR service, upload files, send messages or create calendar events.
4. Fill `manual-extraction.csv` without copying the answer. Preserve the exception, alternative, prohibition and unresolved question. Check against `checked-register.csv` and `checked-summary.txt` only after doing your own review.
5. Run `python3 verify_records.py` (Python 3 standard library) for exact fixture checks and deliberate negative cases. This checks the prepared files, not a user's real notice.
6. Apply the method to `practice-notice.md`; compare with its answer checks at the bottom only after working.

## Why the exception matters
The source says only people whose telephone number, email or preferred contact method changed must respond by 23 October 2026. If nothing changed, no response is required. The closure on 19 October 10:00–12:00 requests no task. Do not turn it into an instruction to contact someone. The issuer’s text does not resolve whether an unchanged email should be repeated when only a phone number changed.

## Privacy and alternatives
Use fictional/permission-cleared documents. Inspect every page, date, time, identifier and faint line. Review the actual chosen tool’s sharing, retention and account settings before any real upload; do not infer privacy from this offline exercise. For sensitive documents, use suitable local recognition or manual transcription. Keep originals separately from checked summaries. A citation/page label is a route to evidence, not proof of correctness.

Training Workspace deliberately stores changes only in its current browser session. Reload resets the training state; navigation between tabs preserves manually transferred rows. Prepared lecture views (`?scene=...`) are visibly labeled answer demonstrations, never your completed verification. Downloading a CSV is a separate local user action. Its sample output labels identify prepared examples, not live generated answers. The default practice view starts with unchecked Capture/Final checklists, no manually verified rows and an empty register. Confirm rows against their source pages before transferring them. Browser appearance and real OCR/assistant capabilities vary; no Windows/Android runtime claim is made by these materials.

All documents and example data are original Emmanuel Corels Academy educational material under CC BY 4.0. Code/HTML is MIT licensed. Permissions apply to this kit, not third-party software.
