# Add an AI Transformation Step — Lesson 196

All workshop records in this kit are self-authored fictional Academy practice data. No booking, message or external action exists. `simulated-draft.json` is a deliberately authored simulation, not a captured AI response. You need no subscription or connection to complete the manual route.

## Input, instruction, draft and checks
1. Open `sample-input.json` and retain an unchanged original. Create a working copy of `blank-reuse-template.md` in any available document editor. If using LibreOffice Writer, name the document **Lesson 196 Manual Simulation**. The files use UTF-8 text; opening them needs no macros or code.
2. Copy Request ID, Category, Title, Date, Time, Location and Notes into INPUT. Ordinary rules require Request ID, Category, Title, Date, Time and Location to be nonempty. Allowed categories for this exercise are Workshop and Meeting. The category must match exactly; Workshop selects the workshop route. Empty fields or an unrecognized category stop before AI. Accessibility is not a required routing field, but its missing information must stay visible.
3. Map each source label to its matching instruction value. Deliberately putting the title in Date is a mapping mistake, even if a model obeys the instruction. Leave unrelated metadata and private details unmapped. Use only minimal permissions: this exercise never needs send, delete or publish rights.
4. Open `bounded-instruction.txt`. It has one narrow job, protected facts, boundaries and six output labels. It neither decides routing nor grants external-action permission. Copy the checked fictional input into its INPUT section. For a wholly offline simulation, inspect `simulated-draft.json`. Optionally submit the instruction to an available AI tool or supported AI action; verify your account's fields and permissions. Save any actual response separately and label it as that tool's response. Do not claim the supplied simulation came from a tool.
5. Review all six labels: Request ID, Event details, Draft summary, Assumptions, Missing information, Review status. Compare ID/title/date/time/location character for character to the original. Trace every summary claim to the source. Generated wording is a draft, not evidence. “Accessibility details: Not supplied.” must not become a promise about access.
6. Keep the status **Draft only — human review required.** This means a draft awaits review; it is neither approval nor publication. If a required output label is missing, mark incomplete and stop. Correct failed drafts or return to the input before continuing. Do not ask a second model to certify the first; compare actual source evidence.

## Source-matching expected example
CR-104 / Workshop / Bicycle Care Basics / Tuesday 20 October 2026 / 18:00 / East Room. Notes: “Bring a bicycle only if convenient. Tools are provided. Accessibility details not supplied.” The authored simulation preserves these values, uses a summary under 70 words, declares no assumptions and keeps the missing accessibility detail. The category stays an ordinary routing decision outside AI. No price, contact, attendance limit or universal bicycle suitability is supplied.

## Practice and manual answer checks
A. Change the working input Time to an empty string. Expected: stop before transformation; request the missing time. Never guess it.
B. Change Category to “workshop”. Expected: stop, since this exercise uses exact allowed labels. Correct against source; do not ask AI to interpret a fixed category.
C. Change the draft Date to Wednesday 21 October 2026. Expected: reject the changed protected fact.
D. Add “Suitable for all bicycles.” Expected: remove the unsupported claim; fluent style cannot repair unsupported meaning.
E. Delete Missing information. Expected: incomplete structure; stop. Restore the explicit source gap rather than inventing access details.
F. Add “Accessibility is guaranteed.” Expected: reject. The input does not establish that.
G. Clear old values from the reusable template. Expected: placeholders remain blank so yesterday's date/title/location cannot leak into another record.

## Optional offline checks
With Python 3 available, run `python3 check_examples.py` from this directory. It uses only the standard library, reads local fictional JSON and makes no network calls. Expected: one valid simulation accepted, and all six deliberately corrupted cases rejected. `local-check-receipt.json` records our actual local execution. The narrow validator checks these known examples and exact structural rules; it is not a general factual-verification model. You must still compare each generated claim manually. No Python installation is required for the main exercise: use the preceding manual answers.

## Reuse boundary
Keep ordinary required-field checks, exact category routing, fixed labels and permissions outside AI. Use AI only for organizing variable notes and draft wording. Connected and copy-paste routes use the same input, instruction, structure and review boundary. Lesson 197 tests further sample records before any real trigger; this lesson enables none.
