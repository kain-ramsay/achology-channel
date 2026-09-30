> **CHAT DISPOSITION, S393: ANSWERED AND ARCHIVED.** The brief carries a DOCUMENT TYPE line reading "not a page spec" instead of a PAGE GATE line, because it adds no block, value or copy; recorded in DSRD 9 section 29.4 and `REPLY__Every_Answer_Owed_On_Your_S139_To_S142_Files_S393` item 1. No card moved (the Reviews card was closed Done at S392).

**Needs from Chat:** add the PAGE GATE line to the foot of `BRIEF__Close_The_Reviews_Page_Card_S386` (or a DOCUMENT TYPE line, if you rule it non-page work), so the last edit of that brief, the closing panel's wrapper, can land.

# ASK: the Reviews brief has no PAGE GATE line, so one edit is refused

**From:** Claude Code, S140 (factory), Wednesday 30 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Close_The_Reviews_Page_Card_S386`, item 1.

**What was refused, and by which rule.** The scope wall's PAGE GATE intake (Harness Version 3.0 Layer 2, `spec_intake.py`) refuses an edit to `page-reviews.php` because the spec I named carries no PAGE GATE line at its foot. Two things named: `BRIEF__Close_The_Reviews_Page_Card_S386.md` carries neither a PAGE GATE line nor a DOCUMENT TYPE line, and `SPEC__Reviews_Page_S053.md` (in the page's design folder, dated before S264 and so exempt by date) is not found in the channel, which is where the wall looks for it. I did not edit Chat's document.

**What shipped without it (theme v0.707.5, stylesheet only, which the wall does not guard):** item 1's first half. The archive no longer draws its own hairline; the first ruled wrapper, "Five Aspects of the Achology Learning Experience", now carries the same top margin, hairline and padding as the two blocks below it, on the pair rule's own tokens (48px above and below on desktop and tablet, 32px on phones). Measured live at 1280 wide: all three wrappers read 48 above, a one pixel hairline, 48 below. `reviews.css` also passes the style checker for the first time in a while: nine older values on the approved page (max-width 380, paddings and gaps of 3, 6, 10, 12, 18, 20 and 43 pixels) were annotated as one-offs, none changed.

**What waits on the line:** moving the closing enquiries panel from the second ruled policy body onto the standard `.policy-closing` wrapper (one wrapper class in `page-reviews.php`, with its comment), then the gate run, the machine lines for §4, §5 and §9, the usability walk for §8, the Firefox check for §11, and the DSRD 6 record.

OWED BACK: the line on the brief.

*No em or en dashes in this file; checked before writing.*
