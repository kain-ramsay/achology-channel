> Chat: nothing owed unless you want to overturn one of the three choices below; this closes the factory copy half of RULING__First_API_Batch_Named_Factory_Copy_Yes_And_Three_Gate_Lines_S425.

# DONE: the achology-factory copy script, and the first push (Code, factory session, S169, Thursday 15 October 2026)

**Done and read back.** `publish_factory_copy.py` is in the Content Production Factory folder. The first copy is published to the private repository `kain-ramsay/achology-factory`: remote head 4450b8d equals the local head; 384 files in the remote tree (381 copied, plus the generated README, .gitignore and MANIFEST.sha256).

**Why:** Kain asked for the factory to be locked down and versioned (S169). The record repository's .gitignore leaves the Content Type Packs and the api_worker folder out of git, so they were in iCloud and nowhere else.

**What it copies:** the 29 top-level scripts (not underscore scratch), the two json files, the six `000__` rule documents, the whole Content Type Packs folder, and the api_worker folder without its runs. **Never:** Content Records, the channel, run output, scratch, anything over 5 MB, any file named like a key. Nothing moved or changed path.

**Safety it carries, each tested by `--selftest` against a throwaway fixture and a local bare repo:** the destination must be a dedicated clone with the right remote; every file is scanned for an Anthropic key and one hit aborts before anything is written (it caught its own source on the first real run, which I fixed); every copy is hashed against its source; after a push the remote head is read back; an unchanged source makes no commit; a deleted source file leaves the copy.

**How to run it again** (any session, at close is a good habit): `python3 publish_factory_copy.py` shows what changed and publishes nothing; add `--push` to publish. The copy lives at `~/achology-factory`, outside iCloud, and is generated, never hand edited.

**Three choices of mine, for you to overturn:**
1. The six `000__` rule documents (the Standard, this harness, the pipeline, the defect register, the search brief, the folder guide) are in the copy as a labelled snapshot. If you would rather the Standard have no second copy anywhere, set `INCLUDE_RULE_DOCS` to False at the top of the script and the next copy removes them.
2. The Pack proof folders (`PROOF__Ten_Articles_S423`) are inside the copy because they sit inside the packs and you said to copy the packs. They hold article text.
3. The copy is run by hand, not on a timer. A timer is a separate change.

**Not in this repository, and the next candidates:** the hook launcher `~/.claude/achology_hook.py` and the lanes' own instruction folders. I have not looked at either yet.

**Still owed from the same ruling, not done this session:** the first API batch (waits on Kain's key file; the sixteen go into `api_worker/batches/first_batch.txt` then), and the three gate lines with a test each. I have not touched `content_gate.py`.

OWED BACK: none.

*No em or en dashes in this file; checked before writing.*
