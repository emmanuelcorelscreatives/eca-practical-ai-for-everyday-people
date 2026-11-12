# Lesson 206 — Prevent Duplicate Outputs and Actions

Emmanuel Corels Academy · Practical AI for Everyday People

All names, registrations and histories in this kit are self-created fictional practice data. No external message, purchase or real registration is performed. The offline lab is an Academy teaching application, not Google Sheets or a commercial automation product.

## Try the safeguard

Open `duplicate-lab.html` in a browser. It runs locally without a server or network. Reset clears this tab's practice state. Reload also starts empty; this demonstration is not a production database or durable cross-tab lock.

1. Keep SUB-1042, Lina Okafor, Introduction to Community Gardening and Needs step-free access unchanged. Inspect the empty Registration Log, then press **Run input**. RUN-01 must show zero matches, the no-match path, one creation and one destination row.
2. Press **Run input** again without changing the identifier. RUN-02 must show one match, Duplicate blocked, Create: Not run, and the same single destination row. Compare the destination and decision log, not merely the completed badge.
3. Change only the identifier to SUB-1098 and run. This new submission is accepted despite the same personal details. There are now two destination rows, with distinct Source IDs.
4. Reset. Submit SUB-1042, then replay it with a changed note. The lab sends this changed duplicate to manual review without creating or silently updating a row. Checked By remains blank; record a real reviewer only after actual review.

## Spreadsheet fallback

Import `data/registration-empty.csv` into a new practice spreadsheet. Keep existing private sheets closed. After the first run use `data/registration-after-first.csv` as the expected fictional state. In Google Sheets enter `=COUNTIF(A:A,"SUB-1042")` in a separate check cell; it returns 1 for this fixture. Do not paste this formula into column A. For these controlled uppercase, hyphen-and-digit fixtures, a count of zero permits manual addition, one blocks another creation, and more than one requires investigation. COUNTIF is case-insensitive and treats wildcard characters specially, so it is not a universal case-sensitive literal-ID matcher. Before applying this fallback to other source identifiers, document a source-ID policy that excludes case-distinct IDs and wildcard ambiguity; otherwise stop for manual exact review rather than treating the count as authoritative. Do not normalize legitimate distinct IDs merely to fit the formula. COUNTIF is a decision aid, not a lock or a tool that prevents other automation from writing.

Use `data/manual-review.csv` to record the attempted identifier, count, decision and reference. Leave Checked By blank until someone actually checks. The CSV examples are expected fixture states, not evidence of a vendor application run. Capture your own actual spreadsheet observations if completing the exercise there.

## Stable identifiers and overlapping runs

Preserve the source event ID through retries. Never replace it with a new retry ID or infer identity from a name, time, email or generated summary. SUB-1043 and SUB-1042 are different. This lab compares exact strings without trimming or case folding.

A search followed by create has a race: two concurrent runs can each see zero before either writes. This single-tab synchronous lab demonstrates the branch rule, not distributed concurrency safety. Before unattended use confirm a destination unique constraint, atomic create-if-absent, supported idempotency or safe serialized processing with your selected platform. An upsert must not overwrite meaningful changes without an explicit policy. If your tools cannot provide protection, keep the process manual. Plan and permission availability vary.

## Save your evidence

Record the source input, exact identifier, lookup count, branch, creation result, run reference and destination count after first run and replay. Avoid unnecessary personal data. Export the lab evidence with **Download evidence**; its metadata honestly identifies an offline Academy fixture run. `expected-results.json` is an answer key, not a record of your work.

Before reuse: stable ID preserved; exact lookup; match blocks creation; accepted and duplicate decisions logged; destination count checked; overlapping-run protection verified. Next lesson covers timeouts, retries and stop conditions.
