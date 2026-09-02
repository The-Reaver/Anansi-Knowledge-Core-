---
id: 2026-08-23-ratification-line-template-had-duplicated-wording-bug
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i hereby ratify these notes\"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [anansi, knowledge-core, ratification, tooling-bug, template]
sources:
  - ref: "Assistant turn spotting the bug while ratifying 13 notes: \"I also see the ratification line has a duplicated phrase bug ('operator directly ratified via operator directly ratified via...') — my source string duplicated wording the template already adds on top. Let me check how widespread that is before fixing anything.\" Followed by: \"All 13 have it. Fixing that cosmetic duplication in each, plus the secret-scan false-positive itself in the one flagged file.\""
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [846, 849]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The ratification-line generator duplicated a phrase across all 13 notes it stamped, because the script's own source string repeated wording the template already added on top

- id: 2026-08-23-ratification-line-template-had-duplicated-wording-bug
- type: finding
- status: ratified
- ratified: 2026-08-23 — operator directly ratified via explicit operator instruction ("i hereby ratify these notes"), given after reviewing an operator-facing note-by-note review report covering all 7 (all 7 read in full, all 10 cross-referenced links confirmed to resolve, no factual errors found).
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 784-900
- confidence: high — directly observed the duplicated text in a written note file and confirmed via grep that all 13 ratified files carried it
- verified: 2026-08-23
- tags: anansi, knowledge-core, ratification, tooling-bug, template

## Body
When the 13 candidate notes from the 2026-08-22 distillation pass were ratified, the tool that wrote each note's `ratified:` frontmatter line produced a visibly broken result — a phrase reading roughly "operator directly ratified via operator directly ratified via..." A source string that was meant to be inserted once into a template was itself already carrying the same "operator directly ratified via" wording the template wrapper added on top, so the two concatenated instead of one substituting cleanly into the other. Because all 13 notes were stamped in the same batch using the same script, the bug was not isolated to one file — a grep across the batch confirmed all 13 carried the duplicated phrase.

The fix was purely cosmetic (rewriting the ratified-line text in each of the 13 files to remove the duplication) and did not require re-deciding anything about whether the notes should be ratified — the underlying ratification instruction and review were unaffected, only the recorded wording was wrong.

General lesson: when a script assembles a human-readable audit-trail line (like a ratification or approval stamp) by inserting a caller-supplied string into a fixed template, both the template and every caller-supplied string need to be checked together for accidental phrase duplication — this class of bug is easy to introduce silently since each half looks correct in isolation, and it will replicate identically across every record a single batch run produces.

## Links
- relates, 2026-08-20-self-asserted-ratification-lines-are-not-verification.md — a different failure mode in the same category of artifact (a ratification line's text), here a mechanical wording bug rather than a fabricated claim; both underline that the exact text of a ratification line deserves scrutiny, not a rubber stamp.
