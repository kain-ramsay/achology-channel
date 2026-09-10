# SHIP: the quote card is locked as a component. Rule 14's fold-back is done.

**From Code, S110. Date: Thursday 10 September 2026. Theme 0.258.0, nothing on
the card changed to do this.**
**Answers:** the recommendation in `RULING__The_Quote_Card_Is_Settled_S109.md`,
item 4 of what was not settled.
**Board card:** Quote page template.

---

## What was written, and where

Both writes are in the quote page's design folder, and Harness Rule 14 asks for
this file to name them.

1. **The prototype:** `PROTOTYPE__Quote_Card_S109_APPROVED.html`, the card as the
   server rendered it on its own 1200 by 630 frame, cut by `fold_back.py` with
   nothing hand patched, plus the photograph of it beside it as a JPG.
2. **The build sheet:** `BUILD_SHEET__Quote_Card.md`, written from the prototype
   rather than from the code, carrying the twelve rulings, every value as a share
   of the card's own width, and the four open items.

The quote page's own sheet held a copy of the card's values written at S108.
Every row of it about the card's furniture had gone stale within a day. That
section now points at the card's sheet and holds only what is the page's own.
The S108 card picture is in this folder's `Archive (Superseded)`.

The Rule 4 chain now has a top for this component: prototype, then sheet, then
code.

## Two faults found on the way, both fixed, both worth knowing about

**The export tool could not see the site at all.** SiteGround's Antibot answers
an automated browser with a challenge screen, so `fold_back.py` was
photographing a page titled "Robot Challenge Screen" and reporting "none of the
selectors matched", which reads as a bad selector and is not one. It now goes
through the mirror `page_gate.py` already built, which fetches from inside the
host over the SSH line, and it refuses rather than exports if a challenge ever
does arrive. Nothing was defeated; an existing door was used.

**The card baker cannot bake, for the same reason, and that is half of why the
share picture is stale.** `make_quote_cards.py` meets the same front door and
refuses honestly, so it has been unable to write a card. It is fixed in the same
way as part of the stale picture work, which is live in this sitting.

## What is still yours

**DSRD 7 section 15.2 still describes the bottom accent that came off at S109**,
asked for in the S109 ruling and repeated here only because the sheet now
contradicts the section in writing.

**DSRD 8's component record should point at the folder** rather than carrying the
card's values, which is what section 4 of The Shared Rules asks for once a
component is carried across.

## The one item that is Kain's, and it is small

The lockup is a fixed 34 pixels tall on the page and a share of the card's width
in the baked picture, so the picture that travels carries a smaller lockup than
the card he approved. Measured on both renders this session: 5.3 per cent of the
card's width on the page, 3.6 per cent baked. He is being shown it on a render in
this sitting.

---

OWED BACK: DSRD 7 section 15.2 corrected, and DSRD 8's component record pointed
at the folder. Nothing else.

*No em or en dashes in this file; checked before writing.*
