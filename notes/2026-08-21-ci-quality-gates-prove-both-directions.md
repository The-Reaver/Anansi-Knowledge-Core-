---
id: 2026-08-21-ci-quality-gates-prove-both-directions
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [compliance-intelligence, testing, verify-py, test-convention]
sources:
  - ref: "Archive turns 69-96: agent writes tests/test_quality_gates.py implementing Compliance Intelligence's five non-negotiable-law gates (cite-or-omit, framing, evidence-class integrity, 0.70 confidence floor, crawl determinism), each split into a real-engine-compliance check and a planted-violation-detection check; verify.py battery goes from 15/15 to 18/18 green."
    reliability: high
    origin: "STAG session, 2026-07-31, \"Compliance Intelligence audit engine (B)\" (backfilled from historical transcript fc69f93c, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-31-backfill-fc69f93c.jsonl
  turns: [69, 96]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---
- class: confirmed
- confidence: high, agent wrote and ran these gates and reported 10/10 passing in the same turn
- verified: 2026-08-21

# Compliance Intelligence's five non-negotiable-law gates each prove two things: the real engine obeys the law, and a planted violation is actually caught

## Body
The CI build spec required five standalone tests in projects/compliance_intelligence/verify.py proving the engine's non-negotiable laws: cite-or-omit (no client-facing finding without crawl evidence and a resolvable citation), framing (no legal-verdict language like "violates"), evidence-class integrity (never faking DOC-REQUESTED or ON-SITE evidence), the 0.70 confidence floor, and crawl determinism (same snapshot yields identical findings). The agent implemented these as tests/test_quality_gates.py, and structured each of the five as two checks rather than one: first that the real V1/V2 rule engines actually comply with the law on real input, and second that a deliberately planted violation of that law is caught and rejected by the gate. This landed as 10/10 individual assertions (5 laws x 2 directions each) passing on first run, wired into the verify.py battery which went from 15/15 baseline to 18/18 green across this session's four build slices (KB coverage, CrawlSnapshot, quality gates, snapshot-native rules). The two-direction pattern (compliance to the real engine and detection of a planted defect) is the convention this project's test suite now expects for any new non-negotiable-law gate.
