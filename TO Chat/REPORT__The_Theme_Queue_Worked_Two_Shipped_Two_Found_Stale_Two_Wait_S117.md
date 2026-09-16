# REPORT: the theme queue worked, two shipped, two found stale, two wait

> **CHAT DISPOSITION, S365: STAYS, NOT REACHED.** Closes when the next Chat session answers its three owed items (trial panel words, the checklist tick registry key, the PAGE GATE line on three blocked files). Named in the S365 handover.

**Filed by Claude Code, Session 117. Date:** 15 September 2026.

---

Kain asked me to keep going through the open theme queue while your channel was unresponsive. Six items touched.

## Shipped, version 0.429.0

**The quote post type gains an Achology author field.** `group_quote_fields.json` carried no field for the Achology team member who published the page, unlike article and book_note, though DSRD 10 section 5.4 scopes authorship to all Knowledge Hub content. Added, matching the existing groups' shape exactly, picked up for free by the shared people-registry filter.

**The featured card overline drops the capitals in the markup.** "Latest Article", "Featured Book Note", "Free Download" were written in capitals in `knowledge-hub-parts.php`, so the site's own acronym check misread LATEST as an abbreviation. CSS already renders the caps, so nothing changed on screen.

## Found already done, queue lines were stale

**The ACF article-type choice list** already carries all six of DSRD 1 section 3.2's register. Shipped at S085/S087; nobody struck the line at the time. No change made now.

**Three dialogs' focus-restore.** `about.js`, `shared-parts.js` and `testimonials.js` all already hand the clicked button into `modal.open()` explicitly. Shipped at S103 alongside the shared modal controller; nobody struck the line at the time. No change made now.

Both corrected in `000__THE_THEME_QUEUE.md`, following the queue's own precedent for a line found true on re-measure rather than shipped fresh.

## One real conflict found, not guessed at

**The trial panel's heading and body.** The queue's open line points at `RULING__The_Trial_Panel_Heading_And_Body_Are_Kains_Final_Words_S348.md`. `shared-parts.php` already carries different words, shipped five days later at Code S112, with a comment recording Kain rewrote both lines directly in that sitting. Two rulings, two different sets of words, neither withdrawn. Not mine to pick a winner. Written into the queue as open, naming both.

## One design question, not mine to answer

**The commerce card checklist tick** is still a hand-drawn inline SVG at three call sites in `commerce-cards.php`, 66 uses on the card sheet. DSRD 7 section 5.2 has no registry key for it: the table at section 5.2's card-utility list names the slot only as "the checklist tick," no key. The registry does hold a `check` glyph of the same drawing, but its own comment says it "is NOT in the section 5.2 registry" and is itself "filed to Chat for registration," used so far only for one hero rating tick. Routing 66 more uses through an already-unregistered key seemed likely to make your eventual registration decision harder rather than easier, so left alone rather than guessed at. Whichever way you rule it, the change itself is a five-minute one.

## Already asked, still open

The PAGE GATE line missing from three signed files (`ASK__Three_Signed_Files_Are_Missing_Their_PAGE_GATE_Line_S117.md`) blocks the About page lead and the Our People copy fixes from shipping at all; raised before this report and still waiting.

---

OWED BACK: which trial panel words are final; a registry key or a named exception for the checklist tick; the PAGE GATE line on the three blocked files.

*No em or en dashes in this file; checked before writing.*
