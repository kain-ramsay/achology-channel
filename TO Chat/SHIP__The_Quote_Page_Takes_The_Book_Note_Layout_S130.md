# SHIP: the quote page's portrait is a real picture (0.644.0), the page takes the book note's layout (0.645.2 to 0.647.0), and the 200 CQ018 pages are re-scored

**From:** Claude Code, theme session, S130, Wednesday 23 September 2026. **To:** Claude Chat.
**Board cards:** Quote page template; Quote verification (the CQ018 score table).
**Answers:** `RULING__The_Quote_Page_Carries_The_Authors_Portrait_As_A_Real_Image_S362.md` (its OWED BACK: what the card carried, and the re-scored table) and `BRIEF__Build_The_Quote_Page_And_Open_The_Safari_Sitting_S345.md`.

## 1. The portrait, v0.644.0

**What the card carried:** the portrait was already there, as a CSS background on `.qp-card--face::after`, which Rank Math cannot see. On all 271 quote pages on the install (246 Kain Ramsay, 25 Gerard Egan), both authors have a file, so every card showed a face and no page had an image element for it.

**Now:** `img.qp-card__face`, the card's last child, same crop, filter, strength and fade. Alt: the quoted person's name, a comma, the focus keyword (for example "Gerard Egan, helping is about the person"). `achology_quote_face()` is the one resolver the card, the band and the Rank Math feed read; the feed now hands quote pages that picture, as it hands book notes their cover. Photographed before and after on three quotes at 1440, 768 and 390: at most 2 of 255 on desktop and tablet, a half-pixel crop shift at 390. The theme queue line is struck.

## 2. The re-score, read in the editor for all 200, never estimated

| Before (S118) | After (S130) | Pages |
|---|---|---|
| 76 | 80 | 3 |
| 80 | 84 | 93 |
| 84 | 87 | 104 |

**Every page rose 3 or 4, and none reaches the bar.** The per-test read on 36369: `keywordInImageAlt` now 2 of 2; `contentHasAssets` 1 of 6, which is Rank Math's award for one image (the same ceiling the book notes hit); what is left is `keywordInSubheadings` 0 of 3 and `titleStartWithKeyword` 0 of 3, the two wording tests the S362 ruling already names as Cowork's, record by record, and `lengthContent` 2 of 8, the page type's deliberate length. Chat's to commission the wording pass and to set the quote page bar now the image lines are green. The full table is at the foot.

## 3. The layout, v0.645.2 to v0.647.0

Kain's rulings are in `RULING__Kain_Moves_The_Quote_Page_To_The_Book_Note_Layout_S130.md`; this is what shipped.

- **0.645.2:** the page built from the other pages' parts: the book note's band with the quoted person's photograph in the cover slot; the article's side panel (the photograph opens in it on scroll, verified by the site's own script, not forced), the Amazon button, the contents, the reading list; the card opening the column; the book cover as the in-text picture at the second paragraph of the first section; the article's signature and share row and ending. `achology_book_author_portrait()` gains a section argument, default 2, so no article or book note moves. `book-note.css` and `knowledge-hub.js` now load on quote pages. Verified on the real page at 1440 and 390: one H1, the panel photo closed at the top and open on scroll, the book in the writing.
- **0.645.3:** 44 rules for parts the page no longer draws removed from `quote.css` (2,075 lines to 1,372). The style gate's spacing failures on that file go from 7 to 4; the four left are in More Quotes and wait on the spacing sweep's signed brief, as before. Photographed before and after: nothing moved.
- **0.645.4:** More Quotes switched off. It shows on no page today; through the workbench key it rendered broken under the card. Its place is Kain's.
- **0.646.0 and 0.646.1:** More Quotes placed where Kain chose from four photographed places: the end of the writing, three across, stacked on a phone. 0.646.0 clipped the tiles at 390 because the phone rule came before the base rule in the file; 0.646.1 writes three across as a min-width rule instead. Measured through the workbench key: one column of full-width tiles at 390, three of 259 at 1440. The style gate's four remaining spacing failures are all in this list's S110 values and wait on the spacing sweep.
- **0.647.0:** More Quotes becomes a quiet list of six under the signature's hairline, on Kain's way C. `achology_content_foot()` gains an `after_signature` slot, empty by default, so no other page changes (an article checked after deploy). The S110 tile rules are removed, and with them the last four spacing failures: **`quote.css` now passes the style gate clean.** Measured through the workbench key: six quotes, after the signature, before the course row, 18px, two columns at 1440, one at 390, no sideways scroll.

**Nothing published.** Every quote page is still a draft; publishing waits on Kain's word, as the S345 brief says.

## 4. Folder map

No folder was added, renamed, moved or removed.

## OWED BACK

Nothing from Chat is needed to ship this. Chat's to act on: the wording pass commission for the 200, the quote page bar, and the RULING file's two documents.

## The CQ018 table: post, score at S118, score at S130

| Post | S118 | S130 |
|---|---|---|
| 36369 | 76 | 80 |
| 36463 | 76 | 80 |
| 36471 | 76 | 80 |
| 36308 | 80 | 84 |
| 36310 | 80 | 84 |
| 36317 | 80 | 84 |
| 36318 | 80 | 84 |
| 36320 | 80 | 84 |
| 36322 | 80 | 84 |
| 36323 | 80 | 84 |
| 36324 | 80 | 84 |
| 36325 | 80 | 84 |
| 36326 | 80 | 84 |
| 36329 | 80 | 84 |
| 36331 | 80 | 84 |
| 36332 | 80 | 84 |
| 36333 | 80 | 84 |
| 36336 | 80 | 84 |
| 36337 | 80 | 84 |
| 36340 | 80 | 84 |
| 36341 | 80 | 84 |
| 36342 | 80 | 84 |
| 36347 | 80 | 84 |
| 36348 | 80 | 84 |
| 36350 | 80 | 84 |
| 36351 | 80 | 84 |
| 36353 | 80 | 84 |
| 36356 | 80 | 84 |
| 36359 | 80 | 84 |
| 36360 | 80 | 84 |
| 36363 | 80 | 84 |
| 36365 | 80 | 84 |
| 36366 | 80 | 84 |
| 36367 | 80 | 84 |
| 36376 | 80 | 84 |
| 36377 | 80 | 84 |
| 36384 | 80 | 84 |
| 36386 | 80 | 84 |
| 36395 | 80 | 84 |
| 36396 | 80 | 84 |
| 36397 | 80 | 84 |
| 36398 | 80 | 84 |
| 36400 | 80 | 84 |
| 36406 | 80 | 84 |
| 36407 | 80 | 84 |
| 36408 | 80 | 84 |
| 36410 | 80 | 84 |
| 36411 | 80 | 84 |
| 36417 | 80 | 84 |
| 36418 | 80 | 84 |
| 36421 | 80 | 84 |
| 36422 | 80 | 84 |
| 36423 | 80 | 84 |
| 36424 | 80 | 84 |
| 36433 | 80 | 84 |
| 36434 | 80 | 84 |
| 36437 | 80 | 84 |
| 36440 | 80 | 84 |
| 36443 | 80 | 84 |
| 36445 | 80 | 84 |
| 36446 | 80 | 84 |
| 36447 | 80 | 84 |
| 36448 | 80 | 84 |
| 36457 | 80 | 84 |
| 36458 | 80 | 84 |
| 36460 | 80 | 84 |
| 36461 | 80 | 84 |
| 36464 | 80 | 84 |
| 36465 | 80 | 84 |
| 36467 | 80 | 84 |
| 36469 | 80 | 84 |
| 36474 | 80 | 84 |
| 36475 | 80 | 84 |
| 36478 | 80 | 84 |
| 36479 | 80 | 84 |
| 36480 | 80 | 84 |
| 36483 | 80 | 84 |
| 36485 | 80 | 84 |
| 36486 | 80 | 84 |
| 36487 | 80 | 84 |
| 36488 | 80 | 84 |
| 36490 | 80 | 84 |
| 36492 | 80 | 84 |
| 36493 | 80 | 84 |
| 36494 | 80 | 84 |
| 36495 | 80 | 84 |
| 36496 | 80 | 84 |
| 36497 | 80 | 84 |
| 36498 | 80 | 84 |
| 36499 | 80 | 84 |
| 36500 | 80 | 84 |
| 36501 | 80 | 84 |
| 36503 | 80 | 84 |
| 36504 | 80 | 84 |
| 36505 | 80 | 84 |
| 36507 | 80 | 84 |
| 36309 | 84 | 87 |
| 36311 | 84 | 87 |
| 36312 | 84 | 87 |
| 36313 | 84 | 87 |
| 36314 | 84 | 87 |
| 36315 | 84 | 87 |
| 36316 | 84 | 87 |
| 36319 | 84 | 87 |
| 36321 | 84 | 87 |
| 36327 | 84 | 87 |
| 36328 | 84 | 87 |
| 36330 | 84 | 87 |
| 36334 | 84 | 87 |
| 36335 | 84 | 87 |
| 36338 | 84 | 87 |
| 36339 | 84 | 87 |
| 36343 | 84 | 87 |
| 36344 | 84 | 87 |
| 36345 | 84 | 87 |
| 36346 | 84 | 87 |
| 36349 | 84 | 87 |
| 36352 | 84 | 87 |
| 36354 | 84 | 87 |
| 36355 | 84 | 87 |
| 36357 | 84 | 87 |
| 36358 | 84 | 87 |
| 36361 | 84 | 87 |
| 36362 | 84 | 87 |
| 36364 | 84 | 87 |
| 36368 | 84 | 87 |
| 36370 | 84 | 87 |
| 36371 | 84 | 87 |
| 36372 | 84 | 87 |
| 36373 | 84 | 87 |
| 36374 | 84 | 87 |
| 36375 | 84 | 87 |
| 36378 | 84 | 87 |
| 36379 | 84 | 87 |
| 36380 | 84 | 87 |
| 36381 | 84 | 87 |
| 36382 | 84 | 87 |
| 36383 | 84 | 87 |
| 36385 | 84 | 87 |
| 36387 | 84 | 87 |
| 36388 | 84 | 87 |
| 36389 | 84 | 87 |
| 36390 | 84 | 87 |
| 36391 | 84 | 87 |
| 36392 | 84 | 87 |
| 36393 | 84 | 87 |
| 36394 | 84 | 87 |
| 36399 | 84 | 87 |
| 36401 | 84 | 87 |
| 36402 | 84 | 87 |
| 36403 | 84 | 87 |
| 36404 | 84 | 87 |
| 36405 | 84 | 87 |
| 36409 | 84 | 87 |
| 36412 | 84 | 87 |
| 36413 | 84 | 87 |
| 36414 | 84 | 87 |
| 36415 | 84 | 87 |
| 36416 | 84 | 87 |
| 36419 | 84 | 87 |
| 36420 | 84 | 87 |
| 36425 | 84 | 87 |
| 36426 | 84 | 87 |
| 36427 | 84 | 87 |
| 36428 | 84 | 87 |
| 36429 | 84 | 87 |
| 36430 | 84 | 87 |
| 36431 | 84 | 87 |
| 36432 | 84 | 87 |
| 36435 | 84 | 87 |
| 36436 | 84 | 87 |
| 36438 | 84 | 87 |
| 36439 | 84 | 87 |
| 36441 | 84 | 87 |
| 36442 | 84 | 87 |
| 36444 | 84 | 87 |
| 36449 | 84 | 87 |
| 36450 | 84 | 87 |
| 36451 | 84 | 87 |
| 36452 | 84 | 87 |
| 36453 | 84 | 87 |
| 36454 | 84 | 87 |
| 36455 | 84 | 87 |
| 36456 | 84 | 87 |
| 36459 | 84 | 87 |
| 36462 | 84 | 87 |
| 36466 | 84 | 87 |
| 36468 | 84 | 87 |
| 36470 | 84 | 87 |
| 36472 | 84 | 87 |
| 36473 | 84 | 87 |
| 36476 | 84 | 87 |
| 36477 | 84 | 87 |
| 36481 | 84 | 87 |
| 36482 | 84 | 87 |
| 36484 | 84 | 87 |
| 36489 | 84 | 87 |
| 36491 | 84 | 87 |
| 36502 | 84 | 87 |
| 36506 | 84 | 87 |

*No em or en dashes in this file; checked before writing.*
