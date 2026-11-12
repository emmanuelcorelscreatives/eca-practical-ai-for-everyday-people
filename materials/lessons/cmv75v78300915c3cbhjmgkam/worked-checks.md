# Worked checks and spreadsheet entry guide
These are expected mathematical results for fictional data, not captured application output.

## Percentage
25 / 100 = 0.25. Then 0.25 × 80 = 20 units. A rough check: one quarter of 80 is 20.
Storing 25 and multiplying by 80 gives 2000 units, a factor of 100 too high. Formatting stored 25 as a percentage gives 2500%; stored 0.25 displays as 25%.

Optional spreadsheet: in a fresh sheet enter 0.25 into B2, 80 into C2, and type =B2*C2 into D2. Format B2 as a percentage. Expected D2: 20. Inspect the actual underlying value as well as the display; spreadsheet formula-bar presentation may vary. Do not force a misleading screenshot in which stored 25 displays as 25% under ordinary percentage formatting.

## Currency
USD subtotal = 80.00 USD. EUR subtotal = 40.00 EUR. No combined-currency result is justified. A numerical addition of 80+40 does not supply a unit or an exchange rate. Record rate source, date, pair, direction, rate and fee information before any conversion. No formula for conversion is executed here.

## Localized number
After source confirmation, 1.234,56 and 1,234.56 each represent 1234 + 56/100 = 1234.56. In a fresh numeric cell, type =1234+56/100. Expected mathematical result: 1234.56; a locale may display that same quantity as 1.234,56. Preserve each source string as text beside the normalized value. Deleting all punctuation yields 123456, which is 100 times 1234.56.

## Date
Before clarification: 04/05/2026 could mean 4 May 2026 (day/month/year) or 5 April 2026 (month/day/year). After the D1-specific clarification: 4 May 2026 = 2026-05-04. Formatting can change how a stored date appears; it does not prove the intended source order. No date conversion is justified before source confirmation.
