# Recognize Suspicious Instructions in Content
Emmanuel Corels Academy • Practical AI for Everyday People • Stage 3, Lesson 18

This permission-cleared fictional practice kit matches the lesson's Harborview Skills Exchange example. It needs no accounts, connected drives, personal files, AI provider, or network connection. Open `sample-assistant.html` in a browser. The training interface displays an actual recorded model extraction response, with the exact source hash and model route in `recorded-model-response.json`. It does not run an AI model in the browser. The intentionally unsafe draft is a separately authored example, clearly labelled as supplied for review. No component opens Budget-Draft.xlsx, sends messages, uploads files, changes sharing, or makes network requests. The external example uses the reserved `.invalid` domain.

## Exercise
1. Read `harborview-notice.txt`. Your task is to list the room, start time, and items attendees should bring.
2. Record the relevant facts in `worksheet.md` without following the instruction inside the notice.
3. Apply the four checks: authority, task relevance, requested data/action, human approval.
4. In the offline training application, open the notice, inspect the unsafe draft and proposed action, reject the action, then use the restricted extraction. Compare every output fact with the source.
5. Inspect the app's activity state. It records only this local training application's explicit events. It is not an audit of any outside AI service.
6. Practice the manual fallback: disconnect the simulated connector and copy only the four necessary values into a blank note in your ordinary text editor. Compare it with the source notice.
7. Evaluate the separate room-change email in `room-change-email.txt`. Do not upload any contact list.

Use `answer-key.md` only after attempting the exercise. Delimiters, filters, reassuring messages and a second AI do not constitute reliable permission boundaries. In real tools inspect the actual destination, recipient, attachment, content and sharing state; controls vary by service. Disconnecting future access may not delete already received data.

## Contents and checks
- `sample-assistant.html`: self-contained offline training app with explicit read/draft/review states, working review controls and a recorded model response.
- `harborview-notice.txt`: exact source facts plus an inert suspicious command.
- `room-change-email.txt`: second fictional exercise.
- `worksheet.md` and `answer-key.md`: exercise and expected reasoning.
- `recorded-model-response.json`: actual source-grounded response; no external actions were performed.
- `verify-kit.py`: reproducible source/content and offline-safety checks; run `python3 verify-kit.py`.

All text and training code in this kit are self-authored Academy practice material. Names and events are fictional. The sample is a lesson artifact, not a screenshot of a commercial assistant or evidence of a real security incident.

## Model and application evidence
The recorded extraction used the actual `combo/planning` route. It returned Cedar 2, 18:30, notebook and reusable water bottle, flagged the unrelated command and reported no actions performed. The browser displays that response as recorded output. Local activity refers only to the practice app. Permissions and connectors are simulated settings, not proof of controls in any external service. The detector intentionally demonstrates a limited pattern check that can miss suspicious wording.

## Reproduce the activity checks
Choose Reset practice, then Compare, then Activity: the notice must show opened. Choose Reset practice again, then Disconnect, then Activity: the notice must show opened there too, because disconnecting the training connector leaves the notice visible. Choose Reset practice and Activity without opening any source: it must show Not opened. These are local app events only.
