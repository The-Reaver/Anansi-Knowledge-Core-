---
id: 2026-08-21-type-clean-build-is-not-runtime-correct
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, verification, typescript, testing, false-confidence]
sources:
  - ref: "Archive turn 163: the agent's own caveat after reaching tsc 0 errors and a green build states 'Type-cleanliness != runtime correctness. The lib API paths still don't match the backend routes (e.g. toggles calls /api/tools/slots, backend serves /api/tools/entitlements)'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [163, 163]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A frontend that compiles and builds at zero TypeScript errors can still call the wrong backend paths and expect the wrong response shapes
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the tsc-clean-then-OpenAPI-diff-found-drift sequence matches the session's own narrated order of events. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed: after tsc reached 0 errors and the build succeeded, an OpenAPI diff still found substantial path and response-shape drift against the real backend
- verified: 2026-08-21
## Body
Reaching `npx tsc --noEmit` at zero errors and `npm run build` at exit 0 for a STAG-generated Next.js frontend was necessary but not sufficient evidence that the app actually worked: the type system only verifies internal consistency of the code as written, not that the API paths and payload shapes it targets match what the real backend serves. In this session, after the frontend was fully type-clean and building, a live-integration pass against the backend's own OpenAPI schema found the frontend's `lib/api/*` modules were calling nonexistent or wrong paths (e.g. `/api/tools/slots` instead of `/api/tools/entitlements`) and expecting response shapes the backend didn't return. The general lesson: type-cleanliness proves the code is internally coherent, not that it's correct against an external contract; a separate verification step (an OpenAPI/contract diff, or hitting a live server) is required before treating a green build as evidence the integration works.
REVIEW: high-impact
## Links
- related, 2026-08-21-openapi-diff-is-authoritative-frontend-backend-verification.md, the verification method used to close this gap in the same session
