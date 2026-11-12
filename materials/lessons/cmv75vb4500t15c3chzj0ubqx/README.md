# Lesson 176 — Build Answers to Repeated Questions

Emmanuel Corels Academy: Practical AI for Everyday People. This complete self-authored fictional Repair Café exercise matches the lesson. All people are role labels; no real inbox, customer data, organization or external action is represented.

## Start without AI

1. Read `approved-sources.md` and `source-register.csv`. S1/S2 are scenario-approved public material; S3 is internal.
2. Open `questions.csv` in your spreadsheet. Retain the question wording and count. Group “Must I reserve?”, “Can I just arrive?” and “Is registration required?” under the booking question. Keep reserving a specific repair time separate: it requires different facts.
3. Copy `tracker-template.csv` and draft one answer at a time from the opened sources. An assistant is optional: use `drafting-instruction.md` if available. Never paste confidential content.
4. Check the booking condition and toaster certainty. Preserve gaps in fees, parking and the phones policy. Record decisions and routes.
5. Compare with `reviewed-tracker.csv` and `answer-key.md`. The answer key is a fictional worked example, not independent confirmation about a real event.
6. Publish only scenario-approved answers into a local document like `reviewed-faq.md`; do not actually post/send the example. Check the final exported file at phone and desktop size for clipping, complete conditions and a visible escalation footer.

## Included workspace

Open `workspace.html` in a modern browser; it is the course’s self-created FAQ Review Workspace teaching prototype, not a commercial product. It works entirely offline, reads no account and sends no data. Each selector displays a saved training state; review decisions update the local page only. It does not send messages, operate a real AI model or approve a real policy. Use Print / Save as PDF to inspect an actual export. Source and CSV remain the authoritative scenario evidence.

## Reproduce checks

Run `python3 check_materials.py` (standard library only). The checker verifies six questions, the 3/1/1/1 reviewed status summary, three approved public answers, preserved conditions, source IDs, two Unanswered evidence rows and absence of guessed fee/phone answers. This is a local data-integrity check, not a substitute for your source review.

## License and privacy

Self-authored training material under CC BY 4.0; code under MIT. Fictional dates and approvals are labelled. No actual contact address, private source, account data or secrets are included.

Evidence status and the review-outcome dashboard are different: both fees and parking lack evidence; parking is Returned for edit, while the fee request is the dashboard’s Unanswered outcome.
