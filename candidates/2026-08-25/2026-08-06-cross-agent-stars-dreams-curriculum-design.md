---
id: 2026-08-06-cross-agent-stars-dreams-curriculum-design
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone away from the machine; asked to design the STARS/DREAMS curriculum for the other agents and how curricula execute across chats. Captured to the Anansi Atomic Notes Inbox because the repo was not reachable from the phone. (source status: draft)"
project: fleet
tags: [training, curriculum, stars, dreams, cross-agent, resume-protocol, mandate-7, mandate-8]
supersedes: []
superseded_by: null
---

# Cross-agent training system, STARS curriculum plus DREAMS tracker, runs across chats

## Body

Goal: every key fleet agent trains and levels on proof the way Augustin does, and the training runs across chats so no work is trapped in one chat.

Two documents per agent, the Augustin model generalized:
- STARS, the curriculum. An ordered roadmap of the skills the agent must master, cut into small slices, each with a proof gate. Answers what the agent must learn and in what order.
- DREAMS, the tracker. A live scorecard of the agent's level per skill and one composite index. Answers how far along the agent is and what the next task is.

Where they live, so nothing is trapped in a chat:
- In the repo: curricula/<agent>/CURRICULUM.md (the STARS) and curricula/<agent>/PROGRESS.md (the DREAMS).
- Every finished task becomes an atomic note in research/knowledge-home/notes/ (the proof record) and updates PROGRESS.md.
- Everything commits to GitHub.

How a curriculum runs across chats, the resume protocol:
1. A new chat reads READ_FIRST.md, then MASTER_TODO.md.
2. It reads curricula/<agent>/CURRICULUM.md and PROGRESS.md.
3. It finds the next unproven task.
4. It does that task as one slice.
5. It proves the task: verify.py green, or a proving artifact per Mandate 7.
6. It writes an atomic note, updates PROGRESS.md, commits, and pushes.
7. The next chat reads PROGRESS.md and continues from the next task. No chat memory is needed.

The proof rule, so levels are real and not claimed:
- A skill levels up only on a proving artifact (Mandate 7). The DREAMS composite moves only on proof, never on a claim.

How the artifact-building curriculum fits:
- It becomes one shared skill track any agent can run through their STARS. The 25 artifact tasks are a module, and each agent's DREAMS tracks their artifact-building level.

Two operator choices, pending (kept draft until answered):
1. Which agents to start with. Recommendation: Jeremy (knowledge core) and Oluwole (research and sourcing), the two the compliance and knowledge-core work leans on most. Prove the format on two, then roll out.
2. The DREAMS score model. Recommendation: start with the simple TRL 1 to 9 like Augustin's DREAMS, since it already exists and is simple, then upgrade to the fleet's full leveling math (Wilson, Glicko-2, SPRT) later.

Next machine session: build curricula/README.md (the resume protocol), then the first agent's CURRICULUM.md and PROGRESS.md, once the operator picks the two starting agents and the score model.

## Links

- relates-to: 2026-08-06-master-todo-and-offline-guide-established
- relates-to: 2026-08-06-read-first-rulebook-and-dev-process
