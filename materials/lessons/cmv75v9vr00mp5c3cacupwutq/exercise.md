# Practice: a controlled switch
1. Copy comparison-template.csv. Write the fixed date, area, step-free and vegetarian requirements, your own total budget ceiling, departure after 10:00 and return by 18:00. Separate fixed constraints from changing status.
2. Read generated-suggestions.md. Keep every generated claim unverified. List the exact evidence required for Venue A, B, C and Route 2.
3. Open fictional-evidence.csv. Record evidence IDs and missing fields. Venue C's unknown accessibility must stay Unresolved. Price fields remain unknown until your exercise budget/price inputs are supplied; a suggested venue cannot be declared affordable from silence.
4. Use comparison-template.csv to record trigger, alternative, source opened, last checked, extra time, extra cost, access and other gaps. Do not replace unknown time or cost with zero. Record any made-up classroom extension as your own assumption, never official evidence.
5. Rehearse the authored 09:30 closure notice: Venue A closes. The switch trigger is met. Evaluate Venue B's date-specific hours, access, suitable food, reservation conditions, your budget and the return deadline. The lesson's completed example treats B as usable after all checks; the starter dataset deliberately leaves numeric cost/return details for you to verify, so your unfinished worksheet must stay conditional.
6. Rehearse Route 1 interruption. Open the Route 2 classroom notice, then check accessibility, departure/return and added cost before relying on it. Operation alone does not establish arrival before 18:00.
7. Apply the same method to the retail example: match exact variant, location and quantity; check current status and full total before accepting a substitute. Do not buy anything.
8. Fill offline-card-template.md without personal data. Keep a manual route and operator/staff contact method. Offline maps depend on app/region support and do not promise live traffic, alternate routes or public-transport/walking/cycling directions.
9. Final check: clear trigger; suitable verified alternative; current opened evidence; essential details saved; manual route ready. Keep purchases/bookings/cancellations under human control.


## Reproduce the local worked practice
Open index.html in a browser. Its top navigation reaches every evidence page without editing URLs: Research, Suggestions, Venue A, Weekly/special hours, Listing comparison, Venue B, Venue C contact, Journey planner, Route 1 alert, Route 2 rehearsal and Retail evidence. These are self-authored fictional pages, never live official websites.

On Research, edit the dated request and click Generate practice suggestions. The displayed response is scripted. Open Weekly/special hours, Listing comparison and the venue pages. On Venue C, type a question and click Keep unsent draft in this tab; navigate to Venue A and back to retrieve it. Closing the tab ends the draft; no message is sent.

On Journey planner, change the date to 18 October and click the button: the app must reject this unsupported scenario without showing a checked journey. Restore 17 October, after 10:00, with step-free selected, then open the supported scenario alert. This is fixed fictional evidence, not route computation or confirmation of accessible stops, cost or return time.

Import comparison-template.csv and fictional-evidence.csv into Calc using UTF-8, comma separators and every column set to Text in the import dialog. This preserves the literal 09:30 and prevents automatic time conversion. Preserve all unknown markers. Compare your closure and transport rehearsal entries to worked-comparison-closure.csv and worked-comparison-route.csv. A completed worksheet may correctly contain unresolved conditions: it must not turn missing values into approvals. Compare your offline note to worked-offline-card.md; unavailable real addresses, contacts and private references remain unavailable.
