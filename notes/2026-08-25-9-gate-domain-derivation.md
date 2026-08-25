---
id: 2026-08-25-9-gate-domain-derivation
type: finding
status: candidate
source: >
  this chat, item 3 of `2026-08-25-9-gate-precondition-tracker.md` ("bottom-up derivation of the
  specific capability/governance domains each gate is meant to check, and let the final gate count
  fall out of that work rather than being fixed at nine in advance"). Research agent run: web
  search across METR, DeepMind, OpenAI, Anthropic, NIST, ISO, OWASP, SAE, and TRL primary and
  secondary sources. Direct WebFetch of primary-source pages was blocked by this session's network
  egress policy for every domain attempted (arxiv.org, metr.org, openai.com, anthropic.com,
  deepmind.google, epoch.ai, en.wikipedia.org) — all findings below are sourced through
  search-engine-mediated summaries and secondary sources, not this agent's own direct reading of
  primary text. Flagged inline wherever that limitation affects confidence.
project: fleet
tags: [brain-trust, 9-gate, gate-derivation, capability-axis, governance-axis, stars-dreams]
---

# Finding: a bottom-up derivation of 9-Gate's capability and governance domains lands on 10 gates (5 capability, 5 governance) under the most defensible merge logic — not 9, and not forced to be

## Body

## 0. What this document is and isn't

This is the deliverable for precondition item 3 of the 9-Gate Brain Trust verdict
(`2026-08-25-9-gate-brain-trust-verdict.md`): a real, citable, bottom-up derivation of the
capability and governance domains a fleet-wide onboarding/graduation ladder should gate on, and
the gate count that falls out of that work. It is **not** a ratification — it is candidate
research input for the Brain Trust table to adopt, amend, or reject.

It does **not** set Gate 1's specific numeric threshold (that is precondition item 4, assigned to
a separate research agent per the tracker). It does not touch the FLEET_LEVELING crosswalk
(item 1, blocked on file access). It treats the operator's original preference for nine gates as
inadmissible as evidence, per the verdict's explicit instruction, and does not target nine — the
number below is reported honestly, including a sensitivity analysis showing exactly which single
merge decisions would move it up or down, so the Brain Trust can see the count is a function of
real judgment calls, not a fixed target.

## 1. Method

Two source categories were researched, matching the verdict's own scoping call:

- **Capability/autonomy axis** (for early gates): frameworks that measure what an AI agent can
  *do* — task duration, reliability, breadth, planning, tool-use, degree of independence from a
  human.
- **Governance/deployment axis** (for later gates): frameworks that measure what *organizational
  controls* exist around how an agent is run — ownership, risk assessment, monitoring, incident
  response.

For each framework, this document extracts only dimensions/levels the source **itself names
explicitly** as a distinct axis or category — not dimensions this agent invented to fill gaps.
Where a domain required inference beyond what a source states outright, that is flagged as
**extrapolated** rather than **directly sourced**. Domains are then merged into gates only where a
stated structural reason exists to merge them, with each merge decision argued on its own terms
before any count is taken.

## 2. Sources reviewed

### 2.1 Capability/autonomy axis sources

**METR Time Horizon** — *directly sourced.* The 50%-time-horizon is the task duration (measured by
expert human completion time) at which a model's fitted success-probability curve crosses 50%.
METR separately reports an 80%-threshold horizon, which is currently roughly 1/3 the length of the
50%-horizon for frontier models (~40 min vs. ~2 hr) — the two thresholds are explicitly reported as
materially different practical claims, not the same number restated. The 50%-horizon has been
doubling roughly every 7 months over six years of frontier models. This is an empirical,
continuously-tracked metric already cited in frontier model cards, which is why the prior verdict
identified it as the strongest quantitative anchor available.
Sources: [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/),
[Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/),
[METR Time Horizons](https://metr.org/time-horizons/), underlying paper
[arXiv:2503.14499](https://arxiv.org/abs/2503.14499).

**DeepMind "Levels of AGI"** (arXiv:2311.02462, Position paper, ICML 2024) — *directly sourced for
structure, partially extrapolated for exact wording.* The paper defines **two independent axes**:
*Performance* (depth) on a 6-point scale — Level 0 No AI, 1 Emerging, 2 Competent (≥50th percentile
of skilled adults), 3 Expert (≥90th percentile), 4 Virtuoso (≥99th percentile), 5 Superhuman
(exceeds 100% of humans) — and *Generality* (breadth), narrow vs. general, evaluated separately
from performance. A third, related construct, *Levels of Autonomy* (also 0–5: 0 No AI, 1 AI as Tool, 2 AI as
Consultant, 3 AI as Collaborator, 4 AI as Expert, 5 AI as Agent — names confirmed by the sibling
research pass on item 4, `2026-08-25-gate-1-threshold-candidates.md`, which cross-checked search
snippets quoting the primary text directly), is described as "unlocked, but not determined by"
progression through the Levels of AGI — i.e., explicitly decoupled from raw capability, though the
paper itself gates full Autonomy Level 5 behind high Performance (Virtuoso/Level 4 or
Superhuman/Level 5). The paper states it modeled this decoupled, ladder-based ontology on SAE
J3016's levels of driving automation. **Note**: this is a *second, separate* autonomy taxonomy from
the Feng/McDonald/Zhang one below (Operator/Collaborator/Consultant/Approver/Observer) — the two
frameworks are not the same scale despite overlapping vocabulary ("Collaborator," "Consultant"
appear in both with different meanings), which is exactly the kind of ambiguity flagged in §7.
Sources: [arXiv:2311.02462](https://arxiv.org/abs/2311.02462),
[DeepMind publication page](https://deepmind.google/research/publications/levels-of-agi-for-operationalizing-progress-on-the-path-to-agi/).

**"Levels of Autonomy for AI Agents"** (Feng, McDonald, Zhang; Knight First Amendment Institute,
Columbia; arXiv:2506.12469, v2 July 2025) — *directly sourced.* Distinct from and not affiliated
with METR or DeepMind (note: some search-engine summaries mis-attributed this paper to METR; the
actual authors are Feng/McDonald/Zhang). Defines five levels named by the human's role: **L1
Operator** (user makes all decisions, agent acts only on direct command), **L2 Collaborator** (user
and agent share planning/execution with fluid handoffs), **L3 Consultant** (agent leads, consults
user only for expertise/preferences), **L4 Approver** (user interacts only when the agent hits a
blocker it can't resolve itself — a failure state, missing credentials, or a consequential
sign-off), **L5 Observer** (agent acts fully autonomously; user can only monitor or emergency-stop).
The paper's central argument is that autonomy is **a deliberate design decision, separable from
capability and operating environment** — and it proposes third-party "autonomy certificates"
verifying an agent behaves at a claimed level and no higher, which is a close structural analog to
what a Gate checkpoint would need to do. Sources: [arXiv:2506.12469](https://arxiv.org/abs/2506.12469),
[Knight Institute publication](https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1).

**OpenAI, "Practices for Governing Agentic AI Systems"** (Shavit, Agarwal, et al.) — *directly
sourced for the four-dimension claim, extrapolated for precise gradation wording.* Explicitly names
**four dimensions** as jointly constituting how "agentic" a system is: **autonomy**, **efficacy**
(how reliably the agent's actions in its environment actually achieve outcomes), **goal
complexity** (how ambiguous/multi-step/underspecified the objective is), and **generality** (breadth
of task types). This is the single clearest primary-source claim found that names exactly this many
domains as the right decomposition of agentic behavior, which is why it anchors the capability-axis
derivation below. Sources: [OpenAI publication page](https://openai.com/index/practices-for-governing-agentic-ai-systems/),
[paper PDF](https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf).

**Adjacent frontier-lab risk frameworks reviewed but not used as primary sources** — *directly
sourced, out of scope by design, not by oversight.* Anthropic's Responsible Scaling Policy (AI
Safety Levels ASL-1 through ASL-4+, [anthropic.com/responsible-scaling-policy](https://www.anthropic.com/responsible-scaling-policy)),
OpenAI's Preparedness Framework (Low/Medium/High/Critical thresholds across cybersecurity, CBRN,
persuasion, and model-autonomy categories, [openai.com/global-affairs/our-approach-to-frontier-risk](https://openai.com/global-affairs/our-approach-to-frontier-risk/)),
and DeepMind's Frontier Safety Framework (Critical Capability Levels across cyber, autonomous ML
R&D, manipulation, CBRN, [deepmind.google/blog/strengthening-our-frontier-safety-framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/))
are all real, current, and well-documented. They were **not** adopted as primary domain sources
because their scope is catastrophic/societal risk from frontier model *training and release*
decisions made by a single lab, not operational trust for a fleet's own working agents — a
structurally different question from "is this agent cleared to run task X inside this fleet."
ASL-3's concern with "low-level autonomous capabilities" and autonomous replication is cited below
only as corroborating evidence for *why* the Gate 5 autonomy/error-recovery boundary matters, not
as a structural source for gate content.

### 2.2 Governance/deployment axis sources

**NIST AI Risk Management Framework** — *directly sourced for the four-function structure;
unresolved for the Agentic AI Profile specifically.* NIST AI RMF 1.0's core is four explicitly named
functions: **Govern** (organizational culture, policy, accountability — the foundation the other
three depend on), **Map** (contextualizing the system and its impacts before/during deployment),
**Measure** (testing the system against defined trustworthiness characteristics), **Manage**
(turning measurements into prioritization, kill-switch procedures, and disclosure). Source:
[NIST AI RMF core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). **Caveat — genuinely
unresolved**: search results were contradictory on whether a dedicated NIST agentic-AI profile
(referenced in the prior verdict and sometimes labeled "NIST AI 100-5") is already published or
still pending; some sources describe CAISI's AI Agent Standards Initiative (announced February
2026) as targeting a Q4 2026 release, while others describe an agentic profile as already
addressing agent-specific risks. **This must be verified against NIST's own publication page before
any ratified document cites a specific NIST agentic-profile document number or date** — this
research agent could not resolve the contradiction and is not asserting either version as fact.

**ISO/IEC 42001:2023** — *directly sourced for structure via secondary/compliance-vendor summaries
only; the primary standard text is paywalled and was not read directly.* Defines an AI management
system with 38 Annex A controls grouped under nine control objectives (A.2–A.10): AI policies;
internal organization and roles; resources (data, tooling, human resources); AI system impact
assessment; AI system lifecycle (design, verification/validation, deployment, monitoring); data for
AI systems; information for interested parties (transparency); use of AI systems (including
third-party AI use); and supplier/third-party relationships. **Flagged explicitly**: nine control
objectives is a coincidence of ISO's own document structure and carries no bearing whatsoever on
9-Gate's gate count — noted here only for completeness, and explicitly *not* used anywhere in the
derivation below as a reason to land on any particular number, per the same numerology exclusion
the prior verdict already applied to TRL.

**OWASP GenAI Security Project, "State of Agentic AI Security and Governance"** (v2.01, published
2026) — *directly sourced for the two-axis structure; internally inconsistent across secondary
sources on exact level counts, flagged.* Proposes an Enterprise Adoption Maturity Model with two
independent axes: a **Deployment/Adoption-Tier axis** (how much system access and how many
organizational boundaries an agent crosses, from shadow AI up through federated cross-boundary
agents) and a separate **Governance-Maturity axis** (an organization's oversight capability, from
ad hoc awareness to adaptive, telemetry-driven control with kill-switches and real-time drift
dashboards). **Caveat**: secondary sources disagreed on the exact tier count — some described "six
levels" on the deployment axis, others enumerated AT0 through AT8 (nine tiers); the governance
axis was described both as "four levels" and as "Levels 0 through 4" (five levels). This agent
could not fetch the primary OWASP document to resolve the discrepancy. **The specific tier names
and count must be pulled from the primary OWASP publication directly before being cited by number
in a ratified document** — only the *structural claim* (two independent axes: blast-radius
classification, separate from oversight maturity) is used below, not any specific count from OWASP.

**SAE J3016** — *directly sourced, used only as structural precedent, not as content.* Six levels
(0–5) of driving automation, split at the boundary where the automated system vs. the human
performs the full "dynamic driving task." Cited only because DeepMind's Levels of AGI explicitly
names this as its own modeling precedent — it is not itself an AI-agent framework and contributes
no domain content here.

## 3. Derived domains, with citation and confidence label

| # | Domain | Axis | Primary citation | Confidence |
|---|---|---|---|---|
| A | Sustained task duration at 50% reliability | Capability | METR Time Horizon | Directly sourced |
| B | Sustained task duration at 80%+ reliability | Capability | METR Time Horizon (80% threshold) | Directly sourced |
| C | Domain generality / breadth | Capability | DeepMind Levels of AGI (generality axis) | Directly sourced |
| D | Goal complexity / multi-step decomposition | Capability | OpenAI four-dimension framework; DeepMind Level-3 "coordinate subtasks" descriptor | Directly sourced |
| E | Tool-use & environment efficacy | Capability | OpenAI four-dimension framework; DeepMind "use external tools" descriptor | Directly sourced |
| F | Autonomy level / error-recovery without escalation | Capability, bridges to governance | Feng/McDonald/Zhang Levels of Autonomy (Approver/Observer boundary); OpenAI "autonomy" dimension; corroborated by Anthropic ASL-3's "low-level autonomous capabilities" concern | Directly sourced |
| G | Deployment-tier / blast-radius classification | Governance | OWASP Adoption-Tier axis (structural claim only — exact tier count unverified) | Directly sourced (structure); tier count unresolved |
| H | Governance foundation: policy, ownership, accountability | Governance | NIST AI RMF — Govern function; ISO 42001 A.2–A.3 | Directly sourced |
| I | Risk & impact assessment | Governance | NIST AI RMF — Map function; ISO 42001 A.5 | Directly sourced |
| J | Ongoing measurement & monitoring | Governance | NIST AI RMF — Measure function; ISO 42001 A.6; OWASP governance-maturity axis | Directly sourced |
| K | Incident response & managed control (kill-switch, drift response) | Governance | NIST AI RMF — Manage function; OWASP top governance-maturity tier; ISO 42001 incident-management controls | Directly sourced |
| L | Data / third-party / supply-chain governance | Governance | ISO 42001 A.7–A.10 | Directly sourced, but not treated as an independent gate (see §4, decision 7) |

Twelve raw domains, six per axis before any merge decisions.

## 4. From domains to gates: the merge decisions, argued on their own merits

Each decision below is argued for its own structural reason, in the order made, **before** any
running total was calculated — the count in §5 is what fell out, not what was aimed for.

1. **A + B merge into one gate.** Both come from the same instrument (METR Time Horizon) at two
   confidence bars, not two conceptually distinct domains — a single gate can carry two required
   thresholds, the same way TRL sub-criteria can require more than one condition per level.
   → 1 gate.
2. **C stays separate.** DeepMind treats generality as independent of performance/duration by
   design — an agent with a long time-horizon in one domain (e.g. coding) provides no evidence
   about a different domain (e.g. legal research). Collapsing this into Gate 1 would hide exactly
   the kind of over-generalization risk a fleet cares about. → kept.
3. **D and E stay separate from each other and from A+B**, despite the acknowledged overlap
   (long-duration tasks necessarily exercise both planning and tool-use). Reason: METR's Time
   Horizon is a *blended outcome* metric — it cannot tell the fleet whether a failure at hour 3 was
   a planning failure or an execution failure. OpenAI names these as distinct failure modes for a
   reason; a graduation ladder that can only report pass/fail without localizing *why* an agent
   failed is diagnostically weaker than one that can. This is the single most contestable merge
   decision in this derivation — see §6. → kept as two gates.
4. **F stays separate**, and is explicitly the bridge gate to the governance axis, since its
   source frames autonomy as a design/trust decision, not a pure capability measurement. → kept.
5. **G (deployment-tier classification) stays separate and is sequenced first on the governance
   axis.** You cannot size a governance-foundation review, risk assessment, monitoring regime, or
   incident-response plan without first knowing what systems/boundaries the agent will touch —
   OWASP's own model treats this as a separate axis for exactly this reason. → kept, sequenced
   first.
6. **H, I, J, K (NIST's four functions) stay as four separate, unmerged gates.** This is the one
   place in the whole derivation where a single primary source explicitly and deliberately names
   this exact number of domains as its considered structural claim — NIST did not propose three
   functions with Manage folded into Measure, or five splitting Measure in two. Overriding that
   boundary would require a citable reason this derivation does not have. → kept as four gates.
7. **L (data/third-party/supply-chain) does NOT get its own gate.** Unlike NIST's four functions,
   ISO's nine Annex A control objectives are a checklist of controls under one management-system
   structure, not nine independently gate-worthy maturity dimensions ISO itself claims are
   separable. A.7 (data), A.9 (third-party use), and A.10 (supplier relationships) are naturally
   sub-topics of "is there accountable, documented governance" (H) and "was risk to data/third
   parties assessed" (I). Giving every ISO control objective its own gate would reproduce exactly
   the disproportionate multi-axis stacking the original verdict already rejected when it rejected
   replace-stars. → folded into H and I as required content, not a standalone gate.

## 5. Resulting gate sequence (primary candidate: 10 gates, 5 + 5)

| Gate | Name | Axis | Checks | Primary source(s) |
|---|---|---|---|---|
| 1 | Task-Duration & Reliability Capability | Capability | Can the agent complete tasks of a given duration unsupervised, at both a 50% and an 80% success bar | METR Time Horizon |
| 2 | Domain Generality | Capability | Does the demonstrated capability hold across multiple task domains, not just the one it was tuned/tested on | DeepMind Levels of AGI |
| 3 | Goal-Complexity & Planning | Capability | Can the agent decompose an ambiguous, multi-step, underspecified goal into the right subgoals | OpenAI four-dimension framework; DeepMind |
| 4 | Tool-Use & Environment Efficacy | Capability | Given a correct plan, do the agent's actions in its actual environment/tools reliably achieve the intended outcome | OpenAI four-dimension framework; DeepMind |
| 5 | Autonomy Level & Error-Recovery | Capability → bridges to governance | What level of human role (Operator through Observer) is this agent cleared for, including whether it can recover from its own blockers without escalation | Feng/McDonald/Zhang; corroborated by Anthropic ASL-3 |
| 6 | Deployment-Tier / Blast-Radius Classification | Governance | What systems, data, and organizational boundaries can this agent actually touch | OWASP Adoption-Tier axis (structure only) |
| 7 | Governance Foundation | Governance | Does an accountable owner, documented policy, and role structure exist, including data/third-party policy | NIST Govern; ISO 42001 A.2-A.3, A.7-A.10 |
| 8 | Risk & Impact Assessment | Governance | Has a pre-deployment risk/impact assessment been done and documented at this agent's classified blast radius | NIST Map; ISO 42001 A.5 |
| 9 | Ongoing Measurement & Monitoring | Governance | Is there active telemetry/drift measurement against defined trustworthiness characteristics, not just a one-time check | NIST Measure; ISO 42001 A.6; OWASP governance-maturity axis |
| 10 | Incident Response & Managed Control | Governance | Are there tested kill-switch, escalation, and incident-response mechanisms sized to this agent's deployment tier | NIST Manage; OWASP top governance-maturity tier; ISO 42001 incident controls |

**5 capability-axis gates, then 5 governance-axis gates — matching the verdict's instruction that
capability grounds the early gates and governance-maturity frameworks fit the later gates.** The
count is 10, not 9. It is reported exactly as derived.

## 6. Sensitivity analysis — how a single different merge choice moves the count

This table exists specifically so the Brain Trust can see the count is a function of identifiable,
individually-arguable choices, not an artifact this agent tuned toward or away from any target.

| If this single decision were made differently instead | Resulting axis totals | Resulting count |
|---|---|---|
| Baseline (§5) | 5 + 5 | **10** |
| Split Gate 1 back into two gates (50% / 80% separately) | 6 + 5 | 11 |
| Merge Gates 3+4 (treat Gate 1's METR number as a sufficient proxy for planning and tool-use both) | 3 + 5 | 8 |
| Merge Gates 3+4 **and** fold Gate 2 (generality) into Gate 1 | 2 + 5 | 7 |
| Merge Gates 8+9 (NIST Map+Measure treated as one "assess & monitor" gate) | 5 + 4 | 9 |
| Fold Gate 6 (deployment-tier classification) into Gate 7 as a precondition rather than its own gate | 5 + 4 | 9 |
| No merges anywhere — one gate per every raw domain in §3, including L as its own gate | 6 + 6 | 12 |
| Aggressive consolidation — capability collapsed to "capability floor" + "autonomy"; governance collapsed to "classify" + "govern/assess" + "monitor/control" | 2 + 3 | 5 |

**Two of the eight rows above land on nine.** This is flagged, not hidden — and it must be treated
exactly the way the prior verdict treated TRL's 1-9 convention: a structural coincidence that
*could* legitimately support landing on nine, but only if the Brain Trust independently decides
that merging Map+Measure, or folding blast-radius classification into governance-foundation, is
the *right* call on its own merits — never because it produces the number nine. Two other rows
land on 7 or 8, and one lands on 12. The honest conclusion is that the domain set is real and
well-sourced; the exact gate count is a genuine judgment call within roughly a 5–12 range, and this
document's role is to make each judgment call visible and arguable, not to resolve it unilaterally.

## 7. Capability axis vs. governance axis — the explicit boundary, and where it's contestable

**Squarely capability (Gates 1–4):** task duration/reliability, generality, goal complexity,
tool-use efficacy. All four are measured from the agent's demonstrated behavior on tasks, require
no organizational apparatus to assess, and are the domains the prior verdict specifically wanted
grounding Gate 1.

**Squarely governance (Gates 7–10):** governance foundation, risk assessment, monitoring, incident
response. All four are measured from what the *organization running the agent* has built, not from
the agent's own behavior, and map cleanly onto NIST's four functions.

**Genuinely contestable, flagged rather than papered over:**

- **Gate 5 (autonomy level)** is deliberately placed at the capability/governance boundary rather
  than cleanly inside either axis. Its own source (Feng/McDonald/Zhang) argues autonomy is a
  *design decision* — which sounds governance-shaped — but it is also gated by raw capability (an
  agent cannot safely be assigned Observer-level autonomy if it fails Gates 1–4), which is why it
  is sequenced last on the capability side rather than first on the governance side. A reasonable
  alternative structure would make Gate 5 the *first* governance gate instead, on the theory that
  "how much human oversight this agent requires" is fundamentally an organizational risk decision,
  not a capability fact. This document takes no strong position on which placement is correct and
  flags it explicitly for the table.
- **Gate 6 (deployment-tier classification)** is placed as the first governance gate, but it could
  equally be argued to belong on the capability side, since "what systems can this agent touch" is
  partly a function of what it's *capable* of touching reliably (Gates 1–4) and partly a function
  of what an organization *chooses* to grant it access to (governance). §6's sensitivity table
  shows this ambiguity has real consequences for the final count.
- **Gate 5's naming source** is itself contestable: DeepMind's embedded Levels of Autonomy (No
  AI / Tool / Consultant / Collaborator / Expert / Agent) and Feng/McDonald/Zhang's standalone scale
  (Operator / Collaborator / Consultant / Approver / Observer) are two different frameworks that
  happen to reuse "Collaborator" and "Consultant" at different rungs with different meanings.
  Whichever the Brain Trust adopts for Gate 5's actual level names, the ratified document must
  name its source explicitly and not silently blend the two, or "Collaborator" will mean two
  different things in the same governance document.
- **Gate 9 vs. Gate 8** (Measure vs. Map) is the second most contestable merge candidate: NIST
  frames these as temporally distinct (assess before deployment vs. monitor during operation), but
  a fleet running fast iteration cycles may find the practical distinction thin, which is why this
  row appears in §6's sensitivity table rather than being treated as settled.

## 8. Is TRL's 1–9 convention a good structural precedent for the final count?

**Good precedent for:** the general legitimacy of an ordinal, externally-citable maturity ladder as
a governance instrument. TRL is a long-established, non-symbolic, cross-agency (NASA, DoD, DOE,
European Commission) convention for exactly this kind of "is this thing ready to graduate to the
next stage" question, which is why the prior verdict was right to treat it as real precedent for
*building a ladder at all*, and why STARS.docx's own use of it is not disturbed by this work.

**Weak precedent for the specific count of nine, for a structural reason, not a preference:** TRL's
nine levels are nine successive **fidelity stages of validating a single question** — does this
technology work, tested progressively from theoretical principles through laboratory, through
relevant environment, through actual operational environment. It is one axis subdivided into nine
ordinal steps of increasing test realism, not nine independent domains stacked together. 9-Gate, by
contrast, is being built — per this derivation and per the verdict's own instruction — as **two
axes** (capability, then governance), each independently subdivided. That is a structurally
different kind of ladder than TRL's single-axis fidelity progression. Borrowing TRL's *count*
without also borrowing its *single-axis structure* is not a like-for-like inheritance — it would be
citing TRL's number while building something TRL's own methodology didn't produce. If the Brain
Trust wants a citable TRL-inheritance argument for landing on nine, it would need to be argued
through §6's specific merge choices (e.g., the Map+Measure merge, or folding blast-radius
classification into governance-foundation) on those choices' own merits — not through TRL's count
directly, since this ladder's shape does not match TRL's.

It's also worth noting TRL's own count is not universally fixed even within its home domain — other
adaptations (e.g. Manufacturing Readiness Levels) use different counts for structurally similar
purposes, which further weakens "TRL uses nine" as a reason to expect any other ladder should too.

## 9. Summary for the table

- Twelve real, citable capability/governance domains were identified from currently-published
  sources (§3).
- Applying the most defensible, individually-argued merge logic (§4) yields **10 gates: 5
  capability-axis, 5 governance-axis** (§5) — not nine, and not forced away from nine either.
- A sensitivity analysis (§6) shows the honest range is roughly 5–12 depending on specific,
  nameable judgment calls, two of which happen to land on nine — flagged explicitly as a
  coincidence requiring independent justification, never as evidence.
- Three boundary placements are genuinely contestable (§7) and are handed to the table
  undecided rather than resolved unilaterally by this research pass.
- TRL's 1–9 convention remains good precedent for building a ladder at all, but is structurally a
  poor precedent for the specific count, because 9-Gate's two-axis derivation does not match TRL's
  single-axis fidelity-progression structure (§8).
- Two sourcing gaps need direct primary-document verification before ratification: the NIST
  agentic-AI profile's actual publication status, and OWASP's exact tier/level counts and names on
  both axes of its 2026 maturity model (§2.2) — this agent's access to primary sources was blocked
  in this session and only search-engine-mediated summaries were available.

## Links

- extends, `2026-08-25-9-gate-brain-trust-verdict.md`, item 3 of its ratification preconditions
  ("Grounding Gate 1's floor" and "On the number 9" sections specifically).
- extends, `2026-08-25-9-gate-precondition-tracker.md`, resolving item 3's "in progress" status.
- depends on, `2026-08-25-gate-1-threshold-candidates.md`, item 4's research pass on Gate 1's
  specific numeric threshold, which this document's Gate 1 deliberately leaves as an open table
  decision — that note's confirmed DeepMind autonomy-level names are incorporated above.
- affects, `2026-08-25-gate-n-documentation-convention.md`, once a specific gate count is ratified,
  the convention should be checked against the actual adopted sequence.
