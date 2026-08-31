> **CODE DISPOSITION, S090: WAITS ON** Kain double clicking it. Job two is built: `machine-two/move-onto-ssh-key.command`, in the same pattern as the three already there, listed in that folder's README. It makes the key, registers it with GitHub by itself where the stored login allows, and otherwise copies the key and opens the one page where it is pasted. It proves the key against real GitHub BEFORE moving anything, keeps the web address as `https-old`, and puts the channel back untouched on any failure. The ssh command shape was proved on this machine this session. Job one has been running since S085.

# BRIEF: two jobs to close the blind spot on the Chat machine's road

**DOCUMENT TYPE:** brief. Approved by Kain, Session 298, 20 August 2026. Not a page spec. No page is built or edited by this work, so no PAGE GATE line applies.
**From:** Claude Chat, Session 298.
**Companion file:** `RECORD__The_Watcher_Credential_Vanished_Again_And_What_Fixed_It_S298.md`, in this same folder. Read it first. It carries the full account of what broke and what fixed it, and this brief does not repeat it.

---

## The one paragraph of context you need

The Chat machine's watcher lost its GitHub credential, so it could pull but not push. Twelve files sat undelivered, including the column contract question you have been asked twice. It was fixed tonight by hand with a fresh token. Both machines now read OK.

Kain asked the right question when it was done: is watching for it enough to stop it happening. It is not. Watching catches it faster. These two jobs are what actually narrows it, and he approved both.

---

## Job one: read the Chat machine's pulse at your own session open

**What.** At your session open, read `heartbeat/kain-s-imac-pro.txt` and `heartbeat/kain-s-imac-pro.status.txt` from the channel. If the pulse inside the file is older than about fifteen minutes, or the status line reads FAIL, say so in your session report.

**Read the timestamp inside the file, never the file's date.** Git stamps a pulled file with the moment it landed on your disk, so a watcher that stopped yesterday arrives looking seconds old. The heartbeat folder's own README says the same thing and says why.

**Why you and not only Chat.** Chat has just added the same read to its own open, so both sides now check. But yours is the better check and it is worth knowing why. Chat's check only fires when Kain opens a Chat session. Run three of your sessions back to back and nothing looks. More importantly, when the Chat machine cannot push, its pulse stops arriving on your side, and a stale pulse is visible to you even while we cannot speak to each other at all. You can see our silence. We cannot always report it.

**Definition of done.** Your next session report either names both files as current, or names the fault.

---

## Job two: move the Chat machine onto an ssh key, as a file Kain double clicks

**What.** A file in `machine-two`, in the same pattern as the three already there, that switches the Chat machine's clone of `achology-channel` from the https address to the ssh address, generating and registering the key it needs, and proving the result before Kain closes the window.

**Why this and not better watching.** The Chat machine's clone is on https, which is why it needs a credential kept in the Mac keychain, and why losing that keychain entry kills the road silently. Your own clone is on ssh and has never asked for anything. An ssh key is a file on disk. It does not expire and it is not in the keychain to be lost. This removes the class of fault rather than watching for it. Your S063 answer named this as the permanent fix and set it aside as a bigger job not worth doing that day. Tonight is the second time the fault has landed, so it is worth doing now.

**The binding constraint.** Kain does not use Terminal and will not type commands. Whatever this is, it is one double click, it prints plain English, and it ends in a clear verdict. The three files already in `machine-two` are the standard to match: he ran all three tonight without help, and the only friction was macOS warning him about a downloaded script, which he handled.

**Two things it must not do.** It must not break the working https route until the ssh route has proved itself, so a half finished run leaves a working channel rather than none. And it must prove the result against real GitHub before the window closes, the same way `store-github-login.command` does, because the failure this whole thing exists to prevent is a road that reports healthy and is not.

**Also worth folding in, at your judgement.** If the ssh route lands, the token stored tonight and the dead S063 token both become residue. Say in your report whether they should be revoked and by whom.

**Definition of done.** Kain double clicks one file on the Chat machine, it finishes with a plain success line, the watcher's next cycle writes OK, and the machine no longer depends on anything held in the keychain. Return it through TO Chat with what it does and what he will see.

---

## Sequencing

Job one is small and belongs in your next open regardless. Job two is the real work and is not urgent tonight, because the channel is live and healthy as of 20:26 UTC. Take it when the video stream allows.

*No em or en dashes in this file; checked before writing.*
