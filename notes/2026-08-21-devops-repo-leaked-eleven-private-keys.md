---
id: 2026-08-21-devops-repo-leaked-eleven-private-keys
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: sonny
tags: [sonny, shoponlinenewyork, devops, secrets, security, git-history]
sources:
  - ref: "Turns 32-34 and 44: a git-tree metadata pass surfaces 11 committed .pem private-key files under two directory paths (terraform/keys/ and terraform/pem_files/), spanning SSH/EC2, Ansible, Kubernetes, and MySQL access across dev/test/prod environments; the agent confirms it did not open file contents and flags the finding for operator rotation."
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

# ShopOnlineNewYork's devops repo had 11 private-key .pem files committed to git
- id: 2026-08-21-devops-repo-leaked-eleven-private-keys
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, discovered directly via git-tree file listing, file paths and counts explicitly reported
- verified: 2026-08-21
- tags: sonny, shoponlinenewyork, devops, secrets, security, git-history

## Body

As of 2026-08-01, the ShopOnlineNewYork `devops` repository had 11 private-key `.pem` files committed to git, under `terraform/keys/` and a duplicate set under `terraform/pem_files/`, covering SSH/EC2, Ansible, Kubernetes, and MySQL access across dev, test, and prod environments. This is a P0 credential exposure even though the repo is private, because git history preserves the keys for anyone with repo read access, and a delete-only commit does not remove them from history. The agent identified the file paths and key types without opening or reading the file contents, and flagged them for the operator to rotate. Remediation requires both rotating every exposed key and rewriting git history (e.g. with `git filter-repo` or BFG) — a plain delete commit is insufficient.

REVIEW: high-impact

## Links
- relates-to, 2026-08-21-sonnyny-committed-env-file.md, the second P0 secret exposure found in the same session.
