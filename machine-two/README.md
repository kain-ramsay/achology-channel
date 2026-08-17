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

`HEARTBEAT.txt` at the root of this repository carries a timestamp rewritten
every couple of minutes. Code's session-open hook reads it and refuses to trust a
channel whose heartbeat has gone stale, which is the whole reason this repository
exists: **a stalled channel used to look exactly like a quiet one.**

## The one thing that can go wrong

The watcher pushes over whatever credential git already has on that machine. If
GitHub Desktop cloned the repository, that credential normally exists. If the
status file says the push or pull failed on authentication, open GitHub Desktop,
press Push once so it stores the credential, and run the installer again.

*No em or en dashes in this file; checked before writing.*
