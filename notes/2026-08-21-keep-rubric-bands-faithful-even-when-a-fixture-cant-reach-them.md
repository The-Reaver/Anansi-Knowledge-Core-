---
id: 2026-08-21-keep-rubric-bands-faithful-even-when-a-fixture-cant-reach-them
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, geo-platform, audit-engine, rubric, scoring-integrity, decision]
sources:
  - ref: "Turns 44-46 show the pass-fixture run scoring 99 with the internal-link-density band (0.15-0.20 links/word) called out as unreachable for a small page, and turn 86's final report uses the exact phrase 'would have been the stub's sin in miniature' the note quotes."
    reliability: high
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [44, 86]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, the agent states the reasoning and the resulting score explicitly in its own final report
- verified: 2026-08-21
- REVIEW: high-impact

# When a fixture can't reach a rubric sub-check's target band, the right move is to document the gap, not widen the band to force a pass

## Body
While tuning the "pass" fixture for the rebuilt GEO audit engine, the agent found that one sub-check (internal-link density, worth 1 of category 2's 20 points) targets an academic band of 0.15-0.20 links per word — a density that a small, honestly hand-built single page cannot realistically reach without stuffing in dozens of links. Rather than loosen the band so the fixture would score a clean 100, the agent kept the check as specified, added one genuine in-content link for realism, accepted the fixture landing at 99 instead of 100, and documented the one-point shortfall plainly in the build report. The agent's own framing of why this matters: forcing that one point by loosening the rubric "would have been the stub's sin in miniature" — the same class of dishonesty (making a check pass regardless of the real input) that the entire days 3-5 rebuild existed to eliminate. This is a general principle for anyone tuning fixtures against a scoring rubric: a fixture that can't cleanly clear every band is better left short than the rubric being quietly loosened to fit the fixture.

## Links
- extends, 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub.md, the build where this call was made.
- related-to, 2026-08-21-geo-audit-engine-honest-denominator-policy.md, the same session's parallel scoring-integrity rule about not fudging what can't be measured.
