# Clean Categories and Messy Text
Emmanuel Corels Academy · Practical AI for Everyday People · Lesson 146

Self-created fictional community-event requests. No private event records, personal identifiers, sign-in, paid AI or automatic spreadsheet access is required for the exercises. Files contain no macros or external links.

## Open the practice workbook
`Community_Event_Requests.xlsx` is an ordinary workbook with Original, Review Copy and Category List tabs. Import/open it in your permitted spreadsheet; Google Sheets is the product shown in the saved lesson visuals. If an import does not retain a control, use the CSV files and recreate the review columns/list manually. Preserve Original unchanged; do not sort only one column.

1. Inspect Original's six exact rows. Preserve the number 12 and the request for Two people; clean categories only, never rewrite requests.
2. Work in Review Copy. Suggested category, Review status, Confirmed category and Review note begin blank. Category List contains exactly Food, Transport, Accessibility, Supplies, Volunteer, Other.
3. Filter Category original to see FOOD, Transprt, Access, Equipment, volunteers and Pickup. Keep the request text visible; spelling alone does not settle meaning.
4. Optional assistant: provide only these fictional rows and `assistant-prompt.txt`, with no spreadsheet editing access. Interface/access varies. The separate proposal example is an authored exercise answer, not a claimed live AI response.
5. Enter proposals in Suggested category; record Clear or Needs review plus a reason. Leave Confirmed category blank until checking the original request and allowed list. Compare with `review-proposals-example.csv` only after trying this.
6. For EV-101, lunch boxes support Food; EV-102's van supports Transport; EV-103's ramp supports Accessibility; markers and tape in EV-104 fit this list's Supplies; two check-in people in EV-105 support Volunteer. These are local category decisions, not universal synonym mappings.
7. EV-106 says only Pickup. Suggested category and Confirmed category must remain empty. Status: Needs review. Exact question: What is being picked up, and is transport required? Do not invent an answer.
8. After review, confirm only the five supported values. `review-expected.csv` is the instructor reference for this fictional exercise. Filter Review status to Needs review: only EV-106 should remain. If real clarification later arrives, record it and the reason before choosing a category.
9. Preview any find/replace operation. Limit it to the selected category range, do not activate Replace all across the workbook, and never alter Original or request text. Sort/filter whole table rows so IDs/context remain linked.
10. The workbook's Confirmed category cells F2:F7 have a dropdown using the six-category named range. Imports may require recreation: apply only to F2:F7, source Category List A2:A7, allow blank. A valid dropdown choice is not evidence that it is correct for Pickup.

## Independent checks and manual route
Run `python3 verify_reference.py` in this folder for structural/reference integrity checks. It does not make category decisions or approve a person's work. Without Python, compare six IDs and their original text, the approved list, five Clear rows, the blank unresolved row and every explanation. Without AI, use the filter, separate columns and careful manual edits; the evidence and uncertainty rules are identical.

## Five-part final check
Preserve original; use approved list; check row context; confirm clear changes; leave uncertainty visible. A neat column with a guessed value fails this exercise.

## Provenance and licence
All provided data, reference proposals and reasons were authored for this course. No actual external assistant transcript or human event-owner clarification is claimed. The source lesson remains unchanged. Practice files: CC0-1.0.
