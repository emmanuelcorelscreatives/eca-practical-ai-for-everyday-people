# Worksheet: estimate, then verify

Use the checking record to label estimates, hypothetical generated answers, and independent calculations separately. Complete each task before reading answers.md. These are fictional exercises, not purchasing advice.

1. Inspect source-input.csv. Name the quantity and unit price. Is a currency specified? Are taxes, discounts and varied item prices supplied? State what can be calculated with the equal-price assumption and what remains unknown. Do not invent missing values.

2. Before calculating exactly, round 48 to 50 and 19.75 to 20. Record the approximate scale. The authored error fixture proposes 9,480 units. Is that near your estimate? Explain the mismatch in words and distinguish “about ten times the estimate” from “exactly ten times the correct result.”

3. Use 19 < 19.75 < 20 and positive quantity 48 to obtain strict lower and upper bounds. Can 9,480 pass them? Can 954? Why does passing a bound not prove correctness?

4. On a calculator enter 48 × 19.75, checking every digit and decimal before evaluation. Record the operation and result as your own observed calculation. Alternatively calculate on paper. Do not claim a supplied answer file is your observed calculator output.

5. Spot-check with a different decomposition: split 48 into 40+8. Write both products and their sum. Explain why repeating the same wrong copied input twice could produce agreement while still being wrong. Check the source inputs too.

6. Follow formula-map.md with the blank Total-column template. Inspect A2 and B2 before typing `=A2*B2`. Confirm the result, then complete all five rows. Inspect C7 with `=SUM(C2:C5)`. Count the included records and identify what is omitted. Correct the range and record both totals and their difference. Could a rounded estimate of about 1,500 prove the smaller total wrong? Explain the limits of the screen.

7. Combine 12 kilometres and 800 metres. Name one common unit first, convert, then add. Explain why 812 kilometres is invalid. Name a similar issue with hours/minutes or prices per pack/item; do not assume a pack size.

8. Compare 19.75×48 with 197.5×48. Identify the input changed by a factor of ten. Is a calculator malfunction required to explain the second total? Now assess 954: it lies inside the tighter bounds, but is it the exact total?

9. Inspect mean-values.csv. Record minimum, maximum, sum, count and equal-weight arithmetic mean. Reject or accept the plausibility of a reported mean of 31 before calculating. Does a plausible mean establish that every intended record was included? Is the true mean necessarily the midpoint of the endpoints?

10. Classify the three cases in practice-cases.csv. A: 203 tickets at about 5 units each, proposed 10,150. B: 9 boxes at about 30 items each, proposed 271. C: values from 40 to 70, proposed mean 82. Say “implausible,” “plausible but unproven,” or “impossible under stated assumptions.” Do not manufacture exact prices, box counts or a mean from approximate inputs or a range alone.

11. Optional assistant prompt: “Estimate the likely range first. Label assumptions. Then calculate 48 × 19.75 and show the operation.” If you choose to use an assistant, save its actual response separately, mark it generated material, and independently verify it. No provider use is required and no sample response in this kit is represented as a real model response.

12. Write a correction note covering decimal placement, units, row count, formula range, copied values and assumptions. Record what changed, your recalculation, and what remains unverified. Finish with a manual fallback: estimate, split the multiplication, add the products, and compare with bounds.
