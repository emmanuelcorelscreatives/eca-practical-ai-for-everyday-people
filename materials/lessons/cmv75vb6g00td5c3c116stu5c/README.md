# Emmanuel Corels Academy — Lesson 178
## Organize Customer or Volunteer Requests
All four messages and addresses are self-created fictional practice data for a fictional repair café. There are no real customers, accounts, attachments or external actions. This kit matches the saved lesson, including exact message wording and request IDs.

Open the four `messages/*.txt` originals before any generated classification. Open CSVs in LibreOffice Calc (UTF-8, comma separated), or use `request-triage.ods`. `practice-queue.csv` is the learner worksheet. `reviewed-queue.csv` is the authored teaching answer key, **not a transcript of a live assistant run**. `Source checked` means comparison with our opened fictional original; it does not verify truth or authorization. Reviewer decisions and dates intentionally remain blank.

1. Read categories and attention rules. Keep category and attention flag separate.
2. Classify each message manually in the blank worksheet. Copy an exact evidence phrase; record missing information.
3. Optionally submit only the fictional messages plus reusable instruction and categories to an available assistant. Do not use private messages or upload attachments. Preserve the actual returned draft separately; never treat our answer key as a model observation.
4. Count four input IDs and four output IDs. Compare every proposed label, phrase and gap with the original. Correct swapped IDs, unsupported reasons or missing rows.
5. Sort human attention with R-002 urgent first, R-003 suspicious second; preserve R-001 and R-004. Record no completed action, assigned person or authorization that the sources do not contain.
6. Explain why urgent wording alone does not prove urgency/authenticity; why R-003 remains Unclear plus Suspicious; and why R-004 is not a confirmed booking change.
7. If an assistant is unavailable, complete the same worksheet manually. Record corrections in correction-log.csv instead of erasing history.

Expected checks: R-001 Booking or administration + Human review, authorization unknown; R-002 Safety or service issue + Urgent human review, exact location/conditions unknown; R-003 Unclear + Suspicious human review, verify independently without opening; R-004 Unclear + Human clarification, missing date/reference/current/requested slot. A human may override a label with evidence; no percentage substitutes for judgment. Do not invent safety instructions, accuse a sender of proven fraud, or change any booking/customer record.

`verify-kit.py` checks exact messages, IDs, category/flag mapping, blank decisions and no fabricated completed status. It does not validate a real incident. Lesson 179 moves on to simple operational summaries; this kit stays within classification.

Self-authored Academy practice materials, CC0-1.0. Software/product names belong to their respective owners.
