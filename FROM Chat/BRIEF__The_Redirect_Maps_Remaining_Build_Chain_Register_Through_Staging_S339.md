> **CODE DISPOSITION, S101: WAITS ON steps 2 through 5, mine, a future session (substantial, standalone work, not started mid-batch tonight).** Step 1 confirmed already built. The three S079 findings asked about in the S339 correction are answered in full in `REPLY__The_Three_S079_Findings_Checked_None_Are_Old_News_S101.md`, filed the same session: none are old news, all three checked live and still real.

**CORRECTED S339, later the same session, before this was acted on.** Step 1 below, the chain register, is wrong. It is already built: `REPORT__The_Chain_Register_Is_Built_And_What_Its_First_Run_Found_S079.md` in the Archive, closing `BRIEF__Redirect_Chain_Register_And_Cutover_Hook_S293`, dispositioned in full at S306. `redirect_chain_register.py` exists beside `page_gate.py`, fills the five columns, and refuses on an incomplete chain. `cutover_gate.py` is the hook. The reason this brief said otherwise: a folder search that should have checked the Archive silently failed to recurse into it and returned no results, read as "nothing exists" rather than "the search did not work." Steps 2 through 5 below are not affected by this and stand as written.

**Also worth your read while you are in that report:** its own three findings (the whole Knowledge Hub missing from the sitemap, the homepage still a placeholder at the time, and /about/instructors/ carrying the wrong schema with no Person entities) were dispositioned to the board rather than actioned directly, and none of the three appears on either the Redirect Strategy card or the Page readiness records card as they stand today. They may be long since resolved. If any of the three is still real, say so; if all three are old news, say that too, so this stops being an open thread nobody is watching.

---

# BRIEF: build the redirect map's remaining implementation, chain register through to the staging check

**From:** Claude Chat, Session 339. **Date:** 4 September 2026.
**Board card:** Redirect Strategy & Delivery.
**Context:** The redirect map itself is finished, 2,596 rows, every one ruled, held in the Redirect Map | Master File folder. This card's own Definition of Done lists the chain register as "briefed S293," but no file by that name, or naming a chain register, survives anywhere in the channel, live or archived. Either it went to you by a route this channel carries no record of, or it never actually landed. Rather than assume either way, this brief covers the whole remaining build fresh, so nothing here sits on an unverifiable claim.

---

## What is already true, so you are not re-deriving it

The map is complete and ruled: 2,596 rows, in the Redirect Map | Master File folder. The one-hop rule governs it: an old address resolves to its final home directly, never through an intermediate address, and never more than two hops even where one is briefly unavoidable, because AI search crawlers abandon at the third hop and a chain Googlebot survives silently kills AI citations.

## What is still needed, in the order it makes sense to build it

**1. The chain register.** Five destination columns added to the Redirect Master workbook, plus the script that fills them from the map and exits non-zero the moment it finds an incomplete chain. This is what proves, mechanically, that no redirect in the map points at another redirect rather than a live final address.

**2. Chapter 5 reset.** Every existing page readiness record gets its chapter 5 (the redirect chapter) reset, per DSRD 6 Version 7, so each page's record reflects the current map rather than an earlier one.

**3. Build the redirects, then verify them.** Each row in the map moves from ruled to built, then from built to verified, as the work actually lands. This card is the place that count is tracked, so please report it back the same way.

**4. The one-hop test.** Any old address that would need three or more hops to reach its home is flattened to a single direct redirect before go-live. This should catch nothing if the chain register in step 1 is working correctly, but it is the belt to that braces.

**5. The redirect checker, run on staging.** Nothing goes live until this returns green.

## What happens at cutover, named here so the shape of the whole job is visible, not because it is yours to do now

The map applies through Rank Math's Redirections module, then the sitemap is resubmitted, and the search visibility flip fires from its own hook rather than a checklist item. That is cutover work, not this brief's ask.

---

OWED BACK: confirmation the chain register work is understood and queued, and, honestly, whether any of the five steps above is already sitting done from an earlier session this channel simply has no record of. If so, say which, and this brief shortens itself accordingly.

*No em or en dashes in this file; checked before writing.*
