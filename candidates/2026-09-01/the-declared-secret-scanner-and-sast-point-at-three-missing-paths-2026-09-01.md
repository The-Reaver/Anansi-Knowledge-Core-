---
id: the-declared-secret-scanner-and-sast-point-at-three-missing-paths-2026-09-01
type: finding
status: candidate
source: "Recovery session, 2026-09-01 — adversarial panel finding, independently re-verified against the repositories by the session relaying it"
project: fleet
tags: [pre-commit, detect-secrets, bandit, misconfiguration, dead-config]
supersedes: []
superseded_by: null
---

# The fleet already declares a secret scanner and a SAST tool, both aimed at paths that do not exist

## Body

**Verified.** `.pre-commit-config.yaml` declares `Yelp/detect-secrets` with
`args: ['--baseline', '.secrets.baseline']` and `PyCQA/bandit` with
`args: ["-c", "pyproject.toml", "-r", "projects/"]`.

In `stag-fleet`: **`.secrets.baseline` does not exist. `pyproject.toml` does not exist.
`projects/` does not exist.** All three targets are absent.

The config's own comments confirm the tools never run — `pre-commit` is not installed on the
machine, so the hand-rolled installer is the live path, and *"Neither path runs the third-party
hooks above."*

This is worse than the familiar built-but-unwired pattern. These are **mis-wired**: not merely
disconnected, but pointed at nothing, so wiring them tomorrow would fail rather than work. And a
security plan reasoned from their presence, treating the repository as already having secret
scanning and SAST declared and needing only connection.

**The lesson:** a declared-but-dead tool is worse than no tool, because a reader — human or agent —
counts it as coverage. When auditing what a repo has, check that each declared target resolves.
Declaration is not configuration, and configuration is not execution.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
- relates-to: every-geo-security-scanner-is-advisory-by-construction-2026-09-01
