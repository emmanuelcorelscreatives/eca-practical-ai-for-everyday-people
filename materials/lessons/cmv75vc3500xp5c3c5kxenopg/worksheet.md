# Lesson 204 — Test the Approval Boundary

Emmanuel Corels Academy · Practical AI for Everyday People

Prove that a complete rejection and an incomplete approval both stop a harmless action. First run a complete approved control so that an empty destination cannot conceal a broken workflow. All supplied case data is fictional. This kit contains no credentials, real recipients or production connections.

## What this kit proves

The supplied Python model actually executes the gate against the supplied cases and writes a local CSV. It is an optional, reproducible **offline model**, not Zapier execution evidence or an online Google Sheets integration. The manual exercise below needs no code. For the named-platform demonstration specified in the saved visual prompts, obtain real screenshots and actual run histories from the connected test workflow and new test spreadsheet. Do not label offline model results as vendor results.

## 1. Set up a harmless destination

Create a new spreadsheet called **Approval Boundary Test Log**, or copy `empty-test-log.csv` into a dedicated training workbook. Keep the headers Timestamp, Case ID, Validation, Decision, Proposed action and Result. Check that there are zero data rows before testing. Never use an existing private sheet or a production destination. Disable sending, publication, purchases, deletion and production edits. Do not connect those action types for this exercise.

Open `manual-review-queue.csv`. The missing Destination for INCOMPLETE-204-C is intentional: leave it blank. Supporting information is context; it is not one of the four required content fields. The required fields are Case ID, Proposed action, Destination and Final content. Test mode must additionally be on.

## 2. Check the route before running

The final gate must require **Validation = Complete AND Decision = Approve**. Inspect the actual workflow: the test action has exactly one incoming route, from that gate, with no earlier or alternate action path. Confirm all required values are mapped from this case, not a stale sample or default. Review the exact proposal version including destination and final content. A changed version requires fresh review.

## 3. Run the three cases in order

| Case | Validation | Decision | Expected rows for this ID |
|---|---|---|---|
| CONTROL-204-A | Complete | Approve | 1 |
| REJECT-204-B | Complete | Reject | 0 |
| INCOMPLETE-204-C | Incomplete: Destination missing | Approve, for this harmless test only | 0 |

For the control, inspect the fixed proposal, select Approve, inspect the passed gate and completed test action, then search the destination for CONTROL-204-A. There must be exactly one row and Result must equal **Boundary control passed**. Preserve the actual automatically recorded timestamp rather than typing a made-up timestamp.

For REJECT-204-B, preserve the complete proposal and choose Reject. Inspect the stopped gate and Not run action. Search the destination for the exact ID: zero rows; total remains one.

For INCOMPLETE-204-C, leave Destination empty, confirm Incomplete and the missing-field warning, then deliberately choose Approve only to test this harmless boundary. The gate must still stop and the action remain Not run. Search this ID: zero rows; total remains one. In normal work, request the missing information or reject rather than approving incomplete work.

## 4. Manual fallback

Create local folders `Pending`, `Approved`, `Rejected` and `Needs information`. Keep a complete reviewed copy of each proposal and its explicit recorded decision. Put the control in Approved, the rejection in Rejected, and the incomplete case in Needs information even though its test decision says Approve. Move only complete, approved, unchanged proposals to Approved. Add only that control to the training destination, then search all three IDs and count rows. A filename or folder alone never substitutes for checking the recorded proposal, completeness and decision.

## 5. Save evidence, not just a conclusion

Use `evidence-checklist.md`. Capture the empty baseline, each proposal/version and decision, each run's validation and action status, and each destination search/count. Preserve actual failures before repair. An internal green status is insufficient: inspect the destination itself. If a rejected or incomplete case creates a row, pause the workflow, retain evidence, and inspect earlier actions, alternate routes, OR instead of AND, permissive decision mapping, default values and stale samples. Keep all investigation confined to this harmless destination.

## Optional reproducible offline model

Requires Python 3, no packages or network access. From this kit's folder run:

```
python3 check_boundary.py
python3 boundary_lab.py --output practice-run-01
```

On Windows, use `py -3` in place of `python3` where that is your installed Python launcher. A new output folder is required; earlier evidence is never overwritten. Inspect `practice-run-01/run-history.json`, `test-log.csv`, and `summary.json`. The supplied cases should produce one control row, zero rejected rows and zero incomplete rows. The extra checks compare the current proposal against a separate reviewed snapshot of every approval-covered field as well as its version. They refuse content changes even without a version increment, changed reviewed versions, unknown decision values, production mode, other destinations, wrong action types, whitespace-only required content and duplicate case IDs. They do not replace real platform observation. Keep original supplied cases unchanged and create a separate copy for your experiments.

## Reflection

Explain why three empty results are weaker evidence than one successful control and two stopped cases. Name the two gate conditions and show independent destination proof for each result. Continue to Lesson 205, Recognize Partial Failure, only after you can explain the distinction between proposed content, internal execution status and an observed destination action.

## Included observed local run

`observed-local-run-v2/` retains an actual execution of this offline Python model with real UTC timestamps, all three history records, the one-row local CSV, exact-ID counts and a source/result-hash execution-check receipt. These are reproducible local-model observations, not vendor or online-spreadsheet evidence. Your own run should produce equivalent case counts with new timestamps.
