---
id: a-glob-installer-defeats-a-text-parser-and-turns-the-gate-into-a-vacuous-pass-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — independently verified against The-Reaver/The-Geo-Suite- at commit 73a58ced20783975bdf2269bc0a5319f60f672ef while the originating Architecture session was offline"
project: fleet
tags: [gates, hooks, geo, vacuous-pass, fail-closed, verification]
supersedes: []
superseded_by: the-installed-hook-gate-already-fails-closed-on-zero-declared-hooks-2026-08-31
---

# The installed-hook gate would pass vacuously on the GEO repo, because a glob installer names no hooks for a text parser to find

## Body

> **SUPERSEDED AND KNOWN-FALSE.** The vacuous PASS predicted below cannot occur:
> `run_gate()` already fails closed on zero declared hooks. See
> `the-installed-hook-gate-already-fails-closed-on-zero-declared-hooks-2026-08-31`.
> Retained only as the record of the error. **Do not ratify.**

The new `installed_hook_gate.py` failed against the GEO repo with *"installer not found at
`.../scripts/hooks/install-git-hooks.sh`"*. Verified against The-Geo-Suite- at
`73a58ce`: that path does not exist. GEO's layout is `scripts/install-git-hooks.sh` with
hook sources in `scripts/git-hooks/`. The gate had hardcoded the stag layout. **The
fail-closed behaviour was correct** — the bug is the path assumption, and the fix is
installer discovery, not downgrading a missing installer to a warning.

The deeper defect is what happens *after* that path fix. GEO's installer is a glob loop:

```bash
SRC="$REPO_ROOT/scripts/git-hooks"
for hook in "$SRC"/*; do
  name="$(basename "$hook")"; cp "$hook" "$DST/$name"; chmod +x "$DST/$name"
done
```

It names **no hook literally**. `installer_scripts_by_hookfile` (from
`hook_parity_gate.py`) is a text parser over the installer file, so it extracts zero
declared hooks — and the gate reports "0 declared hooks installed, executable, and
correctly wired": **PASS**, vacuously, on a repo with live hooks. That is verbatim the
condition the gate was built to make unreachable, reappearing inside the gate itself.

The structural cause: GEO declares its hooks as a **directory listing**, not as text in a
file. The gate models one declaration mechanism and there are two. For GEO the declared set
is `ls scripts/git-hooks/`, and since the installer copies hooks wholesale, the right
wiring assertion is a **content comparison against the tracked source** — a stronger check
than "references script X", and one that catches silent-disable exactly.

Also verified: GEO's `.git/hooks` carries `pre-commit` and `pre-push`, while
`scripts/git-hooks/` contains only `pre-commit`. GEO's pre-push is installed, undeclared
**and untracked** — the stag warning's class, one degree worse.

**Rule to adopt:** treat "zero declared hooks parsed" as a FAIL in its own right,
regardless of layout. A parser returning an empty set must never be reported as a clean
result.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: defence-in-depth-can-conceal-a-hole-in-the-rule-under-test-2026-08-31
- relates-to: built-not-connected-is-this-fleets-dominant-failure-mode-2026-08-31
