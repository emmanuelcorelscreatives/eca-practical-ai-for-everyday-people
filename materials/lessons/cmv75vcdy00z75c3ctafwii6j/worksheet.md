# Lesson 213 — Add Validation and Review
Emmanuel Corels Academy · Practical AI for Everyday People

## Practice boundary
Use only the three fictional workshop requests supplied here. Names, example.org contact addresses and request details are Academy-created practice data. The requested dates are fixed fictional exercise dates, not current booking requests. Nothing in this kit sends messages, books venues, purchases, deletes or publishes. A passed field check does not establish factual truth or authorization. All proposal text is a supplied study fixture, not evidence of an actual AI generation or external platform run.

## Named platform context
The narrated workflow is Google Forms → Zapier → Google Sheets. In the genuine Google Forms editor, make Request ID, Contact name, Contact email, Requested date, Request details and Permission to contact required. Use a Date question for the requested date and appropriate contact input validation. Required controls only check ordinary form submissions; Zapier must separately validate the actual incoming fields before creating a proposal. Inspect the real interface and your account permissions; this kit does not configure, execute or imitate those services.

## Set up your practice files
Open `requests.csv` and `review-queue.csv` in a new Academy-only workbook. Keep the original input unchanged in its own tab. In Google Sheets use File → Import to place each CSV in a separate new tab; inspect the preview and choose comma separation. Do not upload existing private worksheets. Keep Requested date as the literal supplied value and leave EVT-105 empty. The equivalent manual review queue is supported if your account lacks a built-in approval step. The CSV files are not a Zapier export and do not claim to configure its interface automatically.

Read `mapping-and-proposal.md` before setting up any trigger. Keep the draft workflow unpublished and external sending disabled. Check your actual account's available controls; feature names and plans vary.

## Exercise 1 — Validate incoming fields
Inspect EVT-104's original fields, then map each check to the incoming field with the same meaning. Required fields: Request ID, Contact name, Contact email, Requested date, Request details. Permission to contact must equal Yes. The lesson's visible five-rule filter shows ID, contact email, date, details and permission; retain the form's required contact name too. The local checker enforces all these required fields. A complete record has Validation result Valid and Review status Awaiting review; it is not approved yet.

Load EVT-105. Observe that only Requested date is blank. Do not substitute today, tomorrow or text from unrelated fields. Keep Proposal empty. Record Missing required field, Needs information and Missing requested date. Route it away from proposal creation and the approval queue. Request clarification using your organization's authorized process, outside this exercise.

## Exercise 2 — Prepare meaningful human review
Use the supplied EVT-104 study proposal. Compare Amara Nwosu, 22 October 2026 and 25 volunteers against the source. Keep the label Generated proposal separate from Source record. Include the intended next action Update internal task, destination Workshop planning task list, and assumptions None stated. No booking or accessibility is confirmed. Choose an authorized reviewer; do not put an arbitrary person into a live workflow.

When the reviewer accepts this exact proposal, set Approved and Checked against source. This decision permits only the described internal task update. Keep external sending disabled. A changed content, date, recipient or destination invalidates the prior review and must return through validation and Awaiting review.

## Exercise 3 — Reject unsupported content
EVT-106 contains every required field, but its deliberately flawed study proposal says wheelchair-accessible venue confirmed. The supplied source does not confirm this. Keep Validation result Valid while setting Review status Rejected, Reviewer note Unsupported accessibility confirmation and Action status Stopped. Preserve the original input and proposed text for correction. Rejection must never reach the approved branch.

## Manual fallback
Use `review-queue.csv` with controlled Review status choices Needs information, Awaiting review, Approved, Rejected. Preserve Source record link, Generated proposal, Intended action, Destination, Assumptions and Reviewer note. Local source references identify supplied exercise rows, not private web links. Restrict editing appropriately. Keep external actions manual. Use `answer-key.md` only after completing your own comparison.

## Optional reproducible local check
Python 3, standard library only: run `python3 validate_workshop.py` from this folder. It reads local CSVs, performs deterministic checks and prints expected state comparisons. It makes no network calls, writes no data and does not call any AI or vendor service. This is a training checker, not production authorization or an email address verification service.

## Completion checks
- All three source records remain intact.
- EVT-104 initially waits for review; acceptance changes only the defined internal state.
- EVT-105 keeps its blank date and has no proposal.
- EVT-106 is Valid yet Rejected, and the approved path stays stopped.
- Review package visibly separates source evidence, generated proposal, intended action, destination and assumptions.
- Any material edit requires new review. No external action occurred.

The next lesson covers logging and duplicate protection. This kit intentionally does not implement either feature.
