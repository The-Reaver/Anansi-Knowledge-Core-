# Handoff — Architecture session, 2026-08-31

**Read this first if you are resuming the work of `session_01Q1wJW3McyXVkdvLjvLVKmy`
("you will focus on Architecture.").** It is written to be sufficient on its own: a fresh
session should be able to continue from this document without the original transcript.

Written by a recovery session (`session_01AtFDi8YZ1Sos5nHp4K591q`) on 2026-08-31 while the
originating session was unreachable.

Everything below is marked **[verified]** (checked directly by the recovery session) or
**[relayed]** (reported by the original session and not independently re-checked). Do not
promote a relayed claim to fact without checking it.

---

## 1. Why the original session cannot simply be resumed

**[verified]** The session is bound to bridge environment `env_012jZoxRLYnByvZScLynLPTE`,
registered as `DESKTOP-4UC2LTP:C:\Users\abadm\stag:5229`, created 2026-08-31T00:49:17Z.

When Remote Control was restarted, it did **not** re-register that environment. It minted a
new one: `env_012ucNq3chGWrSyqca579uQJ`, registered as
`DESKTOP-4UC2LTP:C:\Users\abadm\stag:d218`, created 2026-08-31T14:21:26Z. Same machine, same
working directory, **different instance token** (`5229` → `d218`).

The session is pinned to the old environment id. No host answers for it any more, so the
session's `last_init_error` stays frozen at `computer_unreachable` / 2026-08-31T13:42:24Z —
no new connection attempt is even being recorded. Restarting Remote Control again will not
help; each restart mints another new environment.

Two consequences:

- Reconnection in place would require the host to re-register under the *original*
  identity. If the trailing token is a port, starting the host bound to `5229` may achieve
  that. Untested, and not guaranteed.
- Otherwise the recovery path is a **new session on the current environment**
  (`env_012ucNq3chGWrSyqca579uQJ`), resuming from this document.

The original session's transcript remains readable server-side either way. Nothing was lost;
it is the live binding that is stale, not the record.

## 2. The decision the session was blocked on

**[verified]** It stopped because it was waiting on the operator, not because it crashed.
Status is `REQUIRES_ACTION` / `BLOCKED`, on this question:

> Google Drive is authorized, but there's no local Drive folder to write backups into.
> How should `backup_fleet.py` get 40MB of bundles to Drive?

1. **Install Drive for Desktop (recommended by the original session)** — creates a real
   folder; `backup_fleet.py` writes there, a one-constant change matching the working
   OneDrive setup. The Drive connector then verifies cloud-side that each bundle arrived,
   closing the sync-unconfirmed gap OneDrive never had.
2. **rclone** — scriptable, resumable, no desktop client; one more tool to maintain.
3. **MCP connector only** — no install, but 40MB base64 through context is fragile and
   cannot be scheduled.
4. **Keep local backups, Drive later** — leaves the backups on the disk they protect, which
   is the exposure the item exists to close.

**This is still open and is the operator's call.** A resuming session must ask it again
rather than assume an answer.

## 3. State of the in-flight implementation

**[relayed]** The IMPLEMENTATION seat (per `sdlc-model-tiering`, implement-only, no
self-review) was building an installed-hook verification gate against
`reports/BRIEF_R1_INSTALLED_HOOK_GATE_2026-08-31.md`.

Location: `C:\Users\abadm\stag\.claude\worktrees\installed-hook-gate-impl` — a worktree on
the operator's local disk. **Uncommitted.** This is the single most exposed artifact of the
session; the recovery session could not reach it.

- `installed_hook_gate.py` — 292 lines
- `test_installed_hook_gate.py` — 385 lines
- 24/24 tests passing, including the mutation test targeting the silent-disable assertion

Live run against the stag repo main checkout: **PASS**, with the first real catch the brief
predicted — `pre-push` installed in `.git/hooks` but not declared by
`scripts/hooks/install-git-hooks.sh`, surfaced as WARN, not FAIL. Correct behaviour. Per the
brief, adding `pre-push` to the installer is a **separate reviewed change** — do not fix it
here.

Live run against the GEO repo: **FAIL** — `installer not found`. See next section.

## 4. The GEO failure — diagnosed, with a second defect behind it

> **CORRECTION, 2026-08-31, from the resumed session with direct disk access.** Defect 2 as
> originally written below is **WRONG** and must not be acted on as stated. `run_gate()`
> already contains an `if not declared:` branch returning FAIL ("parsed to ZERO declared
> hooks... an unperformed check is not a clean check"), covered by
> `test_unparseable_installer_fails_closed`. The vacuous PASS predicted below **cannot
> occur**, and the rule this document told you to adopt was already implemented before it
> was written. Confirmed empirically: GEO's installer parses to `{}` and the gate fails
> closed.
>
> The structural cause below still holds — GEO declares hooks by directory listing, and no
> text parser can ever satisfy it — but the consequence runs the **opposite** way. Fixing
> installer discovery *alone* moves GEO from "installer not found" to a **permanent,
> unfixable FAIL** on a repo whose hooks are correctly installed: a false block, which by
> ratified precedent (`2026-08-30-the-model-tier-gate-blocks-every-docs-only-commit`) is the
> more corrosive failure.
>
> Also superseded below: the test file is **386** lines, not 385; the stag run is now
> **[verified]**, not [relayed]; the worktree is **intact**; and GEO's HEAD has moved from
> `73a58ce` to `a428c6a` (both defects still reproduce there).
>
> **Operator rulings since:** Drive for Desktop for backups; and the gate gets **two
> declaration mechanisms** — heredoc parser for stag, directory-listing discovery for GEO,
> with wiring verified by content comparison against the tracked source.


**[verified]** against `The-Reaver/The-Geo-Suite-` at commit
`73a58ced20783975bdf2269bc0a5319f60f672ef`.

**Defect 1 — path assumption.** The gate looked for `scripts/hooks/install-git-hooks.sh`.
That is the *stag* layout and does not exist in GEO. GEO's layout is
`scripts/install-git-hooks.sh` with hook sources in `scripts/git-hooks/`.

The fail-closed behaviour was **correct** and must be preserved. Fix this with installer
discovery. Do **not** downgrade a missing installer to a warning — that reintroduces exactly
the failure mode the brief cites (`deploy_verify.py`'s migration check sitting useless for
weeks).

**Defect 2 — the serious one.** GEO's installer is a glob loop:

```bash
SRC="$REPO_ROOT/scripts/git-hooks"
for hook in "$SRC"/*; do
  name="$(basename "$hook")"; cp "$hook" "$DST/$name"; chmod +x "$DST/$name"
done
```

It names **no hook literally**. `installer_scripts_by_hookfile` (from
`hook_parity_gate.py`, ~line 71) is a text parser over the installer file, so after the path
fix it will extract **zero** declared hooks and the gate will report *"0 declared hooks
installed, executable, and correctly wired"* — **PASS, vacuously**, on a repo with live
hooks.

That is verbatim the condition the gate exists to make unreachable, reappearing inside the
gate itself. Structural cause: GEO declares hooks as a **directory listing**, not as text in
a file. The gate models one declaration mechanism; there are two. For GEO the declared set is
`ls scripts/git-hooks/`, and since the installer copies hooks wholesale, the correct wiring
assertion is a **content comparison against the tracked source** — stronger than "references
script X", and it catches silent-disable exactly.

~~**Adopt as a rule:** "zero declared hooks parsed" is a **FAIL** in its own right.~~
**Already implemented** — see the correction at the top of this section.

**Also verified:** GEO's `.git/hooks` holds `pre-commit` and `pre-push`, while
`scripts/git-hooks/` holds only `pre-commit`. GEO's pre-push is installed, undeclared **and
untracked** — the stag warning's class, one degree worse. Surface it; do not fix it here.

## 5. What has already been captured to the Knowledge Core

**[verified]** 19 candidate notes on branch `claude/architecture-session-offline-akvxza` of
`The-Reaver/Anansi-Knowledge-Core-`, in `candidates/2026-08-31/`. All `status: candidate`.
**None have been ratified** — that is the operator's pass, per the README.

Twelve from the session's own defects and rulings: the `refs/stash` backup false green;
`git bundle verify` passing on a corrupt bundle; the prune list that would have blinded the
secret scanner; three misattributions root-caused to git recording no session identity; why a
false block destroys a gate's authority; the 29-day stale lock; four safeguards invoked by
nothing; mutation tests passing under defence in depth; BEDROCK/Jicome missing from the Core;
the glob-installer vacuous pass; built-not-connected as the dominant failure mode; and the
expected-result-restates-the-problem defect.

Seven from the dormant-area audit: STARS/DREAMS blocked on the 9-Gate routing question;
curriculum stocked with no evidence its resume loop runs; the operator dashboard's teaching
half never specced; the language library queued and unscoped for 28 days; the SiteGen design
system as the one area whose mechanism demonstrably runs; the Amaya fold step that has never
executed; and the local/git Core divergence.

Validated: YAML parses, ids match filenames, no dangling links, no duplicate ids across 203
corpus ids.

## 6. A finding that changes how you should search

**[verified]** The Core is **forked**. Four of five note ids the dormant-area audit cited do
not exist in the git repo; the fifth is only an unratified candidate. The audit was searching
the operator's **local Knowledge Home** at `C:\Users\abadm\stag\research\knowledge-home\`,
which ADR-0005 names and which the STARS/DREAMS candidate confirms is where notes are
written. The git repo holds 125 ratified plus 71 candidates — a **partial mirror**.

So "the Core does not hold X" is only true of whichever store was searched, and a cloud
session can reach only the git one. **Name the store whenever you report an absence.**
Reconcile the two stores before trusting any absence-based conclusion, and expect the
dormant-area notes above to have local duplicates — the README says link to the existing
note rather than ratify a second copy.

## 7. What is NOT captured

- **The gate implementation itself.** Still only on local disk, uncommitted. Highest risk.
- **No `raw/` archive for this session.** Only a relayed excerpt was available, not
  turn-by-turn JSONL. Writing a partial archive into an append-only store that declares
  itself the ultimate source of truth would poison it. This is a live instance of the cost
  ADR-0005 names.
- **The 20-item plan and the 11-capability action table** — deliberately not frozen. Three
  exploration agents (capture machinery, review machinery, six dormant areas) had not landed,
  and the operator was explicit about preferring to know over guessing. Their results are
  lost with the session unless re-run.
- **Per-area detail for the dormant areas** beyond what section 5 lists.

## 8. Constraints still binding

From the original brief, unchanged:

- Work in a worktree under `.claude/worktrees/`.
- Do **not** commit, push, or wire the gate into any hook or config.
- Do **not** modify `hook_parity_gate.py`, `install-git-hooks.sh`, any existing hook,
  `verify.py`, `prepush.py`, `security/secret_scan.py`, or `security/secret_scan_baseline.json`.
- No `git clean`, `reset --hard`, `gc`, `prune`, `worktree remove/prune`, or force push.
- Never print a secret.
- `governance/PREFLIGHT_SAFETY_DISPATCH_v1.0.md` is binding for every git operation.
- Implementation seat does not self-review.

## 9. Suggested order on resume

1. Confirm the worktree at `.claude\worktrees\installed-hook-gate-impl` is intact and the
   24 tests still pass. Nothing below matters if that work is gone.
2. Put the Drive question (section 2) back to the operator.
3. Decide whether the glob-installer finding changes the gate's design **before** writing the
   handback. A gate that can report a vacuous pass is not finished.
4. Fix installer discovery; add the zero-declared-hooks FAIL; re-run against both repos.
5. Write the handback per the brief, with both live runs pasted verbatim, and an explicit
   statement of what remains unproven.
6. Ratify or reject the 19 candidate notes — after reconciling against the local Knowledge
   Home, not before.
7. Re-run the three exploration agents if their results are still wanted.

## 10. Open questions

- Is the operator's remembered "Bedrock as a personal learning dashboard" the same idea that
  became Jicome (a children's learning platform), or two things sharing a codename? This
  decides extend-versus-build.
- Does the 9-Gate model replace the ratified STARS/DREAMS TRL 1–9? Sent to the Brain Trust
  2026-08-08; no resolution recorded. One decision gating an entire designed system.
- Should the session-attribution trailer carry a model identifier? The recovery session used
  a plain `Co-Authored-By: Claude` trailer; if `session_attribution_trailer.py` or the tier
  gate expects the model name, these commits will not match.
