---
id: 2026-08-22-agent-breakers-self-test-independently-reproduced-exact-finding-counts
type: finding
status: ratified
ratified: |
  2026-08-22 — operator directly ratified via explicit instruction ("ratify the 13 that hold up"), given after reviewing an operator-facing note-by-note review report covering all 13 (2 factual errors found and corrected -- a 12-vs-13 file-count miscount in two notes, now fixed; the 2 REVIEW: high-impact notes cross-checked against reports/STAG_BRAIN_TRUST_LEDGER.md and commit 77b647e in the compliance_intelligence repo; all 7 cross-referenced note links confirmed to resolve). Not an AI self-certification -- see the ai-reviewed content above, this line records the operator's own ratification act.
project: fleet
tags: [agent-breakers, security-testing, verification, self-test]
sources:
  - ref: "Archive lines 727-739: assistant actually starts the fixture app and runs the agent_breakers harness end-to-end against it, reproducing the README's exact self-test numbers (3 critical, 1 high, 14 medium, 18 total; zero findings on the control route)."
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [727, 739]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# Before committing the agent_breakers security harness, its README's claimed self-test numbers (18 findings) were independently reproduced by actually running it, not just read and trusted

- class: confirmed
- source: this session (STAG repo, 2026-08-22), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 136-783
- confidence: high — directly ran the fixture app and the harness against it in-session and observed the exact match
- verified: 2026-08-22

## Body
`AJ/agent_breakers/` is a real-HTTP self-red-team harness with five safety-railed probes (auth_bypass, tenant_isolation, injection_fuzz, malformed_payload, secret_leak), built against a deliberately-vulnerable Flask fixture app (`selftest/test_dummy_app.py`) as its own proof mechanism. Before recommending it as ready to commit, rather than trusting the README's stated numbers, the fixture app was actually started locally and the harness actually run against it end-to-end: the self-test reproduced exactly what the README claimed — 3 critical, 1 high, 14 medium (18 total) findings — and a control route (`/api/clean/{id}`) produced zero findings, confirming the harness isn't just flagging everything indiscriminately. The harness's safety rails (host allowlist, mutating-route skip, rate budget, dry-run mode, secret redaction in reports) were also read directly against the code, not just the README's description of them.

This is the same discipline used elsewhere in this session (verifying a Brain Trust security finding by reading the underlying code directly rather than trusting a note's citations, verifying a graph-physics feature request against the actual existing implementation rather than the pasted architecture document's framing): a component's own documentation of its test results, capability claims, or safety guarantees is a claim to independently reproduce before it's used as the basis for a "ready to ship" recommendation, not evidence to cite as-is — regardless of how internally consistent or plausible the documentation reads.

## Links
- relates, 2026-08-22-a-probe-that-only-reuses-other-probes-traffic-has-zero-coverage-on-untouched-routes.md — a design bug in this same harness found during its original build (a different session), also only caught by actually running it end-to-end rather than reading the code.
