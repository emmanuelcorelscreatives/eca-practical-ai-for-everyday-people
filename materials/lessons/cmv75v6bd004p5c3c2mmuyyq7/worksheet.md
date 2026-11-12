# Write a Prompt You Can Reuse — Lesson 30
Emmanuel Corels Academy · Practical AI for Everyday People

All event notes and example drafts in this kit are fictional, self-created practice material. They do not describe scheduled real events. No account, subscription, network access or AI assistant is required: use any plain-text editor. A general assistant is optional; never upload unnecessary private material.

## Outcome
Separate recurring instructions from changing values. Fill seven labelled fields, test two cases, compare each result directly with the supplied source and restore a blank master for reuse.

## Files
- `blank-master.txt`: stable instructions, seven fields and five checks.
- `source-cases.json`: exact fictional facts for both authored cases.
- `case-1-filled.txt`, `case-2-filled.txt`: completed prompt copies.
- `example-drafts.md`: source-aligned example wording and a deliberately wrong diagnostic draft; these are authored examples, not evidence of a live assistant run.
- `review-sheet.md`: the five checks with expected observations and a missing-location exercise.

## Exercise
1. Copy `blank-master.txt`; do not overwrite the master. Put Case 1 values into the seven fields, leaving stable instructions unchanged. Compare with `case-1-filled.txt` only after attempting it.
2. Write the announcement yourself, or optionally ask a general assistant to draft it. Keep the result separately and label its provenance. Use only source notes: no invented organizer, fee, refreshment, registration deadline or guarantee.
3. Apply each check from `review-sheet.md` by comparing actual text with the supplied notes. Asking an assistant to review its own answer is not independent verification.
4. Remove the location from a second Case 1 copy. The expected response is `Missing: location.` Stop drafting until the responsible source supplies it; do not infer a venue from the event name or an old copy.
5. Restore the blank master; repeat with Case 2. Replace values, not stable rules. Check the three-book limit and clean/readable condition explicitly.
6. Save completed copies separately under task-based names. Confirm the master has empty values but retains fixed instructions and checklist.

## Completion
You can replace labelled values without rewriting recurring instructions, identify missing information instead of guessing and independently check each resulting draft. Matching fictional notes proves only consistency with those notes, not that any event exists or remains current. Consequential real-world claims need appropriate independent evidence. The next lesson separates instructions from source material more deliberately.

For the missing-location variant, remove Community Room from BOTH SOURCE TEXT and MUST PRESERVE (and every other value in that copied prompt). Keep `Location: [empty — required]` in both sections. The task must stop with `Missing: location.` Do not use the complete original case as extra input.

## Local consistency check
Optionally run `python3 verify-kit.py` from this extracted kit. It checks supplied fixtures and the complete saved delivery schedule, including negative controls. It does not call an assistant, verify real events or measure a new video export. `delivery-schedule.json` retains every saved cue in source order.
