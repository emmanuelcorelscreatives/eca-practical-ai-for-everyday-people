# Answer key and reasoning

Read after attempting the worksheet. These are model answers written by the kit author, not machine-generated execution results.

## Main workshop case

Requested job: prepare existing attendees to pack and arrive using a short, source-only checkbox checklist and flag unknowns.

Card A's actual job: promote attendance through inviting event description. It includes the 10:00 start and provided materials, but correct fragments do not satisfy the requested job.

| Anchor | Expected finding |
| --- | --- |
| Goal | It persuades people to attend instead of helping attendees prepare and arrive. |
| Audience | It addresses a prospective participant rather than someone needing practical arrival and packing instructions. |
| Constraints | It omits 09:40, notebook, reusable water bottle and the east-door step-free instruction, and adds unsupported promotional claims. |
| Format | It is a paragraph, with no checkboxes or clear actions. |

The attendee cannot fully pack and arrive from Card A. Card B supplies all six facts, the requested checkboxes and unknown-information flags. Inspect `traceability.csv`: W1 and W2 support the first checklist action, W3–W6 support the remaining actions. “From 09:40” preserves the source's doors-opening meaning; “must arrive exactly at 09:40” would overstate it. Curiosity is not a substitute for the notebook or reusable bottle.

A strong correction names the required attendee checklist, supported items, checkboxes and no unsupported details. A vague “make it better” gives less direction. The manual fallback can produce the same checklist directly from W1–W6 without using an assistant.

## Extra case P1 — ingredient question

Requested job: identify the dishes containing sesame for someone deciding what to order, using only the fixture menu. The response lists popular dishes, a different job. Correct answer: “Sesame slaw is the dish listed as containing sesame in the supplied menu.” Do not claim a dish is allergen-safe: the fixture says nothing about cross-contact or complete ingredient disclosure.

Correction request: “List the dishes marked as containing sesame in the supplied menu, rather than popular dishes. Do not infer allergy safety or add menu information.”

Anchor findings: wrong selection goal; prospective diner needs ingredient information; source restriction bars invented ingredients and popularity; requested one-sentence form is already satisfied, so format alone does not diagnose the error.

## Extra case P2 — summary request

Requested job: give a two-bullet summary of the library notice for existing borrowers using only the notice. A study schedule does a different job, even if useful for learning.

A valid manual answer:

- The library closes at 16:00 on Friday for maintenance.
- Items due Friday may be returned on Saturday without a late fee.

Correction request: “Summarise the supplied library notice in two bullets for borrowers. Include the closure time and return arrangement, without proposing a study schedule.”

Anchor findings: summary goal replaced by planning; borrowers replaced by students; required notice details omitted; requested two bullets replaced by a numbered schedule. Do not invent reopening time, which is absent from the notice.

## Checking your own work

Accept equivalent plain language if it preserves the facts, source restrictions and requested form. Reject fluent answers that do another job, omit required actions, add unsupported claims or cannot support the intended next action. This answer key supports human checking; it does not claim an automated task-fit score.
