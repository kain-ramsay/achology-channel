# RULING AND SHIP: the article page takes the Knowledge Hub hero, and its contents card moves beside the reading

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.286.0,
deployed, gated and measured at four widths.**
**Ruled by Kain** live in this sitting, on the rendered page, after two smaller
changes to the same region did not fix what he was seeing. His words:

> "I think we're gonna have to apply exactly the same hero styling to the
> article page. It's what we have to the book note page. So this article page is
> now a bit of a block here for us. I don't know what the solution is, but the
> top of the article page is not working. How about you suggest a far better
> design solution than what currently exists? Can you do that?"

**Owning documents:** DSRD 9 section 22, the article page, which is owed several
corrections named below. DSRD 8's entry for `kh-hero`.
**Board card:** none of its own.

---

## The proposal was that neither half is a new design

He asked for a design. What he got is two rulings he had already made, applied to
the one page that never received them. That is worth stating plainly, because it
is the reason to have confidence in it rather than my taste.

**One.** At S108 he ruled the book note's hero the pattern for every Knowledge Hub
page type, which is why `kh-hero` was lifted into components.css that session to
be the one band all of them read. The quote page took it. The article page did
not, so it was the last Knowledge Hub page still opening on a bare white
breadcrumb with no band at all.

**Two.** Earlier in this same session he asked for the contents to remain
"available alongside it as the reader scrolls down the page". On the article it
sat at the very top, was scrolled past in about three seconds, and then nothing
accompanied a reader down three thousand pixels of writing. The book note has had
it beside the reading throughout.

## The diagnosis, because it outlives this page

Measured on the rendered page before anything was drawn, the article's first
screen held three different column widths: the title and the top block at 1104
starting at 168, and the reading bar and body at 880 starting at 280. A reader was
asked to accept two left edges before the first sentence. His own written brief
earlier this session asked for the opposite: "keep the article aligned to the same
left edge throughout."

And the block filling that first screen was a 680 by 810 decorative picture. The
book note's equivalent is a book cover, which carries information; the article's
is atmosphere. It is now the band's ground, where atmosphere is the job.

## What was deleted, and what is recorded rather than lost

Gone: the S081 top grid and every width in it, the article's own hero header, the
featured image block with its rules and its placeholder label, and the trail's
separate 1104 container with its outdent and its 1152 release breakpoint.

**The S081 grid was approved by Kain on four rendered options and its saving was
real**, 1005px of page down to 548. It is superseded rather than wrong, and the
reasons are written at the place it stood rather than deleted with it. The same is
true of the S085 ruling that put the trail on the wider hero block: the trail and
the title still share an edge, but now because they are in the same container
rather than because two containers were kept in step by hand.

## What arrived

The shared band, holding the trail on dark, an overline naming the page type and
category, the title, and the article's own written summary as a standfirst. The
summary is the one already used on every listing card; nothing was drafted.

**The band takes its ground from a token with the bookshelf as its fallback**, so
the book note and the quote page were not touched and did not need to be. A
modifier class would have meant editing them to say they were unchanged.

The contents card floats right inside the body at the book note's own numbers, 300
wide with 40 across to the writing and 32 beneath, bleeding into the gutter above
1040 and going full width on a phone. Not near enough to the book note: the same
numbers, because two sets for one arrangement is how two pages drift.

## The overline needs a note, because it looks like a reversal

Kain deleted a category pill from this page at S080, ruling that a label above the
title repeating a word already in the trail "earns nothing and costs a line". The
overline repeats the category. It is still right here: in the band it costs no
line, and the book note carries the same overline above the same trail. Matching
the book note is the whole point of the change. If he reads it as the pill coming
back, it goes.

## One gate row I turned red on purpose

`header-to-content` wants 48px between the header and the first content. A
full-bleed band is flush against the header by design, so the article now reports
371 where it used to pass. **The book note fails the identical row for the
identical reason**, at 532. Every structural row this page now fails, the book
note also fails.

That is a check that does not know about hero bands, on three page types that all
have one. It is reported here rather than worked around, and it is not mine to
change: the rule belongs to the DSRD before it belongs to the gate.

## Measured after deploy

Title 33px, the standing rule the gate enforces, which moving into a band is not a
licence to change; the book note was caught at 42 doing exactly that at S108. Trail
and title both start at 168 on desktop, 32 on tablet, 20 on mobile. 48 below the
header and 48 below the trail at desktop and tablet. No sideways scroll at 390, 768
or 1024. The card is 300 and floated at 768 and above, 350 and full width at 390.

---

OWED BACK, and this is a longer list than usual because the page changed shape:

- **DSRD 9 section 22.3 and 22.4:** the page opens on `kh-hero`, not on a
  breadcrumb over a title on white. The hero's contents are overline, title,
  standfirst.
- **DSRD 9 section 22.5:** the featured image is the band's ground. The 880 by 420
  banner, and the S081 correction to it, both describe a block that no longer
  exists.
- **DSRD 9 section 22.6:** the contents card is beside the writing, floated right,
  not a cell in a top grid.
- **DSRD 8:** the `kh-hero` entry gains the article page and the fact that the
  band's ground is a token.
- **A question for the DSRD, not for me:** whether `header-to-content` should
  exempt a full-bleed hero band. Three page types now fail it correctly.

*No em or en dashes in this file; checked before writing.*
