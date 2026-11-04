> CODE DISPOSITION, S210: WAITS ON a theme session of its own for this job; read in full by the course page block 3 sitting, which works only that page (Kain's one session, one job).
**For Code (theme session, with one factory step). What this needs from you:** a hidden taxonomy of people and ideas on every page, filled at import from one controlled list, and an importer that refuses any name not on that list. Nothing shows on any page. One DONE naming the theme version.

# BRIEF: the hidden idea tag on every page, and the importer check (Chat, Session 458, 4 November 2026)

**Why.** Kain ruled at Session 457, on the linking strategy page: "The idea list on every record and in Code's importer now, before launch, shown nowhere until the idea pages are built": "Yes". At Session 458 he approved the complete register it is filled from, built from every lesson of the 28 courses: "Yes, that's it". The idea pages themselves come after launch (his ruling of 2 November). The field is built now so that every page written between now and launch already carries it, and no page is reopened later.

**What changed since the S457 strategy page.** That page planned 69 names. The approved register has 1,336: 326 people and 1,010 ideas. Build for the larger list, and for it to grow.

## The controlled list

- **File:** `REGISTER__Tag_List_People_And_Ideas_S458.csv`, in the project folder's Course + Lesson Data | MASTER folder. Columns: `list` (person or idea), `name`, `slug`, `kind_or_type` (for people: thinker or public; for ideas: model, theory, technique, concept, school, tool or experiment), `by` (the person an idea belongs to, by name, where there is one), `lessons`.
- **Every slug is unique** across people and ideas. Chat checked this before sending.
- **The two registers it comes from** sit beside it, `REGISTER__People_In_The_Courses_S458.csv` and `REGISTER__Ideas_In_The_Courses_S458.csv`, and carry each name's lesson keys. They are the source for step 3.
- **The list grows.** Chat adds names by re-issuing the file with a new session stamp. The loader must re-run from the file without hand edits, adding new terms and never deleting a term a page already carries.

## What to build

1. **A taxonomy, `achology_idea`**, registered in the theme beside the 7 categories and the 36 tags, on every Knowledge Hub content type (articles of every kind, book notes, quote articles, workbooks, author biographies, hub guides) and on Help answers. It is **not public**: no archive page, no rewrite rule, no term pages in any sitemap, excluded from Rank Math and from search (DSRD 1 section 9, no thin taxonomy sitemaps). No template prints it until the idea pages are built. Each term carries term meta for `list`, `kind_or_type` and `by`, so a person term and an idea term are told apart, and an idea's maker can be read later for the line 12 link and the schema the strategy page names.
2. **A loader** that builds the terms from the controlled list file, idempotent, as a WP-CLI command you name in the DONE.
3. **The course lessons.** Add an `ideas` field (a list of slugs) to each lesson in the theme's course lesson data, filled from the lesson keys in the two register files: every person and idea whose lesson keys include that lesson. Build it as a step that re-runs from the files, as the lesson paragraphs build step does. Printed nowhere.
4. **The records contract.** A new optional row in every content record's Page fields table: `| ideas | slug; slug; slug |`, semicolon separated, slugs from the controlled list only. Write it into the records contract and the upload contracts register for every type above.
5. **The importer check.** The importer reads the `ideas` row, sets the terms, and **refuses the record** if any slug is not in the controlled list, naming the bad slug. A record with no `ideas` row imports as now: the row is optional until Chat's tagging pass fills it.
6. **The rule for what goes in the row** (Chat's, for the tagging pass; written here so the importer's test notes match it): a page carries a person or idea only where the page teaches it as its subject or a substantial part, the same threshold as the modality tags (DSRD 1 section 5, ruled S311). A passing mention does not count.

## What done looks like

- The taxonomy exists, hidden, and the loader has built all 1,336 terms from the file. Read back: the count by `list` is 326 person and 1,010 idea.
- Every course lesson in the theme data carries its `ideas` list. Read back: lesson 001-011 carries `aristotle`; lesson 001-132 carries `abraham-maslow` and `maslows-hierarchy-of-needs`.
- The importer refuses a test record carrying `not-a-real-idea` and names it, and imports a test record carrying `drama-triangle` (slugs drop a leading "The").
- No page on the build site shows any change, and no new URL or sitemap entry exists. Checked by fetching one page of each type and the sitemap index.
- The records contract and the upload contracts register carry the new row.

## After this ships

Chat runs the tagging pass over the Knowledge Hub records and Help answers, a batch at a time through the importer. Code is not asked to tag.

## Not in this brief

The idea pages, their template and look, the Learn It Free First block on course pages, and every visible link line from the strategy page. All come after launch.

*Kain's words above are quoted with their session. No em or en dashes in this file; checked before writing.*
