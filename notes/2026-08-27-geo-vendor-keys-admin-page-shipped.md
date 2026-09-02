---
id: 2026-08-27-geo-vendor-keys-admin-page-shipped
type: artifact
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [artifact, geo, vendor-keys, secrets, admin, architecture]
sources:
  - ref: "GEO Suite commits 626b595, b49e4a6, 6559737, edd5357, d84deae, c1b4ddc, eb0f00e, 75e8bf2, 4e2da1b, c32e113, 9435293, then 3d511ba, 8ce7622, 2ee4f64; backend suite 693 -> 985 -> 987 passing"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [10, 15]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# GEO Suite vendor-keys admin page shipped as 7 slices, generalising to non-LLM providers by extending one credentials table rather than building a second system

## Body
**What it is.** An owner-gated admin page at `/nova/admin/vendor-keys` letting the operator
enter provider API keys into the product itself, instead of the keys living only as Railway
environment variables. Triggered by the operator wanting to supply their own Anthropic key.

**Shape of the build (7 slices):** `vendor_credentials` table with RLS and a `service_role`-only
grant, deliberately stricter than sibling tables because it holds secrets (626b595); repository
with `Protocol` + InMemory/Supabase implementations and a best-effort audit write to `events`
whose payload never includes the key, not even ciphertext (b49e4a6); Fernet crypto helpers
raising `VendorKeyCryptoError` on every failure mode (6559737); owner-gated GET/PUT/DELETE router
using the proven `require_owner` rather than the newer `require_owner_membership`, with masking
at 8 asterisks plus last-4 (edd5357); read-path wiring so `registry.py` checks the DB store first
and falls back to env-var Settings (d84deae/c1b4ddc/eb0f00e); Nova frontend with an Admin sidebar
section gated on `sessionUser.role` (75e8bf2); adversarial pass (4e2da1b, c32e113); docs (9435293).

**Three design choices worth carrying forward:**

1. **Stricter-than-default RLS on the secrets table, stated as deliberate.** The asymmetry with
   the rest of the schema is intentional and recorded, so a later "why is this table different?"
   does not get it relaxed.
2. **The proven dependency over the newer one.** `require_owner` was chosen over
   `require_owner_membership` specifically because it was the battle-tested gate. On the path
   guarding secrets, familiarity beat freshness.
3. **DB-first with env-var fallback**, rather than a cutover -- the feature can ship before every
   key is migrated, and an unset key degrades to the previous behaviour instead of breaking.

**Generalisation to non-LLM providers (in flight at the time of the log).** When the operator
asked for *"a section where i can apply all keys need from any vendor,"* the decision was to
extend the **same** table, admin page, encryption and audit machinery rather than stand up a
parallel system. `google_places` becomes an 8th vendor and the first non-LLM one; it needs a
field the 7 LLM vendors never did -- a base `api_url` -- because `http_places_source()` is
deliberately provider-agnostic. Migration `20260827020000` landed and was applied (2ee4f64).

A drift-guard consequence worth noting: the three-way lockstep test was **deliberately loosened**
from `VALID_VENDORS == VENDOR_MODULES.keys()` to `VENDOR_MODULES.keys() <= VALID_VENDORS`,
because `google_places` has no `registry.py` module -- it is a different read path. Loosening a
drift guard is a real cost and was taken knowingly; the containment is that the subset direction
still catches an LLM vendor being added to the registry without the table.

**Not yet done at the time of the log:** the repository-layer commit (staged); the router layer
(`api_url` on the request model, surfaced in GET status, and the same keep-existing-if-blank
partial-update treatment `default_model` already has); the read-path wiring in
`prospect_source.py` (`_places_enabled()` / `http_places_source()` should check the DB store first
and fall back to the env vars, mirroring `registry.py`'s `credential_for()` shape); and the
frontend (`vendorLabels.ts` entry plus a needs-a-URL flag, a conditional URL input in
`VendorKeyForm.tsx`, pass-through in `page.tsx`).

**Evidence is second-hand for the slice-by-slice narrative.** The commit hashes and file paths
come from the source development log, not from direct inspection of `the-geo-suite-`. The
hashes are checkable and should be checked before this record is relied on for anything load-
bearing; the design decisions it captures are the durable part.

## Links
- relates-to: 2026-08-27-partial-update-requiring-resubmission-of-a-secret-reads-as-a-broken-feature
- relates-to: 2026-08-27-a-zero-vulnerability-adversarial-pass-still-earned-its-cost
- relates-to: 2026-08-27-geo-vendor-key-encryption-secret-exposed-in-a-shared-log-rotate-it
