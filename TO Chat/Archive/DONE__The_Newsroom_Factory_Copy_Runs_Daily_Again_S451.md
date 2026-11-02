ARCHIVED, Chat S452 (2 November 2026): answers the S451 ASK; nothing owed.

> Chat: nothing owed. This answers ASK__The_Newsroom_Factory_Copy_Stopped_On_22_October_S451.

# DONE: the newsroom factory copy runs daily again (Code, factory session, S203, Monday 2 November 2026)

**What runs the copy.** `publish_factory_copy.py` in the Machine room of The Achology Newsroom. It had no schedule. Since S169 it ran only when a session ran it by hand ("at close is a good habit"), so the copy was made only by sessions that remembered to make it.

**Why it stopped.** No session ran it after S181 on 22 October. The move of The Achology Newsroom into the project folder at S434 broke nothing: every path the script reads exists, and today's run read them all. The "(unknown)" source on 9bd5227 came from that S181 run itself, which ran where the script could not read the project's git head or anything under the user Library. The same run left the record-autosave job definition out of the copy as "not found on this machine". Both are present in today's copy.

**What changed.**
- New background job `com.achology.newsroom-copy` (beside the two existing ones in the user LaunchAgents folder) runs `publish_factory_copy.py --push` every day at 19:00 and at each login, using the same Python as the record autosave job. A day with no machinery change publishes nothing, by the script's own rule.
- `publish_factory_copy.py`: one entry added to its list of outside files, so the copy also carries this new job's definition under `launcher/`. Nothing else in the script changed.
- The dedicated clone is now `~/achology-newsroom`, the script's own default, cloned by the script. The old `~/achology-factory` clone still points at the pre-rename address, was never updated by the S181 run, and is no longer used; it is left in place, untouched.

**The first new copy.** e863801, "Factory copy 2026-11-02 10:34 from achology-record 244b02e3", made by the scheduled job's own first run (not by hand), pushed to `kain-ramsay/achology-newsroom` main, remote head read back and matching. launchd reports the run exited 0 and lists the job with its daily 19:00 trigger.

**One note on "today's records".** The repository carries the Machine room's machinery (the gate, the importers, the rule documents, the packs, the API worker, the newsroom machine and the launcher files), never Content Records. That is the S169 design ("It never carries data"), unchanged here. If Chat wants the records in it too, that is a new ask.

Nothing touched any WordPress page and no request went to the build site.

*No em or en dashes in this file; checked before writing.*
