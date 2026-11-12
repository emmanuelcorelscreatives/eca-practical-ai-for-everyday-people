# Lesson 191 — Measure Time and Quality Across Runs

This Emmanuel Corels Academy practice kit accompanies Stage 32. Every person,
event and time in the supplied example is fictional or an authored demonstration.
The timing figures reproduce the lecture's self-created demonstration results;
they are not stopwatch observations from an actual AI tool or performance promises.

## Task and acceptance
Turn an approved event brief into a readable information sheet. Preserve event
title, date, time, location, audience and requested action. Label gaps and conflicts;
add no unsupported facts. The task is complete only when the final artifact passes
every item in acceptance-checklist.md. Label an AI-produced draft as generated;
the opened original brief or scan remains the evidence.

## Equal boundaries
For both routes start when opening the prepared input pack and stop only when the
final file passes all acceptance checks. Complete the manual baseline, rather than
guessing from memory. Assisted raw work includes preparation, requesting, processing,
transfers and relevant retries. Put verification, correction and manual recovery in
the checking/correction category; include every minute exactly once, never twice.
Log interruptions separately and state whether excluded from active-task totals.
Keep operator, tools, conditions, source and acceptance rules consistent; record
workflow/prompt version and any unavoidable differences.

## Exercise
1. Inspect four fictional cases in source-briefs.md. For a poor-scan trial use a new
   scan of your own permission-cleared brief. The kit provides a textual uncertainty
   fixture, not a genuine OCR observation or a supplied image scan.
2. Complete and check a manual information sheet for each selected case. Save it.
3. Use your existing documented workflow to draft the same output. Save the original
   generated draft and record actual raw time, then check it against the source.
4. Correct unsupported details and retain uncertainty. Save the accepted final and
   record all checking/recovery time. If abandoned, keep the row and explain why;
   leave acceptance blank or revise rather than treating abandonment as completion.
5. Copy blank-log.csv and record your real work. Do not mix your observations with
   lecture-demo-results.csv. Run python3 calculate.py lecture-demo-results.csv to
   reproduce the lecture arithmetic. Run python3 -m unittest -v test_calculate.py.
6. Compare only equally accepted outcomes. Retain slower and failed runs; a failed
   fast draft is not an equally completed task. If recovery finishes manually, mark
   the final route and include recovery. Explain conditional decisions, not guarantees.

## Expected demonstration results
Complete brief: manual14:20, raw4:10, check4:20, total8:30, difference+5:50.
Missing location: manual16:10, raw3:50, check8:10, total12:00, difference+4:10.
Conflicting times: manual18:40, raw4:30, check10:50, total15:20, difference+3:20.
Poor scan: manual17:00, raw4:40, check13:50, total18:30, difference-1:30.
Three positive differences and one negative: assistance was slower on the poor scan.
Mean difference is177.5 seconds (2m57.5s); median is225 seconds (3m45s).
Show four individual results and their range(-90 to350 seconds) alongside either
summary. No fixed number of runs suits every evaluation; choose representative cases.

The evidence supports using this tested workflow for clear digital briefs, careful
review for missing/conflicting inputs, and considering a manual route for poor scans.
Your own measured evidence may support a different decision. Lesson192 assembles
steps, templates, cases and results into a repeatable project.
