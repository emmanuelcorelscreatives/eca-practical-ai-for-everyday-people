# Lesson 190 — Handle Exceptions Explicitly
Emmanuel Corels Academy · Practical AI for Everyday People

All people, events, venues and source records in this kit are fictional Academy exercise fixtures. No booking, publishing, sending or legal service occurs. This is a low-risk event-information drafting workflow; practice using local copies only.

## Outcomes and practice files
Use `workflow-checklist.md` for the normal path and all exception rules. Copy `prompt-instructions.md` into your AI drafting session with the supplied source; do not send personal data. Use `output-template.md`, `manual-fallback.md` and `exception-record.csv` as the reusable output/record files. `cases.json` supplies five fully traceable cases; each original value retains its source identity. `workflow.py` is an OPTIONAL deterministic teaching simulator, not an AI tool or claim of a real external action.

## Exercise
1. Open cases.json and inspect NORMAL. Verify event name, date, start/end times, venue, intended audience, contact and approved announcement facts. Copy only those facts into an output template. Mark Awaiting human review; never mark approved or published.
2. Inspect MISSING (case EVT-014). Its required start time is blank. Record the input-check stop, ask “What time does the event begin?”, assign Request owner and create NO draft. After an answer, return to the complete input check; do not jump to final output.
3. Inspect CONFLICT. The signed event form says June 12, 2027; the flyer draft says June 19, 2027. Preserve both source names/values; assign Event coordinator; label Unresolved conflict. Do not infer a winner from recency or majority. No finished sheet is created. A partial scratch draft, if useful, must say UNRESOLVED — DO NOT PUBLISH and stay outside final output.
4. Inspect OUTSIDE: the request asks for a legal waiver. Record the boundary and retain the submission. Redirect to an authorized reviewer or appropriate qualified local provider, without drafting legal language or implying a completed referral.
5. Inspect UNAVAILABLE: simulate failure before creating any draft. Check whether a prior action succeeded before retrying. This exercise allows ONE later retry; if still unavailable, use manual-fallback.md with verified facts and Awaiting human review. A damaged input is not retried; record it and request a usable copy.
6. For each case verify detection, correct response, source traceability, visible status, blocked final output and usable recovery. Ask a partner to follow the records without an explanation.

## Optional reproducible simulator
Python 3.10+; no installation or network needed. From the kit directory run `python3 workflow.py` (Windows: `py -3 workflow.py`), then `python3 test_workflow.py` (`py -3 test_workflow.py`). The first command prints only five JSON dry-run observations; no files, messages or external actions are created. The second should report 8 tests OK. Inspect expected-results.jsonl and compare statuses/owners/draft flags, not output spacing. This simulator performs a structural entry check; a human must confirm real source accuracy, meaning, timing plausibility, permissions and contact details.

## Submission and marking
Submit your filled exception record, normal checklist, reusable instructions, normal draft and manual fallback draft. Keep original sources apart from generated drafts and unresolved questions. All five rows must retain case/source identity and the expected recovery route. No unresolved case enters final output. Review every name/date/time/venue/contact/phrase against opened evidence; use example.invalid contacts only. Never treat an assumption as evidence or a dry run as an external action. Higher-impact uses (payments, safety or public messages) need their own stronger authorization controls. Next lesson measures time and quality; this kit deliberately invents no measurements.
