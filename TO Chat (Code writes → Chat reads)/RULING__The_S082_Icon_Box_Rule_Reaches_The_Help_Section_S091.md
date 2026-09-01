# RULING: Kain's S082 icon box rule reaches the /help/ section

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Authority:** Kain, in session, on the two blocks side by side.
**Shipped:** theme v0.126.2, deployed, all three deploy proofs current.
**Filed under:** Harness Rule 14.

---

## The ruling, in his words

He put two screenshots side by side, the Knowledge Hub article page's Related
Further Reading block and the /help/ answer page's Other Related Questions
block, and said:

**"Please follow the same icon size rules throughout the Help section as what
we have already agreed on in the Knowledge Hub article pages"**

## This is not a new rule. It is his S082 rule reaching a page it never got to

The rule is already his, given at S082 and quoted in knowledge-hub.css:

> "this is completely disjointed and needs the top of the top line of text,
> and the bottom of the bottom line of text to align within the icon box
> sitting before it. Bring the icon box up in size to accomodate this please."

It was built for the Hub article page, extended to the book note page at S086,
and **scoped there deliberately**. That file's own comment says the site-wide
question "is still reported rather than assumed". This is Kain answering it
for the /help/ section.

## What was measured, before and after, on the rendered page

Before, on the answer page at 1440: the badge was the registered 36 square,
the two lines beside it were 52.4px tall together, a 24px heading at 1.25 and
a 14px supporting line at 1.6. The box sat 8.2px inside the text top and
bottom, aligning with nothing. The same arithmetic he objected to at S082.

After: the box is 52.4 square, the glyph is 24, and both edges land on the
text block's edges exactly.

**The box follows this block's own type, not the Hub's numbers.** The Hub's
heading is 21 and its box is 50.65; the Help heading is 24 and its box is
52.4. The rule is that the box matches the text beside it, so copying the
Hub's 50.65 would have broken the rule while appearing to obey it.

## Three faults found while checking, all fixed in the same pass

1. **The phone badge drew 27 wide inside its declared 36.** It is a flex child
   and nothing stopped it shrinking when the heading wanted the room. The
   Hub's box carries `flex-shrink: 0` and holds its square at the same width,
   measured the same minute. A mark declared at 36 that draws at 27 is not a
   size anyone approved, so the guard went in.
2. **The /help/ landing heading has no supporting line.** "Popular Articles"
   is one line, so the box stretched to 30 tall, kept its declared width and
   drew as a squat rectangle. The rule is now asked with `:has()` against the
   supporting line itself, so it applies only where there are genuinely two
   lines to align to, and a header that gains or loses its second line moves
   by itself.
3. Both were re-measured at 375 and at 1440 after the fix, on the rendered
   pages, rather than reasoned about.

## What was NOT swept, and it needs your eye

**`.help-popular__head` is on eight surfaces**, not three: the /help/ landing
and answer pages, and also the 404 page, Member Testimonials, About, the
Founders' Letter, the Manifesto and the Code of Ethics.

Kain named the Help section. `.help-page` is on the three /help/ templates and
on none of the other five, so that is the scope line, and the same call the
Hub made and recorded when it scoped to two pages.

**So five surfaces still carry the unaligned box, and still squash on the
phone.** Verified on the rendered About page after deploy: 36 square, glyph
18, unchanged. That is correct against the rule as it stands and probably
wrong against what he actually wants, but a change reaching five more page
types is a sweep and needs his word.

## A separate finding on the component itself, not acted on

The section header component's build sheet gives its title as **Como 22px/600**.
The Knowledge Hub renders it at **21px** and the /help/ block at **24px**.
**Neither surface matches the sheet, and they do not match each other.** Read
this turn from `COMPONENT_DATA__section-header.json`, row "Title".

I have not touched any of the three. It is a component question, it needs the
prototype rather than the code to settle it, and it was not what he asked for.

## What is asked of Chat

1. This ruling written into the section header component's record, as the
   answer to the open site-wide question that component's own note carries.
2. The five unswept surfaces put to Kain as one yes or no: do they follow.
3. The 22 against 21 against 24 title discrepancy raised at the component's
   own sitting.

OWED BACK: nothing blocking. The /help/ section is correct as he asked.

*No em or en dashes in this file; checked before writing.*
