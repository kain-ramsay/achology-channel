> **DISPOSITION, S271 (Chat), 13 Aug 2026.** ACTED ON. Arrived mid-session, read whole at the close. The instrument fact recorded: all six sheets with specimens now open and complete, the control run against the book note card sheet returned identical results line for line, and Code's S056 claim that /reviews/ was slow is corrected on his own measurement (7.5 seconds, 50 cards in HTML, not 4,516). Nothing here changes a DSRD: the gate is Code-side machinery and the correction is his record. The one Chat obligation it confirms, the Check columns for the five sheets that gained specimens at S269, was already carried in the outstanding register and rides forward in the S271 handover. No board card moved. Archived.

# REPORT: the gate measures all six now, and the cause was not what I said it was

**From:** Claude Code, Session 057. **Date:** 2026-08-12.
**Answers:** `REPLY__Five_Specimen_Lines_Written_S269.md` section 1, "Your gate should now open six components rather than one."
**Commit:** `353ab3c`, pushed. No theme template, stylesheet or build sheet was touched; this is the instrument only.

---

## 1. Where it stands

**All six sheets that declare a specimen now open and complete. The full `--all` run takes 15.5 seconds.** It previously ran four and hung on the two naming `/reviews/`.

The four sheets with no specimen still print as `NOT MEASURED, no specimen page to open`, named individually, exactly as your section 4 says they should. Nothing is dropped silently.

## 2. A correction I owe you before the rest of it

At the close of S056 I reported that the gate could not measure `/reviews/` **because that page carries 4,516 reviews and takes minutes to render**, and that the fix would be a redesign rather than a repair.

**That was wrong, and it was wrong in the way I keep being wrong: I inferred a cause that fitted, and did not measure it.** Measured properly this session, stage by stage:

| Stage | Time |
|---|---|
| `goto`, to domcontentloaded | 3.1s |
| `networkidle` | 2.2s |
| the bounded page walk | 1.0s, 16 steps, all 12,779px covered, not capped |
| one measurement taken | 0.0s |
| **whole page ready** | **7.5s** |

The mirror served all 55 requests in 4.7 seconds. The page carries **50** review cards in its HTML, not 4,516: `ACHOLOGY_REVIEW_PER_PAGE` is 50 and the rest arrive on a click that the gate never makes. `/reviews/` was never slow. My sentence about 4,516 reviews was a plausible story about a number I knew, attached to a symptom I had not investigated.

The S056 fix to the unbounded walk was a real defect and is not withdrawn. It simply was not this one, and I said it was.

## 3. What was actually wrong

**One line.** `settle()` ended with an unbounded `Promise.all` over every incomplete image on the page. Eight lazy images never complete, so it never resolved, and the gate waited for as long as it was left. Two things stranded those eight, and both are now fixed:

1. **The walk scrolled back to the top before attaching the handlers.** Chrome had already decided not to fetch images that were no longer in view.
2. **An image the browser never starts fires neither `load` nor `error`,** so waiting on it is waiting on nothing at all.

The eight, named, since they are a fact about the page rather than about the gate: five `proof-card` member portraits, `grid-courses.webp`, the `warm-room__portrait`, and the footer logo. All `loading="lazy"`, all `naturalWidth` 0.

**This was never a `/reviews/` defect.** It would have hung the gate on any page carrying a stranded lazy image. `/reviews/` was simply the first page to have one.

## 4. The two changes

**One, it settles the component rather than the page.** This is Kain's instruction in session, in his words: stop it loading the whole page for a component near the top of it. The assertions already name the exact selectors a sheet cares about, so the gate now scrolls each measured element into view, **leaves it there**, and waits only for the images inside those elements. Being in view is what makes a lazy image load; scrolling away again is what stranded them. A component at the top of a long page now costs one scroll instead of a walk of the whole thing.

`goto` drops from `networkidle` to `domcontentloaded` for the same reason. Waiting for a whole page to go quiet is the thing this was told to stop doing, and on a page whose scripts poll it would never arrive at all.

**Two, the image wait is bounded and names what it gave up on.** It races an eight second deadline and reports every image still incomplete, by filename, with the sentence that a width or height read off one of those is not trustworthy. This is the general fix and it matters more than the first one: an unbounded wait is a gate that can hang rather than fail, and a gate that hangs is worse than one that fails, because from outside it looks identical to one that is working.

Where a sheet names no selectors, the old whole-page walk is still the fallback, with S056's bound intact and the image wait now bounded too.

## 5. The proof that it is not weaker

The obvious risk in measuring less is that the gate stops seeing something. So, the control, run against `BUILD_SHEET__book-note-card.md`, the one sheet carrying real assertions:

| | Previous code | New code |
|---|---|---|
| Passed | 67 | 67 |
| Failed | 0 | 0 |
| Uncomparable | 0 | 0 |
| Waived | 6 | 6 |
| Rows unchecked | 4 | 4 |

**Identical, line for line, including every measured value**: the same 12px radius, the same 160px book cover height, the same `matrix(1.25, 0, 0, 1.25, 0, 0)` cover echo. The book cover measurement is the important one, because the lazy-image problem this instrument was built around is exactly that image, and it still reads correctly.

## 6. What the two reviews sheets actually report, now they can be read

Both open, both complete, and both report **every row unchecked**:

| Sheet | Result |
|---|---|
| `BUILD_SHEET__review-card.md` | 0 passed, 0 failed, 38 rows unchecked |
| `BUILD_SHEET__global-impact-block.md` | 0 passed, 0 failed, 67 rows unchecked |

Neither has a Check column yet, so there is nothing for the gate to assert against. That is the truthful state and not a fault, and it is what your section 4 already says: the Check columns are Chat's under the S261 ruling, and these two are among the five awaiting theirs. **The gate can now open them the moment you write one.** Until then, "opens six" and "measures six" mean different things, and the printout says which is which rather than letting the second be assumed from the first, which is the mistake I made at S056.

The same is true of the article, quote and workbook sheets: they open, they complete, and they report 35, 28 and 27 rows unchecked respectively.

**So the honest headline is: six open, six run to completion, one carries assertions.** The gap is no longer in the instrument.

*No em or en dashes in this file; checked before writing.*
