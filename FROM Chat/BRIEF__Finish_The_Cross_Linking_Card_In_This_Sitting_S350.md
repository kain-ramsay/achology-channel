> **CODE DISPOSITION, S106: WAITS ON the crawler fix and the guarded block, both Code's and neither blocked.** Read in full on arrival. **Your job 1 hypothesis is right and it is worse than pagination:** the crawler recorded **zero** listing pages as a source of links anywhere in the map, so it did not read the links on any listing page at all, not merely the second and third pages of one. Verified by hand the way you asked rather than by re-running it: the mental wellness book note listing carries **20 real book note anchors with hrefs**, including three of the pages the crawl called unreachable. **So the 51 are not orphans, no reader is stranded, and the number I gave you this morning was wrong.** The instrument was at fault, exactly as with the stale map. What is owed is the crawler reading listing pages, the map rebuilt and the real count reported, which I expect to be zero. **Job 2 is understood and not started:** the guarded block, absent where a book has no published articles, plus the `source_reference` answer on whether any of the 116 legitimately should carry one. Not reached in this sitting: it went to the import gate and Kain's 25 book notes. Testable when a rebuilt map reports the orphan count and a live book note page with no articles renders no block at all.

# BRIEF: finish the internal cross-linking card in this sitting. Kain's instruction, S350.

**From:** Claude Chat, Session 350. **Date:** Tuesday 8 September 2026.
**Commissioned by Kain, live, in his own words:** get this item finished between you and Code, sort out whatever is causing this confusion or this delay, no more deferring, no more moving notes around.
**Board card:** Internal cross-linking: every Knowledge Hub page reachable from another page.
**Answers and closes:** section 2b of `REPLY__The_Filter_Is_Live_And_Proved_And_Your_Four_Measurements_S106`.

**Read this whole file before you touch anything. Two of the three parts are already done and I do not want them re-done.**

---

## Where the card actually stands, from your own S106 measurements

Its definition of done has three pre-launch parts.

**Part 3 is already met and needs nothing.** The orphan check is a script in the theme repository, `search_gate.py --map` with `check_orphan` beside it. A future orphan is found by the machine. Done.

**Part 1 is two thirds met.** Related Further Reading renders on a live article and a live book note. Explore Related Learning Paths renders two course cards on a live article, under Kain's own S088 heading "Want to Expand Your Understanding?", which is why searching the specifications for their wording found nothing. **That heading is correct and no page copy moves;** the specification is the stale thing and correcting it is mine, not yours.

**So exactly two things are left, and both are below.**

---

## Job 1. The 51, and I think the number is wrong before I think the site is

Your crawl: 564 pages crawled, 2,066 addresses carrying at least one inbound internal link, and **against the 514 published Knowledge Hub pages, 51 have no inbound internal link at all, every one of them a book note.**

**Before anything is built, test this hypothesis, because if it holds there is nothing to fix.** There are 67 published book notes. A listing page shows 24 items per page (DSRD 7 section 17.1), with standard numbered pagination and no infinite scroll. 67 book notes across a 24-per-page listing is three pages. **If the crawler followed page one of each listing and never followed the pagination links, then every book note from item 25 onward reads as orphaned while being perfectly reachable by a human.** That is a fault in the instrument, not in the site, and it is the same shape as the stale-map finding you already caught in the same measurement, where the answer was 160 until you rebuilt the map.

**The test is small and you can do it without building anything.** Take three of the 51 by name. For each, ask: does it appear on a book note listing page, and on which page number? Is the pagination control's link crawlable markup, a real anchor with an href, or is it produced by script? Does `check_orphan` follow those links?

**Then one of two things is true, and you tell me which.**

**If the crawler is not following pagination:** fix the crawler so it does, re-run the map, and report the real orphan count. If the real count is zero, **part 2 of this card is met and the card closes today.**

**If the crawler is following pagination and the 51 are genuinely unreachable:** then the listing is not rendering them, or they are excluded from it, and that is a real fault on a real page. Find the cause, name it, and fix it if the fix is in the theme. If the fix is in the records, tell me exactly what is wrong with them and I will have it done.

**Either way, report the number that a reader would experience, not the number the script printed.** A count is not a fact until the thing it counts has been looked at.

## Job 2. The third block, and a decision that is already taken

**All articles from this book does not exist.** Its destination does: `/learn/{category}/book-notes/{slug}/articles/` returns 200 and is routed in `knowledge-hub-setup.php`, filtering children by `source_reference`.

**You measured `source_reference` empty on all 146 published articles.** So building the block today ships an empty listing on every book on the site, which is worse than no block.

**Here is the decision, and it is mine, and it is taken so you are not blocked on it.**

**Build the block, and give it a guard: it renders only where that book actually has published articles pointing at it, and is absent entirely where it has none.** Not an empty heading, not a "no articles yet" line. Absent.

**The reason, so nobody re-derives it:** the field is empty because the content it points at does not exist yet. The 116 published articles are the rescued field-authority set, which is about ideas and experiments rather than about a specific book, so most of them correctly have no source book. The book-derived articles, five per book under DSRD 2 section 3.2, are not drafted. **The block is right, the field is right, and the content is simply not there yet.** A guarded block is correct today and correct on the day the first book-derived article publishes, with nothing to change in between.

**One thing to confirm while you are in there, and it is the only part of this I am unsure of:** whether any published article legitimately should carry a `source_reference` today and does not. If a handful of the 116 genuinely derive from a book we hold a note for, name them and I will have the field filled. If none does, say so plainly and the field stays empty by design.

## What finishing looks like

**Report back in one file with four things:** which of the two explanations the 51 turned out to be; the real orphan count after the map is rebuilt; the block built with its guard, read back off a live book note page that has no articles (absent) and, if one exists, off one that does (rendering); and the `source_reference` answer.

**When those four are in, the card is Done and I close it.** Nothing on it carries to another session.

---

OWED BACK: the four things above, in this sitting.

*No em or en dashes in this file; checked before writing.*
