# REPORT: zero orphans. The crawler was the fault, and it was worse than pagination.

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** job 1 of `BRIEF__Finish_The_Cross_Linking_Card_In_This_Sitting_S350.md`, whole.
**Board card:** Internal cross-linking: every Knowledge Hub page reachable from another page.

---

## 1. The answer

**Zero orphans. Every one of the 514 published Knowledge Hub pages carries at least one inbound internal link.**

**So it was the first of your two explanations**, and part 2 of that card is met.

## 2. It was your hypothesis, and it was worse than you guessed

You reasoned that the crawler might follow page one of each listing and miss the pagination, leaving every book note from item 25 onward reading as orphaned.

**It never read a listing page at all.** Not page two and three of one: none of them, ever.

**The cause.** `crawl_set()` builds its list from the sitemap plus every published **post**. A listing page is not a post: `/learn/{category}/book-notes/` is a rewrite rule, so it could not enter the set from either source. The tell was already sitting in the map I had: **zero listing pages appeared as a source of links anywhere in it.**

**Checked by hand before the fix, as your file asked and as I should have done before reporting 51.** The mental wellness book note listing carries **twenty real anchors with hrefs**, three of them to pages the map called unreachable. No reader was ever stranded.

## 3. What is built, and it is wider than the fault on purpose

Kain instructed it in the sitting. Theme commit `55995fe`.

**The crawl now follows what it finds.** Any same-site page discovered in a link is queued and read, assets and admin excluded, hard ceiling of 5000.

**Adding listing pages to the seed list would have fixed these 51 and left the class untouched.** The next page type reachable only through a route nobody enumerated would fail the same way, silently, and read as an orphan. Item 7's subject is what a search engine finds by following links, so the crawl follows links, and pagination, hubs and tag pages arrive free because they are linked.

**The number that shows the size of the blind spot:**

| | |
|---|---|
| pages seeded, from the sitemap and the post list | 564 |
| **pages discovered by following links** | **971** |
| pages actually read | 622 |

**971.** Before this change that figure would have been 0, which is the whole fault in one number, and the map now records `pages_seeded` and `pages_discovered` separately so it can never hide again.

**The floor, so the zero is not the only thing you have:** the least-linked published page carries one inbound link, and the next four carry two. Nothing is clinging on by an accident of the crawl.

## 4. One thing the crawl surfaced that is not mine to judge

**618 addresses linked from the site's own navigation and footer return 404**, and because they are in site-wide chrome, all 622 crawled pages carry them. Checked five by hand rather than trusting the count: `/pricing/`, `/courses/`, `/academy/schools/`, `/academy/personal-growth/` and `/tcf/purposes/` all return 404.

**I am not calling it a defect.** Most of it is almost certainly the academy section not being built yet, which is expected on a half-finished site. But it is worth someone's eye before cutover, because on a live site every one of those is a dead link on every page.

Named, not acted on, and not counted against this card.

## 5. What is left on the card

Job 2 only: the guarded block, absent where a book has no published articles, and the `source_reference` answer on whether any of the 116 legitimately should carry one. Not reached in this sitting.

## 6. The record of my own error, because it went to you as a finding

I reported 51 orphans, every one a book note, from a script's output, without opening a single one of the 51 to see whether a reader could reach it. **A count is not a fact until the thing it counts has been looked at**, which is your own sentence from this brief and it should not have needed writing.

---

OWED BACK: nothing on job 1. Job 2 when the sitting has room.

*No em or en dashes in this file; checked before writing.*
