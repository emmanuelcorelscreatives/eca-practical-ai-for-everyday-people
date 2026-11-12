# Source → extract → structure → verify → record → preserve
Keep four distinct layers: original notice; recognized draft text; unchecked assistant extraction; checked record. Never overwrite the original with corrected OCR.

## Source check
Both Maple Court pages must be visible, ordered and readable. Inspect corners, focus, glare, dates, times and small print. Missing or unreadable pages require a new source; do not guess.

## Seeded mistakes to find
The OCR fixture changes 23 October to 28 October and 12:00 to 17:00. The unchecked extraction fixture says “All residents” while dropping the no-change exception. A correct date alone does not make that row safe.

## Structured fields
Document date; event/deadline; requested action; who acts; exception/condition; alternative; contact; unresolved question; source page. Quote important conditions. Do not infer missing facts.

## Expected checked records
Contact review: issued 6 October 2026, deadline 23 October 2026, send updated contact details only if listed details changed; otherwise no response. Page 1 supplies that condition. Page 2 supplies the online alternative and identity-document prohibition.
Closure: 19 October 2026, 10:00–12:00; requested action None stated. Preserve the online alternative and no-emailing-identity-documents warning separately from any action. Page 2 supplies the event.

Unresolved: whether previous email addresses should be repeated when only a telephone number changed. Record the gap; contact the issuer through a trusted original route only if necessary. The exercise performs no contact.

## Final check
Check dates/times, actions, who must act, exceptions/prohibitions and missing information against the original pages. Watch only, unless, except, if and not. Transfer only checked rows to the register; keep source filenames and verification status.

Preserve `2026-10-06_Maple-Court_Contact-Review_Original.pdf` separately from `2026-10-06_Maple-Court_Contact-Review_Checked-Summary.pdf`. No name, telephone number or other private identifier belongs in these filenames. Manual CSV completion remains a full offline fallback if OCR or an assistant is unavailable.

## Field provenance and exact conditions
Every independently copied response row retains the identity-document prohibition. `condition_quote`, `no_change_quote` and `prohibition_quote` preserve exact operative source text beside normalized fields. `field_source_pages` maps each field to its actual source page. Page one establishes the response deadline/actor/exception; page two establishes closure, alternative, contact and prohibition. The primary `source_page` is the event page; `source_pages` covers all source facts in that record. Prepared unchecked fixtures are explicitly UNVERIFIED at row level.
