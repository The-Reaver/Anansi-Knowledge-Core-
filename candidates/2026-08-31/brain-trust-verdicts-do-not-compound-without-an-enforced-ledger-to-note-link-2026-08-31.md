---
id: brain-trust-verdicts-do-not-compound-without-an-enforced-ledger-to-note-link-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: fleet
tags: [brain-trust, governance, knowledge-core, compounding-assets, disposition]
supersedes: []
superseded_by: null
---

# Nine Brain Trust reviews produced ledger rows, and the rule that each verdict becomes a Core note is unenforced

## Body

The Brain Trust has run nine reviews, each recorded as a row in a ledger. The standing rule
that every verdict also becomes a Knowledge Core note is **not enforced by anything**, so
whether a verdict compounds depends on whoever closed the review remembering to write it.

A ledger row is a receipt that a review happened. A note is the reusable conclusion. Without
the second, the panel's output evaporates at exactly the rate the fleet forgets — which is
the failure Mandate 9 exists to prevent: a task only counts as a compounding asset if it is
captured and reused.

There is a second, subtler gap: **findings have no disposition tracking**. A review produces
findings; nothing records which were acted on, which were rejected with reasons, and which
were quietly dropped. Those three outcomes are indistinguishable afterwards, so a finding that
was silently ignored looks identical to one that was considered and declined.

**Two mechanisms follow:** a gate requiring every ledger row to carry a linked Core note id,
and a disposition field per finding with a closed set of outcomes. Both are cheap; both turn
an honour-system rule into a checkable one.

## Links

- relates-to: 2026-08-04-mandate-9-compounding-assets-ratified
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: an-sdlc-review-that-leaves-no-artifact-cannot-be-audited-2026-08-31
