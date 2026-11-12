# Original media and reproduction notes

This is a deliberately simple, fictional Academy recording, not a private conversation. The original 26-second mono PCM recording has 573,300 frames at 22,050Hz. Two generic eSpeak-NG voices were used: `en-gb` for Speaker 1 and `en-us+m3` for Speaker 2, both at rate 155 words/minute. Neither voice is a clone of a human instructor. The exact voice texts, placement and actual generated speech-end times are in `recording-and-cues.json`.

For equivalent practice media, use your own authorized recording of the four exact lines, retain the speaker changes, and add a short musical cue at nine seconds. Recheck all timing against your actual recording; synthesizer versions may produce different durations. Do not claim the supplied cue windows were measured from a replacement recording. The exact supplied WAV remains the reference for this kit.

The musical cue is an original 1.5-second synthesized three-note chord (261.63, 329.63 and 392Hz), beginning at 9.000 seconds. Its label is `[music begins]`. No door sound is present. The video is a simple original digital conversation-card illustration accompanying that unchanged supplied audio; it does not represent footage of real people.

`waveform.json` was measured from the supplied original audio as the maximum absolute normalized sample amplitude in each 0.05-second interval. The application renders that real envelope and caption boundaries from the exact supplied JSON, not an invented vendor timeline.

The Qwen3-ASR text in `actual-asr-transcript.txt` came from an actual separate transcription of the original WAV without expected text or forced alignment. Its metadata retains source/model hashes. It contains no word timing or speaker labels. The separate starting WebVTT includes intentionally authored timing/speaker/reading defects for the exercise; those added defects are not attributed to Qwen. A learner can instead use a real editor's caption generation when available.

The complete caption-practice application is self-contained HTML/JavaScript and uses only the supplied same-folder WAV and data embedded from the recording metadata. Use the controls to import the provided draft, edit cue wording/start/end, replay the original and export a separate WebVTT. The generated-source and runtime proofs are retained by Academy production; no coding is required in this lesson.

The earlier caption-workbench.html is retained only as immutable source for course illustrations and intentionally has a smaller feature set. The complete learner application is caption-practice.html; it additionally inserts/splits cues and imports the exported caption file into real native full/narrow video players.
