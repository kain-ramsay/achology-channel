**For Code (factory). What this needs from you:** know that every paid Claude call in The Machine now stops unless its batch brief was built from the vault, and fix the API worker's record path, which points at a folder that no longer exists.

# NOTE: the vault gate guards every paid copy run (Chat, S444, 25 October 2026)

Read from the vault first: 00 READING ORDER and 00 THE MAP in The Newsroom; the gate's own README in the vault_gate folder in The Machine.

## What changed, on Kain's yes

Kain asked for a gate that makes it impossible to draft or edit copy without the process defined in the vault. Chat built it this session:

1. **vault_gate.py** (a new vault_gate folder in The Machine) builds a batch brief by walking 00 READING ORDER for the kind, writes it with a READING_LIST.json naming every note used and its checksum, and holds any page with no record or no stances.
2. **require()** is now called before every paid Claude call: in the API worker's get_client (which covers the worker, its fix scripts and its stance scripts), in the newsroom machine's call, and in the fact check trial's Claude call. A run needs the environment variable ACHOLOGY_VAULT_BATCH naming a batch whose brief is still true to the vault, stances and records, or it stops before connecting.
3. Chat's seat has a hook that blocks writing into Content Records or any drafts folder without a covering brief. Code's sessions are not under that hook.

Shown blocking on 25 October: no brief, a made-up brief, a hand-edited brief. A true brief passes.

## The fault found while testing

`api_worker.py --selftest` fails before reaching the gate: RECORDS is built from The Machine's own folder plus "Content Records", but the records live in The Stock since the S434 move. Every real run would fail the same way. Please point RECORDS (and any reading-list "records" paths) at The Stock's Content Records folder, by finding it by name, and rerun the self-test.

## What is retired

Queue item 1 of the S442 queue (the proof run on the quote page "Why We Keep Looking One Level Deeper Than You Need") is withdrawn: Kain has dropped that test. Do not rerun it.

**OWED BACK:** a DONE in TO Chat when the record path is fixed and the self-test passes, quoting its last line.
