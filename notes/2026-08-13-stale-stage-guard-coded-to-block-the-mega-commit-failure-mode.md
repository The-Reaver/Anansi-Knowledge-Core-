---
id: 2026-08-13-stale-stage-guard-coded-to-block-the-mega-commit-failure-mode
type: decision
status: ratified
ratified: "2026-08-13, operator instruction, direct re-verification by this session's Claude; the gate was run live against the real incident's staged file set before landing, not just reasoned about"
project: fleet
tags: [fleet, git, governance, code-the-rule, mandate-coded-not-remembered, pre-commit-hook]
sources:
  - ref: "scripts/gates/stale_stage_guard.py, .pre-commit-config.yaml, scripts/hooks/install-git-hooks.sh"
    reliability: high
    origin: written and wired this session
  - ref: "python scripts/gates/stale_stage_guard.py --root . run against the real 538-file staged incident set"
    reliability: high
    origin: run live, this session, correctly flagged 513/538 files, 48 directories, 90% stale
  - ref: "python scripts/gates/hook_parity_gate.py --root . confirming both hook-declaration files stayed in sync"
    reliability: high
    origin: run live, this session
provenance:
  archive: research/knowledge-home/raw/2026-08-12-geo-poller-fix-and-platform-identity-session.jsonl
  turns: [1, 30]
risk_class: B
evidence_state: CORROBORATED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# A new pre-commit gate, stale_stage_guard.py, blocks the exact accidental-mega-commit failure mode found and recovered from the same day

## Body

Matches the fleet's own standing instruction, given verbatim in an earlier session and re-invoked
here in spirit: "these cannot be notes or documentation alone this must be coded" / "call rules
mandates and laws that I institute are to be coded." The operator did not ask for a written
reminder to be more careful; they asked for something that mechanically stops the failure from
happening again, and that is what got built.

**What it checks, every commit:** the staged file set (`git diff --cached --name-only
--diff-filter=ACMR`). Passes silently, always, for anything that looks like one coherent piece of
work. Only raises a flag when the staged set looks like an accidental sweep-in of unrelated,
previously-staged content -- more than 25 files staged, AND either spanning more than 4 top-level
directories or more than half the files carrying an on-disk mtime older than 6 hours. Old files
riding into a fresh commit is exactly the signature of stale staged content, since a genuinely fresh
piece of work was, by definition, just written.

**Deliberately a speed bump, not a wall:** a real, deliberate, wide commit still happens in this
fleet sometimes (cited directly in the gate's own docstring -- commit `2668967`, "a single clean
drop" landing 41 files across several directories in one intentional batch). An explicit override,
`ALLOW_STALE_STAGE_COMMIT=1`, skips the check for a genuinely deliberate wide commit and prints a
confirmation line so the override is visible in the hook's own output, not silent.

**Verified against the real incident before landing, not just unit-tested in the abstract:** run
directly against the actual staged set from the mega-commit this same day produced -- correctly
flagged 513 of 538 files, spanning 48 top-level directories, 90% with a stale mtime. This is the
same discipline the fleet already applies to test claims generally (a claim is worthless without a
reproducible command against the real thing it's about, not a synthetic stand-in).

## Links

- extends, 2026-08-13-git-add-does-not-reset-the-index-a-stale-staged-backlog-can-ride-along-into-any-commit.md
  -- the finding this gate exists to prevent from recurring.
- depends, `scripts/gates/hook_parity_gate.py` -- the existing gate that already enforces
  `.pre-commit-config.yaml` and `install-git-hooks.sh` never drift apart; the new gate had to be
  added to both files in the same change or this one would have failed the commit.
