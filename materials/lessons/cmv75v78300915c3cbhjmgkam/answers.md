# Answer key
Use after your attempt. All results below are exercise expectations.

P1: wrong numerical interpretation, with a percentage-storage risk. Source confirms rate 0.25, display 25%, base 80 units, result 20 units. Incorrect 25 × 80 = 2000; stored 25 with ordinary percentage formatting displays 2500%. A claimed display/storage mismatch must be investigated, not reproduced as fake software output.

C1: mixed currency units. Keep 80.00 USD and 40.00 EUR separately. Converted result and overall currency total remain blank. Missing: exchange-rate source, rate date, currency pair, direction, rate and fee information. Never label 120 as USD or EUR from these inputs.

N1 and N2: format ambiguity before clarification. Ask for decimal/grouping convention for each source. After clarification, both normalize to 1234.56, checked by 1234 + 56/100. Original strings stay unchanged. Workbook locale is supporting context, not proof of correct import parsing.

D1: initially unresolved. Day/month/year gives 4 May 2026; month/day/year gives 5 April 2026. After the supplied source confirms day/month/year, record 4 May 2026 and 2026-05-04. A display-format change alone is insufficient evidence.

E1: rate 0.125; 0.125 × 64 = 8 units. Manual check: one eighth of 64 is 8. The claim 800 is 100 times too large.
E2: 30 USD and 20 EUR separately, no converted total.
E3: 2500.75; check 2500 + 75/100. Stripping punctuation to 250075 creates a 100-fold error.
E4: unresolved; candidates 7 August 2026 and 8 July 2026. Ask for source date order; leave verified date blank.
E5: source-specific month/day/year means 8 July 2026, or 2026-07-08. Do not apply E5's evidence to E4.

Accept a completed audit only when every interpretation is tied to its supplied source, arithmetic is repeatable, and unresolved conversion/date fields remain visibly unresolved. An assistant warning is a lead for inspection, not independent mathematical or source evidence.
