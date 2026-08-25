---
id: 2026-08-06-ci-client-facing-gate-three-conditions
type: ruling
status: ratified
source: Cowork session, 2026-08-06; operator Abad overrode the "attorney terms before any code" gate and directed the slice-by-slice build of the lawyer-facing CI tool to start now (source status: active); mined from candidates/2026-08-25/2026-08-06-ci-lawyer-tool-build-roadmap-and-gate-override.md
project: ci
tags: [ci, client-facing-gate, attorney-terms, professional-conduct, red-then-green]
---

# The CI tool's client-facing gate stays locked behind three conditions even though the internal build gate was overridden

## Body

Nothing the tool produces reaches the partner attorney as working product, and nothing reaches any of his clients, until all three are true: (1) condition 1 — written attorney terms, drafted in reports/CI_ATTORNEY_PARTNERSHIP_TERMS_DRAFT_2026-08-06.md, finalized by outside counsel and signed; (2) condition 5 — a professional-conduct read by an outside lawyer who is not the partner attorney; (3) the Layer 2 red-then-green correction-integrity proof is green.

## Links

- relates: 2026-08-06-ci-gate-override-internal-build-starts-now
