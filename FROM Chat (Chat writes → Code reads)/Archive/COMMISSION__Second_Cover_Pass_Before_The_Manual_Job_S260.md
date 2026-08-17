# COMMISSION: a second cover pass over the 64 misses, before any of it goes to a human

**From:** Claude Chat, Session 260. **Date:** 2026-08-11.
**Authority:** Kain, in session. He stopped a manual job going to Karen on the grounds that the machine sources were probably not exhausted. Chat researched it and agrees.
**Answers:** `MISSES__ISBN_And_Cover_Run_S049.md`, the 64 rows that block publication.
**Status of the human job:** held. A worklist and a briefing email for Karen were built this session and are not being sent until this pass reports.

## 1. What this is and why it is being reopened

Your S049 run was good work and its honesty is why this is possible: you recorded `blocked` as its own state rather than calling it a miss, you refused wrong-book covers rather than accepting them, and you filed a real work list. None of that is in question.

What is in question is whether the four sources you used were used to their limit. Chat researched them this session and found three of the four were not. **Two of the three failures look like reading a URL as a ceiling when it is actually a request.** That is worth knowing for its own sake, beyond this job.

The 64 split into two different problems and they need different treatment:

- **41 rows failed at ISBN lookup.** No identifier, so nothing downstream could run. The cover was never the obstacle.
- **23 rows have a correct ISBN and failed at the cover.** 18 where no source held one, 5 where what was held was too small or a placeholder.

## 2. Google Books, which you used, has five larger sizes you did not see

Two separate findings, either of which alone would have changed the result.

**The search endpoint only ever returns `thumbnail` and `smallThumbnail`.** The full set (`small`, `medium`, `large`, `extraLarge`) is returned by the **volume details endpoint, queried with a volume ID**. If the run took `imageLinks` from search results, the larger sizes were never in the response to be read. Get the volume ID first, then request the volume.

**There is also a direct URL form that takes arbitrary dimensions:**

```
https://books.google.com/books/publisher/content/images/frontcover/{volumeId}?fife=w1600&source=gbs_api
```

`fife` accepts width and height (`w1600`, or `w1600-h2400`). This is not a documented API surface, so treat it as a fallback rather than the primary route, and verify what actually comes back rather than trusting the parameter.

The `zoom` parameter on `books.google.com/books/content?id=...` behaves similarly, running 0 to 5.

**Where an `extraLarge` genuinely does not exist, that is a real answer** and the book falls through to the next source. Google sources covers from publishers and libraries and does not hold a complete set for every title.

## 3. Amazon's image host was very probably misread

Your record says Open Library, Google Books and Amazon's image host "all cap at roughly 500px on the long edge, tested across six titles".

Amazon almost certainly does not. Its cover URLs carry a size suffix, for example:

```
https://m.media-amazon.com/images/I/51z2HY7kn4L._AC_UY218_ML3_.jpg
https://m.media-amazon.com/images/I/51z2HY7kn4L._AC_UY500_FMwebp_QL65_.jpg
```

**`UY218` and `UY500` are the requested pixel height, not a limit.** Raising the number, or stripping the suffix block entirely to leave `51z2HY7kn4L.jpg`, generally returns a much larger image, often the original. If the six-title test used whatever URL the page happened to serve, it measured Amazon's display size rather than Amazon's stored size.

**Test this before building anything on it**, on two or three books whose covers you already hold, so you can compare like for like against what you saved.

## 4. Open Library has a second, larger route

The covers API tops out around 500px, which matches what you found. But a good number of these titles have full scans on Archive.org, where the cover page is available at far higher resolution than the covers endpoint serves. Open Library records link to their Archive.org item where one exists.

## 5. Sources not tried at all

**For covers:** Kobo and Rakuten serve large cover images. Publisher websites are the best single source for the 18 in group 2 and the major houses are consistent enough to be worth scripting. Bookshop.org and Waterstones are worth a pass, particularly for UK editions.

**For the 41 missing ISBNs, which is a different job:** WorldCat, the Library of Congress catalogue, and ISBNdb. None were tried. Several of these are classics that the free catalogues index under a different title, translation or edition, so a title-and-author search that tolerates variation will do better than an exact match. Once an ISBN resolves, everything in sections 2 to 5 becomes available to that row automatically.

## 6. What to run, and in what order

1. Re-test Amazon's size suffix and Google's volume endpoint on books you already hold covers for, and report what the two actually return. **If Amazon's suffix behaves as described, re-run it across all 44 low-resolution rows as well**, not just the 64, since those were saved from Open Library at 400 to 899px and would upgrade for free.
2. Resolve as many of the 41 missing ISBNs as you can.
3. Run every unresolved cover through the full source ladder, stopping at the first result of 900px or more.
4. Keep the S049 verification rule exactly as it stands: **every result checked back against expected title and author before the file is kept.** A wrong cover is worse than no cover, and that check is why 44 rows carry a small correct image rather than a large wrong one. Do not relax it to raise the hit rate.

## 7. What to return

The remaining misses, in the same shape as `MISSES__ISBN_And_Cover_Run_S049.md`, so it can go straight to Karen as a work list.

Plus four counts: how many of the 41 ISBNs resolved, how many of the 64 now have a cover of 900px or more, how many of the 44 low-resolution rows upgraded, and how many rows remain genuinely unsolvable.

And one line per source on whether it earned its place, so the ladder is recorded rather than rediscovered next time.

## 8. What not to do

**Do not lower the 900px bar** to make the numbers look better. The bar exists because DSRD 8 section 20.5 renders the cover at 288px wide and a 500px image is barely 1x.

**Do not upscale a small image.** An interpolated cover is a soft cover with a bigger file size.

**Do not add a fifth `cover_status` value or change the four in the contract.** The `low_res` question you raised at S049 is still open with Kain and is not yours to settle. If your pass upgrades those 44 rows to `ok`, the question dissolves on its own, which would be the tidiest outcome.

*No em or en dashes in this file; checked before writing.*
