# Improvement decision and future retest
Worked-example options: (a) strengthen required-field checking; (b) reduce formatting cleanup; (c) test more realistic inputs.

## Proposed next change from this lesson
Require accessibility details or an explicit “not confirmed” status before any completion decision, and detect the gap before layout work begins. “Not confirmed” makes the missing state visible; it is **not** permission to mark a required fact complete, approve distribution or guess a value. Completion remains blocked until confirmed evidence resolves a required gap. This is a proposed change, not an executed improvement or proven saving.

## Make your own decision
Observed problem and actual record reference: ______
Candidate improvement: ______
Expected benefit (hypothesis): ______
Effort and tradeoffs: ______
Reason selected over alternatives: ______
Version before/after: ______

## Future retest plan — no pass prefilled
Repeat the same complete-brief, changed-schedule and missing-information cases after revising the workflow. Preserve the same acceptance standard and source conditions. Test that normal cases still work, the caretaker qualification is retained, missing information blocks earlier, no facts are guessed, and manual fallback still works. Record actual timings and correction counts. Include a tool-unavailable check if relevant. Compare limitations and order/practice effects. A regression is a new problem introduced by the change.

| Case | Expected check | Actual result | Time | New defect? | Evidence reference |
|---|---|---|---|---|---|
| Complete brief | Required fields preserved; same checks | | | | |
| Changed schedule | All new times and access condition preserved | | | | |
| Missing information | Early flag and stop; no invention | | | | |
| Manual recovery | Confirmed facts only; same checklist | | | | |

Do not claim “fixed” or faster until these actual results exist.
