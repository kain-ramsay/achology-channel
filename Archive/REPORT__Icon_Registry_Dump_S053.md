# REPORT: the icon registry as it actually stands in the theme

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.58.0.
**Answers:** `REQUEST__Complete_Work_Status_And_Icon_Registry_S261.md` part 2.
**Method:** every line below found by search across every PHP and JS file in the theme this turn, previews excluded. Nothing here is from memory.

Kain's instinct was right, and the numbers are worse than the four examples suggested.

## The headline

**37 glyphs are registered. 139 SVGs render outside the registry.** The registry covers roughly a fifth of the icons on this site. `globe` was not an exception; it was the one that happened to get caught.

## 1. The 37 registered glyphs, and who calls each

| Glyph | Called from |
|---|---|
| arrow-right | footer.php, knowledge-hub-parts.php, reviews-setup.php, shared-parts.php |
| award | shared-parts.php |
| book-open | shared-parts.php, single-book_note.php |
| bookshelf | single-book_note.php |
| calendar-days | template-policy.php |
| check | page-reviews.php, single-book_note.php |
| chevron-down | page-reviews.php |
| chevron-left | knowledge-hub-parts.php |
| chevron-right | knowledge-hub-parts.php, shared-parts.php |
| circle-check | shared-parts.php |
| **compass** | **NO CALLER** |
| download | knowledge-hub-parts.php |
| external-link | single-book_note.php |
| file-pen | knowledge-hub-parts.php, taxonomy-kh_category.php |
| file-text | page-about.php |
| globe | page-reviews.php |
| graduation-cap | help-parts.php, manifesto.php, shared-parts.php, single-book_note.php |
| **home** | **NO CALLER** |
| library | code-of-ethics.php, manifesto.php |
| library-big | shared-parts.php |
| lock | help-parts.php, manifesto.php, shared-parts.php, template-policy.php |
| mail | help-parts.php |
| message-circle-question | help-parts.php |
| monitor-play | code-of-ethics.php |
| newspaper | knowledge-hub-parts.php, taxonomy-kh_category.php, template-policy.php |
| notebook-pen | knowledge-hub-parts.php, taxonomy-kh_category.php |
| pen-line | page-about.php |
| quote | founders-letter.php, knowledge-hub-parts.php, reviews-setup.php, shared-parts.php, single-book_note.php, taxonomy-kh_category.php |
| scale | page-about.php |
| scroll-text | page-about.php |
| search | page-reviews.php |
| **sprout** | **NO CALLER** |
| star | reviews-setup.php |
| tag | shared-parts.php |
| tags | taxonomy-kh_category.php |
| users | page-reviews.php, shared-parts.php |
| x | shared-parts.php |

**Three registered glyphs are called by nothing:** `compass`, `home`, `sprout`. `compass` became unused today when the figure register moved countries to `globe`. The other two have never had a caller I can find.

## 2. The 139 SVGs outside the registry, by file

| File | Inline SVGs |
|---|---|
| page-about.php | 27 |
| header.php | 19 |
| page-testimonials.php | 10 |
| footer.php | 9 |
| single-article.php | 7 |
| founders-letter.php | 7 |
| faq-icons.php | 7 |
| code-of-ethics.php | 7 |
| template-policy.php | 5 |
| manifesto.php | 5 |
| 404.php | 5 |
| single-faq_article.php | 4 |
| courses-setup.php | 4 |
| template-policies-index.php, template-our-people.php, template-author-profile.php, page-reviews.php | 3 each |
| taxonomy-kh_category.php, taxonomy-faq_category.php, single-book_note.php, learn-listing.php, archive-faq_article.php | 2 each |
| rank-math-feed.php | 1 |

**Not all 139 are drift.** Three groups are legitimately outside a glyph registry and should stay there:

- **Breadcrumb chevrons and the home mark**, which repeat across almost every template and carry their own `icon-breadcrumb` class.
- **The footer's social marks**, at `viewBox="0 0 16 16"`, which are brand logos rather than interface glyphs.
- **Artwork**, such as `page-about.php` line 220's 780x200 signature drawing.

**The rest is the drift surface.** `page-about.php` alone carries 27, which is how it rendered a globe for months that DSRD 7 §5.2 did not know existed. `header.php` at 19 is the next largest.

## 3. Registered meanings, where a meaning exists

The registry stores drawings, not meanings, so this is assembled from where each glyph is actually used. **Marked CLEAN where one glyph means one thing, CONFLICT where it does not.**

| Glyph | Meaning in use | |
|---|---|---|
| star | the rating value, 4.66 | CLEAN, since the figure register |
| award | the count of ratings given, 175,162 | CLEAN, since the figure register |
| quote | written reviews, and the quote content type | **CONFLICT.** Two meanings: the reviews figure, and a Knowledge Hub quote. Both are "somebody's words", so it may be acceptable; it is a decision, not an accident |
| users | students | CLEAN |
| globe | countries | CLEAN, since the figure register |
| library-big | courses | CLEAN in the register. **Trap:** `library` is a completely different drawing under a near-identical name, and it is what a careless call returns. It cost a defect today |
| library | used on the code of ethics and manifesto for a general "body of work" sense | CLEAN in itself, dangerous only next to `library-big` |
| graduation-cap | courses and study | **CONFLICT with library-big**, which the figure register uses for courses. Two glyphs, one concept |
| bookshelf | the book note closing panel | CLEAN, ruled S255 |
| notebook-pen | the book note content type | CLEAN |
| newspaper | the article content type | CLEAN |
| file-pen | the workbook content type | CLEAN |
| lock | membership and gated content | CLEAN |
| circle-check, check | confirmation | Two glyphs, one concept, worth a look |

**Two real conflicts for you to rule on:** `quote` carrying both written reviews and the quote content type, and `graduation-cap` against `library-big` for courses.

## 4. What I have not done

I have not touched any of the 139. Pulling them into the registry is a sweep across most of the theme's templates and needs a signed sweep brief from Kain, not a decision from me. When you rewrite DSRD 7 §5.2, the useful thing for me is a ruling on **which of the 139 should become registry calls and which are legitimately inline**, and then a brief. Until that exists the count only grows, because every new page hand-writes its own.

*No em or en dashes in this file; checked before writing.*
