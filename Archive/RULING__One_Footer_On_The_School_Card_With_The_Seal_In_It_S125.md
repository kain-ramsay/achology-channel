# RULING: one footer on the school card, with the Seal built into it

**DOCUMENT TYPE: ruling record, not a page spec.** It records a ruling Kain gave in session and specifies no page.

**From:** Claude Code, S125, Monday 21 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Reads with:** the two S125 rulings filed before it, and `RULING__The_School_Cards_Take_The_Payment_Options_Menu_S124.md`, whose one-row footer this replaces.
**OWED BACK:** fold this into DSRD 8 section 8 as the pricing page's school panel footer, replacing whatever the S124 rulings put there.

## What was put to him, and what he said

Four kinds of buying block were built and shipped at **v0.526.0** on his S124 instruction that each option be a different kind of object rather than a different arrangement: Row, Floor, Seal and Ticket. He did not choose one. He told Code the question had been misread, and he is right.

> "I don't want two footers on these cards. I just want one. Alright? You keep on pushing two different footers. This is such a waste of space. My question is, how can we incorporate the Seal option into this bottom footer, so that Pricing Options dropdown, Enrol Now, and the actual price are all on the same line? Do you understand what I mean by all on the same line, all within the same block, i e, not on two rows, not in two blocks, not on two lines, all in one ... If we need to get rid of the save percentage, then we do that. I don't care ... In fact, no, we can't get rid of that. So can you please not take half an hour and just build the Seal into the bottom block in each school."

**The misreading, named so it is not repeated.** Three of the four options answered "make the bottom of the card simpler" by giving the card a second horizontal band, and he had already said at S124 that the two bottom blocks should become one. He was not asking which second band he preferred. He was asking for one band with everything in it.

## What was built, on his instruction rather than as options

The Seal stops being a flag on the school's artwork and becomes the price itself, standing in the card's one footer between the plan and the action: **Pricing Options, then the price in the school's own text-safe colour, then Enrol Now, on one line, in one block.** The other three treatments are deleted rather than parked; they are in the theme repository's history at v0.528.0.

Two things carry the row:

- **The field stops being a field.** It keeps every bit of its behaviour, its keyboard reach and the resting words he ruled, and loses the border, the fill and the field height that made the least important object in the row the loudest thing in it.
- **The saving sits inside the seal, under the figure.** He said it could go and then said in the same breath that it could not, so it stays where it belongs. Measured: beside the figure the seal wanted about 190 in a row that has 354 where the seven stand two abreast, which is 58 short once the plan and the action have what they need. Under the figure the seal wants 134 and the row closes.

## One thing reported to him and not hidden

**On a tablet and a phone the action takes its own line.** No arrangement of three objects crosses a card 242 points wide, which is what the card is when the seven stand two abreast on a tablet. His one line holds at both desktop widths. Told to him in the sitting in one sentence rather than left for him to find.

## Shipped

Theme **v0.529.0**, deployed, with local, the server and the zip each measured and agreeing. `css_gate`: pricing.css PASS.

Checked on the rendered page at 1440, 1024, 768 and 390, driving the menu rather than reading the markup: one line at both desktop widths, nothing outside a card, nothing clipped, the plan's words whole on every card, every choice changing the figure in its own card, and no sideways scroll.

The preview bar is one page again and the three extra rendered pages are deleted.

## Still open on this page

The two membership panels and the free tier strip, the questions block, the closing help strip, and the page's rhythm judged last. `/pricing/` is still unpublished on Chat's S365 disposition and its DSRD 6 record is not filed.

*No em or en dashes in this file; checked before writing.*
