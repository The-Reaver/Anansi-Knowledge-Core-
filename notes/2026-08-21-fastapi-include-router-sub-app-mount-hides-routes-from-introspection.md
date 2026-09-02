---
id: 2026-08-21-fastapi-include-router-sub-app-mount-hides-routes-from-introspection
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, fastapi, starlette, testing, backend, route-introspection, project-brief-step0]
sources:
  - ref: "Archive turns 74-85 (2026-07-15T16:49-16:52): turn 74 finds only 3 default routes after include_router; turn 81 spots the pinned fastapi/starlette versions and the pytest-200-vs-empty-app.routes contradiction; turn 83 diagnoses the sub-app Mount as cause; turn 85 confirms 200 via TestClient against the real app.main.app."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [74, 85]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, directly reproduced and cross-checked with TestClient in the same session
- verified: 2026-08-21

# In this backend's pinned FastAPI/starlette versions, include_router mounts as a sub-app, so app.routes[].path never lists the router's child routes

## Body
In the `project_brief_step0_resolved` backend's installed dependency versions (fastapi 0.139.0, starlette 1.3.1), `FastAPI.include_router()` mounts the router as a sub-application (a `Mount`) rather than copying its child routes onto the parent app's top-level route list. The practical effect: iterating `app.routes` and reading each entry's `.path` will NOT show the routes registered by an included router -- only default paths like `/openapi.json` and an unlabeled `None` mount entry appear, even when the router's routes are fully live and functional. During this session this looked exactly like "the router failed to mount" (only 3 routes visible after including 4+ routers with unconditional, non-swallowed imports), which cost real debugging time chasing what appeared to be an import or mounting bug. The routes were correctly registered the entire time; the enumeration method used to check was simply wrong for this dependency combination. This was confirmed by hitting the same route through `TestClient`, both against the router in isolation and through the real production `app.main.app` assembly -- both returned correct 200 responses with the right response body, even while `app.routes` enumeration showed nothing for that path.

Rule for this codebase: never trust `app.routes[].path` to confirm whether a router registered. Always verify a route exists by making an actual request through `TestClient` against the real app assembly.
