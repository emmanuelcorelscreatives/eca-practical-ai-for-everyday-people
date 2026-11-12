# Understand Connected-App Permissions
Emmanuel Corels Academy · Practical AI for Everyday People · Stage 3, Lesson 16.

Open `permission-simulator.html` in a modern desktop browser. It works entirely offline: no network requests, account connection, uploads, messages or real permission grants. All controls simulate decisions using self-authored fictional data. It is a teaching tool, not a replica of any provider's current interface. The saved lesson asks for a Windows 11 browser demonstration; learners can practice the simulator on other platforms too.

The task is to extract the dates in **Community Garden Schedule — Sample.docx** into a new summary draft, leaving the source unchanged. The matching JSON file is the accessible machine-readable source. Sample dates are illustrative, not a real calendar.

## Practice
1. Read `exercise.md`, record your decision, and use **Review requested permissions**. Decline the broad request.
2. Choose only the sample file and viewing access; choose session access. Confirm account, resource, capability and duration before allowing it.
3. Run the sample, compare each date with the source and remove the deliberately unsupported sentence.
4. Inspect the simulated activity record, disconnect, and verify that future access stops while the draft remains.
5. Reset and use manual handoff. It copies the local example only; it does not upload anything.

Read-only limits source changes; it does not promise that a real service never retains or shares retrieved information. Check the real provider's current resource scopes, data terms and account settings. Do not bypass organization approval. If suitable narrow access is unavailable, decline or use a permitted manual method. Revoking access is not an undo function.

`answer-key.md` gives expected decisions and source-backed dates. `verify.py` checks the kit and simulator's safety/content boundaries with Python 3, without external packages. No real credentials or private files are required.

The draft is a deterministic, prewritten teaching fixture containing one deliberate unsupported sentence. No AI model is called, and no provider authorization is performed. The app demonstrates decisions and state transitions, not a vendor service. Actual QA captures use Linux Chromium with the same platform-independent app; Windows-specific steps are not taught.

Use the visible Practice navigation for Capabilities, Read-only and retention, Organization approval, Checklist, Decision rule and the next-lesson preview. Manual handoff records a separate local run. After removing the unsupported sentence, choose **Save reviewed draft** to download a local text file; this is a real local save, with no upload or publication.
