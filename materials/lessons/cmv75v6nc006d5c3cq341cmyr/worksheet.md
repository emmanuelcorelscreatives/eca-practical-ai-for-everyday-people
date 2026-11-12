# Use Critique Without Treating It as Verification

Emmanuel Corels Academy • Practical AI for Everyday People • Stage 7, lesson 40.

All event names, brief, drafts and worksheet data here are self-authored fictional training material. No real event, private account, assistant execution, message, registration or publication is implied. These materials reproduce the saved lesson's example and do not amend its narration.

1. Open original-event-brief.md and weak-draft.txt. Identify what is source evidence and what is an intentionally faulty output.
2. Open comparison-blank.csv in your spreadsheet or use a text editor. In Calc, select comma as separator and UTF-8. Keep six columns. Do not import the generated critique into OPENED EVIDENCE.
3. Optional: use critique-request.txt with a suitable assistant, providing only the fictional brief and draft. If no assistant is available, use critique-example.md as a prepared teaching example or find issues manually. Never describe that prepared example as a real tool execution.
4. Record possible weaknesses. comparison-diagnosis-only.csv shows the intermediate state with evidence, status and correction deliberately blank.
5. Reopen the brief yourself. Copy the relevant source wording into OPENED EVIDENCE. Compare the date/day, registration, repair outcome, parking/accessibility, format and one-item quantity. Notice that the prepared critique omitted the last issue.
6. Assign plain statuses. CONTRADICTED BY BRIEF means the source explicitly conflicts; UNRESOLVED means this source does not establish the claim; REQUIREMENT NOT MET means a required instruction/format/limit was not followed. SUPPORTED is available for checked details such as 10:00–13:00 or the meeting room. Do not use numerical confidence as a substitute for evidence.
7. Write the smallest corrections. Parking/accessibility can be removed because unnecessary to this announcement. If needed, consult an appropriate authoritative source or organizer; do not infer the opposite from silence or invent a contact result.
8. After checking, optionally use revision-request.txt or revise manually. checked-revision.md is the prepared answer, not a newly observed generated response. Compare every retained detail against the brief and check heading, bullets, no new promises, and length ≤120 words.
9. Run `python3 check_materials.py` locally if Python is available. It checks supplied file consistency, weekday, row coverage, blank diagnosis evidence, and revision length. It does not perform AI truth detection, contact an organizer, or validate a real event. A manual fallback is to tick the six worksheet rows and count the revision's whitespace-separated words.

## Expected checks

Saturday 17 October 2026 differs from Sunday 18 October. Registration and repair guarantee are contradicted by the brief. Parking/accessibility remain unresolved rather than disproved. Paragraph layout and missing one-item limit fail requirements. The revision retains time, exact meeting-room location, deadline, quantity and no-guarantee qualification, omits unsupported promises and uses a heading and five bullets. Compare your completed sheet with comparison-answer.csv only after your own review.

## Scope and permission

Use this kit for learning; do not publish the event as genuine. Generated feedback is optional diagnosis. Opened evidence supports decisions. Human judgment approves the final result. The next lesson covers when to switch tools; this kit stays within critique versus verification.
