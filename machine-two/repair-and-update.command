#!/bin/bash
#
# REPAIR THE CHANNEL ON THIS MACHINE, AND BRING THE WATCHER UP TO DATE.
#
# Kain: double click this file in Finder. It fixes the stuck channel, installs
# the corrected watcher, and proves both before it lets you close the window.
#
# It asks for no password, installs nothing, downloads nothing from anywhere but
# your own GitHub repository, and touches nothing outside your home folder.
#
# WHAT IT IS REPAIRING. The watcher on this machine used to write and commit one
# shared HEARTBEAT.txt every two minutes, and so did the machine Claude Code runs
# on. Two machines rewriting one line in one file guarantees a collision, and when
# the collision happened the old watcher stopped half way through and left the
# repository stuck, so every later cycle failed on the wreckage of the first.
#
# WHAT IT WILL NOT DO, so you can run it without reading it. It never discards
# anything you or Chat wrote. The only file it is ever willing to resolve by
# itself is the heartbeat timestamp, which is a throwaway line rewritten every two
# minutes. If it meets a disagreement about any real file, it stops, names the
# file, and changes nothing.
#
# Safe to run twice. Built by Claude Code at S063.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
DEST="$HOME/.claude"
SCRIPT="$DEST/achology_channel_watch.sh"
PLIST="$HOME/Library/LaunchAgents/com.achology.channelwatch.plist"
HERE="$(cd "$(dirname "$0")" && pwd)"

say() { echo "  $*"; }

echo ""
echo "Repairing the Achology channel on this machine."
echo ""

if [ ! -d "$CHANNEL/.git" ]; then
  echo "STOPPED. There is no channel repository at:"
  echo "    $CHANNEL"
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi

cd "$CHANNEL" || exit 1

# ── 1. Unstick anything left half done ───────────────────────────────────────
# The old watcher could leave a rebase in progress, which blocks every later pull
# with a message about unmerged files. Aborting is always safe here: the watcher
# writes nothing of its own worth keeping, and every real file is safe in the
# commits on either side.
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
  git rebase --abort 2>/dev/null
  say "a stuck rebase was found and undone."
elif [ -f .git/MERGE_HEAD ]; then
  git merge --abort 2>/dev/null
  say "a half-finished merge was found and undone."
else
  say "nothing was stuck."
fi

# ── 2. Stop this machine fighting over the heartbeat ─────────────────────────
# The shared file is no longer tracked. Each machine now writes its own file in
# the heartbeat folder, so two machines never touch the same path and there is
# nothing left to collide over.
git rm --cached -q HEARTBEAT.txt 2>/dev/null && say "the shared heartbeat file is no longer tracked here."
mkdir -p heartbeat

# Anything uncommitted goes into a commit of its own first, so the pull below
# cannot be blocked by a half-saved file and nothing is ever carried silently.
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -q -m "channel: local state before the S063 repair" 2>/dev/null \
    && say "your uncommitted local changes were committed first, so nothing can be lost."
fi

# ── 3. Bring the two sides together ──────────────────────────────────────────
# Rebase, so the history stays one line. The loop resolves ONLY the heartbeat
# file and stops on anything else, which is the promise at the head of this file.
say "fetching from GitHub ..."
if ! git fetch -q origin 2>/dev/null; then
  echo ""
  echo "COULD NOT REACH GITHUB. The login is probably still missing."
  echo "Run store-github-login.command in this same folder first, then run this again."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi

git rebase -q origin/main 2>/dev/null
guard=0
while { [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; } && [ "$guard" -lt 40 ]; do
  guard=$((guard + 1))
  # Every path git is unhappy about on this step.
  conflicts=$(git diff --name-only --diff-filter=U)
  # Anything that is not the heartbeat is a real disagreement and is not mine.
  real=$(printf '%s\n' "$conflicts" | grep -v '^HEARTBEAT.txt$' | grep -v '^heartbeat/' | grep -v '^$')
  if [ -n "$real" ]; then
    git rebase --abort 2>/dev/null
    echo ""
    echo "STOPPED, and nothing was changed."
    echo ""
    echo "Two sides disagree about a real file, which is not something this"
    echo "script should decide. Send these names to Claude Code:"
    echo ""
    printf '    %s\n' $real
    echo ""
    read -n 1 -s -r -p "Press any key to close."
    exit 1
  fi
  # Heartbeat only. Take whatever the other side says; it is a timestamp.
  for f in $conflicts; do
    git rm -q --cached "$f" 2>/dev/null || true
    rm -f "$f" 2>/dev/null || true
  done
  git add -A 2>/dev/null
  GIT_EDITOR=true git rebase --continue >/dev/null 2>&1 || GIT_EDITOR=true git rebase --skip >/dev/null 2>&1 || break
done

if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
  git rebase --abort 2>/dev/null
  echo ""
  echo "STOPPED, and nothing was changed. The repair could not finish by itself."
  echo "Tell Claude Code, and send him this line."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi
say "the two sides are back on one line."

if ! git push -q origin main 2>/dev/null; then
  echo ""
  echo "The repair worked locally but GitHub refused the push."
  echo "Run store-github-login.command in this same folder, then run this again."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi
say "pushed. GitHub and this machine agree."

# ── 4. Install the corrected watcher ─────────────────────────────────────────
mkdir -p "$DEST"
cp "$HERE/channel_watch.sh" "$SCRIPT" && chmod +x "$SCRIPT"
say "the corrected watcher is installed."
launchctl unload "$PLIST" 2>/dev/null
launchctl load "$PLIST" 2>/dev/null
say "restarted."

# ── 5. Prove it ──────────────────────────────────────────────────────────────
echo ""
echo "Running one cycle now, so any problem shows up while you are here ..."
bash "$SCRIPT" >/dev/null 2>&1
sleep 2

STATUS="$DEST/achology_channel_watch.status"
echo ""
if [ -f "$STATUS" ]; then
  cat "$STATUS"
  echo ""
  if head -1 "$STATUS" | grep -q '^OK'; then
    echo "REPAIRED. The channel is live on this machine."
    echo "From here the watcher keeps itself up to date, so this is the last time"
    echo "you have to run anything by hand."
  else
    echo "It ran but could not finish. The line above says why."
  fi
else
  echo "It has not written a status file yet. Give it a minute, then tell Claude Code."
fi

echo ""
read -n 1 -s -r -p "Press any key to close."
echo ""
