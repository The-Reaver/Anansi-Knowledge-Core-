---
id: 2026-08-21-railway-chosen-as-hosting-platform-for-stag-platform
type: decision
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, railway, deploy, hosting-decision, architecture]
sources:
  - ref: "Archive turn 239: the agent's grounded deployment roadmap states two Railway services (backend+frontend) in one Railway project, one shared Supabase project, plus Stripe/Twilio/Resend, based on the railway.json files already present in both backend/ and frontend/"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [239, 239]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Railway was the locked hosting decision for stag-platform: backend and frontend as two services in one Railway project, one Supabase project for Postgres+Auth, Stripe/Twilio/Resend for money/SMS/email
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the deploy architecture matches the session's roadmap and the actual live Railway deploy achieved by session end. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the deploy roadmap and every subsequent step this session assumed and acted on this architecture, and the backend was actually deployed live on Railway by the end of the session
- verified: 2026-08-21
## Body
For the `project_brief_step0_resolved` project (the stag-platform repo), the deploy architecture is: two Railway services (backend and frontend) inside one Railway project, both deployed from the same single GitHub repo (`The-Reaver/stag-platform`) with each service's Root Directory pointed at its own subfolder, both pointed at one shared Supabase project for Postgres and Auth, plus Stripe, Twilio, and Resend as the external providers for billing, SMS, and email respectively. This matches the `railway.json` files already present in both `backend/` and `frontend/` (each specifying its own build/start commands and healthcheck), and no alternative host (Render, AWS, etc.) was considered or evaluated this session — Railway was treated as the given, locked choice throughout the deploy walkthrough.
REVIEW: high-impact
## Links
- related, 2026-08-21-railway-never-set-a-manual-port-variable.md, the biggest Railway-specific gotcha hit while executing this deploy
