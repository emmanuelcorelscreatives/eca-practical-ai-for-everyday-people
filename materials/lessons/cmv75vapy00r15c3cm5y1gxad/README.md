# Lesson 164 — Edit Audio with Transcript-Based Tools

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 28

Learn to remove irrelevant speech without changing a speaker’s meaning. This kit supplies a **fictional synthetic practice recording**, exact transcript, functional local browser editor, preserved original and sample edited copy. It is supplemental practice, not a recording of Emmanuel Corels or evidence of a third-party transcription service. Nothing is uploaded. The Academy-authored tool is a real bounded practice editor, not a screenshot imitation of a commercial editor.

## Start

Extract the whole kit. Open `editor.html` in a current desktop browser; the bundled demo loads without an account or server. Local playback may require pressing Play because browsers restrict autoplay. Use headphones at a comfortable level. Keep the untouched kit as your original; duplicate it before experimenting.

1. Choose **Load practice copy** to see the practice WAV and preserved original.
2. Read the five transcript lines, then play the recording. It says “ten,” “reusable container,” “beside the library,” and the weather condition. These details must remain.
3. Choose **Select filler phrase** (or click the third transcript line). Only “Um, I was just thinking aloud.” and its trailing pause are selected in the waveform.
4. Choose **Remove selection**. The two retained sections join and the filler disappears. **Undo** restores the actual prior samples and transcript.
5. Play the result, including the sentence before the cut, the new join and the following sentence. Listen at normal speed for clipped words, awkward tone, repeated syllables and unclear references. Undo if unsafe; a sample-perfect cut alone does not prove a good listening result.
6. Choose **Compare original / edited**. Independently play both and check purpose, meaning, names, number ten, location, the weather condition and intent. The checklist is intentionally unchecked: a tool cannot confirm these human judgments for you.
7. **Check transcript** presents a deliberately seeded “nine” error while retaining the original audio. Replay, then apply the verified word ten. This is a manual practice error, **not a genuine ASR observation** or claim that a service misheard the audio. Never correct an unclear recording by guessing.
8. Choose **Export copy**, download `community_update_edited_review.wav`, and play the downloaded file itself. Keep the original, project files and review note. Browser autoplay and download settings vary.

## Own-recording/manual fallback

Record yourself reading `transcript-original.txt`, with consent for any other participant. Keep the master untouched. Convert a working copy to **mono PCM WAV, 24,000 Hz**, then choose the local file input. This bounded exercise editor supports only that format/rate and manual ranges for own recordings; it does **not** perform ASR or align a new recording to the supplied transcript. Do not reuse the demo’s timestamps for your own speech. Select your own start/end in seconds, preview, remove, undo and export. Alternatively use an installed waveform editor or a transcript editor available to you, without assuming paid/account-specific features exist. Protect permissions and do not upload private recordings without authorization.

For the bundled demo, the optional manual range is 4.405–7.085 seconds; use `alignment.json` for exact sample boundaries. Your own recording will have different timing. Preserve the weather condition. Do not treat every filler as irrelevant in other contexts; tone and context can matter.

## Files and results

- `audio/community_update_practice.wav`: 312,120 frames / 13.005 seconds, untouched synthetic source.
- `audio/community_update_edited_review.wav`: 247,800 frames / 10.325 seconds, illustrative removal of the one filler range only.
- `alignment.json`: exact frame ranges, sample rate and truthful synthetic provenance.
- `transcript-original.txt`, `transcript-edited.txt`: complete original and expected retained words.
- `worksheet.md`, `answers.md`, `review-note-template.md`: practice, separate expected checks and blank judgment record.
- `editor.html`, `demo-data.js`: full working offline tool and bundled exact demo audio.
- `execution-proof.json`: actual local PCM preparation measurements. These are physical measurements, not speech recognition or proof of human comprehension.
- `verify-kit.py`: standard-library exact sample/word/range checker.
- `LICENSE.md`: Academy-authored material and demonstration provenance.

The browser editor is deliberately small: no cloud, ASR, saving project edits to disk, loudness normalization, multiple channels or arbitrary codec support. Reopening resets its in-memory state. Keep your exported file and review note yourself. The original synthetic source remains unchanged. The sample edited file is an answer for comparison, not evidence that you listened to your own export.

## Review screens

Open `editor.html?state=manual` for the supplied manual fallback demonstration: the real original waveform highlights the removed interval, the edited waveform marks the sample-derived join, and playback starts at that join. The preserved original stays separately playable. Open `editor.html?state=checklist` for the blank six-item final review checklist. These query views perform the same local selection/removal operations on the bundled demo; they do not assert you have completed the checks. Refreshing restores the original in-memory practice state.
