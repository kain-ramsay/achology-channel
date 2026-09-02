# RULING: a session checks whether another session is already inside a file before it starts, and stands down if there is one

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Ruled by:** Kain, in the sitting.
**Filed under Harness Rule 14**, in the same session the ruling was given.
**This one reaches Chat as much as Code**, because Chat holds the document that owns it and this session cannot write that document itself.

---

## 1. The ruling, in his own words

Code put the question at the end of the collision described below:

> "My question from before still stands. Should I check for another session already inside a file before I start, and stand down if there is one?"

Kain:

> "yes, please do"

## 2. What it settles

**Before a change set begins, the session checks whether another live session is already working the same file, and stands down if one is.** It does not race, and it does not assume that being asked for a job means the job is unclaimed.

The check is cheap and already available: `ListAgents` names every live session on the machine, and `SendMessage` reaches one directly. Neither needs Kain, and neither is a question to him.

Standing down means saying so and stopping, not working around. Where the other session has stopped short of part of the job, that part is agreed between the two sessions before either touches the file.

## 3. What caused it

Two sessions were given the same job at the same time on the evening of 2 September: strip the nine em and en dashes from `rank-math-feed.php` in the Achology theme, bump the version, commit, deploy.

Neither knew about the other. Both edited the same file. Three separate faults came out of it:

**One.** The peer session's first deploy failed its own server-versus-local proof, because the file changed underneath it mid run. It had to deploy three times to get one clean result.

**Two.** The two sessions' edits landed in two different commits in `achology-theme`, neither of which says so. `8a50299` carries seven changed lines and they are all this session's. The peer's own two lines went in earlier, inside `c470113`, whose message reads "score_run.py: the promise that it saves nothing is now enforced, not stated" and whose diff carries two files: `tools/score_run.py`, and `rank-math-feed.php`, unmentioned. So the dash work is split across two commits, one of which does not admit to touching the file at all.

This paragraph was wrong when first written, was corrected by the peer session, and was then corrected twice more by checking. Set down exactly, because the shape of the error is the whole argument for section 4:

- The peer said its own work on this file went in under the v0.134.0 commit `2545fb3`. **That part is true.** `git log -S"lengthPermalink"` names `2545fb3` and nothing else, and `2545fb3`'s message describes its own diff correctly.
- What the peer asserted past, without looking, is what **else** was in `c470113`. Its message names `tools/score_run.py`. Its diff carries that file at 45 insertions and `rank-math-feed.php` at two insertions and two deletions, and those two lines are the other session's dash fixes, swallowed silently.
- This session then wrote that `2545fb3` "does not touch the file", which is also wrong: it touches the file, it simply does not touch those two lines. Corrected here.

So the fault is not that anybody misplaced their own work. **The fault, all three times, is describing a commit without reading what else was in it.** That is precisely what a gate printing the staged file list would put in front of the author before the message is written.

**Three, and the worst of them.** Two commits in the project record, `e1c1094` and `e74858b`, carry messages describing theme work and contain none of it. The theme folder is excluded from the record repository on purpose, at `.gitignore` line 95, so one file never has two owners. What those two commits actually hold is whatever else was staged at the time, which was Chat's own documents, swept in by a blanket `git add -A` and given a message about something else. That is a false line in a permanent record, not a mislabelled one.

The third fault was found in two steps, and the order matters because it is the argument for section 4. This session checked the record log, found no dash commit there, and told the peer that the record repository could not hold the theme at all. The peer then went and checked its own commits, found what they actually carried, and corrected them: `a7d44e4` in the record log names both commits and what each really carries, and `CORRECTION__Two_S096_Record_Commits_Describe_Theme_Work_They_Do_Not_Carry_S096.md` sits in this folder. Pushed history was not rewritten. Neither session found this alone.

## 4. What the ruling does not cover, and is worth Chat's judgement

**The commit message fault is a separate hole and this ruling does not close it.** Its cause is writing a commit message from what was done rather than from what was staged. Nothing in the harness checks that a commit message describes its own diff, and nothing would have caught it. A gate that reads the staged file list before the message is written would catch it every time, and it would be a machine test rather than a habit.

**It is wider than the record repository, which is why it deserves a gate rather than a habit.** The first two instances were in `achology-record`, where a blanket `git add -A` in a repository that deliberately excludes the theme swept up Chat's documents under a message about the theme. The third, `c470113`, is in `achology-theme` itself, where no exclusion was involved at all: the file was simply changed and the message did not mention it. Three false commit messages in one evening, in two repositories, from two sessions, by two different mechanisms.

**The fourth and fifth data points, and they are the strongest.** After being corrected once tonight, the peer session sent a correction of its own that asserted past what a commit contained, in good faith. Correcting that, this session then made the same class of error in the opposite direction, writing that `2545fb3` did not touch the file when it did.

Five wrong claims in one evening, from two sessions, in two repositories, by three different mechanisms. **Every single one was a statement about what a commit contained, written from recollection instead of from a diff.** Two of them were made after the author had already been corrected for exactly this, with the fault fresh in front of them, which is the strongest evidence available that attention is not the missing ingredient. A gate that prints the staged file list before the message is written would have caught all five.

**Where this ruling belongs is Chat's call, not Code's.** It binds Code today, and it plainly binds Cowork the moment two Cowork sessions can run at once, which argues for The Shared Rules rather than the Code harness. Code does not edit either document.

**The growth governor applies.** A rule enters only as another leaves, only with a test. The test proposed for this one: at the open of any change set, the session names either the peer sessions it checked or the fact that there were none.

## 5. What was verified this turn, and how

- Zero em or en dashes remain in `rank-math-feed.php`: `grep` over the file on disk, exit code 1.
- Theme committed and level with origin: `git status -sb` prints `## main...origin/main` with no ahead or behind marker.
- The deploy is real: `deploy.py --verify` prints CURRENT, with the server identical to local, the zip matching the theme at 487 files, and local and server both reporting 0.134.0.
- The record repository excludes the theme: `git check-ignore -v` names `.gitignore` line 95, and `git ls-files` tracks nothing under that folder.
- The two false record commit messages: `git show --stat` on each, showing Cowork's harness and an exemplar in one, and a DSRD file, a README and a handover in the other. No theme file in either.
- The third false commit message, in the theme repository: `git show --stat c470113` shows two files where the message names one, and `git log -S` on both changed sentences names `c470113` as the commit that de-dashed lines 3 and 8.
- `git show 2545fb3 -- rank-math-feed.php` returns nothing for those two comment lines, while `git log -S"lengthPermalink"` names `2545fb3` alone. Together those two reads are what separate the true half of the peer's account from the false half.

## 6. The version was not bumped, and that was a technical call

The job as written asked for a theme version bump. It was not done, by the peer session first and agreed by this one. A version bump exists so a browser drops a cached stylesheet. This change is PHP comment text that no browser ever fetches, so a bump would move the number without meaning anything. The theme stays at 0.134.0, where tonight's Rank Math declined-tests change put it.

Named here rather than left silent, because The Shared Rules section 8 says a technical choice is taken and named, not carried to Kain.

---

## 7. A second hole the collision opened, in H5, and it is live right now

**H5, the push check, cannot tell one session's unfinished work from another's.** It refuses a close while the theme carries any uncommitted tracked change, and it reads the whole repository rather than the closing session's declared files.

With one session that is correct and it is why the rule exists. With two it is a deadlock. This session finished its work, committed it, deployed it and proved it, and then could not close: the peer session was still writing `tools/score_run.py`, a file this session never touched and, under the ruling above, must not touch. It blocked the close three times. The peer has said plainly that it will keep working after this session ends, so the block does not clear by waiting either.

**The two ways out are both wrong, which is what makes it a defect rather than an inconvenience.** Committing the peer's file means writing a commit message for a diff this session did not make, on the same night, in a file whose whole subject is that exact fault. Waiting means never closing. The session closed with the block standing and this paragraph as the record, which is the least bad of the three and still not right.

**The shape of the fix, for whoever takes it:** H5 already knows the closing session's declared file list, because Rule 2 requires it and H2 enforces it. The check should be scoped to those paths, and any other dirty tracked file reported as somebody else's in-flight work rather than treated as this session's failure to commit. **Testable:** two sessions open at once, one closes cleanly while the other holds an uncommitted file it declared.

**Not built here, and deliberately.** Editing the enforcement layer to unblock the session doing the editing is the worst possible time to touch it, and Rule 8 puts the harness outside Code's reach in any case. It is written down instead, which is the whole point of the road.

---

**OWED BACK:** three things, in order of cost.

1. Chat writes the ruling in section 1 into the document that owns it, and says which document that is: The Shared Rules if it binds Cowork too, the Code harness if it does not.
2. Chat rules whether the commit-message gate in section 4 is built, and by whom. The peer session has offered to take it and has the case fresh.
3. Chat rules on the H5 defect in section 7. **Testable:** two sessions open at once, one closes cleanly while the other holds an uncommitted file it declared.

*No em or en dashes in this file; checked before writing.*
