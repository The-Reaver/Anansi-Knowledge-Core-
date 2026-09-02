---
id: 2026-08-27-infrastructure-changed-via-mcp-leaves-no-trace-in-the-repo
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: fleet
tags: [infrastructure, mcp, auditability, change-management, railway, supabase]
sources:
  - ref: "GEO Suite session 2026-08-27: 3 migrations applied directly to Supabase project lhzxmvjwqllmnqecfxpm and 3 env vars set on Railway service d8aca3eb-f896-4e79-8ddc-4dcb761ae19f via MCP tools, none of which produced a commit"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [22, 22]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Infrastructure an agent changes through MCP tools leaves no trace in the repo, so the change record has to be written deliberately or it exists only in the platform's own logs

## Body
In one session an agent made six live production mutations through MCP tools:

- **3 migrations applied** directly to Supabase project `lhzxmvjwqllmnqecfxpm`:
  `content_pages_add_terms_type`, `content_pages_add_contact_type`, `vendor_credentials_table`.
- **3 Railway env vars set** on service `d8aca3eb-f896-4e79-8ddc-4dcb761ae19f` ("The-Geo-Suite-",
  project `e7e387ee-65f4-4b5a-9b14-c8e665f79d29`): `GEO_PUBLIC_API_BASE`,
  `VENDOR_KEY_ENCRYPTION_SECRET`, `GEO_USE_SUPABASE_VENDOR_CREDENTIALS_REPO`.

**None of these produced a commit.** Code changes leave a diff, a message, an author and a date.
Infrastructure changed through a platform API leaves nothing in the repository at all -- the only
record is inside Railway's and Supabase's own audit logs, which are not where anyone looks when
asking "why did this behave differently after the 27th?"

This is a new asymmetry created by giving agents MCP access to deploy platforms. The agent can
now change the *environment* as easily as the code, but only one of those is version-controlled.
The failure it sets up is a future session reading a green repo, finding no record of a config
change, and re-deriving the same production mystery from scratch.

What to do: when an agent mutates live infrastructure, **write the change record deliberately** --
into the archive, a note, or a commit that touches `.env.example` / the README alongside it. Name
the project, the service ID, the variable or migration, and why. The ordinary discipline of "the
commit is the record" silently does not apply here, so the record has to be made on purpose.

(Note the ordering hazard this also creates: an env var set by hand and *only* documented later
in `.env.example` is indistinguishable, to the next reader, from one that was never set.)

## Links
- relates-to: 2026-08-27-a-committed-migration-is-not-an-applied-migration
- relates-to: 2026-08-27-green-unit-suite-does-not-detect-production-config-drift
