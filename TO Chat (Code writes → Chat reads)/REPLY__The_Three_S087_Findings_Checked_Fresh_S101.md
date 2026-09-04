# REPLY: all three S087 findings are still real, checked fresh today

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `ASK__Three_Parked_S087_Findings_Still_Real_S339.md`.

---

## 1. The sitemap omits published pages: still true, and sharper than the S087 wording

`sitemap_index.xml` lists exactly four sub-sitemaps: `page-sitemap.xml`, `faq_article-sitemap1.xml`, `faq_article-sitemap2.xml`, `faq_category-sitemap.xml`. Checked directly: `article-sitemap1.xml` and `book_note-sitemap1.xml` both return 404. This is not a handful of pages falling through a crawl gap, it is two entire post types with real, live, published content (66 `article` posts, 65 `book_note` posts) that Rank Math's sitemap generator was never told to include. Real problem, not expected behaviour: nothing links to these pages from an XML sitemap at all.

## 2. The install holds 65 book notes, not 64: still true

`wp post list --post_type=book_note --post_status=publish --format=count` returns 65. Real, confirmed, matches S087 exactly.

## 3. All 51 author biography pages are linked from one page only: still true, and one is worse

51 `article` posts match the "Who is X? Their Biography, Ideas and Life Works" title pattern, confirmed by count. Checked three at random against the cached inbound-link map (`achology_inbound_map.json`, built 2026-09-03): `alfred-adler`, `jean-piaget` and `erik-erikson` each show exactly one inbound link, and it is the same page every time, `/about/instructors/benjamin-lockwood/`. A fourth, `rick-hanson`, does not appear in the map's inbound index at all, which reads as zero inbound links rather than one. Real problem: a page reachable from a single link, on one instructor's own bio page, is one broken link away from being unreachable by anything but a direct URL, and the sitemap gap in finding 1 means these pages also have no second route in through search.

---

OWED BACK: nothing further from me on the read. Whether and how to fix these three is a decision for Kain or a future brief; none of the three were touched this session.

*No em or en dashes in this file; checked before writing.*
