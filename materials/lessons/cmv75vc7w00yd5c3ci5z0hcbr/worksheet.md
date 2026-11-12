# Practice worksheet

1. Before running anything, write the expected decision, failure reasons and downstream action for each input in practice-inputs.json.
2. Open the offline lab. Inspect the contract: request_id and title must contain text, due_date must be a real YYYY-MM-DD date, priority must be low, normal or high.
3. Run R-001. Verify every field, the green validation result and Saved draft. Read the actual history row; an earlier completed step alone is not sufficient evidence.
4. Run R-002. Confirm that due_date is absent, validation stops and Save draft is skipped. Record the exact missing-field reason rather than saying the entire run vanished.
5. Run R-003. Verify both date-format and priority errors appear together. Presence alone is insufficient.
6. Open History and Validation log. Compare all three actual results with your predictions and expected-results.json. Export the log if wanted, or enter your observations in the CSV template. Include an assigned manual owner and actual resolution time only when applicable; leave unknowns empty.
7. Manual recovery: select R-002, inspect its source card, enter the confirmed date 2026-11-06 and recheck. Repeat for R-003 using the source-authorized date and normal priority. Preserve old failures in history; continue only after a new pass.
8. Extra negative controls: whitespace-only title; impossible date 2026-02-30; priority NORMAL; date tomorrow. Each must stop. Restore a valid input and ensure it continues. A falsely stopped valid case also needs rule repair.
9. Explain separately why a structurally valid record can still contain false wording, lack permission or be inappropriate. Structural validation grants no approval to send or publish it.

Expected core outcomes: R-001 continue/Saved draft; R-002 stop/missing required field: due_date/Skipped; R-003 stop/date format not accepted: due_date AND priority not in allowed values/Skipped.

Recovery checklist: Open stopped record → Confirm source → Correct or request missing value → Recheck structure → Resume only after passing. Never silently guess missing values. Compare maintenance, corrections, usage and recovery effort with the manual process before expanding automation.

Evidence check: in Run history, inspect RUN-001, RUN-002 and RUN-003 individually. Confirm the original input, completed receiving/transformation steps, all validation reasons and saved/skipped outcome. Open Review sheet: only passing runs belong there. After recovery, inspect the original failed run again to prove its input and failure were retained.
