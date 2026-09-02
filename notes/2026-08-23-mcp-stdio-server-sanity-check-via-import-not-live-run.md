---
id: 2026-08-23-mcp-stdio-server-sanity-check-via-import-not-live-run
type: finding
status: ratified
ratified: "2026-08-23 — operator directly ratified via explicit operator instruction (\"promote and push\"), given after the operator's own prior pattern of requesting review before ratification in this session and after a review confirming all 5 accurate, cross-references resolved, and no injection/security concern in the flagged subagent output."
project: fleet
tags: [mcp, anansi, python, gotcha, verification, stdio]
sources:
  - ref: "Operator's message includes 'python anansi_mcp.py'; assistant flags that running it directly won't print anything useful since it's an MCP stdio server that sits waiting for JSON-RPC on stdin and looks 'stuck', offers an import/syntax check instead; operator says 'check it with an import check'; assistant confirms syntax and import both clean with no server-loop side effects"
    reliability: high
    origin: "2026-08-21 live session; provenance backfilled and verified 2026-08-25"
provenance:
  archive: research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl
  turns: [940, 950]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# An MCP stdio server script should be sanity-checked with a plain Python import, not by running it directly in a terminal, since running it directly just makes it sit waiting on stdin and looks stuck
- class: confirmed
- source: this session (STAG repo, 2026-08-23), raw archive research/knowledge-home/raw/2026-08-21-live-f810b6ef.jsonl lines 901-978
- confidence: high, directly executed both checks and observed the results
- verified: 2026-08-23

## Body

The operator asked to run `python anansi_mcp.py` directly to check it. Before doing that, it was flagged that this would not produce a useful result: `anansi_mcp.py` is an MCP stdio server, so launched standalone in a terminal it does not print anything or exit — it sits waiting for JSON-RPC messages on its standard input and looks "stuck," which is normal behavior for this kind of process, not a bug. It is only meant to be spawned by its host (Claude Code) as a subprocess, which was already happening automatically via its existing registration.

The safe alternative used instead, at the operator's direction: an import check rather than a live run. `python -m py_compile` (or equivalent syntax check) confirmed the file parses with no errors, and `python -c "import anansi_mcp"` completed with zero output — no exceptions and no unwanted side effects, meaning importing the module alone does not start the server loop. This is possible specifically because the file's server-start code is guarded behind an `if __name__ == "__main__":` block; that guard is what makes a plain import silent rather than hanging, and is worth confirming is present before trusting an import-only check to be side-effect-free on any similar script.

General technique for future sessions: to sanity-check any Python MCP stdio server (or similar long-running stdio/socket-listening script) without actually running its main loop, use a syntax check plus a bare `import` of the module, and confirm its entry point is guarded by `if __name__ == "__main__":` rather than executing top-level.

## Links
- relates, 2026-08-21-mcp-server-registration-mid-session-requires-restart-to-take-effect.md, a different MCP-related gotcha from the same registration effort (session-restart timing rather than how to safely inspect the server script itself).
- relates, 2026-08-08-anansi-reaches-every-tool-through-one-mcp-server-and-the-das.md, describes anansi_mcp.py's two-backend design (Hub-if-running, else direct anansi_hub import) that this import check confirmed still parses and imports cleanly.
