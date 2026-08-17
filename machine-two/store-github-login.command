#!/bin/bash
#
# GIVE COMMAND LINE GIT ITS GITHUB LOGIN, ON THE CHAT MACHINE.
#
# Kain: double click this file in Finder, exactly like install-watcher.command.
# It asks you for one thing, pastes it into the Mac's own keychain, and proves
# it worked by talking to GitHub before it lets you close the window.
#
# WHY IT IS NEEDED. The watcher installed cleanly at S280 and then stopped at
# "Username for 'https://github.com':". GitHub Desktop is logged in, but it keeps
# its login inside itself, so the git that the watcher runs cannot see it. This
# stores a login where that git looks: the macOS keychain, under github.com.
#
# WHAT IT DOES NOT DO. It asks for no Mac password, installs nothing, changes no
# setting outside git's own, and touches nothing outside your home folder. The
# token you paste is never printed, never written to a file, and never sent
# anywhere but GitHub.
#
# It is safe to run twice. It replaces what it finds rather than stacking.
# Built by Claude Code at S063, answering Chat's note of 18 August 2026.

set -uo pipefail

CHANNEL="$HOME/achology-channel"
USERNAME="kain-ramsay"

echo ""
echo "Giving command line git its GitHub login on this machine."
echo ""

# 1. The clone has to exist, same first check the watcher installer makes. A
#    login stored for a repository that is not here proves nothing.
if [ ! -d "$CHANNEL/.git" ]; then
  echo "STOPPED. There is no channel repository at:"
  echo "    $CHANNEL"
  echo ""
  echo "Clone kain-ramsay/achology-channel to exactly that path in GitHub"
  echo "Desktop first, then run this again."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi

# 2. Point git at the Mac keychain by name rather than assuming it is already
#    pointed there. On some Macs it is set and on some it is not, and a stored
#    credential that nothing reads looks exactly like a credential that did not
#    store.
git config --global credential.helper osxkeychain
echo "  git will now keep logins in the Mac keychain."
echo ""

# 3. The token. Read with -s so it never appears on screen and never lands in
#    the scrollback, which is the one place a pasted secret usually leaks.
echo "Now paste the token you copied from GitHub, then press return."
echo "Nothing will appear as you paste. That is deliberate."
echo ""
read -s -r -p "Token: " TOKEN
echo ""
echo ""

if [ -z "${TOKEN:-}" ]; then
  echo "Nothing was pasted, so nothing was stored. Run this again."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi

# 4. Store it, for both spellings of the host. git asks for github.com; some
#    tools ask for www.github.com, and one missing entry is a prompt nobody is
#    sitting in front of to answer.
for HOST in github.com www.github.com; do
  printf 'protocol=https\nhost=%s\nusername=%s\npassword=%s\n\n' \
    "$HOST" "$USERNAME" "$TOKEN" | git credential-osxkeychain store
done
echo "  the login is in the keychain."
echo ""

# 5. PROVE IT. The whole reason the watcher failed quietly for a night is that
#    nobody made it try in front of a person. This asks GitHub a real question
#    over the real address, with the credential it just stored, and reports the
#    answer plainly.
echo "Asking GitHub whether it accepts it ..."
echo ""
OUT=$(cd "$CHANNEL" && GIT_TERMINAL_PROMPT=0 git ls-remote \
        "https://github.com/$USERNAME/achology-channel.git" 2>&1)
RC=$?
unset TOKEN

if [ $RC -eq 0 ]; then
  echo "IT WORKS. GitHub accepted the login."
  echo ""
  echo "Nothing else to do and nothing to remember. The watcher will pick this"
  echo "up on its own within two minutes, and from then on anything Chat writes"
  echo "into the channel travels by itself."
else
  echo "GitHub did not accept it. What it said:"
  echo ""
  echo "    ${OUT:-no message}"
  echo ""
  echo "The usual cause is the token being copied short, or missing Contents"
  echo "permission on the achology-channel repository. Make a new one and run"
  echo "this again. Nothing is broken by trying twice."
fi

echo ""
read -n 1 -s -r -p "Press any key to close."
echo ""
