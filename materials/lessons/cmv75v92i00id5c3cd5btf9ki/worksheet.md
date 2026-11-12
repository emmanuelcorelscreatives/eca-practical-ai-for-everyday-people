# Extract Actions Without Inventing Owners
Emmanuel Corels Academy · Practical AI for Everyday People · Lesson 112

This is a self-authored fictional community-event practice kit, with no real participants or confidential records. `Community_Event_Planning.wav` is deliberately synthetic (eSpeak NG), not a real recording. Long quiet gaps preserve the exact source timestamps taught in the lesson. The audio is for practicing evidence replay, not voice quality or ASR benchmarking. Do not upload real voices without the permission required by your organization and local rules.

## Open and practice
1. Download and extract the complete lesson ZIP. Open `demo.html` locally in a current browser; no account, server, network, recording or upload is needed. Press play or use the timestamp buttons to replay the supplied audio. It starts with silence; use 00:42 to hear the first sentence.
2. Read `corrected-transcript.txt`, keeping the audio and transcript separate from your extraction. The transcript is authored ground truth for this fictional exercise, not automatically certified transcription.
3. Open `exercise-actions.csv` in any spreadsheet, or copy the five column headings into a notes app. Fill the rows using only explicit commitments, dates and conditions. Write “Not stated — confirm” for missing information.
4. Optionally copy `extraction-instruction.txt` with the fictional transcript into an authorized extraction tool. Treat its output as generated, not evidence. No particular product or paid plan is required. Manual extraction is an equivalent fallback.
5. Replay every supporting passage. Compare your result with `reviewed-actions.csv`; that file is an authored checked answer key, not a claimed model output. Keep the six rows and source quotes intact.
6. Write the three questions: who asks the printer; who owns the checklist; what is Mateo’s deadline? Neither the question addressed to Sofia nor Omar’s proposal assigns them responsibility.
7. Now open `confirmation.txt`. Update only Mateo’s missing due date to 21 October 2026 and add the confirmation as a distinct evidence note. Do not treat it as part of the original recording.
8. Select a TaskBoard Demo view (Scene 54 or 55). Enter a title, owner, due date and evidence note, check that you reviewed the source, and press “Save practice task”. The task list is local to this browser; “Clear practice tasks” deletes only this app’s practice entries. Transfer only supported work to this new practice task list. Leila’s venue map is due 16 October; Sofia’s accessibility note is due 20 October; Mateo’s booking confirmation is due 21 October after the new confirmation. Keep the badge order conditional on budget approval; keep printer and checklist items unassigned in the review list. This kit sends nothing automatically.

## Expected checks
- Exactly six original rows, one proposal and one explicitly conditional purchase.
- Omar is not the printer-enquiry owner merely because he proposes it.
- Sofia has not accepted the checklist; “before orientation” is not a dated deadline.
- Mateo is an accepted owner, initially without a due date. Missing timing does not erase the action.
- Sofia’s accessibility acceptance at 03:48, not Omar’s question alone at 03:20, supports her assignment.
- Friday 16, Monday 19, Tuesday 20 and Wednesday 21 October 2026 are the correct weekdays.
- A nearby date is never borrowed into a task without a clear link.

## Files and reproducibility
`build_audio.py` reproduces the synthetic practice recording using Python 3 and eSpeak NG (optional; the ready-to-play WAV is already included). Run `python3 build_audio.py` from this folder after installing eSpeak NG with your operating system’s package manager. It makes no network calls and writes `Community_Event_Planning.regenerated.wav`, preserving the supplied recording. Use `--output PATH` for another new local output path. Exact reproduction is checked against the supplied recording; a different eSpeak version may require inspection. `verify.py` uses Python 3 standard libraries to check row counts, dates, missing fields and waveform length: run `python3 verify.py`. `verification.json` records the actual check run for this supplied kit.

`demo.html` is a locally authored ClearNote Demo 1.0 / PlainNotes 1.0 / TaskBoard Demo 1.0 teaching app, explicitly fictional. It is not a screenshot or representation of a commercial tool, Windows certification, live AI output, or a real meeting. Its evidence display, audio playback, reviewed answer key and local practice task list are operational; it does not claim to run a transcription or extraction model. Browser rendering may vary; the data files remain the authoritative exercise inputs.

## Reuse
The Academy’s fictional text, CSV, HTML, Python and synthesized practice audio in this folder are supplied under CC0 1.0. eSpeak NG is an external tool, not redistributed here. Use this dataset for learning; it grants no rights to other people’s private recordings.
