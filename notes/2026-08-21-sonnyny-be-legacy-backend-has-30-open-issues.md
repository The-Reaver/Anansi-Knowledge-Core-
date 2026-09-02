---
id: 2026-08-21-sonnyny-be-legacy-backend-has-30-open-issues
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, sonnyny-be, repo-archival, open-issues]
sources:
  - ref: "Turn 22 states 'sonnyNY-BE (JS, 30 open issues, likely an older backend)' directly in the org map; no individual issue was triaged in this session."
    reliability: medium
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [20, 22]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# ShopOnlineNewYork's superseded sonnyNY-BE backend has 30 open issues, unreviewed, blocking a safe archive
- id: 2026-08-21-sonnyny-be-legacy-backend-has-30-open-issues
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: medium, the issue count came from a metadata pass; individual issue contents were not reviewed in this session
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, sonnyny-be, repo-archival, open-issues

## Body

The superseded JavaScript backend `sonnyNY-BE` in the ShopOnlineNewYork organization (one of roughly 5 duplicate/legacy backend repos, superseded by the canonical `SonnyBackEndRepo`) had 30 open GitHub issues as of 2026-08-01. Before this repo can be safely archived as part of the org's duplicate-repo cleanup, those issues need to be checked for any representing live/unresolved obligations and migrated to the canonical backend repo if so — none of the 30 issues were individually reviewed or triaged in this session, so it is not yet known whether any are still relevant.

## Links
- extends, 2026-08-21-sonny-seven-active-vs-fifteen-dead-repos.md, one of the duplicate repos identified in that breakdown.
