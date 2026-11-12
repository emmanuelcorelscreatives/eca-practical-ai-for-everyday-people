# Lesson 200 — Design a Reviewable Approval Request

This fictional Community Garden practice kit matches the saved lesson. Work offline; no real account, recipient, post or booking is involved. All consequential external actions remain disabled. This lesson builds the request; the next lesson teaches decision branches.

## Open the evidence

Open `event-brief.json`, `venue-confirmation.md`, the banner and its permission record. These are self-created teaching records. Compare date (Saturday, 24 October 2026), time (10:00–13:00), activities, free entry and fictional location with `approval-request-v1.json`. Accessibility details and contact method are deliberately absent. Do not fill them with guesses.

## Build and inspect the packet

1. Open `approval-practice.html` in a browser. It is a functional, product-neutral Academy practice app, not a reproduction of Zapier or Power Automate. It has no network connector or publishing function. Use its section selector to inspect the same record from workflow through audit log.
2. Read the full action and exact destination, including page ID and non-public visibility. Open `test-destination-action-config.json` separately and compare channel, page ID, name, visibility and disabled publishing state. This is a fictional local target record, not a connected vendor account. The consequence concerns one proposed post, not unrelated pages.
3. Inspect the complete generated draft and actual included banner. Open the linked records; the comparison table is only a convenience, never a replacement for reading evidence.
4. Keep assumptions, absent facts and generated wording visibly separate from opened records. The version-1 request is incomplete. Approval is unavailable while essential details and reviewer authority remain unresolved.
5. Inspect explicit decision controls, the version and audit fields. Do not turn an empty decision, timeout or service failure into approval. Real publishing stays disabled even if a practice rejection is recorded. Reject creates a browser-local record with version, reviewer, decision and time; the Audit view shows the same record after changing sections or reloading. It never changes the supplied CSV: for the manual exercise record decisions explicitly in your own copied register. Clear browser site storage to reset a local practice record.
6. Build a manual fallback: copy the complete packet and all supporting records into a folder called `Pending Review`. Keep `review-register.csv` beside it; leave the decision/time blank and external action Disabled.
7. Complete `approval-request-template.md` for a second fictional draft, preserving the same action boundary. Use no real private account data.

## Check understanding

A request must make six things inspectable: action, destination, complete content, support, uncertainty and version. A friendly page name without page identity is insufficient. A generated summary cannot independently confirm itself. A hidden attachment cannot be approved merely from a paperclip icon. Review authority must cover the specific destination.

## Exercises

A. List every absent field in version 1 and explain why each should remain unresolved. B. Identify the source for the location, date, time and entry claims. C. Replace the vague heading “Draft ready — Continue” with an explicit consequence. D. Change the destination to a second fictional page in your copied packet: explain why earlier approval would no longer cover it. E. Leave the decision blank in the register: explain the only safe external-action state. F. Explain a manual packet's minimum contents when your subscription has no built-in approval feature.

## Expected observations

See `answer-key.md`. Optional machine-readable checks: run `python3 check_kit.py` from this directory using Python 3 (standard library only). No packages, accounts or API keys needed. The check validates this supplied teaching dataset and safety boundaries; it does not approve real content or establish a user's permissions.
