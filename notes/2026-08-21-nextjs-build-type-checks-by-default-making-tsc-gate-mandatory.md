---
id: 2026-08-21-nextjs-build-type-checks-by-default-making-tsc-gate-mandatory
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, nextjs, typescript, build, ci-gate]
sources:
  - ref: "Archive turns 142-145: the agent runs tsc to zero errors and only then runs the production build ('Zero TypeScript errors. Let me confirm cleanly and then run the build'), and turn 145 confirms 'TypeScript compiles and the whole webpack/type-check pass succeeds' as part of the build itself"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [142, 145]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `next build` type-checks the whole project by default, so any TypeScript error blocks the production build, not just a lint warning
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed: `npm run build` only succeeded once `npx tsc --noEmit` reached zero errors, and this ordering was treated as a hard prerequisite throughout the session
- verified: 2026-08-21
## Body
`next build` type-checks the entire Next.js project as part of the production build by default, meaning any outstanding TypeScript error (not just a runtime bug) is enough to fail `npm run build` and block deployment. This is why, throughout this session's frontend rewiring, `npx tsc --noEmit` reaching zero errors was treated as a strict prerequisite gate that had to be cleared before even attempting the production build, and it is the reason a `tsc --noEmit == 0` check belongs in an automated validator as the direct analog of a backend's import/boot check — for a Next.js frontend specifically, a passing type-check is not just good practice but a literal build requirement.
## Links
- related, 2026-08-21-three-validator-checks-added-env-parity-tsc-gate-db-integrity.md, the validator check added this session that encodes this requirement
