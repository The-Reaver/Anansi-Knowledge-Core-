---
id: 2026-08-21-adapt-few-lib-modules-to-many-consumers
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, frontend, typescript, refactoring, leverage-pattern]
sources:
  - ref: "Archive turn 163: the agent's own end-of-task results summary after reaching tsc 0 errors, detailing the lib/hook-layer changes (role helpers accepting a flexible RoleLike union, billing.ts/members.ts gaining consumer-facing wrappers) that cleared ~107 TypeScript errors across ~30 files by editing a handful of shared modules"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [163, 163]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# When many generated frontend consumers expect a simpler API than the few lib/hook modules actually provide, adapt the few provider modules rather than editing every consumer
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the ~107-error/~30-file figure and named examples match the session's results summary. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent applied this and reported it cleared roughly 107 TypeScript errors across about 30 files by changing a handful of lib/hook modules
- verified: 2026-08-21
## Body
Taking a STAG-generated Next.js frontend from ~107 TypeScript errors to zero, the winning pattern (carried over from a prior handoff and confirmed again this session) was to identify the small number of shared lib/hook modules that many page/component consumers import, and adapt those few provider modules to accept the flexible inputs and expose the convenience functions/fields the many consumers actually expect, instead of rewriting every consumer to match a stricter original API. Concrete examples: role-helper functions (`isOwner`, `canToggleTools`, etc.) were changed to accept a flexible `RoleLike` union (string, membership object, or null) instead of a strict `ViewerRole` type, clearing roughly 15 errors from a single change; `lib/api/billing.ts` and `lib/api/members.ts` gained consumer-facing camelCase types and internal-token convenience wrappers around existing token-passing functions. The general leverage principle: in a codebase where a handful of library modules are imported by dozens of consumers, reconciling type mismatches at the library layer is far cheaper than reconciling them at every call site.
REVIEW: high-impact
## Links
- related, 2026-08-21-component-superset-props-reconciles-parallel-designs.md, the equivalent technique applied one layer up, at the component-prop level
