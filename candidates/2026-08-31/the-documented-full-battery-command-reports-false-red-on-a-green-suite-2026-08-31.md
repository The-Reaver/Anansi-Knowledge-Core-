---
id: the-documented-full-battery-command-reports-false-red-on-a-green-suite-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — verified directly against The-Reaver/The-Geo-Suite- at 73a58ce and against this repo"
project: geo
tags: [ci, testing, false-red, documentation-drift, gates]
supersedes: []
superseded_by: null
---

# The command the README called "the full battery" reports 10 of 74 files RED while pytest reports 1074/1074 GREEN

## Body

`ci_verify_geo.py` is the command GEO's README documented as the full test battery. Running
it reports **10 of 74 test files RED**. The same 74 files are **1074/1074 GREEN** under real
`pytest`.

The cause is a convention collision, not a regression. `ci_verify_geo.py` is a
standalone-runner battery ported from a parent monorepo — every test file executed via
`runpy` as its own `__main__`, pytest-free by design. Six of the repo's test files have
since grown real pytest fixtures and imports, which that runner explicitly rejects with
*"imports pytest: this battery is pytest-free and standalone."*

**Wiring the documented command into CI would have shipped a gate that failed on its own on
day one** — a false red baked in from the first run, guaranteeing the override reflex before
the gate ever caught anything real. The team correctly wired `python -m pytest -q` instead
and corrected the README in the same commit, leaving the runner reconciliation as separate,
honest work rather than folding it into "wire the test suite into CI."

**Check next time a documented command is wired into automation:** run it first and confirm
it is green on a known-good tree. Documentation drifts silently from the code it describes,
and a command's authority in a README is not evidence it still works.

## Links

- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
