---
id: 2026-08-21-railway-raw-editor-variable-paste-landed-on-wrong-geo-service-and-silently-failed-to-save
type: finding
status: ratified
ratified: "2026-08-21 — ratified by explicit operator instruction (\"ratify the 92 that hold up\"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification."
project: fleet
tags: [railway, geo, deploy, supabase, credentials, ops-footgun, sdlc]
sources:
  - ref: "Railway/Supabase credential-wiring session transcript, 2026-08-13: four paste-then-verify cycles covering a variable paste landing on the wrong service (geo-frontend instead of geo-suite) and a direct-host vs. Session-pooler SUPABASE_DB_URL mismatch"
    reliability: high
    origin: "2026-08-12 backfill session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-12-backfill-20b5a40c.jsonl
  turns: [131, 173]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Wiring GEO Suite's live Supabase secrets into Railway took four separate "done"/"verify" round-trips: one paste landed on the wrong Railway service, and a wrong connection-string value needed two more rounds to fix, with no error surfaced at any point

- id: 2026-08-21-railway-raw-editor-variable-paste-landed-on-wrong-geo-service-and-silently-failed-to-save
- type: finding
- status: ratified
- ratified: 2026-08-21 — ratified by explicit operator instruction ("ratify the 92 that hold up"), given after the operator's own review of the aggregate high-impact review summary (92/93 held up, 1 flagged and excluded) recorded in OPERATOR_AGENDA.md. Individual note content was AI-reviewed with real evidence checks (see the ai-reviewed line below); this line records the operator's own ratification act per Mandate 1, not an AI self-certification.
- ai-reviewed: 2026-08-21 — high-impact review pass at operator's direct request, holds up after correcting two overstatements (attempt-1 root cause presented as fact rather than unconfirmed hypothesis; title claiming two confirmed wrong-service landings instead of one) against research/knowledge-home/raw/2026-08-12-backfill-20b5a40c.jsonl lines 131-174. This is AI review, not operator ratification; still pending the operator's own sign-off.
- class: confirmed
- source: STAG session, 2026-08-12, "Infrastructure completion status" (backfilled from historical transcript 20b5a40c, 2026-08-21)
- confidence: high for the wrong-service finding (attempt 2) and the direct-host-vs-pooler finding (attempts 3/4), both stated explicitly by the agent in the transcript; the underlying Railway/CLI commands themselves are not preserved in this condensed archive (only a generic "Bash" tool-call marker survives), so exact invocations like `railway variables --service <id>` are a plausible inference, not something directly visible in this source
- verified: 2026-08-21
- tags: railway, geo, deploy, supabase, credentials, ops-footgun, sdlc
- REVIEW: high-impact

## Body

After GEO Suite's backend and frontend were first proven live on Railway on 2026-08-13 (see the ratified note on that deploy), the operator tried to wire the real Supabase credentials into the backend so the agent could verify a live DB round-trip. This took four "I pasted it, verify it now" cycles across roughly 45 minutes, and by the end of the archived transcript the round-trip was still not verified:

1. **First attempt**: operator said the secrets were pasted; the agent redeployed and found none of the five Supabase variables present anywhere in the project (neither service). The transcript never establishes why — the agent could only offer two unconfirmed hypotheses: either the paste went into a different Railway project (e.g. the pre-existing `sandbox-small-business-tool-set`), or the Raw Editor paste was never saved via the explicit "Update Variables" button, leaving the change pending and invisible to `railway variables`/redeploys with no error shown to the person pasting. Which of these actually happened is not resolved anywhere in the archive.
2. **Second attempt**: after the operator re-saved, the agent found the variables had landed on the wrong Railway service. The project has two services, and the backend one is named `geo-suite` — identical to the Railway *project* name (`geo-suite`), while the actually-different service is `geo-frontend`. All seven variables, including `SUPABASE_SERVICE_ROLE_KEY` (a secret meant to be server-only, never exposed to a public-facing frontend), had been pasted into `geo-frontend` instead of the backend. This was caught before a frontend deploy was triggered, so the key was never actually shipped anywhere — but it was one click away.
3. **Third attempt**: variables now correctly present on the right service, but `SUPABASE_DB_URL` was the direct-host Supabase connection string rather than the Session pooler string that Railway's network can actually reach (a gotcha already documented in `RAILWAY_ENV_MANIFEST.md`) — confirmed by the error signature changing from `ConnectionRefusedError` (placeholder host) to `OSError: Network is unreachable` (real but unroutable direct host).
4. **Fourth attempt**: operator reported the pooler string was pasted; the agent found `SUPABASE_DB_URL` unchanged from the direct-host value. The archived transcript ends here, with the agent asking for a screenshot rather than burning another deploy cycle on an unconfirmed edit — the live DB round-trip was not verified within this session.

The generalizable lesson: in a two-service Railway project where one service happens to share its name with the project itself, and where the Raw Editor's save state is not obviously reflected in the UI, an operator's "done" is not reliable evidence that a variable change actually reached the intended running service. Each of the first three claims of "done" turned out to be wrong for a different reason, each only caught by the agent independently re-checking `railway variables --service <id>` rather than trusting the report and proceeding straight to a redeploy-and-verify cycle.

## Links
- extends, 2026-08-13-geo-suite-first-live-deploy-two-real-bugs-found-only-by-actually-deploying.md, this is the credential-wiring follow-on to that same live deploy, working through the same project's Railway console.
