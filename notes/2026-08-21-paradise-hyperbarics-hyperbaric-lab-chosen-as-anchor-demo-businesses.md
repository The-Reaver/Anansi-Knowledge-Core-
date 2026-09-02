---
id: 2026-08-21-paradise-hyperbarics-hyperbaric-lab-chosen-as-anchor-demo-businesses
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (the stale '90-point gate' figure was corrected to the live 93-point PUBLISH_THRESHOLD per `projects/geo_platform/backend/app/core/rubric.py:75` and the operator's 2026-08-08 ruling; the underlying decision — the two businesses and their 14/100 and 29/100 scores — was never in question). Operator retains veto per Mandate 1."
project: fleet
tags: [geo, demo, hbot, sales, decision]
sources:
  - ref: "Turns 176-180: turn 176 is the operator naming both businesses by name and URL, turn 180 is the agent's reported scores (14/100, 29/100) and gate/schema findings from running the real audit engine against both sites."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [176, 180]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The operator picked Paradise Hyperbarics and Hyperbaric Lab as the two real, named businesses the GEO Suite demo walks through — both scored live by the real audit engine (14/100 and 29/100) before any credentials were wired up
- id: 2026-08-21-paradise-hyperbarics-hyperbaric-lab-chosen-as-anchor-demo-businesses
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — operator named both businesses explicitly by name and URL; scores are the agent's own reported output of running the real audit engine against them, same session
- verified: 2026-08-21
- tags: geo, demo, hbot, sales, decision
- REVIEW: high-impact

## Body
The operator named the two real businesses for the GEO Suite sales demo to walk through: Paradise Hyperbarics (https://www.paradisehyperbarics.com/) and Hyperbaric Lab (https://hyperbariclab.com/). The prior readiness queue had specified one business per live vertical (one HBOT, one chiropractor); the operator instead chose two HBOT businesses, which the agent flagged as a deviation but treated as an intentional operator call rather than something to correct. Because the audit-scoring code path needs zero credentials (see the related zero-cost-demo-path finding), the agent ran the real audit engine against both sites immediately, before Supabase was even wired to the frontend: Paradise Hyperbarics scored 14/100 and Hyperbaric Lab scored 29/100, both far below the platform's 93-point publish gate (raised from 90 by direct operator ruling, 2026-08-08 — see `2026-08-08-operator-ruling-2026-08-08-geo-publish-gate-rises-to-93-rank.md`), both missing LocalBusiness/Organization schema. These two real, low, verifiable scores were then wired into the demo's fallback/sample data (replacing placeholder businesses) so the Nova UI shows real, grounded numbers for the operator's actual picks even before live Supabase auth was working end to end.

## Links
- relates, 2026-08-21-geo-demo-proof-path-needs-zero-new-paid-services.md, the finding that made scoring these two businesses possible before any paid service was wired up.
- relates, 2026-08-16-38-real-hbot-businesses-live-scored-zero-clear-the-gate.md, the later, larger 38-business market-research run these two businesses were the seed/proof-of-concept for.
- relates, 2026-08-16-gate-90-vs-93-staleness-in-session-materials-and-live-ui.md, the sibling note documenting this exact code-correct/prose-stale 90-vs-93 pattern, caught and fixed once already before this note repeated it.
