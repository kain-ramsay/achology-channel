#!/bin/bash
# channel_watch.sh: keep the channel repository and its origin in step, and
# leave proof that the road is alive.
#
# Run by the launchd agent com.achology.channelwatch, which fires on any change
# inside the channel folders and again every two minutes as a backstop. One run
# does four things, in this order and for these reasons:
#
#   1. Commit anything written locally, so Code's and Chat's writes both travel.
#   2. Pull with rebase, so the other side's writes arrive before we push.
#   3. Push.
#   4. Write HEARTBEAT.txt and a status file, whether or not anything changed.
#
# THE HEARTBEAT IS THE POINT, and it is why step 4 runs even on a quiet cycle.
# The fault this repository exists to fix is that a stalled channel looks exactly
# like a quiet one: an empty folder reads as "nothing was written" whether that
# is true or the transport died. A timestamp rewritten every cycle makes silence
# measurable, so Code's session-open hook can say the road is down instead of
# reporting an empty channel as though it were news.
#
# HOW OFTEN THE HEARTBEAT IS COMMITTED, which is a real tension and was got wrong
# first time. Written to disk every cycle, because Chat reads the working tree on
# this machine directly and wants it fresh. Committed only when something else is
# travelling anyway, or when the last commit is more than ten minutes old, because
# a commit per cycle would be seven hundred a day and "what changed today" would
# stop being answerable from the log. Ten minutes sits inside the fifteen the
# session-open hook calls stale, so the far side still sees a beat before the
# alarm.
#
# THE BUG THIS SHAPE FIXED, kept because the lesson is general: the first version
# wrote the heartbeat every cycle and committed it never, and git refuses to
# rebase with unstaged changes, so the pull failed on the very first quiet cycle
# and the status file said the channel could not be trusted. The watcher was
# correct to shout. The fault was that its own housekeeping was making the mess
# it then reported. Hence --autostash below as well: no housekeeping file of ours
# is ever allowed to block the leg that brings the other side's work in.
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
stale_lock_taken=0

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

write_status() {
  # $1 = OK or FAIL, $2 = the sentence. Written whole each time rather than
  # appended, so the hook reads a state rather than a log it must interpret.
  printf '%s  %s\n%s\n' "$1" "$(stamp)" "$2" > "$STATUS"
}

if [ ! -d "$CHANNEL/.git" ]; then
  write_status FAIL "No git repository at $CHANNEL. The channel is not set up on this machine."
  exit 1
fi

cd "$CHANNEL" || { write_status FAIL "Cannot enter $CHANNEL."; exit 1; }

# Written first, so that even a failing cycle proves the watcher itself ran. A
# missing heartbeat and a stale one mean different things: never started, against
# running and unable to reach GitHub.
stamp > HEARTBEAT.txt

changed=$(git status --porcelain | grep -cv 'HEARTBEAT.txt$' || true)

# Age of the last commit, so a quiet channel still beats on the far side.
last_commit=$(git log -1 --format=%ct 2>/dev/null || echo 0)
age=$(( $(date +%s) - last_commit ))

if [ "$changed" -gt 0 ]; then
  # The message names the count and the folders touched, so the log answers
  # "what moved and when" without anyone opening a diff.
  folders=$(git status --porcelain | sed 's/^...//; s/"//g' | cut -d/ -f1 \
            | sort -u | tr '\n' ',' | sed 's/,$//')
  git add -A
  if ! git commit -q -m "channel: $changed change(s) in $folders"; then
    write_status FAIL "Changes were staged but the commit failed. Nothing is lost; the next cycle retries."
    exit 1
  fi
elif [ "$age" -gt 600 ]; then
  git add HEARTBEAT.txt
  git commit -q -m "heartbeat" 2>/dev/null
fi

# Pull before push, always, even on a quiet cycle: this is the leg that brings
# the other side's writes in. Rebase, so the history stays a single line and a
# merge commit never appears in a channel nobody is branching. Autostash because
# an uncommitted heartbeat must never be the reason the other side's work cannot
# land; see the note at the head of this file.
if ! git pull -q --rebase --autostash origin main; then
  write_status FAIL "Pull failed. The local channel may be behind origin, so a quiet channel cannot be trusted until this clears."
  exit 1
fi

if ! git push -q origin main; then
  write_status FAIL "Push failed. Local commits exist that the other side cannot see."
  exit 1
fi

note=""
if [ "$stale_lock_taken" -gt 0 ]; then
  note=" A lock left by a dead run was taken over after $((stale_lock_taken / 60)) minutes; cycles before this one did nothing."
fi

if [ "$changed" -gt 0 ]; then
  write_status OK "Pushed $changed change(s). Channel and origin agree.$note"
else
  write_status OK "Nothing to send. Channel and origin agree.$note"
fi
