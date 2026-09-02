---
id: 2026-08-23-agent-breakers-secret-leak-false-positives-against-live-anansi-hub
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"i ratify this\"), given after reviewing an operator-facing review report covering all 6 (all read in full, all 6 cross-referenced links confirmed to resolve, no factual errors found)."
project: fleet
tags: [agent-breakers, secret-leak, false-positive, anansi-hub, security-testing, validation]
sources:
  - ref: "Assistant reports 5 critical/high findings against the live Hub with no crash (line 1178), then fetches /api/data directly and confirms all 5 matched Core note slugs about prior resolved incidents and bare env-var names, not live secrets (lines 1180-1185)"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [1178, 1185]
risk_class: A
evidence_state: SUPPORTED
source_rating: F6
next_review: 2026-11-27
classified: 2026-08-29
---

# agent_breakers' secret_leak probe flagged 5 critical/high findings against the live Anansi Hub that were all confirmed false positives on direct inspection

## Body
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 1085-1237
- confidence: high, directly fetched /api/data and inspected the actual unredacted regex matches behind each finding
- verified: 2026-08-23

Running `agent_breakers` against the real, live Anansi Hub for the first time (after fixing the request-timeout crash recorded separately) produced 5 critical/high `secret_leak` findings. Rather than trust the harness's own severity labeling, the assistant fetched `/api/data` directly and inspected the actual unredacted regex matches behind each finding. All 5 were confirmed false positives: two matched the filenames/slugs of existing Knowledge Core notes that are themselves *about* prior credential-leak incidents already resolved and documented earlier in the fleet's history — the probe's pattern matched descriptive note-ID text, not a live credential. The other three matched bare environment-variable names (for a transactional-email API, a webhook secret, a test database password, and a payment-provider secret key) quoted inside a note discussing an already-assessed, already-accepted-as-low-risk Railway build-log warning — variable *names* only, not the underlying secret values.

This is the same class of false positive the repository's own secret-scanning pre-commit hook had already hit multiple times earlier in the same day (pattern-matching on text that describes or names a secret, not text that contains one), now independently rediscovered by a structurally different tool — `agent_breakers`' own regex-based `secret_leak` probe — running against real production data instead of a fixture. That makes this a legitimate validation result confirming both tools share the same blind spot, not a false alarm to dismiss without checking.

## Links
- relates, 2026-08-22-secret-scan-regex-false-positive-token-assignment-shape-in-code.md, the same false-positive class caught earlier the same day by the repo's own pre-commit secret scanner
- relates, 2026-08-23-agent-breakers-context-request-lacked-timeout-exception-handling.md, the fix that made this same harness run against the live Hub possible in the first place
