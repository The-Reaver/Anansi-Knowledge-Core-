---
id: concurrent-session-pointer-drift-lesson-2026-08-31
type: lesson
status: candidate
source: this chat, 2026-08-31, discovered while working GeoSuite's AUDIT_AND_REPORTS_ROADMAP.md, fixed in The-Reaver/The-Geo-Suite- PR #6
project: fleet
tags: [concurrency, coordination, ledger-drift, geosuite, hand-maintained-pointer]
supersedes: []
superseded_by: null
---

# A hand-maintained "next free number" pointer is a shared mutable variable with no lock — expect it to drift the moment two sessions land work concurrently

## Body

GeoSuite's `AUDIT_AND_REPORTS_ROADMAP.md` tracks its own work-item numbering (S-1, S-2, ...) with a
plain sentence — "The next slice picked from this file should be numbered **S-N**" — plus a table
row marking that number "next free". This is exactly the same shape as an auto-increment counter,
but implemented as text in a markdown file that every session reads and hand-edits independently,
with no lock, no atomic increment, and no single writer.

**What happened, concretely:** this session's own S-48 fix correctly set the pointer to S-49 when
it closed S-48. In the same short window, a different concurrent session picked up a real slice
(talking-points selection/ranking), used S-49 for it, landed 5 real commits and merged them to
`main` — but never updated the pointer or the tracking table. The next time this session checked
GeoSuite's status, the roadmap was telling the truth about the past (S-48 done) and a lie about the
present (S-49 "next free," when it had already been fully spent). This is not a hypothetical risk:
the roadmap file's own `docs/build-ledger.md`-adjacent renumbering note already records exactly one
prior instance of the same failure ("this line previously said S-42, and by then three separate
S-42 commits already existed — someone will write a third S-42, and someone already had").

**The generalizable lesson:** any hand-maintained "next free identifier" pointer — a slice number, a
ticket counter, a migration timestamp convention, a note-id sequence — degrades from a source of
truth into a stale guess the moment more than one writer can advance the underlying state without
also updating the pointer in the same atomic action. It is not a one-time bug to fix; it is a
structural property of the mechanism. Two mitigations, neither applied here (both left as an
observation, not implemented in this pass):
1. **Detect drift instead of trusting the pointer** — before using a "next free" number, grep the
   codebase's actual history (`git log --all`) for any commit already claiming it, the same
   verification this session did before writing the pointer-fix note itself.
2. **Derive the number instead of hand-maintaining it** — a script that computes "next free" from
   real commit-message/file evidence at read time can't drift, because there is nothing to forget
   to update.

This applies wherever multiple concurrent sessions (this fleet's normal operating mode) touch a
shared hand-maintained sequence — not just GeoSuite's roadmap. Anansi's own note-id convention
(`<slug>-<date>`) sidesteps this specific failure by keying off content and date rather than an
incrementing counter, which is itself worth naming as *why* that convention was the right choice,
not just an arbitrary one.

## Links

- geosuite-s48-fix-2026-08-31 (this candidates folder) — the slice whose closure correctly set the
  pointer that then went stale
- knowledge-core-supersedes-link-ruling-2026-08-25 (notes/) — a related but distinct concurrency
  problem this Core already solved for itself (two sessions independently creating the same new
  candidate file), worth comparing mitigations against if this pattern recurs
