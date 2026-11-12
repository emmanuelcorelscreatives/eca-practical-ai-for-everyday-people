# Fictional workshop workflow — decision specification
This is a platform-neutral exercise specification, not a screenshot or claim of an executed commercial service.

1. Read one unchanged request. Required fields are Request ID, Contact, Activity, Date, Attendance Estimate, Accessibility Notes (explicit None is valid), and Permission Confirmed.
2. Missing contact: create only an exception record “Clarification required”; do not draft an accepted task card, invent contact details, or mark successful completion.
3. Search existing-id-log.csv by exact ID before creating a new card. WR-104 is already present. Compare the record, then record “Duplicate confirmed” only after the human checks the match. No second card or accepted duplicate log entry.
4. Ambiguous note: quote “Quiet space may be needed; safety arrangement unclear” verbatim. Status “Manual assessment required”; block approval and all downstream actions. A person must obtain context; this exercise supplies no safety arrangement.
5. Complete ordinary record: draft the card with matching fields and record an internal proposed log row; pause at Human Review. Compare dates, attendance, notes, identity and permission to original. Only then approve the internal record.
6. Mapping study fault: Accessibility Notes → General Notes is wrong even when the wording is unchanged. Fix destination to Accessibility Notes and rerun the affected test, retaining source bytes.
7. No external message, publication, payment, booking or real participant action is permitted or claimed by this lab. A human-reviewed internal draft is its maximum outcome.
