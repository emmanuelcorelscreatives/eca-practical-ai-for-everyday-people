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

For each case record: actual run ID/time; proposal version; validation and missing fields; decision; gate state; action state; exact-ID search count; total destination count; evidence file references; observed discrepancies. State whether evidence is manual, the local Python model, or an actual named-platform execution. Never merge those provenance categories into a claim of vendor proof.
