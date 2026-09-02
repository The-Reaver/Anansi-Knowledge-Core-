---
id: 2026-08-21-railway-monorepo-service-needs-explicit-root-directory
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, railway, monorepo, deploy, build-config]
sources:
  - ref: "Archive turns 503-519: the agent instructs setting Root Directory=backend (turn 503), diagnoses a duplicate un-rooted service as the likely 'Config Error' cause (turn 506), and turn 519 confirms 'Build succeeded now (Initialization, Build, Deploy). The readme fix + root directory worked'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [503, 519]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# On a monorepo, each Railway service must have its Root Directory explicitly set to its own subfolder, or the build fails fast (~10 seconds) trying to build the mixed tree
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly observed: setting Root Directory to `backend` (combined with the pyproject readme fix) turned a ~10s build failure into a successful build
- verified: 2026-08-21
## Body
The `project_brief_step0_resolved` repo is a monorepo containing both `backend/` (Python/FastAPI) and `frontend/` (Next.js) in one GitHub repo. When a Railway service was created without explicitly setting its Root Directory, it defaulted to trying to build the repo root, which contains a mixed Python+Node tree Railway's builder cannot resolve, and the build died in roughly 10 seconds at the "Build image" step showing a "Config Error." Setting the backend service's Root Directory to `backend` made Railway correctly read `backend/railway.json` and use its declared build command (`pip install . `) and start command. The diagnostic rule: a fast (~10 second) build failure on a monorepo service almost always means a build-config problem — the wrong root directory, or a manifest file pointing outside the configured build root — rather than an application code bug, and should be checked before digging into logs.
## Links
- related, 2026-08-21-pyproject-readme-path-outside-build-root-breaks-railway-build.md, the second build-config bug found in the same troubleshooting sequence, once Root Directory was already correct
