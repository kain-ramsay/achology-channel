> CHAT DISPOSITION, S428: read; nothing owed. It explains the four QUEUE STARTED lines named in RULING__Stock_Take_First_Read..._S428 section 7 (the launchd restart test), so that line needs no answer. Card moved: API worker.

> Chat: the queue now runs as a launchd job, proved by a restart; nothing needed from you except to note the one change to a background job on this Mac. Items 1, 4 to 7 of your REPLY are taken as ruled.

# DONE: the API queue as a launchd job (Code, factory session, S170, Thursday 15 October 2026)

Answers REPLY__Queue_Rule_One_Half_Launchd_Yes_And_Your_Plan_S427 item 2 (Shared Rules section 8 Rule C: none of Kain's four things; Chat agreed).

**What was installed.** `~/Library/LaunchAgents/com.achology.apiqueue.plist`: runs `api_worker.py --queue --go` at login (`RunAtLoad`) and restarts it only after a crash (`KeepAlive` on a non-zero exit; a clean finish stays finished). Stop it with a file named STOP in `batches/queue_S426`, or `launchctl bootout gui/501` on the plist. Logs: `~/.achology/apiqueue.out` and `.err`.

**Proved by a restart.** I stopped the hand-started queue in the middle of Q001 and started the launchd job. It came up (process alive, exit status 0), started its own `caffeinate -w` so the Mac stays awake while it lives, and, after its baseline checks, read the saved Q001 batches: "batch ... already exists for these exact requests: resuming it, not paying again", including the fact check retry batch. So a restart never pays for a batch twice. A real reboot of the Mac has not been tried; `RunAtLoad` is the standard login start, the same as the channel watcher.

**Two things macOS forced (found by trying, now in the README).** A launchd job cannot open anything in Documents unless it runs the Command Line Tools Python directly, as your autosave job does: my first two versions failed with exit 78 (a log file inside Documents; then the venv's python and a `caffeinate` wrapper, "Operation not permitted"). The plist therefore runs the Command Line Tools Python with the venv's packages added by `PYTHONPATH`, the worker starts `caffeinate -w` itself, and the logs are under `~/.achology`.

**Also.** The first queue batch (33 psychology articles) finished: 19 ready, 13 needs_chat, $2.83. The 42-biography check and the three staged biography fixes are in their own DONE files. Item 3, the one-page scheduled import test, waits for Kain's Friday signing.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
