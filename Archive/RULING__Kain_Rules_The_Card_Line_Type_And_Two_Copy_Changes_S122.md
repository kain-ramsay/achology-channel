# RULING: the choice card's two lines, and two copy changes Kain made in the same sitting

**From:** Claude Code, S122, Thursday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files rulings and specifies no page.

Read with the three S122 rulings before it: The Chooser as the layout, his own
copy for the four cards, and a colour per card with the "Edge and tint" design.

## Ruling one: the card's two lines are set apart by weight

He put the fault himself:

> "having two lines of text just exactly the same font, it doesn't really sit right with me ... why don't you rethink how you've structured them and propose how you can improve the look of it from a fonts perspective that aligns with our font rules and standards and spacing."

He was right. On every card the first line qualifies the price directly above it
and the second is a separate fact: "$7 Trial" is qualified by "For Your First 30
Days", while "Then $34.50 Per Month" is a different statement entirely. One size
and one weight told a reader the two carry the same weight.

Shown four type structures, all built from rows that already exist in DSRD 7
sections 3.1 and 3.2 with no size, weight, colour or spacing step invented, he
ruled:

> "Weight not size is my choice"

**Both lines stay on the 12px Card Stats row. The first takes weight 600 in
brand dark, the read colour (section 1.1); the second stays 400 in soft grey.**
No size, face or case is added. It is the same move the site already makes on
the opening paragraph of every reading page, "set apart by weight alone"
(section 3.2).

**The three that lost are deleted:** the first line tucked under the price in mid
grey; the first line as an uppercase Como label with the second at 14px; and the
two joined into one line with a middle dot. All three are in the theme's history
at v0.472.0.

## A correction folded in just before it, and worth the record

Earlier in the same sitting he said the line under the price "was previously
smaller, looked much, much better" and asked for the cards to be "a bit more
succinct, a bit more compact and neater looking". He was right and the cause was
mechanical rather than a choice: before his copy, the line directly under the
price was the price's own qualifier at 12px; his copy replaced the qualifier
with a line of its own, and that line was put on the 14px facts row instead of
the 12px row the qualifier had. **Nobody chose 14.** Both lines went to the 12px
Card Stats row, the pair tightened from 8 apart to 4, and the button came up
from 24 to 16. The card went from 244 tall to 226.

## Ruling two: his replacement page title

> "Flexible Pricing to Fit Your Budget"

It replaces "Choose how you want to learn." The orange Achology rule (section
3.0) does not reach it: the word is not in the title.

## Ruling three: his replacement subheading, and the segment it retired

His new lead, typed in exactly as given:

> "Start with a single course, take two courses at the same time, explore a school, or open up the full Achology curriculum. We value transparent pricing and hope you do too."

Its second sentence said what his own third statement segment already said ("We
value honest and transparent pricing. Our pricing reflects this."). Both sets of
words were his, so the overlap was put to him on the rendered page rather than
resolved by Code, and he ruled the segment out: **"Claude, please just put it
in."** Two segments remain where there were three, and the strip takes two
columns at the desktop tier rather than three.

## Two register questions still open for Chat, restated so they are not lost

From the previous S122 ruling and unchanged: DSRD 7 section 3.1 has no row for a
choice card's price, which takes the 33px Statistic Figure row, and none for a
choice card's name, which takes the 12px Overline row. Both are existing steps
used by a new role, so no size was created, but the register does not know about
the role. And the palette holds three distinct accent families where the card row
wants four.

## The fold-back, complete this session (Harness Rule 14)

- Built, gated (`css_gate.py`: `pricing.css` PASS) and deployed at theme
  **v0.473.0**; server, local and zip proved identical by `deploy.py`.
- The approved state exported as the prototype's next version, in the Pricing
  Page folder inside Homepage + Commercial Design Prototypes.
- Read back off the rendered page: first line 12px at 600 in #354149, second
  12px at 400 in #5E6B75, cards 226 tall at 1440 and 390, nothing overflowing,
  every button clearing 44px.
- One fault of Code's own fixed on the way: the preview builder opened its tab
  behind whatever Kain had in front, which is how he was handed a blank
  favourites tab after a restart. The tab is made current now.

## OWED BACK

Nothing to answer. Write the rulings into the documents that own them.

*No em or en dashes in this file; checked before writing.*
