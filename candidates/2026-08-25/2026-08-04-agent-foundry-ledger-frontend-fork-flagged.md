---
id: 2026-08-04-agent-foundry-ledger-frontend-fork-flagged
type: finding
status: candidate
source: this chat, 2026-08-04, flagged during the Agent Foundry code review, genuinely unresolved (source status: draft)
project: fleet
tags: [agent-foundry, anansi, decision-needed]
---

# Whether Agent Foundry Becomes the Anansi Ledger's Front End Is Still Undecided

## Body

Agent Foundry, structurally, is close to what a front end for the Anansi capability ledger would look like: it already tracks agent configuration (name, prompt, model). It does not track agent capability, meaning what an agent has learned, what has been proven, and what is reusable, which is exactly what the ledger spec captures. Whether Agent Foundry should become that front end, or whether the ledger should live somewhere else and Agent Foundry stays a separate, smaller tool, is a real fork. Abad has not ruled on it.

## Links

(none recorded in source)
