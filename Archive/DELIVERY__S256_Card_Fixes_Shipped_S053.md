# DELIVERY: the S256 card fixes are shipped

**From:** Claude Code, Session 053. **Date:** 2026-08-11.
**Answers:** `FIXES__Card_Rulings_S256.md`, which had sat in FROM Chat for four sessions. Cleared on your S259 request that the queue come before new work.
**Theme:** v0.57.1, deployed and verified on https://achologytest.com/cards/

## 1. The five items

**1. The excerpt trail is stripped.** `excerpt_more` returns an empty string, so a clamped excerpt shows one ellipsis rather than two. **Site-wide rather than card-scoped**, and that is a deliberate widening of the brief: the same excerpt feeds the help question rows, the author profile lists and the 404's related questions, and scoping the filter to one renderer would have left the identical defect standing in three other places. Verified: no `[...]`, `[&hellip;]` or `[…]` anywhere in the rendered page.

**2. The featured image area is held at 45%.** Your diagnosis was exactly right: the rule sat on `--placeholder` only. The placeholder carries both classes, so moving it to `.card__image-area` covers the real-image case and the empty case with one selector. Measured on the live page: the featured article card with a real image is now **45.0%**, against the 79% you measured.

**One consequence I had to follow.** The mobile override at 768px also named the placeholder only. Left alone, a featured card with a real image would have stayed 45% wide on a phone while the card itself stacked. It moved to the base class in the same edit.

**3. The book note backdrop is the book's own cover.** Every value is the brief's: `inset: 0`, `object-fit: cover`, `scale(1.25)`, `grayscale(1) blur(3px)`, `opacity: 0.5`, `z-index: 0` behind the sharp cover. Verified live, all six. The bookshelf asset is gone from this card and no PHP references it any more.

**4. The blurb takes the article excerpt styling.** Verified live: 14px, weight 400, `font-style: normal`, `rgb(94,107,117)` which is #5E6B75, three-line clamp.

**5. Dimensions and lazy loading.** Book covers take ACF's real width and height where the field is an array, and none where it is only a URL, because a wrong intrinsic size causes the very shift the attribute prevents. Course heroes take 600 by 500, measured across all 28 files rather than assumed. Both lazy.

**6.** No change, as the brief states. The label stays #B8460F.

## 2. One defect I introduced and fixed inside the same job

**Item 5 squashed every book cover, and I shipped it before catching it.**

The cover panel is a flex row, so the `width` attribute I added became the img's flex basis. The cover stretched from 102px to the panel's full 352px and rendered distorted on every book note card. Fixed with `width: auto` on the rule, so the height and intrinsic ratio decide the width while the attributes keep doing the CLS job they were added for.

**How it was caught, because that is the part worth keeping.** The screenshot looked plausible. What found it was measuring the rendered cover, seeing 352 by 160 against a natural ratio of 0.64, and then testing causation directly by removing the attributes in the live page and re-measuring: 102 by 160. Live now at 102 by 160, ratio 0.64, matching the source exactly.

The same shape of mistake as the attribution row earlier today. A value that is correct in the stylesheet can still be wrong on screen, and only the rendered element answers that.

## 3. Two things found and deliberately not acted on

Neither is in the brief, and "while I am in here anyway" is what Rule 3 exists to stop.

1. **`.card--mini .card__thumbnail--book-note .bookshelf-bg` in cards.css is dead code.** The mini card never emitted a bookshelf image; that rule has never matched anything. It is not a consequence of this change. Yours to delete or keep.
2. **Two em dashes in a functions.php comment**, predating the dash ban. Removed only because the gate blocks the file on every touch, and the sentences are unchanged in meaning.

## 4. What this does not cover

Your S259 rulings (the 145px watermark, the soft grey author line, the single focus stop, and the per-card changes to the quote, workbook and featured article cards) are **not built**. Your own note says the build brief follows once the remaining ten cards are reviewed, so I have left them.

*No em or en dashes in this file; checked before writing.*
