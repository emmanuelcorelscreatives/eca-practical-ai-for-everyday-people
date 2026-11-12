# Lesson 187 — Write the Trigger and Required Inputs
Emmanuel Corels Academy | Practical AI for Everyday People

All event details here are fictional teaching examples. No event, email address or external action is real. This kit is a starting-rule exercise, not a final-output design lesson.

## Start rule
Start when the event brief is marked READY FOR DRAFTING. A conversation or draft request alone is not the trigger. If readiness is unclear, ask the owner.

## Practice
1. Open complete-brief.json and check the trigger and each required field using checklist.md.
2. Compare incomplete-brief.json. Do not invent missing information; record a clarification request.
3. Use prompt-library.md with the complete brief only. AI is optional: write a draft manually if unavailable.
4. Mark source facts separately from any newly generated wording. Compare date, time, place, audience, description and response method with the source. Samira must review before any sharing; nothing in this exercise sends or publishes anything.
5. Choose your own successful everyday task and fill four-lines-template.md. Test one complete and one incomplete input with another learner. Revise unclear rules before adding tools or permissions.

## Manual fallback
Create two local folders or document sections: ready briefs and needs clarification. Check incoming briefs yourself. Put complete, marked-ready inputs in ready briefs; incomplete or contradictory inputs go to needs clarification with exact questions for their owner. Use a saved instruction/template only when ready.

## Check
Run `python3 check_inputs.py` offline (Python 3 standard library only), or compare manually with expected-checks.md. It validates required information and the readiness marker, not the truth of real-world facts. Do not include private data.
