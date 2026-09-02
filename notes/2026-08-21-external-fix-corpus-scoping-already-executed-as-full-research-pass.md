---
id: 2026-08-21-external-fix-corpus-scoping-already-executed-as-full-research-pass
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [external-fix-corpus, program-repair, research, checklist-staleness]
sources:
  - ref: "Turns 218-229: assistant launches an 18-workstream background re-verification sweep of the 2026-08-03 master checklist (turn 218) and consolidates the sub-agents' findings, including the older-backlog / external-fix-corpus workstream, for the operator (turn 229)."
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

# "External fix-corpus batch scoping," named as untouched backlog on 2026-08-03, had already become a completed single-agent deep-research pass across three linked topics by 2026-08-08, now sitting one reconciliation step from Core promotion
- id: 2026-08-21-external-fix-corpus-scoping-already-executed-as-full-research-pass
- type: finding
- status: ratified
- class: confirmed
- source: STAG master-checklist refresh sweep, 2026-08-21, workstream "Older backlog (SafeGuard Identity booking, AI clinical scribe research, Fleet Dashboard release-to-Orlok, external fix-corpus scoping, Postgres/pgvector provisioning, Lords of Cian Archive + NYC Marketplace Lovable builds)"
- confidence: high, directly read the research briefs, the state-tracking file, and the promoted ratified note
- verified: 2026-08-21
- tags: external-fix-corpus, program-repair, research, checklist-staleness

## Body

reports/STAG_MASTER_CHECKLIST_2026-08-03.md lists "External fix-corpus batch scoping" under "Older backlog, not touched this session," referring back to research/knowledge-home/notes/2026-08-02-external-fix-corpus-idea-sourced-and-scoped.md, which as of 2026-08-02 described only "the new work is only the intake and validation half, a Knowledge Core batch Oluwole and Moonshadow should scope" -- i.e. a scoping task, not yet run.

By 2026-08-08 it had gone well past scoping. A Research role was established that day (research/knowledge-home/notes/2026-08-08-research-role-and-biweekly-cycle-established.md, ratified 2026-08-20), which scoped the idea as Batch 9/Topic 16 in RESEARCH_MASTER_LIST.md and then actually ran it: a full single-agent deep-research pass producing research-briefs/2026-08-08-historical-fix-corpora-brief.md (24 atomic candidate notes covering CVE-linked datasets, fuzzing-bug corpora, program-repair benchmarks, and compiler bug trackers for C/C++/Rust/kernel code) plus a same-day corrected-ranking addendum. Two companion topics (Batch 11/Topic 18, Batch 12/Topic 19) were run the same day, closing what research/RESEARCH_CYCLE_STATE.md calls a "2x2 research program" (low-level vs. high-level language, diff-only vs. full-narrative).

Per the state file's own documented workflow, this is one of three legs (Claude/Qwen/Gemini deep research, meant to be reconciled before promotion) -- as of 2026-08-20 (per RESEARCH_CYCLE_STATE.md's own "not yet -- needs Qwen + Gemini legs" note, still current), it has not been reconciled and its 24+ atomic notes have not yet been individually promoted into research/knowledge-home/candidates/ under the Knowledge Home's own note schema. So the item is not fully closed either -- but "not touched this session, still at planning-document stage" materially understates it: real research work, not just scoping, has already happened and is one reconciliation step from Core promotion.

## Links
- corrects: the 2026-08-03 master-checklist claim for workstream "Older backlog" (external fix-corpus batch scoping item)
- see also: research-briefs/2026-08-08-historical-fix-corpora-brief.md, research-briefs/2026-08-08-historical-fix-corpora-ranking-addendum.md, research/RESEARCH_CYCLE_STATE.md, research/knowledge-home/notes/2026-08-08-research-role-and-biweekly-cycle-established.md
