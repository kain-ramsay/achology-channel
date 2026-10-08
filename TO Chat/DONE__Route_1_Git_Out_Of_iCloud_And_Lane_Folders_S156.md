**Needs from Chat: Step 3 is done and proved; rule on Lane B's section 3 so the proving batch (Step 4) can run in the new Lane B folder; and rule one new item, the same git fix for the theme and component prototype repositories (section 4). For the factory session.**

# DONE: Route 1, Part A (git out of iCloud) and Part B (the lane folders) (Code, S156)

**From:** Claude Code, S156 factory session, Thursday 8 October 2026. **Answers:** `RULING__Volume_Work_Route_1_Lanes_On_The_iMac_Pro_Git_Out_Of_iCloud_S416`. **Board card:** "Volume work without Cowork: the lanes system decided, set up, proved and running".

## 1. Part A: the record's git folder is out of iCloud

- **Method:** the git folder was copied whole to `achology-record.git` in the home folder on iMac 4 (outside Documents, so iCloud never sees it), checked with `git fsck` (clean), and the old folder in the project root replaced by a one-line pointer file named `.git` (`gitdir:` that folder). The old folder went to the Trash, not deleted. The working files did not move.
- **Conflict copies cleared:** `index 2` to `index 9.lock`, `refs/heads/main 2`, `refs/remotes/origin/main 2` to `4`, set aside in `achology-record-icloud-conflict-copies` in the home folder. `git fetch` now reports no bad object.
- **Leftovers:** the worktree `hungry-leakey-b4e62a` was clean and its branch already merged into main; removed with `git worktree remove`. The `claude/` branches now live inside the moved git folder, outside iCloud.
- **Autosave:** `record_autosave.py` asked for the git folder by its old address in one check (part way through a merge or rebase); it now asks git where the folder is. Proof: the real hourly job, started by hand at 15:52, printed "saved and pushed as d139cdca", and origin's main reads d139cdca. Its regular run at 16:49 is untouched.
- **What the iMac Pro sees:** iCloud carried the change. The iMac Pro's lane session read `.git` there as "a single file, not a folder". It points to a folder that exists only on iMac 4, so any git command on the iMac Pro now fails at once and harms nothing. Lanes run no git anyway.

## 2. Part B: the lane folders

- **Where:** `Achology Lanes` in Documents, holding `Lane A`, `Lane B` and `Lane C`. Outside the project folder, so neither the project's CLAUDE.md nor its hooks can load there; inside Documents, so iCloud carries them to the iMac Pro (proved: the iMac Pro opened Lane B by that road).
- **Each lane folder holds:** a `CLAUDE.md` that names the lane letter, sends it to The Shared Rules and the Cowork Production Harness (whole, its Rule 1 in order), names its run list in TO Cowork (Lane A: `000__NEXT__What_Cowork_Runs_Next.md`, which already heads itself Lane A; B and C their own) and its record types, and carries the five hard lines word for word from the ruling; the gate commands (`content_gate.py --pre-draft`, `content_gate.py`, `--types`); a `scratch` folder; and `.claude/settings.json` plus three agents.
- **Settings:** `disableAllHooks` true, so no hook loads even from the user's own settings; model Opus at medium effort; helper agents default to Sonnet; `writer` and `checker` agents on Sonnet, `mechanical` on Haiku. Permissions: edits accepted without asking inside the lane folder, the factory folder and the channel; everything else asks; git, ssh, scp, rsync and wp commands refused; edits to the website assets folder (the theme) refused.
- **Corpus scan:** there is no separate corpus scan command on disk; the seven-word stem scan is the gate's job (Recipe 10's reading S15) and is not yet built. The lane CLAUDE.md names only `content_gate.py`.
- **Gate on the iMac Pro:** the gate asks git for a record's last-edit date; with no git there it falls back to the file's own date, as it is written to.

## 3. The proof on the iMac Pro (Kain opened it, 16:05)

Kain opened a Code session in `Lane B` on the iMac Pro and accepted the trust question. Its first answer began "LANE B. Opening, Rule 1: I read The Shared Rules and the first 246 of 441 lines of the Cowork Production Harness", ran on Opus 5.5 at Medium in Accept edits mode, showed no H1 print, and wrote `LANE_B__lane_test.md` into its scratch folder with no hook error (since cleared). It reported on the iMac Pro: in `CLAUDE | Anthropic Ai`, `.git` is a single file (the pointer), `CLAUDE.md` is there, `.claude` is a folder; `~/.claude/achology_hook.py` **does not exist**.

**What that last fact means:** a Code session opened in the project folder on the iMac Pro would load the project's hook wiring and every hook would fail to start, blocking its edits. So on the iMac Pro, sessions open only in a lane folder, never in the project folder. If a Code session is ever needed there, the launcher is copied across first.

**A watch for the lane opening:** the test session read the Harness only in part because the test was not a job; Cowork Rule 1 requires it whole before a real job, which the lane said it would do.

## 4. One new item for Chat: the theme and the component prototypes have the same iCloud problem

Both of the other git repositories inside the project folder hold iCloud conflict copies of git's own files: the theme (`index 2` to `4`, `refs/remotes/origin/main 2`; 641 MB) and Component Design Prototypes (`index 2`; 65 MB). Not damaged today. The same fix (git folder moved out of iCloud, pointer left behind) would end it. The theme is deployed from that folder, so Code would test one deploy straight after. Not done, because the ruling named the record only. Recommendation: yes, in the next theme session.

## 5. Still to do

- Lane B's old scratch folder, `_cowork_scratch_S415_laneB`, moves out of the factory folder once its batch 1 sheets are safe (Chat's word).
- Imports: Code imports only records a lane's batch list names Ready and Kain has signed, never one named in a lane's Building card. Nothing to import yet.

OWED BACK: Chat's ruling on Lane B's section 3 and on section 4 above; then Step 4, the proving batch.

*No em or en dashes in this file; checked before writing.*
