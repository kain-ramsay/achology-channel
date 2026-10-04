# Schema build: the JSON-LD the specifications ask for and the theme did not publish

Branch `cloud-feature/schema-build`, from main at `2bc5aeb`. Sources: `cloud-reports/job9-schema-audit.md` (branch `cloud-report/job9-schema-audit`), DSRD 10 §9, DSRD 3 §5.3, §5.4 and §5.7, DSRD 1 §9. DSRD 10 governs where DSRD 3 differs (DSRD 3 says so itself).

## What was built, in one table

All new code is in `schema-parts.php` (required once from `functions.php`). Every builder returns data and reads nothing from WordPress by itself. One function, `achology_schema_print()`, prints each node as its own `<script type="application/ld+json">`, the house style of `single-faq_article.php` and `template-author-profile.php`.

| Page type | Result | Wired into | Commit |
|---|---|---|---|
| Book notes | BreadcrumbList, speakable WebPage | `single-book_note.php` | `0cd4286` |
| Course pages | BreadcrumbList | `template-course.php` | `967a198` |
| Courses directory | BreadcrumbList | `template-courses.php` | `5e8f767` |
| Articles | Article extension: speakable, about, mentions | `single-article.php` | `44c2bc3` |
| Quote pages | Quotation (CreativeWork), BreadcrumbList, speakable WebPage | `single-quote.php` | `8104cf5` |
| Workbook pages | LearningResource + DigitalDocument, BreadcrumbList | **function only** | `e052839` |
| Knowledge Hub listing pages | CollectionPage, BreadcrumbList | `learn-listing.php` | `fe47036` |
| School pages (7) | WebPage, BreadcrumbList | **function only** | `28bd62e` |
| Academy and Schools directories | CollectionPage (with a list of the 7 schools), BreadcrumbList | **function only** | `f5b5da9` |
| Accreditation | WebPage, EducationalOrganization, BreadcrumbList | **function only** | `29679db` |
| Membership | WebPage with two Offers, BreadcrumbList | **function only** | `ce05fa5`, `787b2a5` |
| Webinar pages | WebPage, Event (only when its data is given), BreadcrumbList | **function only** | `bce176c` |
| Rank Math filters | breadcrumb and CollectionPage removal for the wired types | `rank-math-feed.php` | `83f9968` |

"Function only" means no template for that page exists in this theme, so the function and its test are written and no template was created.

## What was not changed

- No existing block was edited or moved. In the seven existing files the build touches, the diff is **107 insertions and 0 deletions**.
- Nothing a visitor sees changed. A script block of type `application/ld+json` is not rendered, and the test compares each wired template's visible HTML against the baseline (below).
- Nothing was deployed, no pull request opened, main untouched.

## Per page type: spec line, what the test proved, what it could not

"The test" is `cloud-reports/schema-build/run.php`, output in `output.txt` (**460 checks, 460 passed, 0 failed**). How it works is in the next section.

### Book notes
- **Spec line.** DSRD 10 §9 Standard 3 and DSRD 1 §9 ("Book note: Home > Learn > [Category] > Book Notes > [Book Title]"); DSRD 3 §5.4 (speakable: Summary section + Key Themes section); job 9 audit rows for book notes. The existing Review block was left as it is.
- **Proved.** One BreadcrumbList with the full trail (Home, Learn, category, Book Notes, book) and addresses; one WebPage carrying a `speakable` with four selectors; all existing blocks printed byte for byte and in order; visible HTML identical; all four selectors match one element each in the rendered stand-in page (headless Chromium).
- **Could not prove.**
  - The spec names "Summary" and "Key Themes". The live note's sections are named differently. I mapped them to the first and fourth headed sections ("What this book is actually saying", "What you can take from the book"). Whether that is what the spec meant: **cannot tell**.
  - Whether Rank Math also prints a WebPage on a book note. If it does, the new WebPage shares an `@id` (`url#webpage`) so the two should merge, but I could not run Rank Math to see.
  - DSRD 3 §5.7 item 2 also lists `affiliateUrl` (Genius Link) on the book note. It is **not built**: no Genius Link address is held anywhere in the theme, and it belongs in the existing Review block, which I was told not to change.

### Course pages
- **Spec line.** DSRD 10 §9 Standard 3, DSRD 1 §9 ("Course page: Home > Academy > [School Name] > [Course Name]").
- **Proved.** BreadcrumbList with Home, Academy, "The School of …", course name, and each address; the existing Course block unchanged.
- **Could not prove / not done.**
  - DSRD 3 §5.7 item 5 lists `courseCode` and `educationalLevel` for the Course block. `achology_schema_course_extra()` returns `courseCode` (the DSRD 5 catalogue number) and is **not wired**, because adding it means editing the existing Course block. `educationalLevel` is not built at all: no document gives a level per course. Which level each course is: **cannot tell**.

### Courses directory
- **Spec line.** DSRD 10 §9 table row "Academy, Schools dir, Courses dir", Standard 3; DSRD 1 §9 ("Courses directory: Home > Courses").
- **Proved.** BreadcrumbList added beside the existing CollectionPage (kept as is).

### Articles
- **Spec line.** DSRD 10 §9 ("Article + speakable"); DSRD 3 §5.3 and §5.7 item 1 ("Extend Rank Math Article with speakable, about (tags), mentions (source book)"); §5.4 (Hook section + Look section).
- **Decision.** The existing Article block in `single-article.php` is not edited. The new block is a second node with the same `@id` carrying only `speakable`, `about` and `mentions`, so anything that merges by `@id` sees one Article. Reason: DSRD 3 itself words the job as an *extension*, and the brief said not to change existing blocks.
- **Proved.** Both nodes present; same `@id`; selectors match (`.kh-article__body .ach-opening` and `.kh-article__body > h2:first-of-type + p`).
- **Could not prove / flagged.**
  - Two Article-typed blocks on one page is arguably against Standard 2 ("one block of each schema type per page"). It is the trade made above, and the alternative (a property on the existing block) is one edit if Kain and Chat prefer it.
  - Hook is read as the unheaded opening paragraph; Look has no section of that name in the current six-section article and is read as the paragraph under the first headed section. Which section the spec meant: **cannot tell**.
  - `about` lists tag names only with no addresses, because DSRD 10 says the tag pages "do not currently resolve".

### Quote pages
- **Spec line.** DSRD 10 §9 ("CreativeWork + quotation"); DSRD 3 §5.3 and §5.7 item 3 (`text`, `creator` Person, `isBasedOn` book note, `speakable`); §5.4; DSRD 1 §9.
- **Proved.** Type is `CreativeWork` + `Quotation`; `text` is the quote; `creator` is a Person; `isBasedOn` is the book note's address when one exists and is **absent** when none does (a course quote); the trail; a speakable WebPage; the two selectors match one element each; visible HTML identical.
- **Could not prove.** The two headings' mapping (Hook/Look interpretation → "What the Quote Might Be Saying" and "What Can We Take Away From It?"): **cannot tell**. Whether Rank Math also prints a WebPage: cannot tell.

### Workbook pages (function only)
- **Spec line.** DSRD 10 §9 ("LearningResource + DigitalDocument", ruled S353); DSRD 3 §5.3 and §5.7 item 4 (`isAccessibleForFree` boolean, `educationalLevel`); DSRD 1 §9.
- **Proved.** One node carrying both types; `isAccessibleForFree` is a real boolean, derived from `is_members_only`; `contentUrl` is given only when the workbook is free; `educationalLevel` is given only when supplied and is absent when not; trail Home, Learn, Category, Workbooks, short name.
- **Could not prove.** There is no workbook template, so it has never run on a real page. Where `educationalLevel` comes from: **cannot tell** (no source field is named).

### Knowledge Hub listing pages
- **Spec line.** DSRD 10 §9 table and decision (c), S219 ("CollectionPage + BreadcrumbList; Rank Math's CollectionPage switched off"); DSRD 1 §9 (per-category and cross-category trails).
- **Proved.** Both routes through `learn-listing.php` (category-scoped and cross-category) print the CollectionPage and the right trail with addresses; the per-book route (function) gives the six-level trail.
- **Could not prove.** The paged URLs (`/page/2/`) use the page's base address, so every page of a listing names the same CollectionPage. Whether Rank Math's graph prints on these rewrite routes at all: **cannot tell**.

### School pages, Academy and Schools directories, Accreditation, Membership, Webinar pages (function only)
- **Spec lines.** DSRD 10 §9 table rows "School pages (7)", "Academy, Schools dir, Courses dir", "Accreditation", "Membership, Pricing", "Webinar pages", all "Theme JSON-LD, flipped at S218"; DSRD 3 §5.7 items 7 to 9; DSRD 1 §9.
- **Proved.**
  - Schools: all seven render WebPage + BreadcrumbList, trail Home > Academy > "The School of …"; an unknown school returns nothing.
  - Directories: CollectionPage listing seven schools; trails Home > Academy and Home > Academy > Schools.
  - Accreditation: the UKRLP number 10099815 as an identifier, SoMAP as the recognising body, on the site's `@id`; no name, logo or profile restated.
  - Membership: two Offers with USD price, availability and the two checkout addresses; $7 for the first 30 days then $34.50 a month, and $345 a year.
  - Webinars: Event with `eventAttendanceMode` = `OnlineEventAttendanceMode`; with no event data the Event is **not emitted**.
- **Decisions.**
  - **/pricing/ is not built.** `page-pricing.php` already prints WebPage, OfferCatalog and BreadcrumbList for it (S128). A builder would be a second source, so only `/membership/` is built (commit `787b2a5` removes the option I first wrote; the earlier commit stays in history).
  - **Accreditation wording.** The credential is "recognised by SoMAP", as the certificate block in `course-parts.php` words it ("SoMAP independently verifies"). It does not claim more than the page does.
  - **Webinars.** No document gives a webinar's name, date or link, so all are arguments. Without name, start and join address, no Event is emitted, because an Event short of Google's required values earns nothing, as the About page's video rows are dropped under the same rule.
- **Could not prove.**
  - None of these has a template, so none has run on a page.
  - Whether Google reads the two-part trial price on the monthly Offer: **cannot tell** (the row's Rich Result column is "None").
  - The Academy's own breadcrumb row is not in DSRD 1 §9; it is read from "breadcrumbs mirror the URL hierarchy exactly".
  - The seven-school list inside the directories' CollectionPage goes beyond the spec row. It is one property and is flagged.
  - Whether `/webinars/` as an index page will exist: **cannot tell**.

### Rank Math filters (`rank-math-feed.php`)
- **Spec line.** DSRD 10 §9 Standard 2 and Standard 3, decision (c).
- **What changed.** Book notes, quotes, the course template, the Courses template and the listing routes were added to the theme-owned breadcrumb test; the listing routes were added to the CollectionPage removal.
- **Proved.** Six stand-in cases: the BreadcrumbList is removed (and the WebPage's pointer to it) on each of the five wired types, the CollectionPage on listings, and nothing is removed on an unrelated page.
- **Not done on purpose.** No WebPage removal anywhere (cannot tell if Rank Math prints one). No filter for the function-only types (nothing to test against, and `/pricing/` is already listed).
- **Could not prove.** The filters have never run inside Rank Math. Standard 1 says Rank Math prints nothing on a singular page, but `rank-math-feed.php`'s own article code assumes it prints Organization, WebSite and WebPage there. The two statements conflict (the job 9 audit's open question), and I could not settle it without Rank Math.

## How the test works, and what it cannot do

`cloud-reports/schema-build/` holds: `stub.php` (a stand-in for WordPress, so the real theme templates run under plain PHP 8.3), `render.sh`, `cases.php` (one case per page type), `run.php` (the driver), `selectors.js` (Chromium selector check), `output.txt` (the committed result).

Run it from a checkout with a copy of the main tree beside it:

`php cloud-reports/schema-build/run.php <this tree> <baseline tree>`

For each case it renders the template, or calls the function, with stand-in data and then:

1. finds every JSON-LD block and checks it parses as JSON with `@context` `https://schema.org`;
2. checks every property the spec lists for that type is present, and that nothing the spec forbids is (for example `isBasedOn` with no book note);
3. for wired templates, renders the baseline too and checks every block it printed is still printed byte for byte and in the same order, and that the visible HTML is identical once the script blocks are removed (runs of whitespace collapsed, because the line breaks around a removed script block are not visible);
4. checks every speakable selector matches an element on the rendered page.

**It does not prove:** anything about WordPress, Rank Math, ACF or the real database; that the stand-in data is shaped like production data; or that Google accepts the output. I could not download WordPress here and did not run Google's Rich Results Test. **Where Rank Math may also publish the same type, the test says nothing.** That is the largest open question in this build.

## Other things to know

- **Placement.** Blocks print in the page body after the main element, where all 25 existing blocks already sit. DSRD 3 §5.7 says "in the `<head>`". The spec and the theme disagree; I followed the theme.
- **Breadcrumb label.** Last crumbs use the record's `breadcrumb_title` when set, as DSRD 1 §9 says. The visible trail on book notes and quotes still prints the full title, so where the field is set the two differ until the visible trail moves. That is a visible change, so it was not made here.
- **Encoding.** The new blocks add the two flags `JSON_HEX_TAG` and `JSON_HEX_AMP`, so a title containing `</script>` cannot end a block early. The existing blocks do not have them and were not changed.
- **`autostubs.php`** in the test folder is generated by `render.sh` and lists the WordPress functions the stand-in stubs to null. It is committed because the test needs it to run.
- **PHP syntax check.** `php -l` on every changed file (`functions.php`, `learn-listing.php`, `rank-math-feed.php`, `schema-parts.php`, `single-article.php`, `single-book_note.php`, `single-quote.php`, `template-course.php`, `template-courses.php`, and the four PHP files in the test folder): **no syntax errors**.
