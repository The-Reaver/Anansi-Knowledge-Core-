---
id: 2026-08-21-ci-physician-funding-brief-published-with-market-rate-estimates
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (added an explicit staleness/expiry caveat: these are aging, non-re-fetchable estimates that must not be treated as current pricing). Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, funding, cost-estimate, presentation, artifact]
sources:
  - ref: "Archive turns 199-204: agent produces and publishes a physician-facing funding brief for Compliance Intelligence with development-value, one-time launch-cost, and ongoing-cost figures, explicitly labeled throughout as planning estimates rather than bids."
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (B)\" (backfilled from historical transcript fc69f93c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-fc69f93c.jsonl
  turns: [199, 204]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: believed-unconfirmed
- confidence: low, all dollar figures are the agent's own market-rate estimate (e.g. ~$130/hr assumption), explicitly disclaimed as not a bid or financial advice, and unverified against any actual vendor quote
- verified: 2026-08-21

# A physician-facing funding brief for Compliance Intelligence was produced with market-rate development-value and ongoing-cost estimates, explicitly labeled as planning estimates rather than bids

## Body
The operator asked for a presentation-ready document to show a team of non-technical physician investors what the Compliance Intelligence project (HBOT marketing compliance, ADA/HIPAA, and AI-assisted design tooling) would cost to fund, walked through at a beginner level: the software development life cycle, the tech stack in plain language, and every cost bucket (development, one-time launch, and ongoing/maintenance). The agent produced a published artifact with these headline figures: development value already built, estimated at $150k-185k (based on ~1,240 hours at a ~$130/hr mid-market US rate — explicitly framed as market value, not money actually spent, since the work was AI-assisted); one-time finish-and-launch cost of ~$16k-30k at agency pricing; ongoing monthly cost under two models, ~$150-400/mo run-lean (recommended starting point) versus ~$2,200-4,200/mo if a dev firm is kept on retainer; and an estimated year-one total of ~$18k-35k to go live and run lean. The agent flagged that a one-time healthcare-attorney review of the finding templates before they reach a paying clinic should be budgeted as a real cost outside of software. All figures were explicitly labeled as planning estimates, not quotes, with a recommendation to get written quotes before relying on them.

Brain Trust revision: these figures are 2026-07-31 planning estimates, now nearly a month old at time of review, and the published claude.ai artifact they live in is not a durable, independently re-fetchable source (no re-derivation trail if pricing assumptions change). They must be treated as stale and must not be relied on as current pricing without re-deriving them against present-day rates and, ideally, an actual vendor quote, before use in any real funding conversation.

## Links
- extends, 2026-08-21-ci-deploy-cost-rough-estimate.md, the same session's separate ongoing-hosting cost estimate that this funding brief's monthly figures build on
