---
id: 2026-08-21-geo-d3-audit-engine-real-implementation-replaces-always-95-stub
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision (the fail-fixture and near-blank-page scores had already drifted from their archived values by the time of the 2026-08-21 AI review, and the review noted they were stated as present-tense standing facts with no date qualifier; the Body now marks these figures as a dated 2026-07-22 build-day snapshot rather than a current fact). Operator retains veto per Mandate 1."
project: fleet
tags: [geo, geo-platform, audit-engine, stub, anti-gravity, quarantine, testing]
sources:
  - ref: "Turns 26-86 (rubric.py/audit_engine.py writes, pass-fixture run scoring 99, fail-fixture run scoring 87 with all five defects in fix_list, 15/15 full suite, and the final report at turn 86 restating these figures) support every specific claim in the note, including the hedge that only 3 of 5 injected defects are individually named in the narration (robots.txt block, footer phone mismatch, broken internal link — confirmed at turns 53-56)."
    reliability: high
    origin: "STAG session, 2026-07-22, \"GEO days 3-5 audit engine\" (backfilled from historical transcript d4e8f900, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-22-backfill-d4e8f900.jsonl
  turns: [26, 86]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: high, the agent's own final report gives concrete before/after scores and a passing 15/15 test run
- verified: 2026-08-21
- REVIEW: high-impact

# The GEO days 3-5 build replaced the always-95 audit stub with a real engine that reads artifacts and branches on them

## Body
On 2026-07-22, following spec `specs/SPEC_GEO_D3_audit_engine.md`, an agent rebuilt the GEO platform's AI-Search Readiness audit engine (`projects/geo_platform/backend/app/services/audit_engine.py`) to replace the quarantined stub that had hardcoded a score of 95 and inspected nothing (the defect recorded separately as the BG1 finding). The new `run_audit(site_dir, *, cwv=None)` function parses real HTML/JSON-LD/robots.txt artifacts with a stdlib DOM parser and scores across seven weighted categories defined in a new `rubric.py`.

Verification evidence from this build, as of the 2026-07-22 build session: a hand-built "pass" fixture site scored 99 (normalized) and was marked AI-Optimized; a "fail" fixture with five deliberately injected defects (confirmed by name in the source transcript: a blocked crawler in robots.txt, a phone-number mismatch between page and footer, and a broken internal link; the remaining two defects are not individually named in the archived transcript) scored 87 as of 2026-07-22, was marked not-passed, and named all five defects in its fix_list; and a near-blank page scored 26 as of 2026-07-22 and was blocked — where the old stub would have scored it 95 regardless of input. **These specific score figures are a point-in-time snapshot of the 2026-07-22 build day, not a standing fact:** a 2026-08-21 re-check already found the fail-fixture score had moved to 85 (a 2-point drift from the archived 87 attributed to later rubric tuning), and the number should be expected to keep moving as the rubric is further tuned. Treat the pass/fail/blocked outcome shape (a real, input-sensitive scoring spread rather than a flat 95) as the durable claim; re-verify the exact numbers against the live fixtures before citing them.

The full regression suite (8 pre-existing tests plus 7 new ones) passed at 15/15, and the FastAPI app still imported cleanly with the audit route intentionally left returning HTTP 501 pending the by-site-id facts-repository wiring (a separate, already-tracked gap). The sibling `site_engine` component was deliberately left quarantined, as it was explicitly scoped to a later days-6-8 build.

## Links
- corrects, 2026-07-22-bg1-fake-audit-stub-quarantined.md, replacing the always-pass audit stub this finding describes with a real implementation that branches on its input.
- related-to, 2026-07-24-geo-site-engine-real-implementation-quarantine-lifted.md, the parallel days-6-8 rebuild of the sibling site_engine component that this session's agent deliberately left untouched.
