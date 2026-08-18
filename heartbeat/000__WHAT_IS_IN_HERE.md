# heartbeat: one file per machine, and never a shared one

## What this folder is

Each machine on the channel writes its own timestamp here, every couple of
minutes, into a file named after itself. Nothing else ever writes to another
machine's file.

That is the whole design, and it exists because the obvious alternative failed.

## Why it is one file per machine

Until 18 August 2026 both machines wrote and committed a single `HEARTBEAT.txt`
at the repository root. One file, one line, rewritten every two minutes on two
machines at once.

**That does not risk a conflict, it guarantees one** the moment both machines are
awake: two divergent commits touching the same single line, every cycle. Chat
spotted it, Kain reported it from the GitHub Desktop side ("3 ahead, 2 behind,
and the only conflicting file is HEARTBEAT.txt"), and both machines were found
wedged mid-rebase because of it.

Two machines writing two paths cannot conflict. There is nothing to merge.

## What still lives at the root

`HEARTBEAT.txt` is still written at the root of this repository every cycle, and
is now **untracked**, listed in `.gitignore`. Code's session-open hook reads its
timestamp off its own machine's disk to answer "did my watcher run", which never
needed the file to travel to the other machine.

So: the root file answers "is my own watcher alive", and the files in here answer
"is the other machine alive". Two different questions that one file was being
asked to answer at once.

## The two files each machine writes

- `<machine>.txt` is the pulse: one UTC timestamp, rewritten every cycle.
- `<machine>.status.txt` is the health: `OK` or `FAIL` and one plain sentence.

**The health file exists because Chat could not read its own.** Its filesystem
connector reaches these two channel folders and nothing else, so
`~/.claude/achology_channel_watch.status` has always been invisible to it. That
made Kain the monitoring system for the road that was built to stop him being the
courier, which is the same fault wearing a different hat. Both watchers now write
their health into the channel, where each side can read the other with its own
eyes and nobody has to relay anything.

## Reading the age, and the one trap in it

**Read the timestamp INSIDE the file. Never the file's date.**

Git stamps a pulled file with the moment it landed on your disk, so a heartbeat
that stopped yesterday arrives looking seconds old. Trusting the file date would
produce a monitor that reports healthy exactly when it is wrong, which is the
failure this whole repository exists to prevent. Code's session-open hook reads
the contents for this reason, and its alarm was tested against a stopped machine
rather than assumed.

## Reading it

The newest timestamp in here is the last time that machine reached GitHub. A file
more than about fifteen minutes old means that machine's watcher has stopped or
cannot push, which is the thing this repository exists to make visible: **a
stalled channel used to look exactly like a quiet one.**

*No em or en dashes in this file; checked before writing.*
