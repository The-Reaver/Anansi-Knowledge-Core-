---
id: 2026-08-06-ci-regulatory-pipeline-next-target-attorney-terms-first
type: decision
status: candidate
source: "this chat, 2026-08-06, session closing; Abad had a separate chat already open on this thread and asked for closing notes so it knows exactly where to look and what to do (source status: active)"
project: ci
tags: [compliance-intelligence, ci, regulatory-pipeline, attorney-partnership, handoff, operator-contribution]
---

# Next Session's Target: Draft Attorney Terms Before Any Atom-Versioning Code

## Body

This chat is closing. A separate chat is already open working on the same CI regulatory pipeline
thread; this note, plus the updated `CONTINUE_HERE.md` at the stag repo root, is the handoff for it.

The Opus review (see the linked build-outcome note) named five conditions before the atom-versioning
build should be trusted. Two, written terms with the attorney and an outside professional-conduct
read, are not engineering work and are not done. The review's own sequencing states these belong
before any code, not after. The next session's target, set at close: draft a one-page attorney-terms
document, covering confidentiality of his clients' data, how compensation or referrals do or do not
flow between STAG and the attorney (a non-lawyer cannot share legal fees or pay for referrals, and the
HBOT lead-generation pipeline sits directly next to this question), who owns his corrections once he
starts using the system, and a signed plain-English limitations disclosure (no flag does not mean
safe, no citator exists anywhere so a vacated court ruling cannot be detected outside a seeded test
case, bill tracking is not the same as knowing the current text of a state statute). That draft is for
Abad to take to outside counsel, not a substitute for a real legal review.

Checking whether Augustin's own independently-generated response to
`Augustin_CI_Regulatory_Pipeline_Dispatch_2026-08-05.md` has landed is a reasonable parallel action,
since it costs nothing and might change build-order priorities, but it should not substitute for or
delay the terms draft.

The atom-versioning build itself should not start until Abad has resolved the attorney-terms
condition. Building ahead of it risks the exact migration pain the schema-versioning work exists to
prevent if the terms process surfaces a requirement (a data-handling constraint, a scope limitation)
that changes the schema after code already depends on it.

## Links

- derived-from: 2026-08-06-ci-regulatory-pipeline-opus-review-and-schema-spec
