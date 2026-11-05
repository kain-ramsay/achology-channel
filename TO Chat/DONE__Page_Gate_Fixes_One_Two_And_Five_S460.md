**For Chat. What this needs from you:** one look, not a ruling: the gate no longer fails four Help, front page and Enquiries lines that were instrument faults; the Enquiries page and the instructors page still fail on other lines, named below. Code, factory session, S460, 5 November 2026. Completes RULING__Four_Gate_Instrument_Fixes_From_The_S180_Sittings_S446 (with DONE__Page_Gate_Fixes_Three_And_Four_S460).

# DONE: all five page gate instrument fixes are in, and the three pages re-run

Gate version: page_gate.py at commit efa88e6b on main, pushed (the gate carries no version number of its own).

**Fix 1, a filled band is its own boundary.** A block painted with a fill that is not the page's own, or a background picture, and as wide as the content, is a boundary like a bordered card: no hairline is asked of it and the space outside it is held to 48 (32 on a phone). Two bands that touch are left alone, because "48 outside" cannot apply to a pair that is flush by design (this was found by the side-by-side run below: without it, the Hub list pages' signed flush pair would have gained a failure on tablet).

**Fix 2, a wall is measured to its last card.** Where a wall is the last thing above a line, the space is measured from its last card or tile, not from its box.

**Fix 5, a card's own padding is not a boundary.** The padding inside a card that draws its own edge (a border all round, or a fill narrower than the content, at least 64 tall) is never read as a second owner of the boundary. A full-width band keeps every reading it had, and margins are still measured.

**The fifth instrument line from RULING S180 (Halo band), and fix 3 widened: the whole check now runs on the settled page.** Touch 3 holds the Help answer's last part 24 low until it is scrolled to. The gate now sets reduced motion for the whole run, so spacing and the accessibility scan both read the page as it settles. Proved on the Help answer: unsettled 24 above, reduced motion 48, after scrolling to the foot 48 (32 on a phone).

**Tests** (scratchpad test_spacing_fixes.py, written and seen failing first): 13 cases pass, each fix with a control that must not change (no fill and no border; a small filled pill; two touching bands; a block that is not a wall; plain padded words; a full-width filled band).

**The three re-runs, before and after the changes, same flags:**
- Help answer (first-course-complete-beginner): the band line is a carve-out with 48 outside, desktop, tablet and phone. The foot reads 48/48 (32/32 on a phone). Both of its hairline failures are gone.
- Knowledge Hub front page: the wall now reads 48 above its line (32 on a phone); the three hairline failures are gone, all three widths.
- Enquiries: the boundary owner failure on the members card's 24 padding is gone. Its other lines still fail, as before, for reasons these fixes do not touch: its dark top band and main block overlap by design (no hairline, gap minus 96, minus 64 on a phone), the off-scale 144 and 96 padding, header to content, the page record, and the chain register.

**Seventeen pages run through the old and new measuring code side by side** (the three above plus about, courses, help, topics, quotes, articles, workbooks, tags, policies, help category, ladder of inference, code of ethics, instructors, Hub subject lists): no page gained a failure. Changes seen, all the right way or equivalent: Hub list pages' recorded "parted by space" carve-outs now read as the band edge with 48 passing; the about page's phantom 32-above line is gone (it was the same rise, measured unsettled); the help category page's band line is a carve-out. **One reading to know about:** on the instructors page the 32 padding on the second people group (a filled card narrower than the content) is now a carve-out as a card's own padding; its 48 margin failure stays. If you read that group as a band, say so and I narrow the rule. One site-state difference, not from this change: the topics articles list read one image with wrong dimensions in the old run and none in the new.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
