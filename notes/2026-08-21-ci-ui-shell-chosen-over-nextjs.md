---
id: 2026-08-21-ci-ui-shell-chosen-over-nextjs
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, frontend, vite, nextjs, ui, decision]
sources:
  - ref: "Operator's AskUserQuestion choice between the two-frontend fork, and the agent's edit stripping the LossExceedanceCurve import from the chosen Vite shell"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [124, 181]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — operator's explicit choice via an AskUserQuestion turn, then implemented and verified green in the same session
- verified: 2026-08-21

## Body
As of 2026-07-31, the Compliance Intelligence project had two frontends: `frontend-vite` (`ci-ui-shell`, an 812-line shell with clients/engagements, KB search, evidence intake, and a command palette, matching `SPEC_CI_UI_SHELL`) and `frontend/` (a thin Next.js `Shell` wrapper). When the operator asked to see and polish the UI, the agent surfaced this fork and asked which to invest in; the operator chose the Vite `ci-ui-shell`. As part of the same decision, the agent stripped the `LossExceedanceCurve` (FAIR/actuarial) view and its import out of `ci-ui-shell`, replacing the actuarial/legacy ternary with a single compliance-findings table (severity, what-we-saw + URL, authority citation, evidence class, confidence) — consistent with the actuarial engine being out of CI's scope and slated for relocation to the Valen agent. The `LossExceedanceCurve.tsx` file itself was left on disk, not deleted, since moving it out of the tree wasn't this agent's job. The live shell was then run against a real seeded engagement (7 cited findings from the risky fixture, 1 correctly filtered below the 0.70 confidence floor) to confirm the table rendered real data before any visual polish began.

## Links
- precedes, 2026-08-21-ci-ui-design-system-clinical-trust.md, the aesthetic direction chosen for this same shell later in the session
