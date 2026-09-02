---
id: 2026-08-25-multi-agent-diagnostic-sweep-pattern
type: finding
status: ratified
ratified: "2026-08-25 — Brain Trust + AJ ratification pass (seats: Celestina, Jasiah, Oluwole, Omar, Sentinel; AJ independent audit). Vote and conditions recorded in reports/STAG_BRAIN_TRUST_LEDGER.md. Operator ruling per Mandate 1."
project: agame-sports-rebuild
tags: [diagnostics, multi-agent, code-review-methodology, content-accuracy]
sources:
  - ref: "Two parallel-agent sweep rounds on a real 94-page Astro site: 3 lens-agents (turn 2) and 5 content-area agents (turn 50), A-Game Sports rebuild, 2026-08-25"
    reliability: medium
    origin: "A-Game Sports rebuild remote session, 2026-08-25; transcript reconstructed manually and ingested into the Core by the bridge-cse session the same day"
provenance:
  archive: research/knowledge-home/raw/2026-08-25-agame-remote-diagnostics-and-content-sweep.jsonl
  turns: [4, 60]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

> **Provenance added 2026-08-25 on ingest.** This note was authored in a remote container with no
> access to the Core, so it originally carried no ADR-0005 provenance pointer. The session
> transcript has since been ingested (96 records) and the turn range above was read off that
> archive, not estimated. Ratified 2026-08-25 by the Brain Trust + AJ pass; the
> conditions that ruling attached have been applied to this note.

# A three-lens parallel-agent sweep finds cross-page factual drift a linear read misses
- id: 2026-08-25-multi-agent-diagnostic-sweep-pattern
- type: finding
- status: ratified
- ratified: 2026-08-25 Brain Trust+AJ
- class: confirmed
- source: A-Game Sports rebuild diagnostics session, 2026-08-25
- confidence: high — directly observed across two rounds on a 94-page site
- verified: 2026-08-25
- tags: diagnostics, multi-agent, code-review-methodology, content-accuracy

## Body
Splitting a full-codebase or full-site audit into parallel subagents by lens (architecture / code-quality / content-SEO) and then, in a second pass, by content area (About/Legal, Camps, Sport-hub pages, etc.) surfaced defects a single linear pass would not: the same real fact (a director's years of experience) stated as three different numbers across three separate pages, none internally wrong on its own — only visible by cross-referencing outputs from independent agents each reading different subsets of the same site. The pattern that worked: run N agents read-only over disjoint file sets with an identical structured-finding prompt, then synthesize by hand into one report, deduplicating same-root-cause findings across files rather than listing near-duplicates. A global grep pass (e.g. for exact-duplicate H1 strings) run by the orchestrator directly, before or after the agent sweep, catches the class of bug agents can miss when it spans files outside any single agent's assigned batch.

## Links
- extends, ../../structure-notes/brain-trust-on-demand-protocol.md, applies the standing Brain Trust on-demand pattern to a content-accuracy domain rather than a build/security domain
