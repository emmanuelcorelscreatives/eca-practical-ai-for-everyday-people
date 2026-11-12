# Lesson 194 — Triggers, Actions and Conditions

Emmanuel Corels Academy · Practical AI for Everyday People

This permission-cleared, self-created practice kit implements the lesson's fictional community workshop enquiry example. All people and submissions are invented. `example.test` addresses are reserved classroom placeholders. No message is sent, no service is connected, and no external action is performed. The Automation Practice Board is our own local classroom application, not Zapier, Make or a representation of their interfaces. No account or paid platform is needed.

## Start the exercise

Open `practice-board.html` in a browser. It works offline without dependencies. The page's state is held in memory and disappears on reload. Keep private information out of this classroom app. Use `fictional-submissions.json` as the exact source records.

1. Choose FS-104 and select **Load fictional sample**. Check that the trigger reveals Submission ID, Name, Reply address, Request type and Message.
2. Read the condition: value **Request type**, comparison **equals**, criterion **Workshop request**. Select **Evaluate condition**. FS-104 must match.
3. Inspect all mappings: Name → Contact name; Reply address → Reply address; Message → Enquiry summary. The identifier and category are also retained in the created record.
4. Select **Preview mapped record**. The panel says **PREVIEW ONLY**. Verify Samira Noor, samira@example.test, Workshop request and Saturday session for beginners against FS-104.
5. Select **Create simulated record**. Confirm one workshop row and compare every field with the source. A green label alone is not sufficient evidence.
6. Load FS-105, evaluate, preview and create. Its Venue question category must produce a **NO MATCH** and a manual-review record with **Review category manually**. The workshop draft count must remain one.

The app prevents duplicate insertion of the same submission into the same table within a session. This is a classroom convenience; it does not demonstrate production deduplication or integration reliability. The controls are deliberately fixed to one category rule so the boundary is visible. The optional missing-information example adds a local clarification guard; do not confuse that guard with the single category comparison being taught.

## Manual fallback: no software required

Use `manual-worksheet.csv` in a document, spreadsheet or on a whiteboard. For FS-106, copy Request type exactly: **Workshop request**. Record **MATCH**, route it to Workshop review draft, then copy the source fields without rewriting the message **Evening introduction**. For FS-107, record **NO MATCH** for **General question**, and route to Manual-review record. Do not alter the first workshop draft. Finally compare each copied field to its original.

## Missing data and exact comparisons

FS-108 deliberately has no reply address. Do not invent one: record **Manual clarification** and identify Reply address as missing. The lesson explains this boundary separately from the one-rule build. Exact comparisons are case-sensitive here: `workshop request` does not equal `Workshop request`. A real form should use controlled categories or an explicitly designed normalization policy rather than silent reinterpretation.

## Four checks

- Did the trigger expose the exact submitted data?
- Did the comparison evaluate correctly?
- Did only the intended route run?
- Does the created record preserve all mapped values?

## Optional reproducible verification

With Python 3 installed, run `python3 simulate.py` to print the local outcomes, then `python3 check.py`. No network or packages are required. The check verifies five outcomes, exact field mapping, missing-data clarification, a case-sensitive nonmatch and deterministic output. The output of `simulate.py` must match `expected-results.json` exactly as parsed JSON. These checks prove this small local simulation, not the behavior or permissions of any external platform.

## Expected outcomes

| ID | Request type | Outcome |
|---|---|---|
| FS-104 | Workshop request | Workshop review draft |
| FS-105 | Venue question | Manual-review record |
| FS-106 | Workshop request | Workshop review draft |
| FS-107 | General question | Manual-review record |
| FS-108 | Workshop request; reply address missing | Manual clarification |

Stop here: connecting live apps, credentials, publishing and sending are outside this lesson. Lesson 195 prepares limited permissions.
