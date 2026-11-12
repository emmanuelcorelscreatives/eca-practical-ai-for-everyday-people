# Lesson 182 — Choose the Right Tool for Each Step

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 31

## What you will practise
Use search to locate evidence, open the source before recording its meaning, use a spreadsheet to calculate, and use an editor to present a checked one-page budget note. The three roles matter more than brands. Everything in this kit is fictional, self-authored practice data; credits are a training unit and these are not real offers or vendor websites.

## Start with the brief
Neighborhood Skills Workshop needs a one-page planning estimate for a four-hour workshop. Assume 35 attendees; attendance is not confirmed. The unknowns are venue hire, printing and refreshments. Open `sources/index.html` in a browser, follow each actual local link, and inspect the full source pages. The local practice-source finder is an honest offline alternative to public search, not a fabricated Google result. `practice.local` addresses in the lesson are fictional labels, not live sites or links to visit.

1. Before opening evidence, use `source-register-blank.csv` and leave all three amounts blank. Never ask an AI assistant to invent a price.
2. Search the local index for the venue, printing and refreshments topics; open each matching page. Record title, local link, your actual access date, rate, unit and conditions. Use a new access date for your run; 15 October 2026 in the saved lesson is an illustrative practice date.
3. Read venue price and four-hour/furniture condition together. Record the printing minimum, not only the per-page rate. Preserve the refreshments per-attendee unit.
4. Open `workshop-budget.xlsx` in any compatible spreadsheet. The `Inputs` sheet starts with three empty costs for practice. Fill quantities and unit costs from evidence, then enter `=B2*C2`, `=B3*C3`, `=B4*C4` and `=SUM(D2:D4)` in D2:D5. Compare all three rows against the sources. Keep the attendance assumption visible.
5. After doing the exercise, open `Checked answer` in the same workbook or `expected-budget.csv`. Check the formulas and their referenced cells as well as their displayed answers. A total over the wrong range can still look plausible.
6. Open `budget-note-template.html` in an editor, or copy its structure into your preferred document editor. Transfer the three checked costs, total and credits unit. Preserve 35 assumed attendees, the four-hour hire including furniture and the printing minimum.
7. Compare your note against the spreadsheet and sources. Replace any claim of confirmed attendance with assumed attendance. Do not turn a planning estimate into a booking or purchase.
8. Export or print your completed note to PDF using your editor's actual controls. Open the real exported file and inspect its title, three amounts, total, unit, assumption, conditions and source details. Check that all content fits, is readable and is unclipped. `expected-budget-note.html` is a printable answer document, not a claimed executed PDF export.

## Expected checks
Hall: 1 × 180 = 180 credits. Printing: 100 × 0.12 = 12 credits. Refreshments: 35 × 2.40 = 84 credits. Total: 180 + 12 + 84 = 276 credits. Exactly three cost rows contribute. Attendance remains an assumption. The venue rate is for four hours and includes tables and chairs; printing has a 100-page minimum.

## Manual fallback
If a preferred app is unavailable, record evidence in plain text, use a calculator and choose any capable editor. The included `check_budget.py` can independently reproduce exact decimal arithmetic with Python 3, but coding is optional and is not required for this lesson. If a source is missing, leave the amount blank and request the missing information; do not manufacture a total from guesses. Add tools only when they improve evidence, calculation, presentation or checking.

## Practice variations
- Change assumed attendance to 40 while retaining the other source terms. Expected refreshments 96 credits, total 288 credits; mark the new assumption in the note.
- Hide the refreshments source. What should remain blank? The refreshments rate and resulting amount, and any complete total dependent on it. Request evidence rather than guessing.
- A draft says “35 confirmed attendees.” Correct its certainty while preserving the number and all unchanged facts.

## Deliverables and self-check
Save your source register, formula workbook and exported one-page PDF. A pass requires three traceable opened sources, exact units/conditions, valid referenced formulas, the independent arithmetic check, an explicitly assumed headcount, and an opened readable final PDF. `exercise-checklist.md` records these observations. Keep all files local; no account login, external sending, purchase or publication is required.

All kit content is self-authored fictional training material, licensed CC0-1.0. No private user files or accounts are included.
