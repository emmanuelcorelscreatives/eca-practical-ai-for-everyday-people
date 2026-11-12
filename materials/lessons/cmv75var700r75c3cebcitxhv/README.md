# Generate and Correct Captions — Lesson 165

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 28.

This self-authored, fictional practice recording contains two clearly synthetic eSpeak voices and a short original musical chord. It contains no private meeting, personal voice, real participant identity, or borrowed media. “Amina” is a fictional name spoken in the first line. The samples are a useful exercise, not a transcript of an outside event.

Start with [worksheet.md](worksheet.md). Play `original-recording.wav` or `practice-video.mp4`. Keep the original unchanged and work on a copy. Open `caption-practice.html` in a modern browser. The WAV is loaded directly from the same extracted folder; no file chooser is shown. The complete caption-practice workbench is a working Academy practice application, not an imitation of a commercial editor. It imports a deliberately flawed supplied draft; **it does not perform speech recognition or claim that its imported errors came from an ASR model**. Your real editor's caption generation can be used instead. Feature availability and labels depend on that editor and account.

- `draft-captions.vtt`: deliberately flawed starting point.
- `corrected-captions.vtt`: one reviewed model answer, not a universal reading-speed standard.
- `original-transcript.txt`, `recording-and-cues.json`: exact authored source and actual sample event positions.
- `correction-log.csv`: learner copy to record changes; `answer-key.md` lists intended repairs.
- `generation-source.md`: origin and reproduction notes for the supplied fictional media. Learners do not need to run synthesis tools to practice caption correction.

## Permission and disclosure
All teaching text, data, application source and recordings in this lesson kit are original Academy exercise material released under CC0-1.0. The voices are generic synthesized eSpeak voices, not Emmanuel Corels or any other person's cloned voice. No endorsement by eSpeak, an editor vendor or an accessibility standard is claimed. Original speech is slow and intentionally simple for caption practice; do not use its synthetic sound as evidence about a real person.

The final video contains the caption examples being taught. They are exercise content, separate from the course video's compositor subtitles. The exact library training correction uses 00:00:20.000–00:00:23.000 and “The library opens at nine.” Speaker attribution is also shown in the model answer.

## Actual transcription example

`actual-asr-transcript.txt` contains a real Qwen3-ASR-1.7B result from the exact supplied WAV, with unchanged-source/hash and model provenance in `actual-asr-provenance.json`. It heard the first name as “I'm in.” rather than the intended fictional “Amina.” This is why comparison with the source matters. That result has no word timestamps or speaker diarization; do not pretend the authored exercise cue times/labels were model observations. The supplied flawed VTT deliberately adds additional training defects and is separately labeled. Running this source transcription did not check or gate any course narration.

## Complete learner application and retained illustration source

Use **caption-practice.html** to complete all worksheet steps. It supports actual adding and splitting cues, direct editing, replay and WebVTT export. To verify your exported result, choose the downloaded WebVTT using **Import exported WebVTT**. The two real native video players consume that file as a caption track; one is a narrower viewport, not a claim about a physical phone or a particular mobile OS. Watch normal playback and listen to the actual original audio. Extract the entire kit so relative media links work. If your browser blocks a local file's automatic fetch, use the file picker for the supplied corrected VTT instead.

`caption-workbench.html` is the preserved earlier minimal illustration source used in the course's verified native visual captures. It only edits existing cues and loads an answer; it cannot insert/split a cue or validate an exported caption file. Do not use that limited illustration source as the complete exercise tool. It is retained unchanged for source provenance, not advertised as a full editor.
