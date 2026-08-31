---
id: the-installed-hook-gate-already-fails-closed-on-zero-declared-hooks-2026-08-31
type: correction
status: candidate
source: "Resumed architecture session (session_01YPtX6tJPMqXJh1p8hUXGR8) reading installed_hook_gate.py directly on disk, 2026-08-31, refuting a prediction this recovery session made without file access"
project: fleet
tags: [gates, hooks, geo, false-block, correction, verification-discipline]
supersedes: [a-glob-installer-defeats-a-text-parser-and-turns-the-gate-into-a-vacuous-pass-2026-08-31]
superseded_by: null
---

# The gate never had the vacuous-pass hole — the real risk is the opposite, a permanent false block on GEO

## Body

The superseded note predicted that fixing the installer path alone would make
`installed_hook_gate.py` parse GEO's glob-loop installer to zero declared hooks and report a
vacuous PASS. **That was wrong.** `run_gate()` already contains an `if not declared:` branch
returning FAIL — *"parsed to ZERO declared hooks... an unperformed check is not a clean
check"* — covered by `test_unparseable_installer_fails_closed`. Confirmed empirically: GEO's
installer parses to `{}` and the gate fails closed. The rule the superseded note urged the
fleet to adopt had already been implemented before that note was written.

**The structural observation survives; the consequence inverts.** GEO genuinely declares its
hooks by directory listing (`scripts/git-hooks/`), and no text parser over
`scripts/install-git-hooks.sh` can ever satisfy it. So fixing installer discovery *alone*
moves GEO from "installer not found" to a **permanent, unfixable FAIL on a repo whose hooks
are correctly installed** — a false block, which by ratified precedent
(`2026-08-30-the-model-tier-gate-blocks-every-docs-only-commit`) is the more corrosive
failure, because it trains the override reflex. The operator has since ruled: the gate gets
two declaration mechanisms — heredoc parser for stag, directory-listing discovery for GEO,
with wiring verified by content comparison against the tracked source.

**The lesson worth keeping is about the reasoning, not the gate.** The prediction was made
from a brief's description of a parser plus a repo's installer, without reading the gate's
own source, because the source was on a machine this session could not reach. It was stated
with more confidence than that evidence carried, and it was the loudest claim in a handoff
another session was asked to act on. An agent reasoning about code it cannot open should
mark such a claim as a hypothesis to check first, never as a defect to fix — and the party
with disk access outranks the party with inference, every time.

## Links

- supersedes: a-glob-installer-defeats-a-text-parser-and-turns-the-gate-into-a-vacuous-pass-2026-08-31
- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
- relates-to: the-knowledge-core-is-forked-between-a-local-store-and-this-git-repo-2026-08-31
