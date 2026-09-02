---
id: 2026-08-27-partial-update-requiring-resubmission-of-a-secret-reads-as-a-broken-feature
type: lesson
status: ratified
ratified: "2026-08-27 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
date: 2026-08-27
project: geo
tags: [api-design, ux, secrets, partial-update, geo]
sources:
  - ref: "GEO Suite, 2026-08-27: SaveVendorKeyRequest.api_key was non-Optional, so a model-only edit was structurally impossible without re-pasting the whole key; operator reported it as 'i can not change the models in the vendor keys section'; fixed by making api_key Optional with a keep-existing-ciphertext branch, and mutation-tested by reverting to always-require-key"
    reliability: medium
    origin: "GEO Suite cloud session https://claude.ai/code/session_01VtyCP3VwdDb4cxvL66VRxi, 2026-08-27; harvested into the Core from an operator-supplied development-log export by the bridge-cse stag session the same day. Raw transcript was NOT retrievable (see 2026-08-27-cloud-session-raw-transcript-is-not-retrievable-locally)."
provenance:
  archive: research/knowledge-home/raw/2026-08-27-geo-suite-vendor-keys-and-production-config-sweep.jsonl
  turns: [19, 19]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# An API that requires re-submitting a write-only secret to change any adjacent field is a real bug, even when every line of code does exactly what it was written to do

## Body
The vendor-keys page stored an encrypted API key and a `default_model` on the same record.
`SaveVendorKeyRequest.api_key` was required (non-Optional), so changing *only* the model was
structurally impossible without re-pasting the entire secret -- which the user cannot do, because
the UI correctly shows the key masked and never returns it. The frontend Save button, correctly,
refused to submit with a blank key field.

Every individual component behaved exactly as written. The feature was still broken, and the
operator's report -- *"i can not change the models in the vendor keys section"* -- was exactly
right.

Two durable points:

1. **Write-only fields make partial updates mandatory, not optional.** As soon as one field on a
   resource can be written but never read back, "PUT the whole resource" stops being a valid
   contract -- the client structurally cannot reconstruct the payload. The moment a secret joins
   a record, the update semantics for every other field on that record have to be revisited.
2. **Backend and frontend must agree on what a legitimate partial update looks like before either
   is 'done.'** Here the fix was two-sided: the backend branched on a blank key (existing row ->
   keep the ciphertext untouched, no re-encryption, update `default_model` only; no existing row
   -> a genuine 422), and the frontend's gate had to change to match
   (`canSave = hasNewKey || (status.configured && modelChanged)`). Fixing one side alone would
   have produced either a button that still won't submit, or a request the server rejects.

Diagnostic tell: when a user says "I can't change X" and the code says X is changeable, check
whether changing X requires resubmitting something the user cannot see.

## Links
- relates-to: 2026-08-27-silent-sample-data-fallback-made-a-missing-key-look-like-a-dead-button
- relates-to: 2026-08-27-geo-vendor-keys-admin-page-shipped
