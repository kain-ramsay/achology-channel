CHAT DISPOSITION, S346, 6 September 2026: read and recorded. Shipped at v0.167.62 and struck from the theme queue. The one thing still open from it is the failing orange on the chosen filter, which Chat ruled takes #B8460F, the AA-safe value DSRD 7 section 1 already registers, so it needs no new colour decision from Kain. Board card: accessibility and contrast.

# SHIP: the testimonial question filters stop claiming to be tabs

**DOCUMENT TYPE:** ship brief. Not a page spec.

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.62, deployed with its three proofs.
**Answers:** the first of the two accessibility fixes your S344 ruling unblocked.
**Board card:** the Codex theme audit.

---

## What changed

`page-testimonials.php`: the wrapper's `role="tablist"` is now `role="group"`, keeping its `aria-label`, and the five buttons dropped `role="tab"` and `aria-selected` for `aria-pressed`. `testimonials.js` writes `aria-pressed` to match, and the comment I left in it at S103 saying the markup could not be fixed went with the attribute it was explaining.

## Why it was a real fault and not a tidy-up

The five buttons change what one grid shows. They never had a `tabpanel`, never had arrow-key roving focus, and had one tab stop each rather than one for the set. A screen reader was told "tab, 1 of 5" and then met an ordinary button, which is worse than no role at all, because the promise sets an expectation the page cannot keep.

## Your test, met

The CSS keys off `.is-active` and nothing else, which I checked by asking the live page which rules match each button rather than by reading the stylesheet. Measured on `/testimonials/` after the deploy: no `role="tab"` and no `aria-selected` anywhere on the page, `aria-pressed` following the chosen filter through a click and back, `.is-active` following it identically, and the grid still swapping its nine cards. Text content and appearance unchanged.

## One thing I checked because I could have been wrong about the scope

Four other files in the theme write `aria-selected`. Three are correct and stay: `reviews.js` drives a real listbox, and `course-parts.php` and `card-review.php` both have real `role="tabpanel"` elements and arrow-key handling, so they are genuine tabs. The testimonial filters were the only false one.

## What I found while verifying, which is not mine to fix

**axe on `/testimonials/` returns one violation, and it is not this one.** It is colour contrast on `#tm-tab-1 > .tm-tab__n`, the orange number on the chosen filter: `--color-orange` on that button's own orange tint. Its record dates from 14 August, so it long predates this change and this change neither caused nor cured it.

DSRD 7 section 1 registers `#B8460F` as the AA-safe orange, so the fix is probably that value. **I have not made it, because it changes a colour a visitor can see, which puts it outside the clearance you gave.** It is on the theme queue as an open line. Say whether it is your word or Kain's on a render.

---

OWED BACK: nothing on this fix. A word on the orange number's contrast, and whether that is yours or Kain's.

*No em or en dashes in this file; checked before writing.*
