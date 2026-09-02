---
id: 2026-08-21-pre-seeding-agent-knowledge-ranked-by-determinism-not-narrated-as-prose
type: decision
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [stag, knowledge-transfer, skills, claude-md, hooks, agent-hardening, methodology]
sources:
  - ref: "Archive turn 101 is the operator's verbatim question ('Is Pre-Seeding valid? Do my agents actually need to learn by failing... or can I codify them into a Skill Library'); turn 102 gives the four-layer determinism-ranking framework; turns 153-180 show the hook/CLAUDE.md/Skill/reference scaffold actually built and the enforcement hook exercised with three verified exit codes (0/2/0) at turn 177."
    reliability: high
    origin: "STAG session, 2026-07-17, \"Project brief step 0 deployment handoff\" (backfilled from historical transcript db88cef4, 2026-08-21)"
provenance:
  archive: research/knowledge-home/raw/2026-07-17-backfill-db88cef4.jsonl
  turns: [101, 183]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---
- class: confirmed
- confidence: medium, this is a stated methodology adopted in the session rather than a benchmarked or externally-validated result
- verified: 2026-08-21

# Pre-seeding future agents with lessons learned manually is valid, but each lesson must be pushed to the most deterministic layer it can hold, and a Skill is a different genre of writing than a chat instruction

## Body
The operator asked whether solutions and patterns worked out manually with the agent (while budget-constrained and unable to run autonomous agents) can be "pre-seeded" so future agents don't have to "learn by failing" on their own. The answer given and acted on in this session: pre-seeding is not just valid but necessary for stateless LLM agents, because failing-and-recovering within a single run teaches the agent nothing that persists into the next run -- only externalizing the lesson into a file the next run actually reads compounds over time.

The operating rule adopted for deciding *where* to put a given lesson: push it to the most deterministic layer that can hold it, checked in this order --
1. **Enforcement** -- a hook, lint, or validator that makes the mistake structurally impossible to commit, not merely discouraged.
2. **Always-on invariants** -- a file like `CLAUDE.md`, loaded on every turn -- reserved for small, universal, non-negotiable rules, because every token placed there taxes every subsequent turn.
3. **Task-triggered procedures** -- a Skill, where only the one-line `description` is loaded by default; the body loads only when a task matches. This is a specific correction to a common assumption: Skills are not "read on day one" the way `CLAUDE.md` is -- only their descriptions are always in context.
4. **Reference** -- long docs read only on demand.

A separate, distinct point established alongside the ranking rule: a chat instruction given live and a Skill saved to a filesystem are different genres of writing, not the same content in a different location. A chat instruction can stay terse because it can lean on the live conversation's shared context (e.g. "fix that route"). A Skill must be self-contained for a reader with zero prior context -- it needs explicit preconditions, numbered steps, named failure modes, and a verification step -- and its `description` field is literally the retrieval trigger: a vague description means the Skill silently never fires.

Named clash risks to design against when building out this kind of scaffold: over-broad Skill descriptions causing the wrong Skill to fire (or two to conflict); `CLAUDE.md` bloat diluting the model's attention on every turn; the same rule duplicated across `CLAUDE.md`, a Skill, and a validator silently drifting out of sync over time (single source of truth, reference rather than copy); and operational Skills going stale by naming a specific file or flag that later moves.

## Links
- extends, origin-scaffold-emission-hardens-projects-on-day-one.md, the concrete implementation (meta-agent's `_emit_agent_scaffold()`, planting a hook/CLAUDE.md/Skill into every generated project) that this ranking framework justifies and was built to satisfy in the same session.
