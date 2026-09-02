---
id: 2026-08-21-supabase-session-pooler-required-for-railway-ipv4
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, supabase, railway, postgres, connection-pooling]
sources:
  - ref: "Archive turns 347-351: the agent explains 'for a backend hosted on Railway, copy the Session pooler one (it's IPv4-friendly — Railway needs that; the Direct one is IPv6-only on new projects and will fail)', and turn 351 confirms the operator's DB URL was already the correct Session-pooler string"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [347, 351]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A Railway-hosted backend must use Supabase's Session pooler connection string, not the Direct connection, because Supabase's Direct connection is IPv6-only on new projects
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the Session-pooler-vs-Direct distinction and the connectivity claim are corroborated by the actual railway.json region config and DB host string appearing in the transcript. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — the agent explicitly guided the operator to the Session pooler string and confirmed it was already correctly chosen; the connection was later proven to work from Railway's US-West region to Supabase's US-East pooler
- verified: 2026-08-21
## Body
For a backend hosted on Railway connecting to a Supabase Postgres database, the correct connection string is the Supabase **Session pooler** (host pattern `aws-0-<region>.pooler.supabase.com`, port 5432, username `postgres.<project-ref>`), not the Direct connection string, because Supabase's Direct connection is IPv6-only on newer projects while Railway requires IPv4 connectivity; the Session pooler is IPv4-compatible and also supports the prepared statements that `asyncpg` uses (unlike Supabase's Transaction pooler mode). As of this session, the connection-string UI in the Supabase dashboard had moved behind a green "Connect" button rather than living under Settings → Database, which the operator initially could not find. This same Session-pooler string is what should populate both `SUPABASE_DB_URL` and `DATABASE_URL`.
REVIEW: high-impact
## Links
- related, 2026-08-21-alphanumeric-db-password-avoids-connection-string-parsing-failures.md, the related password-format gotcha that made this same connection string fail authentication repeatedly
