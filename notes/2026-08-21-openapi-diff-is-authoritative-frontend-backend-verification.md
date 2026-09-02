---
id: 2026-08-21-openapi-diff-is-authoritative-frontend-backend-verification
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, openapi, fastapi, verification, frontend-backend-contract]
sources:
  - ref: "Archive turns 221-232: the agent regex-matches all 23 frontend data-plane calls against the 42 real OpenAPI paths ('All 23 paths resolve ... ALL_MATCH'), finds a response-shape mismatch ({ok,message} vs {id,status}), and delivers the full path/shape reconciliation table naming the wrong-path examples"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [221, 232]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Booting the FastAPI app and diffing its own generated OpenAPI schema against every frontend fetch call is the authoritative way to verify a frontend API client against a real backend
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the 42/23 path counts and named mismatch examples match the session's verification pass. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent applied this method, verified all 23 frontend data-plane calls resolved against the 42 real OpenAPI paths, and it surfaced substantial real path/shape drift that a type-check alone had missed
- verified: 2026-08-21
## Body
After the STAG-generated frontend reached zero TypeScript errors and a green build, the operator asked for the API paths and response shapes to actually be verified against the running backend rather than trusted. The method used was to boot the backend app and call `app.openapi()` to get its own authoritative route table (42 paths) and component schemas, then regex-match every frontend `method + path` call (23 data-plane calls) against that real route set, and compare each request/response shape field-by-field against the OpenAPI component schemas. This surfaced substantial drift the type-checker could not see, because the frontend had been written against an imagined API: wrong paths (`GET /api/tools/slots` instead of `GET /api/tools/entitlements`; `/billing/subscription` instead of `/billing/subscriptions/{client_id}`; `/api/members/*` instead of `/accounts/me/members`; `/admin/me` which doesn't exist at all), and wrong response shapes (an admin action result typed as `{ok, message}` when the backend actually returns `{id, status}`). Because live Supabase/Stripe/Twilio credentials and a running database were not available in this environment, this OpenAPI-diff method was explicitly used as the strongest verification achievable short of hitting a fully live server.
REVIEW: high-impact
## Links
- related, 2026-08-21-type-clean-build-is-not-runtime-correct.md, the reason this extra verification step was necessary beyond a green tsc/build
