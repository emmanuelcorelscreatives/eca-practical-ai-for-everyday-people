# Lesson 102 — Refresh Information That Can Change

Emmanuel Corels Academy · Practical AI for Everyday People

## What you will practise
Recheck prices, schedules, availability and rules close to a real decision. This offline kit uses only the lecture’s fictional Harbor Science Centre outing and Riverline Transit. It contains no real private data, live search, booking or payment. Dates/times are simulated exercise observations, not a claim about today.

## Open the practice sources
Unzip the kit and open `index.html` in a browser. Local links work without internet or installation. Open `initial.html` first; do not read the answer key until you have made your note. `research-search.html` illustrates an AI-assisted lead and prompt; it does not call an AI service. The venue/transit snapshots are source evidence within this fictional scenario, never real-world authority.

## Exercise 1 — Scope and initial evidence
Plan Saturday 17 October 2026 at Harbor Science Centre for two adults, arriving before 11:00 and returning that evening. Copy `evidence-note-template.md` to your notes app. Record exact scope, opened page, simulated check time (venue 14 October 10:20; planner 10:27), price per adult, subtotal, date-specific hours, availability, entry conditions and planned train. Keep the service charge and final total unresolved. Distinguish generated lead from opened evidence. Do not treat regular opening hours as the date-specific exception.

## Exercise 2 — Refresh without erasing history
Move the exercise clock to 16 October 2026 at 19:00 and open `refreshed.html`. Preserve each initial value as Previous; add Refreshed values with this check time. Mark which fields changed, which stayed the same and which became clearer. Calculate the subtotal difference. Check the revised arrival against the before-11:00 requirement. Availability describes the snapshot only; it does not reserve tickets.

## Exercise 3 — Decision and unresolved checks
Write a three-item decision-impact note. Then list what remains unknown. Open `checkout-review.html` and `live-status.html`: neither completes a purchase or supplies live status. Schedule separate checks at checkout and just before departure. Never turn blank alerts into a claim that service is normal.

## Manual fallback
If AI-assisted search fails, open saved source pages directly and compare date, place, variant/customer type, quantity, total cost, availability, schedule and conditions with your dated note. If retrieval itself is unavailable, retain old values as historical and mark current values unresolved; do not invent a fresh confirmation.

## Check your work
Compare your completed note with `answer-key.md` and `completed-evidence-note.md`. Use the prepared classroom lead button on `research-search.html`; this only reveals a saved fixture, never makes a provider call. Optional: run `python3 verify_scenario.py` to verify the kit’s arithmetic, arrival constraint, unresolved fields and local links using only Python’s standard library. This verifies supplied exercise data; it does not certify your note or any real-world facts. Keep the fictional source snapshots and check times attached to your work.
