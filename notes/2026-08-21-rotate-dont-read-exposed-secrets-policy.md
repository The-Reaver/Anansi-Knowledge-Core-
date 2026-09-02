---
id: 2026-08-21-rotate-dont-read-exposed-secrets-policy
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [security, secrets, operating-principle, agent-behavior]
sources:
  - ref: "Turns 34 and 44: the agent states it did not open the contents of exposed private keys or the committed .env file, and instead reports file paths and secret type for the operator to rotate — applied consistently to both P0 findings in the same session."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [34, 44]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# When a diagnostic finds committed secrets, report file paths and flag rotation — do not open the contents
- id: 2026-08-21-rotate-dont-read-exposed-secrets-policy
- type: decision
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, agent explicitly stated this handling and applied it consistently to both findings in this session
- verified: 2026-08-21
- tags: security, secrets, operating-principle, agent-behavior

## Body

When a repo audit surfaces committed secrets — private keys, `.env` files, or similar — the agent's applied practice was to identify and report the file paths and secret type without opening or reading their contents, and to flag them for rotation by the human operator rather than attempting remediation itself. This was applied in this session when 11 `.pem` files and a committed `.env` file were found across the ShopOnlineNewYork organization: the agent named the exact files and explained the risk but explicitly declined to read them, leaving both credential rotation and git-history rewriting — both irreversible or credential-sensitive actions — to the operator to execute.

REVIEW: high-impact

## Links
- relates-to, 2026-08-21-devops-repo-leaked-eleven-private-keys.md, one of the findings this policy was applied to.
- relates-to, 2026-08-21-sonnyny-committed-env-file.md, the other finding this policy was applied to.
