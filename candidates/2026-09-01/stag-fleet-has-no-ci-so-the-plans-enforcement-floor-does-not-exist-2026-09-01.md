---
id: stag-fleet-has-no-ci-so-the-plans-enforcement-floor-does-not-exist-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — adversarial panel finding, independently re-verified against the repositories by the session relaying it"
project: fleet
tags: [ci, enforcement, aj-audit, verification-discipline, critical]
supersedes: []
superseded_by: null
---

# The plan's entire enforcement model rested on a CI surface that does not exist in the repo it targets

## Body

**Verified in one command.** `/home/user/stag-fleet` has no `.github` directory;
`git ls-files | grep -c '^\.github'` returns **0**. Stag-Fleet has no CI at all.

The security plan's central thesis was that CI is the only enforcement no clone can opt out of. Its
Phase 1 named CI "the enforcement floor". Its Phase 3 put `terraform plan` in CI. And its §7 stated
every control must land in Stag-Fleet — the repository with no CI.

The plan even wrote *"Stag-Fleet's CI surface needs checking"* and then never ran the `ls` that
answers it. AJ's own audit of 2026-08-09 already carried this as recommendation #1 — *"Stand up
minimal CI... the highest-leverage single action"* — unchanged since 2026-08-03.

**Two lessons, and the second is the durable one.** First: a foundational assumption stated as a
to-do inside a document is an assumption nobody will check, because it reads as already handled.
Second: **the answer was one command away and free.** The cost of verifying was seconds; the cost of
not verifying was an entire architecture built on a floor that isn't there. When a document names
something it did not check, that is the thing to check first, not last.

## Links

- relates-to: three-blind-reviewers-rejected-the-security-plan-unanimously-2026-09-01
- relates-to: validate-the-measuring-tool-before-trusting-its-aggregate-2026-08-31
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
