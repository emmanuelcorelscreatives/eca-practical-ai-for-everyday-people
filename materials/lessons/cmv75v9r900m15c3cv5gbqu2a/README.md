# Lesson 134 — Check Current Prices and Availability

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 23

This is a self-created fictional practice environment. Every seller, product listing, hotel, stock state, price and date is a teaching fixture. The fixed time **14 October 2026 07:10 UTC** is part of the authored example, not the time a real provider was checked. There are no live search, AI, maps, payment, booking or shopping connections. No order or external action occurs. Values have no specified currency: do not assign a currency or compare them to real offers.

## Run and practice

Open `index.html` locally in a modern browser. Its form controls genuinely calculate totals, change variants, validate quantity, reveal delivery only after a fictional broad area is entered and switch optional extras. Data and calculations are local; no personal information is needed. The shortlist is explicitly scripted practice material, not a live AI answer. The map-style card is a fictional directory card, not a real map or inventory source.

1. Read the requirement: two Northstar Trail backpacks, 30 L, Dark Blue, needed by 23 October 2026.
2. Use the scripted candidate shortlist only as a lead. Open Northstar Outfitters. Select 30 L, Dark Blue and quantity 2. Check that the page can supply both.
3. Before entering a broad fictional delivery area, delivery cost/date and a complete total remain unknown. Enter `Academy practice area`, then observe estimated arrival 21–22 October, delivery 8 and mandatory service charge 2. Items 96 + mandatory costs 10 = 106. Gift wrap 6 is optional and initially unchecked; selecting it changes the actual local calculation to 112. Leave it unchecked for the saved course example. An estimate is not a guarantee.
4. Open Trail Market. Its default Black 22 L price 43 is the wrong variant. Correct 30 L Dark Blue costs 51 each, but only one is available. Quantity 2 must fail; do not invent a usable total or compare it as a valid cheaper alternative.
5. Open hotel practice. Select Riverside, 4–6 November 2026, two adults, one Standard Double room. The two-night base is 180 plus mandatory 24 = 204; optional breakfast 30 is excluded unless selected, then total becomes 234. Compare a nightly amount with a stay total only after matching the basis. Read free cancellation until 30 October; the later cancellation charge amount is not supplied and remains unresolved.
6. Fill `comparison-blank.csv` or the local editable comparison sheet. Record check time, exact option, dates/quantity, availability, each cost category, conditions, total, source and unresolved questions. `comparison-expected.csv` is an answer key for the fixed fictional example only.
7. The refresh demonstration changes local stock from two to one and invalidates a quantity-two option. It does not fetch current inventory. Record the new uncertainty rather than treating the earlier timestamp as permanent approval.

## Manual fallback and stop point

A regular browser and basic sheet are enough: shortlist → open source → select exact option → calculate full payable cost → record evidence/time. In real life open actual provider pages yourself and refresh shortly before a decision. If destination, quantity, dates or options are missing, leave the full total unresolved. Keep final payment/booking under your control; this app has no purchase action.

Run `python3 verify-kit.py` for fixture arithmetic, date order, blank failed-option totals and CSV alignment. This validates authored sample data, not real prices, availability, or your personal research. See `EXERCISE.md` and `ANSWER-KEY.md`.

Source links in the sheet and CSV open fixture landing pages. Re-select the recorded exact capacity, colour, quantity and fictional delivery area; a source link alone does not preserve or prove the prior selection. The blank browser sheet has three editable rows.
