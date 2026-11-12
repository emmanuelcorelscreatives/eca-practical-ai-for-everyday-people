# Learner delivery worksheet
1. Draw Request → Required fields → Exact Request ID check → Draft → Human review → Save reviewed document → Log. Rejection stops before save; correction returns to draft review; invalid input stops before draft.
2. Identify each required field and compare EVT-042 with its source. What fact is missing? Never invent registration details.
3. Run the normal case and retain input, complete draft, exact approved version and log entry. Approval covers that version only.
4. Run EVT-043. Identify the unsupported price claim and reject. Prove no saved document or downstream action exists.
5. Run EVT-044. Name both missing checks and prove draft/review were not run.
6. Resubmit EVT-042 after approval. Prove exact-match detection preserves the original record and creates no second document.
7. Run EVT-045, approve the checked draft, observe Save reviewed document failure. Check existing output, approved version, permission/destination, and duplicate risk. Use manual fallback; record a responsible name. Do not regenerate after approval.
8. Export evidence. Include field mapping, drafting instruction, review checklist, run log, five case outcomes and manual recovery evidence. External actions must equal zero.

Manual fallback: open source; compare Request IDs; copy only the approved version; save with the same ID; record Manual completion and responsible person. Rejected/invalid records cannot use this fallback. A correction requires renewed review. Do not blindly rerun after an unknown connection outcome.

Reflection for Lesson 216: record time, corrections, maintenance burden and which decisions must remain human. This lesson does not claim an external message was delivered.

Additional edge checks: For an uncommitted correction, Approve is disabled. Commit a revised body, then verify all four checks reset before approval. After an EVT-045 failed save, resubmit EVT-045: the new attempt stops as duplicate, while manual fallback still resolves the earlier approved attempt and displays its source and exact approved content together. Complete manually once; a second attempt must refuse duplicate output. For another editable ID (for example EVT-047), leave source notes empty and permission unchecked: the displayed invalid record must be that actual ID, not EVT-044. Correct and resubmit under the same ID; the earlier invalid attempt is retained and the valid attempt reaches review. These extra IDs are learner-created fictional edge cases, not new narrated examples.

Further evidence attribution: reject a valid learner-created ID (e.g. EVT-047 after corrected submission) and verify the rejection heading and action/output count belong to that actual attempt. After the duplicate EVT-045 attempt, inspect Connection failure and Run history: both must identify the preserved original failure attempt, not the later duplicate. Match attempt number as well as Request ID.
