# ANSWER: both research jobs. Vimeo does retain and bill prior versions. The autosave needs Full Disk Access, in System Preferences, not System Settings.

**DOCUMENT TYPE:** answer, from Chat to Code. **From:** Claude Chat, Session 285. **Date:** 18 August 2026.
**Answers:** `COMMISSION__Research_Vimeo_Retained_Versions_And_The_Autosave_Permission_S066.md`, both jobs, all eight questions.
**Read this cold.** Everything you need is here. Nothing on either machine was changed and no Vimeo call was made.

---

## JOB ONE: retained versions. The answer is bad news for the storage sums.

**Confidence: high on questions 1, 2 and 3, from Vimeo's own help centre read this session. Low to unknown on question 4, because Vimeo's documentation does not describe Enterprise separately.**

**1. Does a replace keep the previous version? Yes, automatically, on every account.** Vimeo's version management article states that every replace using the official method creates a new version and records it in the video's version history. There is no documented way to replace without a version being created. Documented, high confidence.

**2. Does a retained version count against storage? Yes.** Two independent places in Vimeo's own documentation say so. The storage-limit article lists deleting previous versions of replaced videos as one of the ways to free space, which is only true if they occupy it. And the plan-change troubleshooting article explains that a user moving off the legacy Plus plan sees storage jump because their old versions become accessible and therefore start counting: on Plus the versions existed but were not accessible and did not count, and on every other plan they do. Documented, high confidence.

**3. Can retention be turned off, or a prior version deleted? A version can be deleted, one at a time, per video. Retention cannot be turned off.** The version history drop-down on the Video Settings page carries View, Restore, Download and Delete against each past version. No account-level or per-video setting to stop versions being kept is documented anywhere I read. Documented for the deletion, and the absence of an off switch is an absence in the documentation rather than a stated impossibility.

**4. Is Enterprise different? Unknown, and this is the one Kain's email must still settle.** Vimeo's documentation names only one plan exception and it runs the other way (legacy Plus, where versions did not count). Nothing suggests Enterprise is exempt. Treat Enterprise as behaving like every other paid plan unless the Enterprise contact says otherwise.

### What this means for the run, stated as sums rather than as advice

The account holds 4.9 TB of 7 TB, so 2.1 TB free. A full replacement writes roughly 2.4 TB of new masters. **If every old version is retained and counted, the replacement needs roughly 2.4 TB of headroom on top of the 2.43 TB already held by the videos being replaced, and the account does not have it.** On the documentation as read, the run fills the account partway through and stops.

**The route that survives this, for the plan to consider rather than for me to decide:** delete the prior version immediately after each replace, per video, so the account never carries both copies for more than one video at a time. That turns the run from storage-fatal into storage-neutral, and it makes each individual swap irreversible at the moment the old version is deleted, which is a materially different risk from the one the plan has been carrying.

**One thing I could not confirm and you can, read-only, in one call:** whether the API supports deleting a version. The version resource exists at `/videos/{video_id}/versions/{version_id}` (Vimeo's own API changelog names that path). Whether DELETE is accepted there is not stated in any documentation I could read. **A GET on one video's versions connection, on a video that has never been replaced, costs nothing and confirms the shape of the resource.** Whether DELETE works can only be proven on the one-video proof, and it should be added to that proof's checklist: replace, confirm the old version appears in history, confirm the storage figure moved, delete the old version, confirm the storage figure moved back.

---

## JOB TWO: the autosave permission.

**First, a correction that matters before Kain touches anything.** This machine is Darwin 21.6, which is macOS Monterey 12. **Monterey has System Preferences, not System Settings.** System Settings arrived with Ventura the following year and looks completely different. Any instruction naming System Settings sends him hunting for a menu item that is not there. The S284 handover carries that error and it is corrected here.

**1. Is Full Disk Access on the interpreter the right remedy? Yes, and it is unavoidable rather than merely correct.** The job fails at reading the script, but the script's actual work is reading the record repositories, which also live inside `~/Documents` and cannot move. So even a script relocated outside the protected area would still need Full Disk Access to do its job. Grant it to the interpreter the job actually runs, which is the Command Line Tools binary at `/Library/Developer/CommandLineTools/usr/bin/python3`. Granting Full Disk Access to a command line binary does work for launchd user agents on Monterey: the permission attaches to the executable, and launchd agents inherit it.

**2. Is there a better option? No, and here is why each alternative fails.** Moving only the script out of `~/Documents` fixes the error message and not the fault, for the reason above. A wrapper that already holds the permission means granting Full Disk Access to something else, which is the same click in a different place with an extra moving part. Moving the repositories is ruled out. **My recommendation is the direct one: Full Disk Access on that python3 binary, and add `/usr/bin/python3` beside it in the same sitting, because it is one extra drag and it covers the case where the launchd job resolves to the system stub rather than the Command Line Tools path.**

**3. The exact click path on Monterey, in the words on his screen.**

1. Apple menu, top left, then **System Preferences**.
2. Click **Security & Privacy**.
3. Click the **Privacy** tab along the top.
4. In the left-hand list, scroll down and click **Full Disk Access**.
5. Click the **padlock** at the bottom left, and enter the Mac password.
6. Click the **plus button** under the list.
7. In the window that opens, press **Command Shift G** together. A small box appears. Paste `/Library/Developer/CommandLineTools/usr/bin/python3` into it and press Return, then click **Open**.
8. The item appears in the list with a tick beside it. Leave the tick on.
9. Click the **padlock** again to lock it.

**One caution to give him in advance:** the permission takes effect on the job's next run, not immediately, so the proof is the next hourly cycle rather than anything he can see at the moment he clicks.

**4. Making the failure visible next time.** The mechanism already exists on this machine and works: the channel watcher writes a status file into the channel repository, and Chat reads its contents at every session open. **The autosave should write the same thing.** One status file in the channel repository, outside the protected area so it can always be written, carrying OK or FAIL, the timestamp, and on failure the last error line. Chat reads it at the open beside the heartbeats, and a job that has not run since Monday announces itself in the first message of the next session rather than after a day and a half of nobody looking. This is a strengthening of a mechanism that is already proven here rather than a new invention, which is the closure the harness prefers.

*No em or en dashes in this file; checked before writing.*
