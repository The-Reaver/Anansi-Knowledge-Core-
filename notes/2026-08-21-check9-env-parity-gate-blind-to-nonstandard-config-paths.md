---
id: 2026-08-21-check9-env-parity-gate-blind-to-nonstandard-config-paths
type: finding
status: ratified
ratified: "2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py"
project: fleet
tags: [meta_agent, validator, gate-battery, false-positive, geo_platform]
sources:
  - ref: |-
      Archive lines 624 and 627: the agent reads Check 9's env-parity gate implementation and states "Check 9 only recognizes pydantic settings fields at the exact path app/config.py, but this project's config is at app/core/config.py, and it doesn't track settings.X attribute access -- so it wrongly thinks SUPABASE_URL/SUPABASE_KEY are phantom".
    reliability: high
    origin: "2026-07-18 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-18-backfill-0dc45404.jsonl
  turns: [624, 627]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# The gate battery's Check 9 (environment-parity check) only recognizes Pydantic settings declared at the exact path app/config.py, so it false-flags real, in-use secrets as phantom when config lives elsewhere

- ratified: 2026-08-21 — operator directly ratified via scripts/knowledge_home/ratify.py
- class: confirmed
- source: STAG session, 2026-07-18, "A2 provisioning environment gates" (backfilled from historical transcript 0dc45404, 2026-08-21)
- confidence: high — the agent read Check 9's implementation directly and confirmed the exact-path assumption and lack of attribute-access tracking
- verified: 2026-08-21

## Body

In `projects/geo_platform`, Check 9 of the gate battery flagged `SUPABASE_URL` and `SUPABASE_KEY` as "phantom" (declared but apparently unused) secrets. Investigation showed this is a gate limitation, not a real defect: Check 9 only looks for a Pydantic `BaseSettings` class at the literal path `app/config.py`, and it does not track `settings.X` attribute-access reads. This project's config module lives at `app/core/config.py`, and the keys are legitimately read via `settings.SUPABASE_URL` / `settings.SUPABASE_KEY` inside `permissions.py`. The gate's suggested fix — deleting the "unused" keys — would have broken deploy.

Any future project whose Pydantic settings module is not at the exact path `app/config.py` should expect Check 9 to false-positive on real, in-use secrets, and that finding should be treated as a gate artifact rather than acted on, unless Check 9 itself is fixed to resolve the actual config module location and to track attribute-access reads.

## Links
- co-occurs, 2026-08-21-run-gate-battery-against-throwaway-copy-not-live-tree.md, surfaced during the same throwaway-copy gate-battery run.
