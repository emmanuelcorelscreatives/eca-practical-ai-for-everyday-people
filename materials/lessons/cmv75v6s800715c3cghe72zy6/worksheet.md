# Add Placeholders and Input Requirements

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 8, Lesson 44

These supplemental practice materials match the saved lesson. All event details are fictional, not a real invitation or a verified schedule. No account, purchase, publication or external action is required. Files are ordinary UTF-8 text; use any notes app or document editor. Keep your existing prompt filing system.

## Practice

1. Read `blank-master.txt`. Identify the permanent task, changing inputs and reusable output requirements. Square brackets are a human visual convention, not a universal technical command.
2. Duplicate the blank master. Keep the original blank. Fill every required input using `fictional-event-inputs.json`, or compare with `filled-practice-copy.txt`.
3. Search for an opening square bracket. The completed copy should have none. Then check every required input for meaning: deleting a bracket label does not supply a fact.
4. Mark an unknown optional value “not provided”. Never silently fill it with a guess. Try making contact unknown; the supplied registration instruction can still form the ending.
5. If an assistant is available, submit the completed copy. Label its actual response “Generated draft — not event evidence”, retain it separately, and trace every event detail to the inputs. Product features and account availability vary. The sample in this kit is HUMAN-WRITTEN, not a claimed assistant result.
6. Submit the separate `missing-date-copy.txt` if available. Expected behavior: ask for Event date and produce no announcement. Record what your assistant actually does; an unexpected draft is a failed requirement, not evidence that the missing fact was supplied. Manually stop and ask for the date if necessary.
7. Without an assistant, use the completed copy as a human writing brief. Write your own announcement or inspect `human-written-practice-announcement.txt`. The same input checks still apply.
8. Give only the blank master to another learner. Ask them to identify required and optional fields and explain what happens when information is missing. Revise unclear field labels without changing the task or filing system.

## Expected checks

Required fields: event name, event date, start and end time, location, purpose. Optional fields: cost, registration, what to bring, contact. A blank required input must stop drafting. Unknown optional fields should be explicit. Keep assumptions visible and never present them as event facts; asking for a missing fact is preferable here.

The complete fictional copy supplies Community Repair Café; 7 November 2026; 10:00 to 13:00; Riverside Community Hall; helping neighbors repair portable household items; free entry; registration not required; one portable household item; events@example.org. Compare the exact meanings, not merely word overlap. Do not introduce repair guarantees, accessibility arrangements, eligibility rules, staffed services or other unsupported facts. Before publishing a real event, confirm changing details with its organizer.

The announcement requires one heading, 80–120 words, welcoming plain language and an ending based on supplied contact or registration instructions. The human-written sample has 85 whitespace-separated words including its heading; this is a checkable formatting example, not proof of an assistant's reliability.

Optional local verification for someone comfortable running Python: `python3 check_materials.py`. This checks the supplied fixtures only. It does not validate real-world facts, judge arbitrary generated prose, or certify a video.

Next lesson: Include a Quality Check in Every Template. This kit focuses on placeholders and input requirements, not replacing that lesson.
