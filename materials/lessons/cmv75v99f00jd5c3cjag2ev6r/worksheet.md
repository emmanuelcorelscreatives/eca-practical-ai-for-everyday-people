# Test Assumptions and Tradeoffs — Academy practice kit
All option scores below are fictional teaching values, not checked product evidence or buying advice. AI may organize this comparison; you choose priorities and make the judgment.

## Evidence, preferences, constraints, unknowns
Evidence: in this exercise the supplied fictional scores. In a real decision, record the actual opened source and date; generated organization is not opened evidence.
Preferences: the weights you choose. Constraints: offline use is required. Option C fails offline use and is excluded from recommendations regardless of its illustrative total. Unknowns: Option C support cost is unknown; its fictional support-quality score does not resolve support cost.

## Reproduce the lesson
Open scores.csv and weights.csv in a spreadsheet, or use calculate.py with Python 3. Copy ease, reliability, cost and support scores into B:E and weights into B6:E6 (equal) and B7:E7 (convenience scenario). In F2 use =SUMPRODUCT(B2:E2,$B$6:$E$6); in G2 use =SUMPRODUCT(B2:E2,$B$7:$E$7), then fill through row 4. Formula ranges must be the same size. Five always means better, including cost: a higher cost score means more favorable cost, not a higher price. Check that each weight row sums to 1 (100%).

Equal weights 25%,25%,25%,25% give all three illustrative totals 4.00. Convenience scenario 40%,35%,20%,5% gives A 4.15, B 4.20 and C 3.65. C remains ineligible. The four numbers are one named priority scenario: ease increases and the remaining shares rebalance to retain 100%; scores and offline requirement stay fixed. Do not infer a pure causal effect of only one numeric weight, since the other shares change too.

Manual Option B check: 5×0.40 + 3×0.35 + 5×0.20 + 3×0.05 = 2.00+1.05+1.00+0.15 = 4.20.

## Exercise
1. Run `python3 calculate.py` and compare expected-results.csv.
2. Record why C cannot win even if its raw total rises.
3. Test a separate reliability-priority scenario: ease 20%, reliability 50%, cost 20%, support 10%. Keep source scores fixed. Predict and calculate the eligible leader.
4. Leave unknown information blank or explicitly marked unknown. Never enter neutral 3 merely to complete a ranking. An assumption must be labeled as a scenario.
5. Complete decision-record.md. Check opened evidence, visible unknowns, 100% weights, aligned formula ranges and consistent scoring direction. Explain the result conditionally; tested stability does not prove universal correctness.

No private account data or paid software is needed. CSV files are interoperable; calculate.py uses only the Python standard library. Python results are actual executions of the fictional worksheet, not observations about real products.
