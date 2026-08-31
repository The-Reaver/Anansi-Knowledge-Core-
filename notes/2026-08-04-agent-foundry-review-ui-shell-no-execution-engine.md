---
id: 2026-08-04-agent-foundry-review-ui-shell-no-execution-engine
type: finding
status: ratified
source: "this chat, 2026-08-04, direct code review of the Agent Foundry Lovable project (source status: active)"
project: fleet
tags: [agent-foundry, lovable, build-outcome]
---

# Agent Foundry Is a UI Shell Over Database Tables, Not Yet an Agent Platform

## Body

Agent Foundry describes itself as an enterprise AI agent workspace for building, managing, and running AI agents. What actually exists is CRUD screens over four Supabase tables (agents, tasks, knowledge, dashboard counts), with authentication properly gated server-side. Every service function is a direct database read or write carrying a "MIGRATION POINT: Replace with fetch('/api/...')" comment. Nothing in the app calls an LLM and nothing executes a task; an "agent" today is a database row with a name, a system prompt, a model field, and a temperature. The app's own internal branding says "AgentWorks," not "Agent Foundry." No project knowledge notes exist for it, unlike SafeGuard Identity.

## Links

- touches: 2026-08-04-safeguard-identity-review-real-and-engineered
