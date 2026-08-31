---
id: a-mandate-can-name-an-enforcement-mechanism-that-does-not-exist-2026-08-31
type: finding
status: candidate
source: "Architecture session (session_01Q1wJW3McyXVkdvLjvLVKmy) capability audit, 2026-08-31 — relayed by the operator into a recovery session; observed on the operator machine and NOT independently re-verified here"
project: fleet
tags: [governance, mandates, enforcement, verification, registry]
supersedes: []
superseded_by: null
---

# Nothing checks that a mandate's declared enforcement mechanism actually exists

## Body

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
