# RULING: Kain rules the artwork card for the seven school panels

**DOCUMENT TYPE: ruling record, not a page spec.** It records a ruling Kain gave in session and specifies no page.

**From:** Claude Code, S124, Wednesday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**OWED BACK:** fold the ruling into DSRD 8 section 8 as the pricing page's school panel treatment, and note in DSRD 9 section 36 that the panel now carries the school hero artwork.

## What was put to him

Five visual directions for the seven school panels, built into the theme and rendered on the whole page at `achologytest.com/previews/pricing.html`, one on screen at a time from the option bar, every one checked at 1440, 1024, 768 and 390 before he saw any of them. Not one word, figure, link or price differed between them, and all five kept the stack he ruled at S123 with one course name per row.

- **Artwork.** The school's own watercolour in the card's head, over the whisper of its colour that DSRD 8 section 8.1 approved on the course card.
- **Band.** A solid header in the school's deep colour with the name reversed out in white.
- **Spine.** A colour edge down the card, a short rule under the name, and the money on an off-white floor.
- **Crest.** The artwork as a round badge sitting on the card's top edge.
- **Lift.** The seven as white objects with the card shadow on an off-white ground.

Code recommended Band. Kain ruled otherwise, which is the point of putting five in front of him.

## His ruling, in his words

> "I'm gonna be honest with you, the artwork version looks absolutely stunning. Very, very, very nice. So let us let us let us go with this option ... our the artwork option is is is our choice. We're definitely going for this."

## What was done with it in the same session

- The artwork treatment stopped being a variant and became the card. The four that lost were deleted rather than parked; they are in the theme repository's history at v0.512.1.
- Shipped and deployed as theme **v0.513.0**. Local, the server and the zip were each measured and agree.
- The approved state was exported as the pricing page's prototype under Rule 14's fold-back.

## Three corrections made silently in the same pass, because the written standards already required them

None of these was a design choice and none changed a word.

1. The money row and the action row are pinned to the card's floor, so two cards sitting side by side put their prices and their buttons on the same line. Measured before the fix at 1440: the grid made the cards equal in height and their contents were not.
2. The school name is held at a whole number of its own line boxes, so a school whose name wraps does not shunt its whole card down against its neighbour.
3. Four rules naming a flex arrangement on the card's head and a price element this card does not have were removed. They read as live layout and drew nothing.

## One filing decision, named so it can be overturned in a word

The Pricing Page folder held a prototype named for the component last ruled on, `PROTOTYPE__course-index-with-monthly-figures.html`. Each fold-back exports the whole page, so a second ruling would have made a second near-identical copy of one truth. There is now one prototype for the page, `PROTOTYPE__pricing-page.html`, and the S123 file is deleted rather than kept beside it; the course index inside it is unchanged and is the same artefact Kain approved at S123. Technical call, Code's, per The Shared Rules section 8.

## One fault reported and deliberately not touched

On a phone, nine of the twenty-eight rows in the course table print the middle price on top of the full price. It is an overlap rather than a tight fit, measured at 390. The course block is signed off and Kain ruled it closed, so it was reported to him in the sitting and left alone pending his word.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
