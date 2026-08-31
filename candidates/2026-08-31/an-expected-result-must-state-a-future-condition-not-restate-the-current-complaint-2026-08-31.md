---
id: an-expected-result-must-state-a-future-condition-not-restate-the-current-complaint-2026-08-31
type: lesson
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [planning, writing, review, self-correction, remediation-plans]
supersedes: []
superseded_by: null
---

# A remediation plan's "expected result" that restates the problem is not a result, and hides that the action was never specified

## Body

In a remediation plan, the action "CI on the GEO repo" was given the expected result *"1210
passing tests currently prove nothing automatically — they run only when someone remembers."*
That is the present-day problem restated in the outcome column. It reads as substantive and
commits to nothing.

The actual expected result: *every push runs the suite automatically, a red suite blocks
the merge, and "the tests pass" becomes a fact about the repo rather than a claim about
someone's memory.*

Why this matters beyond style: an expected result is the acceptance criterion. If it
describes the current state, the item can never be shown to be done — and, worse, nobody
notices the action was under-specified, because the row looks complete. A plan full of such
rows audits as thorough while being unfinishable.

**Check next time a plan is written or reviewed:** read every expected result alone and ask
"is this a condition that is false today and would be true when this is finished?" If it is
true today, it is a complaint, not a result. Rewrite it as an observable future state.

## Links

- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
