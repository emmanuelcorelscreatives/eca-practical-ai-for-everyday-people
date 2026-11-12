# Avoid False Precision in Rankings — Lesson 119
Emmanuel Corels Academy · Practical AI for Everyday People

Compare three rooms for a fictional community workshop. Every venue, price and note is invented practice material. The source sheet is authoritative only within this exercise; it is not evidence of real availability or accessibility.

## Work through the lesson
1. Read `source-notes.md`. Separate exercise facts, preferences, constraints and unknowns in `comparison-template.csv`.
2. Optionally ask an available assistant: “Organize these supplied notes. Separate source-sheet facts from assumptions. Mark missing information unknown. Do not invent scores, weights, prices, features or a winner.” Trace each returned fact to the supplied notes. Do not search for invented venues as though they were real.
3. Open `illustrative-scores.csv` in a spreadsheet. These are instructor-authored illustrative generated-style assumptions, not an observed assistant response or defensible ratings. Cedar's travel score is seven. Cost scores six, eight and seven have no conversion rule. River's accessibility five falsely substitutes for unknown information.
4. Arrange the score columns in B:E, with Cedar, River and Market in rows 4–6. Put the assumed weights 40%, 30%, 20%, 10% in B2:E2. In F4 enter `=SUMPRODUCT(B4:E4,$B$2:$E$2)` and fill down. Some spreadsheet locales require semicolons instead of commas. These formulas test arithmetic, not judgment.
5. Change only the travel/equipment allocation to 35%/15%, leaving cost/accessibility at 40%/10%. Both sets total 100%. This five percentage point transfer reverses Cedar and Market. It is one controlled choice: a fixed total requires reallocating weight.
6. Restore the original weights. Test Cedar's equipment score at six and at eight. Its possible total overlaps Market's. Keep that uncertainty visible rather than reporting a precise winner.
7. Restore River's accessibility to unknown in the honest comparison. Do not silently treat missing values as zero, a neutral five, or a justified numeric total. Required access is a threshold; a high equipment score cannot qualify an unverified venue.
8. Use `manual-fallback.md` when scores or weights cannot be justified. Record facts, advantages, disadvantages, constraints, unknowns and your preferred tradeoff without a universal winner.
9. Consult `expected-checks.md` after your attempt. Python is optional: `python3 check-arithmetic.py` reproduces the arithmetic with the standard library. A calculator or an ordinary notes app also works.

The failed-ranking example is explicitly instructor-authored, rather than evidence that an assistant produced a particular failure. The opening 8.43 is a separate unsupported precision illustration; do not alter inputs to manufacture that total. No accounts, purchases, live venue contacts, screenshots of private data or completed external actions are required.
