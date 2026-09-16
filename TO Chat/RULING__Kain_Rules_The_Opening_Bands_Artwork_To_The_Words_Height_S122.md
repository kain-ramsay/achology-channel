# RULING: Kain rules the pricing page's opening band, and the artwork takes the words' height

**From:** Claude Code, S122, Wednesday 16 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files one ruling and specifies no page.

## The fault Kain found, in his own words

> "But it's it's this image that is creating all this kind of wasted space. Right? You've not even... you've not done anything to minimize the sheer volume of white space underneath it. So what are you seeing yes for when you have not even... it's like you've you've not even acknowledged the ridiculous amount of space that comes underneath it."

He was right and Code was wrong. Code had put four rendered options to him that
varied how the four route summaries were drawn, and all four left the hole
untouched. Measured on the rendered page at 1440 before the fix: the artwork 320
tall, his words 234 tall, 87px of nothing under the words, the band 711 tall.

## The ruling

Shown four rendered whole pages, one on screen at a time behind a bar, each
closing the space a different way, Kain ruled, whole:

> "I want the Fits the words option please!!!!!"

The artwork takes the height of the words beside it, at every width, so the two
columns of the band finish on the same line. Measured after: both 234, the gap
zero, the band 624 tall, which is 87px shorter.

**The three that lost are deleted rather than parked behind a switch:** the
artwork running the panel's whole right side beside the routes; the artwork
reduced to a small mark with the words taking the width; and no artwork at all.
All three are in the theme's history at v0.461.0.

## What was corrected silently on the way, each against a written sentence

- The lead took 16 under the page title. DSRD 7 section 4.3's table: "reading
  text under the page title | 24". Now 24.
- The band's head centred its two columns, which put the eyebrow 47px below the
  panel's own padding. A number on no scale, and the imbalance he named at S121
  ("It doesn't seem balanced in spacing").
- Kain's three statement segments joined their words at 768 and below. The
  stylesheet hides his line breaks there so the words wrap on their own, and a
  hidden break carries no space: his first segment read "Each course offers
  avarying length of freeAchology membership." on every phone. Fixed at source.

## The fold-back, complete this session (Harness Rule 14)

- Built, gated (`css_gate.py`: `pricing.css` PASS) and deployed at theme
  **v0.462.0**; server, local and zip proved identical by `deploy.py`.
- The approved state exported as the prototype's next version, in the Pricing
  Page folder inside Homepage + Commercial Design Prototypes.
- Checked at 1440, 1024, 768 and 390 before he saw anything.

## One thing for the record, not a question

Kain put a long piece of ChatGPT feedback on this page to Code in the sitting.
Three of its points are worth taking and all three are **copy** rather than
design, so they are his to supply: a line per route saying who it suits; the
lifetime-versus-membership distinction moved up near the top; and what
membership gives stated before the price. Three of its points asked for things
the page already does, checked live: the search reaches all 28 courses including
the folded ones, the count updates as you filter, and there is a reset. One of
its points is factually wrong: it claimed the page alternates between "Access All
Pass" and "Access All Areas Pass"; read off the rendered page, the page says
"Access All Areas Pass" in both places and nothing else. The rest asked Code to
undo Kain's own rulings and was not acted on.

## OWED BACK

Nothing. Write the ruling into the document that owns it. DSRD 4 section 3.1
already records that Kain's package leads the layout and the DSRDs lead every
figure; this adds the band's artwork behaviour to the pricing page's record.

*No em or en dashes in this file; checked before writing.*
