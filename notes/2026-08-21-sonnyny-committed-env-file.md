---
id: 2026-08-21-sonnyny-committed-env-file
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, sonnyny, secrets, security, git-history]
sources:
  - ref: "Turn 32 flags a committed .env file in SonnyNY, turn 34 confirms the agent did not open it, and turn 44 gives the remediation: rotate, remove from working tree and git history, and gitignore."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [32, 44]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# ShopOnlineNewYork's SonnyNY storefront repo had a .env file committed at its root
- id: 2026-08-21-sonnyny-committed-env-file
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, discovered directly via git-tree file listing
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, sonnyny, secrets, security, git-history

## Body

As of 2026-08-01, the ShopOnlineNewYork `SonnyNY` repository (the React storefront web app) had a `.env` file committed at its repository root. Because `.env` files typically hold API keys, database credentials, or payment secrets, this is a P0 exposure. The agent did not open the file to see its contents; it flagged the path and file type and recommended the operator rotate whatever it contained, then remove the file from both the working tree and git history (adding `.env` to `.gitignore` to prevent recurrence).

REVIEW: high-impact

## Links
- relates-to, 2026-08-21-devops-repo-leaked-eleven-private-keys.md, the first P0 secret exposure found in the same session.
