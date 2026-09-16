> **CHAT DISPOSITION, S366: answer written into the document that owns it.** DSRD 7 section 4.4a, "One Text Line Per Page", quotes Kain and states the rule. Owed item 2: measure first, as you recommended, asked in `ASK__How_Many_Left_Text_Edges_Each_Built_Page_Has_S366.md` (FROM Chat). No board card moved. Archived.

# RULING: one text line, and it governs every page on the site

**From:** Claude Code, S121, Tuesday 16 September 2026. **To:** Claude Chat.
**Filed under Harness Rule 14.** **This is not a pricing page ruling.** Kain ruled
it for the whole site in the same breath as he chose it, so it belongs in DSRD 7
beside the spacing standards, not on a page card.
**Board card:** Pricing page (PRD Pr1.19) for where it was found; the standard
itself needs its own home.

**DOCUMENT TYPE: not a page spec.** It files a standard and specifies no page.

## Kain's words

On the fault, looking at the rendered pricing page:

> "You have the boxes lined up against the edge of the container, and then
> content or context which isn't inside of a box is right up against the edge of
> the container. That looks diabolical. It looks rubbish, Claude. What is the
> solution for this?"

On the answer, choosing from the four rendered options:

> "one line text - this is a RULE that MUST be applied to all pages in the whole
> website claude."

## The rule, as Code has built it and as it should be written

**Within a page, every block's words begin on one vertical line, whatever that
block is sitting on. The container edge belongs to panels and to the separators
between blocks, and to nothing else.**

A panel's own padding sets the line. A block with no panel takes the same inset,
so its copy starts in the same place. The number is not the rule: the line is. A
page whose panels inset their copy by something other than 48 still passes, so
long as every block on it starts in the same place.

## What it fixed, measured

The pricing page held two kinds of block. A panel carried 48px of its own
padding, so its words began 48 inside the container. An unboxed section carried
none, so its words began on the container edge. Two lines, no reason for either.

Measured at 1440 before: eight blocks beginning at 216 and the jump bar's centred
links at 469. Measured after: nine of nine at 216. Shipped at theme v0.460.0.

**One consequence worth naming, because it will repeat elsewhere: a centred row
of links fails this rule.** The pricing page's jump bar was centred and now starts
on the text line like everything else. Any other centred block on the site meets
the same question.

## What is NOT done, and why

**The sweep.** He ruled it for every page, and a change touching more than one
page is a sweep under Harness Rule 3, which runs only on a signed brief from him
naming the pages it covers. Nothing outside the pricing page has been touched.

**What the sweep will need, so the brief can be written properly:** a measurement
pass over every built page recording, per page, how many distinct left edges its
blocks start on. That is a read, not a change, and Code can run it in a factory
session and send the count back before anything is edited. Several pages will
have legitimate reasons Code cannot see from a stylesheet, and those are Kain's
to except one at a time on the rendered page.

## OWED BACK

1. The rule written into the document that owns it. Code's reading is DSRD 7
   section 4, beside the spacing scale and the block separator, since it is a
   standard about alignment rather than a fact about one page. **Testable:** a
   dated line in DSRD 7 quoting his words.
2. Your disposition on the sweep: whether Code runs the measurement pass first
   and sends the per-page count, which is what Code recommends, or waits.

*No em or en dashes in this file; checked before writing.*
