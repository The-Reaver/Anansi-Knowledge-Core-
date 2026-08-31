---
id: pre-push-ignores-unknown-arguments-so-a-typo-silently-downgrades-it-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — VERIFIED directly against The-Reaver/Stag-Fleet at branch anansi-home-dashboard (b19dd5f), cloned and inspected; originally relayed from the capability audit and since confirmed in prepush.py"
project: fleet
tags: [pre-push, cli, silent-failure, security-gate, argument-parsing]
supersedes: []
superseded_by: null
---

# A misspelled flag turns the pre-push security gate non-blocking, and says nothing

## Body

**Verified in `prepush.py`.** Argument handling is three lines: `argv = sys.argv[1:]`, then
`fast = "--fast" in argv` and `strict = "--strict" in argv`. Pure membership tests, so any
unrecognised token is discarded silently. The only `sys.exit(2)` guards `--fast` and
`--strict` being combined; nothing rejects an unknown flag.

**One refinement to the original claim.** The blocking stage -- staged secrets and stray
`.env` files -- is documented in the file as failing CLOSED and still runs. What a typo
silently costs is the *strict* mode in which a red `verify.py` exits 1; in default mode the
test suite is advisory, printing "Re-run with `--strict` to make this exit 1". So `--stict`
does not disable the secret scan, it downgrades test-blocking to advisory -- narrower than
"runs non-blocking", and still a silent downgrade of a gate the operator believes is strict.

The pre-push gate ignores arguments it does not recognise. Passing `--stict` instead of
`--strict` does not error — the gate runs in its permissive, non-blocking mode and reports
success. The operator sees a green push and believes strict enforcement ran.

A single transposed character silently downgrades a security control, and every downstream
assurance inherits the downgrade. Nothing distinguishes this from a genuinely clean strict
run, so the failure is undetectable from the output alone and can persist indefinitely.

**Reject unknown arguments.** This is a two-line change and it converts a silent, permanent
downgrade into an immediate, obvious error. The general form: a security tool must fail on
input it does not understand, never proceed in a weaker mode. Permissive argument parsing is
appropriate for convenience tools and actively dangerous for gates, because the whole point of
a gate is that its state is trustworthy without inspection.

**Check next time any gate or scanner takes flags:** confirm that an unrecognised flag is an
error, and that the strict mode you think you are running is named in the output rather than
assumed.

## Links

- relates-to: a-gate-that-does-not-declare-fail-open-or-fail-closed-cannot-be-audited-2026-08-31
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
