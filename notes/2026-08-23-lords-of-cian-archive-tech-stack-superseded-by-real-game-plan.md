---
id: 2026-08-23-lords-of-cian-archive-tech-stack-superseded-by-real-game-plan
type: finding
status: ratified
ratified: "2026-08-25 — anansi-promote skill run, 7/10 (novelty 2, evidence 2, actionability 1, generality 1, non-contradiction 1). Promoted WITH REVISION: one factual claim is contradicted by the real repository."
project: lords-of-cian
tags: [lords-of-cian, archive, tech-stack, supersession]
sources:
  - ref: "Direct within-session correction, 2026-08-23; router claim checked against the real repository 2026-08-25 and found contradicted"
    reliability: medium
    origin: "2026-08-23 Lords of Cian session; re-verified 2026-08-25 anansi-promote run"
provenance:
  archive: research/knowledge-home/raw/2026-08-23-lords-of-cian-cult-network-and-archive-planning.jsonl
  turns: [1, 96]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The earlier same-day speculative tech-stack proposal for the Lords of Cian archive is superseded by a real, reconciled game plan the operator supplied later the same session

- id: 2026-08-23-lords-of-cian-archive-tech-stack-superseded-by-real-game-plan
- type: finding
- status: ratified
- ratified: 2026-08-25 — anansi-promote skill run, 7/10 (novelty 2, evidence 2, actionability 1, generality 1, non-contradiction 1). Promoted WITH REVISION: one factual claim is contradicted by the real repository.
- class: confirmed
- source: this chat, 2026-08-23, Lords of Cian session
- confidence: high, direct within-session correction
- verified: 2026-08-23
- tags: lords-of-cian, archive, tech-stack, supersession
- project: lords-of-cian

## Body

Earlier in this same session, before the real archive status was known, a speculative proposal was drafted (see `2026-08-23-lords-of-cian-archive-and-studio-tech-stack-proposal`) guessing at the tech stack and inventing a `spoiler_tier` field for a Supabase schema believed not to exist yet.

Later the same session the operator supplied a real, fleet-reviewed, adversarially-reviewed strategy deliverable, "Lords of Cian Interactive Archive — Game Plan, Backlog & Engagement Roadmap" (dated 20 August 2026), describing an archive already substantially built as a Lovable project against a real repository, `The-Reaver/My-Rivals-Distance-Archive`. The speculative proposal's stack guess held up in substance (React, TypeScript, Tailwind, Supabase), with one correction: the actual router is TanStack Router, not Next.js, itself one of the contradictions the real plan's own audit step is meant to resolve. The invented `spoiler_tier` field is superseded by the real system's already-built four-level reader clearance model and a `published_books` unlock cascade tied to per-item book placement.

The operator also clarified the archive and a separate "studio app" are two different applications, not one system with two frontends as the earlier proposal assumed, and asked to focus on the archive specifically. The independence question the earlier proposal raised (`2026-08-23-archive-studio-independence-open-question`) is set aside for now rather than resolved, since it was framed around an assumption the operator has since corrected.

The earlier proposal and open-question notes are kept on disk rather than deleted, per this Core's own no-deletion convention, and should be read as historical context for how the real plan was arrived at, not as current direction. The real plan itself lives as a Claude Project doc, `lords-of-cian-archive-game-plan.md`, not in this Core.

## Links

- supersedes: 2026-08-23-lords-of-cian-archive-and-studio-tech-stack-proposal
- relates: 2026-08-23-archive-studio-independence-open-question (set aside, not resolved)
- relates: 2026-08-23-lords-of-cian-archive-repo-empty-and-possible-live-security-exposure

## Revision, 2026-08-25

The claim that "the actual router is TanStack Router, not Next.js" is **contradicted by the repository
itself**: `The-Reaver/My-Rivals-Distance-Archive` (checked 2026-08-25) contains
`apps/web/next.config.mjs`, i.e. a Next.js app. Note that the same repo's schema is a `knowledge_core`
operational schema on a `claude/lovable-build-review-nmep29` branch, so it may not be the reader-facing
archive at all -- meaning the router question is genuinely unresolved rather than settled either way.
Treat both the original TanStack claim and this Next.js observation as unreconciled until someone
confirms which codebase the deployed archive actually runs.
