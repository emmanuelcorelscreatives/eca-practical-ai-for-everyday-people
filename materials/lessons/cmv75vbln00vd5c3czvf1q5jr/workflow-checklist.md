# Event workflow checklist
Purpose: turn approved community event facts into a draft information sheet. Does not book or publish.
Required fields: event_name, date, start_time, end_time, venue, audience, contact, approved_facts.
Normal path: open source → check all fields and source agreement → draft using verified facts → compare every field and phrase with source → mark Awaiting human review. Human approval is separate.

| Exception | Detection rule | Response | Owner | Record/recovery |
|---|---|---|---|---|
| Missing input | Any required field empty | List exact missing fields, ask clarification, no draft | Request owner | Keep case ID/source; re-enter full input check |
| Contradictory input | Required fact differs across sources | Show each value/source, label unresolved, no finished sheet | Event coordinator | Keep both sources; resume after authorized decision and input recheck |
| Outside scope | Requested output is not event information sheet | Explain boundary and redirect; retain request | Authorized reviewer | Referral route, no completed-action claim |
| Tool unavailable | Temporary failure with usable verified input | Check prior outcome; at most one later retry; manual fallback after failure | Workflow operator | Record attempt/outcome; fallback waits human review |
| Damaged input | Input cannot be opened/read reliably | Stop and request usable source; no blind retries | Request owner | Preserve failure/source; recheck replacement |

No unresolved case silently enters final output. Keep opened evidence, generated drafts and unresolved questions separate. Record assumptions only in harmless scratch drafts, visibly labeled; never as approved facts.
