---
id: 2026-08-21-geo-audit-engine-honest-denominator-policy
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, geo-platform, audit-engine, rubric, scoring-integrity, decision]
sources:
  - ref: "Turns 1 and 24 show the operator's verbatim denominator-exclusion instruction ('anything you cannot measure is excluded from the denominator, never assumed') and the agent's own confirmation that points_available equals 90 with cwv supplied / 75 without, matching the note's figures exactly."
    reliability: high
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [1, 24]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, the operator specified the rule directly and the agent's own test suite asserts the resulting numbers
- verified: 2026-08-21
- REVIEW: high-impact

# The GEO audit engine excludes unmeasurable rubric categories from both the numerator and the denominator, never assumes a pass or averages around a gap

## Body
When the operator commissioned the GEO days 3-5 audit-engine rebuild, the instruction was explicit: "anything you cannot measure is excluded from the denominator, never assumed." The rebuilt engine implements this as a hard rule rather than a best-effort guideline. The seven rubric categories are: category 7 is always excluded (not_measured, contributing to neither numerator nor denominator regardless of input), and category 5 (Core Web Vitals) is excluded unless a `cwv` argument is actually supplied to `run_audit`. Categories 1, 2, 3, 4, and 6 are always measured. The practical effect, confirmed by an assertion in the new test suite: `points_available` equals 90 when CWV data is supplied and 75 when it is not — the denominator itself shrinks honestly rather than the missing category being scored as a pass, a fail, or an average. This is the scoring-integrity backbone that keeps a partial-data audit from silently inflating or deflating a client's score, and it is the structural opposite of the quarantined stub's behavior (hardcoding a 95 regardless of what, if anything, was actually measured).

## Links
- extends, 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub.md, the build event that implemented this scoring rule.
