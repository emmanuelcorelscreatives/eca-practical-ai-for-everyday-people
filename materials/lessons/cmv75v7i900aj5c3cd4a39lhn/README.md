# Evaluate images, audio and translations

This kit supplies the actual practice files for all three media. Start with worksheet.md, keep the originals, and record findings in review-log.csv. Use answers.md after completing the checks.

The garden PNG is an AI-created fictional source, not a photograph of a real event. The audio is a supplied 48-second synthetic recording, not real participants. Flawed outputs were deliberately authored to illustrate possible errors; they are not retained failures from live AI runs. No account, model subscription, microphone or participant recording is required.

- Images: garden-original.png, garden-illustrative-flawed.png, garden-corrected.png.
- Audio: garden-planning-recording.wav; audio-script.txt gives intended source content and actual timing; transcript-flawed.txt and transcript-reference.txt support comparison.
- Translation: notice-es.txt, translation-flawed.txt, translation-reference.txt and glossary.csv.
- Optional schematic aids: the three garden SVGs and garden-map.txt. Use the PNGs for faces, hands, clothing, textures and shadows.
- Provenance: fixture-provenance.json and image-operation-proof.json describe actual authoring and its limits.

Open PNGs in a real image viewer/editor and WAV in a real audio player. Arrange originals and outputs side by side. If your editor lacks a comparison tool, use two windows. You may inspect the supplied corrected file without performing an edit, but do not claim you edited or listened until you actually do so.

Optional offline package check: run `python3 check_fixtures.py` in the extracted kit folder. It uses only the Python standard library, reads local files and writes nothing. It verifies hashes, decoded PNG pixel preservation, WAV structure and authored text consistency. It does not judge image truth, acoustic intelligibility, human identity, or translation quality.
