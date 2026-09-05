# SHIP: the workbench key opens nothing outside the build ground

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.29, deployed with its three proofs.
**Closes:** the theme queue's workbench key line, the Codex audit's third item.
**Board card:** the Codex theme audit.

---

## What the audit named, and what was actually there

It named one door: the /cards/ workbench.

There were six, in four files, each carrying its own copy of the same two lines. The /cards/ page. Reading an unpublished post. Putting an unpublished post back into the main query so it is not a 404 before permissions are ever consulted. The course page's design chooser. And the two further-reading blocks, which list drafts alongside published pages.

Adding the new condition to five of six would have left the sixth open and looking closed, and nothing in the theme would have said so. So the key now has one owner, `achology_workbench_request()`, and every door calls it. Switching it off anywhere switches it off everywhere by construction.

## The test is the site's own address, not a constant

The queue line proposed an environment constant naming the build ground. **That would not have worked, and it is worth saying why rather than quietly doing something else.**

Cutover is a clone. A clone copies wp-config.php. A constant saying "this is the build ground" would be copied to achology.com with everything else, and the guard would announce itself as working while protecting nothing.

That is not a hypothetical. This same page's first guard trusted `REMOTE_ADDR`, was deployed and tested, and let the whole world through, because behind SiteGround's proxy `REMOTE_ADDR` is not what a naive reading expects. The note is in the theme, a few lines above the change.

So the test is `home_url()`, the site's own stored address. A clone's new address closes the door the moment the address changes, with nobody remembering anything. It is read from the database, not from the request, so a forged Host header cannot claim to be the build ground. `ACHOLOGY_BUILD_GROUND` remains available for a future staging host, and it can only ever turn the key on somewhere, never off.

## What is proved, and what is not

**Proved, measured after the deploy:** on the build ground nothing changed. /cards/ with the key 200, without it 404, with a wrong key 404. A draft article with the key 200, without it 404. Home and a book note 200.

**Not proved:** the off case. There is only one host today, so the guard cannot yet be seen refusing a real request, and this project's own rule is never to trust a guard that has not been. I have not called it done; I have put it on the queue as a cutover check: `cutover_gate.py --golive` should request the workbench address on the live site and fail on anything but a 404. That is the moment the fact becomes testable, and it is the moment it matters.

---

OWED BACK: nothing. Say if you would rather the cutover check were a line on the cutover list than on the theme queue.

*No em or en dashes in this file; checked before writing.*
