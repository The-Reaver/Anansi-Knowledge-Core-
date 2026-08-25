# Delivery Lessons Corpus: Field Format and Ability Taxonomy

This is an original draft, built from scratch for this project. Treat every code and field
name here as a proposal that can be renamed, merged, or dropped.

## 1. Field format

Every corpus item uses this seven-field shape.

| Field | What goes here |
|---|---|
| Item ID | `<ABILITY>-<NNN>`, e.g. `VER-014`. Renumber freely once you have a real sequence. |
| Title | One line naming the specific failure or lesson, not the general category. |
| Ability | One code from the taxonomy below. |
| Situation | What the team was trying to do, and what happened instead. Two to four sentences. |
| Source | A real, working URL plus the publication date. If no real source exists for a lesson, the item is marked `Constructed` in the Situation field and the reasoning is your own, not attributed to an incident. |
| Lesson | The specific, transferable rule this incident teaches. Not "be careful," but the actual check or gate that would have caught it. |
| Cost | S / M / L, sized by blast radius and recovery time as described in the source. |

## 2. Ability taxonomy

Eight codes, each naming a distinct point where delivery work commonly fails.

**VER — Verification.** Confirming an artifact behaves correctly against real conditions, not against a mock, a stub, or a status code that only means "request accepted." A VER failure is a test or check that passed on a technicality while the real system was broken.

**ART — Artifact creation.** Producing the actual runnable, usable deliverable, as opposed to a plan, a stub, or a partial version. An ART failure is work that looks done but doesn't run, doesn't exist where it's supposed to, or was never actually built.

**REL — Release.** Getting finished work out of a branch and into the state where it counts: merged, deployed, communicated, and reversible. A REL failure is work that was completed but never landed, or landed without a way back out.

**REV — Review.** Independent evaluation of work by someone other than its author, before it moves forward. A REV failure is a review that happened in name only: rubber-stamped, skipped, or performed without enough context to catch a real problem.

**RAT — Ratification.** Final human sign-off on a decision or recommendation. This step is never automatable and never delegable to an AI system; the AI's job stops at producing a labeled, unratified recommendation. A RAT failure is a sign-off that happened without a real named person actually deciding, or that got treated as a formality.

**RCK — Recheck.** Confirming that a previously recorded fact, state, or approval is still true before relying on it again. An RCK failure is stale information trusted as current: an expired approval, a cache that was never invalidated, a claim nobody rechecked against the live system.

**REC — Recall.** Finding and reusing relevant prior work instead of missing it or duplicating it. An REC failure is redoing work that already existed, or missing a prior decision that should have changed the current one.

**FAI — Failure analysis.** Documenting a real breakage in enough detail that someone else can recognize the same pattern before it happens to them. This is not its own kind of work so much as a lens applied to the other seven: almost any VER, ART, REL, REV, RAT, RCK, or REC item can also carry a FAI tag when it's written up as a postmortem-style lesson rather than a how-to. FAI items must be sourced from a real incident, either your own team's history or a public postmortem; a FAI item with no real source is labeled `Constructed` and is treated as a lower-confidence teaching example, not as evidence.

## 3. Sourcing rule for FAI items

Real incident with a public writeup → cite it directly, with URL and date.
Real incident from your own team's history → cite the internal record (commit, ticket, doc) instead of a public link.
No real incident available → write the item as `Constructed`, keep it short, and don't attach false specifics like timestamps or quoted dialogue that never happened.
