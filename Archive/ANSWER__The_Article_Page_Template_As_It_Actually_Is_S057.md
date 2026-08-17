> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Used whole as the ground truth for the S272 Article Page design session, which produced two of Kain's rulings now in DSRD 9 section 22. The one open use left, the article page spec's reconciliation section, is carried in the S272 handover under the article page's parked items and resumes when page design resumes. Kain directed at the S273 open that all six S272 files archive. No board cards moved by this file.

> **STAYS IN TO CHAT, S271 (Chat), 13 Aug 2026.** Read at the S271 open, deliberately not consumed: S271 was the DSRD 7 icon and type session, and this answer is the ground truth for the Article Page design work (Knowledge Hub page card 1). It is read whole at the session that works that card, and it closes there. This supersedes the S270 note, which said it is read at the next open whichever comes first; two sessions reading it whole without working the card would be the read-and-parked failure by another route.

# ANSWER: the article page template, block by block, as it actually is

**From:** Claude Code, Session 057. **Date:** 2026-08-12.
**Answers:** `QUESTION__The_Article_Page_Template_As_It_Actually_Is_S268.md`.
**Nothing was changed.** This is a read of the template file, the stylesheet, the live rendered page and the database, all made this session at theme v0.60.17.

**How the page was read.** A plain fetch from outside the host returns HTTP 202 and a SiteGround captcha interstitial, not the page. Every fact below comes from a fetch made from inside the host (`https://127.0.0.1` with the Host header set), which is the route `page_gate.py` already uses, plus `wp eval` against the live database. Worth knowing on your side too: an external fetch of any page on this site measures the captcha, not the page.

---

## 1. Does it render, and where

**Address.** `https://achologytest.com/learn/psychology/articles/the-power-of-self-awareness-in-personal-growth-test/`

That is the only `article` post in the database at any status: post 439, published, titled "The Power of Self-Awareness in Personal Growth (TEST)". The title carries the word TEST and it is public.

**Does it resolve today.** Yes, tested rather than assumed: HTTP 200, 85,736 bytes, at the deployed theme version 0.60.17 (confirmed active by `wp theme list`).

**Template and stylesheet.** `single-article.php` renders it. `knowledge-hub.css` styles it, and it is enqueued **conditionally**, at `functions.php:312`:

`is_singular( array( 'article', 'book_note', 'quote', 'workbook' ) ) || is_tax( 'kh_category' ) || get_query_var( 'ach_listing' ) || is_page( 'cards' )`

Ahead of it in the chain, all global: `fonts.css`, `base.css`, `components.css`, `cards.css`, `style.css`, `header.css`, `footer.css`, `policies.css`, `help.css`, `people.css`.

**Readiness record.** One exists, at `DSRD 6 Records (pages with no design folder yet)/Single Article/DSRD6_RECORD.md`, created by the S264 backfill on 2026-08-12. **Its verdict is not ready and every line is open:** all eleven chapters read `not run`, the `Theme version at last update` line still reads the template's `{0.00.0}` placeholder, and the §12 exemptions line reads `none`. No chapter of DSRD 6 has ever been run against this page, by machine or by anyone else.

---

## 2. The eleven blocks

| # | Block | Emitted? | Real data or placeholder |
|---|---|---|---|
| 1 | Sticky header | yes | real |
| 2 | Breadcrumb | yes | real: Home > Learn > Psychology > Articles > title |
| 3 | Hero (pill, title, meta) | yes | real: pill "Psychology", H1, "12 July 2026 · Kain Ramsay · 2 min read" |
| 4 | Featured image | yes | real: an uploaded PNG, `srcset` present, not the placeholder branch |
| 5 | Article body | yes | real |
| 6 | Author signature block | yes | real, from the people registry |
| 7 | Hairline | yes | n/a |
| 8 | Related Further Reading | yes | **live query, but on its fallback branch: one card, not four** |
| 9 | Source Book Callout | yes | **declared placeholder, and it is hardcoded invented book data** |
| 10 | Hairline | yes | n/a |
| 11 | Explore Related Learning Paths | **no. The block does not render at all** | n/a |
| 12 | Rainbow stripe + footer | yes | real |

**The two things to take from that table.** Block 11 is absent from the live page entirely, heading and all. And because the hairline at item 10 sits *outside* that block's `if`, the page currently ends on a hairline with nothing beneath it before the footer.

---

## 3. The two card rows

### Related Further Reading

**Class families emitted:** `.kh-compact-row` wrapping `a.card.card--mini.card--clickable`, each holding `.card__thumbnail` (with `--article` or `--book-note`), `.card__content`, `.card__type-label`, `.card__title`, `.card__watermark`.

**It is a live query, in two stages,** and this matters because the second stage is what is actually running:

1. **Stage one, tags.** `get_posts` over post types `article` and `book_note`, status publish, 4 posts, excluding this one, `tax_query` on `kh_tag` against this article's own tag term IDs. Ordering: WordPress default, date descending.
2. **Stage two, the fallback.** Where stage one returns nothing *and* a primary category exists, the same query re-runs against `kh_category` on the article's primary term.
3. **Where both return nothing,** four hardcoded prototype cards render, declared as placeholders in the code.

**What runs on the live page: stage one returns 0.** Article 439 carries tags `grow-self-awareness` and `unlock-personal-growth`; the only published book note carries `build-mental-resilience`, `find-purpose-and-direction`, `understand-your-mind`, and there is no other published article. So the category fallback fires, finds the one Psychology book note, and **exactly one card renders.** The placeholder branch is not what you are looking at on the live page.

**Does it still scroll horizontally?** Yes, it is still a scroll row and has not become a grid. `knowledge-hub.css:199` sets `display: flex; overflow-x: auto; scroll-snap-type: x mandatory`, with the cards at `min-width: 300px; max-width: 340px; flex-shrink: 0`. The visible consequence today is a horizontal scroll row containing one card.

### Explore Related Learning Paths

**Class families:** `.kh-section` with `.kh-section__header` and `.kh-course-grid`, the cards rendered by `achology_course_card()` as `.card--course`.

**It is a live query and it resolves to nothing.** `achology_courses_for_content( get_the_ID(), 2 )` reads the page's authored tag order, which is the `kh_tag_order` post meta field and then the `lead_tag` field, per DSRD 1 §5.7. **Article 439 carries neither field.** `achology_content_tag_order(439)` returns an empty array on the live site, confirmed by `wp eval`. The function deliberately does not fall back to the WordPress tag list, and the code says why: `term_order` is zero on every imported row so the read would come back alphabetical, and roughly six pages in seven would show a confidently wrong course. No courses resolve, the whole `<section>` sits inside `if ( $ach_courses )`, and it is skipped.

**It is not a placeholder any more.** The invented course data Kain stopped at S252 is gone; the block reads `courses-setup.php` or renders nothing. Nothing is fabricated here.

**One stale value.** The template asks for **2** courses. DSRD 9 §22.10 as corrected at S268 says "3 at desktop, 2 side by side at tablet, 2 stacked on a phone", superseding the two-card row from DSRD 1 §3.4. The template predates that correction and has not been moved onto it.

---

## 4. What data fills each slot

| Slot | Source | When empty |
|---|---|---|
| Category pill, breadcrumb category, `articleSection` | first `kh_category` term (the one the permalink uses) | pill and two breadcrumb rungs omitted; trail becomes Home > Learn > title |
| H1, breadcrumb current, schema headline | `the_title()` | n/a |
| Date | `get_the_date('j F Y')` | n/a |
| Author, meta line | ACF field `author` (a slug) resolved through `achology_person()`, the people registry | the author segment and its separator are omitted |
| Author link target | `achology_person_url($slug)`, resolving to `/about/instructors/{slug}/` | n/a |
| Reading time | word count of `get_the_content()` at 200 wpm, minimum 1 | never empty |
| Featured image | `has_post_thumbnail()`, rendered at size `large` | a declared placeholder div, `kh-article__banner--placeholder`, labelled "Featured image" |
| Author avatar and bio line | the people registry, via `achology_author_card($slug)` | the whole signature block is omitted where no author slug is set |
| Related row | the two-stage query in §3 above | four hardcoded prototype cards |
| Source book cover, title, author, description | ACF `source_reference` pointing at a `book_note`, then that post's title, its `source_book_author` field, its excerpt, and its `book_cover_image` field at size `medium` | **a hardcoded placeholder book: "Insight: The Power of Self-Awareness in a Self-Deluded World" by Tasha Eurich, with an invented description, linking to `href="#"`** |
| Course cards | `achology_courses_for_content()` reading `kh_tag_order` then `lead_tag` | the entire section is omitted |

**On the live page right now:** `source_reference` is empty, so the placeholder book is what a visitor sees, attached to a dead link. Its cover panel renders empty because the placeholder branch sets no cover.

---

## 5. Everything ruled since July, and whether this template carries it

**Block heading standard (S263).** Carried, and it passes. The two supporting lines are "Click on the cards below for more reading on this important topic." (12 words, one sentence) and "Find practical learning opportunities that build on the ideas explored in this article." (13 words, one sentence), both inside DSRD 7 §3.3 rule 2's 12-to-25 range and rule 3's one-or-two-sentence limit. My own S054 sweep report records the article page as passing the checker with zero failures. **Neither line was among the seven rewrites**, so nothing shipped this week reached this template.

**Icon registry.** Partly. Three glyphs come through `achology_icon()`: `home`, `notebook-pen`, `book-marked`. **Four are emitted inline, and all four are already registered**, so these are duplicates rather than gaps:

| Glyph | Registered? | Does the inline drawing match the registered one? |
|---|---|---|
| chevron-right (breadcrumb separator) | yes | **yes**, identical path. A pure duplicate |
| compass (Related Further Reading header) | yes | **no.** Inline draws the older straight-edged `<polygon>`; the registry holds the newer rounded `<path>` |
| graduation-cap (Learning Paths header) | yes | **no.** Inline is the older Lucide drawing |
| newspaper (article card watermark) | yes | **no**, and this one is deliberate and documented in the code as one of the ten S054 drift pairs left for Kain's eye |

So two undocumented drift pairs on this page, compass and graduation-cap, plus one duplicate. I am naming them and leaving them, as your file asks.

**"An article shows its category, its school and its courses."** Two of three. Category is shown twice, in the pill and the breadcrumb. Courses have their block, currently empty for the reason in §3. **School is shown nowhere on the page.** The thing that would carry it is the §22.9 school variant ruled at S268, and that variant is not built.

**Author attribution key.** Carried correctly and fully. The ACF `author` field holds a slug, `achology_person()` resolves it through the people registry, and no WordPress user is involved anywhere: not in the byline, not in the signature block, not in the Article schema. Verified live: post meta `author = kain-ramsay`, byline linking to `/about/instructors/kain-ramsay/`. The template also switches Rank Math's competing Article block off for this post type so the registry-authored block is the only one on the page.

**In-body link ceiling and first-mention rule.** They apply. DSRD 1 §6.4 rule 7 is written as "the working ceiling for a support answer or a short article" and is not scoped to help articles. But **this is a content rule about the writing, and the template neither enforces it nor can.** As a fact about the one live article rather than about the template: its body carries **zero** in-body links, so the ceiling is not breached and the first-mention standard is simply unmet on that article.

**External links.** None in the article's own zone. The page carries 15 external anchors and every one is header or footer chrome (the Circle community, the social accounts, the ICO registration, the cookie database). The four requirements DSRD 7 sets for external links are not engaged by anything this template emits.

---

## 6. The two straight questions

### Was this page ever approved by Kain's eye?

**I cannot tell you it was, and I will not reason it out.** What the record actually holds is one thing: the template's docblock and the version-control history both carry a specific instruction from Kain dated 2026-07-12, that the column is left-aligned to the page-container edge so content lines up with the header and footer logos. That proves he looked at the page at least once. It is not a sign-off.

Against it: there is no approval record for this page anywhere I can read, no prototype file in a design folder for it, and its own DSRD 6 record has every one of Kain's lines reading `not run`. Under the S258 standard the page is unsigned.

### What do I already know is wrong or unfinished

My own list, in my order.

1. **The source book callout ships invented book data on a live public page, attached to a dead link.** A title, an author and a description of a book that has nothing to do with the article, plus `href="#"`. It is honestly declared as a placeholder in the code, which changes nothing about what a visitor sees. This is the same failure class as the invented course data Kain stopped at S252, still live, on the same page.
2. **The source block has one variant and S268 ruled two.** No school variant exists, so a school authority article would have no link to its own school anywhere on the page. This is the largest gap between the ruled spec and the build.
3. **The course block asks for two cards. The corrected spec says three at desktop.**
4. **The second hairline renders when the block below it does not,** leaving the page ending on a rule with nothing under it.
5. **Four glyphs bypass the icon registry**, two of them drawing a different mark from the registered one, per the table above.
6. **The related row degrades silently and has no floor.** The category fallback returns whatever it finds, so a scroll row built for four cards currently holds one, with no minimum and no "nothing to show" state between a full row and a nearly empty one.
7. **The page's DSRD 6 record is entirely open.** Eleven chapters `not run`, theme version placeholder never filled. Nothing about this page has been gated.
8. **Not measured, so not claimed:** whether the rendered banner matches §22.5's 880 by 420 at `object-fit: cover`. The image is real and loads; I have not put a ruler on it and will not imply I have.
9. **The one published article is a test post**, titled with "(TEST)" and public on a noindex site. Whatever happens to the template, that post is not launch content.

*No em or en dashes in this file; checked before writing.*
