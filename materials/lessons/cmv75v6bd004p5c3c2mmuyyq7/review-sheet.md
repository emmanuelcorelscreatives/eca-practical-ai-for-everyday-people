# Five checks and expected observations
Use actual source-to-draft comparison, not an assistant's confidence score.

| Check | Case 1 expected observation | Case 2 expected observation |
|---|---|---|
| Task | Announcement to local residents | Announcement to students and staff |
| Protected details | Green Corner Workshop; 18 November 2026; 14:00–15:30; Community Room; registration required; event form | Riverside Book Swap; 3 December 2026; 12:30–14:00; Library Entrance; up to three clean, readable books; information desk |
| Unsupported additions | No price, organizer, guarantee, extra activity or registration deadline | No fee, promise, organizer or extra activity |
| Format | One heading and two short paragraphs | One heading and two short paragraphs |
| Missing information | All required case facts are supplied; no factual assumption needed | All required case facts are supplied; no factual assumption needed |

## Missing-location variant
Delete the location from a separate copy of Case 1 source and leave that required value empty. Expected: `Missing: location.` The task must stop rather than guessing. The original complete case retains Community Room; do not overwrite it.

## Record your result
For each check, note the exact draft quotation, matching source value and pass/fail. Repair only supported details. Recheck the repaired draft; preserve your original for comparison.

## Master check
All seven labels remain; all values are empty. Stable task rule, no-guessing rule and checklist remain. Neither Green Corner nor Riverside values should be embedded in the blank master.

For the missing-location variant, remove Community Room from BOTH SOURCE TEXT and MUST PRESERVE (and every other value in that copied prompt). Keep `Location: [empty — required]` in both sections. The task must stop with `Missing: location.` Do not use the complete original case as extra input.
