# Lesson 201 — Handle Approve, Reject and Edit Paths
Emmanuel Corels Academy · Practical AI for Everyday People

This is a self-authored platform-neutral training simulator. Riverside Reading Day, its records, date and decision timestamps are fictional practice material. Organizer-supplied values are not independently verified. Permission is confirmed only for this simulation. Nothing is posted, sent, purchased or deleted; no accounts, network requests or credentials are used.

## Start without installing a platform
Open `simulator.html` in a browser. Choose a lesson panel, then use the record selector and **Run selected record**. The four main cases match the narrated demonstration: A-001 approved and unchanged, A-002 rejected for a missing start time, A-003 edited v2 and unreviewed, A-004 blank and pending. Further A-005–A-009 cover unknown decisions and changed destination/content/attachments/version. The app uses preset teaching fixtures; its draft is supplied example text, not live AI output.

Only a recognized approval for the exact reviewed version, destination, content and attachment set reaches the **simulated** action log. The real Publish control is permanently disabled. An approved example demonstrates routing, not factual validation: its missing start time remains unresolved, so do not use it as permission to publish a real announcement.

## Practice
1. Inspect Input and Draft. Record the supplied event name and proposed date, missing time, draft label, proposed action and authorized destination. Do not invent a venue, price, booking link or accessibility claim.
2. Run A-001. Confirm the unchanged v1 record reaches only a simulated action. Inspect Run history.
3. Run A-002. Check the reason is preserved, the archive path is selected and the action is **not reached**. A rejection notice alone would be insufficient if the action path remained connected.
4. Run A-003. Compare read-only reviewed v1 with editable v2. The added 10:00 is explicitly an assumption without confirmation; v2 requires new evidence and fresh review, with no inherited approval.
5. Run A-004 and A-005. Blank stays pending; an unexpected value goes to manual review. Neither defaults to approval.
6. Try A-006–A-009. For each, identify the changed field that invalidates earlier approval. Only one outcome may occur per record.
7. Complete `decision-log-template.csv` for the main cases using only the fictional role, timestamp, decision, reason, reviewed version, destination and supporting reference. Avoid unnecessary personal data.
8. Use the manual-folder fallback below. Verify the rejected item cannot enter the action log and retain its reason. If the file/version match is unclear, stop and complete the task from the original material manually.

## Manual folder fallback (Windows)
Run `prepare-manual-queue.ps1` with PowerShell in a new Academy practice directory. It refuses an existing destination and creates only its own new numbered folders, two clearly fictional records and a CSV decision log. It makes no changes to other files. Open that destination in Windows File Explorer. Observe A-002 in **03 Rejected** and only A-001 in **05 Simulated Action Log**; the latter is a simulated record, not a real publication. Folder names alone do not enforce workflow safety: keep movement manual, check the logged decision and exact version first, and do not automate copying from rejected/changes-requested folders into the action folder.

## Check your results
Python 3 is optional: `python check_routes.py` runs nine fixtures, two unknown-value checks and 25 incomplete-field checks, and `python route_engine.py` prints actual local routing results. The browser applies the same rules, requiring explicitly present, nonempty string version/content/destination fields and present arrays of nonempty attachment references (an explicitly empty array is permitted). Missing or malformed fields block approval. Rejection preserves a local decision/archive record including the reason and a clearly simulated owner-notification trace; no actual message is sent. Click Run history to inspect these outputs. Compare results with `expected-results.csv`. One simulated action, eight blocked/pending/review outcomes and zero real external actions are expected. These tests check routing behavior, not truth of supplied event facts.

Final check: action/destination/content/supporting information opened; assumptions visible; permissions confirmed; reviewed version matches; rejection stops; edits return for review; unknown values stop; manual fallback documented. Keep real external actions disabled while practicing. Next lesson: **Recheck Changed Content Before Action**.
