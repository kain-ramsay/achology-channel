# RULING and SHIP: four related questions on every help article, and the thank-you turns orange

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Ruled by:** Kain, in session, from the rendered help article.
**Shipped:** v0.38.13, deployed to achologytest.com, verified across a sampled spread
of articles and on the rendered page.

## The ruling

He noticed some articles showing three related questions and some four, and set the
standard himself:

> "what I think I would like for you to set is a standard, and that is a minimum and
> a maximum of four. Four related questions in the related questions block on every
> single page... and that's just within the FAQs pages articles."

And separately, on the thank-you line added earlier the same session:

> "maybe you could actually just make that text orange rather than gray"

**Please write the four into DSRD 2 §2.24** as part of the help article's definition,
so it is a standard rather than a note in a commit message.

## The measurement that shaped the fix

Counted across all 250 published articles before touching anything:

| hand-picked related links in the body | articles |
|---|---|
| four | 57 |
| three | 72 |
| two | 67 |
| no list at all | 54 |

So **139 articles were short**, and the block's length was effectively arbitrary. Kain
saw three and four; the real spread was zero to four.

## How it was fixed, and why not in the content

**In the template, not in 139 article bodies.** Editing the content would have meant
inventing 139 sets of editorial choices, which is exactly the kind of judgement that
is not mine to make, and it would have put the standard in 250 places instead of one.

The rules the template now follows:

1. **The writer's hand-picked links lead, unchanged, in their own order.** Nothing
   editorial is overwritten or reordered.
2. **Where the writer chose fewer than four, the block is topped up** from that
   article's own primary category, by the editor's Order field with newest as the
   tiebreak, carrying the linked answer's excerpt as its sub-line exactly as the
   hand-picked rows do.
3. **Never a repeat and never a self-link.** Anything the writer already chose, and
   the article itself, are excluded from the top-up.
4. **Where a writer chose more than four**, the list is trimmed to the first four.
5. Category sizes run from 7 to 36 answers, so the category always covers the
   shortfall. A section-wide pass sits underneath as a net that should never fire.

**One thing was deleted:** the separate fallback query that used to run only for an
article with no in-body list, rendering its own duplicate copy of the row markup. The
top-up covers that case and every other short case through one path, so the block can
no longer render two different ways. That is one less duplicated block, which serves
DSRD 3 §2.6's Source-of-Truth Rule as a side effect.

## The colour

The thank-you line is now **#C64E14**, the AA-safe orange, not the brand #ED6922.
DSRD 7 §5.1 names that exact value for that exact reason, read this turn: "label text
#C64E14 (AA-safe orange, 2026-07-16), 14px labels fail AA in brand orange." This line
is 15px on white, so the same reasoning applies and the brand orange would have failed
contrast.

## Verification, on rendered pages rather than source

**Twelve articles sampled across every starting count**, three that had four already,
three that had three, three that had two and three that had none:

**Exactly four related questions, with no self-link and no duplicate: 12 of 12.**

On the article page itself: four rows, the thank-you computes as rgb(198, 78, 20) in
Como, and the stylesheet is serving at 0.38.13. `php -l` on the deployed template:
no syntax errors. `css_gate help.css`: PASS.

## Scope note, same as the previous ruling

This touches every help article, so it is a sweep in the Rule 3 sense and there was no
signed brief. Built on Kain's direct ruling in session and recorded here. The question
I raised in `RULING__Helpful_Strip_Stays_Quiet_And_Takes_Como.md` about how the harness
should treat a ruling that arrives from Kain directly rather than through you still
stands, and it has now come up three times in one session.

*No em or en dashes in this file; checked before writing.*
