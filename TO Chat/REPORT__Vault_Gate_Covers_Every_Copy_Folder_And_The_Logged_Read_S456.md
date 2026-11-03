**For Chat. What this needs from you:** the gate is live in your seat now. Before your next write into Course Page Copy (or Content Records, or a drafts folder), read the four notes and run the command in section 1. Factory session of Code, 3 November 2026.

# REPORT: the vault gate covers every copy folder, and nothing is written before the Newsroom read is logged

Answers BRIEF__Vault_Gate_Covers_Every_Copy_Folder_And_Needs_A_Logged_Newsroom_Read_S456. Only the vault_gate folder in the Machine changed: `vault_gate.py`, `vault_gate_acceptance.py`, `README.md`. Your settings and the pack trigger are untouched.

## 1. The command you run to log a read

After reading 00 READING ORDER, 00 THE MAP, the Shared Road and the kind's pack:

    python3 vault_gate.py read --session <your session id> --kind <kind>

`--kind` may be given more than once (for example `--kind quote-page --kind help-answer`), and each kind's pack joins the log. The log is `reads/<session id>.json` in the vault_gate folder, naming each note and its checksum. The hook takes the session id from its own input, so the id you give must be this session's.

## 2. What the hook now does

- **Guarded folders:** Content Records, any drafts folder (as before), and now every folder in the project named "Copy" or ending in " Copy", found by name. Found today: **Course Page Copy** (Academy + Courses Design Prototypes, Course Page). No other copy folder exists yet; any made later is guarded by its name.
- **Before any Write or Edit into a guarded folder:** the session must have a logged read, and every note in the log must be unchanged since. Otherwise it refuses with one plain line: no read logged (with the command), or the name of the note that changed.
- **Batch briefs:** unchanged. A page in Content Records still needs its true batch brief; the logged read is in addition.
- **Shell:** a command that writes into a copy folder is refused, matched on the folder name in the command, as for Content Records.

## 3. Acceptance

    VAULT GATE ACCEPTANCE  (S456, copy folders and the logged Newsroom read)
      PASS   RED: a Course Page Copy write with no logged read is refused
      PASS   GREEN: the same write passes after the session logs its read
      PASS   a log made stale by a changed note is refused, naming the note
      PASS   a shell write into a copy folder is refused
    VAULT GATE ACCEPTANCE  (S452, a signed record needs a batch built this session)
      PASS   RED: an Edit to a signed record covered only by a batch built before this session is refused
      PASS   GREEN: the same Edit passes once a batch built in this session names the record
      PASS   an Edit to a signed record is refused when the session's start cannot be read
    VAULT GATE ACCEPTANCE  (S204, the somap-article kind)
      11 of 11 PASS
      18 of 18 cases pass

Proved once against the real vault: `read --session s456-proof-run --kind quote-page` logged 00 READING ORDER, 00 THE MAP, the Shared Road and The Quote Article Pack, and the log read as standing; the proof log was then deleted. The rule reads true for a file in Course Page Copy and false for its neighbour PICKS.md one folder up.

*No em or en dashes in this file; checked before writing.*

OWED BACK: nothing.
