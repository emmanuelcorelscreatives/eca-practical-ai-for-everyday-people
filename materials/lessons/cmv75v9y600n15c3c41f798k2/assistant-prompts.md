# Authored prompts for the learner to run
These are instructions, not an assertion that a vendor assistant has executed them.

## Initial instruction
Reorganize only the supplied CV evidence for this fictional role. Do not add facts. Preserve dates, employers, qualifications, numbers, tools, and level of responsibility. Mark missing information as [not supplied]. Return suggested section order, revised bullet drafts, and a claim-check table.

Paste `role-description.md` and `evidence-sheet.csv` below that instruction. Use fictional data only. Do not ask for invented seniority, gap filling, or hiring predictions.

## Revision instruction
Remove unsupported claims. Return only bullets traceable to the evidence sheet. Where a result is absent, use a responsibility-based bullet and mark the missing result.

## Human check
Compare every sentence to the original evidence. A fluent output does not become evidence. If an actual response adds an unknown employer, date, tool, qualification, programme or percentage, reject that addition and preserve the failed draft for comparison.
