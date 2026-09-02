> **CHAT DISPOSITION, S329:** read. Written onto the Hosting & Go-Live card's page body (the break, what was ruled out, the two routes, the cost). Kain's next Code sitting installs a modern rsync, or Pooka & Co are asked what changed; named in the S329 handover. Board cards moved: Hosting & Go-Live (page body). Archived.

# FINDING: the deploy proof cannot run, it broke overnight, and it is not anything on this side

**From:** Claude Code, Session 093. **Date:** 2 September 2026.
**This is a waiver, not a question.** Harness Rule 12's deploy check refuses every close, and I cannot satisfy it tonight without either Kain's password or weakening the proof. It is recorded rather than worked around.
**Board card:** Hosting and Go-Live, since the server is Pooka and Co's ground.

---

## Nothing is waiting to deploy, and that is the first thing to know

**The last real deploy landed** at about 00:11, sent `acf-json/group_article_fields.json`, and returned **all three proofs green**. The change was then confirmed live by reading the choice list back off the install, not by trusting the printout. PROOF 3 still agrees, local and server both 0.132.1, and the site returns 200 on the homepage, /about/ and /reviews/, checked this turn.

## What is broken

**PROOF 1 only**, the server-against-local comparison. Every run, in both real and dry-run mode:

    rsync: [Receiver] change_dir#1 ".../themes/achology/" failed: Permission denied (13)

## The timeline is the useful part

**It worked at 00:11 and was broken by 09:31.** Nothing on this machine changed the server in between except one `wp acf json sync`, which writes to the database and not to the filesystem. **So this is a server-side change made overnight**, which on SiteGround usually means maintenance.

## What was ruled out, each measured rather than assumed

- **Not a permission fault on the folder.** It is `drwxr-xr-x`, owned by the SSH user. SSH can `cd` into it and count its 71 entries.
- **Not a dead key or a missing path.** SSH works throughout, including WP-CLI.
- **Not the pull direction.** rsync itself can list that same folder, its parent, and the home folder. Only the push fails.
- **Not my S093 exclude change.** It fails identically with `--delete-excluded` removed, and it was in use on the successful 00:11 deploy.
- **Not the tilde in the remote path.** Fails the same with the path written out in full.
- **Not the old-arguments hardening.** `--rsync-path="rsync --old-args"` changes nothing.

## The remaining suspect, and why I stopped

**The two ends are twenty years apart:** this Mac ships Apple's rsync **2.6.9** from 2006, protocol 29, and the server now runs **3.5.0**, protocol 32. Versions 3.4 and above added hardening that is known to break old clients, and the overnight timing fits an upgrade.

**There is no other rsync on this Mac**, checked in the three usual places. Installing one needs Kain's password, and he had just parked the sitting.

**I did not make the proof pass by asking it less**, and that is deliberate. A check that reports green because it stopped looking is the exact failure this session already met once tonight, on the security fix, where PROOF 1 printed "identical" while every file was still being served.

## What it waits on

**One of two, and the first is cleaner.** A modern rsync installed on this Mac with `deploy.py` pointed at it. Or Pooka and Co saying what changed on the server overnight, since it is their ground by the scope document.

**Until then Rule 12's check refuses every session close**, and the theme cannot be proved current by machine even when it is. That is the cost, stated rather than hidden.

OWED BACK: nothing from Chat. Naming it so it reaches the board and is not rediscovered from cold.

*No em or en dashes in this file; checked before writing.*
