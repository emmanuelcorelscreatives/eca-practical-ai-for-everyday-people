# Lesson 193 — Decide Whether Automation Is Worth It
Emmanuel Corels Academy · Practical AI for Everyday People · Stage 33

This is a self-authored fictional practice kit, not a platform export or evidence of a live automation. No sign-in, connector, payment or external action is needed. Use a text editor or import the UTF-8 CSVs into a spreadsheet. Preserve the source inputs and compare them with every proposed draft.

## 1. Define the task and safe boundary
Task: when a fictional practice request arrives, copy its subject, details and contact preference into a draft for human review. Stop at human review. Do not send, publish, buy, delete, or edit shared records. The task is narrow; unrelated requests go to manual handling.

## 2. Measure first
Open `task-assessment.csv`. Describe your own task, typical frequency, variation, consequence of an error, and manual fallback. Time a complete manual run from receipt to checked result. Use `effort-observations.csv` to record observed minutes, including review and correction. Leave unobserved quantities blank; zero means measured or justified zero, not unknown. Frequency must represent the same stated period used in all totals.

## 3. Simulate three requests
Read `practice-inputs.csv`. For each record, fill `simulation-worksheet.csv` with trigger, copied fields, transformation, draft result, review question and outcome. Keep the original alongside your draft. A normal in-scope record can become a draft; a missing required detail needs clarification; an out-of-scope request must not be squeezed into the normal path. No email addresses or real recipients are supplied.

Map subject → draft subject, details → draft body, contact preference → review note. A generated rewrite is proposed wording, not independent proof. Do not invent missing details. Check required fields, fidelity to the input, visible missing details, scope and a recorded human decision.

## 4. Compare complete effort
For one consistent period, manual total = number of runs × complete checked manual minutes per run. Automation total = one-time setup + one-time testing + number of runs × (review + expected correction + monitoring minutes per run) + maintenance minutes for the period. Recurring monetary cost is a separate amount and currency; do not silently add money to minutes. If monitoring is measured for the whole period, record it once rather than both per run and per period. Use `decision-calculator.py` optionally with your own measured JSON inputs. It reports an arithmetic comparison, not permission to automate. A small time difference can reasonably favor a simpler manual method. High consequences or unresolved checks can rule out automation even if estimated minutes are lower.

## 5. Decide and retain a fallback
Record observed totals, uncertainties, failure consequences, decision and fallback in `decision-record.csv`. A valid result is to stay manual. If testing automation, keep it narrow and draft-only with human review. Manual fallback: copy input, create draft, check, save for review. Record no completed external action.

## Self-check
Compare your simulation with `expected-checks.md` only after attempting it. These are illustrative expected decisions for this fictional exercise, not measured platform results. The optional calculator uses no network, packages, accounts or live automation. Run `python3 decision-calculator.py example-assumptions.json` then `python3 check-calculator.py`; the example values are explicitly invented assumptions for arithmetic practice and must not be called measured savings.
