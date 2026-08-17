# FINDING: the site header does not fit between 768px and 879px, so every page scrolls sideways there

**From:** Claude Code, S048. **Date:** 2026-08-06. **Theme:** v0.38.52.
**Found by:** the DSRD 6 walk of the Policies index (page 10), §7 and §8.
**Severity:** hindrance under DSRD 6 §8's three-level scale, on every page of the site.

## RESOLVED the same session, 2026-08-06, v0.38.53

Kain ruled the fix directly in session on the rendered options rather than
waiting for a sweep brief, which Rule 14 makes his to do. The mobile menu now
takes over up to 880px. Verified live at 375, 768, 800, 879, 880 and 1440: the
sideways scroll is gone at every width and the menu opens. Kain confirmed the
result at phone, iPad and laptop width.

**The ruling and the document correction Chat still owes are in
`RULING__Mobile_Nav_Triggers_At_880_Not_768_S048.md`.** The one item that
outlived this finding and needs an answer is the page_gate sampling question at
the end of that file. Everything below is the original finding, kept because it
is the evidence behind the ruling.

## What happens

Measured on the live site, not in a preview:

| Viewport | Page scroll width | Sideways scroll |
|---|---|---|
| 640px (the 200 percent zoom equivalent) | 640 | no |
| 768px | 880 | yes, by 112px |
| 870px | 880 | yes, by 10px |
| 900px | 900 | no |

The single element pushing it out is the header's Sign In button, `a.btn-signin.site-header__cta`, whose right edge sits at 880px in a 768px viewport. `.site-header__inner` reports a natural width of 880px, so it cannot compress below that.

Confirmed on a second page, `/about/`, at 870px: identical numbers, identical natural width. It is the shared header, so it is every page.

## Why the band is exactly this wide

The mobile navigation takes over at `max-width: 767.98px`. Above that the full desktop header renders, and it needs 880px. So from 768px to roughly 879px the site shows a desktop header that does not fit the window it is in. The mobile toggle is `display: none` throughout that band, so there is no fallback.

768px is iPad portrait. This is not an obscure width.

## Why no gate caught it

`page_gate` measures at desktop, tablet 900 and phone 375. Tablet is sampled at **900**, which is just above the top of the broken band, so the gate has been stepping over it on every page it has ever measured. That is worth fixing whatever is decided about the header: a gate that samples one point inside a range cannot see a range.

## What I propose, and what I need

Two things, and both are decisions rather than typing:

1. **How the header should behave in that band.** The obvious candidates are moving the mobile navigation breakpoint up to where the desktop header actually fits, or making the desktop header compress to fit 768. That is a design question about what the site looks like on an iPad, and it belongs to Kain and to the mega menu and footer design session that `BRIEF__Accessibility_Statement_Space_Sentence_S248.md` already defers other header questions into.

2. **A signed sweep brief**, because the fix lives in the header and the header is on every page.

Separately, and mine to do once someone rules on the above: **`page_gate` should measure at 768 as well as 900**, so this class of defect cannot hide between sample points again. I have not changed the gate yet, because changing what the instrument measures mid-walk would make the nine records already filed incomparable with the ones still to come. That sequencing is worth a ruling too.

*No em or en dashes in this file; checked before writing.*
