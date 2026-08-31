---
id: 2026-08-06-agent-development-lifecycle-adlc-gameplan
type: decision
status: candidate
source: "Cowork session 2026-08-06, operator on phone; asked for the definitive gameplan and roadmap as a visual life cycle showing how training leads to an agent that builds complex apps on command. An infographic was delivered to the operator this session and should be committed to the repo and registered as an artifact. (source status: active)"
project: fleet
tags: [adlc, lifecycle, curriculum, roadmap, agent-foundry, certification, capstone, strategy]
---

# The Agent Development Life Cycle (ADLC), the definitive gameplan to a build-complex-apps agent

## Body

The Agent Development Life Cycle has three parts: an engine that runs on every task, a ladder the engine climbs, and a big loop where deployment feeds back into training.

The Engine, runs on every single task, and repeats forever:
1. Assign. The curriculum (STARS) hands the agent its next task.
2. Build. The agent builds it as one small slice.
3. Prove. It must pass verify.py green or a proving artifact. No proof, no credit (Mandate 7).
4. Capture. The lesson becomes an atomic note in the Knowledge Core (Mandate 8).
5. Level up. The tracker (DREAMS) records the win and raises the score.
Then back to Assign for the next task.

The Ladder, climbed by running the engine over and over, bottom to top:
- Rung 1, Foundation, low-level heavy: C, C++, Rust, systems. The operator's heavy focus.
- Rung 2, Architecture: distributed systems, databases, security. The Uber and TikTok backbone.
- Rung 3, Integration (Capstone): build a whole small app from nothing, then a bigger one.
- Rung 4, Certification: DREAMS confirms the foundation, architecture, and whole-app skills are proven. Green light.
- Rung 5, Deployment: packaged in the Agent Foundry as a callable program, so "build me a fintech app" routes to it.

The Big Loop, so it compounds:
Deployment is not the end. A deployed agent takes real build requests, each real job is captured as notes and becomes the next, harder training, which feeds back into the engine. Real work and training become the same loop.

The systems (the pipes):
- STARS, the curriculum, what to learn next.
- DREAMS, the tracker, how far along and the score.
- Knowledge Core, the memory, atomic notes so nothing is relearned.
- GitHub repo, the single source of truth, nothing lost.
- Proof gates, verify.py and Mandate 7, only proven work counts.

Honest framing: this is a climb, not a switch. Simple real-time multi-user apps come early. A full production Uber is the top. The low-level heavy foundation makes every rung above it faster, safer, and higher quality.

To do on the next machine session:
- Commit the infographic (delivered to the operator this session) into the repo, for example reports/agent_development_lifecycle.html, and register it in the artifact registry as "Agent Development Life Cycle."
- Add the architecture track and the capstone track to the curricula, alongside the low-level-heavy foundation.
- Define the graduation bar in DREAMS that certifies an agent as ready to build complex apps.

## Links

- extends: 2026-08-06-does-training-translate-to-building-complex-apps
- relates-to: 2026-08-06-cross-agent-stars-dreams-curriculum-design
