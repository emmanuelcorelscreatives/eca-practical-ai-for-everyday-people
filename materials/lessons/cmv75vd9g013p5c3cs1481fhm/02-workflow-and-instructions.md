# Repeatable draft-and-check workflow, version 1.0
Purpose: create a clear event information sheet for attendees from approved evidence. Output remains a local draft until a responsible person finishes all checks. The tool never sends, purchases, posts or grants permission.

## Inputs and gate
Use one case's event name, date, venue, full schedule, accessibility details, contact route and permission status. Record source IDs and versions. Remove unnecessary private information. If a required field is absent, contradictory, uncertain or not permitted, list the problem and stop completion. Do not fill missing facts from another case or a model's memory. Tool availability varies; check your own account, plan, region, device, administrator settings and version.

## Reusable optional AI instruction
“Using only the approved source record I supply below, prepare a local event information-sheet draft with sections Event, Date and venue, Schedule, Accessibility, Contact and Review status. Preserve qualifications and uncertainty. Do not invent missing details, contact routes or evidence. If required information is absent or contradictory, list it and mark NOT COMPLETE instead of completing the sheet. Clearly identify the source ID/version used and separate any editorial suggestion from source facts. Do not send or publish anything. Source record: [paste only the one approved case record].”

Record actual tool/version and your exact instruction if you use AI. Save its actual output separately. The supplied practice drafts are authored examples and must not be recorded as your tool's output.

## Checks and correction
Open the source record alongside the draft. Check every event/date/time, venue, access qualification and contact label; check meaning, completeness and layout at the destination. Log each defect, supporting source and correction. Another AI agreeing is not independent evidence. Use the opened source and your own arithmetic/inspection. For high-consequence output, obtain suitable stronger review before action.

## Manual fallback
If the tool is unavailable or the draft fails, open `05-final-artifact-template.md`, copy approved facts into its fields, preserve access qualifications, then apply the same checklist. Missing facts remain blocked even during fallback. In case three, record the stop, open S3-C, log the recovery source, then complete manually. Count time already spent plus recovery; do not restart the timer at fallback.

## Whole-task measurement
Before work, define the same finished artifact and acceptance checks for manual and assisted runs. Record preparation, generation/drafting, checking, corrections, formatting, recovery and attributable maintenance. Define category boundaries to avoid double counting. Use comparable tasks; note practice/order effects. Save timing and test notes, including failures. Compare checked outcomes, not generation speed alone. Maintenance not incurred is zero; unknown is unknown, not zero.
