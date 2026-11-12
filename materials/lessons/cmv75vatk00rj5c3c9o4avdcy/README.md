# Lesson 167 — Inspect the Exported Media
Emmanuel Corels Academy · Practical AI for Everyday People · Stage 28

All examples are self-authored fictional practice material. No real person, event or private account appears. Casey Lee and 27 are training literals. The voice is synthetic libflite, not the course instructor. This is a media-inspection exercise, not a universal loudness specification.

## Run the exercise
1. Keep every file together. Run `python3 -m http.server 8767` in this directory and open `http://localhost:8767/inspector-final.html`. No upload, account or external request is needed. Or play each MP4 in your normal media player.
2. Open `practice-faulty.mp4`, preserving it unchanged. Write your intended destination, display shape, message and test device in `inspection-target.md`. Unknown details stay “missing”. The browser's narrow viewport is only representative; it does not replace a real phone check.
3. Set a normal listening level and listen to the opening. The audio says **fifteen**, while the deliberately faulty opening caption says **fifty** and starts late. Compare against `approved-script.txt`. Check names, number 27, timing, completeness and important sound identification. The SRT timings are editable drafts: confirm against the actual recording rather than assuming they are perfect.
4. Inspect opening, middle, transitions and ending; try wide and narrow playback. Record observed cropping, visibility and playback behavior, not imagined defects. `SOURCE AND EXPORT` is intentionally wide so a narrow **crop** demonstrates lost text; the **fit** setting preserves the full frame. These controls simulate display shape and do not claim device certification.
5. Enter findings in `review-table.csv`: check, result, evidence, action. Include the time, actual words, player/device and display shape. Use passed, corrected, unresolved or not tested; never treat an export status as a pass.
6. Use the local editor's caption field and Download caption source to save caption-learner.srt. Place it beside the builder and run `python3 build_samples.py --caption caption-learner.srt --output my-corrected.mp4`. This consumes your saved caption source and refuses to overwrite existing exports. Then compare your new file and `practice-correct.mp4` with the faulty file. These two exports differ in the opening caption and its timing. They remain deliberately small training clips, not a claim that all timing/volume/device checks passed.
7. Play the complete corrected export and repeat relevant checks. Keep the original, corrected export, approved script and review record together. Test on the actual destination device before release. If it remains unavailable, record **not tested** rather than asserting success.

## Expected observations and limits
- Faulty file opening: spoken “fifteen”; visible “fifty”; caption delay 0.6 seconds. This is an intentional failure, not a transcription recommendation.
- Correct file opening uses “fifteen” and starts at 0.0 seconds. The rest of the script and audio are identical; check all timing by listening.
- The name-and-number table must compare CASEY LEE to CASEY LEE, and 27 to 27. The table explicitly labels a normalized comparison: the actual sample caption spells “twenty seven”. It is a separate instructional comparison, not an extracted real personal record.
- Cropping may hide wide text; fitting may introduce empty margins. Record the actual selected mode and observed result.
- No universal dB target, fabricated device test, automatic transcript approval or upload/publication occurs.

## Files and rebuilding
`build_samples.py` consumes existing approved-script.txt and SRT sources without overwriting them. The reproducibility command `python3 build_samples.py --fixture-build --replace-fixtures` intentionally rebuilds the supplied fixture exports; learners should instead use a new --output name to retain originals. The builder also writes equivalent WebM playback copies, ASS rendering source and SHA-bound construction receipts. `inspector-final.html` is the supported functional local browser app, not a screenshot pretending to be third-party software. Its native video controls play an equivalent WebM copy for browsers without H.264 support; the original MP4s remain the inspection targets. The “editable source” tab previews a manual caption correction on the sample; re-export is supplied by the reproducible builder, not falsely claimed as a browser export feature. `verify_samples.py` checks actual media streams, duration and unchanged audio between exports.

Permission: these Academy-authored practice files may be copied, adapted and shared under CC BY 4.0 with attribution to Emmanuel Corels Academy. FFmpeg, browser, operating-system and font software retain their own licences. Synthetic voice output is included solely as a fictional training recording.

The app starts playback reviews at zero. Scripted screenshot spot checks seek explicitly and retain proof; they do not alter the learner defaults. Browser review-table edits persist locally across navigation and can be downloaded as CSV; do not enter private data.

Fixture source generation: `python3 prepare_aligned_fixture.py` explicitly rebuilds synthetic sentence recordings and source captions from approved-script.txt. Caption boundaries derive from native recording frame counts with 0.4-second reading pauses, and the final instruction remains visible through the ending. Run this only when reproducing the training fixture; ordinary caption edits use build_samples.py and preserve those approved inputs.

`inspector.html` is retained byte-for-byte as the original source for earlier reviewed course screenshots. Its six ordinary navigation routes are functional; the internal, undocumented `?state=complete` capture route is unavailable in that archived edition. Use inspector-final.html, which repairs that route, for the exercise. This archival source is not a third-party application imitation.

For automated execution with read-only sources, use `--output-dir WRITABLE_DIRECTORY` on the fixture preparer or exporter and `--report WRITABLE_FILE` on verify_samples.py. Inputs remain in this source directory; ordinary learner exports retain existing files.
