# Expected checks — authored fictional demonstration
These values reproduce the authored lesson's fictional demonstration; they are not fresh benchmark measurements or a promise of future savings.

| Measure | Manual | Automated | Difference |
|---|---:|---:|---:|
| Batch elapsed | 38:00 (2280 s) | 24:00 (1440 s) | 14:00 (840 s) saved |
| Active effort | 38:00 (2280 s) | 14:30 (870 s) | 23:30 (1410 s) saved |
| Corrections | 2 | 3 | Report type, not just count |

Normal A manual active/elapsed is 05:40 (340 s); automated elapsed 03:50 (230 s), active 01:35 (95 s), waiting 02:15 (135 s), corrections zero for automated. The duplicate's active effort is 03:50 (230 s) manual versus 01:20 (80 s) automated. The lesson does not give every individual case duration; blank entries must remain unreported until actually measured.

Initial setup is 52:00 (3120 s), distinct from 11:00 (660 s) maintenance for mapping repair and required retest. 1410 − 660 = 750 s = **12:30 net active effort saved after maintenance**, before recovering initial setup. If allocating both setup and this maintenance to this one batch, 1410 − 660 − 3120 = −2370 s = **39:30 additional effort**, not a positive saving. Frequency and future maintenance change the decision; no universal break-even prediction is supplied.

Automation has one mapping correction and two formatting corrections; manual has two corrections including Normal A's activity-title typo. Mapping-fixture.csv is a labelled broken example; correct only the destination, keep its wording and source unchanged, then compare the retested card.

Expected case outcomes: Normal A/B/C may reach internal reviewed records; Missing Contact → Clarification required; WR-104 → Duplicate confirmed after comparing log; Ambiguous Safety Note → Manual assessment required, approval blocked. Safe exception handling is not a successful completed automation job. There should be no new duplicate card, invented contact/safety decision or external action.

## Calculator checks without code
With summary-values.csv opened in Calc, column C contains numeric seconds/counts. Enter `=C2-C3` for 840, `=C4-C5` for 1410, `=C4-C5-C7` for 750, and `=C4-C5-C7-C6` for −2370. Format seconds explicitly; entering 38:00 as an ordinary spreadsheet time may mean hours rather than minutes. Keep original seconds column visible. Compare formula results against this guide.
