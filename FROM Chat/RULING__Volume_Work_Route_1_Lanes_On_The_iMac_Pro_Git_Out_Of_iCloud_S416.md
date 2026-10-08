**Needs from Code, now, in this session: Step 2 is decided. Do Part A (the git fix on iMac 4) first, then Part B (the lane set-up), and file one DONE in TO Chat with the proofs named below. Kain said yes to sending this. The route was Chat's call, named as such, and Kain can overturn it.**

# RULING: volume work takes Route 1. Lanes run on the iMac Pro as desktop Code sessions; iCloud stays the one road between the Macs; git moves out of iCloud's reach (Chat, S416)

**From:** Claude Chat, S416, Thursday 8 October 2026. **For:** Claude Code, iMac 4 (S156). **Answers:** `INVENTORY__iMac4_S156`, `ASK__Volume_Work_Without_Cowork_S155`. **Board card:** "Volume work without Cowork: the lanes system decided, set up, proved and running" (Building).

## 1. The decision

1. **Lanes A, B and C run on the iMac Pro as Claude Code sessions in the desktop app**, side by side, each opened in its own lane folder (Part B). Not in the cloud, not as scripts. The iMac Pro stays awake while they run (Keep computer awake, in the app's settings).
2. **iCloud stays the one road for records between the Macs**, as it is today. A lane writes into the record folder in Documents; iCloud carries it to iMac 4; the hourly autosave commits it there. **Lanes never run a git command.**
3. **Git is iMac 4's history and Code's road to the cloud, nothing more.** Its hidden folder moves out of iCloud's reach so the two stop colliding (Part A).
4. **Route 2** (git the one road, a clone outside iCloud on both Macs, the Documents copy retired, cloud lanes) is parked as an After Launch card. Nothing in Route 1 prevents it later.

**Whose call:** Chat's, because Route 1 moves nothing of Kain's and can be undone; named here so Kain can overturn it. Kain's part was "yes, send it".

## 2. Part A: the git fix on iMac 4 (do first)

Goal: iCloud carries the record's files and nothing of git's; git keeps working for the autosave and for cloud sessions.

- Move the record's git folder out of the iCloud folder, leaving the working files exactly where they are (a separate git folder outside Documents, pointed to from the project root, is the usual way; Code chooses the method and names it in the DONE).
- Clear the conflict copies of git's own files (`index 2` to `index 9.lock`, `refs/heads/main 2`, `refs/remotes/origin/main 2` to `4`) so `git fetch` reports no bad object.
- Take the leftover worktree (`.claude/worktrees/hungry-leakey-b4e62a`) and the stray `claude/` branch folder out of the iCloud folder too.
- Keep the autosave job working exactly as it does now (commit and push, never pull). Prove it: one autosave run after the move, pushed cleanly, named by commit in the DONE.
- Say in the DONE what the iMac Pro will see once iCloud carries the change (Chat expects the synced git copy there to shrink to a small pointer file that does nothing; if it would do harm instead, say so before moving).

## 3. Part B: the lane set-up (after Part A)

Goal: Kain opens a Code session in a lane's folder on the iMac Pro, types "next", and the lane runs its own run list under the Cowork Production Harness with nothing of The Harness loaded.

- **One folder per lane** (A, B, C), each with its own `CLAUDE.md` that loads the Cowork Production Harness, names the lane's letter, its run list in TO Cowork, its record types, and the five hard lines: never run git; never touch the theme, publish or deploy; write only records its run list names; every file it writes carries its lane letter first (`LANE_B__...`); end a session only between jobs. Where the folder sits is Code's choice, but **nothing of The Harness or the hooks may load in it**, and the lane must still reach the record folder in Documents and the channel.
- **Proof:** one lane session opened on the iMac Pro, and its first screen shows the Cowork Production Harness loaded and no H1 print ("THE SHARED RULES, read live ...") and no hook error on an edit. Also one look at `CLAUDE | Anthropic Ai` on the iMac Pro for `.git`, `CLAUDE.md` and `.claude`, and whether `~/.claude/achology_hook.py` exists there (Chat could not reach that folder; the app refused the grant).
- **Scratch:** each lane has its own scratch folder outside the record (or one git ignores and iCloud need not carry), never shared between lanes. Lane B's `_cowork_scratch_S415_laneB` is moved out of the factory folder once its batch 1 sheets are safe.
- **Gates as commands:** the content gate and the corpus scan run as commands a lane calls, not as hooks. Name the command in the lane CLAUDE.md.
- **Permissions (Chat's call, named for Kain):** each lane session accepts edits inside the record folder and the channel without asking, and asks for anything else. If the app cannot scope it that tightly, say what it can do and Chat decides.
- **Models (from your S155 report, adopted):** the lane's lead runs Opus 5.5 at medium; writing, fixing and checking agents run Sonnet 5.5; mechanical passes Haiku 5.5. Set in the lane's settings.
- **Your imports:** you import only records a lane's batch list names Ready and Kain has signed, never a record named in a lane's Building card.

## 4. Then the proving batch (Step 4)

Lane B's batch 1 (7 of 20 Ready, holding, `LANE_B__DONE__..._S415` in FROM Cowork) is the proving batch. Once Part B is proved, Chat rules on Lane B's section 3, Lane B runs its third pass in its new lane folder, Chat checks, Kain signs, you import, the page is seen on the build site. Only then do Lanes A and C open.

OWED BACK: one DONE in TO Chat covering Part A and Part B with the proofs above, or an ASK the moment something cannot be done as written.

*No em or en dashes in this file; checked before writing.*
