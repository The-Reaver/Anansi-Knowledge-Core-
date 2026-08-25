---
id: 2026-08-25-9-gate-brain-trust-verdict
type: ruling
status: candidate, pending operator ratification
source: >
  this chat, running the fleet deliberation process the operator specified in
  `2026-08-08-heavy-chat-handoff-addendum-routing.md` ("let the brain trust and AJ render the
  verdict... individual investigations, table deliberations, debate, vote, verdict. follow the
  mandate"). Multi-agent workflow: 4 independent investigations, 3 position cases, 3 rebuttal
  rounds, 4 independent votes, 1 synthesis. Vote: hybrid-or-other, 4-0.
project: fleet
tags: [brain-trust, ruling, 9-gate, stars-dreams, fleet-leveling, mandate-7, mandate-1]
---

# Brain Trust candidate verdict: the 9-Gate model is neither a replacement for STARS.docx nor a parallel system to FLEET_LEVELING — it becomes the fleet's single onboarding/graduation ladder, with both existing systems repositioned around it

## Body

## Verdict

The Brain Trust's candidate ruling is **hybrid-or-other**, by a vote of 4-0. All four judges converged on this position after the rebuttal round.

The 9-Gate proposal does not replace STARS.docx, and it does not stand up as a second, independently-scored fleet-wide system next to FLEET_LEVELING. Instead: 9-Gate becomes the fleet's single fleet-wide onboarding/graduation ladder — the sequential, externally-verified answer to "is this agent cleared to operate, and at what checkpoint." STARS.docx is left untouched and remains the sole authority on Augustin's CTO-training competency depth. FLEET_LEVELING is redefined as a coarse, non-authoritative label *derived from* Gate status, rather than a second system scored independently and reconciled by policy.

## Reasoning

The deliberation tested three positions against each other through investigation, debate, and two rebuttal rounds. Two of the three broke down under direct examination; hybrid did not.

**Replace-stars failed on its own central claim.** Its argument that a 9-Gate system could absorb STARS's floor cap and ceiling-durability discount as "one axis, hardened" rather than a new multi-axis apparatus was, by its own author's admission, "the single most contestable claim in the entire case" — and it was never resolved. Once each gate has to clear an external capability threshold (METR/DeepMind), a governance-maturity bar (NIST/ISO/OWASP), *and* the existing SDLC-phase floor simultaneously, that is arguably more stacked dimensions per level than STARS's original composite, not fewer — closer to the fuller TRL/IRL/SRL matrix the Brain Trust already rejected as disproportionate, not further from it. Its retreat to an Augustin-only scope also created a new problem: an asymmetric one-agent exception, with Augustin alone running on Gate-status while the rest of the fleet stays on FLEET_LEVELING untouched. That is not a reduction of fragmentation; it is a new, narrower kind of it. And it asks the Brain Trust to retire an already-ratified document on the strength of an unbuilt promise — that Augustin's SDLC-phase rubrics can be faithfully reproduced gate-by-gate — rather than verifying that equivalence before asking for the retirement.

**Layer-on-fleet-leveling made the strongest case for leaving STARS alone, but never solved the problem it set out to solve.** Its own revised position concedes, without qualification, that Augustin would permanently carry three independently-scored systems — STARS, FLEET_LEVELING, and Gate — held in alignment only by a crosswalk table and an authority rule that must be hand-drafted, hand-ratified, and hand-maintained. That is exactly the fragmentation scenario the operator's own brief warned against, reproduced in full by the position's preferred design. Its proposed tie-break (FLEET_LEVELING governs deployment decisions, Gate governs graduation claims, and the two may legitimately disagree) is institutionalized ambiguity, not a resolved crosswalk — a treaty between two live, independently-scored systems that can drift every time either one changes.

**Hybrid won by supplying a sharper, falsifiable test and passing it: count the independently-scored systems per agent, going forward.** Under hybrid, Augustin carries exactly two (STARS, untouched and still authoritative on CTO depth; Gate, fleet-wide) — and the fleet in general carries exactly one independently-scored axis (Gate), because FLEET_LEVELING is redefined as derived rather than tracked in parallel. This is drift-prevention by construction, not by treaty: there is nothing on the other side of the crosswalk to fall out of sync, because nothing else is independently scoring the same territory. Hybrid also revised itself in direct, responsive terms across the rebuttal round — most notably by keeping Gate a standalone, externally-citable ladder ("cleared Gate 6, externally verified") rather than burying gate criteria inside FLEET_LEVELING's internal stage-transition rules, which was layer's strongest objection and which hybrid answered rather than dismissed.

## Disposition of the two existing systems

**STARS.docx**: unchanged. Its weighted 0-100 composite index, weakest-link floor cap, ceiling-durability discount, ratified status, and live tracking via the augustin-dreams-tracker artifact all remain exactly as ratified. STARS is not merged into, reinterpreted by, or made subordinate to 9-Gate. It gains only a citation noting that Augustin's fleet-wide onboarding/graduation status is separately tracked via Gate, with STARS explicitly named as the sole authority on his CTO-training competency depth.

**FLEET_LEVELING_2026-08-01.md**: its four stage names (Seed → Designed → Active/Beta → Alpha) survive, but its status changes — it becomes a coarse, non-authoritative summary label *derived from* Gate status rather than an independently-scored fleet-wide system in its own right. This requires, before ratification (not after, as a follow-up):
- a gate-range-to-label crosswalk table, with explicit acknowledgment that 9 does not divide evenly into 4 and any mapping is a deliberate design choice, not a natural one;
- confirmation, checked rather than assumed, of whether FLEET_LEVELING's four stages currently carry documented per-transition criteria — if they do, Gate's value-add is real but narrower than "filling an empty gap," and the ratified document must say so;
- a documentation convention that gate stages are always written "Gate N," never bare "level N" or "stage N," to permanently disambiguate from STARS's own 1-9 TRL numbers.

None of this crosswalk work is done yet. It is a precondition for ratification, not a formality to backfill afterward.

## Grounding Gate 1's floor

Investigation found no single existing standard that already plays "TRL-for-agents" off the shelf — the field splits into capability/autonomy evals versus governance/security maturity versus org-adoption maturity, and none was built to be "Gate 1" out of the box. The deliberation's converged recommendation, adopted here: ground Gate 1 on the **capability/autonomy axis**, not the governance-maturity axis, since 9-Gate's scope is fleet-wide onboarding/graduation rather than deployment-risk control.

The real, currently-published, citable sources to build from:
- **METR's Time Horizon metric** (task-length-at-50%-success, doubling roughly every 7 months) as the quantitative anchor — empirical, currently tracked, already cited in frontier model cards. Sources: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ and https://metr.org/blog/2026-1-29-time-horizon-1-1/
- **DeepMind's "Levels of AGI" ontology** (arXiv:2311.02462, ICML 2024) as the structural precedent — the closest existing analog to a TRL-style ladder built specifically for AI systems, itself explicitly modeled on SAE J3016.
- NIST AI RMF's Agentic AI Profile, ISO/IEC 42001, and OWASP's 2026 Agentic AI maturity model are real and citable but better suited to later gates' deployment-risk and governance-control requirements than to Gate 1's capability floor — using them at Gate 1 would reintroduce the multi-axis stacking problem that sank replace-stars.

This is a deliberate adaptation the Brain Trust still has to do, not a straight lift from any of these sources — none was built for this purpose, and the specific Time Horizon threshold or autonomy rung that constitutes "cleared for Gate 1" is a table decision, not one this ruling can make.

## On the number 9

Abad's numerology — his personal, symbolic reasoning for choosing nine — is not evidence and does not appear anywhere above as justification for the gate count, per his own explicit instruction. It must not appear as fact in any ratified version of this ruling. If referenced at all, it belongs in a footnote naming it plainly as the operator's personal motivation for proposing the number, segregated from the rationale.

The organizational choice of a 9-stage structure is judged on its own terms, separately: investigation found the case for exactly nine gates does not yet stand on structural merit alone. It is plausible — TRL's own established 1-9 convention is a real, non-symbolic precedent, and STARS already uses it — but unproven, absent a bottom-up derivation showing nine distinct, non-arbitrary capability/governance checkpoints actually exist to gate on. This ruling does not fix the count at nine. The ratified document must record that derivation — the actual domains identified while building the FLEET_LEVELING crosswalk — and let the count follow from it. If it lands on nine, the citable justification is inheritance of TRL's existing convention, not symbolism. If it lands elsewhere, the Brain Trust ratifies that number instead.

## Dissent

None. All four judges voted hybrid-or-other; there was no minority ballot. Where the judges' reasoning varied was in emphasis, not outcome:

- Judges 1 and 3 weighted most heavily hybrid's rebuttal of replace-stars's "one axis, hardened" claim — that stacking external capability and governance requirements onto STARS's existing floor is substantively closer to the rejected multi-axis matrix, not further from it.
- Judges 2 and 4 weighted most heavily layer's own admitted failure to solve the fragmentation problem — the permanent three-independently-scored-systems outcome it conceded outright — and hybrid's construction-level fix for it.
- All four judges independently flagged hybrid's "count the independently-scored systems per agent" test as the decisive, most falsifiable argument of the debate, and all four noted hybrid was the most consistent about naming its own unresolved dependencies (the crosswalk is undrafted, FLEET_LEVELING's actual per-stage criteria are unverified, Gate 1's capability-vs-governance axis choice is a scoping call, not a settled fact) rather than treating them as closed.

No judge found replace-stars's or layer's core structural objections to hybrid unanswered. This was a clean, non-contentious 4-0.

## What remains for the operator's ratification pass

This is the fleet's candidate verdict, produced through the mandated investigation/debate/vote process — it is not yet ratified. Before Abad ratifies it, the following unbuilt work must actually be done, not assumed:

1. **Draft and ratify the Gate-range-to-FLEET_LEVELING-label crosswalk table**, including the explicit acknowledgment that nine does not divide evenly into four stages.
2. **Check FLEET_LEVELING's actual current content** — does it already carry documented per-transition criteria behind its four labels? If yes, Gate's claimed value-add (filling a currently-empty gap) shrinks to "formally validating existing criteria," and the ratified document needs to say so rather than overclaim.
3. **Do the bottom-up derivation** of the specific capability/governance domains each gate is meant to check, and let the final gate count fall out of that work rather than being fixed at nine in advance.
4. **Decide and ratify Gate 1's specific threshold** — the actual Time Horizon number or DeepMind autonomy rung that constitutes "cleared" — since the investigation and this ruling only narrow the candidate sources, they don't set the bar.
5. **Adopt the "Gate N" documentation convention** fleet-wide to disambiguate from STARS's own 1-9 TRL numbering before any Gate goes live.
6. **Confirm STARS's citation-only edit** (the note pointing to Augustin's Gate status) with whoever holds ratification authority over STARS.docx, since even a non-substantive edit to an already-ratified document should get that sign-off explicitly rather than by implication.

Until those six items are done and separately ratified, this verdict is a direction the fleet has voted to pursue, not a system that functions as described.

## Links

- resolves, `2026-08-08-heavy-chat-handoff-addendum-routing.md`, the routing note that sent this
  question to the Brain Trust and AJ.
- extends, `2026-08-08-heavy-chat-handoff-research-role.md`, the original handoff that first
  flagged the STARS/FLEET_LEVELING fork.
- affects, `STARS.docx`, cited but not modified in substance — gains only a pointer citation to
  Gate status, per this ruling.
- affects, `FLEET_LEVELING_2026-08-01.md`, redefined from an independently-scored system to a
  derived label, pending the crosswalk work item 1 above.
- blocks, the STARS/DREAMS dashboard rebuild, until items 1-6 above are done and this ruling is
  ratified.
