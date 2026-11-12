# Recognize Partial Failure — Lesson 205

This Emmanuel Corels Academy exercise uses self-authored fictional community-event requests. Samira N., Riverside Reading Circle, TEST-205-B and RUN-205-017 are practice records. The timestamp is a fixed fictional exercise time. Nothing is sent, published, purchased, deleted or externally shared. The Python program runs offline. Its JSON is a genuine local simulation result, not a claim that a third-party automation or Google Sheets ran.

## What you are learning

Inspect which individual steps completed. Preserve completed work and recover only what remains. A failed overall status does not mean earlier external changes were reversed. A successful status does not prove the final content is correct.

## First use: inspect a controlled failure

Python 3 is needed only to execute the offline example. You can also complete the exercise by reading the supplied CSVs and the expected observations below. In a terminal opened in this kit directory run:

```
python3 workflow.py reset
python3 workflow.py run
python3 workflow.py inspect
```

Windows users may use `py` instead of `python3` if their installation provides that launcher. These commands write only `practice-state.json` in the current directory. Reset replaces that local practice state; inspect or copy your previous exercise before resetting. Do not use this practice program against real accounts or private records.

The input has a blank event-details field. Step 1 captures it and completes. Step 2 creates Request Log row 18 and completes. Step 3 fails with `Required event details are missing`; no draft is created. Open `practice-state.json` to independently inspect the local destination state: one request row and an empty draft list. The JSON entry `spreadsheet_row: 18` models the spreadsheet location; it is not a claim that a CSV physically occupies worksheet row 18 when opened.

## Four questions before recovery

1. What completed? Form capture and creation of Request Log row 18.
2. What did not complete? Generate review draft.
3. What changed outside the workflow? In a real deployment inspect the destination application. In this offline example inspect `request_log` in the saved state: it contains one matching row, blank details and the correct fictional identity.
4. What remains? Obtain authorized event details, then finish the review draft without recreating the row.

Use `recovery-log-template.csv` for your observations. `recovery-log-observed.csv` shows the state before a recovery decision, with the final two cells deliberately blank. Use `unknown` or `not visible` if actual evidence is unavailable. Never infer that hidden history proves a step did not run. Retention and permissions vary across tools.

## Actual platform and destination inspection

Locate RUN-205-017 by identifier, time or test record in the actual tool history. Confirm TEST-205-B and Riverside Reading Circle before inspecting the run. Expand each step and compare its captured input and output. Check the trigger input includes blank event details, the spreadsheet action input matches that record and its output identifies row18, and the draft action reports the missing required details with no output. Open the actual destination spreadsheet and verify row18, then inspect the review-draft folder to confirm no matching draft exists. Do not treat a platform output claim alone as destination proof. Read waiting, skipped, canceled and not-run statuses exactly as displayed; these are different from failed. If permissions or retention hide evidence, record unknown or not visible rather than guessing. This inspection comes before any retry or manual recovery.

## Manual fallback

The supplied `authorized-practice-detail.json` is a self-authored exercise source, not an AI inference or a real event confirmation. It supplies `discussion begins at 18:00`. Read it and verify TEST-205-B before applying it:

```
python3 workflow.py recover
python3 workflow.py inspect
python3 workflow.py check
python3 workflow.py inspect
```

The recover command records “awaiting checking” until the separate check command compares the saved draft with the saved destination row. Inspect both yourself, then run check. Check that exactly one request row remains, that one manual review draft references row 18, and that its event, contact and supplied details match the source. It must remain `For review — not sent`. The original run must still say `Failed`: a manual recovery does not rewrite its history. `recovery-log-completed.csv` models the recovery decision and final disposition. These CSVs are examples, not permanent audit records or proof of a third-party action.

## Destination spreadsheet practice

Create NEW Academy-only Google Sheets named `Request Log — Practice` and `Automation Recovery Log`, if you have authorized access. Do not use personal workbooks or show other files. Add your own headers in Request Log and place the TEST-205-B record at actual worksheet row 18; keep its details cell blank until the authorized manual step. The supplied `request-log-row18.csv` records the intended location explicitly; importing it alone will not position it at row 18. Copy the eight headers from `recovery-log-template.csv` into the recovery sheet. Populate the observed state first, leaving Recovery decision and Final disposition empty, then populate the completed example after inspecting the manual draft. Avoid exposing unrelated sheets, account names or browser tabs in captures. The offline JSON exercise does not require a Google account.

## Why not restart everything?

On a separate scratch state, run the same blank input twice:

```
python3 workflow.py reset --state duplicate-demo.json
python3 workflow.py run --state duplicate-demo.json
python3 workflow.py run --state duplicate-demo.json
python3 workflow.py inspect --state duplicate-demo.json
```

There are two request rows and still no draft. This intentionally unsafe simulation has no duplicate protection, illustrating why an overall restart can repeat completed actions. Do not generalize its replay semantics to a vendor: inspect that platform's actual retry behavior and input first. Duplicate prevention itself is the next lesson.

## Check your work

```
python3 checks.py
```

The checks exercise the missing-field failure, completed row, no draft, safe manual completion, original failed history, unsent state, duplicate hazard and a separate successful run with an explicitly faulty category mapping: unchanged source Community discussion is incorrectly mapped to Sports in both destination row and draft. That final case demonstrates why inspecting content matters even when operations completed. Checks verify this supplied example; they do not validate a real account or guarantee your own workflow.

## Handover exercise

Write a two-sentence handover distinguishing original failure from manual completion. It should name RUN-205-017 and TEST-205-B, preserve row 18, identify the supplied detail and state that the draft was checked but not sent. Compare with the completed recovery log. Then explain one limitation of a platform's run history and what destination evidence you would inspect.
