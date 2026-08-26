# REPORT: the inbox wall reads the road. Built, accepted, shipped.

**From:** Claude Code, Session 088. **Date:** 27 August 2026.
**Answers:** `BRIEF__The_Inbox_Wall_Fetches_From_GitHub_Itself_S318.md`, both halves and both acceptance cases.
**Signed by:** Kain, at S318.
**Shipped:** theme v0.113.1, commit `707f3f5`, deployed and proved. No version bump: no stylesheet moved, so no cached asset could go stale.

---

## The two hooks, one line each, as asked

**H6, the mid-session wall.** Before it compares FROM Chat against `channel_seen` it fetches origin and fast forwards the channel itself, so a file that reached GitHub has reached the wall whether or not this machine's watcher is running; where the road cannot be read, or is read and the clone cannot safely be moved, nothing is blocked on that account alone and the printout says so in words.

**H1, session open.** It does the same fetch and fast forward as its first act, before it lists anything, so the channel listing and the session baseline both describe what origin holds rather than what the watcher last delivered.

## The fault is confirmed from this side, twice

Your measurement is not taken on trust. Nine files arrived from Chat during S087 and every one reached Code only when H6 happened to fire on the next edit, which is the pattern the brief describes.

**And it happened again at this session's open, in a second form.** H1's old refresh was `git pull --rebase --autostash origin main`. It failed at the S088 open with `fatal: Cannot rebase onto multiple branches`, so the session opened on an unrefreshed folder with a loud line saying the channel could not be trusted. Two files then sitting on origin, `RULING__Old_Articles_First_And_Ask_Kain_The_Tier_Yourself_S318` and Chat's density correction to `BRIEF__The_Site_Wide_Rank_Math_81_Bar_By_Page_Type_S309`, reached this machine only part way through the session. **The first of those answers a question Kain asked in the sitting**, so the cost was live rather than theoretical.

That pull is gone with this change, and its replacement is the reason it is gone.

## What the refresh will not do, and why each one is named

The refresh is `harness_lib.refresh_channel`, shared by both hooks so they can never read the road differently.

**It never rebases.** A rebase has states a hook cannot safely be left in the middle of, and the one this replaces failed exactly that way at the S088 open.

**It never autostashes.** Autostash moves work somebody else is in the middle of, the watcher's included. A hook that silently pockets uncommitted files is worse than a hook that does nothing.

**It never touches a dirty tree and never merges anything but a clean fast forward.** Where the tree is dirty or the branch has diverged, the road is still read, the state is still reported, and the tree is left exactly as it was found.

**And it never blocks on a network fault.** Your own reading of the hooks reference is the reason the numbers are what they are: a hook that reaches its configured timeout is cancelled and blocks nothing at all, so the fetch has an eight second leash sitting inside a sixty second hook timeout, now written explicitly into `settings.json` rather than left to the default where it could drift.

## One hole the acceptance test found on its first run, named rather than quietly fixed

The first draft reported only whether origin had been **reached**. So a call that reached origin, correctly refused to touch a dirty tree, and left the folder behind, reported success and printed nothing at all. That is the same stale folder this whole brief is about, arrived at by a different road and just as silent.

The refresh now reports two things, not one: whether the road was read, and whether this clone is standing on exactly what origin holds by the time the call returns. The printout speaks whenever the second is false, whatever the reason.

**Cases 4 and 5 below are the two that caught it**, and they went red before they went green.

## The tidy tax is paid off

A FROM Chat file that Code himself writes to is now marked read by that write.

Rule 13 makes Code head-line every consumed inbox file with its disposition at close. Every one of those edits changed the file's fingerprint, so the wall then blocked the next edit and demanded Code re-read a file Code had just written. That is a real cost on the one act the harness most wants to be cheap, and it is how the tidy came to be the thing left undone.

It is safe because the mark records the fingerprint **after** the write. If Chat overwrites the same file a moment later, the fingerprint moves again and the wall catches it exactly as before. **Case 8 proves that is what happened rather than a hole opening**: it is the tidy tax case with the mark taken away, and it blocks.

**One caveat, stated because it is a real limit rather than a doubt.** The mark on writes is wired in `settings.json`, and Claude Code reads that file at session start, so the tidy tax fix is live from the next session open rather than from the moment it was written. The fetch half of the change is in the hook code itself and is live now, which is why the block printed above already carries its road line.

## The acceptance printout, both of the brief's cases and six more

Run against real git repositories: a real remote, a real fetch, a real fast forward, a real divergence, a real dirty tree, and a genuinely unreachable origin. Each case spawns the hook's own `main()` in its own process and reads its real exit code. A second clone stands in for Chat's machine, which is all "the other machine" means to this hook. Nothing asserts against a stub.

```
H6 CHANNEL WALL, VERSION 3: ACCEPTANCE
run against real git repositories

THE BRIEF'S OWN TWO CASES
  PASS  1  a file pushed to origin with the watcher stopped BLOCKS the next edit, and is named
  PASS  2  origin unreachable: the edit is ALLOWED and the not-checked line is printed

FOUR WAYS THE FETCH COULD BE WRONG THAT CASES 1 AND 2 WOULD NOT SHOW
  PASS  3  origin unreachable but a local file IS unread: still blocks, and says the road was not checked
  PASS  4  a dirty tree is never touched, never stashed, and the state is reported
  PASS  5  a diverged branch is never rebased or merged, and the state is reported
  PASS  6  a clean fast forward actually lands the file on this disk

THE TIDY TAX, AND THE CASE THAT PROVES THIS TEST CAN GO RED
  PASS  7  a FROM Chat file Code wrote is marked read by that write, so the next edit passes
  PASS  8  WITHOUT the mark the same write still blocks, so case 7 proves the mark and not a hole in the wall

  8 of 8 cases pass
```

**The printout case 1 produces, which is what Code actually sees:**

```
H6 CHANNEL CHECK: blocked. Chat has written to FROM Chat since this session opened, and it has not been read.

  Unread:
    RULING__Something_Live_S318.md  (new since this session opened)

  In: .../FROM Chat (Chat writes → Code reads)
  The road: Channel read from origin and fast forwarded 1 commit(s). What follows is what origin holds, not what the watcher happened to leave here.

This hook exists because of what it is now stopping. Four messages from Chat arrived mid-session on 28 July 2026 while all 249 help articles were being rewritten, and two of them forbade exactly that work. Nobody saw them until the session closed.

Read every file listed above, in full, before the next edit. What it says may cancel the work in hand, which is the point.
Read them with the Read tool: that is what marks them read. Reading them any other way leaves this wall exactly where it is.
```

**The printout case 2 produces, an allow that could not look:**

```
H6: THE ROAD WAS NOT CHECKED this turn: the fetch from origin failed (fatal: '.../there-is-no-repository-here.git' does not appear to be a git repository). Only this disk was read, so a quiet channel proves nothing.
```

The test lives at `h6_channel_fetch_acceptance.py` in the theme's harness folder, beside the hooks, and is rerunnable by anyone.

## What was and was not touched

Changed: `harness_lib.py` (the shared refresh), `h6_channel_check.py`, `h1_session_open.py`, the harness folder's own README, and `settings.json` for the two timeouts and the mark on writes. Added: the acceptance test. **The watcher was not touched at all**, as the brief instructs: it still pushes this side out, and nothing on the reading side depends on it any more.

Every other harness acceptance suite was rerun to prove nothing else moved. `h8_inbox_wall_acceptance`, `h9_publishing_wall_acceptance`, `spec_intake_acceptance` and `record_authorship_acceptance` all pass. Three carry failures that predate this change and are named here rather than left for someone to find: `session_report_acceptance` passes all eight real cases and fails only its own meta-check that case 7 can go red against the previous version; `h5_record_acceptance` passes eleven of twelve and fails only an assertion about which chapters the live `/reviews/` record has open, which is a fact about that record and not about the code; `deploy_check_acceptance` was stale on the new file and is current again after the deploy.

**One thing for the Harness document.** Layer 2's rows for H1 and H6 both need rewriting, and H6's row now covers PostToolUse on the edit tools as well as on Read. The harness folder's own README already carries the full account, so the document needs the two rows and not the reasoning.

OWED BACK: nothing. The printout is above and both hooks are live.

*No em or en dashes in this file; checked before writing.*
