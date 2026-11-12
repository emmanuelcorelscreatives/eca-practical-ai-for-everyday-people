# Community Workshop Check — learner guide
Practical AI, Stage 10, Lesson 57: Percentages, Averages and Totals.
All data are self-created fictional workshop figures. They are not a real customer report or evidence of software output. Use paper and a calculator, or any spreadsheet; an assistant is optional. No account, purchase, upload or code is required.

## 1. Inspect before calculating
Open attendance.csv in a spreadsheet or copy it starting at A1 in a blank sheet named Community Workshop Check. The header is row 1, and B2:B4 must contain 24, 30, 36. Confirm attendee counts refer to three separate sessions, use one unit and include each intended observation once. These are attendance observations; do not infer 90 unique people across sessions. Estimate a total around 90 and an average around 30.

In A5 type Total; in B5 enter =SUM(B2:B4). In A6 type Arithmetic mean; in B6 enter =AVERAGE(B2:B4). Inspect the exact range in the formula bar. Expected values are in answers.md. Independently type 24+30+36 on a calculator, then divide by 3. Write what each result measures.

## 2. Missing and zero are different
Open comparison.csv in a separate sheet starting A1. B3 is genuinely empty; C3 contains a recorded 0. Use =AVERAGE(B2:B4) and =AVERAGE(C2:C4) outside the input range. Count recorded observations in each column. The first is the mean of known observations only; it does not resolve the missing session attendance. Do not silently fill a missing value with zero. Paper fallback: sum the two known values and divide by two; separately sum the three recorded values and divide by three.

## 3. Choose the question and denominator
Read quantities.csv. Values 0.20 and 0.25 are fractions representing 20% and 25%, not 0.20% and 0.25%.
For filled places, calculate =18/60 and format the result as percent. With a calculator use 18/60*100 and append %. Do not multiply by 100 and then apply spreadsheet percent formatting, which would display 3000%.
For participation, calculate =(92-80)/80 and display as percent. Reverse direction using =(80-92)/92. Keep full precision until reporting to two decimal places. Label the sign or use the word decrease.
For rates, calculate =(0.25-0.20)*100 as a plain number and label it percentage points. Calculate =(0.25-0.20)/0.20 and format as percent for relative change. With rates typed as 20% and 25%, the equivalent relative formula is =(25%-20%)/20%.

## 4. Ask, inspect, reconcile
Use prompts.md if an assistant is available. Treat any response as generated, then reproduce each operation with inspected spreadsheet formulas or a calculator. Populate audit-template.csv with your actual observations; leave the assistant column blank if none was used. No assistant run is claimed by this kit.
Check units; intended values included once; missing versus zero; correct whole; original denominator for change; percent versus percentage-point label. A numeric match alone is insufficient. For a mismatch, trace inputs, range, units, denominator and label before accepting an answer.

## 5. Practice and fallback
Complete exercises.md before consulting answers.md. For every paper calculation record inputs, operation, result, label, assumptions and unresolved values. If a whole is missing or an original value is zero, leave the requested percentage unresolved with a reason. Never guess a denominator. The next lesson develops formula and range inspection further.
