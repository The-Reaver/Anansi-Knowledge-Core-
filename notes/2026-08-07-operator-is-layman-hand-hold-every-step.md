---
id: 2026-08-07-operator-is-layman-hand-hold-every-step
type: note
status: ratified
source: operator directive, 2026-08-07 (source status: ratified by operator, 2026-08-07, reinforced)
project: fleet
tags: []
---

# Standing rule: the operator is a non-developer, hand-hold every technical step

## Body

The operator is a layman, not a developer. Every technical action given to the operator must be fully hand-held: name the exact application to open, the exact button to click, the exact command to type, and what the screen should show after each step so success and failure are obvious. Assume no prior knowledge of terminals, Python, git, or package managers. Never hand the operator a command that is likely to fail in his environment (for example a pip install that needs a Python version he does not have); choose the path with the fewest steps and the least that can break, and explain why in plain words. This applies to every agent and every session.

## Links

- 2026-08-07-brain-trust-verdict-and-vote-protocol
