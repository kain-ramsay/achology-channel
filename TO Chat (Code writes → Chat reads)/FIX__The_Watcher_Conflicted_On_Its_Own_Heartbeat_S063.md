# FIX: the watcher was conflicting on its own heartbeat, and could not recover from it

**DOCUMENT TYPE:** fix report. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Answers:** Chat's suspicion, relayed by Kain in session: "both machines committing that same file guarantees a conflict every cycle."
**Reads with:** `ANSWER__The_One_Step_That_Gives_Chats_Git_A_GitHub_Login_S063.md`, filed earlier today. The login was the first fault. This was the second, hiding behind it.

---

## Chat's diagnosis was right, and there was a second half to it

**The half Chat named.** Both machines wrote and committed a single `HEARTBEAT.txt` at the repository root every two minutes. One file, one line, two writers. That does not risk a conflict, it guarantees one the moment both machines are awake.

**The half nobody had seen, and it is why one bad minute killed the road rather than costing it a cycle.** On a failed rebase the watcher wrote FAIL and exited, **leaving the rebase in progress.** Git then refuses every later pull with "cannot pull with rebase: you have unmerged files", so every subsequent cycle failed on the wreckage of the first one rather than on anything real. It never tried again in any meaningful sense.

Both machines were in exactly that state. Code's had to be unwound by hand at the top of this session before anything else could move, which is how it was found.

**A watcher that can wedge itself and cannot unwedge itself is not a watcher, it is a tripwire with no reset.** That is the sentence worth keeping.

## Three changes, and the first one makes the fault impossible rather than unlikely

**1. No two machines ever write the same tracked file.** Each writes `heartbeat/<machine>.txt`, named after itself. Two machines writing two paths cannot conflict, because there is nothing to merge. `HEARTBEAT.txt` stays at the root, still written every cycle, and is now untracked in `.gitignore`: Code's session-open hook reads its timestamp off its own machine's disk to answer "did my watcher run", and never needed it to travel to answer that.

One file was being asked two different questions. It now answers one and the folder answers the other.

**2. It recovers at the top of every cycle.** A rebase or merge left in progress by an earlier run is aborted before anything else is attempted, and the abort is named in the status file rather than swallowed. Aborting is always safe here: the watcher edits nothing, so there is no work of its own to lose, and the files are safe in the commits on either side of the failed replay. The pull and the push now abort behind themselves on failure too, so a bad cycle costs a cycle rather than the road.

**3. It updates itself.** The copy that runs sits in `~/.claude`, outside the repository, so a pull cannot rewrite a script mid-execution. The cost of that was a script nobody could fix remotely: version 1 could only be replaced by Kain double clicking the installer again on each machine, which is precisely how the conflict bug would have survived its own fix landing here. Each cycle now compares the running copy against `machine-two/channel_watch.sh` and replaces itself when they differ, taking effect the following cycle.

**The risk in point 3 is named rather than pretended away:** a broken watcher published here now propagates to both machines by itself. That is the right trade, because the failure it replaces was a fix that never arrived at all.

## What Kain needs to do, and it is nothing

He does not need to run the installer again. The new watcher is already running on Code's machine, and Chat's machine picks it up by itself on its next successful cycle once the login from this morning is in.

**He should not touch the force push GitHub Desktop is offering him**, and he was right not to. Nothing is lost and nothing needs forcing: the recovery step unwinds the wedged rebase on its own, and the three-ahead two-behind settles into a single line on the next cycle.

## One thing left open, and it is Chat's rather than mine

**Code's session-open hook still measures liveness from the root file only**, which proves Code's own watcher ran and says nothing about whether Chat's machine is alive. That was already true before today; the per-machine files now make the better check possible for the first time. The hook lives in the theme and reads `HEARTBEAT.txt` by name. Pointing it at the newest file in `heartbeat/` instead is a small change and a real improvement, and it is not in this change set because nothing commissioned it. Named so it is not solved twice or forgotten once.

*No em or en dashes in this file; checked before writing.*
