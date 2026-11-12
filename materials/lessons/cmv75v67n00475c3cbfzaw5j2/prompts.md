# Copyable prompts and manual template

## Vague request for comparison
Turn these event notes into a short public announcement. Make it clear and friendly.

Community garden morning. Saturday, 18 October. Starts 09:00. Bring gloves if available. Meet at the east gate.

## One-example prompt
TASK: Turn event notes into a short public announcement.

REQUIREMENTS: Use a friendly heading, two short sentences, and one final action line beginning `Action:`. Use only supplied details. Mark missing information as `Not provided.` Keep the examples separate from the new input.

EXAMPLE INPUT:
Book-swap table. Tuesday, 14 October. Starts 16:00. Bring one labelled book. Library entrance.

EXAMPLE ANSWER:
Share a book with your neighbours.
The book-swap table opens on Tuesday, 14 October, at 16:00 by the library entrance.
Bring one labelled book to take part.
Action: Meet at the library entrance.

NEW INPUT:
Community garden morning. Saturday, 18 October. Starts 09:00. Bring gloves if available. Meet at the east gate.

## Contrasting example block
Insert this after the ordinary example and before NEW INPUT. It teaches a missing-time boundary, rather than another nearly identical full-information event.

EXAMPLE INPUT 2 (fictional practice):
Seed exchange. Thursday, 23 October. Meet at the community hall. Bring spare seeds. Start time is not supplied.

EXAMPLE ANSWER 2:
Share seeds with your neighbours.
The seed exchange is on Thursday, 23 October, at the community hall; Start time: Not provided.
Bring spare seeds.
Action: Meet at the community hall.

Replace NEW INPUT with this separate fictional practice case:
Neighbourhood clean-up. Sunday, 26 October. Meet at the north gate. Bring a reusable bag. Start time is not supplied.

## Classification prompt
TASK: Classify the new message using one label only: Information, Request, or Confirmation.
DEFINITIONS: Information reports a fact or update. Request asks someone to do something. Confirmation states attendance or acceptance.
EXAMPLES:
The room has changed to Hall B. → Information
Please bring two chairs. → Request
NEW MESSAGE:
I can attend on Saturday.
OUTPUT: Only the label.

## Precise correction
Use the exact structure shown in the example: one heading, two short sentences, then one `Action:` line. Rewrite using only the new input.

## Manual editor template
[Friendly heading]
[Sentence 1]
[Sentence 2]
Action: [Required action or 'Not provided']
