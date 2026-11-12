# Distinguish Observation from Interpretation

An offline practice kit for Stage 11, Lesson 64. All event, bus and library examples are self-authored fictional teaching material. The sample summaries are authored examples, not records of a live assistant response. No account, installation or paid tool is required. Nothing here verifies an actual venue or person.

Open `source-notes.txt`, `practice-claims.csv`, and a blank copy of `review-template.csv` in a text editor or spreadsheet. You can also copy the table onto paper. Keep `answers.md` closed until you finish.

## 1. Find the exact support

Read the three workshop sentences in `source-notes.txt`. For each claim W01–W11 in `practice-claims.csv`, write one of: **Directly stated**, **Interpretation**, or **Missing information**. Copy the exact supporting sentence for directly stated claims. For an interpretation, record which words add a judgment, cause, emotion, prediction or quality. For missing information, write a question you would need answered.

A missing item is a gap in the source. It does not establish that something bad happened. An interpretation can be plausible without being established. Labeling a claim does not prove it.

## 2. Repair an authored weak summary

> Interest was disappointing, organizers moved to a better room, and several attendees were worried the event would be inaccessible.

Underline “disappointing,” “better,” and “worried.” Then check the rest: Does “organizers” have support? Are “attendees” and “registrants” interchangeable? Is asking a question the same as complaining? Is an inaccessible event established?

Write a corrected summary containing all three established facts, preserving the numbers and groups. Add one sentence that makes the important gaps visible. Do not invent an organizer, reason, emotion or access status.

Expected check: three exact facts retained; no unsupported judgment; uncertainty remains visible. Compare your wording against `answers.md`, not against another assistant’s confidence.

## 3. Try a better instruction, optionally

Use `prompts.txt` with the fictional source in an assistant you already have permission to use. Otherwise write the response yourself. Keep your actual output separately; the kit does not promise any assistant’s behavior.

Check every quotation manually against `source-notes.txt`. Under Directly stated, the expected response includes three source statements with matching quotations. Under Interpretation, no proposed explanation is established by the source. Under Missing information, expect the registration target, room-change reason, room comparison, question wording and answers, and actual access features. A neatly formatted response can still be wrong.

## 4. Transfer the habit

Classify B01–B03 and L01–L04. For the bus, subtract 8:10 from 8:25; label the 15-minute difference as a checked calculation from stated times, rather than an exact source quotation. Do not infer the driver’s motive. For the library, separate a count change from a claim about its cause.

Expected check: the bus calculation is 15 minutes; the library change is 4 books. Neither establishes cause. See `answers.md` for the distinction between a supported calculation and a directly quoted observation.

## 5. Manual fallback and final check

Draw “Source says” and “Possible interpretation” columns. Copy exact source support into the first. Put possible explanations into the second with an uncertainty label. Add a short missing-information list below. Two assistants agreeing is not additional source evidence.

Before using a summary: find exact support, label added meaning, and show what is missing. Check numbers, group names, and verb strength. Do not turn “three registrants asked” into “attendees complained.”

Optional data-file check, if Python 3 is already available: run `python3 check_fixtures.py` from this kit directory. Expected result: `PASS: 18 fixture classifications; 2 arithmetic checks; exact source quotations`. This checks the supplied answer data; it does not grade your writing, validate any real-world claim, or provide browser proof.
