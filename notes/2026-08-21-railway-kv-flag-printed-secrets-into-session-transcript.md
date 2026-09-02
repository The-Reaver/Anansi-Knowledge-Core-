---
id: 2026-08-21-railway-kv-flag-printed-secrets-into-session-transcript
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is after independent spot-check confirmed the claim. Operator retains veto per Mandate 1."
project: fleet
tags: [geo, railway, security, secrets, cli, process]
sources:
  - ref: "Turn 313: the agent's own self-report, in the same turn the command ran, naming the `railway variables --service geo-suite --kv` command, the three secret categories exposed (DB password, JWT secret, service-role key), and the self-caught/scoped-to-names-since framing."
    reliability: high
    origin: "STAG session, 2026-08-14, \"GEO Suite completion\" (backfilled from historical transcript b9b0acfa, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-08-14-backfill-b9b0acfa.jsonl
  turns: [313, 313]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Running `railway variables --kv` without scoping to variable names printed the DB password, JWT secret, and service-role key in full into the agent's own session transcript
- id: 2026-08-21-railway-kv-flag-printed-secrets-into-session-transcript
- type: finding
- status: ratified
- class: confirmed
- source: STAG session, 2026-08-14, "GEO Suite completion" (backfilled from historical transcript b9b0acfa, 2026-08-21)
- confidence: high — self-reported by the agent in its own narration, same session, immediately after the command ran
- verified: 2026-08-21
- tags: geo, railway, security, secrets, cli, process
- REVIEW: high-impact

## Body
While checking Supabase configuration to plan the Knowledge Core's durable-storage wiring, the agent ran `railway variables --service geo-suite --kv` without restricting the output to variable names only. The `--kv` flag prints full key=value pairs, so the command's output — captured into the agent's own session transcript — included the actual values of the database password, JWT secret, and service-role key for the operator's live Supabase project. The agent caught this itself, did not reuse or repeat the values, and scoped every subsequent check to names only. Because these were the operator's own authenticated CLI session and nothing was sent to a third party, this was not an external leak — but the values now persist in this session's transcript/logs, so the agent recommended rotating those three values as a reasonable precaution. The generalizable lesson: any Railway (or similar platform) CLI command that can dump full variable values, not just names, should be treated as secret-exposure-risk by default and scoped defensively before running it, even in a fully-authenticated, operator-owned session — the transcript itself becomes a place secrets can leak to.

## Links
- relates, 2026-08-16-knowledge-core-vector-store-never-persisted-note-content-only-embeddings.md, the durable-storage work this Supabase config check was in service of when the leak happened.
