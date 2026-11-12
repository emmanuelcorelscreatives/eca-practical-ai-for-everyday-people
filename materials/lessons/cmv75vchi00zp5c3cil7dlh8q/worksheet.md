# Compare It with the Manual Process — Lesson 216
Emmanuel Corels Academy · Practical AI for Everyday People · Stage 36

## Start here
This kit supplies six **fictional workshop requests**, an existing ID log, paired timing sheets, a correction log, and a manual fallback. No request is sent to a person or service. All contacts use the reserved example.org domain. Work on copies, retain the originals, and never replace blanks with guesses.

Open CSV files in LibreOffice Calc using UTF-8, comma separator and quoted text. Treat Request ID, dates and duration text as text where appropriate; numeric duration columns explicitly use seconds. Save your working workbook under a new name. This kit does not require a paid no-code service.

## Exercise 1 — Make the two routes comparable
1. Read requests.csv and existing-id-log.csv. Choose the same task-card fields for manual and automated routes: ID, Contact, Activity, Date, Attendance Estimate, Accessibility Notes, Permission Confirmed.
2. Manual route: open request, check required fields, search ID log, copy to a task card, compare with original, and log the outcome. Stop for missing contact, confirmed duplicate, or ambiguous safety wording.
3. Automation route: required-field check → duplicate check → draft task card → log row → pause for human review. The workflow must have no external send/publish action. For an offline exercise, walk this decision flow using workflow-spec.md rather than claiming an unexecuted platform run.
4. Check draft against the opened original before internal approval; generating a draft does not verify its accuracy. Approval remains unavailable for unresolved exceptions.

## Exercise 2 — Measure the whole job
Use timing-template.csv, one row per case and route. Start before opening the request; finish after the final check or documented safe stop. Record elapsed seconds and active-human-work seconds separately. Waiting equals elapsed minus active only where the two are a non-overlapping partition of this exercise. Review, corrections and recovery are already included in the active total; do not add them twice. Record setup and maintenance separately, once per workflow/batch, not once per case.

The template is deliberately blank: perform and record your own observations, including safe exceptions. Do not copy the lesson's demonstration times as measured personal results. source-known-timings.csv records only values explicitly supplied by the authored demonstration. Other individual-case timings are not recoverable from totals and remain blank.

## Exercise 3 — Find and repair a mapping mistake
Using mapping-fixture.csv and the unchanged request for Normal B, compare the task card where its Accessibility Notes wording is in General Notes. Mark the wrong destination, fix only that mapping, then retest. Do not rewrite the source text. Record one mapping correction and the retest in your own correction log. The fixture is an explicitly broken study example, not an approved output.

## Exercise 4 — Write the four-part report
Fill report-template.md with batch size, elapsed and active savings; number/type of corrections; initial setup versus recurring maintenance; cases kept manual and why. Use your own observations, or clearly label the authored figures as a fictional demonstration. Include timing sheet, correction log, exceptions, fallback, and mapping retest evidence. Check answers in expected-results.md.

## Preserve manual fallback
Use manual-fallback.md if the platform, connection or linked tool is unavailable. No missing evidence, meaning or permission may be inferred by either route.
