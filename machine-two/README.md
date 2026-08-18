# machine-two: the watcher for the machine Chat runs on

## For Kain, and it is one step

Open this folder in Finder on **the machine you use Claude Chat on**, and double
click **`install-watcher.command`**.

That is the whole job. It prints what it is doing and ends with either
`INSTALLED` or one plain sentence saying what is wrong. It asks for no password,
touches nothing outside your own home folder, and is safe to run twice.

If macOS refuses to open it because it came from the internet, right click it and
choose Open instead, then Open again on the warning. That prompt is macOS being
careful about a downloaded script, and the file is one of ours.

## Why this exists

Code's machine has had a watcher since the channel was built, so anything written
there reaches GitHub within seconds and anything Chat writes arrives without
anyone doing anything.

The machine Chat runs on has had nothing. Until this is installed, every delivery
from Chat's side needs Kain to press Push in GitHub Desktop by hand, and every
read on that side risks being stale unless he pulls first. Chat named that itself
on the day the road opened, and named it correctly: **a manual step at every
sitting is the kind of step that gets skipped on the day it matters.**

Built by Claude Code at S062 on Kain's instruction, after Chat asked for it.

## What the installer actually does

1. **Checks the clone exists** at `~/achology-channel`. If it does not, it stops
   and says so rather than installing a watcher with nothing to watch. A watcher
   pointed at a missing folder is worse than none, because it reports healthy.
2. **Copies the watcher** to `~/.claude/achology_channel_watch.sh`. It runs from
   there rather than from this repository on purpose: what runs must not sit
   anywhere that a pull can rewrite underneath it or a sync layer can replace
   with a placeholder.
3. **Writes a launch agent** with two triggers. It fires within a second or two
   of any change in the two live folders, and again every two minutes whatever
   happens. The second one is not redundant: a watcher that only reacts cannot
   prove it is alive, and the interval is what keeps `HEARTBEAT.txt` fresh on a
   silent day.
4. **Runs one cycle immediately**, so that if the machine cannot push, the
   failure appears while Kain is still sitting there rather than three days later
   when a file quietly does not arrive.

## Afterwards

`~/.claude/achology_channel_watch.status` holds one line saying OK or FAIL and
one sentence of plain English. That file is the answer to "is the road up".

**The heartbeats, and there are now two kinds (changed S063).**

`HEARTBEAT.txt` at the root is written every couple of minutes and is **no longer
tracked by git**. Code's session-open hook reads its timestamp off its own
machine's disk to answer "did my watcher run", which never needed the file to
travel anywhere.

`heartbeat/<machine>.txt` is the tracked one, **one file per machine and never a
shared one**, which is what answers "is the other machine alive". That folder's
own README says why, and the short version is that both machines committing one
shared file every two minutes does not risk a conflict, it guarantees one. Both
machines were found wedged mid-rebase because of it.

Either way the point stands: **a stalled channel used to look exactly like a
quiet one**, and a timestamp makes silence measurable.

**The watcher updates itself now.** Each cycle it compares the copy running in
`~/.claude` against `machine-two/channel_watch.sh` in this repository and replaces
itself when they differ, taking effect the next cycle. Before S063 a fix to the
watcher was not a fix until somebody remembered to double click the installer
again on each machine, which is how version 1's conflict bug survived a fix
landing in the repository.

## The one thing that can go wrong, and it went wrong (S280)

The watcher pushes over whatever credential git already has on that machine, and
**on this machine it had none.** The installer ran clean on 18 August 2026 and the
first cycle stopped at `Username for 'https://github.com':`. GitHub Desktop is
logged in and keeps its login inside itself, so the git the watcher runs cannot
see it. The advice this section used to give, press Push once in GitHub Desktop
and the credential appears, is wrong for that reason and has been replaced.

**The fix is the second file in this folder: double click
`store-github-login.command`.** It asks for one thing, a GitHub token, stores it
in the Mac keychain where command line git looks, and proves it by asking GitHub
before it lets you close the window. It asks for no Mac password, installs
nothing, and is safe to run twice.

Getting the token is five clicks in Safari and one copy. The numbered walk is in
`ANSWER__The_One_Step_That_Gives_Chats_Git_A_GitHub_Login_S063.md`, in the TO Chat
folder, and Chat sits with Kain while he runs it.

*No em or en dashes in this file; checked before writing.*
