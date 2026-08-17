# RECORD: the Book Note page template, built and gated

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Answers:** `BRIEF__Book_Note_Page_Template_S251.md`, in full.
**Live page for Kain:** https://achologytest.com/learn/psychology/book-notes/mans-search-for-meaning/
**Shipped:** v0.39.1, deployed over SSH, cache purged, commit `4bbff9b`.

**Status in the words Rule 6 allows: changed and verified, with four recorded exceptions and four items waiting on a ruling.** The page is not "done" and I am not calling it that. Kain has not yet ruled it by eye, and DSRD 9 §32.9 item 9 reserves tablet and phone for his judgement in Safari.

---

## 1. What was built

One template serving all 598 book notes.

**New:** `single-book_note.php`, `book-note.css`, `book-note.js`.

**Changed:** `base.css` (the four §20.5 named values), `components.css` (the `.policy-next--image` variant, authored at the panel's one home, not copied into the page), `shared-parts.php` (three glyphs), `knowledge-hub-setup.php` (the two per-book routes), `learn-listing.php` (source-book scope), `group_book_note_fields.json` (six fields), `people-setup.php` (the §11 docblock), `functions.php` (enqueues), `style.css` (version).

**Not built:** the related-courses block. Reason in §5 below. It is the one block of the ten that is absent, and its absence is deliberate and reported rather than quietly filled.

---

## 2. The DSRD 6 gate, chapter by chapter

| # | Chapter | Verdict | Evidence |
|---|---|---|---|
| §1 | Copy standards | **PASS** | Zero words on this page were written by me. Every string resolves from a named source per brief §4, and the closing panel's title, lead and three rows are Kain's words character for character. Zero em dashes and zero en dashes on the rendered page (gate line 12). |
| §2 | Page structure and headings | **PASS** | Exactly one H1. Five H2s, no H3s, no sixth section. The five anchor ids are as locked at DSRD 9 §32.7 and were read off the rendered page: `what-the-book-says`, `where-the-author-comes-from`, `what-it-means-for-society`, `what-you-can-take`, `where-to-take-this-next`. |
| §3 | Metadata and preview data | **PASS**, with the §3.3 canonical carve-out | Title 47 chars, description 148 chars, both produced by running the DSRD 9 §32.8 formulas mechanically, not by writing copy. Canonical absent and correct: the build site is noindex by design, the carve-out amended into §3 row 3 at S245. |
| §4 | Schema markup | **PASS** | One `Review` block, `itemReviewed` a `Book` carrying name, author and ISBN. `reviewRating` is `achology_rating` only, mapped 3/4/5 exactly as `group_book_note_fields.json` instructs. `goodreads_rating` is deliberately absent from schema. No `aggregateRating` and no star markup: nothing asks Google for a result it will not grant. |
| §5 | Search visibility | **PASS** | Title ladder rung 3 won at 47 characters; rungs 1 and 2 measured 74 and 64 and were rejected by the formula, not by me. Breadcrumb resolves five rungs. |
| §6 | AI visibility | **PASS** | The note body is real indexable prose in five named sections, the book is identified by ISBN in schema, and the author, rating and source book are all machine-readable rather than baked into images. |
| §7 | Accessibility | **PASS**, one item for Kain | Every link and button reachable, focus visible via the theme's `:focus-visible` ring. All four external links carry `target="_blank"`, `rel="noopener"`, a visible arrow and a visually hidden "opens in a new tab"; the two Amazon links additionally carry `rel="sponsored"`. The scrollspy carries no ARIA state and every contents link stays reachable without it, per §20.3. The one item Kain rules by eye is the highlight itself, which only exists with the shelf pinned. |
| §8 | Ease of use | **PASS** | Two next steps at the top, two in the shelf, three at the foot. Nothing else, exactly as the S249 removal ruled. |
| §9 | Speed | **PASS** | Hero cover carries `fetchpriority="high"`, shelf cover lazy. One stylesheet and one script, both enqueued only on `is_singular('book_note')`. Gate line 13: nothing failed to load. |
| §10 | Visual consistency | **PASS with two recorded exceptions** | Hairline spacing 48/48 desktop and tablet, 32/32 phone, at every boundary. Gutters 20/32/48. Container 1200. The two exceptions are the H1 size and the full-bleed hero, both below. |
| §11 | Verification on the live page | **PASS** | Every asset loads. Every link resolves except `/learn/authors/viktor-frankl/`, which is §5 item 4 below. |
| §12 | What varies by page type | **PASS** | The 1200px container with a two-column reading zone is DSRD 9 §32.2's approved exception, recorded there. |

---

## 3. The page gate printout

```
PASS      hairline-spacing   desktop boundary 1 (bn-read | bn-sep): 48 above, 48 below
PASS      hairline-spacing   tablet  boundary 1 (bn-read | bn-sep): 48 above, 48 below
PASS      hairline-spacing   mobile  boundary 1 (bn-read | bn-sep): 32 above, 32 below
PASS      hairline-edges     no line at page top or bottom
FAIL      boundary-owner     desktop boundary 1: firstOfB_marginTop 48px, declared by .bn-sep in book-note.css
FAIL      boundary-owner     desktop boundary 1: firstOfB_paddingTop 48px, declared by .bn-sep in book-note.css
FAIL      header-to-content  desktop: 636.8px (want 48)
FAIL      header-to-content  tablet:  966.0px (want 48)
FAIL      header-to-content  mobile: 1096.7px (want 32)
PASS      content-width      page-container: 1200px
FAIL      h1                 42px / 700
PASS      gutters            desktop: 48 / 48   tablet: 32 / 32   mobile: 20 / 20
PASS      meta-title         47 chars: Man's Search for Meaning: Summary and Key Ideas
PASS      meta-description   148 chars
CARVE-OUT canonical          absent, and correct: page is noindex
PASS      dashes             0 em, 0 en
PASS      assets-load        nothing failed
FAIL      links-resolve      /learn/authors/viktor-frankl/ (404)
NOT-BUILT links-resolve      planned in DSRD 1, not built yet: /academy/, /academy/schools/,
                             /certification/, /courses/, /accreditation/,
                             /academy/neuro-linguistic-programming/
------------------------------------------------------------------------------
13 passed, 7 failed, 1 not built yet, 1 carved out
cache-purge  dynamic cache purged before measuring
```

**css_gate:** `book-note.css` PASS, `components.css` PASS, `base.css` PASS.

Three stylesheets the gate fails are pre-existing and were not touched by this change set: `cards.css` (7), `people.css` (3), `testimonials.css` (24). Reported, not swept.

---

## 4. The four recorded exceptions, each with its quoted authority

**1. H1 at 42px, where DSRD 7 §3 sets 32px.** DSRD 9 §32.3's element table: "H1 | Como Hero Heading 42px/700, line-height 1.15 | white". The page-specific spec is the later and more specific instruction, and it is what Kain approved by eye.

**2. Header-to-content, where DSRD 9 §26 wants 48px.** DSRD 9 §32.3 opens: "Full bleed." The hero starts immediately beneath the header by design and the breadcrumb takes `--sp-lg` inside it. §26 assumes a page whose first block sits in the container.

**3. Boundary-owner, twice.** The spacing itself passes at all three widths; what the gate objects to is that `.bn-sep` is not a class DSRD 8 names. See §5 item 1: this is a registration gap, not a spacing defect.

**4. The canonical.** Already carved out at DSRD 6 §3 row 3, S245.

---

## 5. Four things waiting on a ruling from you

**1. `.bn-sep` needs registering, or a registered carrier needs naming.**
DSRD 7 §4.3 is explicit that a page-level separator is carried by a block: "The element carrying the hairline owns the full measurement. If it carries `border-bottom`, its `padding-bottom` is the space above the line and its `margin-bottom` is the space below; if `border-top`, the mirror." The page gate's check 4, ruled by you at S227, fails any boundary spacing "declared outside a DSRD 8 component". Those two rules cannot both be satisfied by any page-level separator on any page. The policy family passes only because DSRD 8 §12.4 happens to name its classes. Either `.bn-sep` gets a DSRD 8 entry, or check 4 gets an exception for the §4.3 carrier. Not mine to choose.

**2. The related-courses block cannot be built.**
DSRD 8 §7's card carries a school line, student count, teaching hours, average rating, price and two CTAs. No course page exists (Code confirmed this at S243, which is why `primary_recommended_course` is empty on all 620 master rows), and the brief closes the only workaround: "All course card facts and prices | DSRD 5 and DSRD 4, read at build. Never typed from the reference page, which carries sample data." So the block waits, and its hairline waits with it.
Worth knowing while you rule: `single-article.php` took the other route at S044 and now ships two hardcoded sample courses with invented prices, under a comment saying they "render until course pages exist to query". That is a live page showing made-up money. I have not touched it, because it is another page, but it should not stay that way.

**3. The Achology rating ticks.**
The approved page renders three orange ticks beside "Essential Reading", the top of the three-step scale, and that is the only rating it shows. Whether "Recommended" shows one tick or three is not proved by anything, and DSRD 9 §32.9 item 1 specifies only the words. Built as rank on the scale, which reproduces the approved page exactly, and flagged rather than presented as settled. Related: the `Check` glyph is not in the DSRD 7 §5.2 registry, and the approved page's own CSS says "registration owed DSRD 7 5.2 (S250)". Both need one line.

**4. `/learn/authors/{slug}/` is not in DSRD 1's planned-URL table.**
The hero's author link goes there per brief §4, and the gate reports it as a broken link rather than a planned one. Either DSRD 1 gains the pattern, in which case the gate reads it as NOT-BUILT and the page passes, or the link waits for the Author Hub. The breadcrumb variant `.breadcrumb--on-dark` is in the same position: the approved page's own CSS calls it "a hero variant pending DSRD 7 registration (S250)".

---

## 6. Six places the documents and the approved page disagree

Reported, not chosen, per the brief's own instruction: "Where this brief and that page disagree, the page is correct and this brief is the thing to fix. Tell me, do not choose."

1. **DSRD 9 §32.2 says the note column "measures 880 at desktop".** It measures **792**, on the approved page and on the build alike. The arithmetic is forced: 1200 container, less 48 gutters each side, less the 264px shelf, less the 48px gap. The claim that §27's two-width rule is unbreached rests on a number that cannot exist at this container width.
2. **DSRD 9 §32.5 calls the shelf's buttons "Get this book at Amazon" and "See the related course".** The approved page and DSRD 8 §20.2 both say **"Buy on Amazon"** and **"See related course"**. Built to §20 and the page.
3. **DSRD 9 §32.3's element table omits the Achology rating line entirely**, then §32.9 item 1 adds it. The approved page puts it between the author line and the standfirst, and the author line's margin-bottom is 8px there, not the table's 24px.
4. **DSRD 8 §20.3 and §13.2 both name `--color-orange-link` as #C64E14.** The token was darkened to **#B8460F** by Kain at S248, after §20 was written. The build reads the token, so it follows the newer decision, and the rendered contrast is better than the documented value.
5. **The approved page uses `<hr>` for its separators.** An `<hr>` is a third element at the boundary, so the page reads as two boundaries with a block between them; the gate measured it exactly that way. Rebuilt as a `border-top` carrier per §4.3. Rendered result identical, structure now the one §4.3 describes.
6. **The brief's page-gate line names the class families as `.shelfp*`, `.pn*`, `.crs*`, `.auth*`, `.hero*` and `.sech*`.** Those are the prototype's names. In the theme the same blocks are `.shelfp*` (correct, §20 names it), `.policy-next*`, `.card--course`, `.author-card`, `.bn-hero*` and `.kh-section__header`. The build reuses the theme's real classes rather than introducing a second set, per DSRD 3 §2.6.

---

## 7. The data contract, and what the import still needs

`group_book_note_fields.json` was the as-built contract and it was missing six of the fifteen fields the page reads. Added: `goodreads_url`, `author_slug`, `author_website_url`, `isbn`, `amazon_url`, `cover_status`. `amazon_genius_link_url` is kept but its instruction now reads "RETIRED, do not fill", because removing a field is a data decision, not a build one.

**Three consequences for the upload CSV, which currently carries 15 columns:**

1. **`post_title` on all 620 master rows is the bare book title**, not the DSRD 9 §32.8 H1 formula. The page's H1 is `post_title`, so every note would publish with the wrong H1. The formula has to run at CSV build.
2. **Six of the fields the page reads are not in the 15-column contract at all**: `author_slug`, `author_website_url`, `goodreads_url`, `isbn`, `amazon_url`, `cover_status`. Four exist in the master and simply need adding to the export; `author_slug` exists as `prod_book_author_slug`; `author_website_url` and `goodreads_url` exist nowhere and are unfilled on all 620 rows.
3. **`achology_author` must be set at import**, not just the ACF `author` field. Verified on the test post: `achology_person_works('benjamin-lockwood')` returns 1 row, the book note, so the profile writing list works. That is brief §5's own acceptance check and it passes.

---

## 8. The test post

One `book_note` exists on the build site, seeded to render and gate the template before the import: post 10901, slug `mans-search-for-meaning`. Its field values are real, read from `Book_Note_Master.xlsx` this session. Its body is the approved page's own copy, because `post_content` is empty on all 620 master rows and I draft none. **It should be deleted at import time** so it does not collide with the real row.

---

## 9. What Kain still has to rule by eye

Desktop is rendered and in front of him. DSRD 9 §32.9 item 9 reserves tablet and phone for him in Safari, and item 8 reserves the scrollspy highlight, which only exists with the shelf pinned beside the text. I have verified all three tiers behave to §20.4 (single column and static shelf below 1024, 28px gap, shelf above the note, no horizontal scroll at 375px), but behaving and looking right are different questions and the second one is his.

---

## 10. Two spacing defects Kain caught on the rendered page, S050 (v0.39.3)

He looked at the built page and said the spacing around the breadcrumb was broken and that there was no space under the closing panel. Both were real, both were against written spec, and both are now corrected and re-measured. Recording them because of what they say about the gate rather than because they were hard to fix.

**1. The gap under the breadcrumb measured 96px. It should be 48.**
The shared `.policy-breadcrumb` carries `margin-bottom: 48px`, and DSRD 9 §32.3's element table separately gives the hero grid "Grid padding-top | `--sp-2xl` 48px". Two owners supplying one space, which is precisely what DSRD 7 §4.3's first sentence forbids: "One owner supplies the space; every block touching it supplies zero." The grid is the owner §32.3 names, so the breadcrumb now contributes nothing.

**2. The closing panel and the rainbow stripe were touching at 0px.**
On every book note. DSRD 7 §4.3 ruling 5: "The 48px spacing still applies at those edges: the first block sits 48 below the header, the last block sits 48 above the footer." I had read that ruling as being about where hairlines are and are not drawn. It is not: it sets the spacing at both page edges whether a line is drawn there or not. 48 at desktop and tablet, 32 on phone.

**Measured after the fix**, at 1440px and 375px: breadcrumb to cover 48 and 48; reading zone to hairline 48 and 32; hairline to panel 48 and 32; panel to footer 48 and 32; no horizontal scroll. `css_gate book-note.css` PASS. The page gate's totals are unchanged at 13 passed, 7 failed, because none of the seven was a spacing failure.

**The point worth taking.** `page_gate` passed hairline-spacing at all three widths both before and after this fix, because it measures the boundaries where hairlines are drawn and neither of these two is one. A 96px gap under a breadcrumb and a page whose last block touches the footer are both invisible to it. Kain found both by looking. Two suggestions, which are Chat's to weigh, not mine to build: the gate could measure the space below the last block against §4.3 ruling 5, and it could flag any boundary where two elements both contribute space, since that is a defect by §4.3's own first sentence regardless of what the total comes to.

**One thing he raised that I have NOT changed.** He said the spacing looked wrong "both above and beneath" the breadcrumb. Beneath was 96 and is fixed. **Above measures 24px**, which is DSRD 9 §32.3's own value ("Breadcrumb padding-top | `--sp-lg` 24px") and is what the approved page carries. Changing it would depart from both the spec and the page he approved, so it is a design decision rather than a defect fix, and it is his to make rather than mine to assume. Put back to him on the rendered page.

*No em or en dashes in this file; checked before writing.*
