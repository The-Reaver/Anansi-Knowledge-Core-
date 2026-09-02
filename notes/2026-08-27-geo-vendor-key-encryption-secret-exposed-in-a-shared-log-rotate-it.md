---
id: 2026-08-27-geo-vendor-key-encryption-secret-exposed-in-a-shared-log-rotate-it
type: finding
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [security, secrets, rotation, railway, geo, operator-action]
sources:
  - ref: "Operator-supplied GEO Suite development log, 2026-08-27: the log's own text records the Fernet key generated for the live Railway service, in plaintext. Verified during ingest that the value had not yet reached research/knowledge-home/raw/ or .claude/anansi_live_capture/, and it was redacted at ingest so it never entered the archive"
    reliability: high
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [19, 19]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# The live GEO Suite VENDOR_KEY_ENCRYPTION_SECRET was written in plaintext into a shareable development log and should be rotated

## Body
**Operator action required.** The Fernet key set as `VENDOR_KEY_ENCRYPTION_SECRET` on the
live GEO Suite Railway service (service `d8aca3eb-f896-4e79-8ddc-4dcb761ae19f`, project
`e7e387ee-65f4-4b5a-9b14-c8e665f79d29`) was written out in plaintext in the development log that
session produced, and that log was then exported and uploaded to another session.

That key is the sole protection on every vendor API key stored in `vendor_credentials` -- an
Anthropic key and any other provider credentials the operator saves through
`/nova/admin/vendor-keys`. Anyone holding both the key and a copy of that table can decrypt all
of them.

Containment as of ingest, verified rather than assumed:
- The value is **not** in `research/knowledge-home/raw/` and **not** in
  `.claude/anansi_live_capture/` -- checked directly by content search before writing anything.
- It was redacted at ingest (`<redacted-production-secret>`), so it never entered the archive.
  Because this was a redaction *at ingest* rather than an edit to committed archive content,
  ADR-0005's append-only rule is untouched and no `.redaction-log.txt` entry is required.
- It **is** still in the uploaded log file on local disk under `~/.claude/uploads/`, and in the
  source cloud session's own transcript, neither of which this ingest controls.

Recommended: rotate the key on Railway. Note the real cost of rotation -- it is not a
drop-in swap. Every ciphertext in `vendor_credentials` was encrypted under the old key and will
fail to decrypt under the new one (`VendorKeyCryptoError`), so rotation means re-entering each
stored vendor key through the admin page afterwards, or writing a re-encryption step. At the time
of the log the table held very little, which makes now the cheapest moment to do it.

Standing lesson underneath the incident: a generated secret should be set into the platform and
never echoed into any artifact intended for a human to read later -- not a summary, not a handoff,
not a commit message. Refer to it by variable name and state that it was set.

## Links
- applies: notes/2026-08-21-rotate-dont-read-exposed-secrets-policy.md — the standing rule to
  report the path and secret type, never open the contents, and leave rotation to the
  operator. Worth recording that this incident's handling converged on that policy
  independently, before the policy had been read: the value was located with a targeted
  regex, never printed, redacted at ingest, and rotation left to the operator.
- relates-to: notes/2026-08-21-railway-kv-flag-printed-secrets-into-session-transcript.md
- relates-to: 2026-08-27-geo-vendor-keys-admin-page-shipped
