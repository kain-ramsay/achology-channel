#!/bin/bash
# channel_watch_commit.sh: the manual side of the channel's write path.
#
# FIXED S295. Chat reported the push race coming back within two hours of a
# manual clear, twice in one day, and named the cause precisely: "a manual
# git operation racing the watcher's own pull-rebase-push cycle" (diagnosed
# first at S069, repeated at S074, and repeated again at S295 because each
# fix before this one cleared the RESULT rather than the RACE). Every prior
# fix ran `git commit`/`git push` by hand in ~/achology-channel from a Code
# session. Those commands know nothing about com.achology.channelwatch,
# which fires on the same repository every two minutes and on every file
# change. Two processes committing, pulling and pushing the same repository
# with no coordination between them will collide the moment both are awake,
# and clearing the collision does nothing to stop the next one.
#
# THE FIX IS A LOCK, not another clear. This script and channel_watch.sh
# contend for the exact same lock directory, $HOME/.claude/
# achology_channel_watch.lock.d. Whichever gets there first runs; the other
# waits its turn. That is Chat's own first option in
# ASK__The_Push_Race_Came_Back_Within_Hours_S295.md, chosen over the other
# two named there (retry-with-backoff would still let both sides touch the
# working tree at once and only paper over the failure it causes; removing
# manual operations entirely is not available, because Code's own archiving
# of consumed channel files at session close is exactly such an operation
# and has no other route).
#
# FROM NOW ON, EVERY MANUAL WRITE TO ~/achology-channel GOES THROUGH THIS
# SCRIPT, NEVER RAW git ADD/COMMIT/PUSH. That is the actual fix: the lock
# only closes the race if both sides use it. Called as:
#   bash ~/.claude/achology_channel_watch_commit.sh "commit message"
#
# THE RUNNING COPY LIVES IN ~/.claude, NOT THE THEME, for the same reason
# channel_watch.sh does: the theme sits inside iCloud Drive, and an evicted
# file becomes a placeholder stub. This file propagates the same way that
# one already does, via machine-two/channel_watch_commit.sh in the channel
# repository itself, read and self-copied by channel_watch.sh's existing
# self-update step, widened in the same edit that adds this file's row.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
LOCKDIR="$HOME/.claude/achology_channel_watch.lock.d"
MSG="${1:-channel: manual write}"

if [ ! -d "$CHANNEL/.git" ]; then
  echo "channel_watch_commit: no git repository at $CHANNEL." >&2
  exit 1
fi

cd "$CHANNEL" || { echo "channel_watch_commit: cannot enter $CHANNEL." >&2; exit 1; }

# WAIT FOR THE LOCK, rather than skip like the watcher does on a busy cycle.
# A manual write is session-driven and generally wants to finish rather than
# be silently deferred to whenever the next automatic cycle happens to run.
# Same ten-minute abandoned-lock rule as the watcher, so a lock left by a
# killed run does not wedge this side either.
waited=0
while [ -d "$LOCKDIR" ]; do
  lock_age=$(( $(date +%s) - $(stat -f %m "$LOCKDIR" 2>/dev/null || echo 0) ))
  if [ "$lock_age" -gt 600 ]; then
    rmdir "$LOCKDIR" 2>/dev/null
    break
  fi
  if [ "$waited" -ge 60 ]; then
    echo "channel_watch_commit: the watcher has held the lock for 60s; giving up rather than waiting indefinitely. Nothing was touched; retry." >&2
    exit 1
  fi
  sleep 1
  waited=$((waited + 1))
done

if ! mkdir "$LOCKDIR" 2>/dev/null; then
  echo "channel_watch_commit: lost the race for the lock at the last moment; retry." >&2
  exit 1
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT INT TERM

# SAME RECOVERY AS THE WATCHER, for the same reason: a rebase or merge left
# half done by an earlier failure must not poison this run either.
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
  git rebase --abort 2>/dev/null
fi
if [ -f .git/MERGE_HEAD ]; then
  git merge --abort 2>/dev/null
fi

git add -A
if git diff --cached --quiet; then
  echo "channel_watch_commit: nothing staged; nothing to commit."
else
  if ! git commit -q -m "$MSG"; then
    echo "channel_watch_commit: commit failed. Nothing pushed." >&2
    exit 1
  fi
fi

if ! git pull -q --rebase --autostash origin main; then
  git rebase --abort 2>/dev/null
  echo "channel_watch_commit: pull failed and was rolled back cleanly. Local commit stands; retry the push later." >&2
  exit 1
fi

if ! git push -q origin main 2>/dev/null; then
  if git pull -q --rebase --autostash origin main 2>/dev/null && git push -q origin main 2>/dev/null; then
    : # the far side had moved between our pull and our push; settled now
  else
    git rebase --abort 2>/dev/null
    echo "channel_watch_commit: push failed twice. Local commits exist that the other side cannot see." >&2
    exit 1
  fi
fi

echo "channel_watch_commit: pushed clean."
