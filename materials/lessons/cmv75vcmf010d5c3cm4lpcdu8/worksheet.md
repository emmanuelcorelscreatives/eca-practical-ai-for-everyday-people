# Lesson 220 — Set Boundaries for a Task-Performing Assistant

Emmanuel Corels Academy · Practical AI for Everyday People

## What you will practise
Define allowed resources, prohibited actions, human review points and the conditions for stopping. The fictional community event is self-created practice, not an actual event or account. The included product-neutral app is a deterministic teaching sandbox, **not a language model or a vendor assistant**. Its actions are limited to local reads and one draft write. Its behavior demonstrates the boundary contract; it does not prove any AI product will follow these instructions reliably.

## Start with the manual version
1. Open `approved-event-brief.pdf` and `checklist-template.md`.
2. Read `boundary-card.md`; keep instructions separate from the reference facts.
3. Copy date, venue, activities and the accessibility note exactly. Mark coordinator and attendance estimate missing.
4. Leave start time awaiting confirmation. Do not invent it when the task requires it.
5. Compare the draft with the brief and check there is no unsupported equipment claim.
6. Keep it a draft. No messages, publication, purchases or shared-record changes are part of this exercise.

## Optional functional sandbox
Requirements: Python 3 and Poppler's `pdftotext` command (install using your operating system's package manager). No network account, AI subscription or API key is used. From this kit directory run `python3 app.py`, then open `http://127.0.0.1:8765`. It binds loopback only; do not expose it publicly. Stop with Ctrl+C. The app reads only this kit's approved PDF and template and writes only the fixed `sandbox/event-checklist-draft.md` destination. It intentionally uses deterministic practice rules so actual reads/writes and stop conditions can be inspected. Opening the app is not evidence a third-party assistant ran.

In Instructions, inspect the five boundary sections. In Knowledge, inspect the actual brief and allowed template. In Tools, confirm only approved-file reads and sandbox-draft writes are available. In Preview, choose a scenario and run it. Draft creation and saving are separate steps: inspect the source and draft first, then choose Save draft. A repeat save is refused rather than silently overwriting. For a fresh exercise, close the app and move the existing practice draft manually before restarting; the app has no delete tool.

## Six checks and expected outcomes
| Practice request / condition | Expected observation | Manual fallback |
|---|---|---|
| Prepare draft from approved brief | Actual PDF/template reads; supplied details preserved, missing coordinator/estimate marked; no external action | Copy confirmed items into template |
| Include confirmed event start time | STOPPED — REQUIRED INFORMATION MISSING; ask for confirmed time, no save | Mark awaiting confirmation |
| Conflict: approved section A says capacity 80; B says 120 | STOPPED — CONFLICTING INFORMATION; show both labelled scenario values, choose neither | Ask responsible person to confirm |
| Purchase supplies and email volunteers | ACTION NOT PERMITTED; offer only a reviewable draft alternative; no tool for either action | A person handles consequences separately |
| Sandbox permission unavailable | STOPPED — SANDBOX PERMISSION UNAVAILABLE; no fallback path or save claim | Restore approved access or use manual template |
| Venue provides audio equipment (not in brief) | STOPPED — EVIDENCE UNVERIFIED; no invented fact/save | Remove or label unverified until confirmed |

The conflict and access cases are explicitly selected training conditions. The app does not manufacture contradictory reference evidence or pretend the host filesystem actually failed. The activity panel distinguishes those simulations from real tool operations. `expected-results.md` has the detailed checking rubric. `python3 test_app.py` exercises the actual PDF read, allowed-path write, no-clobber guard and all stop cases inside an isolated temporary copy.

## Create your own card
Write one concrete purpose, exact allowed file/template/destination, prohibited actions, review point and stop rule. Ask: purpose? allowed resources? prohibited actions? review before what? stop when? Limit tools, destinations and time to the task. Test a normal request, missing required information, a prohibited action and a stop/escalation condition before reuse. Persistence and isolation are not accuracy, competence, authority or accountability. The person approving consequences remains responsible.

Next lesson: Watch for Untrusted Content Instructions. This lesson does not teach that separate topic in advance.
