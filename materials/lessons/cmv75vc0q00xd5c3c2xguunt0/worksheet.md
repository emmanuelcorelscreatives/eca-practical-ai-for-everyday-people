# Recheck Changed Content Before Action
Practical AI for Everyday People · Lesson 202 · Emmanuel Corels Academy

Use fictional EVT-014. Nothing in this exercise sends or publishes. Open `simulator.html` locally in a current browser; it needs no sign-in, external library or server. Select a case, inspect the full approved snapshot and editable current package, then press Compare current package. The initial approval is a teaching fixture, not proof the fictional event is real. The visible evidence panel separates a proposed brief from generated draft assumptions.

## Practice
1. Select unchanged. Confirm package ID, version, action, destination, date, subject, message, attachment identity AND content revision, and linked record identity AND revision. Match reaches only a simulated action.
2. Select date-changed: 18 October becomes 19 October 2026. Expect fresh approval required, old decision stale and sending disabled. A timestamp alone cannot authorize this change.
3. Restore the approved date by choosing destination-changed. Words remain identical but the destination is Public social channel. Expect changed destination and no simulated action.
4. Select unsupported-promise. The tools guarantee is absent from the supporting brief. Comparison catches changed content; a human must also correct or verify the claim. Equality never validates facts or consent.
5. Choose attachment-changed. The filename stays the same but contentRevision changes. Expect stop. In production compare exact immutable bytes or a cryptographic digest, not this training revision label.
6. Choose linked-record-changed. The record ID remains BRIEF-014 but revision differs. Expect fresh review. Real integrations need a complete immutable representation of every action-relevant linked record.
7. Select missing-attachment and blank-date. Expect Cannot compare / manual review, never match, with no default continuation after timeout.
8. Choose rejected and edit-resubmit. Rejected stops with a reason; edit creates a fresh request, neither reaches action. Choose v2-approved to see the separately approved 19 October package pass.
9. In an unchanged case edit the JSON date or recipient, leaving version unchanged. Compare again: a version label is insufficient and the changed actual value still stops the workflow. Reload case to reset.
10. Press Run all fixtures. Read the actual 17 local outcomes and compare each to `expected-results.csv`.

## Manual fallback
Use `prepare-manual-queue.ps1 -Destination NEW_ABSOLUTE_DIRECTORY` in PowerShell, or manually create an Approval Queue with Awaiting Review, Approved Snapshot, Rejected and Needs Recheck. The script refuses any pre-existing destination and writes only new Academy files. Keep the reviewed v1 snapshot separate from the editable v2 package. Open both PDFs and review-status.txt under Needs Recheck/EVT-014-v2. Record the changed date, remove approved status and request fresh review. Do not execute a real action from this exercise.

## Check your understanding
Why is a same-name edited attachment different? Why does a timeout mean unknown rather than unchanged? What must happen if the destination changes between approval and action? Answers and observed fixture expectations are in `answer-key.md`.

The offline simulator uses a recursively complete exact comparison of this bounded JSON schema. It is a teaching implementation, not a secure approval service: browser memory is editable, it has no authenticated reviewer, and it cannot prevent another writer changing a live service after comparison. Production must protect snapshots and perform final comparison and action atomically or against a provider-supported immutable version; if that cannot be proved, stop for manual review. Keep consequential actions disabled until tested. The next lesson teaches limiting scope and an off switch; this kit stays on changed-content approval.

## Fresh review lifecycle
Select unchanged, enter a rejection reason and click Reject. Compare again: the package stays rejected and cannot reach action. Click Create fresh review request to begin a new version. Read its changed fields and complete snapshot in the simulated reviewer decision record. Approve that displayed revision, then Compare again. A later edit requires another fresh request. Edit and resubmit follows the same lifecycle. Blank nested attachment fields, missing linked-record properties, whitespace-only dates and nonnumeric versions all stop as unknown. Run all fixtures is a read-only results report; it does not change the selected package or its decision. Decisions record time, reason and exact reviewed values together; the record remains an editable local training record, not authenticated evidence.
