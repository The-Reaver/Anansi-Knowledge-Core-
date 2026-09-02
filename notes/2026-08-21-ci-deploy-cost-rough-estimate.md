---
id: 2026-08-21-ci-deploy-cost-rough-estimate
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, cost, deploy, railway, go-live, estimate]
sources:
  - ref: "Operator's cost-analysis request and the agent's resulting cost table/breakdown for moving Compliance Intelligence to a real database and going live"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [189, 196]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: believed-unconfirmed
- confidence: low — the agent's own back-of-envelope figures from general platform pricing knowledge, not a live quote from Railway/Supabase/OpenAI pricing pages, and not independently verified in this backfill
- verified: 2026-08-21

## Body
When the operator asked for a cost analysis to move CI to a real database and go live, the agent gave a rough monthly estimate (not a live-fetched quote): backend host (Railway) $5-20, frontend host $0-5, managed Postgres $5-25 (Railway PG ~$5-10 or Supabase Pro $25), optional LLM remediation drafting (GPT-4.1-mini) ~$0-20 (roughly $0.02-0.05/audit, engine works fully without it since findings are deterministic and the LLM only drafts remediation prose), domain+TLS ~$1/mo — totaling roughly $25-60/mo at testing scale, and $50-150/mo estimated at small-production scale (multiple consultants, dozens of audits/day). The agent flagged that the dominant future cost driver isn't infra or the LLM but a headless-browser (Playwright) render service, needed only if many prospect clinic sites turn out to be JavaScript-rendered SPAs the stdlib crawler can't read — and flagged this as an open decision (JS-rendering on day one vs. fast-follow) rather than something already decided. This session ended before the operator's follow-up request (a fully walked-through, non-technical cost/SDLC presentation for a team of doctors funding the build) was produced — treat this note as the raw estimate that presentation would need to be built from and verified against, not as a finalized figure.

## Links
- feeds, 2026-08-21-ci-json-store-blocks-go-live.md, the Postgres line item in this estimate is the fix for that gap
