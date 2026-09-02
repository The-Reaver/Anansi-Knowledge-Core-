---
id: 2026-08-21-geo-demo-proof-path-needs-zero-new-paid-services
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (the auth-gate function name was updated from the stale `require_owner` to the current `require_sales_agent`, per the 2026-08-16 code change for the sales-agent master panel). Operator retains veto per Mandate 1."
project: fleet
tags: [geo, cost, demo, supabase, stripe, twilio, sequencing]
sources:
  - ref: "Turns 158-175: turn 158 is the operator's question on whether building the demo first and wiring paid services later hurts the process, turn 175 is the traced-code answer (no Stripe/Twilio calls in the audit path, stateless JWT auth gate, Supabase free tier sufficient)."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [158, 175]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# GEO Suite's live-audit "prove it works" demo moment needs zero new paid services — Stripe and Twilio are never called in that code path, and Supabase's free tier covers the rest
- id: 2026-08-21-geo-demo-proof-path-needs-zero-new-paid-services
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — traced the actual call path (`/sales/audit-current`, `require_sales_agent`) rather than reasoning from docs; direct code read
- verified: 2026-08-21
- tags: geo, cost, demo, supabase, stripe, twilio, sequencing
- REVIEW: high-impact

## Body
The operator asked whether building the demo first and wiring paid services (Supabase/Stripe/Twilio) later — deferring the money his business partner would put in until after showing a working demo — would hurt the process. Tracing the actual code, not the docs: `/sales/audit-current` (the live AI-search-readiness audit against a real business URL) does a live HTTP fetch and scores it in-process, with zero database writes — pure compute. `require_sales_agent` (the auth gate in front of it, updated 2026-08-16 from the narrower `require_owner` to support the sales-agent master panel — a superset of owner, not a different actor) only verifies a Supabase JWT signature against Supabase's public JWKS endpoint and checks a role claim — no database row lookup at all. Stripe (billing) and Twilio (post-sale SMS/voice) are never called anywhere in this path; they belong to entirely different parts of the app. The only real requirement to make the "Audit" button work live in front of an investor/partner is a Supabase project with Auth turned on and one owner/sales-agent account created — and Supabase's free tier costs $0 (it pauses after 7 days of inactivity, which is manageable by logging in periodically before demo day). So the sequencing the operator proposed (build and prove first, pay for the rest after) does not hurt the process — the demo's actual proof moment was already free.

## Links
- relates, 2026-08-21-paradise-hyperbarics-hyperbaric-lab-chosen-as-anchor-demo-businesses.md, the two real businesses this zero-cost audit path was proven against.
