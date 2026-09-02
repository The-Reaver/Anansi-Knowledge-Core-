---
id: 2026-08-21-defects4c-existence-contradiction-between-two-core-sources
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (Brain Trust resolution applied: Defects4C independently confirmed real via live lookup, closing the contradiction this note names). Operator retains veto per Mandate 1."
project: fleet
tags: [external-fix-corpus, defects4c, contradiction, source-conflict]
sources:
  - ref: "Turns 218-229: assistant launches an 18-workstream background re-verification sweep of the 2026-08-03 master checklist (turn 218) and consolidates the sub-agents' findings, including the older-backlog / external-fix-corpus workstream where this source conflict surfaced, for the operator (turn 229)."
    reliability: high
    origin: "STAG master-checklist refresh sweep, 2026-08-21, workstream \"Older backlog (SafeGuard Identity booking, AI clinical scribe research, Fleet Dashboard release-to-Orlok, external fix-corpus scoping, Postgres/pgvector provisioning, Lords of Cian Archive + NYC Marketplace Lovable builds)\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [218, 229]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Two dated Core sources directly disagree on whether the "Defects4C" bug-repair dataset is real -- named here rather than silently resolved
- id: 2026-08-21-defects4c-existence-contradiction-between-two-core-sources
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Older backlog (SafeGuard Identity booking, AI clinical scribe research, Fleet Dashboard release-to-Orlok, external fix-corpus scoping, Postgres/pgvector provisioning, Lords of Cian Archive + NYC Marketplace Lovable builds)"
- confidence: medium -- the two sources are in direct, dated conflict; this note reports the conflict rather than resolving it in either direction
- verified: 2026-08-21
- tags: external-fix-corpus, defects4c, contradiction, source-conflict

## Body

While re-verifying the "external fix-corpus batch scoping" item (see the companion finding on that item's actual progress), two ratified/candidate Core sources were found in direct disagreement over the same named dataset.

research-briefs/2026-08-08-historical-fix-corpora-brief.md (part of the 2026-08-08 Batch 9/Topic 16 research pass) reports, under its "defects4c-name-preexists-scope-assumption" atomic note, high confidence, that a real dataset named "Defects4C" was found and directly confirmed: "Wang, Xie, Hu, Liu, Yu, Kong, Li, 'Defects4C: Benchmarking Large Language Model Repair Capability with C/C++ Bugs,' ASE 2025, arXiv:2510.11059, Nov 2025" -- fetched directly from the project site and arXiv abstract, and cited repeatedly through the brief's synthesis and ranking addendum as a top-tier, test-validated benchmark.

research/knowledge-home/notes/2026-08-20-precedent-mining-bug-fix-corpora-for-sourced-examples.md (ratified 2026-08-20, harvested from a different session) states the opposite in its own revision note: "'Defects4C,' could not be confirmed to exist under that name during this review -- it may be a garbled reference to Defects4J or a different corpus entirely."

Both are dated Core sources with stated confidence levels; neither cites or links to the other. This sweep did not independently re-verify the arXiv ID (arXiv:2510.11059) or the project site (defects4c.github.io) named in the 2026-08-08 brief, so it cannot adjudicate which source is correct -- only that they conflict and the conflict is currently unresolved anywhere in the Core. If the Batch 9/Topic 16 research is reconciled and promoted (see the companion finding), this contradiction should be resolved as part of that pass, not carried forward silently.

**Resolution (2026-08-25, Brain Trust review):** Jasiah and Oluwole independently ran live lookups (WebSearch/arXiv/IEEE Xplore/OpenReview/ResearchGate) and confirmed "Defects4C" is a real dataset: arXiv:2510.11059, ASE 2025, also indexed on IEEE Xplore (document 11334503) and OpenReview (gXK3Y6WNVv). The 2026-08-08 brief was correct. The 2026-08-20 note's "could not be confirmed" claim was a failed/incomplete lookup (plausibly a training-cutoff gap for an Oct 2025 paper), not evidence of nonexistence, and has been corrected directly -- see `notes/2026-08-20-precedent-mining-bug-fix-corpora-for-sourced-examples.md` (already separately corrected; not touched by this note). This is not a genuine unresolved contradiction as of 2026-08-25.

## Links
- see also: research-briefs/2026-08-08-historical-fix-corpora-brief.md (asserts Defects4C is real), research/knowledge-home/notes/2026-08-20-precedent-mining-bug-fix-corpora-for-sourced-examples.md (originally asserted it could not be confirmed; corrected 2026-08-25), research/knowledge-home/candidates/2026-08-21/2026-08-21-external-fix-corpus-scoping-already-executed-as-full-research-pass.md
- resolved-by: Brain Trust review, 2026-08-25 (live lookup confirming arXiv:2510.11059 / IEEE Xplore 11334503 / OpenReview gXK3Y6WNVv)
