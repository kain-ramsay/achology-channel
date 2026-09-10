> CHAT DISPOSITION, S357: answered. DSRD 7 section 5.2.1 gains the plus and minus rows; DSRD 8 section 27 ruling 3. Nothing else owed. Archived.

# RULING AND SHIP: the contents card takes Kain's wording, and a round plus and minus

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.282.0,
deployed and measured on both an article and a book note.**
**Ruled by Kain** live in this sitting, on the rendered card. His words:

> "Could you please make the following text changes; YOUR GUIDE TO THIS ARTICLE
> - change to - ARTICLE NAVIGATION PANEL / Table of contents - change to - Table
> of Contents / and please replace the Hide and Show toggle for a round plus and
> minus icon"

**Owning documents:** DSRD 7 section 5.2, the icon registry, which is owed two
rows by this change. DSRD 9's record of the contents card and DSRD 8's component
entry, both already owed from the two earlier rulings this sitting.
**Board card:** none of its own; site-wide.

---

## What is on the page

The label reads ARTICLE NAVIGATION PANEL, drawn in capitals by the stylesheet
from sentence-case words, which is how every label on this site works. The
heading takes his capital C: Table of Contents. In the corner, a round control
holding a minus when the list is open and a plus when it is closed.

## Two rows the registry did not have

The registry held no plus and no minus, so improvising one was not available:
section 5.2 exists to stop exactly that. Both are now in it, as Lucide's own
drawings, the same source as every other row.

**The round part is not in the glyph.** Lucide has circled variants, and taking
one would have put a second drawing of the same idea into a registry whose whole
premise is one canonical drawing per mark. The circle is drawn by the card's own
stylesheet instead, which also means the ring answers to the card's divider
colour rather than to a shape frozen inside an SVG.

OWED BACK: section 5.2 gains a row for `plus` and a row for `minus`.

## The word is still there, it is just not drawn

A control whose only label is a shape has no name to read out. Hide and Show
stay in the markup as hidden text, so the button still announces itself as "Hide
the table of contents" and "Show the table of contents", and the script that was
already writing that word keeps writing it, untouched.

**Both glyphs are rendered and the stylesheet shows one.** The state therefore
lives in `aria-expanded` and nowhere else. The alternative, swapping the glyph in
the script, would have made a second copy of the state for the first one to
drift away from.

## What was measured after it shipped

On both page types: the button is 44 by 44, which is the touch floor, and the
visible circle is 32 sitting flush with the card's content edge. Minus when open,
plus when shut, the list genuinely hidden in the second state, and the accessible
name correct in both. The hover ring takes the readable orange rather than the
bright one, because a 15px stroke inside a circle is a mark and the bright orange
sits under the 3 to one bar for marks on white.

---

OWED BACK: the two registry rows named above. Nothing else.

*No em or en dashes in this file; checked before writing.*
