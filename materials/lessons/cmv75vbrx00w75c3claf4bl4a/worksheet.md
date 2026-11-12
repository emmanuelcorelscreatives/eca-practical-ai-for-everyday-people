# Connect Apps with Limited Permissions — Lesson 195

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 33

This kit uses self-created fictional data. It performs no live authorization, sends no messages and does not connect to Zapier, Make or any other service. Real permission wording and connector capabilities vary. Never infer a narrower permission from a friendly connection label.

## Your boundary

One new **Event Interest Test** response, exactly three fields, one private draft in a dedicated **Test Automation** destination. Keep the workflow OFF. No contacts, older responses, unrelated forms, account-wide editing, sending, publishing, public sharing or deletion permissions are needed for this exercise.

| Step | Required data | Required action | Not required |
|---|---|---|---|
| Form trigger | Name placeholder, Event choice, Note | Read one new test response | Contacts, older responses, unrelated forms |
| Draft action | Only those three mapped fields | Create one private test draft | Send, publish, share publicly, delete, browse unrelated files |

## Fictional input

Use `sample-response.csv` or `sample-response.json`. Name placeholder: **Sample Person**; Event choice: **Morning session**; Note: **Please provide accessibility information.** The name and event are invented; the note is a harmless example, not a disclosure about a real person.

## Before authorizing any real connector

1. Read service identity, intended test account and every actual requested capability. If any wording is unclear or you cannot explain why access is needed, cancel the pending authorization without granting it. Inspect the connector documentation or ask your account administrator before proceeding. Apply this rule separately to both trigger and action connections. Do not put credentials or private account details in this kit.
2. Compare the literal request against the boundary above. If optional scopes exist, retain only what the exercise requires.
3. If a fixed scope exceeds the boundary, cancel. Choose a suitable alternative or a separate test account containing no unrelated material, after evaluating the still-broad capability. The test account does not make an unsuitable scope narrow.
4. If no suitable connector/plan/admin permission exists, use the manual fallback below. Do not buy, approve extra access or activate a workflow merely to finish.
5. Inspect the draft connection separately; trigger approval does not authorize the action. Record actual words in `permission-record-template.csv` only after observing them.

## Manual fallback — no live connections

Open `practice.html` locally in a browser. The worksheet is a genuine working local exercise, not a vendor UI simulation. Select each permission case and compare your decision with `answer-key.md`. Press **Create local practice draft** once. Check that exactly one local practice draft shows the three exact sample fields and that its simulation state is draft-only. This page makes no network requests and cannot prove a cloud file is private: if you use a real destination, separately inspect its actual sharing controls.

Delete the local draft using its button. Complete the cleanup record with an honest manual-fallback status: no live workflow or app connections existed. Reload resets this in-memory exercise; nothing is sent, published or stored remotely. Use the CSV template for your own record. A draft is not evidence of live connector authorization.

## Optional real-platform exercise

Only with an appropriate test account and acceptable scopes, choose the exact Event Interest Test source and map the three fields. Keep workflow OFF. If available, run one isolated platform test. Open the actual destination: verify exactly one private draft, matching values and correct folder. Stop if any older/private real record appears. Do not treat a success badge as proof.

Clean up separately: remove the test output, confirm workflow OFF then delete/inactivate the test workflow, inspect shared-connection dependencies, remove only exercise connections, and refresh to verify removal. Disconnecting does not remove copied data. If removal fails, record unresolved access and use the provider's authorized-app controls or administrator support; never mark it confirmed prematurely.

## Exercises and checks

- Complete the six scope cases in `permission-cases.csv` before reading answers.
- Create and inspect one local draft, then attempt a second: the page must prevent a duplicate.
- Remove the draft and record all five cleanup categories, distinguishing observed state from not applicable.
- Explain why deleting a draft, disabling a workflow and revoking access are separate actions.
- Prepare for Lesson 196, **Add an AI Transformation Step**, without implementing that later lesson here.

Run `python3 check_kit.py` optionally to verify supplied sample/schema/case coverage. This is a file check, not a live authorization check.
