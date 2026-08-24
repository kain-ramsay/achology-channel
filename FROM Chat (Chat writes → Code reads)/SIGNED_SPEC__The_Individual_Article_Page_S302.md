# SIGNED SPEC: the individual article page

**From:** Claude Chat, Session 302. **Date:** 24 August 2026.
**Signed by:** Kain, S302, on rendered pages and rendered options in the side panel. Every ruling below was taken by his eye on real content, never described to him.
**Standing rule 19:** this spec is the entire instruction for this page. Build only to it. Where it does not settle something, stop and ask through the channel; do not fill the gap with judgement.
**Board card:** Knowledge Hub Page Designs, line 1.

---

## 1. What the page is

The page a reader lands on when they open any Knowledge Hub article, at `/learn/{category}/articles/{slug}/`.

**One template serves all six article types.** Book-derived, buyer-intent, field-authority, instructor-attributed, video-derived, and author biography. They differ by two switches only, both keyed off `article_type`, and both are named in this spec. There is no second article template and none is coming.

## 2. The blocks, top to bottom

1. Site-wide header (DSRD 8 §18)
2. Breadcrumb, at the 1200px frame
3. Hero: category pill, H1, meta line
4. Featured image
5. Article body
6. Author signature block
7. Hairline
8. Related Further Reading
9. Source block **(conditional, see §5)**
10. Hairline
11. Explore Related Learning Paths
12. Closing "Where next?" panel
13. Rainbow stripe and site-wide footer (DSRD 8 §19)

**Widths.** Everything sits in the 880px reading column except the breadcrumb, which sits at the 1200px frame. No other width transitions on the page. DSRD 9 §22.2 and §27.

## 3. What was ruled this session, and it is the reason this spec exists

Four rulings, each taken on a render. All four are written into DSRD 9 and are repeated here only so you build without cross-referencing.

**Related Further Reading is three cards.** Three at desktop, two side by side at tablet, **two stacked on a phone**. The phone count steps down to two; it does not stack all three. Ruled against four and six, seen with real titles and excerpts at true lengths. DSRD 9 §22.8.

**Explore Related Learning Paths is two cards.** Two at every width. Ruled against three, on the real signed course card inside the 880px column with DSRD 5 figures. At a third of 880px the course title and the two-button row break up; at half they do not. And most lead tags map fewer than three courses, so a third slot is usually the weakest recommendation on the page. DSRD 9 §22.10.

**The two rows deliberately differ,** three above and two below, judged side by side rather than derived.

**The source block is three cases, and the school variant is cancelled.** See §5.

**The instructor article's close carries its heading, reading "What Could You Do With These Ideas?"** DSRD 9 §22.6.

## 4. The two faults being fixed in the same pass

Both already commissioned in `BRIEF__Kill_The_Fallback_Book_And_Build_The_School_Variant_S302`, amended by `BRIEF__Source_Block_Is_Three_Cases_And_The_School_Variant_Is_Cancelled_S302`.

**Delete the hardcoded fallback book.** `single-article.php` renders Tasha Eurich's *Insight* whenever `source_reference` does not resolve. Every one of the eighteen instructor articles currently shows another author's book as though it were deliberate.

**Do not build the school variant.** Cancelled by Kain at S302.

## 5. The source block, block 9

| The article came from | The block shows |
|---|---|
| A chapter of a book | The book, linking to its book note. DSRD 9 §22.9 anatomy, unchanged |
| A lesson from a course | The course the lesson came from, linking to the course page. Overline reads "From this course" |
| Neither | **Nothing. The block is not rendered at all.** Related Further Reading, then the hairline, then the course row |

Case three covers field-authority, buyer-intent, instructor-attributed, and any author biography with no source book.

**Why nothing rather than a substitute.** The alternative rendered was lifting the lead tag's first course into its own block above the row. The same course then appeared twice within one screen, because block 11 is already filled from the same lead tag by the same rule.

## 6. Everything else, and where it is already ruled

Nothing below is open. Read each from the section named.

| Block | Where it is specified |
|---|---|
| Breadcrumb | DSRD 9 §22.3, at the 1200px frame |
| Hero, pill, H1, meta | §22.4. **The H1 is the 33 step, not 36**: the row read 36px, which is not on the nine-step type scale and is not what the theme renders. Corrected S302 |
| Featured image | §22.5. The composite banner does not exist yet, see §8 |
| Article body | §22.6. H2 24 step, H3 21 step |
| Author signature block | §22.7. The bio is **read from the people registry in the theme**, never written into a page and never carried in an upload file |
| Byline and author link | The byline is the Achology pen name or instructor who wrote the piece, linking to `/about/instructors/{slug}/`. The source author is a different person with a different page |
| Course selection | DSRD 1 §5.7. The page reads its own `lead_tag` field, never the first term returned by `wp_get_object_terms`. No course is ever chosen by hand |
| Where next panel | §22.10a. **Copy approved by Kain at S282 and not reopened**: title `Where next?`, lead `Three places to take this idea next.`, three named rows. Use that copy verbatim |
| Tag pills | Removed entirely, §22.11 D3. They stay removed |

## 7. What is deliberately not on this page

Tag pills. A "More from this book" section, which belongs on the book note page. A standalone section divider; hairlines do that job. All three at §22.11.

## 8. The one thing this spec does not settle

**The featured image.** The image production formula exists in DSRD 7 §12 but no composite banner has ever been produced, so Kain has never seen one on a page. Build the slot to §22.5 at 880 by 420 with a 12px radius and leave the current placeholder in it.

**Do not invent a banner and do not substitute a stock image.** When the first real banners exist they go in front of Kain on this page, and that is a separate sitting.

## 9. What comes back

The rendered live page through TO Chat, with its DSRD 6 record, on **two** of the eighteen instructor articles so Kain sees case three twice, plus one article with a source book so he sees case one. Safari on his Mac, his iPad and his phone.

The page is not signed until he has looked at the real thing.

*No em or en dashes in this file; checked before writing.*
