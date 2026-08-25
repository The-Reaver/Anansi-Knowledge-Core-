---
id: 2026-08-04-device-folder-access-repeatedly-failed
type: finding
status: ratified
source: this chat, 2026-08-04, repeated device_request_folder_access attempts across the session (source status: active)
project: fleet
tags: [device-bridge, blocked, finding]
---

# Real Stag Repo Was Never Reached This Session, Folder Access Timed Out Every Attempt

## Body

Every attempt this session to get write access to Abad's real stag repo (C:\Users\abadm\stag) via the device folder-access dialog timed out, at least five separate times across the session. This is not a rejection by Abad; the dialog itself never got a response in time, likely due to the device bridge intermittently disconnecting. The practical consequence: nothing was written directly into the real stag repo this entire session. Mandate 9's text, the Anansi ledger spec, and the actual ledger code all exist only as session-delivered files and in this session's own memory, not in the real repo.

## Links

- affects: 2026-08-04-anansi-ledger-real-red-green-proof-not-yet-run
