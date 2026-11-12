# Practice worksheet

## Prepare the source

Read input-response.json. Identify five submitted fields: name, email, workshop topic, question and optional preferred month. The form title is context, not a response field. The month is an empty string; no date or answer has been supplied. Do not replace it with a guessed value.

## Route A — connected practice, if suitable

Create a new self-owned Community Workshop Enquiry form with those fields, and submit only the provided fictional record. Inspect the recorded response before choosing a trigger sample. In a new workflow select the submitted/new response event for this exact form. Read each connection's actual permission request; cancel if unsuitable. Record decisions in permission-record.csv without account identifiers or credentials.

Add exactly one document creation action. Name the document REVIEW — Workshop enquiry — followed by the mapped name, and use a new Workshop Drafts — Review folder. Map each input to its matching labelled template location. The greeting, labels and DRAFT — NOT SENT text are fixed wording. Leave the month blank with a visible label if your platform cannot supply the missing-value note; never infer a month. Do not choose a send, reply, calendar or publish action.

Read the preview, test the document action once, then open the actual created document. Inspect sharing and check for any separate automation watching the folder. A green success icon proves neither correct wording nor appropriate access. Keep screenshots only of your new practice material; exclude private data. Do not include tokens, account addresses or permission secrets in public evidence. Do not activate unattended running for this exercise.

## Route B — manual simulation

Create a new Workshop Drafts — Review folder. Copy draft-template.md into a new document titled REVIEW — Workshop enquiry — Maya Chen. Replace the three corresponding placeholders with the exact name, topic and question. Replace the missing month placeholder with Not supplied — reviewer must confirm. Keep Reviewer notes empty. Save and reopen it. Compare the source and final document field by field.

Optionally reproduce the same manual template mapping with:

    python3 make_draft.py input-response.json "Workshop Drafts — Review/REVIEW — Workshop enquiry — Maya Chen.md"

Run from this kit directory with Python 3. The output path must not exist; the script refuses to overwrite an earlier document. This safeguard belongs to this optional reference utility, not a claim that the connected workflow contains duplicate protection.

## Inspect and hand off

Complete review-checklist.md and evidence-record.csv. Mark the accessibility question UNRESOLVED: no opened venue evidence exists. Keep the record in the review location. No message is addressed or sent. For the manual route record connector permissions as NOT CONNECTED, rather than inventing a permission screen or run history.

Challenge: change only the input name and question to another fictional test record and predict which draft fields change. Preserve the missing-value handling. Do not invent dates or answers, and do not reuse a real person's enquiry. Explain why creating a document is an external record-writing action even when no message is sent.
