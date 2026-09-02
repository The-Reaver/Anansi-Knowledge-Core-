---
id: 2026-08-21-sonny-seven-active-vs-fifteen-dead-repos
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, repo-sprawl, org-structure, technical-debt]
sources:
  - ref: "Turn 22's org map names the same 7 active repos, the same ~15-repo split into Flutter/backend/frontend clusters, and the same named junk repos (deleteThisRepo, an empty contributor-named repo, an empty Rust fork) that this note states."
    reliability: high
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

# Of ShopOnlineNewYork's 22 repos, only 7 were active and the rest were duplicate or dead
- id: 2026-08-21-sonny-seven-active-vs-fifteen-dead-repos
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, based on a direct GitHub metadata pass across all 22 repos (push dates, sizes, languages)
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, repo-sprawl, org-structure, technical-debt

## Body

As of 2026-08-01, of the 22 repositories in the ShopOnlineNewYork GitHub organization, only 7 were actively maintained (pushed within roughly the prior two weeks): `SonnyNY` (React storefront web app), `sonny-admin-dashboard` (Next.js/TypeScript admin UI), `SonnyBackEndRepo` (main Java/Spring backend), `CJ-dropshipping` (Java dropship-integration service), `sonny-app-flutter-2.0` (current Flutter mobile app), `Sonny-Python` (data-mining/automation utilities), and `devops` (Terraform/Ansible infrastructure). The remaining roughly 15 repos were duplicate, superseded, or abandoned, falling into three clusters: about 5 Flutter mobile repos (`Sonny-App-Flutter`, `Sunny-Flutter-App-CompleteCode`, `sonnyNY-Flutter`, `SonnyNY-flutter-frontend`, all superseded by `sonny-app-flutter-2.0`), about 5 backend repos (`SonnyNY-JavaBackend`, `AdminManagement-API`, `Shop_Online_NewYork_Project`, `sonnyNY-BE`, all superseded by `SonnyBackEndRepo`), and about 3 web-frontend repos (older than `SonnyNY`), plus outright junk (an empty repo named after an individual contributor, an empty Rust experiment fork, and a repo literally named `deleteThisRepo` that was never deleted). The organization had no clear single source of truth per stack — that ambiguity was flagged as the single biggest structural problem in the org, ahead of any individual code issue.

REVIEW: high-impact

## Links
- extends, 2026-08-21-sonny-org-is-shoponlinenewyork-22-repos.md, the org-level discovery this breakdown refines.
