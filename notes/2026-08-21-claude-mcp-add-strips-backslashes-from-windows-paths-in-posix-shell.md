---
id: 2026-08-21-claude-mcp-add-strips-backslashes-from-windows-paths-in-posix-shell
type: finding
status: ratified
ratified: "2026-08-26 — Brain Trust + Augustin + AJ review (7 independent seats: Celestina, Elijah, Oluwole, Jasiah, Sentinel, Augustin, AJ), promoted as-is. Operator retains veto per Mandate 1."
project: fleet
tags: [claude-code, mcp, windows, shell, bash, anansi, gotcha]
sources:
  - ref: "Turn 2: assistant runs `claude mcp add anansi --scope user -- python C:\\Users\\abadm\\stag\\anansi_mcp.py` from the Bash (Git Bash/POSIX sh) tool; `claude mcp get anansi` afterward shows Args stripped to `C:Usersabadmstaganansi_mcp.py`, confirming the backslashes were silently consumed by the shell's escaping, and the server fails with a -32000 Connection closed error until re-added with forward slashes."
    reliability: high
    origin: "STAG session, 2026-08-21, \"Anansi local API + MCP registration\""
provenance:
  archive: research/knowledge-home/raw/2026-08-21-anansi-hub-mcp-setup-and-closeout.jsonl
  turns: [2, 2]
risk_class: B
evidence_state: SUPPORTED
source_rating: F6
next_review: 2027-02-25
classified: 2026-08-29
---

# `claude mcp add` run from a POSIX shell silently strips backslashes from a Windows path argument
- class: confirmed
- source: STAG session, 2026-08-21, "Anansi local API + MCP registration"
- confidence: high, directly reproduced and fixed in this session
- verified: 2026-08-21

## Body

Running `claude mcp add anansi --scope user -- python C:\Users\abadm\stag\anansi_mcp.py` from a POSIX/Git-Bash shell (the Bash tool in this environment, which runs Git Bash, not cmd.exe or PowerShell) silently consumed every backslash in the Windows path. `claude mcp get anansi` afterward showed `Args: C:Usersabadmstaganansi_mcp.py` — no slashes at all — and the server failed to connect with `-32000: MCP error -32000: Connection closed`. There was no error or warning at add-time; the command reported success and only the follow-up `claude mcp get` revealed the corrupted path.

The fix: re-run the add with forward slashes instead of backslashes (`python C:/Users/abadm/stag/anansi_mcp.py`), after first removing the broken entry with `claude mcp remove anansi -s user`. Windows accepts forward-slash paths natively, so this sidesteps the shell's backslash-escaping behavior entirely rather than fighting it with quoting.

Practical rule: after any `claude mcp add` for a stdio server on Windows run through a POSIX-style shell, always verify with `claude mcp get <name>` before assuming the registration is live — a "success" message from `add` does not guarantee the args survived escaping intact. Prefer forward-slash paths for the command args when adding from such a shell.

## Links
- extends, 2026-08-08-anansi-reaches-every-tool-through-one-mcp-server-and-the-das.md, this is the Windows-shell gotcha for the same MCP registration step described there.
