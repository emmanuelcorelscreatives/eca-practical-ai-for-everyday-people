# Tell the Tool What to Preserve
Emmanuel Corels Academy · Practical AI for Everyday People · Stage 5 / Lesson 28

All names, venue and events in this kit are fictional Academy-authored practice material. The two draft files reproduce the exact authored lesson demonstrations; their wording is a controlled teaching example, not a promise of an unconstrained assistant response or evidence of a real meeting. Use any general assistant available to you, or complete the manual fallback in a regular text editor. No account, paid product, API key or installation is required for the manual exercise.

## Protected written source
The protected date strings come from the authored visible SOURCE TEXT in scenes 13–14 and the PRESERVE EXACTLY list in scenes 31–32: `18 November 2026 at 18:30` and `25 November 2026 at 18:30`. The narration says “18th” and “25th” when verbalizing these same calendar dates. In this written exercise, copy the written source character for character, including its absence of ordinal suffixes and its quotation punctuation. Do not replace written strings with a transcription of their spoken rendering. No case date, year, source text or narration has been changed.

## Practice
1. Open `source-notice.txt`. Keep the SOURCE TEXT label on the original in every comparison. Mark all five exact strings listed in `protected-details.json`; the dates each include the full time. Separately list the four essential meanings.
2. Compare `flawed-draft.txt` directly with the source. Record altered, omitted and unsupported content in `comparison-template.csv`. Record venue literal presence separately from the essential meaning that the venue remains unchanged; all four meaning checks have separate columns. Do not rely on an assistant's claim of preservation.
3. Optionally paste `weak-prompt.txt` into your chosen assistant. Save its actual response separately, clearly labeled AI DRAFT. A model may preserve everything; do not manufacture an error to match the flawed example.
4. Use `strong-prompt.txt` with the same source. Save the actual result. Compare the five literal strings character for character, then reread for all four meanings and unsupported additions. Quotations require the exact words and punctuation, not simply quotation marks.
5. Compare `faithful-draft.txt`, the exact authored successful demonstration from scenes 41–42, using the same checks. `flawed-draft.txt` likewise retains the exact authored demonstration from scenes 25–26. These are controlled examples, not promises that your assistant will produce the same words.
6. Try the 15-word constraint in `conflicting-prompt.txt`. The protected strings alone exceed 15 words; a safe response flags that conflict. A response that silently drops details fails.
7. Manual fallback: copy the five protected strings directly into a new editor document. Rewrite only surrounding wording, add the four essential meanings, then perform the same direct comparison. Highlighting text is a reminder, not an enforcement mechanism.
8. Repeat with a short paragraph you authored or have permission to use. Choose one name, one date or number, one quotation and one essential meaning. Avoid personal or sensitive information.

## Completion checks
Your comparison identifies every literal mismatch and meaning change; the final rewrite retains all five exact strings and four meanings without unsupported additions. Record what the first instruction failed to protect and how you strengthened it. A faithful rewrite can preserve an incorrect source: verify consequential source facts separately before sharing, especially attendance, money, rights, health or safety details.

See `answer-key.md` after attempting the comparison. `check_exact_strings.py` checks only literal presence and reference word count; meaning, quotation context, additions and factual truth still require human comparison.
