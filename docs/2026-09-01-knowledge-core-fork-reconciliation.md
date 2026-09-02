# Knowledge Core fork reconciliation — 2026-09-01

The Core exists in **two git repositories**. This is the first measurement of what each actually holds.

| | `The-Reaver/Anansi-Knowledge-Core-` | `Stag-Fleet/research/knowledge-home/` |
|---|---|---|
| ratified notes | **125** | **860** |
| candidates | **119** | **210** unique ids (211 files; the extra is a second `README.md`) |
| solutions / structure-notes / loop | 0 / 0 / 0 | 93 / 12 / 1 |
| corpus | 2 | 0 |

---

## Finding 1 — neither fork contains the other

This was the working assumption worth testing first, and it is false in both directions.

| | notes | candidates |
|---|---|---|
| **only in the Core** | **102** | **100** |
| only in the Fleet | 837 | 191 |
| present in both | 23 | 19 |
| **union of unique ids** | **962** | **310** |

**102 ratified notes exist only in `Anansi-Knowledge-Core-`.** Anyone treating the Fleet's
`knowledge-home/` as the corpus — which its 7× size invites — is working from a set that is missing 102
ratified notes, including the whole `2026-08-04`/`2026-08-05` ADLC and note-schema foundation.

## Finding 2 — of the 23 notes present in both, **all 23 differ**

Not one shared note is byte-identical. That sounds alarming and is not: the **bodies are identical**.
Every difference is in the header.

## Finding 3 — the real finding: each fork holds half of a complete note

Field coverage across every note in each fork:

| Field | Core (125) | Fleet (860) |
|---|---|---|
| `status` | **100%** | 84% |
| `project` | **100%** | 47% |
| `supersedes` | **100%** | 0.2% |
| `superseded_by` | **100%** | **0%** |
| `risk_class` | **0%** | **89%** |
| `evidence_state` | **0%** | **89%** |
| `next_review` | **0%** | **89%** |
| `classified` | **0%** | **89%** |
| `source_rating` | **0%** | **79%** |

The two forks are **complementary and almost perfectly disjoint**:

- The **Core** carries the ratification status and the supersede chain, and **no evidence
  classification at all**.
- The **Fleet** carries the Evidence Standard §7/§9 classification, and **no supersede chain at all**.

A worked example, `2026-08-04-anansi-ledger-real-red-green-proof-not-yet-run.md` — same body, verbatim,
in both:

| | Core | Fleet |
|---|---|---|
| dialect | YAML frontmatter | `- key: value` bullets |
| `status` | `ratified` | `active` |
| supersede chain | present | absent |
| `risk_class` / `evidence_state` / `next_review` / `classified` | absent | `B` / `SUPPORTED` / `2027-02-25` / `2026-08-29` |

**A merge in either direction silently destroys data.** Copying the Fleet over the Core loses 125
ratification records and every supersede link. Copying the Core over the Fleet loses ~767 evidence
classifications. The only non-destructive merge is a **field-level union**, not a file-level pick.

## Finding 4 — I deepened this divergence, in this session

The fork predates me, but two workstreams I ran on **opposite sides** are exactly the two columns above:

- the **supersede backfill** — 166 files, 331 insertions, 0 deletions — applied to the **Core**;
- **Evidence Standard Pass One** — 230 files classified — applied to the **Fleet**.

Each was correct work. Run on opposite sides of an unreconciled fork, they turned a size difference into
a *schema* difference, and neither repo can now be restored from the other. **The lesson generalises past
this repo: parallel improvement on unreconciled forks does not average out — it compounds into mutual
irreplaceability.**

## Finding 5 — dialects

The Core is **100% YAML frontmatter**. The Fleet is **402 YAML / 458 bullet** — a near even split, and the
bullet dialect is the one carrying most of the Evidence Standard fields. Any merge tool must read both.

---

## The merge rule this analysis supports

Field-level union, per note id, with these precedences:

| Field | Winner | Why |
|---|---|---|
| body | either (identical on all 23 checked; **verify per note, do not assume**) | |
| `status` | **Core** | `ratified` is a deliberate record produced by a hard-gated process (mandate `ratification`); the Fleet's `active` is the pre-ratification default. Never downgrade a ratified note. |
| `supersedes`, `superseded_by`, `project` | **Core** | the Fleet has effectively none |
| `risk_class`, `evidence_state`, `next_review`, `classified`, `source_rating` | **Fleet** | the Core has none |
| dialect | **YAML** | the Core's is uniform; the Fleet's split is the legacy |

Two rules that are not negotiable, because both have already bitten this fleet:

1. **Parse before and after, assert equality on every field not being changed.** This is the guard that
   made the 166-file supersede backfill safe (0 reverts).
2. **`evidence_state` never becomes `SETTLED`** during a merge, and `status` is never downgraded.

## What is NOT decided here, and is the operator's call

**Which repository is canonical.** That decision governs the merge direction, where future notes land,
and what the `anansi` skill reads. It is an architecture decision with a live blast radius — 962 note ids
— and it is not mine to make. The options are: promote the Core (smaller, cleaner schema, better
governance metadata), promote the Fleet (7× the content, better evidence metadata), or keep both with a
declared sync direction.

**Nothing has been merged.** This document is measurement only. No note in either repository was
modified by this reconciliation.

| # | Next | Owner |
|---|---|---|
| F1 | Decide the canonical repository. | operator |
| F2 | Verify body-identity across all 23 shared notes before any union, and re-run the check at merge time. | agent |
| F3 | Build the merge as a script with a parse-before/parse-after equality guard, dry-run first, diff reviewed before it writes. | agent |
| F4 | After merging, one repo becomes a mirror with a declared sync direction, or the fork re-diverges within a week. | operator + agent |
