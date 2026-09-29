**Needs from Chat:** three things. (1) Read the score finding: every article, book note and quote page is held under 95 by the same two page-type tests, so "fix only the failing tests" has nothing to fix on 458 of them, and 171 help answers lose points on two keyword placements. (2) Rule on the help-answer importer: 32 of this brief's pieces, and items 9 and 10, cannot land because no import route exists for help answers. (3) Take the stage 5 refusals on the 21 new pieces back to Cowork and the gate standards.

# REPORT: the S389 Cowork push, read back and re-scored

**From:** Claude Code, S139 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Push_The_Cowork_Fixes_To_The_Live_Site_After_The_Courses_Page_S389` (the version with items 1 to 10).
**Tools:** `article_body_update.py` (the only route that writes a body; draft or published status untouched), its `--with-seo` path for named page fields, the publish gate's rendered read-back, and `score_tests`' own reader plus Rank Math's analyser results for points per test. Rank Math's "Recalculate Scores" was pressed by Kain, not driven by me.

## What was pushed

**Method, so the count can be trusted rather than assumed.** Every live Knowledge Hub page (972 posts) was dumped from the install, and every record in Content Records was converted by the tool's own rules and compared with its live page, word by word. A page was pushed only where its words differed from its record (the fixes), or where a Cowork report names a page field that differs. Markup-only differences (28 help answers carry `<p>` tags from an older import, one book note, one article) were not pushed: no word changes.

**659 pages pushed, 659 of 659 now match their records** (re-dumped and re-compared after the push: 0 behind).

| Type | Pushed | Brief's count |
|---|---|---|
| Field authority articles | 114 | |
| Instructor articles | 58 | |
| Author biographies | 51 | 51 (item 8) |
| Book notes | 42 | |
| Articles and book notes together | 265 | 243 (item 6); the extra 22 are older record fixes never pushed, found by the word compare |
| Help answers | 201 | 168 (item 6) + 13 (item 2) + 19 with SEO fields |
| Quote pages | 193 | 187 (item 6) + the CQ018 titles (item 3) |

- **Item 3, the 135 CQ018 SEO titles:** every title in Cowork's export checked against its record before the push: 133 match exactly. **Two records carry an unescaped "|" inside the table cell** (`why-we-cant-occupy-two-spaces-at-the-same-time`, `until-problems-have-owners-they-never-go-away`), so the record reader cuts the title at the pipe. Both were set from the export's full title and read back: "We Can't Occupy Two Spaces at the Same Time | Kain Ramsay", "Problems Have Owners, or They Never Go Away | Kain Ramsay". **For Cowork:** escape the pipe in those two records.
- **Page fields:** pushed only where a report names them (19 help answers' SEO title and description; quote page excerpts and descriptions where the quote tables name them; the CQ018 titles). Not pushed: 36 book note excerpts and 7 book note SEO titles that differ from their records but that no S388 or S389 report names. **The 9 book note SEO titles** read "... Summary and Key Ideas \| Achology" in the record: the same escaped-pipe reading fault, so the live titles end "Summary and Key Ideas " with a trailing space and no brand. Named here rather than written, because the right value is a reading of the record's escape, and the importer should be fixed to read it (factory, next session) rather than the titles patched by hand.
- **Item 4, mothers-who-cant-love:** pushed, read back clean.
- **Item 8, the 51 biographies** (and the twelve S354 records inside them): all 51 pushed; `demand_evidence` is a record field with no place on the install, so the push is the body.
- **what-is-achology:** not pushed, as the brief says.
- **Read-back:** 15 pages across every type through the publish gate's rendered check, all clean (mothers-who-cant-love, the-road-less-travelled, abraham-maslow, malcolm-gladwell, maslows-hierarchy-of-needs, the-origin-of-cognitive-therapy, ai-conversations-get-worse, empathy-in-counselling, achology-code-ethics, where-should-i-start-with-achology, valts-achology, the two pipe-title quote pages, helping-people-help-themselves, why-self-pity-is-powerless).

**Two process facts, stated because they are true.** (a) My first three batches ran side by side and shared the tool's one remote temporary file, so about half their pages were skipped; no page received another page's text, because each staged row carries its own post ID with its body, and the re-compare caught every skip, which was then pushed. Batches run one at a time from then on. (b) Four quote pages were refused by the SSH connection as too long to stage as a command argument; they were staged through standard input instead, with the tool's own conversion and its own update code, and two titles were set the same way. Both helpers ran from my scratchpad, wrote only `post_content`, the two Rank Math fields and the excerpt, and changed no status.

## Not pushed, and why

- **Item 1 (7 CBT help answers), item 5 (4 life coaching answers), item 7's 7 NLP help answers, item 9's nlp-certification-free, item 10's 16 life coaching answers:** none of these is on the install, and **there is no import route for help answers**: no importer creates a `faq_article`. 32 help answer records sit in Content Records with nowhere to go. Building one is factory work on the pipeline's stage 5 and 6 (the field-authority importer's shape, draft hardcoded, the help-answer converter this tool already carries, the category term, the hero picture). **Chat's decision:** commission it, and I build it next factory session.
- **Item 7, the 14 question articles:** the importer's stage 5 checks refuse all of them (`import_field_authority_articles.py --type hub-question-article`, plan only): 19 of the folder's 20 records have no featured image on disk (the brief says import without; the importer's check 3 refuses, and dropping it is a gate change I have not made unasked), **19 carry `source_type: demand-question`, which is not one of the ACF field's choices on the install** (a theme field, so a theme queue item or a record change), 4 carry process text in the body, 1 has an H1 in the body, 1 lacks an internal link, 1 fails body shape. Per the pipeline, the batch waits on the records or the field. The stray empty `neuro-linguistic-programming-vs-natural-language-processing.md` is the 20th file; not deleted this session (outside this change set's files).
- **Item 6a, CQ018-023-2's address change:** refused at the publishing wall. `publish_gate.py --clear` on the live page refuses on nine checks that any quote page update can break (the first four named: dsrd6-record, icon-registry, image-budget, image-lazy-below-the-fold). These are the quote page template's, not this record's. No page links to the old address (searched on the install). It waits on the quote template's clearance; nothing was worked around.
- **Item 9, the three biography tag fixes and the accent check:** `kh_tag_order` is a record field the body tool does not write; landing it needs the biography importer's term path. The `content_gate.py` accent change and the free-tier sweep were not started this session.
- **Item 10's Disclaimers check before Q20:** not started (it rides with the importer).

## The scores

Kain recalculated every score in Rank Math; I read the stored score of all 659 pushed pages from the install, and for the 629 under 95 I read each Rank Math test's points from the analyser in the editor (no save, the no-write guard on). The new rows are in my score table (`achology_rank_math_scores.tsv`: 287 replaced, 372 added). Against the previous table, 120 of the 287 moved: 77 up, 43 down.

| Type | Pages | Mean now | S131 mean | 95 or over | 90 to 94 | Under 90 |
|---|---|---|---|---|---|---|
| Articles (all three article records) | 223 | 88.9 | 88.8 | 0 | 12 | 211 |
| Book notes | 42 | 88.0 | 87.9 | 0 | 0 | 42 |
| Help answers | 201 | 88.2 | 88.4 | 30 | 14 | 157 |
| Quote pages | 193 | 89.3 | 88.5 | 0 | 117 | 76 |

**What holds the 629 pages under 95, counted from the analyser's own points:**

- **Every article, book note and quote page (458) is short on the same two tests:** `contentHasAssets` (the four-images-or-videos test; an article earns 1 of 6 with its one picture) and `lengthContent` (the 2,500-word test; 4 of 8 at these lengths). Both are the page-type shortfall the pipeline already accepts (section 5, items 6 and 8: "Where a page type carries fewer than four, the length and media tests are accepted as partial"). With both partial, the ceiling for these pages is below 95: an article that earns every other point scores 89, which is exactly where 214 of them sit. So **there are no failing tests to fix on 405 of these 458**; the rest carry one extra: `keywordInImageAlt` on 7 articles, `titleStartWithKeyword` on 1 article and 5 quote pages, `linksHasInternal` on 1 article, `keywordInSubheadings` on 53 quote pages (the three fixed headings carry no keyword: the same 53 that the heading ruling in the S390 ask covers, as far as I can tell; the table names them).
- **Help answers (171 under 95):** `keywordInSubheadings` 159, `keywordInPermalink` 148 (the address was set before the keyword was re-chosen), `contentHasShortParagraphs` 55 (a paragraph over 120 words), `keywordIn10Percent` 51, `keywordInContent` 51, `keywordInMetaDescription` 12, `titleStartWithKeyword` 2.

**The question this puts to Chat:** the 95 target cannot be reached on articles, book notes and quote pages without more pictures or more words, both of which the standard declines on purpose. Either the target is read against each type's honest ceiling (DSRD 6 section 5 item 11 owns that), or those two tests join the refused list. Until that is ruled, "fix the failing tests" applies to the 171 help answers and the 67 other pages with an extra short test, all named in the table below.

## Per-page table

Every page pushed, with its stored score, its type's S131 mean, and every test short of full marks with its points. "none under 95" marks a page at 95 or over.

