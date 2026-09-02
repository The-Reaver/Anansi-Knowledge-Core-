---
id: 2026-08-21-alphanumeric-db-password-avoids-connection-string-parsing-failures
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [stag, postgres, connection-string, url-encoding, password]
sources:
  - ref: "Archive turns 389-496: turn 389 shows the decisive 'Invalid IPv6 URL' parser error during a DB connection attempt, diagnosed as an unescaped-special-character password malforming the connection string; turns 494-496 show the assistant generating a strictly alphanumeric password and writing it directly into .env, then having the operator paste that exact same string into Supabase's password-reset field so both sides match by construction"
    reliability: high
    origin: "2026-07-10 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-07-10-backfill-ebf4b889.jsonl
  turns: [389, 496]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A database password with special characters caused repeated, confusing "password authentication failed" errors by breaking the connection-string URL parsing, not by being wrong
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, the "Invalid IPv6 URL" parser error and the generate-once-paste-both-sides technique match the session's diagnosis. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-07-10, "Frontend rewiring TypeScript errors" (backfilled from historical transcript ebf4b889, 2026-08-21)
- confidence: high — directly diagnosed via a decisive "Invalid IPv6 URL" parser error and confirmed fixed once a strictly alphanumeric password was used on both sides
- verified: 2026-08-21
## Body
A Supabase database password containing unescaped special characters produced a connection string that standard URL parsers mis-split — in this session it manifested as an `Invalid IPv6 URL` error and authentication falling back to the wrong Postgres username, even though `supabase link`/`db push` worked fine because the CLI prompts for the password separately rather than embedding it in a URL. Resetting the password to a purely alphanumeric value (no `@ ! # $ %` etc.) eliminated the parsing ambiguity entirely. Because manually copying a password between the provider's reset dialog and the `.env` file kept introducing copy errors, the reliable technique used was to have the assistant generate the alphanumeric password and write it directly into the connection-string `.env` lines, then have the operator paste that exact same string into the provider's password-reset field — guaranteeing both sides match by construction rather than by careful transcription. General lesson: prefer strictly alphanumeric secrets for anything embedded in a URL-form connection string, since special characters can silently corrupt parsing in ways that look identical to "wrong password."
REVIEW: high-impact
## Links
- related, 2026-08-21-supabase-session-pooler-required-for-railway-ipv4.md, the connection string this password issue was blocking
- related, 2026-08-21-windows-notepad-silently-saves-env-as-env-txt.md, the other mechanism (a stale editor copy) that caused ".env edits don't seem to take effect" in the same deploy sequence
