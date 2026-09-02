---
id: 2026-08-21-sonny-org-is-shoponlinenewyork-22-repos
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, github, org-structure, repo-discovery]
sources:
  - ref: "Turns 5, 9, 12, 20, and 22: turn 5 rules out the Desktop\\SONNY Obsidian vault as a false lead, turn 12 confirms no SONNY code under the operator's primary GitHub account, turn 20 reaches 22 repos once more org URLs are supplied, and turn 22 confirms the ShopOnlineNewYork organization and its stack mix."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [5, 22]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# "SONNY" is not one repo — it is the 22-repo ShopOnlineNewYork GitHub organization
- id: 2026-08-21-sonny-org-is-shoponlinenewyork-22-repos
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, agent directly enumerated the org via GitHub and reported concrete counts to the operator
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, github, org-structure, repo-discovery

## Body

When the operator asked for an assessment of "my SONNY repo," the codebase did not exist as a single repository anywhere obvious. A `Desktop\SONNY` folder on the operator's machine turned out to be an unrelated Obsidian vault of business/planning markdown notes (identifiable by its `.obsidian` folder, ~150 files, not a git repo), and a sibling `Desktop\SONNY Game Plan` folder held only one business-plan `.docx`. The operator's primary logged-in GitHub account (`The-Reaver`) held only unrelated `Stag-*` repos, nothing SONNY-named. The actual codebase turned out to live under a separate, private GitHub organization the operator also has access to: `ShopOnlineNewYork`, containing 22 private repositories spanning Java/Spring, JavaScript/React, TypeScript/Next.js, Flutter/Dart, Python, and Terraform/Ansible infrastructure. A request to "assess the SONNY repo" was therefore actually a request to assess a 22-repo organization, not one codebase — and when a described codebase can't be found locally or under the obvious account, checking other orgs the account can access is the resolving step.

REVIEW: high-impact

## Links
- precedes, 2026-08-21-sonny-seven-active-vs-fifteen-dead-repos.md, the follow-on structural breakdown of the 22 repos.
