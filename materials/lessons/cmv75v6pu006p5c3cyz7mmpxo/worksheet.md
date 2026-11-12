# Set a Stop Rule for Good Enough

Emmanuel Corels Academy · Practical AI for Everyday People · Stage 7, Lesson 42

Use only the fictional notes in `source-notes.md`. Goal: a community-board notice of **at most 90 whitespace-separated words**, accurate and easy to scan. This is a classroom comparison, not permission to publish an incomplete real notice.

1. Read source notes before looking at the drafts. Separate confirmed facts from gaps.
2. Open `first-weak-output.txt`. Find the missing deadline and unsupported audience claim. Record exact defects in `comparison-blank.csv`.
3. Compare factual correction v1 with the source. Its facts pass, but examine the dense paragraph as a board notice.
4. Open v2. Verify unchanged facts, visible separate registration line, readable layout and word count. The registration method remains visibly missing; do not invent it.
5. Compare v3. It adds an optional closing, length and review effort. Explain why the shorter v2 serves this particular purpose better.
6. Complete `decision-record.md`. Accept v2 **for this bounded classroom exercise**, with the missing-method limitation visible. A real notice that must enable registration is held until its organizer supplies a confirmed method.
7. Practice: make three targeted revisions of the weak output, preserving passed facts. Three is a practice limit, never a universal production rule. Compare your result against the original notes after each edit.

Initial prompt: “Using only the supplied notes, draft a warm community-board notice of no more than 90 words. Include the registration action. Label any missing information instead of guessing.”

Correction 1: Add the supplied deadline; remove the unsupported audience claim. Preserve all confirmed details and label the missing registration method.
Correction 2: Preserve verified wording, separate the registration action and stay under 90 words.
Correction 3: Change only the closing. Keep verified details, limitation and length limit intact. Decide whether that preference is worth the extra review.

Five checks: purpose, must-haves, independent checks, destination, marginal value. One failed critical requirement is not canceled by a good average. Consequential decisions need stronger evidence and proper human review.

Manual fallback: open the best checked draft in an ordinary editor, correct the single defect and inspect the final artifact. No paid assistant, personal account or external action is needed.

Optional deterministic checks: run `python3 check_examples.py` from this directory. It checks exact fixture facts, the intentional weak-output failures and word limits; it cannot certify subjective tone or real-world suitability. On a system without Python, use the printed checklist and count space-separated tokens manually. No external dependencies or network are used.

Open `cleartask-practice.html` in a browser for the functional offline ClearTask practice worksheet. Navigate the prepared fictional fixture states, edit the notice, count current words and download a decision note. It makes no network requests and generates no AI response; all outputs are clearly identified as prepared examples. It is a purpose-built Academy application, not a copy of a vendor product.
