---
id: a-gate-that-does-not-declare-fail-open-or-fail-closed-cannot-be-audited-2026-08-31
type: decision
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: fleet
tags: [gates, fail-closed, auditability, convention, safeguards]
supersedes: []
superseded_by: null
---

# Every gate should declare fail-open or fail-closed in its docstring, and be tested for it

## Body

The gate battery holds 34 gates. Reading them tells you what each checks; it does not tell you
what each does when the check **cannot be performed** — a missing input, an unparseable file,
an unreachable dependency. That behaviour is the gate's real strength, and today it is
discoverable only by reading each implementation closely.

The consequence is that the battery's coverage cannot be read off the code. A fail-open gate
and a fail-closed one look identical in a list, and only one of them is a control. The
existing evidence cuts both ways: `deploy_verify.py`'s migration check failed open and sat
useless for weeks, while `installed_hook_gate.py` fails closed on an unparseable installer —
and nobody could tell which was which without opening the file.

**Adopt as convention:** every gate states `fail-open` or `fail-closed` in its docstring, and
carries a test exercising that path — feeding it the unperformable case and asserting the
declared outcome. Then the battery's true strength is a property you can grep for rather than
a belief.

Default to fail-closed. An unperformed check is not a clean check.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: the-installed-hook-gate-already-fails-closed-on-zero-declared-hooks-2026-08-31
- relates-to: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
