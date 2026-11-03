**For Code, factory session. What this needs from you:** widen the vault gate so no copy anywhere in the project is written by Chat's seat until that session has logged its Newsroom read, then report back with the gate's acceptance run.

# BRIEF: the vault gate covers every copy folder, and nothing is written before the Newsroom read is logged (Chat, S456, Branch 1, on Kain's yes)

**Read from the vault first:** 00 READING ORDER and the Shared Road in 17 Packs, so the read the gate asks for is the one the vault names. **Model line:** Sonnet 5.5 for the build and the acceptance run; no API calls.

## Why

Kain asked at S454 and S455 why this seat keeps writing without opening the Newsroom. The gate today blocks writes only into Content Records and folders with "drafts" in their name. Course Page Copy, in the Course Page design prototypes folder of the website assets, and the other copy folders are not guarded, so a session can write course copy, supporting lines or Help text with no Newsroom read at all. That is how copy reaches Kain that ignores the packs.

## What done looks like

1. **Every copy folder is guarded.** The gate's protected set covers, besides Content Records and drafts folders: every folder named Course Page Copy or ending in "Copy", and every copy folder the website assets and design prototypes hold. Find them by name, never by a path written into the rule; list the folders you added in your report.
2. **A logged Newsroom read is required first.** A new subcommand, for example `vault_gate.py read --session <id>`, is run by Chat after reading 00 READING ORDER, 00 THE MAP, the kind's pack and the Shared Road. It writes a small log naming the session, the notes read and their checksums. The hook refuses any Write or Edit into a guarded folder from a session with no log, or whose log is older than a change to any note it names, and prints one plain line saying which read is missing. The hook input carries `session_id`.
3. **Batch briefs still work as now.** A page inside a batch whose brief is true to the vault passes as today; the logged read is needed in addition, not instead.
4. **The shell path stays shut** for the new folders, as it is for Content Records. Match on the folder name in the command, as the current check does.
5. **Acceptance:** extend `vault_gate_acceptance.py` with four cases: a Course Page Copy write with no log is refused; the same write after a logged read passes; a log made stale by a changed note is refused; a shell write into a copy folder is refused. All pass, printed.
6. Update the gate's README to name the logged read and the wider folder set.

## Limits

Change only the vault_gate folder in the Machine. Do not touch Chat's settings, the pack trigger (Branch 1 changed it at S456 to print each pack once a session) or any copy file.

OWED BACK: a REPORT into TO Chat with the folders added, the acceptance printout, and the exact command Chat runs to log a read.

*No em or en dashes in this file; checked before writing.*
