# Actual source-audio ASR observations

These are actual unconditioned Qwen3-ASR-1.7B CPU results for the supplied synthetic recording. They are not the seeded error fixture, a human listening claim, a pronunciation score, or an accuracy guarantee. The model received audio only, without the script, expected words, hotwords or forced alignment. Original audio remains unchanged.

Source: Community Garden Planning.wav ·32.86 seconds ·SHA256 a96550b8aeb64ea47cff5d06ad0a30b8ff4d17bdf8c5386b959b717e6dc89888.

Elapsed ranges below come from exact native assembly frame offsets. They are not word-level recognition timestamps.

## whole-recording ·0.000–32.860s

Hello, I am Amara and WOSU. We are planning the community garden. I'm Diego Ruiz. Thanks, Amara. I can help check the planting plan. We have room for 40 raised beds. The planning visit is on the 16th of October, 2026. The estimate is 1,500. Please place the tool storage near the eastern gate. That is all for this recording.

## passage-01 ·0.000–5.210s

Hello, I am Ammar and Wosu. We are planning the community garden.

## passage-02 ·5.710–11.175s

I am Diego Ruiz. Thanks, Amara. I can help check the planting plan.

## passage-03 ·11.675–14.285s

We have room for forty raised beds.

## passage-04 ·14.785–19.550s

The planning visit is on the 16th of October 2026.

## passage-05 ·20.050–22.615s

The estimate is one thousand five hundred.

## passage-06 ·23.115–26.265s

Please place the tool storage near the eastern gate.

## passage-07 ·26.765–29.765s

[No text returned by ASR for this masked overlap.]

## passage-08 ·30.265–32.360s

That is all for this recording.

## What to inspect

The recognizer transcribes the clear quantity/date/estimate/storage passages, but its first name/surname recognition varies between the whole clip and isolated introduction. The supplied fictional participant list provides the authorized spelling Amara Nwosu; ASR alone does not establish identity or spelling. The whole-clip output omits the masked overlap, and the overlap-only request returns no text. Retain the uncertainty marker rather than treating silence or a plausible guess as recovered words. Compare your own playback observations with these machine results and keep disagreements visible.

Pinned model revision: 7278e1e70fe206f11671096ffdd38061171dd6e5.
