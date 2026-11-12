# Lesson 126 — Check Before Adding Calendar Events
Emmanuel Corels Academy · Practical AI for Everyday People

## Run the safe exercise
Open `calendar-practice.html` in a modern browser. It is a self-created, offline practice app: no accounts, network requests, real invitations or actual calendar writes. It does not impersonate a commercial calendar. Use the step selector and Next to follow the authored lesson. The assistant draft is a fixed, explicitly labeled practice fixture, not a live model response. Reset returns to step 1 and clears the simulated saved record, invitations and action status. Selecting a later lesson step does not create a saved event: the Saved event view requires an actual local Save privately action or confirmed invitation simulation.

Editable calendar, title, date, start/end time, all-day, recurrence interval/weekday, link and permission fields retain your entries while navigating lesson steps. Final review shows those actual entries; saving snapshots them only after the reviewed fields agree with the organizer source, so later edits do not rewrite the saved record. Reset clears draft edits, destination-fixture observation and saved records. The named-zone, custom-repeat menu and unresolved end-choice controls are explicitly disabled teaching fixtures, not discarded input. The organizer-confirmed end date is fixed for this exercise. Deliberately change a title or permission and navigate to final review: the mismatch must remain visible and both actions must be blocked. Restore the confirmed source values, open the step-65 local destination fixture, then save privately. Change the draft title afterward and verify the Saved event view still shows the original submitted title. Reloading the page starts a new session.

Read `original-note.txt` before opening `organizer-confirmations.md`. First list missing facts. Ask an assistant, if available: “Turn this note into a proposed calendar entry. Label assumptions and missing information. Do not save anything or invite anyone.” Do not supply private details. Alternatively organize the same fields manually.

## Work in order
1. Mark the proposed entry **Draft, not scheduled**. Compare every field to the original note.
2. Confirm destination calendar, title, exact date and weekday, all-day off, 3 PM rather than AM, and one-hour duration. Do not trust whichever account opened by default.
3. At the unresolved zone stop, draft a clarification asking for a city or named time zone. Reveal the organizer confirmation and set Europe/London. Compare event versus display zone; Asia/Singapore displays 11 PM to midnight next day on 18 November, without changing the intended London event.
4. Set a two-week Wednesday pattern, starting 18 November 2026. “Through March” is not an ending rule. Stop again; reveal the exact final-date confirmation, 24 March 2027. Inspect first, intermediate and final occurrences in `expected-occurrences.csv`.
5. Keep method Online and link empty until supplied. Review a 15-minute reminder separately from invitations.
6. Treat names as insufficient addresses. Compare all three confirmed example.com addresses exactly; check modify off / invite others off / view guest list on.
7. Use the app review states. Before the link is supplied, both Save actions must be blocked. At step 65 click Open local destination fixture and inspect its Community garden planning call heading. It is actual offline practice software representing the supplied reserved example URL, not a real meeting service.
8. At final review select Save privately: observe local simulated Saved status without invitations. Reset, then select step 65, open the local destination fixture and select step 66, choose Save and invite, inspect the separate three-guest dialog, cancel once, then confirm. Observe **Invitations recorded in simulation**, never real messages sent.
9. Examine the recurrence preview and the distinct “This event” versus “Entire series” choices. This demo displays scope choices without editing a real calendar. In a real app, read its exact external-notification wording before any action.

## Submit
A completed checklist, your missing-information questions, ten occurrence dates, the event/display-zone comparison, and two sentences explaining why draft, private save and invitation are different. Never include personal contacts or private calendars.

## Manual fallback
Use `review-checklist.csv` as a text/spreadsheet checklist when no assistant or calendar is available. Mark unresolved fields; do not proceed until required information is confirmed. A polished draft is not evidence of a saved event.

## Validation
Run `python3 validate_fixture.py` beside the files (Python 3.9+). It checks the weekday, ten biweekly dates, correct endpoint and regional-zone conversion with the standard library. It makes no network request. Compare your answers with `answer-key.md` after completing the exercise.
