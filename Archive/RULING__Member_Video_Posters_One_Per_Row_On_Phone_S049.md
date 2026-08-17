# RULING: the member video strip goes one clip per row on phone

**From:** Claude Code, S049. **Date:** 2026-08-06. **Filed under Harness Rule 14.**
**Shipped:** v0.38.65, deployed and verified live on both pages.
**Follows:** `RULING__Member_Video_Posters_Phone_Shape_S049.md`, which fixed the shape. This fixes the size, and closes the block.

## Kain's words

Ruled on the rendered page in Safari at phone width, after the shape fix shipped:

> "on mobile, it's too small. It's way too small. Uh, I think what we can do is, uh, like, what you've... the way we have this for tablet is fine. But I think when it goes to mobile, you just break those videos down so there's only one per line."

Two decisions in that, and both are recorded: **phone goes to one per row, and tablet is ruled fine as it stands.** The tablet half matters as much as the phone half, because it closes the tier rather than leaving it unexamined.

## And his question, which was the right one

> "Then that gives you the complete final solution for responsiveness across both pages. Plus any other page, um, on the website that we're gonna use this block. Am I right in assuming this?"

**Yes, and it is worth saying why rather than just agreeing.** The strip has one home: `achology_member_stories()` in `shared-parts.php`, with its rules in `components.css`. Neither page carries a private copy. So the two pages using it today, /about/ and /testimonials/, take this change together, and any page that adopts the block later inherits all three tiers without anyone remembering to do it.

That is the Source-of-Truth Rule (DSRD 3 §2.6) paying out. Had this block still been hand-authored per page, as several were before the collapse passes, this would have been two fixes today and a third one forgotten in six months.

## What changed

`components.css`, phone tier only:

```css
.about-proof__strip { grid-template-columns: repeat(2, 1fr); }   /* was */
.about-proof__strip { grid-template-columns: 1fr; }              /* is */
```

767.98px is DSRD 7 §4.1's own phone boundary, quoted from the canonical file this session: *"3 breakpoint tiers with CSS-exclusive boundaries: mobile <768px, tablet 768-1023px, desktop >=1024px"*. No new breakpoint was introduced.

## Verified live on both pages, at both sides of the boundary

Measured at 767 and 768 deliberately. A tier change is only proved by reading the page on both sides of its own boundary, and this is the lesson from S048, where `page_gate` sampled tablet at 900 and never saw the iPad defect sitting between 768 and 879.

```
/about/          390    one per row    350 x 197    ratio 1.78
                 767    one per row    727 x 409    ratio 1.78
                 768    2 + 3          344 and 224  ratio 1.78 both
                1440    2 + 3          432 and 283  ratio 1.78 both
/testimonials/   390    one per row    350 x 197    ratio 1.78    no sideways scroll
```

The artwork's own ratio is 1.78. Every card at every width matches it, so nothing is cropped at any tier, and the phone poster is now more than twice the width it was.

## What this closes

The three tiers of this component are now each ruled by Kain on a render rather than inherited: desktop and tablet keep the two-then-three composition he set at 2026-07-21, phone runs one per row from S049. Nothing about this block is waiting on a ruling.

*No em or en dashes in this file; checked before writing.*
