---
id: 2026-08-21-testclient-context-manager-exercises-full-lifespan-locally
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [stag, fastapi, testclient, lifespan, local-verification]
sources:
  - ref: "Archive turns 543-545: 'let me actually exercise the startup path locally ... Using a TestClient runs the full lifespan and hits /health' (turn 543), and turn 545 reports 'The critical fix works — STARTUP OK. /health status: 200'"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [543, 545]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Entering FastAPI's TestClient as a context manager runs the app's full lifespan startup, letting a startup crash be reproduced and fixed locally before deploying
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — used directly to verify the lifespan fix: printed "STARTUP OK. /health status: 200" locally, matching what Railway's healthcheck needed
- verified: 2026-08-21
## Body
To verify that a FastAPI app actually completes its startup sequence — not just that it imports — the agent used `with fastapi.testclient.TestClient(app) as client:` (the context-manager form specifically), which runs the app's full ASGI lifespan (startup and shutdown) the same way a real server process would, then made a request to `/health` inside that block. This exactly reproduced the startup path a platform healthcheck (like Railway's) exercises, and confirmed both that the job-poller startup crash was fixed and that the asyncpg pool could actually connect to the live Supabase database, all without needing a deployed environment. General lesson: for any ASGI framework with a lifespan/startup hook, use the test client's context-manager entry point (not a bare instantiation) to catch startup-only bugs before they reach a real deploy.
## Links
- related, 2026-08-21-import-boot-check-misses-runtime-lifespan-startup-crashes.md, the gap in the existing boot check that this technique closes
