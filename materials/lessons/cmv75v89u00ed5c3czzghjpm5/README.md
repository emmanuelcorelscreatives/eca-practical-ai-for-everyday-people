# Lesson 88 — Build Quizzes and Flashcards from Sources

Emmanuel Corels Academy · Practical AI for Everyday People

This self-authored fictional community-garden source matches the lesson. It is not a real garden policy, water-safety recommendation, or live assistant transcript. The complete source is CC0; use it without uploading private material.

1. Read `source-passage.txt`, keeping S1–S5 visible. Verify all five sentences arrived before asking any assistant to help.
2. Use `prompt-template.txt` with a permitted assistant, or do the work manually. The prompt requests 3 short-answer, 2 multiple-choice and 4 flashcards; generated output remains unverified.
3. Inspect the deliberate failures in `unverified-draft-errors.json`. Correct changed scope, false premises and vague keys; remove duplicate/trivial cards; keep missing installer information unresolved.
4. Build the smaller final set: 3 short-answer + 2 multiple-choice + 3 useful flashcards. Compare each question and key to the source, not merely to one another.
5. Open `source-study-workspace.html` locally in a browser. The custom Academy course application is a deterministic exercise, not a third-party AI service. Answer before revealing each key; show evidence afterward.
6. Use `verification-table.csv` for final items and `draft-review-history.csv` for revised, removed and unresolved draft decisions. Use `verified-study-set.json` as the checked reference. SA3 is explicitly a calculation, 2 × 200 = 400 liters; no barrel installer or collection date is provided.
7. Repeat practice on separate days. Record incorrect answers and revisit supporting sentences. No online account, personal data, or network access is required for the local exercise.

Manual fallback: open `manual-study-set.html` in a document editor or browser. Keep question, answer and supporting sentence in adjacent columns. Hide the answer while recalling; reveal, compare and correct. Paper is also possible as narrated, while course illustrations remain screen based.

Run `python3 verify.py` to check the supplied set size, source links, arithmetic and unsupported-question exclusion. This checks supplied data integrity, not any future assistant output. You must still inspect actual generated questions yourself.

## Expected review decisions

- SA2: replace “all garden plants” with “seedlings”, retaining Tuesday and Friday mornings (S2).
- MC1: remove the false drinking-water-safety premise; correct statement preserves “without making the water safe to drink” (S4).
- FC1: preserve “during water restrictions”, both seedlings and newly planted beds (S3).
- FC2: replace vague “clean” with “limit debris and mosquitoes” (S5).
- Remove repeated covered-barrel fact and trivial gap-fill card. Keep the meaningful origin question.
- Who installed the barrels: missing from source; remove or mark unresolved, never invent.

All files are self-authored exercise material. Instructor identity and authored lesson narration are not changed by this kit.
