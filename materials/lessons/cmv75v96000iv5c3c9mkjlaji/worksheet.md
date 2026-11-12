# Lesson 115 — Separate Facts, Preferences and Constraints
Emmanuel Corels Academy · Practical AI for Everyday People

## Purpose and practice boundary
Keep evidence, personal priorities and nonnegotiable conditions separate before asking AI to compare options. All products, supplier statements, dates and prices in this kit are self-authored FICTIONAL practice data. They describe no real product or purchase. No AI answer or live application result is claimed here.

## Your practice task
You want a small fictional desk fan for a shelf. The shelf's usable width has been measured as 35 cm in this exercise. A fan must fit that width and work from your existing USB-A power source. You initially strongly prefer easy carrying; quiet operation matters less. These are the exercise user's priorities, not universal preferences.

1. Open `source-cards.md`. Inspect each option's exact model, version, region and package. Use only those cards. Their fictional issue date is 2026-01-15; no external currency is asserted.
2. Open `comparison-template.csv` in a spreadsheet or a text editor. Keep one option per row and enter the evidence, exact card location, preference interpretation, constraint status and unresolved question separately.
3. Copy the narrow instruction in `ai-instruction.txt` if you use an assistant. Supply the cards and your stated preferences. If AI is unavailable, complete the same table manually.
4. Check every returned fact against an opened card. Missing warranty, noise or dimension information stays UNKNOWN or needs confirmation. AI may not estimate it.
5. Check width and connector constraints before preferences. Use only satisfied / not satisfied / unknown. An unmet constraint rules out the option in this exercise; unknown requires checking, not exclusion as if failure were proved.
6. Change only the preference from easy carrying to quiet operation. Keep source evidence and constraints fixed. Record a different interpretation only when supported; unknown noise data cannot become quietness evidence.
7. Compare your work with `expected-checks.md`; do not treat it as a purchase recommendation. Complete `reflection.md` before deciding.

## Useful distinction
Evidence: “The inspected A1 card lists a carrying handle.” Interpretation: “A1 may suit someone who values portability.” Decision: “I choose A1.” The first is a source claim, the second depends on priorities, the third remains yours. A source's statement is not independent proof of real-world performance.

## Arithmetic and manual fallback
No weighted score is needed. Optionally check shelf fit with a spreadsheet: if the width cell B2 is numeric, `=IF(B2<=35,"satisfied","not satisfied")`. For missing width use a separate unknown status; never enter 0 to fill a gap. If your spreadsheet uses semicolon separators, adapt to its locale. Inspect the referenced cell and confirm by hand: 32 <= 35, 38 > 35. A stated width can still need real-world clearance confirmation; the exercise's simple width comparison does not claim total physical fit.

Do not upload private purchase records or account data. These supplied examples require no sign-in, installation, paid plan or external action. The next lesson chooses decision criteria; this lesson does not prescribe ranking weights or automate a final choice.
