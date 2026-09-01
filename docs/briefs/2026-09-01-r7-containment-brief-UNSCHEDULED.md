# R7 containment — unscheduled security brief

**Status: UNSCHEDULED. Not a plan. Nothing here is adopted, and nothing here is work.**

This brief holds the R7-shaped content that was cut from
`docs/specs/2026-09-01-security-arsenal-integration-plan-v2.md` when the operator ratified the Brain
Trust slate on 2026-09-01 under **Option A** (`docs/decisions/BRAIN_TRUST_DECISION_RECORD_2026-09-01.md`).

It exists so the thinking is not lost and so the next person does not rediscover it. It does **not**
exist to be executed. It sits behind GEO, exactly where the operator has twice placed the Ambient
Clinical Scribe, and where §8.8 of `PROJECT_BRIEF_AMBIENT_CLINICAL_SCRIBE_2026-08-30.md` puts it.

## Why it is unscheduled rather than deferred-with-a-date

The panel rejected adopting a scribe security architecture 3–2, and the two approve-with-changes votes
agreed on the substance. The reason is mechanical, not editorial: **adopting a security architecture
for a project starts the project.** The ACS brief states in its own §8 that the ACS is *"Not started.
Not scheduled."* A ratified security plan for it would have acquired a live workstream, a named owner
and a claim on the operator's hours without anyone ever voting to start it.

## The three gates that must clear before any of this becomes work

1. **The ACS is scheduled.** Not "prioritised" — scheduled, with slice numbers, against GEO's deadline.
2. **A design-partner site exists.** Orlok's correction to I6 stands: settling R7 is not "one phone
   call," because there is no hospital to call. The action is *get a site*, then ask.
3. **The panel is composed for the docket.** A privacy-and-compliance seat under a name the reviewed
   document did not create, plus a verification-and-risk seat (TYR or an equivalent independent
   security lens). Ratified I8, rejected 5–0 by the seats themselves.

Until all three clear, nothing below carries panel authority and must not be cited as decided.

## The open question that governs everything else

**Is R7 physical or contractual?** Does "patient information must never leave the hospital system" mean
bytes must not traverse a network the hospital does not own, or that any processor must be under a BAA?

The two readings produce entirely different architectures, and the cost difference is roughly an order
of magnitude. Both product documents independently identify this as the highest-leverage open question
and the cheapest next action. **It has now been identified as the next action three times across three
documents and performed zero times.** Restating a recorded next action is not performing it; that is
this fleet's most-repeated failure, and this brief is at risk of being the fourth restatement.

**Ratified disposition:** this is a standalone operator action item with a date, routed outside any
security plan. It is not a gate on fleet remediation. GEO's exposed deploy path and its tenant-isolation
history are due regardless of what a hospital says.

## Constraints the panel established, which any future plan inherits

- **R7 says "patient information." It does not say "code, dependencies, logs or findings."** v2 widened
  it silently and without authority. Any future document that widens it must say who authorised the
  widening. (Oluwole, I1.)
- **Self-hosted runners do not achieve containment on their own.** They move *execution* inside the
  boundary and leave the *repository* — source, history, issues, artifacts, and the sixteen baselined
  credential-shaped findings in `research/knowledge-home/raw/` — on Microsoft-operated infrastructure.
  If R7 is physical, the breach has already happened at `git push`. They also need ephemeral per-job
  isolation (ARC on Kubernetes) or you get cross-job contamination on a PHI-adjacent runner, plus an
  image pipeline, patching, and a named owner inside hospital IT at 3am. Hospital IT will not put an
  internet-connected runner that long-polls github.com on a clinical VLAN without change control
  measured in months. And the runner's core function — outbound to github.com, PyPI, npm — is the first
  thing a default-deny egress policy must allowlist. (Orlok and Celestina, I5. Rejected 3–2.)
- **A vendor that receives only source code is not a business associate.** The BAA-per-engine
  construction in v2 was wrong and is not carried forward.
- **This is not an architecture.** Celestina's I1 finding: v2 has no data-flow model, no trust-boundary
  model and no key-custody model, and its own §10 concedes it. Whatever replaces this brief must start
  with those three, not with a phase list.
- **A document must not be reviewed by the agents it creates.** The reviewer must predate, and be able
  to outlive, the thing it reviews. This is the rule that cost the last review its privacy seat.

## What is NOT here, deliberately

Phase −1 PHI classification, runtime default-deny egress, `terraform plan` network segmentation,
self-hosted runner architecture, the consent interlock, audio-at-rest key custody, retention schedules
and the breach clock. All of it was in v2. None of it is adopted, and reproducing any of it as a work
item is a breach of the ratified decision.

The one control that survived the cut is in the runbook, not here: a **build-time** egress gate that
fails the build on a call path from Red-classified code to a frontier provider. It ships now precisely
because zero Red code exists, so it blocks nothing while establishing the mechanism.
