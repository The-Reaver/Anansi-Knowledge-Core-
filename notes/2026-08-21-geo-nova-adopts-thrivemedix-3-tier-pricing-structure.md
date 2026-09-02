---
id: 2026-08-21-geo-nova-adopts-thrivemedix-3-tier-pricing-structure
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, nova, pricing, decision, sales]
sources:
  - ref: "Turns 90-157: turn 90 shows the $6,900 placeholder and one-per-vertical business queue, turn 101 identifies the ThriveMedix sheet's real tier structure, turn 111 is the agent's unanswered feature-copy question, turn 113 is the agent proceeding on the safer default after no response, turn 157 confirms the 3-tier grid live on /nova replacing the placeholder."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [90, 157]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# GEO Suite's Nova demo replaced its single $6,900 placeholder price with a 3-tier structure ($500/$2,500/$4,500 per month) taken from the operator's ThriveMedix reference sheet, keeping the real price points but rewriting the feature copy to match what GEO Suite actually does
- id: 2026-08-21-geo-nova-adopts-thrivemedix-3-tier-pricing-structure
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — implemented, tested (67/67), and verified live on the deployed Nova UI this session
- verified: 2026-08-21
- tags: geo, nova, pricing, decision, sales
- REVIEW: high-impact

## Body
The operator supplied a screenshot (`Pricing.md`) that turned out to be a ThriveMedix service-package pricing sheet, not a single number: Starter $500/mo, Full-Service Growth $2,500/mo ("most popular"), Growth+Social $4,500/mo. The Nova demo's `/sales/report` endpoint at the time only supported one flat `price` param, rendered as a single $6,900 placeholder. Before writing tier content into the live demo, the agent flagged that the sheet's feature bullets (ADA/WCAG compliance, YouTube/Instagram/Facebook management) described ThriveMedix's own product, not GEO Suite's (AI-search readiness audits, site generation, GEO monitoring), and asked whether to keep those price points with GEO-accurate feature copy. The operator did not respond to that specific follow-up question before the agent proceeded — so the agent took the safer default itself: kept the three real ThriveMedix price points and tier names, but wrote GEO-Suite-accurate feature bullets under each tier, and flagged it explicitly for the operator to override. This is now live at the Nova `/nova` route, replacing the old single-price strip with a 3-column pricing grid. Because the feature-bullet content was an agent default rather than an operator-confirmed choice, it is worth a deliberate operator review before demo day, distinct from the price points themselves (which came directly from the operator's source document).

## Links
- relates, 2026-08-16-starter-tier-sales-priority.md, the operator's later sales-strategy directive to prioritize selling this same $500/mo Starter tier specifically.
