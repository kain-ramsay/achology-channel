# RULING: the five member video posters keep their own shape at phone width

**From:** Claude Code, S049. **Date:** 2026-08-06. **Filed under Harness Rule 14.**
**Shipped:** v0.38.64, deployed and verified live. **Pages affected: two**, /about/ and /testimonials/, which share the component.

## How it arrived

Kain checked the About page at phone width, which is DSRD 6 §11 item 5, the check that exists precisely because he judges pages on a desktop screen. He found it immediately:

> "the page looks fine apart from the five aspects of the ecology experience block. That bit there, um, is crushing the images in, so there's no responsiveness there... they won't display correctly in mobile view."

Asked for the fix and given it in plain terms, he ruled:

> "Yes, please go ahead."

**This is the §11 item 5 check earning its place.** My own walk of this page, filed earlier the same session, recorded §7 and §8 as passing at phone width. It measured layout, overflow and scroll, all of which were genuinely fine. It never asked whether a picture was the right shape, and no gate does. His eye caught in seconds what the instruments were never going to.

## What was wrong

`components.css` carried, inside the phone media query:

```css
.proof-card { flex-basis: 200px; }
```

`.proof-card` declares `aspect-ratio: 16 / 9`, which is the shape of the poster artwork, 460 x 258. Its parent `.proof-figure` is a **column** flex container, and in a column container `flex-basis` sets the height, not the width. So that line pinned every card to 200px tall while the grid gave it 167px wide: a landscape frame turned portrait, and `object-fit: cover` then cropped the sides off the picture to fill it. Measured on the live page before the change, each card rendered 167 x 200, a ratio of 0.83 where the artwork is 1.78.

**It is a leftover.** This strip used to be a horizontal scroller, where `flex-basis` sized each item along the row and 200px was its width. The scroller became a grid; the line survived and silently reversed meaning. The `scroll-snap-align` still sitting on `.proof-card` is the other survivor of that layout. It is harmless, so I have left it rather than tidy something nobody asked me to touch.

## Verified live, not asserted

```
components.css?ver=0.38.64, phone width 390px
  card 1   167 x 94   ratio 1.78     image ratio 1.78
  card 2   167 x 94   ratio 1.78     image ratio 1.78
  card 3   167 x 94   ratio 1.78     image ratio 1.78
  card 4   167 x 94   ratio 1.78     image ratio 1.78
  card 5   167 x 94   ratio 1.78     image ratio 1.78
  the artwork's own ratio            1.78
```

Card and image agree with the artwork to two decimal places on all five, so `object-fit: cover` has nothing left to crop.

## Two things for the record

1. **This touched a shared file and therefore two pages**, which Rule 3 would normally send to a sweep brief. It ran on Rule 14 instead: Kain reported the defect from the live site and ruled the fix in session, and his word is the authority a brief would only have repeated. Testimonials carries the identical component and is fixed by the same change; it needs no separate pass.
2. **Still open, and his, not mine.** At phone width the five now sit two across at 167px wide, which is small for a video poster. The shape defect he reported is fixed; whether they should also go one per row at full width is a composition question on a composition he set himself (the two-then-three arrangement, 2026-07-21). Put to him next time he has the page open, not decided here.

*No em or en dashes in this file; checked before writing.*
