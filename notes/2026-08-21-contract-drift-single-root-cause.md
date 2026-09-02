---
id: 2026-08-21-contract-drift-single-root-cause
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, meta-lesson, contract-drift, validation, code-generation]
sources:
  - ref: "Archive turn 459: the delivered STAG_LIFECYCLE_AND_HARDENING.md summary states '§3 Diagnostic report ... All 5 classes trace to one thing: contract drift at an unchecked seam,' the direct source of this note's claim"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [459, 459]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Every deploy-blocking bug hit during this session's frontend-backend reconciliation and Railway deploy traced to the same root cause: contract drift at an unchecked seam
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, all five cited incidents traceable to the source transcript and consistent with sibling notes in this batch. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent traced this pattern across five distinct incidents in the same session (tool entitlements table, jobs table columns, tool-catalog slugs, .env.example vars, frontend API paths) and it held in every case
- verified: 2026-08-21
## Body
Across a single session spent taking a STAG-generated FastAPI + Next.js + Supabase project from ~107 TypeScript errors to a live Railway deploy, every bug that cost real time had the identical shape: two parts of the system that were supposed to agree — the frontend's API client vs. the backend's real routes, a service's table references vs. what migrations actually created, one migration's column names vs. what the application code queried, three separate definitions of the same tool catalog (an enum, a Stripe price map, and a SQL seed), and the `.env.example` template vs. the config module that actually reads environment variables — had silently diverged, because nothing machine-checked the seam between them. Each individual file was syntactically valid and compiled or imported cleanly in isolation; the drift was only visible where the pieces met. The durable lesson: in an AI-generated multi-layer codebase, correctness within a single file or module is not evidence that the seams between modules agree, and every such seam needs a machine-checked gate rather than an assumption that independently-generated pieces will match.
REVIEW: high-impact
## Links
- related, 2026-08-21-three-validator-checks-added-env-parity-tsc-gate-db-integrity.md, the concrete generation-time checks built in this same session to catch this exact pattern going forward
