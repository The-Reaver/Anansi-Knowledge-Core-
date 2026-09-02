---
id: 2026-08-30-the-oluwole-amaya-fold-in-ruling-was-proven-end-to-end-brief-to-push
type: finding
status: ratified
ratified: "2026-08-31 — operator directly ratified via scripts/knowledge_home/ratify.py (CLI)"
class: confirmed
source: "Oluwole weekly design-research scheduled task, 2026-08-30 session, full closeout"
project: fleet
tags: [oluwole, amaya, knowledge-core, brain-trust, governance, verification, end-to-end]
sources:
  - ref: "Direct observation of this session's own sequence: design-brief-2026-08-29.md written -> zero-adoption gap found -> 4-seat Brain Trust review convened and ruled -> candidate note corrected on a real QA catch -> ratify.py run successfully on the operator's own machine (verified: file moved from candidates/2026-08-30/ to notes/, status: ratified) -> git commit 9dc1712 pushed to origin/anansi-home-dashboard, confirmed by the operator's own pasted terminal output"
    reliability: high
    origin: "same session, 2026-08-30, operator-confirmed each step via pasted terminal output rather than agent self-report"
provenance:
  archive: research/knowledge-home/raw/2026-08-30-oluwole-design-brief-and-closeout.jsonl
  turns: [1, 27]
risk_class: C
evidence_state: SUPPORTED
next_review: 2026-11-30
classified: 2026-08-30
---

- class: confirmed
- confidence: high — every step verified by direct file/git inspection or the operator's own pasted terminal output, not asserted
- verified: 2026-08-30

# The research-produces, Brain-Trust-decides, operator-ratifies loop ran end to end for the first time on this pipeline, brief to pushed commit, in one session

## Body

This session is the first complete, verified run of the fold-in mechanism `vanguard-research-harvest-and-review-cadence.md` now specifies, and it happened somewhat by accident: the mechanism didn't exist until this session's Brain Trust review created it, and then the same session immediately exercised it end to end. Sequence, each step independently confirmed rather than taken on the prior step's word: (1) Oluwole produced `design-brief-2026-08-29.md`, sourced and verified programmatically for citation completeness; (2) an operator question surfaced that the Amaya fold-in step had never executed across six prior briefs, verified via `git log` and a line-by-line content check, not inference; (3) a cold adversarial-review subagent independently re-derived those facts and caught one real overstatement; (4) a 4-seat Brain Trust panel (Amaya, Oluwole, Celestina, Jasiah), run as independent subagents with no shared context, unanimously ruled a concrete fix, and Jasiah's seat caught a second real defect (an unverifiable provenance claim) in the same candidate note; (5) the operator ran `ratify.py` on their own machine, confirmed by directly inspecting the resulting file's location and `status:` field; (6) the operator staged, committed, and pushed the result, confirmed by the actual git output (`9dc1712 pushed to anansi-home-dashboard`).

The generalizable lesson: this fleet's layered verification discipline (self-check, then adversarial subagent, then independent Brain Trust seats, then the operator's own hands on the final ratify/commit/push) caught two real defects in a single candidate note before it reached the Core, and neither defect was cosmetic — one was a factual overstatement (3 of 6 briefs, not 6 of 6), the other was a process-integrity gap (an unverified review claim, the exact failure class `2026-08-20-self-asserted-ratification-lines-are-not-verification.md` already warns about). The layering worked as designed, on a live case, not just in the abstract.

## Links
- relates-to: 2026-08-30-six-oluwole-design-briefs-piled-up-with-zero-folded-into-design-principles — the specific finding this end-to-end run was about.
- relates-to: research/knowledge-home/structure-notes/vanguard-research-harvest-and-review-cadence.md — the mechanism this session created and then immediately exercised.
- relates-to: 2026-08-20-self-asserted-ratification-lines-are-not-verification — the standard Jasiah's seat held this session's own work to, and caught it failing once.
