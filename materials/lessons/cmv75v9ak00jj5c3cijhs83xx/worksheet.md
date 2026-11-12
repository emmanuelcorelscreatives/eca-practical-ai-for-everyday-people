# Avoid False Precision in Rankings — Lesson 119
Emmanuel Corels Academy · Practical AI for Everyday People

Compare three rooms for a fictional community workshop. Every venue, price and note in this kit is invented, self-authored practice material. The source sheet is authoritative only inside this exercise; it is not evidence of real availability or accessibility.

## Work through the lesson
1. Read `source-notes.md` and separate exercise facts, preferences, constraints and unknowns in `comparison-template.csv`.
2. Optional AI instruction: “Organize these supplied notes. Separate source-sheet facts from assumptions. Mark missing information unknown. Do not invent scores, weights, prices, features or a winner.” Check every generated factual entry back to the supplied notes. Do not ask a real search engine to verify invented venues.
3. Open `illustrative-scores.csv` in any spreadsheet. These are deliberately unsupported generated-style assumptions, not defensible ratings. The cost scores six, eight and seven have no conversion rule. River Room's accessibility five falsely replaces unknown information. Remove that five in your honest comparison.
4. Copy the numeric score columns B:E into a working sheet, with rows 2–4 holding Cedar, River and Market. Set B7:E7 to 25%,25%,30%,20%. In F2 enter `=SUMPRODUCT(B2:E2,$B$7:$E$7)` and fill down. Some spreadsheet locales require semicolons instead of commas. These formulas test arithmetic, not judgment.
5. Change only the travel/equipment weight allocation to 30%/25%, leaving cost/access at 25%/20%. Both allocations total 100%; the five percentage point transfer reverses Cedar and Market. This paired transfer is one controlled choice: keeping a fixed total necessarily reallocates weight.
6. Restore the original weights. Test Cedar equipment at seven, then nine. Compare its range against Market's total. Keep the uncertainty visible; do not present an exact winner.
7. Use `manual-fallback.md` if a score scale, weight or evidence cannot be justified. Step-free access is a non-negotiable constraint in this exercise. Unknown is not confirmed; a compensating equipment score cannot qualify an option.
8. Check `expected-checks.md` after your attempt. A calculator or pen-free notes app suffices; Python is optional. `check-arithmetic.py` reproduces arithmetic only and needs Python 3, no external libraries.

No accounts, purchases, live venue contacts or personal information are required. Never upload private information to an assistant. These files contain no screenshots or claims of completed external actions.
