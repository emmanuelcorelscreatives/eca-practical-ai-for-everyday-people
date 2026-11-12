# Optional real local synthetic-fixture demonstration

This kit includes original self-authored text, an abstract banner and the actual Academy app/generator sources. It intentionally excludes private runtime audio and exports. The course producer actually generated neutral eSpeak NG speech, imported it and the banner, decoded and played audio, detected a changed negative caption word, restored the exact script, exported an MP4, fully decoded it and played a WebM preview derived from that saved MP4. The local demonstration does not claim a human original recording or outside consent.

## Requirements and alternatives
The optional source runner needs Python 3, eSpeak NG (`espeak-ng` on PATH) for generation, FFmpeg (`ffmpeg` and `ffprobe` on PATH) for export, and a current local browser. No Python packages or external account are required. These are optional local tools, not mandatory programming lessons. If unavailable or uncertain, follow the ordinary guide in an editor you already have or complete the text/abstract-graphic fallback. Review the actual installed voice/software terms; espeak-ng-copyright.txt preserves the producer’s installed software copyright notice, not a grant over another person.

## Local use
Work in a new private copy of the kit. Keep a backup of supplied inputs. In a terminal opened in that copy, optional commands are:

    python3 generate-practice-audio.py
    python3 run-private-demo.py

Generation refuses an existing runtime fixture; it will not replace your recording. It writes `practice_narration.wav` and `practice_narration.srt` plus a local generation receipt, using the exact supplied text and actual PCM frame counts for caption sentence boundaries. This is deterministic synthesis, not ASR or a claimed human recording. Do not publish these private runtime outputs.

The launcher starts an owned local server on 127.0.0.1, prints its actual URL and optionally opens the browser. Press Enter in its terminal to stop that exact server. It does not expose a public link. Verify your host and filesystem access separately.

In the app, import only `self_created_banner.jpg` and your generated `practice_narration.wav`. Select `Licensed neutral synthetic narrator`. The original-recording option is deliberately blocked because this fixture does not supply one. Listen with the actual audio controls. Inspect the real waveform/duration and compare every caption with the script/audio. You can select `not` for comparison. Changing it to `now` should block export; restore the exact text before proceeding. Review meaning and unintended people honestly; the checkboxes are manual records, not an automated permission decision.

Export locally. Inspect the actual saved `Edited Output/practice_event_clip.mp4`, the app’s honestly labeled derived WebM preview if needed, the output metadata and actual permissions. `Originals` copies must stay byte-identical. The source runner is for this exact fixture, not a general editor or validator for arbitrary human recordings. Never imply upload, publication, authenticity or consent from a successful export.

## Safety boundaries of this exercise
No cloning, impersonation, human speaker identity or real event is supplied. The default eSpeak NG en-us voice is a machine voice. A neutral-voice route does not grant rights over added source text or people. Stop on uncertain inputs, changed purpose or changed audience. Manual fallback remains available.

The exact-fixture app verifies cryptographic hashes of the selected image and audio against the actual synthesis receipt and on-disk source before export. A substituted image or WAV is blocked; this is not a general editor for arbitrary media. Each new MP4 export runs and records its own checked full decode before success is reported.
