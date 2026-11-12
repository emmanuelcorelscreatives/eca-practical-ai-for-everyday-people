# Use Manual Handoffs Before Automating
Emmanuel Corels Academy — Practical AI for Everyday People, Lesson 185.

## What this kit is
All event details are self-authored fictional teaching data. “Approved event brief, version 1” is the source label inside this fictional exercise, not evidence of a real approved event. Sam is a fictional name. No private information, booking, real contact details, or external action is involved. Work in a new local document and spreadsheet; do not share or publish the exercise.

## Files and starting point
Read source-notes.txt without changing it. missing-date-input.txt is the deliberately incomplete failure case. assistant-instruction.txt contains the narrow handoff instruction. expected-review-table.tsv is a model answer for checking after your attempt, not a captured AI response. draft-information-card.txt is a checked example draft, not a publishable announcement. handoff-log-template.tsv records your observations. answer-key.md explains acceptance and failure behavior. provenance.md describes authorship.

## Do the manual workflow
1. Open source-notes.txt in a plain text editor. Identify title, date, opening time, instruction, entry cost, contact, unknown capacity, source and assumption. Select the whole block through its final line; copy once, leaving the source unchanged. Never replace unknown capacity with zero.
2. In an available general assistant, paste the instruction followed by the complete notes. Use only this fictional data. If no assistant is available, create the same four-column table manually in a document. Do not pretend a model ran. The task is organizing and inspection, not tool access.
3. Compare every table row with the original notes, especially 14 May 2027, 10:00–13:00, Sam, unknown capacity, source label and assumption. Correct dropped or invented information before continuing. Record actual changes in the handoff log. Use expected-review-table.tsv only after you make your own attempt; wording may differ if meaning and status remain exact.
4. Copy the checked table to a blank spreadsheet. Inspect four separate headers: item, value, status, source or note. If everything lands in one column, stop and use the spreadsheet's tab-delimited import/paste options, or make four columns manually. Tool interfaces differ. Recheck the original source after repairing the format. Keep date and time as text where needed so automatic date conversion does not change them. No calculation is required.
5. Compare the spreadsheet with the source, not just the assistant. Missing or unsupported values remain unresolved. Copy only checked fields to a new document draft, preserving the source and assumption. Explicitly mark room capacity for confirmation and the entire document as DRAFT — HUMAN REVIEW REQUIRED. Compare against draft-information-card.txt after your attempt.
6. Check title, date, opening time, Sam, bring instruction, free entry, unknown capacity, source and uncertainty. Do not add a venue address, registration link, capacity number, confirmed schedule or booking. Save with a clear draft name; do not publish it.

## Failure drill
Start a separate run from missing-date-input.txt. Mark Date missing, stop the handoff and return to the source to request clarification: “What date belongs to this event, and which source version confirms it?” Do not infer the date from your memory or the answer key. The original file can demonstrate recovery only after you explicitly record this clarification step. If a tool is unavailable, use the plain-document table route above; record which tool was unavailable and verify every field manually.

## Completion evidence
Save your checked table, draft and completed log. Each handoff needs its actual comparison source, format observations, any changes and a pass/stop decision. Explain one weak point discovered and why automating it now would hide a risk. Do not connect services, schedule messages or automate this exercise. Next lesson concerns recovering from missing or poor input.
