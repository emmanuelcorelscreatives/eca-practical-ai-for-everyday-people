# Lesson 123 — Build a Realistic Weekly Plan

Emmanuel Corels Academy · Practical AI for Everyday People

All records are fictional Academy practice data. Nothing in this kit has been saved to a calendar or sent to an assistant. Keep your personal commitments private. This is a time-planning exercise, not advice about health or care duties.

## Work through the example

1. Read `available-windows.csv`. These windows remain AFTER fictional fixed work, care, travel, a Wednesday appointment, meals, recovery and other unavailable time. Precise fixed-event times were not supplied by the lecture; do not invent them or infer that every blank calendar cell is available. Wednesday has no workable window.
2. Total the six windows in minutes, convert to hours, and subtract an adjustable two-hour buffer. Explain when your own buffer might differ.
3. Read `requested-and-selected-tasks.csv`, initially looking only at requested minutes. Compare the requested total with usable capacity BEFORE asking for a schedule.
4. Copy the prompt in `assistant-prompt.txt` to a suitable assistant only if you choose. The example is a draft, not a verified model response or an external action. An assistant is optional.
5. Make your own priority choices. The lecture defers the 3-hour personal project and reduces cleaning to one essential hour. The second cleaning hour is removed scope, not completed work. Study, groceries, laundry and administration remain protected.
6. Inspect `reviewed-draft.csv` and `capacity-allocation.csv`. Check every start/end time and duration. Saturday has a 30-minute gap between groceries and the family call. That known transition is not counted as protected uncertainty buffer. The two-hour buffer is reserved separately on Monday 20:00–21:00 and Sunday 17:00–18:00. One hour of usable capacity remains unassigned to flexible tasks: Friday 19:30–20:00 plus Saturday 11:30–12:00 (the visible transition).
7. Compare your answers with `expected-checks.md`. Run `python3 check_plan.py` if Python is already available; the manual arithmetic below is sufficient and no software installation is required.
8. Open `weekly-capacity-planner.html` locally in a modern browser. It is an Academy self-created offline worksheet, not an account-connected service. Choose the teaching state from its menu. The Calendar form is a draft rehearsal: its save action is intentionally disabled, and no calendar events are created.

## Try your own fictional variation

Use `blank-plan.csv` to build another week with fewer available hours. Keep fixed commitments outside the available windows. Pick a buffer and priorities, leave deferred work visible, and calculate before scheduling. Check overlap, transition realism, visible unscheduled tasks, and planned work ≤ usable capacity. Do not submit real personal calendars with this exercise.

## Manual fallback

Write the same windows and tasks on a blank page or a plain digital table. Subtract the buffer, then schedule priorities only while capacity remains. Keep deferred work separately visible. No assistant, app connection or account is necessary.

## Before a real calendar entry

After your own review, manually check title, actual date, start, end, time zone, recurrence and reminder in your chosen app. This example deliberately supplies weekdays rather than real dates and does not select a personal time zone. Verify those missing fields yourself before any real save. A generated table and a saved event are different things; a visible event does not prove a reminder exists.

## Files

- CSV inputs, selected plan and capacity allocation: reproducible lecture arithmetic.
- `assistant-prompt.txt`: optional complete fictional input and constraints.
- `expected-checks.md`: worked answer and deliberate error exercise.
- `check_plan.py`: standard-library offline validation, no networking.
- `weekly-capacity-planner.html`: real self-created local interactive teaching worksheet; no real assistant/calendar integration.
- `blank-plan.csv`: editable personal-practice template; do not upload private versions.
- `LICENSE.txt`: Academy-created content permission.
