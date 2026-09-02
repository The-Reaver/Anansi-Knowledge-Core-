---
id: 2026-08-21-knowledge-core-proto-store-scaled-13x-since-08-03-checklist-snapshot
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision — added a parenthetical noting the note count has already grown past the 557 figure (683 as of reverification). Operator retains veto per Mandate 1."
project: fleet
tags: [anansi, knowledge-core, checklist-refresh, proto-store, structure-notes, scale]
sources:
  - ref: "Archive turns 218-229: STAG master-checklist refresh sweep, 2026-08-21, workstream 'Living Knowledge Core / Anansi' — direct file count against the live repo tree, cross-checked against commit a535f05"
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Living Knowledge Core / Anansi\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

- class: confirmed
- confidence: high, direct file count against the live repo tree
- verified: 2026-08-21

# The Living Knowledge Core proto-store has grown from 42 atomic notes / 0 Structure Notes (2026-08-03) to 557 atomic notes / 4 Structure Notes (2026-08-21) — the master checklist's snapshot is 18 days and ~13x out of date

## Body

The 2026-08-03 master status checklist described the pre-deployment proto-store at
`research/knowledge-home/` as holding "42 atomic notes, zero Structure Notes, as of 2026-08-03."
As of 2026-08-21, `research/knowledge-home/notes/` holds 557 atomic `.md` notes and
`research/knowledge-home/structure-notes/` holds 4 Structure Notes (`artifact-registry.md`,
`brain-trust-on-demand-protocol.md`, `native-library-curriculum.md`, `terminal-glossary.md`).
That is roughly 13x growth in atomic notes and the first Structure Notes of any kind, all
accumulated in the 18 days since the checklist's snapshot date.

This growth is not one commit — it is the accumulated output of a governance process that has
been running continuously: dated `candidates/` batches reviewed against a promote/reject rubric,
then ratified into `notes/`. The single largest jump is documented in commit `a535f05` ("Clear the
entire Anansi candidate backlog and close both governance gates," 2026-08-21), which alone moved
the note count from 395 to 543 by promoting 176 candidates in one sweep. `research/knowledge-home/
candidates/` still holds 256 files across 7 dated folders plus `needs-work/`, `_to_delete/`, and
two archived batches — so the pipeline is active, not caught up to zero, but the backlog has been
worked down aggressively rather than left to accumulate since 08-03.

Separately and unchanged: `specs/SPEC_KNOWLEDGE_CORE.md` still reads "Status: build-ready, not yet
released to Orlok" (last content commit 2026-08-10, `f638846`), and section 8 still states "Not
released to Orlok. GEO stays priority 1. Phase 2 opens only on the operator's word, after Phase 1
is clear." No evidence was found in commits or notes since 08-03 that Phase 1 of the CI (Compliance
Intelligence) sequence has closed. So the checklist's claim about the *spec's* build/release status
still holds today — only the *proto-store's scale* claim is stale. This is a case the checklist's
own method anticipates: two sub-claims under one workstream, one confirmed unchanged, one
materially outdated — named separately rather than collapsed into a single verdict.

(Reverified 2026-08-25: `research/knowledge-home/notes/` had already grown to 683 atomic notes, up
from 557 four days earlier, while `structure-notes/` still held exactly 4. The 13x figure above
captures the 2026-08-21 snapshot only and should not be read as still-current at promotion time —
the direction and pace of growth are the durable finding, not the specific counts.)

## Links
