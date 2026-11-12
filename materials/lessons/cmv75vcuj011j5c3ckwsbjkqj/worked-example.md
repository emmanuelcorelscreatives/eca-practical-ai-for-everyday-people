# Authored teaching example — not observed AI output

These self-authored fictional draft pairs reproduce the lesson's comparison pattern. They are not provider responses, measurements or a prediction that v4 always fails. Generate and save your own outputs in separate files during practice.

## C01
Working v3: Join the Riverside Reading Circle on Saturday, 24 October 2026, 14:00–15:30, in the Cedar Room. Attendance is free. Booking is required.

Candidate v4: Riverside Reading Circle — Saturday, 24 October 2026, 14:00–15:30, Cedar Room. Free; booking required.

Expected check: both preserve all six source fields and required action. Candidate is shorter; this alone never approves the entire change.

## C02
Working v3: Neighbourhood Story Hour — Sunday, 25 October 2026, 11:00. Location: Hall A or the courtyard, depending on weather. Final location requires confirmation.

Candidate v4: Neighbourhood Story Hour — Sunday, 25 October 2026, 11:00. Join us in the courtyard.

Expected check: candidate fails by selecting an unsupported location. Reopen the fixed notes, restore both options and the unresolved decision, then recheck.

## C03
Working v3: Repair Café — Tuesday, 27 October 2026, East Workshop. Bring one small item. Start time: not supplied; confirmation needed.

Candidate v4: Repair Café — Tuesday, 27 October 2026, East Workshop. Bring one small item.

Expected check: candidate fails by dropping the missing-time warning, even though its remaining statements match supplied facts.

## C04
Working v3: Community Seed Swap. Date conflict: Saturday, 7 November 2026, versus Sunday, 8 November 2026; confirm before publishing.

Candidate v4: Community Seed Swap — Sunday, 8 November 2026.

Expected check: candidate has a critical unsupported date selection. Both dates must remain visible; stop publication pending clarification.

## Illustrative comparison conclusion
C01: working PASS, candidate PASS. C02 and C03: working PASS, candidate FAIL. C04: working PASS, candidate FAIL — critical date conflict. Keep working v3 available and do not replace it with this example v4. This describes only these authored examples. No timing or aggregate score is invented.
