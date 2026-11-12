# Source mapping and proposal instruction

All values are fictional study data; these are setup notes, not a vendor configuration export.

| Incoming field | Fixed check | Failure behavior |
|---|---|---|
| Request ID | Exists, nonblank | Stop; Needs information |
| Contact name | Required on source form; nonblank on incoming record | Stop; Needs information |
| Contact email | Exists; basic suitable pattern | Stop; Needs information |
| Requested date | Exists; date input appropriate | Stop; Needs information; do not infer a date |
| Request details | Exists, nonblank | Stop; Needs information |
| Permission to contact | Exactly Yes | Stop; no proposal or approval queue |

Map fields by meaning, never by nearby position. Required form controls do not replace downstream validation; imports, changed forms and failed mappings can bypass form controls. Presence and a basic email pattern do not prove correctness, consent, deliverability or identity. No rule delegates the decision about a missing field to AI.

## Proposal step instruction from this lesson
Use only supplied fields. Label missing information. Do not claim booking, accessibility, price or availability. Produce a draft confirmation note; output remains internal. Keep Generated proposal distinct from Source record. The supplied CSV proposals are prewritten fixtures for a reproducible comparison, not generated service output.

## Review package
1. Original input, identified by request ID.
2. Exact proposed output.
3. Intended next action: Update internal task.
4. Destination: Workshop planning task list.
5. Assumptions and missing information, explicit even when None stated.

Approval authorizes only this exact package and action. Any material edit requires repeat validation and fresh review. No send/publish/purchase/delete/booking step belongs to this exercise.
