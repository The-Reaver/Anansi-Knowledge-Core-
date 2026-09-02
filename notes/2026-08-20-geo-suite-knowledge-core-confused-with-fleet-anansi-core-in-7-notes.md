---
id: 2026-08-20-geo-suite-knowledge-core-confused-with-fleet-anansi-core-in-7-notes
type: finding
status: ratified
ratified: "2026-08-20 — anansi-promote skill run, 9/10 on the promotion rubric (novelty 2, evidence 2, actionability 2, generality 1, non-contradiction 2). Independently verified against the live projects/geo_platform/knowledge_core/ directory and commit history this session. Written with real ADR-0005 schema and a genuine provenance citation (this session's own archived transcript), rather than the legacy flat schema used for the rest of this session's promotions, per this same batch's own self-critique note. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, anansi, knowledge-core]
sources:
  - ref: "This session's own review, verification, and gate-closure work, 2026-08-20"
    reliability: high
    origin: "direct observation and verification, this session"
provenance:
  archive: research/knowledge-home/raw/2026-08-20-anansi-candidate-promotion-and-gate-closure-session.jsonl
  turns: [1, 20]
links:
  - "2026-08-20-reject-recommended-for-geo-kc-confusion-cluster-pending-operator"
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Seven candidate notes describing a Knowledge Core build roadmap were found to confuse the GEO Suite product's own, already-substantially-built Knowledge Core with the separate, fleet-wide Anansi Core

## Body

Seven candidate notes in the 2026-08-20 batch, all describing a proposed roadmap of build batches for a "Knowledge Core," were found on verification to be confusing two separate systems that happen to share a name. The notes treat the roadmap as describing an unbuilt future system for the fleet-wide Anansi Knowledge Core, but the roadmap document they actually cite targets a different, already-substantially-built system: the GEO Suite product's own internal Knowledge Core, located under the GEO platform's own project directory, which already had 55 Python files and 7 real commits spanning 2026-08-02 through 2026-08-15 at the time of this review, including two bugs found in its already-built code that had already been separately ratified into the fleet's own Anansi Core. This is a real, consequential confusion between the two systems, not a minor wording issue.

## Links
- relates, 2026-08-20-reject-recommended-for-geo-kc-confusion-cluster-pending-operator
