---
id: 2026-08-21-strip-required-signal-test-pattern-proves-scoring-engine-reads-input
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, geo-platform, audit-engine, testing, anti-stub, methodology]
sources:
  - ref: "Turns 62-65 show the test suite being written and run (all 7 pass) right after the fail-fixture result, and turn 86's final report explicitly labels it 'Anti-stub proof (test 5): stripping the JSON-LD drops category 1's score — the engine reads its input', matching the note's description exactly."
    reliability: high
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [62, 86]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, described directly in the agent's own final report as test 5 of the new suite
- verified: 2026-08-21
- REVIEW: high-impact

# Stripping a required signal from a passing fixture and asserting the corresponding score drops is a concrete way to prove a scoring engine isn't a stub

## Body
While rebuilding the GEO audit engine to replace a stub that had previously scored every input 95 regardless of content (the BG1 finding), the agent added a specific regression test built for exactly that failure mode: take the known-passing fixture site, strip out its JSON-LD structured data, re-run the audit, and assert that category 1's score drops. A hardcoded or input-blind scorer would produce the same score either way; this test only passes if the code actually reads the artifact and branches on what it finds. The general pattern is reusable beyond this one engine: for any scoring or gating function, a "does it even look" test — remove one thing the rubric claims to require, then assert the score responds — is a lightweight, concrete defense against the exact class of failure (an always-pass gate) that this project had already been burned by once.

## Links
- extends, 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub.md, the build where this test was written.
- related-to, 2026-07-22-bg1-fake-audit-stub-quarantined.md, the earlier always-pass stub failure this test pattern is a direct defense against.
