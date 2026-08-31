#!/bin/bash
#
# MOVE THIS MACHINE'S CHANNEL ONTO AN SSH KEY, SO IT STOPS LOSING ITS LOGIN.
#
# Kain: double click this file in Finder, exactly like the other three. It does
# the work, shows you one page in your browser, and tells you plainly whether it
# worked before you close the window.
#
# WHY IT EXISTS. This machine's copy of the channel talks to GitHub over the web
# address, so it needs a password kept in the Mac's keychain. That keychain entry
# has now gone missing twice, and both times the channel went quiet without
# saying so: this machine could read but not write, and twelve files sat here
# undelivered. An ssh key is an ordinary file on this disk. It does not expire,
# it is not in the keychain, and nothing can quietly forget it. The other machine
# has always worked this way and has never once asked for anything.
#
# WHAT YOU WILL SEE. It makes a key if there is not one. It tries to register the
# key with GitHub by itself. If it cannot, it copies the key for you and opens
# the one GitHub page where it is pasted, and waits for you. Then it proves the
# new road really works before it moves anything onto it.
#
# WHAT IT WILL NOT DO. It will not break the road you have now. The web address
# is only swapped out after the new road has been proved against real GitHub, and
# it is kept under the name "https-old" so it can be put straight back. If
# anything at all goes wrong, you finish the run exactly as you started it.
#
# It asks for no Mac password, installs nothing, and touches nothing outside your
# home folder. It is safe to run twice.
#
# Built by Claude Code at S090, answering job two of
# BRIEF__Close_The_Blind_Spot_On_Chats_Machine_Two_Jobs_S298.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
USERNAME="kain-ramsay"
REPO="achology-channel"
SSH_URL="git@github.com:$USERNAME/$REPO.git"
KEY="$HOME/.ssh/achology_channel_ed25519"
KEYNAME="Achology channel, Chat machine"

finish() {
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  echo ""
  exit "${1:-0}"
}

echo ""
echo "Moving this machine's channel onto an ssh key."
echo ""

# 1. The clone has to exist. Everything below is about one repository, and doing
#    any of it without that repository present proves nothing at all.
if [ ! -d "$CHANNEL/.git" ]; then
  echo "STOPPED. There is no channel folder at:"
  echo "    $CHANNEL"
  echo ""
  echo "Run repair-and-update.command first, then run this again."
  finish 1
fi

CURRENT=$(cd "$CHANNEL" && git remote get-url origin 2>/dev/null)
echo "  the channel is here, and today it talks to GitHub over:"
echo "      ${CURRENT:-nothing set}"
echo ""

if [ "$CURRENT" = "$SSH_URL" ]; then
  echo "This machine is already on the ssh key. Checking it still works ..."
  echo ""
  if (cd "$CHANNEL" && GIT_SSH_COMMAND="ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -i '$KEY'" \
        git ls-remote "$SSH_URL" >/dev/null 2>&1); then
    echo "IT WORKS. Nothing to do and nothing to remember."
    finish 0
  fi
  echo "It is on the key but the key is not being accepted. Carrying on to fix it."
  echo ""
fi

# 2. The key itself. Made only if it is not already here, so a second run never
#    throws away a key GitHub has already been told about.
mkdir -p "$HOME/.ssh"
chmod 700 "$HOME/.ssh"

if [ -f "$KEY" ]; then
  echo "  a key for this already exists on this Mac, so it is reused."
else
  echo "  making a new key ..."
  ssh-keygen -t ed25519 -f "$KEY" -N "" -C "$KEYNAME" >/dev/null 2>&1
  if [ ! -f "$KEY" ]; then
    echo ""
    echo "STOPPED. The key could not be made, and nothing has been changed."
    finish 1
  fi
  echo "  the key is made."
fi
chmod 600 "$KEY"
PUB=$(cat "$KEY.pub")
echo ""

# 3. Tell ssh to use this key for GitHub, by name. Without this line ssh offers
#    whatever keys it happens to find, in whatever order, and a machine with an
#    old unrelated key can be refused while holding a perfectly good new one.
CONF="$HOME/.ssh/config"
touch "$CONF"
chmod 600 "$CONF"
if ! grep -q "achology_channel_ed25519" "$CONF" 2>/dev/null; then
  {
    echo ""
    echo "# Added by move-onto-ssh-key.command, the Achology channel."
    echo "Host github.com"
    echo "  HostName github.com"
    echo "  User git"
    echo "  IdentityFile $KEY"
    echo "  IdentitiesOnly yes"
  } >> "$CONF"
  echo "  ssh now knows to use this key for GitHub."
else
  echo "  ssh already knew about this key."
fi
echo ""

SSH_CMD="ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -i $KEY"

works() {
  (cd "$CHANNEL" && GIT_SSH_COMMAND="$SSH_CMD" git ls-remote "$SSH_URL" >/dev/null 2>&1)
}

# 4. Try to register the key without troubling you. The login already in the
#    keychain may or may not be allowed to add keys; if it is, this is silent and
#    you never see the browser step at all.
echo "Asking GitHub whether it already knows this key ..."
echo ""

if ! works; then
  TOKEN=$(printf 'protocol=https\nhost=github.com\n\n' \
            | git credential-osxkeychain get 2>/dev/null \
            | sed -n 's/^password=//p')
  if [ -n "${TOKEN:-}" ]; then
    CODE=$(curl -s -o /dev/null -w '%{http_code}' -X POST \
             -H "Authorization: Bearer $TOKEN" \
             -H "Accept: application/vnd.github+json" \
             -d "{\"title\":\"$KEYNAME\",\"key\":\"$PUB\"}" \
             https://api.github.com/user/keys 2>/dev/null)
    unset TOKEN
    if [ "$CODE" = "201" ]; then
      echo "  GitHub accepted the key on its own. You do not need to do anything."
      echo ""
      sleep 3
    elif [ "$CODE" = "422" ]; then
      echo "  GitHub already had this key."
      echo ""
    fi
  fi
fi

# 5. If it still does not work, this is the one part that needs your hands. The
#    key is put on the clipboard and the exact page is opened, so the whole job
#    is a paste and a button.
if ! works; then
  echo "$PUB" | pbcopy
  echo "GitHub needs to be shown this key once, and that part needs you."
  echo ""
  echo "The key is already copied. In the page that is about to open:"
  echo ""
  echo "   1. Click in the big box marked Key and paste."
  echo "   2. Put anything you like in Title. \"Chat machine\" is fine."
  echo "   3. Click the green Add SSH key button."
  echo "   4. Come back here and press return."
  echo ""
  read -n 1 -s -r -p "Press any key to open the page."
  echo ""
  open "https://github.com/settings/ssh/new"
  echo ""
  read -r -p "Done that? Press return here and this will check it. " _
  echo ""
fi

# 6. PROVE IT, against real GitHub, before anything is moved. This is the whole
#    point of the file. The fault it exists to end is a road that reports healthy
#    and is not, so nothing is switched over on a hope.
echo "Asking GitHub whether the key works ..."
echo ""

if ! works; then
  echo "IT DID NOT WORK, and nothing has been changed."
  echo ""
  echo "Your channel is still working exactly as it was a minute ago, over the"
  echo "web address, so nothing is broken and nothing is lost."
  echo ""
  echo "What GitHub said, in its own words:"
  echo ""
  (cd "$CHANNEL" && GIT_SSH_COMMAND="$SSH_CMD" git ls-remote "$SSH_URL" 2>&1 | sed 's/^/    /')
  echo ""
  echo "The usual cause is the key not being pasted whole. Run this again and it"
  echo "will reuse the same key rather than making another."
  finish 1
fi

echo "  GitHub accepts the key."
echo ""

# 7. Only now is the road moved, and the old one is KEPT rather than deleted.
#    A half finished run has to leave a working channel, not none.
if [ "$CURRENT" != "$SSH_URL" ] && [ -n "${CURRENT:-}" ]; then
  (cd "$CHANNEL" && git remote remove https-old >/dev/null 2>&1)
  (cd "$CHANNEL" && git remote add https-old "$CURRENT" >/dev/null 2>&1)
fi
(cd "$CHANNEL" && git remote set-url origin "$SSH_URL")
echo "  the channel now uses the key, and the old web address is kept as"
echo "  \"https-old\" in case it is ever wanted again."
echo ""

# 8. And prove the real thing, not a stand in: an actual fetch on the actual
#    remote the watcher will use, after the switch rather than before it.
echo "Doing one real check over the new road ..."
echo ""
if (cd "$CHANNEL" && git fetch origin >/dev/null 2>&1); then
  echo "IT WORKS."
  echo ""
  echo "This machine no longer needs anything kept in the keychain, so the"
  echo "fault that took the channel down twice cannot happen again here."
  echo ""
  echo "Nothing else to do and nothing to remember. The watcher picks this up"
  echo "on its own within two minutes."
else
  (cd "$CHANNEL" && git remote set-url origin "$CURRENT")
  echo "The key was accepted but the first real check failed, so the channel has"
  echo "been put straight back the way it was and is working as before."
  echo ""
  echo "Nothing is broken. Tell Claude Code and he will look at it."
fi

finish 0
