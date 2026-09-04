# REPORT: the two missing importers are built and registered, and every record they read refuses for reasons that sit in the records and the theme

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** part one of `BRIEF__Build_The_Missing_Import_Route_And_Export_The_220_S338.md`; the OWED BACK line of `RULING__H9_Widening_Confirmed_Again_It_Did_Not_Land_S339.md`; section 5 of `BRIEF__The_77_Rescued_Article_Hero_Images_From_Canva_Export_To_Live_Page_S340.md`.
**Board cards:** the rescued field-authority articles (Salvage); the quote pages; the publishing wall.
**Nothing was sent to the install.** Both importers ran in plan mode only. No post was created, no term was created, no page changed.

---

## 1. What exists now

Two scripts in the Content Production Factory folder, beside the two older importers:

- `import_field_authority_articles.py`: reads every record in the field-authority-article folder, skipping batch reports and any file named `SUPERSEDED__`, and creates article drafts over WP-CLI with the hero attached from the record's own `featured_image` and alt text.
- `import_quote_pages.py`: the same for the quote-page folder, creating quote drafts. It carries no payload of its own: everything install-reaching is imported from the first script, so the two cannot drift.

Both are draft-only by construction, exactly as the S339 ruling defines it: the create carries `'post_status' => 'draft'` as a hardcoded literal with no input path around it, and the update path carries no status key at all, so a body-only re-run cannot change what it did not touch (the S100 lesson). Neither ever creates a taxonomy term. Both run the pipeline's stage 5 checks on every record (fields complete against the type's own standard, body shape by the stage 5 checker's own function, the named file on disk and inside its budget), then check the values the theme can actually read, confirmed against the live theme and install rather than assumed: category and tag terms on the install, the author as a key in the people registry, `article_type` and `source_type` against the ACF field's own choice lists, and the source book resolved to a post ID or left empty. Every record must also pass the words-survive proof before anything is sent. A record failing any check is refused and its reasons printed; nothing edits a record.

**The markdown conversion is written once, in the first script, and is wider than the two older importers' copies.** The field-authority bodies carry H3 sub-headings (nine records), bold (twenty nine) and a link whose address contains round brackets (a DOI), none of which the older converters render; this one keeps H2 as H2 and H3 as H3, renders bold, and reads a bracketed address whole. The two older importers still carry their own copies and should adopt this one the next time either is opened. Named rather than done unasked.

## 2. The register, and the S339 OWED BACK answered plainly

Both halves of the S339 ruling are on disk and were read there this session, not taken from the S338 claim: `reviewed_scripts()` walks the Content Production Factory folder (the code says so since S100), and the register's own standard reads "cannot publish a post itself, whether or not it creates one as an unpublished draft". The two scripts the ruling names are registered with hashes matching their bytes, checked this turn. The two new importers are registered under the same standard, each with its install-reaching payloads quoted in its entry. The acceptance suite was run three times this session, before and after the register changes: sixty three of sixty three cases as specified, every time.

## 3. The plan runs, read off the install this session

**Field-authority articles: eighty two record files read, none imports.** Refusals by class, a record may carry several:

| Count | Class |
|---|---|
| 82 | the images folder does not exist yet |
| 82 | a kh_tag outside the locked register, which would mint a term |
| 82 | lead_tag outside the locked register |
| 80 | source_type is not one of the ACF field's choices |
| 72 | author is not a key in the people registry |
| 23 | article_type is not one of the ACF field's choices |
| 2 | lead_tag is not one of the record's own kh_tag values |

**Quote pages: twenty five read, none imports.**

| Count | Class |
|---|---|
| 25 | demand_evidence missing |
| 25 | author is not a key in the people registry |
| 5 | image_quote_text differs from quote_text |

## 4. What each class is, and whose it is

1. **The images (82).** Expected: Kain's Canva export has not landed. The importer's default folder for the WebP heroes is a folder named `articles` inside the theme's `images/knowledge-hub` folder, Code's call, overridable at run time; when the S340 brief's PNGs land, the run is rename, convert, gate, import, in that order, and the attach step happens at import rather than as a separate pass.

2. **The tags (82 of 82, the frozen exemplar included).** DSRD 1 section 5.6, read this turn: "These 36 slugs are the addresses the Redirect Master's old-tag rows point at; Claude Code builds the tag pages at exactly these addresses." Every field-authority record carries free-text topic tags instead (`history of psychology`, `research ethics`, `harry harlow`, and so on), and the exemplar set the pattern with `self-awareness, personal-growth, know-yourself`. Two consequences the importer refuses on rather than causes: WordPress would have minted two hundred or so new terms outside the locked register, and the theme's course derivation (DSRD 1 section 5.7, `achology_courses_for_content`) maps registered slugs only, so the Explore Related Learning Paths block would render nothing on all eighty two pages. This is a record-side fault across the whole type and it is a retagging decision, which is content and therefore Kain's through you.

3. **The author key (72 articles, 25 quotes).** The records carry `charlotte-avery` (seventy of the seventy two) and `frederick-martin` (all twenty five quotes). The people registry's keys are `charlotte-j-avery` and `frederick-s-martin`, the full-name keys approved at S048, and the byline resolves by exact key, so an unknown one renders no author at all. The same slip appeared in the S335 profile metadata sets and was caught at S097. Record-side, mechanical.

4. **source_type (80).** The records carry `study`, `framework`, `original-synthesis`, `salvage`, `legacy-page`, `historical-overview`, `concept-explainer`, `psychological-concept`, `exercise` and `research-synthesis`; the theme's ACF field offers `book`, `course`, `instructor` and `lecture-transcript`. Nothing in the theme reads `source_type` (confirmed S092), so the page would not break; the admin dropdown would show blank and a save from the admin would empty it. Either the field's choice list grows, which is a theme edit for the theme queue, or the records' vocabulary narrows. A decision, not Code's.

5. **article_type (23).** Nineteen records carry `field-authority-article`, two `school-authority` and one `salvage-rewrite`; the register value in DSRD 1 section 3.2 and the ACF choice is `field-authority`. Record-side, mechanical.

6. **lead_tag not among the record's own tags (2).** Named in the printout by record.

7. **The quotes' missing demand_evidence (25).** Drafted at S300 before stage 0 existed. The five S329 fields are reported NOT RUN on these pre-standard records, per Kain's S332 ruling, and do not refuse; `demand_evidence` is not one of the five and does. The quote-page standard already says of this batch that "nothing downstream should treat them as ready".

8. **image_quote_text differs from quote_text (5).** Against the standard's own rule that the two are always identical (the S300 no-cap ruling). Record-side.

9. **The source book.** All twenty five quotes name The Ultimate Life Coaching Handbook's book note, and that book note is not on the install (sixty five are; not this one). `source_book_reference` therefore stays empty and the address is kept as plain meta, and the S303 ruling already says the source book block renders only where the quote has a source book. It resolves itself the day the book note is imported and the quotes are re-run.

10. **The quote type has no `author` field.** The pipeline's shared core gives every type an `author`, and the article and workbook ACF groups carry one; the quote group does not. The value is written as plain meta, and whether the quote template reads it that way or the group gains a field is a decision for the quote page build.

## 5. What this means for the queue

Nothing of either type can land until the records change: the tags on all eighty two field-authority records and all the author keys are the two classes that touch every record. The scripts need nothing further from Code until then. When the records are corrected at source, the run is one command per type, plan first, then push, then verify.

OWED BACK: nothing from Code on this file. Items 2 to 8 in section 4 are yours to route to their sources, and item 4's theme half belongs on the theme queue if the choice list is the side that moves.

*No em or en dashes in this file; checked before writing.*
