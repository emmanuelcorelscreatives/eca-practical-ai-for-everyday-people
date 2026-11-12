# Practice worksheet

## 1. Establish the task
Read the garden notes in `practice-data.json`. Try the vague request in `prompts.md` once, or predict the different forms it could produce. Record which details the instruction leaves open: heading, sentence count, action label and missing-information handling.

## 2. Use one matching example
Copy the complete one-example prompt. Keep TASK, REQUIREMENTS, EXAMPLE INPUT, EXAMPLE ANSWER and NEW INPUT unmistakably separated. The book-swap example teaches the pattern; only the garden notes supply current details. Save your own draft under `my-garden-draft.txt`.

Check that the draft contains a friendly heading, exactly two short body sentences and one final `Action:` line. It must preserve Saturday, 18 October, 09:00, optional gloves (`if available`) and the east gate. It must not import the book-swap date, library entrance, book requirement or 16:00. Do not add a registration link, organizer, price or promise.

## 3. Add a contrasting missing-time example
Use the second example in `prompts.md` and then the clean-up input. The new notes omit a start time. Your draft must explicitly say `Start time: Not provided.` rather than import 09:00 or invent a time. Keep the two-sentence body and final Action line. The clean-up place, date and item must come from its own notes. These details are a self-authored additional practice case, not extra facts about the garden event.

## 4. Classify with exact labels
Use the classification prompt. Definitions: Information reports a fact or update; Request asks someone to do something; Confirmation states attendance or acceptance. Return only the single allowed label for each new message. First classify `I can attend on Saturday.` Then classify the three additional messages in `practice-data.json` separately. If classification affects safety, money, a deadline or a person, read the original message and apply the actual rules yourself; matching a pattern is not evidence.

## 5. Repair a mismatch
Take a draft with no heading or Action line and use the precise correction in `prompts.md`. Identify the mismatch before adding examples. Record whether the correction fixed it and whether it introduced sample details.

## 6. Manual fallback
Copy the four-line template from `prompts.md` into any normal editor. Fill it from the garden notes without an assistant. Check it against the same criteria. Save only permission-cleared examples. A useful pattern can work without continued prompting.

## Review checklist
- Same task as the example?
- Correct heading, two body sentences, Action line and section order?
- Exact labels and consistent separators?
- Only current input details, with no imported example facts?
- Missing details marked rather than guessed?

Write one sentence explaining why a polished format does not establish factual correctness. Compare your work with the author-written exemplars. Optional Python check: run `python3 check_answers.py --demo`; to check your own JSON, copy the `structured_response` schema in the data file and run `python3 check_answers.py my-response.json`. This is a local optional exercise, not a prerequisite for using the kit.
