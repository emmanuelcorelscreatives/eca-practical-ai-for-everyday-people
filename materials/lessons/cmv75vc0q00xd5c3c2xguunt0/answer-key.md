# Expected checks
All seventeen fixture results are listed in expected-results.csv; Run all fixtures calculates them from the actual current and approved objects.

Only unchanged and v2-approved match; both reach only simulated action, with real action always disabled. Date, destination, message, same-name attachment revision, linked-record revision, and version changes stop as changed. Missing attachment and blank date stop as unknown, not match. Reject stops; edit requires a new version and fresh review. Different contents under an identical filename still need review. A failed lookup cannot establish equality. Recipient/destination change needs a new approval, even if the words match. Snapshot hashes support equality, not factual accuracy or permission. Protect immutable snapshots and bind final action to the exact version checked.

Approval in this teaching data concerns the displayed package only. The brief does not substantiate an opening time or tools guarantee, so neither can be made true by an approval click. Record why a package was rejected; a draft edit never inherits old approval.

Five malformed fixtures (empty attachment, empty linked record, whitespace date, string version, missing attachment revision) must stop as unknown. A rejected unchanged package stays rejected until a deliberately fresh review request is created and approved. Run all fixtures must leave the selected package and decision unchanged.
