---
id: 2026-08-27-compliance-intelligence-is-a-separate-product-geo-a-future-thin-consumer
type: decision
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: ci
tags: [compliance-intelligence, architecture, product-scope, geo, compensation]
sources:
  - ref: "GEO Suite session 2026-08-27: operator clarified CI's scope in free text and chose the compensation structure; architecture resolved by direct reasoning. Proposal artifact https://claude.ai/code/artifact/176bf060-a15e-4b9d-8d22-9d61822e4be0"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [4, 5]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# Compliance Intelligence is a separate regulatory-law-tracking product built as its own service, with GEO Suite as a future thin consumer, not its host

## Body
Two decisions were fixed about Compliance Intelligence (CI), both from the operator directly.

**Scope, corrected by the operator.** CI is a **regulatory-law-tracking product** covering
California, EU and US law. It is **not** a legal-docket-ingestion pipeline, which is how the
agent had been reading it -- and which is also the shape the rejected external "Federal
Litigation Tracking" documents assumed. The correction matters beyond CI: several of the external
proposals reviewed in the same session were arguing for an architecture serving a product that
does not exist.

**Architecture.** CI is built as its own **separate service**. The GEO Suite is positioned as a
future **thin consumer** of it, not as its host. This keeps a regulatory-tracking product with
its own compliance surface, own update cadence and own legal-review loop from being coupled to
the GEO Suite's release cycle.

**Compensation structure**, chosen by the operator: *"Monthly team budget + separate founder
fee."* The proposal artifact deliberately leaves the founder-fee number and the equity percentage
**blank** for the operator to fill in -- the agent did not invent figures it had no basis for,
which is the correct handling for a commercial term only the operator can set.

Open: the founder-fee and equity figures remain unfilled.

**Reconciliation with the 2026-08-21 ratified note (operator ruling, 2026-08-27).** The
promotion pass escalated an apparent conflict: `2026-08-21-ci-is-a-three-version-compliance-
suite-not-an-actuarial-engine` describes CI, from its README/VISION, as a three-version
compliance *audit suite* scoring clinics against FDA/FTC/ADA rules, while this note records
the operator describing it as a *regulatory-law-tracking* product. Asked which description is
current, **the operator ruled: regulatory-law-tracking.**

These are not in conflict once ordered correctly. Regulatory-law tracking is what the product
*is* — the thing being built and sold, tracking California/EU/US law as it changes. The
three-version structure and heuristic scoring describe *how the audit engine consumes that
tracked law* to score a site. The 2026-08-21 note remains accurate about the engine's
internals; this note is the senior statement of product identity and scope. Where the two
appear to disagree about what CI fundamentally is, this one governs.

## Links
- reconciles-with: notes/2026-08-21-ci-is-a-three-version-compliance-suite-not-an-actuarial-engine.md
  — see the reconciliation note in the body. Not a supersession: that note's V1/V2/V3
  structure and its "heuristic, not actuarial" scoring stand.
- relates-to: notes/2026-08-21-ada-title-iii-wcag-binding-section-508-benchmark-only.md
- relates-to: 2026-08-27-source-verifies-on-terminology-and-fails-on-numeric-hero-claims
