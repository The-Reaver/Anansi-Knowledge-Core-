---
id: an-sdlc-review-that-leaves-no-artifact-cannot-be-audited-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: fleet
tags: [sdlc, review, audit-trail, seat-separation, artifacts]
supersedes: []
superseded_by: null
---

# The implement/review split works and leaves no evidence that it happened

## Body

The SDLC seat separation earns its cost. In one night it caught two real defects the
implementing seat had missed, including a prune list that would have blinded the secret
scanner. That is the mechanism doing exactly what it exists to do.

But **a review leaves no artifact**. Nothing records that a slice was reviewed, by which seat,
against what, or with what outcome. The separation is therefore *asserted* rather than
auditable — and it has already been violated once, which was discoverable only because someone
happened to notice.

An unenforced separation degrades quietly and in the direction of convenience: the seat that
is busiest starts reviewing its own work, no artifact is missing because none was ever
expected, and the first evidence of drift is a defect that should have been caught.

**Require a review record per slice** — seat, target, findings, disposition, outcome — as a
committed artifact. Then "this was independently reviewed" becomes a fact about the repository
rather than a claim about a process, and a missing record is itself the signal.

This is the same shape as the Brain Trust's unenforced verdict-to-note rule: a good mechanism
whose output is not required to exist.

## Links

- relates-to: brain-trust-verdicts-do-not-compound-without-an-enforced-ledger-to-note-link-2026-08-31
- relates-to: per-file-verification-caught-a-prune-list-that-would-have-blinded-the-secret-scanner-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
