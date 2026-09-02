---
id: 2026-08-21-metadata-only-github-repo-diagnostic-technique
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [technique, github-api, git-tree, repo-audit, usage-efficiency]
sources:
  - ref: "Turns 26-34 and 44: the agent states its intent to use GitHub API metadata and targeted file fetches rather than cloning, executes that approach across the 22-repo org to surface secrets and bloat findings, and turn 44 confirms zero cloning occurred at low token cost."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [26, 44]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A repo-org health/security/bloat audit can run almost entirely on GitHub API metadata, no cloning needed
- id: 2026-08-21-metadata-only-github-repo-diagnostic-technique
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, this is exactly the technique the agent used and the results it produced in this session
- verified: 2026-08-21
- tags: technique, github-api, git-tree, repo-audit, usage-efficiency

## Body

A structural, security, and bloat audit of a GitHub repository or organization can be performed almost entirely from GitHub API metadata — repo size and language stats, branch counts, and recursive git-tree listings with per-blob sizes, plus targeted raw-file fetches for specific paths — without cloning any repository content. Applied across the 22-repo ShopOnlineNewYork organization in this session, this metadata-only approach found leaked secrets (committed `.pem` keys and a `.env` file), the exact source of multi-hundred-MB bloat (unoptimized images vs. dead git history), and the duplication map across repos, all at near-zero token/download cost. The git-tree listing specifically can distinguish bloat living in the current working tree from bloat living only in history, which matters for deciding whether a fix is "delete + gitignore" versus "history rewrite required."

## Links
- relates-to, 2026-08-21-sonnyny-one-gb-bloat-mostly-images-and-history.md, a finding produced by this technique.
- relates-to, 2026-08-21-devops-repo-leaked-eleven-private-keys.md, another finding produced by this technique.
