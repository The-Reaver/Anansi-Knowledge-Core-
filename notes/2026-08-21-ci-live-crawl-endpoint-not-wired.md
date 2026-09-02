---
id: 2026-08-21-ci-live-crawl-endpoint-not-wired
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, crawler, api, go-live, architecture-gap]
sources:
  - ref: "Agent builds shared/snapshot.py and v2/rules/snapshot_pack.py this session, then states the crawl_domain -> snapshot -> rules pipeline isn't yet wired to a point-at-a-domain endpoint"
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (A)\" (backfilled from historical transcript c5583566, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-c5583566.jsonl
  turns: [96, 196]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high — stated directly by the agent after reading the API layer
- verified: 2026-08-21
- REVIEW: high-impact

## Body
As of 2026-07-31, the Compliance Intelligence FastAPI backend's audit endpoint takes pasted HTML as input, not a domain to crawl. Earlier in the same session the agent built `shared/snapshot.py` (a `CrawlSnapshot` builder: domain BFS honoring robots.txt/sitemap, forms, trackers, TLS, security headers) and `v2/rules/snapshot_pack.py` (snapshot-native rules), both green in the test battery — but the two are not yet connected end to end. There is no "point at a clinic's domain, get a cited audit back" endpoint. This was flagged as the second of two honest gaps (alongside the HBOT lexicon coverage gap) between the engine's current state and the operator's "prove it can do what we say" go-live bar, and is listed as go-live step 3 (wire the live crawl) in the sequenced path the agent gave the operator.

## Links
- depends-on, 2026-08-21-ci-hbot-lexicon-coverage-gap.md, both are named the same session as the honest gaps before the engine matches the sales claim
