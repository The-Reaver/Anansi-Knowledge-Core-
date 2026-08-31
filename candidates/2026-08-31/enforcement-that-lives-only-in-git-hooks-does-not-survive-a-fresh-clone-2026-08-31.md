---
id: enforcement-that-lives-only-in-git-hooks-does-not-survive-a-fresh-clone-2026-08-31
type: finding
status: candidate
source: "Recovery session, 2026-08-31 — observed directly: this repository, freshly cloned into a cloud container, had an empty .git/hooks with only samples"
project: fleet
tags: [git, hooks, enforcement, fresh-clone, ci, safeguards]
supersedes: []
superseded_by: null
---

# Every gate in this fleet is off by default, because .git/hooks is not tracked by git

## Body

Observed directly rather than inferred: the Knowledge Core repository, cloned fresh into a
cloud container, has an **empty `.git/hooks/`** — nothing but git's own `.sample` files. Every
mandate gate, secret check, ratification gate and attribution trailer this fleet has built is
therefore inert in that checkout, silently, from the first commit.

This is not a bug in any hook. `.git/hooks/` is never tracked by git, by design. It follows
that hook-based enforcement is **opt-in per clone, per worktree, per machine** — a fresh
clone, a new laptop, a cloud session, a CI runner and a linked worktree each start with zero
enforcement until someone remembers to run the installer.

Three consequences worth stating plainly. Enforcement measured on the machine where the hooks
were installed says nothing about anywhere else. `--no-verify` is not the main bypass; *not
installing* is, and it needs no intent. And a cloud session — which cannot run the installer
against a container it does not control — is structurally the least protected place work
happens, while looking identical to a protected one.

**Verified on the fleet repo too:** `Stag-Fleet/.claude/settings.json` declares **zero
hooks** -- `hooks` is empty. Whatever session hook warms the Core or captures transcripts
lives in one machine's *user* settings, not in the repository, so no clone and no cloud
session inherits it. Enforcement and capture both depend on one machine's local
configuration.

**The only durable fix is a CI backstop** running the same checks server-side, where no clone
can opt out. Hooks are a fast local convenience; CI is the enforcement.

## Links

- relates-to: safeguard-existence-does-not-imply-invocation-2026-08-31
- relates-to: geo-pushes-straight-to-main-with-no-staging-environment-2026-08-31
- relates-to: a-glob-installer-defeats-a-text-parser-and-turns-the-gate-into-a-vacuous-pass-2026-08-31
