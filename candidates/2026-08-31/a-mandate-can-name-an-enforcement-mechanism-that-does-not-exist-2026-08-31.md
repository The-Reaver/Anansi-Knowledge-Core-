---
id: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — VERIFIED directly against The-Reaver/Stag-Fleet at branch anansi-home-dashboard (b19dd5f), cloned and inspected; originally relayed from the capability audit and since confirmed in governance/mandates.json and scripts/gates/mandates_gate.py"
project: fleet
tags: [governance, mandates, enforcement, verification, registry]
supersedes: []
superseded_by: null
---

# Nothing checks that a mandate's declared enforcement mechanism actually exists

## Body

**Verified.** `governance/mandates.json` holds **28 mandates, all 28 carrying a `mechanism`
field**. Seventeen are honest prose -- "Agent-contract; not machine-gatable" -- which is
creditable. Of the **eleven that name an actual file, ten of those named files do not exist**
on the branch: `master-todo.md`, `brain-trust-on-demand-protocol.md`, `GEO_DEVELOPMENT_LOG.md`,
two `research/knowledge-home/candidates/2026-08-09/...` notes, and several `CLAUDE.md` paths
including `/Users/abadm/.claude/CLAUDE.md` -- a **macOS** path in a fleet running on Windows.

**And `mandates_gate.py` never reads the `mechanism` field at all.** It checks that the
registry parses, that rules are non-empty, that six governance law files exist, that specs
carry a compliance section, and that two allowlists keep their honesty-disclosure lines.
Enforcement claims themselves are unchecked.

Each mandate in `governance/mandates.json` declares a `mechanism` — the script or hook that
enforces it. **Nothing verifies that the named thing exists**, is installed, or runs. The
registry is a set of claims, and a claim that stops being true does so silently.

This is not hypothetical: `sdlc-model-tiering`'s enforcement claim was fiction for days
before anyone noticed. The mandate said it was enforced; the enforcement was not reachable;
every gate passed.

This is the governance-layer form of the same defect found in the gate battery — a safeguard's
existence taken as proof it runs. Here it is worse, because a mandate is the fleet's highest
authority: a mandate whose mechanism is fictional does not merely fail to enforce, it
**licenses the belief that the rule is covered**, which stops anyone looking.

**The fix is a gate asserting each mandate's `mechanism` names something real** — script
present on disk, hook installed and executable, invoked by something. Register no mandate
whose mechanism cannot be resolved, and fail the gate rather than warn: an enforcement claim
that cannot be checked is not a weaker claim, it is an unverified one.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
- relates-to: a-false-block-destroys-a-gates-authority-and-takes-its-true-positives-with-it-2026-08-31
