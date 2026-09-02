---
id: 2026-08-21-jq-unavailable-in-windows-git-bash-env
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [environment, windows, git-bash, jq, python, tooling]
sources:
  - ref: "Turns 30-31: a jq pipeline fails with a command-not-found error in the operator's Windows/Git Bash shell; the agent immediately switches to python to parse the same JSON output."
    reliability: high
    origin: "STAG session, 2026-08-01, \"SONNY repo assessment\" (backfilled from historical transcript 6cdc2fce, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-01-backfill-6cdc2fce.jsonl
  turns: [30, 31]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# jq is not installed in the operator's Windows/Git Bash shell; use python for JSON parsing instead
- id: 2026-08-21-jq-unavailable-in-windows-git-bash-env
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-01, "SONNY repo assessment" (backfilled from historical transcript 6cdc2fce, 2026-08-21)
- confidence: high, agent hit the missing-command error directly and switched tools mid-session
- verified: 2026-08-21
- tags: environment, windows, git-bash, jq, python, tooling

## Body

In the operator's Windows/Git Bash shell environment, the `jq` command-line JSON processor is not installed, so shell pipelines that pipe GitHub API JSON output through `jq` fail with a "command not found" error. `python` (available as `python`) is a reliable fallback for parsing and filtering JSON payloads, such as GitHub git-tree API responses, in this environment. This is an environment quirk worth remembering before reaching for `jq` in any future scripted GitHub API workflow on this machine.

## Links
- relates-to, 2026-08-21-metadata-only-github-repo-diagnostic-technique.md, the workflow this substitution was needed for.
