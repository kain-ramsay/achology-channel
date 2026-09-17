# RULING: a colour per choice card on the pricing page, and the card design is settled

**From:** Claude Code, S122, Wednesday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files rulings and specifies no page.

Read with the two S122 rulings that come before it: The Chooser as the page's
layout, and Kain's own copy for the four cards.

## What started it, in his words

He asked what design effort had gone into the four cards. The honest answer,
given to him, was almost none: every value on them was legal and off the
approved list, which is checking rather than designing. Four faults were named
to him rather than excused.

- The card was the site's generic white card, reached for without asking what a
  card that sells something should look like.
- The price was 24 against an 18 name, so on a page about money the money was
  barely louder than its own label.
- The action was a small orange text link at the foot of the card.
- The four were equal, so nothing told a reader where to start.

## Ruling one: the treatment goes on all four cards, each in its own colour

Shown four card designs and choosing the ranked row, he then widened it:

> "I like ranked row, but I think we just need the same styling to be applied to all four cards, if that makes sense. Not the same color. Different different colors or different shades ... that this kind of system applied to each card, like what you've applied to card three, except different colors for each."

And on why the pass earns its weight:

> "the access all areas pass, it's not gonna be for everyone. That's like we're pitching a premium product here."

## Ruling two: the card design is "Edge and tint"

Shown four designs of that treatment, he ruled:

> "Edge and tint"

Each card carries its colour three times over: on its top edge, as a six per
cent wash of its own ground, and in its full-width filled button. The name is an
overline, the price leads at the 33px Statistic Figure row, and Kain's two lines
sit between them.

**The three that lost are deleted:** the edge alone on a white card, a solid
band of colour carrying the name, and the colour carried by the price itself.
All three are in the theme's history at v0.466.0.

## The four accents, and the one thing Chat needs to record

| card | accent | DSRD 7 source |
|---|---|---|
| On-Demand Courses | soft grey #5E6B75 | section 1 |
| Discounted Bundles | brand dark #354149 | section 1 |
| Access ALL Areas | brand orange #ED6922 | section 1 |
| Membership Plans | AA-safe orange #B8460F | section 1 |

Every accent is a section 1 value and not one is invented. **School colour is
deliberately not used:** section 2 scopes it to "wherever a school is named", and
these cards name ways to buy rather than schools.

**The palette holds three genuinely distinct accent families and this row wants
four.** The fourth here is the orange's own AA-safe partner, so the last two
cards are two weights of orange rather than two different colours. This was put
to Kain on the render rather than fudged. **A true fourth colour is an addition
to DSRD 7 section 1: his to approve, Chat's to write, never Code's to invent.**

**Two register questions for Chat, both arising from this ruling and neither
settled here.** Section 3.1 has no row for a choice card's price, which now takes
the 33px Statistic Figure row; and no row for a choice card's name, which takes
the 12px Overline row. Both are existing steps used by a new role, so no size was
created, but the register does not yet know about the role.

## Still open and still his

Three of the four cards carry the same two lines, which is a copy problem rather
than a design one. It was named to him on the render and he has not ruled on it.

## The fold-back, complete this session (Harness Rule 14)

- Built, gated (`css_gate.py`: `pricing.css` PASS) and deployed at theme
  **v0.467.0**; server, local and zip proved identical by `deploy.py`.
- The approved state exported as the prototype's next version, in the Pricing
  Page folder inside Homepage + Commercial Design Prototypes.
- Measured on the rendered page at 1440 and 390: four distinct accents, all four
  cards equal in height, every button at 44px, nothing overflowing, one text
  edge.
- One fault found and fixed before he saw anything: the card is a column flex box
  and the button was giving up its own height, so all four rendered under 44px on
  a phone.
- One em dash in `pricing.css`'s own header comment, predating this sitting,
  cleared on the way past.

## OWED BACK

Nothing to answer. Write the rulings into the documents that own them, and
record the two register questions and the palette question above.

*No em or en dashes in this file; checked before writing.*
