---
id: safeguard-existence-does-not-imply-invocation-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy), 2026-08-31 — relayed by the operator into a recovery session after the originating machine went offline mid-run; not yet reconciled against a raw/ archive"
project: fleet
tags: [gates, hooks, wiring, false-green, safeguards, keystone]
supersedes: []
superseded_by: null
---

# Four safeguards were correct, committed, and invoked by nothing — and every gate passed

## Body

Four separate safeguards were found built, correct, committed, and called by nothing at
all. They passed every gate the repo has, because the existing `hook_parity_gate.py`
compares two *declaration* files to each other and never inspects what is actually
installed in `.git/hooks/`. **Two documents can agree perfectly while describing an empty
directory.**

The gate battery had 34 gates, 7 of them wired.

The general principle this establishes, and which most of the fleet's plans silently
assume: **"a safeguard exists" does not imply "a safeguard runs."** Today that implication
is false, and every downstream claim resting on it inherits the falsehood. Reviewing that a
control is correctly written proves nothing about whether it is reachable.

**Check next time a control is added:** verify invocation, not authorship. Assert the
control is installed, executable, and actually referenced by whatever is supposed to call
it — and treat "cannot determine" as failure, never as pass. The silent-disable case (a
hook present and executable but no longer calling its script) is the worst of all, because
it looks healthiest.

## Links

- relates-to: a-glob-installer-defeats-a-text-parser-and-turns-the-gate-into-a-vacuous-pass-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
- relates-to: a-stale-git-lock-froze-a-repo-for-29-days-without-erroring-2026-08-31
