---
id: geosuite-build-ledger-ruling-2026-08-25
type: ruling
status: ratified
source: "Operator decision on the concretized geosuite-build-ledger-proposal-2026-08-25, requested directly in an Anansi Knowledge Core session, 2026-08-31"
project: geo
tags: [geosuite, build-ledger, site-generator, ruling, enforcement]
supersedes: [geosuite-build-ledger-proposal-2026-08-25]
superseded_by: null
---

# Approved: GeoSuite gets a build-ledger, on the condition enforcement is a real gate, not a "fold it in" hope

## Body

**Decision: approve**, on the terms the concretized proposal laid out, with one binding
condition on enforcement.

**Why approve, given the fleet's own bias against speculative process.** The proposal's
two example entries aren't hypothetical — they're two real, already-paid-for production
bugs (a page shipping without its persistence half; a hero-image reference only 9 of 10
theme files actually got). This isn't "process for a problem that might happen." It's
the second time the same class of mistake has cost real rework, which is exactly the bar
this Core's own founding rule ("recall before you guess, capture after you learn") exists
to clear. The trigger is also genuinely narrow — a hidden coupling, a wrong count once
checked, or a gap no existing test would catch, not "every fix" — so the recurring cost
this ruling accepts is bounded, not open-ended.

**Storage location is correct as proposed.** The authoritative copy belongs in
`The-Reaver/The-Geo-Suite-/docs/build-ledger.md`, not primarily here. A ledger only
reachable from a repo most GeoSuite sessions can't see fails at the one job it has — this
is the same reasoning that put `raw/` archives in this repo rather than assuming a
disconnected session could always reach some other store. An optional cross-reference
note here (`project: geo`) is fine as a secondary index, never the primary copy.

**The one condition: enforcement must be a real gate at the moment this ships, not a
someday-fold-in.** The proposal's own enforcement answer was "fold into the
adversarial-review pass" — worded as an intention, not a wired-in check. A convention a
reviewer has to remember to apply is a convention that erodes the first time a reviewer is
rushed. So: whoever implements this must, in the same change, add the ledger-trigger
question as a literal checklist line in whatever governs GeoSuite's adversarial-review
pass — not merely reference it in prose. Until that line exists, the ledger is a place to
write things down, not an enforced gate, and should be described that way.

**What this ruling does not do.** It does not create `docs/build-ledger.md` or touch the
`The-Reaver/The-Geo-Suite-` repo — that repo may have another session active in it, and
doing so is out of scope for a session working in the Anansi repo. This ruling closes the
open design question; building it is a separate, concrete follow-up:

1. Create `The-Reaver/The-Geo-Suite-/docs/build-ledger.md`, seeded with the two entries
   already named in the superseded proposal (the `_persist()` glob coupling; the 9-of-10
   hero-theme miss), in the `Files: <file> (<function>)` format the proposal specified.
2. Add one pointer line to that repo's own `CLAUDE.md` directing agents to the ledger
   before touching site-generator internals.
3. Add the ledger-trigger checklist line to the adversarial-review pass GeoSuite fixes
   already go through.

## Links

- supersedes: geosuite-build-ledger-proposal-2026-08-25
- relates-to: 2026-08-07-site-generator-mirrors-build-methodology
- relates-to: skill-eval-gate-2026-08-25
