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

This paragraph was wrong when first written, was corrected by the peer session, and was then corrected again by checking it: the peer believed its two lines had gone in under the v0.134.0 commit `2545fb3`. They had not. `git log -S` on the two changed sentences names `c470113`, and `2545fb3` does not touch the file. Recorded in full because the correction chain is itself the evidence for section 4.

**Three, and the worst of them.** Two commits in the project record, `e1c1094` and `e74858b`, carry messages describing theme work and contain none of it. The theme folder is excluded from the record repository on purpose, at `.gitignore` line 95, so one file never has two owners. What those two commits actually hold is whatever else was staged at the time, which was Chat's own documents, swept in by a blanket `git add -A` and given a message about something else. That is a false line in a permanent record, not a mislabelled one.

The third fault was found in two steps, and the order matters because it is the argument for section 4. This session checked the record log, found no dash commit there, and told the peer that the record repository could not hold the theme at all. The peer then went and checked its own commits, found what they actually carried, and corrected them: `a7d44e4` in the record log names both commits and what each really carries, and `CORRECTION__Two_S096_Record_Commits_Describe_Theme_Work_They_Do_Not_Carry_S096.md` sits in this folder. Pushed history was not rewritten. Neither session found this alone.

## 4. What the ruling does not cover, and is worth Chat's judgement

**The commit message fault is a separate hole and this ruling does not close it.** Its cause is writing a commit message from what was done rather than from what was staged, in a repository that deliberately excludes the thing being worked on. Nothing in the harness checks that a commit message describes its own diff, and nothing would have caught it. A gate that reads the staged file list before the message is written would catch it every time, and it would be a machine test rather than a habit.

**Where this ruling belongs is Chat's call, not Code's.** It binds Code today, and it plainly binds Cowork the moment two Cowork sessions can run at once, which argues for The Shared Rules rather than the Code harness. Code does not edit either document.

**The growth governor applies.** A rule enters only as another leaves, only with a test. The test proposed for this one: at the open of any change set, the session names either the peer sessions it checked or the fact that there were none.

## 5. What was verified this turn, and how

- Zero em or en dashes remain in `rank-math-feed.php`: `grep` over the file on disk, exit code 1.
- Theme committed and level with origin: `git status -sb` prints `## main...origin/main` with no ahead or behind marker.
- The deploy is real: `deploy.py --verify` prints CURRENT, with the server identical to local, the zip matching the theme at 487 files, and local and server both reporting 0.134.0.
- The record repository excludes the theme: `git check-ignore -v` names `.gitignore` line 95, and `git ls-files` tracks nothing under that folder.
- The two false commit messages: `git show --stat` on each, showing Cowork's harness and an exemplar in one, and a DSRD file, a README and a handover in the other. No theme file in either.

## 6. The version was not bumped, and that was a technical call

The job as written asked for a theme version bump. It was not done, by the peer session first and agreed by this one. A version bump exists so a browser drops a cached stylesheet. This change is PHP comment text that no browser ever fetches, so a bump would move the number without meaning anything. The theme stays at 0.134.0, where tonight's Rank Math declined-tests change put it.

Named here rather than left silent, because The Shared Rules section 8 says a technical choice is taken and named, not carried to Kain.

---

**OWED BACK:** Chat writes this ruling into the document that owns it, and says which document that is: The Shared Rules if it binds Cowork too, the Code harness if it does not. Chat also rules whether the commit-message gate in section 4 is built, and by whom.

*No em or en dashes in this file; checked before writing.*
