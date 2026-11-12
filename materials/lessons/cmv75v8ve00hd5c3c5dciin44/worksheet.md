# Extract Lists, Dates and Action Items
Emmanuel Corels Academy — Practical AI for Everyday People, lesson 106.

All names, dates and events in this kit are fictional and self-authored. No private data is needed. Open `community-garden-planning-notes.pdf` (exactly two pages); `source-pages.txt` is an accessible copy. Do not upload confidential files.

1. Copy `blank-extraction.csv`. Use `prompt.txt` with a document-capable assistant if accessible; otherwise read and copy passages manually. Tool availability varies; no paid tool is required. Label generated rows Unverified.
2. Extract the list item, all three dates, and the actions. Preserve exact wording; keep original and normalized dates separate. Do not infer a year or whether 03/04 is day/month or month/day. Mark these Needs clarification.
3. Open each claimed source page and section. In particular, find “Please confirm table delivery.” on page 2. A nearby name does not establish ownership. Preserve Mina only for her own stated action.
4. Work from each source page back to the table to detect omissions. The small-print meeting date must not disappear. Use Found, Missing, Duplicate, Ambiguous or Wrong association for each relevant passage. There is no third page in this packet; a generic three-page checklist does not prove a third page exists.
5. Compare the two reminder mentions. Their explicit same-event context supports merging into one row with BOTH locations. Two similar instructions for different events would remain separate.
6. Repair `deliberately-faulty-output.csv`: unsupported owner, invented deadline, wrong source and duplicate reminder. It also omits the list, Mina's actual action and all dates. This file is a deliberately authored teaching error, not a real assistant transcript.
7. Inspect `ocr-error-example.txt`, which is a labeled simulated error rather than a measured OCR result. Compare the actual page-2 printed date before making a correction. If your own source image is unreadable, retain uncertainty and request a clearer source; do not guess.
8. Compare with `expected-extraction.csv` only after your own check. Accept equivalent row splitting if every source passage and association remains traceable. Keep “Not stated” for unsupported owners/deadlines.

## Expected checks
There is one Materials list item, three date mentions and three distinct actions. The reminder has two source locations but one distinct action. Mina is responsible only for bringing labels. None of the three actions has an explicit deadline. The table-delivery owner is Not stated. The source has no year and no date-order convention for 03/04, so no complete ISO date can be justified. Review-status counts are examples for this supplied packet, not evidence of an assistant's real performance.

## Manual fallback
Open both pages, copy each relevant passage into the blank CSV, add page/section and review status, then run the same omission, duplicate and association checks. Save the original packet and unresolved questions alongside your result. A citation is useful only after its location is inspected.

## Optional interactive source workspace
Open `Academy-Source-Notebook.html` with its adjacent PDF and PNG files; follow `workspace-guide.md`. Its real page links, actual local file attachment, source highlight, duplicate decision and editable manual table let you practise the same checks. Its genuine recorded model response is unverified; its final answer table is separately author-checked. Local edits reset on reload; save durable work in your CSV.
