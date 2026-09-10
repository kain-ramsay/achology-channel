> CHAT DISPOSITION, S357: answered. The two section 20.6 departures and the wash override recorded in DSRD 8 section 20.6 and DSRD 9 section 32.3. Archived.

# SHIP: the quote page's hero is two columns, and the source block lives in it

**From Code, S108. Theme 0.190.0, deployed and measured on the specimen render.**

## What changed

The quote card comes down to 640 and sits hard against the container's left
edge, so its left edge lands exactly on the breadcrumb's home icon. The source
book block moves out of the article body and into the band beside it, against
the reading column's right edge. The banner comes down from 611 to 545, against
the book note's 533.

## Kain's ruling, in his own words

> "if we shift the quote down to 640 in size, then left align that to the end of
> the container so it aligns with the house icon in our breadcrumbs, then the
> quote source block, because of how we've designed that now, would fit perfectly
> next to the quote card on the right hand side of the hero."

He was right and I was wrong, and the correction matters for the record. I
argued the block could not go in the band because putting it there would squeeze
the quote. He was not proposing that: the card getting SMALLER is the move, and
the block then occupies space the narrower card leaves behind. My third
objection, that a narrower card would cost the shared 1200 by 630 picture, was
simply false: that picture is photographed from a card rendered alone on its own
page by `make_quote_cards.py` and never from this one.

## Departures from DSRD 8 §20.6, filed here under §12.3

1. **The block is no longer in the article body.** §20.6 places the shelf panel
   in the writing. It is now a second column of the hero. Everything about the
   block itself is unchanged: same 176 width, same header, same cover, same
   single control, same spacing.
2. **The block is drawn on a dark ground.** Three colours change and nothing
   else: the header to a near-white, its hairline to a faint white, and the
   mark's tile from a 10 per cent orange to a 12 per cent white. The tile had to
   move because a tint of orange is a lift off white and is invisible on dark,
   so keeping the number would have quietly deleted the tile Kain chose.

## One change nobody asked for, named rather than slipped in

The band's wash ran from 93 per cent on the left to 62 on the right. That was
drawn for the book note, where the hero deliberately lets the shelves show
through beside the title. This page now puts CONTENT in that bright corner, and
photographed, the block's white heading sat on pale book spines and was the
weakest thing on the page. The fade is removed **on the quote page only**; the
book note keeps it, because there it is still doing the job it was drawn for.

## What was measured on the built page

At 1440 and at 1024: band 545, card 640 holding its 1200 by 630 ratio, card's
left edge exactly on the home icon, block's right edge exactly on the reading
column's, all three parts of the block sharing both edges, the control's label on
one line, and the writing below unmoved. At 375 the row stacks and the block
centres. Two images reported unloaded at 375 are lazy and 4,500 below the fold;
they load on scroll.

## What page_gate could not do

`page_gate.py` cannot measure this page: the specimen renders only under its
workbench parameter, so the gate fetched a 404 and reported that page's faults,
not this one's. Its verdict on this address is worthless until the quote
template publishes real pages. The evidence above is read off the specimen
render.

## The display standard, after two failures

Kain rejected two preview harnesses in one session with the same words: they gave
him no visual context to decide. The cause was one thing both times. The harness
linked the theme's stylesheets straight off the site with no version on them, so
his Safari served him cached copies from before the day's work and the page
rendered broken for him while my headless check, with an empty cache, passed
every time.

**The standing rule now: a design decision is shown as photographs of the real
page.** The viewer around them carries no site stylesheet at all, so nothing in
it can be cached wrong. Each shot is checked before it is kept, and the viewer
itself is checked too. Written to memory as
`a-preview-never-links-the-live-stylesheets`.

## What I need from Chat

Nothing blocking. Please record the two §20.6 departures and the quote page's
wash override in DSRD 8 and DSRD 9 §32.3 when the quote page's spec is next
touched.
