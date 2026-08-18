#!/bin/bash
# channel_watch.sh: keep the channel repository and its origin in step, and
# leave proof that the road is alive.
#
# Run by the launchd agent com.achology.channelwatch, which fires on any change
# inside the channel folders and again every two minutes as a backstop.
#
# ─────────────────────────────────────────────────────────────────────────────
# VERSION 2, S063. WHAT WAS WRONG WITH VERSION 1, because it is the whole reason
# this file changed and the diagnosis was Chat's.
#
# Version 1 wrote and committed HEARTBEAT.txt on BOTH machines. One file, one
# line, rewritten every couple of minutes on two machines at once. That does not
# merely risk a conflict, it guarantees one the moment both machines are awake:
# two divergent commits touching the same single line, every cycle, forever.
#
# AND THE SECOND HALF, which is what turned a nuisance into a dead road. On a
# failed rebase version 1 wrote FAIL and exited, leaving the rebase IN PROGRESS.
# Git then refuses every later pull with "cannot pull with rebase: you have
# unmerged files", so every subsequent cycle failed on the wreckage of the first
# one rather than on anything real. Both machines were found in exactly that
# state, and on Code's machine it had to be unwound by hand.
#
# A watcher that can wedge itself and cannot unwedge itself is not a watcher, it
# is a tripwire with no reset. So version 2 changes three things:
#
#   1. NO TWO MACHINES EVER WRITE THE SAME TRACKED FILE. Each writes
#      heartbeat/<machine>.txt, its own path, so a conflict is not merely
#      unlikely, it is impossible. HEARTBEAT.txt stays as a LOCAL file, written
#      every cycle and no longer tracked, because the session-open hook reads its
#      timestamp off this machine's disk and never needed it to travel.
#
#   2. IT RECOVERS AT THE TOP OF EVERY CYCLE. A rebase or merge left in progress
#      by a previous run is aborted before anything else is attempted, and the
#      abort is reported in the status file rather than swallowed.
#
#   3. IT UPDATES ITSELF. The running copy lives in ~/.claude, outside the repo.
#      Version 1 could only be replaced by Kain double clicking the installer
#      again on each machine, which means a fix to this file was not a fix until
#      somebody remembered. Each cycle now compares the running copy against the
#      one in the repository and replaces itself when they differ.
# ─────────────────────────────────────────────────────────────────────────────
#
# One run does five things, in this order and for these reasons:
#
#   0. Recover from any rebase or merge a previous run left half done.
#   1. Commit anything written locally, so Code's and Chat's writes both travel.
#   2. Pull with rebase, so the other side's writes arrive before we push.
#   3. Push.
#   4. Write the heartbeats and a status file, whether or not anything changed.
#
# THE HEARTBEAT IS THE POINT, and it is why step 4 runs even on a quiet cycle.
# The fault this repository exists to fix is that a stalled channel looks exactly
# like a quiet one: an empty folder reads as "nothing was written" whether that
# is true or the transport died. A timestamp rewritten every cycle makes silence
# measurable, so Code's session-open hook can say the road is down instead of
# reporting an empty channel as though it were news.
#
# HOW OFTEN THE HEARTBEAT IS COMMITTED, which is a real tension and was got wrong
# first time. Written to disk every cycle, because both sides read the working
# tree directly and want it fresh. Committed only when something else is
# travelling anyway, or when the last commit is more than ten minutes old,
# because a commit per cycle would be seven hundred a day and "what changed
# today" would stop being answerable from the log. Ten minutes sits inside the
# fifteen the session-open hook calls stale, so the far side still sees a beat
# before the alarm.
#
# NO OUTSIDE CODE. The design approved at S277 named fswatch for the trigger.
# This machine has no Homebrew, so fswatch would have meant installing a package
# manager in order to install a watcher, and macOS already ships the capability
# in launchd's WatchPaths. Under Harness Rule 11 the smaller outside surface is
# the better one on a site that takes card payments, and the smallest is none.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
STATUS="$HOME/.claude/achology_channel_watch.status"
LOCKDIR="$HOME/.claude/achology_channel_watch.lock.d"
RUNNING="$HOME/.claude/achology_channel_watch.sh"
stale_lock_taken=0
recovered=""
self_updated=0

mkdir -p "$(dirname "$STATUS")"

# One run at a time. A change arriving during a slow push would otherwise start a
# second run inside the first, and two gits in one working tree is how an index
# lock gets left behind and the watcher dies quietly until somebody notices.
# mkdir is used rather than flock because stock macOS has no flock, and mkdir is
# atomic on every filesystem this will ever sit on.
# A LOCK LEFT BEHIND BY A KILLED RUN WOULD OTHERWISE STOP THIS WATCHER FOREVER,
# silently and with exit code 0, which is the worst failure this project keeps
# meeting: the thing reports healthy and does nothing. Found at S061 by testing
# the alarm rather than trusting it. So a lock older than ten minutes is treated
# as abandoned and taken over, and the takeover is recorded in the status file so
# it is visible rather than merely survived. No legitimate cycle runs that long.
if [ -d "$LOCKDIR" ]; then
  lock_age=$(( $(date +%s) - $(stat -f %m "$LOCKDIR" 2>/dev/null || echo 0) ))
  if [ "$lock_age" -gt 600 ]; then
    rmdir "$LOCKDIR" 2>/dev/null
    stale_lock_taken=$lock_age
  fi
fi
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  exit 0
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT INT TERM

stamp() { date -u "+%Y-%m-%dT%H:%M:%SZ"; }

# THE MACHINE'S OWN NAME, worked out before anything can fail, because the status
# written on a failure is the one most worth having and it is filed under this
# name. Sanitised to letters, digits and hyphens: it becomes a path in a git
# repository, and a computer called "Kain's iMac" would otherwise produce a
# filename carrying an apostrophe and a space.
MACHINE=$(scutil --get ComputerName 2>/dev/null || hostname)
MACHINE=$(printf '%s' "$MACHINE" | tr '[:upper:]' '[:lower:]' \
          | sed 's/[^a-z0-9]\{1,\}/-/g; s/^-//; s/-$//')
[ -z "$MACHINE" ] && MACHINE="unknown-machine"

write_status() {
  # $1 = OK or FAIL, $2 = the sentence. Written whole each time rather than
  # appended, so the hook reads a state rather than a log it must interpret.
  printf '%s  %s\n%s\n' "$1" "$(stamp)" "$2" > "$STATUS"

  # AND THE SAME LINE INSIDE THE CHANNEL, added S063, where BOTH sides can read
  # it. This is the fix for a real limit Chat reported rather than guessed at:
  # "~/.claude/achology_channel_watch.status sits outside the two folders my
  # filesystem connector is allowed to reach. I have never been able to read it
  # and cannot start now."
  #
  # So the health of each machine lived on that machine only, and the sole way to
  # learn whether the far end was alive was to ask Kain to read a file out loud.
  # That makes him the monitoring system for the road built to stop him being the
  # courier, which is the same fault wearing a different hat.
  #
  # The channel is the one surface both of us can read. Writing the status into it
  # means Chat can answer "is Code's machine alive" with its own eyes, and my
  # session open can answer the same about Chat's, with nobody relaying anything.
  #
  # It is deliberately NOT committed on its own. Like the heartbeat it travels
  # when something else travels, or on the ten minute beat, so the log does not
  # fill with seven hundred status commits a day.
  if [ -n "${MACHINE:-}" ] && [ -d "$CHANNEL/heartbeat" ]; then
    printf '%s  %s\n%s\n' "$1" "$(stamp)" "$2" > "$CHANNEL/heartbeat/$MACHINE.status.txt"
  fi
}

if [ ! -d "$CHANNEL/.git" ]; then
  write_status FAIL "No git repository at $CHANNEL. The channel is not set up on this machine."
  exit 1
fi

cd "$CHANNEL" || { write_status FAIL "Cannot enter $CHANNEL."; exit 1; }

# ── 0. RECOVER ───────────────────────────────────────────────────────────────
# Anything a previous run left half done is undone here, before it can poison
# this one. Aborting is always the right move: nothing in this repository is ever
# edited by the watcher, so there is no work of its own to lose, and the files
# themselves are safe in the commits on either side of the failed replay.
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
  git rebase --abort 2>/dev/null
  recovered="A rebase left in progress by an earlier run was aborted."
fi
if [ -f .git/MERGE_HEAD ]; then
  git merge --abort 2>/dev/null
  recovered="${recovered} A half-finished merge was aborted."
fi

# AND THE THIRD SHAPE, found on Code's machine minutes after the first two were
# fixed, which is why it is here: an unmerged index entry with NO rebase and NO
# merge in progress. An interrupted stash pop can leave one behind. It blocks
# every pull with the same "unresolved conflict" message while both --abort
# commands above report nothing to do, so the recovery sails straight past it and
# the road stays shut with the watcher saying only that the pull failed.
#
# Only the heartbeat paths are cleared, and deliberately so: those are timestamps
# and there is never anything in them worth a decision. An unmerged entry on any
# real file is left exactly where it is and named in the status, because
# resolving somebody's actual writing is not a watcher's business.
unmerged=$(git diff --name-only --diff-filter=U 2>/dev/null)
if [ -n "$unmerged" ]; then
  real_unmerged=$(printf '%s\n' "$unmerged" | grep -v '^HEARTBEAT.txt$' | grep -v '^heartbeat/' | grep -v '^$')
  if [ -n "$real_unmerged" ]; then
    write_status FAIL "A conflict is sitting unresolved on a real file, so nothing was touched. Tell Claude Code: $(printf '%s' "$real_unmerged" | tr '\n' ' ')"
    exit 1
  fi
  git rm -q --cached HEARTBEAT.txt 2>/dev/null
  git add heartbeat/ 2>/dev/null
  recovered="${recovered} A stuck heartbeat entry left in the index was cleared."
fi

# ── 1. THE HEARTBEATS ────────────────────────────────────────────────────────
# Written first, so that even a failing cycle proves the watcher itself ran. A
# missing heartbeat and a stale one mean different things: never started, against
# running and unable to reach GitHub.
#
# TWO FILES, AND THE DIFFERENCE BETWEEN THEM IS THE FIX AT THE HEAD OF THIS FILE.
#
#   HEARTBEAT.txt          local only, no longer tracked. Read by Code's
#                          session-open hook off this machine's own disk.
#   heartbeat/<machine>.txt tracked, and unique to this machine, so the far side
#                          can see this machine beating and no two machines ever
#                          write the same path.
#
# The machine's name was worked out at the head of this file, before anything
# could fail, so that a failure status is filed under it too.
mkdir -p heartbeat
stamp > HEARTBEAT.txt
stamp > "heartbeat/$MACHINE.txt"

# ── 2. COMMIT WHAT IS OURS ───────────────────────────────────────────────────
# The heartbeat files are excluded from the "did anything real happen" count, so
# a quiet cycle stays quiet. HEARTBEAT.txt is ignored by .gitignore now and so
# never appears here at all; the grep stays for the days after this lands, while
# an older clone may still have it tracked.
changed=$(git status --porcelain | grep -v 'HEARTBEAT.txt$' | grep -cv '^.. heartbeat/' || true)

last_commit=$(git log -1 --format=%ct 2>/dev/null || echo 0)
age=$(( $(date +%s) - last_commit ))

if [ "$changed" -gt 0 ]; then
  # The message names the count and the folders touched, so the log answers
  # "what moved and when" without anyone opening a diff.
  folders=$(git status --porcelain | sed 's/^...//; s/"//g' | cut -d/ -f1 \
            | sort -u | tr '\n' ',' | sed 's/,$//')
  git add -A
  if ! git commit -q -m "channel: $changed change(s) in $folders"; then
    write_status FAIL "Changes were staged but the commit failed. Nothing is lost; the next cycle retries.$recovered"
    exit 1
  fi
elif [ "$age" -gt 600 ]; then
  git add "heartbeat/$MACHINE.txt"
  git commit -q -m "heartbeat: $MACHINE" 2>/dev/null
fi

# ── 3. PULL ──────────────────────────────────────────────────────────────────
# Pull before push, always, even on a quiet cycle: this is the leg that brings
# the other side's writes in. Rebase, so the history stays a single line and a
# merge commit never appears in a channel nobody is branching. Autostash because
# no housekeeping file of ours is ever allowed to block the leg that brings the
# other side's work in.
#
# THE ABORT ON FAILURE IS THE POINT OF VERSION 2. Without it the failure is
# permanent: the half-done rebase blocks every later cycle, so one bad minute
# takes the road down until a person unwinds it by hand.
if ! git pull -q --rebase --autostash origin main; then
  git rebase --abort 2>/dev/null
  write_status FAIL "Pull failed and was rolled back cleanly, so the next cycle starts from a good state. The local channel may be behind origin until it clears.$recovered"
  exit 1
fi

# ── 4. PUSH ──────────────────────────────────────────────────────────────────
# One retry, because the commonest push failure is the other machine having
# pushed in the seconds since our pull, which a second pull fixes. A second
# failure is real and is reported.
if ! git push -q origin main 2>/dev/null; then
  if git pull -q --rebase --autostash origin main 2>/dev/null && git push -q origin main 2>/dev/null; then
    : # the far side had moved between our pull and our push; settled now
  else
    git rebase --abort 2>/dev/null
    write_status FAIL "Push failed twice. Local commits exist that the other side cannot see.$recovered"
    exit 1
  fi
fi

# ── 5. UPDATE OURSELVES ──────────────────────────────────────────────────────
# The copy that runs lives outside the repository on purpose, so that a pull
# cannot rewrite a script while it is executing. The cost of that was a script
# nobody could fix remotely: version 1 could only be replaced by Kain double
# clicking the installer again on each machine. So the running copy is compared
# against the repository's after every successful pull, and replaced when they
# differ. The new one is used from the NEXT cycle, never mid-run.
#
# The risk is named rather than pretended away: a broken script published here
# now propagates to both machines by itself. That is the right trade, because the
# failure this replaces was a fix that never arrived at all.
if [ -f "machine-two/channel_watch.sh" ] && ! cmp -s "machine-two/channel_watch.sh" "$RUNNING"; then
  cp "machine-two/channel_watch.sh" "$RUNNING" && chmod +x "$RUNNING" && self_updated=1
fi

note=""
if [ "$stale_lock_taken" -gt 0 ]; then
  note=" A lock left by a dead run was taken over after $((stale_lock_taken / 60)) minutes; cycles before this one did nothing."
fi
if [ -n "$recovered" ]; then
  note="$note $recovered"
fi
if [ "$self_updated" -eq 1 ]; then
  note="$note The watcher updated itself to a newer version; it takes effect next cycle."
fi

if [ "$changed" -gt 0 ]; then
  write_status OK "Pushed $changed change(s). Channel and origin agree.$note"
else
  write_status OK "Nothing to send. Channel and origin agree.$note"
fi
