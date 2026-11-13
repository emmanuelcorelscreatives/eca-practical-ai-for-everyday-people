# Approval boundary evidence record

Use actual observed timestamps and results. Blank means not yet checked; do not tick in advance. Training data only. Screenshots must exclude account menus, unrelated files, private tabs and credentials.

- [ ] Dedicated new test-only destination, zero baseline rows.
- [ ] Real external action types disabled, one gate-to-action path only.
- [ ] Four required fields checked; Supporting information retained as context.
- [ ] Exact unchanged reviewed version and explicit decision retained for each case.
- [ ] CONTROL-204-A: Complete / Approve; gate passed; action completed; exactly 1 matching destination row; Result = Boundary control passed.
- [ ] REJECT-204-B: Complete / Reject; gate stopped; action Not run; 0 matching destination rows.
- [ ] INCOMPLETE-204-C: Destination empty / Incomplete / Approve; gate stopped; action Not run; 0 matching destination rows.
- [ ] Total destination count = 1 with no duplicate control ID.
- [ ] Proposal content is labeled as proposed, not a completed action.
- [ ] Failures, run IDs and automatically captured timestamps retained without editing.
- [ ] Manual fallback processes only complete, approved, unchanged proposals.

For each case record: actual run ID/time; proposal version; validation and missing fields; decision; gate state; action state; exact-ID search count; total destination count; evidence file references; observed discrepancies. State whether evidence is manual, the local Python model, or an actual native-platform execution. Also record the actual operator identity/type and submission method, including HTTP versus browser DOM, and label historical baseline/copy/continuation evidence. Never merge those provenance categories into a claim of vendor proof.

Human approval is not established by AI-operator tests. Retain background outbound attempts and whether controls blocked them. Do not replace an unavailable process-exit detail with an invented value.

For the sole shown portable twelve-node experiment, retain all three actual headless form DOM submissions as Test fixture operator, the matching native histories, timestamp 2026-11-12T22:27:51.323Z and workbookSHA eb263912ce6fec4f62b20fe716c5e24528c083917981289ad0dd95f6e5947251. Never mix the separate historical eleven-node HTTP/continuation experiment into this evidence. Genuine native canvas/config/history and real spreadsheet GUI find/count controls still need actual capture.
