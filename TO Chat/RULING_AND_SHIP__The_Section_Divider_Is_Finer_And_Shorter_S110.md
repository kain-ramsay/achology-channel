> CHAT DISPOSITION, S357: answered. The two values written into DSRD 9 section 22.2 (S085 ruling 6). Nothing else owed. Archived.

# RULING AND SHIP: the section heading divider is a quarter finer and stops 30 per cent short of the container edge

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.268.0,
deployed and read back on all four page types that draw it.**
**Ruled by Kain** live in this sitting. His words:

> "could we reduce the decorative lines thickness by 25%. Also, shorten its total
> length by 30% so it fits at least that much less than the current right-hand
> container limit."

**Owning document: DSRD 9 section 22.2**, which holds his S085 ruling 6. **This
component has no design folder and no build sheet**, so under the S257 transition
note its DSRD section is the standard and only Chat can write to it. **That is
what is asked back.**
**Board card:** none of its own; it is site-wide.

---

## Where this came from, because it is not a tidy-up

Kain asked for the divider himself at S085, in his own words, for more vibrancy
and to make sections easier to follow, and corrected me then that it belongs on
the heading's line rather than beneath it. **It reached this sitting as feedback
from outside**, suggesting the decoration be removed altogether and the structure
left to type and spacing.

**He asked what I thought and I said keep it**, for two reasons worth keeping in
the record. The headings are already at their own size and weight with the
standard space around them, so the divider is not propping up a weak hierarchy
and removing it would not reveal a better one. And it is on every article, book
note and help answer, so removing it is a change to the whole site rather than to
the page in front of him. He then ruled this instead: finer and shorter, not
gone.

## What changed, and it is two lines in one file

**A quarter finer: the line is 0.75 rather than 1.** It was already a single
pixel, so this is stated plainly rather than fudged: on a retina screen, which is
what he reads it on, the browser has real device pixels to spend and draws a
genuinely finer line; on an older screen at one device pixel per pixel it rounds
back to roughly what it was. **The honest alternative was refused:** dropping the
opacity a quarter would look thinner on every screen and would not be thinner,
and he asked for thickness.

**Thirty per cent shorter, by a spacer inside the rule rather than a width on
it.** The rule takes whatever width the heading's words leave, so its length is
different on every heading on the site and any fixed width would be a guess. A
spacer taking 30 per cent of the rule's own width is 30 per cent of whatever that
particular heading left.

**Measured at a plain 30 per cent it came out between 33 and 42**, because the
spacer inherits the rule's own 18px gap and 18 is a different share of a 663 wide
rule than of a 147 wide one. That met the letter of "at least 30" and left the
number different on every heading, so the gap is subtracted from the basis and it
is now exactly 30 everywhere.

**One consequence solved rather than discovered later.** The rule hides itself on
a heading with too little room left, at 97. Only 70 per cent of that room is
drawn in now, so the threshold is 97 divided by 0.7, which is 138. At the old 97 a
heading leaving 100 would have kept a cramped rule instead of hiding it.

## Read back on every page type that draws it

The quote page, an article, a book note and a help answer, at 1440: the line
measures 0.75 on all of them, and the shortfall is 30 per cent on every heading
on every one of the four. One book note heading hides its rule, which is the
threshold doing its job on a short measure.

---

OWED BACK: DSRD 9 section 22.2 updated with the two values, since this component
has no build sheet of its own and the section is its standard.

*No em or en dashes in this file; checked before writing.*
