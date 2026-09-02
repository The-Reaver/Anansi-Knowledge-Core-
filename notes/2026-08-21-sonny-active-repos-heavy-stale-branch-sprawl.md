---
id: 2026-08-21-sonny-active-repos-heavy-stale-branch-sprawl
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted with revision, provenance turns range extended to include turn 46 (source of the devops/flutter branch counts). Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, git-branches, technical-debt]
sources:
  - ref: "Turn 44 (the live diagnostic reply) states the SonnyNY (81) and SonnyBackEndRepo (78) branch counts directly; the devops (63) and sonny-app-flutter-2.0 (25) counts are confirmed only in turn 46, the assistant's own later note-extraction/synthesis pass over the same transcript. Citation range corrected on Brain Trust review to include turn 46 as the source of those two counts."
    reliability: medium
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [44, 46]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# ShopOnlineNewYork's active repos each carry dozens of branches, presumed mostly stale
- id: 2026-08-21-sonny-active-repos-heavy-stale-branch-sprawl
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: medium, branch counts were confirmed via GitHub metadata; which branches are actually safe to delete was not individually verified
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, git-branches, technical-debt

## Body

As counted during the 2026-08-01 Phase 1 metadata pass, the active ShopOnlineNewYork repos carried large numbers of branches: `SonnyNY` had 81, `SonnyBackEndRepo` had 78, `devops` had 63, and `sonny-app-flutter-2.0` had 25. The agent presumed most of these were merged or abandoned and flagged the org as needing a branch-cleanup policy, but did not individually verify merge status or safety of deletion for any specific branch in this session — the counts are confirmed, the "mostly stale" characterization is an inference.

## Links
- extends, 2026-08-21-sonny-seven-active-vs-fifteen-dead-repos.md, additional health detail on the same active-repo set.
