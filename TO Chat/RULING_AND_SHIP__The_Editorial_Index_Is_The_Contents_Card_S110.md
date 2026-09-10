# RULING AND SHIP: the Editorial index is the Knowledge Hub's contents card

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.270.0,
deployed and read back on the article and the book note at 1440 and 375.**
**Ruled by Kain** live in this sitting, from three designs he specified in a
written brief and then compared on a real page. His words:

> "I like A, the Editorial index please claude"

**Owning documents: DSRD 9's record of the contents card and DSRD 8's component
entry.** This component has no design folder and no build sheet, so under the
S257 transition note its DSRD section is the standard and only Chat can write to
it. **That is what is asked back.**
**Board card:** none of its own; site-wide.

---

## What is on the page

A white panel with a thin border and the card corner: a short copper rule, the
label "Your guide to this article", the title, then the real section count and
reading time. Numbered rows with fine rules between them, a discreet arrow, and
the section being read on a pale copper ground. Sharing sits below the panel,
outside it, which is his brief.

It draws on the article and the book note, which are the two page types that
carry this card.

## Three of his rulings meet here, and two of them are superseded

**S081 and S082 built the card he has just replaced,** and the values he set then
are recorded at the rules that carried them rather than deleted, because a
superseded ruling that vanishes reads later like a value that drifted.

- **The number is smaller than its title again.** At S082 he asked for it "a bit
  larger and completely aligned", and it went to the title's own size. His S110
  design says "a small muted number" and he approved the render. The tabular
  figures from S082 survive, because that was the other half of "completely
  aligned" and was never about size.
- **The space under the heading closes.** His S082 "a bit more space between
  Table of Contents and the next line" put 24 there. What follows the heading now
  is the metadata line rather than the list.
- **The reading line and the first-section rule are untouched.** S250 and S081.
  The new card keeps the old list and item class names precisely so that
  behaviour is reused rather than rewritten, and a second copy of a ruled
  behaviour is how two pages start disagreeing.

## What the comparison cost and what it bought

The three designs and the switch between them lived behind the workbench key for
one sitting and are **deleted**, files and all. A settled question left as a
switch is a question that gets reopened by accident.

**Four faults were found by rendering rather than by reading, and three of them
were already on the site.**

- The card's entries drew orange and underlined, because a block inside the
  article's reading wrapper must out-specify it. The quote page's build sheet
  carries the same lesson from S108 on a different component.
- Everything in the card centred itself on the book note, because that page
  centres this column, and the component had been built against the page that
  does not.
- **`knowledge-hub.js` was never enqueued on the book note.** So on every book
  note the contents highlighted nothing, the collapse did nothing and the
  copy-link control was inert. The comment beside that condition has said since
  S081 to widen it when another template drew this card; the book note has been
  drawing it. Widened now.
- The CSS counter that drew 01 to 05 was invisible to anything reading the page
  as text, so a screen reader heard an unnumbered list. It is markup now, and the
  current section carries `aria-current="location"`, which the old comment in the
  stylesheet correctly said it did not.

## The one thing that is yours, and it is not small

**His five colours are held as component tokens and are NOT in the palette.**
Four of them sit close to values base.css already registers without being them:
the main text is the brand dark exactly, the secondary is two shades off
`--color-soft-grey`, the divider two off `--color-hairline`, and the copper is a
third orange beside `--color-orange` and the AA-safe `--color-orange-link`.

Scoped to the component they are one place to reconcile. Loose in the palette
they would be four near-duplicates nobody could tell from drift a year from now,
which is the failure the token system exists to prevent. **It needs a decision:
either they become registered tokens with names, or the component adopts the
existing ones.** Not Code's, and not urgent, but it should not sit unrecorded.

## What his brief asked for and did not get

**The contents does not stay with the reader as they scroll.** There is no rail
for it to stand in: the reading column is the full width of the container, and
making room means either narrowing the reading or widening the page. That is the
decision he and I deferred earlier in the same sitting, and it is still open. The
card is built so it drops into a rail unchanged the day it is ruled.

---

OWED BACK: the contents card's DSRD entry updated to this design, and a decision
on whether his five colours become registered tokens or adopt the existing ones.

*No em or en dashes in this file; checked before writing.*
