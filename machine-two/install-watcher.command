#!/bin/bash
#
# THE CHANNEL WATCHER, INSTALLED ON THE CHAT MACHINE.
#
# Kain: double click this file in Finder. That is the whole job. It prints what
# it is doing and ends with either INSTALLED or a plain sentence saying what is
# wrong. Nothing here asks for a password and nothing touches anything outside
# your own home folder.
#
# WHAT IT DOES, so nobody has to take it on trust:
#   1. checks the channel repository is actually cloned on this machine
#   2. copies the watcher script into ~/.claude, outside any sync folder
#   3. writes a launch agent that runs it on every change and every two minutes
#   4. starts it, waits, and reads back the status file it writes
#
# WHY IT EXISTS. Code's machine has had this since the channel was built, so a
# file written there reaches GitHub within seconds. This machine has had nothing,
# which meant every delivery from Chat's side needed Kain to press push in GitHub
# Desktop by hand, and every read risked being stale unless he pulled first. Chat
# named that on day one as the road's weakest link, and it was right: a manual
# step at every sitting is the kind of step that gets skipped on the day it
# matters. Built by Claude Code at S062 on Kain's instruction.
#
# It is safe to run twice. It replaces what it finds rather than stacking.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
DEST="$HOME/.claude"
SCRIPT="$DEST/achology_channel_watch.sh"
PLIST="$HOME/Library/LaunchAgents/com.achology.channelwatch.plist"
LABEL="com.achology.channelwatch"
HERE="$(cd "$(dirname "$0")" && pwd)"

echo ""
echo "Installing the Achology channel watcher on this machine."
echo ""

# 1. The clone has to exist first. Without it there is nothing to watch, and a
#    watcher pointed at a missing folder is worse than none: it reports healthy.
if [ ! -d "$CHANNEL/.git" ]; then
  echo "STOPPED. There is no channel repository at:"
  echo "    $CHANNEL"
  echo ""
  echo "Clone kain-ramsay/achology-channel to exactly that path in GitHub"
  echo "Desktop first, then run this again. The path must match, because the"
  echo "watcher and Claude both look there by name."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi
echo "  the channel repository is here:            $CHANNEL"

# 2. The script lives in ~/.claude rather than in the repo, for the same reason
#    it does on Code's machine: what runs must not sit anywhere that can be
#    evicted, replaced by a placeholder, or rewritten by a pull while running.
mkdir -p "$DEST"
cp "$HERE/channel_watch.sh" "$SCRIPT"
chmod +x "$SCRIPT"
echo "  the watcher script is installed at:        $SCRIPT"

# 3. The launch agent. Two triggers, deliberately: WatchPaths fires within a
#    second or two of any change in the live folders, and the interval fires
#    anyway so the heartbeat stays fresh on a silent day. A watcher that only
#    reacts cannot prove it is alive.
mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>$LABEL</string>
	<key>ProgramArguments</key>
	<array>
		<string>/bin/bash</string>
		<string>$SCRIPT</string>
	</array>
	<key>WatchPaths</key>
	<array>
		<string>$CHANNEL/FROM Chat (Chat writes → Code reads)</string>
		<string>$CHANNEL/TO Chat (Code writes → Chat reads)</string>
		<string>$CHANNEL</string>
	</array>
	<key>StartInterval</key>
	<integer>120</integer>
	<key>RunAtLoad</key>
	<true/>
	<key>StandardOutPath</key>
	<string>$DEST/achology_channel_watch.log</string>
	<key>StandardErrorPath</key>
	<string>$DEST/achology_channel_watch.log</string>
</dict>
</plist>
PLISTEOF
echo "  the launch agent is written at:            $PLIST"

# 4. Start it. Unload first so running this twice replaces rather than stacks.
launchctl unload "$PLIST" 2>/dev/null
launchctl load "$PLIST" 2>/dev/null
echo "  started."
echo ""
echo "Waiting for its first cycle to report ..."
sleep 12

STATUS="$DEST/achology_channel_watch.status"
if [ -f "$STATUS" ]; then
  echo ""
  cat "$STATUS"
  echo ""
  if head -1 "$STATUS" | grep -q '^OK'; then
    echo "INSTALLED. Nothing else to do, and nothing to remember."
    echo "From now on anything Chat writes into the channel travels on its own."
  else
    echo "It ran but could not finish. The line above says why."
    echo ""
    echo "If it mentions authentication: open GitHub Desktop, press Push once so"
    echo "it stores the credential, then run this file again."
  fi
else
  echo "It has not written a status file yet. Give it a minute and look at:"
  echo "    $STATUS"
  echo "If that file never appears, tell Claude Code and send this log:"
  echo "    $DEST/achology_channel_watch.log"
fi

echo ""
read -n 1 -s -r -p "Press any key to close."
echo ""
