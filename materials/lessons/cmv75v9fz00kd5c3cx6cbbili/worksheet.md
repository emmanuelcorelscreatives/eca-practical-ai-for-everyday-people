# Lesson 124 — Plan Meals, Events and Household Tasks
Emmanuel Corels Academy · Practical AI for Everyday People

This self-authored fictional household exercise uses no private household data. It is a planning lesson, not a recipe, medical assessment, booking service or invitation system. Work in an offline notes editor or optional assistant of your choice; accounts and connected tools are not required. Do not upload private personal information. No tools in this kit create calendar events, invite anyone, share access, create tasks or buy anything.

## Start with the evidence
Read `household-brief.md` and `schedule-original.csv`. Mark each statement confirmed, assumed or unknown. In particular, at-home tea and second-adult help are assumptions, not facts. Quantities, preferences, equipment and fixed travel blocks cannot be silently changed.

## Ask for a bounded draft
Copy `assistant-prompts.md` into a chosen assistant, or manually fill `planning-template.csv`. Request separate confirmed inputs, assumptions, missing details, durations, dependencies, checklists and start/end schedule. Treat all output as a draft. `schedule-original.csv` is a deliberately faulty teaching fixture, not an actual model response or a usable approved plan.

## Find the conflict
Using the original brief, calculate required Tuesday departure. Compare cooking 17:30–18:10 with departure. Record the interval and duration that conflict. Check the 35-minute active-preparation limit separately: a 40-minute elapsed block does not by itself prove 40 active minutes; the supplied draft does not specify active time.

## Revise only Tuesday
Use the second prompt. Preserve Monday and Wednesday byte-for-byte in the supplied schedule fixture and preserve the school event plus both travel blocks. Cooking finishes by 17:35 or moves after 20:00. Compare with `schedule-revised.csv`: 16:45–17:20 cooking, 17:20–17:35 eating/packing, departure 17:40. Label ready-to-use ingredients as an assumption. Do not infer a helper is available.

## Audit resources and dependencies
Use `resource-and-dependency-check.md`. Verify vegetarian/no-peanut requirements, supplied ingredients, one burner and oven, and active time at most35 minutes. Unknown ingredient quantities and unspecified recipes mean feasibility remains provisional: this example is not a nutritionally complete meal prescription. Confirm quantities and safe preparation before action. Proposed shopping stays separate from confirmed supplies. Laundry must proceed wash → dry → put away; clean kitchen before setup. Event location, guest requirements and dessert source remain unresolved.

## Copy only approved work
Complete `planning-template.csv` with when/action/check. Use '?' for provisional items. Do not mark conditional event food or setup ready while required information is missing. In your own calendar or task app, inspect permissions and leave guest/sharing fields empty. This kit supplies no importable calendar file and performs no automatic external actions. A digital three-column note is the manual fallback; paper is optional for learners.

## Check and submit
Submit your conflict calculation, Tuesday-only revision, assumption list, dependency checklist and a clearly marked provisional/approved decision for each proposed action. Compare with `answer-key.md`. Optional local verification: with Python3 run `python3 check_schedule.py`. It reads only supplied CSV files and prints actual computed checks; it does not access any account or network. The expected result is in `answer-key.md` and an actual local run is supplied in `check-run.txt`.

## Next lesson
Lesson125, Revise When the Plan Changes, addresses disruption while preserving completed work and existing commitments. Do not solve that different exercise here.

## Supplied offline planner
Open index.html in a browser. It is an actual local scripted practice app, not a live assistant or connected calendar. Use the navigation to inspect the brief, compare the30-minute required-absence conflict, and apply the supplied Tuesday-only revision. The original and revised fixtures now explicitly include a provisional recycling placement and an unscheduled Wednesday leftover-meal proposal. These are teaching data, not approval of a recipe, adult availability, quantity or safe storage. Leave the leftover meal unscheduled until it fits before cleaning; do not silently move the saved Wednesday times. The local approval demonstration copies the fixed school/travel blocks and a birthday-tea start-only marker after an explicit click (no duration is invented); it never saves appointments, invites, shares or purchases. A checked review box is a review step, not evidence a chore is done.


## Check before approval
The fictional teaching brief gives Tuesday16:45–17:35, then after20:00. Cooking16:45–17:20 and eating/packing17:20–17:35 fit that window; departure17:40 leaves five minutes. This resolves the earlier generated cutoff discrepancy without changing the narrated example, fixed event/travel, Monday or Wednesday. Ingredient readiness, quantities, recipes, safe preparation and proposed helpers still need their separate checks; matching times alone is not approval.
Use confirmation-register.csv to record missing details, who could confirm them and the decision. Roles for unresolved items are proposed and unassigned. Only the fixed commitments/start marker can be copied locally; a local copy is not an invitation or completion.
The learner kit makes no claim that its exercise takes exactly12 minutes; final video duration follows native narration.
