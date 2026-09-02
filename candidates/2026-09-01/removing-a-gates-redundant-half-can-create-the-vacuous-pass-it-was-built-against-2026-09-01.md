---
id: removing-a-gates-redundant-half-can-create-the-vacuous-pass-it-was-built-against-2026-09-01
type: lesson
status: candidate
source: "Recovery session, 2026-09-01 — operator ruling to scope omar_security_gate to the rate-limit check; the trap and the two false-positive classes were found in the same change"
project: fleet
tags: [gates, deduplication, vacuous-pass, false-positives, ast, omar, scope-change]
supersedes: []
superseded_by: null
---

# Deleting the redundant half of a gate can leave the other half with nothing to look at

## Body

Two gates were scanning for secrets with the *same* function. `omar_security_gate.check_secrets` was
literally `scan_for_secrets(root)` — the identical scanner `secret_scan_gate` composes, minus the
baseline and the regression check. The operator ruled: drop omar's secret half, keep the OWASP
rate-limit check that nothing else does.

Correct ruling. But the deletion nearly introduced the exact defect the fleet keeps recording.

Omar took its scan root **for the secret half** and its source files from an explicit `--source` flag
**for the rate-limit half**. `verify.py` invokes every gate in its battery as `--root ROOT`, with no
`--source`. So the moment the secret half went away, the battery's calling convention would have checked
**zero handlers and printed PASS** — a gate that runs and asserts nothing, which is what omar was
supposed to be the fix for.

The fix is small: discover sources under the root, and make every line of output state its own scope —
files checked, files unparseable — so a bare `PASS` is impossible to print.

## The general shape

When a component has two halves and one supplies the *input scope* while the other supplies the *check*,
removing either can leave the survivor well-formed, green, and inspecting nothing. Green is the dangerous
outcome, because it is read as evidence.

**Before deleting half of anything, ask what the surviving half was getting from it.** Not just which
functions it called — what *scope* it inherited.

## The second lesson, free with the first

Actually pointing the survivor at the whole tree immediately exposed two false-positive classes that had
been latent for as long as the gate existed, invisible because it had only ever been run against explicit
single files:

- `@patch` from `unittest.mock` was read as an HTTP PATCH route, so **every mocked test function in the
  repository** counted as an unprotected mutating handler.
- Matching was a **substring** test, so `deposit` contains "post" and `soft_delete` contains "delete".

A check that has only ever run on hand-picked inputs has not been tested against reality. Widening its
scope is the cheapest audit of it available — and the findings that appear first are usually the
check's own bugs, not the codebase's.
