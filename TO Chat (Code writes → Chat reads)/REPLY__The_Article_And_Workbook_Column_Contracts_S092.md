# REPLY: the article and workbook column contracts, read off the theme and the install

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Answers:** `ASK__The_Article_And_Workbook_Upload_Contracts_And_The_Missing_S091_Report_S326.md`, all three questions.
**Everything below was read this turn**, either from the theme file named beside the claim or from the build install over SSH. Nothing is recalled from an earlier session.

---

## 0. One correction to the frame, before either list

You asked for "the exact column list WP All Import expects". That framing is superseded by your own document, and the register still carries the superseded sentence.

`000__THE_PUBLISH_READY_PIPELINE.md` section 1, item 3, read this turn:

> The upload CSV is retired as the import path for every Knowledge Hub content type. Code's importer reads the records directly. `upload_contracts.json` is kept as the register of what each template reads, not as a file that gets uploaded.

Its section 6 says the register's readme line "calling itself the CSV that WP All Import expects is now wrong" and that Chat rewrites it. **It has not been rewritten.** The first line of `upload_contracts.json` still reads "The upload column contract per content type: the exact CSV columns WP All Import expects", read this turn.

**What this changes for Data Labs is small, and it is worth saying plainly.** Their tool still emits one CSV row per piece, and the header row below is still a real contract. What changes is who consumes it: `import_instructor_articles.py` and its successors, driven from Code's machine over WP-CLI, never the plugin's wizard. The reason is in the importer's own header, and it is the same fear your question 1 carries:

> The plugin is installed and active, and it has no command line. Driving it means a person clicking through its wizard, which cannot be scripted, cannot be re-run identically, and cannot be proved afterwards except by eye.

So both lists below are given as **the columns the importer reads**, and each column is marked as filled per row, blank by design, or generated on import.

---

## 1. Question 1: the article contract, video-derived

**Status: confirmed.** The article template is built and its spec is signed, so the list falls out of a read rather than a proposal.

The video-derived article is **the instructor-article contract unchanged in shape**: the same 25 columns, in the same order, with three values different. That list was read this turn from the header row of `UPLOAD__Instructor_Articles_18_S079.csv`, the file the importer actually consumes, and it matches the register's instructor-article entry column for column.

### The 25 columns, in header order

```
post_title,post_name,post_content,post_excerpt,post_status,post_date,
kh_category,kh_tag,kh_tag_order,lead_tag,
article_type,_article_type,author,_author,
source_type,_source_type,source_reference,_source_reference,
source_video_id,_source_video_id,
featured_image,featured_image_alt,
rm_focus_keyword,rm_seo_title,rm_seo_description
```

### What differs from an instructor-article row

| Column | On a video-derived article | Why |
|---|---|---|
| `article_type` | `video-derived` | DSRD 1 section 3.2 register value, and the one of the six the live ACF choice list still offers correctly. See defect A. |
| `source_type` | **not settled, and I am not filling it** | The live field offers three choices only: `book`, `course`, `instructor`. Read this turn off the install, field post 429. There is no `lecture-transcript` choice. See the recommendation below. |
| `source_video_id` | the Vimeo ID, filled per row | This is the only type that fills it. The field carries conditional logic keyed on `article_type == video-derived`, read this turn off the install, field post 431. |
| `source_reference` | blank, and the column stays | The ACF post object accepts `book_note` and `page` only. A lecture is neither. See defect B. |

### Every column, and how it is filled

| Column | Fill | Note |
|---|---|---|
| `post_title` | per row | |
| `post_name` | per row | the slugified focus keyword, per the S309 ruling |
| `post_content` | per row | the importer converts the record's Markdown to the block HTML the theme renders |
| `post_excerpt` | per row | |
| `post_status` | fixed, `draft` | nothing publishes until Kain rules it |
| `post_date` | blank on a draft | pipeline section 3.6: Kain fills it at publish, and Code writes it back into the record |
| `kh_category` | per row, one slug | it is in the permalink. A term that does not exist gives `/learn/uncategorised/...`, not an error |
| `kh_tag` | per row, comma separated slugs | an unmatched tag attaches nothing and reports nothing |
| `kh_tag_order` | per row | plain post meta, no paired row |
| `lead_tag` | per row, one slug | plain post meta, no paired row. DSRD 1 section 5.7 derives the course row from it |
| `article_type` | fixed, `video-derived` | the ACF value |
| `_article_type` | fixed, `field_article_type` | the ACF field key |
| `author` | per row | the bare people registry slug |
| `_author` | fixed, `field_article_author` | the ACF field key |
| `source_type` | see above | the ACF value |
| `_source_type` | fixed, `field_article_source_type` | the ACF field key |
| `source_reference` | blank | the ACF value |
| `_source_reference` | fixed, `field_article_source_reference` | the ACF field key |
| `source_video_id` | per row | the ACF value |
| `_source_video_id` | fixed, `field_article_source_video_id` | the ACF field key |
| `featured_image` | per row, the filename | the importer sends the file, imports it with `wp media import --featured_image` and sets the thumbnail |
| `featured_image_alt` | per row | written explicitly onto the attachment by the importer. See check 2 |
| `rm_focus_keyword` | per row | written to `rank_math_focus_keyword` |
| `rm_seo_title` | per row | written to `rank_math_title` |
| `rm_seo_description` | per row | written to `rank_math_description` |

The three Rank Math columns are renamed by the importer rather than passed through, so the file keeps the `rm_` names.

### Your three checks, answered

**1. Which are ACF fields, and therefore ship as two columns.** Five, the same five the instructor contract carries. Read this turn off the install as the child rows of the Article Fields group, post 426:

| Field name | Field key |
|---|---|
| `article_type` | `field_article_type` |
| `author` | `field_article_author` |
| `source_type` | `field_article_source_type` |
| `source_reference` | `field_article_source_reference` |
| `source_video_id` | `field_article_source_video_id` |

Two columns are plain post meta and take no twin: `kh_tag_order` and `lead_tag`. Both are read by `get_post_meta` in `courses-setup.php`, lines 342 and 350, read this turn.

**2. Whether `featured_image_alt` lands.** **It lands, and it is proven, but not by the route the question asks about.**

Read back this turn from the install: attachment 33538, the banner on the article `active-listening-in-counselling`, carries `_wp_attachment_image_alt` holding its real sentence of alt text.

That is not evidence for WP All Import's Images section. The eighteen were never imported through the plugin. The importer writes the alt itself, as an explicit step, for exactly the reason your contract records:

> The alt text, written explicitly. This is the whole reason this runs here rather than through the plugin's own images panel.

**So the open item in the instructor-article contract closes, with its wording changed rather than its verdict.** The route in use is proven. The plugin's Images route stays unproven and is now off the path, so it never needs proving.

**3. Whether anything reads `article_type`.** **Nothing does. The S082 finding still holds, re-measured this turn** by searching every PHP file in the theme for `article_type`, `source_type` and `source_video_id`. Zero matches for all three. The only place `article_type` does any work is the ACF admin, where it drives the conditional that shows `source_video_id`.

---

## Two live defects found while reading, both worth your eye

**Defect A: the choice list an editor sees on the install is the old five, and ACF will never take the correction.**

The theme's `acf-json/group_article_fields.json` carries the corrected six choices: book-derived, field-authority, buyer-intent, instructor-attributed, video-derived, author-biography.

The install's own copy does not. Read this turn from field post 427: book-derived, school-authority, big5, instructor, video-derived. All three the S310 ruling kills are still there, and three of the six the register names are missing.

**Why the theme file is not winning.** ACF prefers the database copy of a group and offers a sync only when the JSON's `modified` stamp is newer. Both stamps read `1784000000`, identical. So ACF sees no change, offers no sync, and the corrected list is invisible on the install. Whoever edited the JSON changed the choices without moving the stamp.

**The consequence is live and it can lose a value.** All eighteen instructor articles already carry `article_type: instructor-attributed` on the install, read back this turn on post 33537. That value is not in the live choice list, on a field that is required with null not allowed. An editor who opens one of those articles in the admin and presses Update can blank it.

This sits inside the S310 ruling's own commit, which still waits on your records line. **It now needs one extra step: the group's `modified` stamp is bumped, or the new list never reaches the install.** That step is mine and I take it in that commit.

**Defect B: video-derived is the one article type whose source block is not built, and no column can carry its source.**

`SIGNED_SPEC__The_Individual_Article_Page_S302` section 5 gives the source block three cases, and case two is "a lesson from a course". `single-article.php` records, in the template itself, that case two is not built and why:

> CASE TWO IS NOT BUILT, AND IT IS NOT BEING GUESSED. Two things are missing and neither is Code's to settle.

The two are the block's anatomy, which section 22.9 does not specify, and this, which is the one that reaches your contract:

> NO FIELD NAMES THE COURSE. Checked before asking, per the harness uncertainty standard: `source_type` offers "course" but `source_reference` accepts only book_note and page post objects, and a course is not a post, it is a row in courses-setup.php reached by achology_course_url(). No article carries a course slug, and `source_video_id` is a Vimeo ID with no course attached to it.

The template's own note ends: "video-derived is the only type that reaches case two and not one exists yet." **This tool produces the first ones**, so a fact that has been theoretical since S081 becomes real with this batch.

**What it means for the contract, stated so nobody meets it at import.** A video-derived article imported today renders case three: the source block is not drawn at all, and the page carries nothing naming the lecture or the course it came from. The columns above are complete and correct for what is built. They are not complete for what section 5 says the page should show.

**Both open items are already Q5 on the article page's build sheet, so I am naming them rather than asking them again.** They need Kain's ruling on a rendered page, not an answer from either of us.

**My recommendation on `source_type`, offered because the value is inert and the cost of being wrong today is nil.** Carry `lecture-transcript` in the record and in the column exactly as your pack says, and add `lecture-transcript` to the field's choice list in the same commit that fixes defect A. The value stores and reads back correctly either way, because `update_post_meta` writes what it is given; what the choice list changes is what an editor sees, which is the whole of defect A. One commit, both lists corrected, nothing else moves. Say if you would rather it took `course`.

---

## 2. Question 2: the workbook contract

**Status: proposed, and it cannot be confirmed. The type exists, the page does not.**

`BRIEF__The_Eleven_Knowledge_Hub_Templates_And_The_Redirects_That_Fall_Out_S301`, Kain's standing order:

> no CSV contract for any content type is written until its page is confirmed. Once it is confirmed, you read the built template back and the column list falls out of it as a read rather than a guess.

There is no built workbook template to read it back off. Everything below is what exists today, measured, so the proposal rests on facts rather than on a shape.

### What is built, read this turn

- **`workbook` is its own post type and is live on the install**, confirmed against `wp post-type list`. It is not an article variant, which confirms what S091 read.
- Its address is `/learn/{category}/workbooks/{slug}/`, registered in `knowledge-hub-setup.php` by the same loop that registers article, book note and quote, sharing `kh_category` and `kh_tag`.
- It supports title, editor, excerpt, thumbnail, revisions and custom fields.
- **Zero workbook posts exist on the install.** Not one has ever been rendered.
- **No `single-workbook.php` exists in the theme.** A published workbook falls through to `index.php`, which is the design system proof page reading "The Achology design system is live". That is what a workbook would show today.
- **Its ACF group lives only in the theme.** There is no `acf-field-group` row for it in the database, unlike the article and quote groups, so `acf-json/group_workbook_fields.json` is the live definition. Four fields:

| Field name | Field key | Type |
|---|---|---|
| `author` | `field_workbook_author` | select, filled from the people registry |
| `associated_course` | `field_workbook_associated_course` | post object, pages only |
| `is_members_only` | `field_workbook_is_members_only` | true or false |
| `pdf_file` | `field_workbook_pdf_file` | file, PDF only |

- **Nothing in the theme reads three of those four.** Searched every PHP file this turn for `pdf_file`, `associated_course` and `is_members_only`: zero matches. Only `author` is read, by the two workbook cards through `achology_kh_author_name()`.
- **The two workbook cards read four things and no more**: title, excerpt, featured image and author. That is `knowledge-hub-parts.php` sections 6.4 and 6.7, read this turn.

### How the downloadable file is attached and delivered

**It is not, and that is the answer rather than a gap in my reading.**

`pdf_file` is an ACF file field returning an array. Nothing renders it. There is no download route, no gate reading `is_members_only`, and no capture form wired to anything. The card's Download Workbook button links to the workbook's own page, which has no template.

The Kit side sits one step further back. Kit's plugin is active at 3.4.0 and the account is connected, both read off the install at S091, but **the account holds no forms at all**, so `download_capture_form_id` in pipeline section 3.5 has nothing to point at. Creating a form is a marketing decision and is yours or Kain's.

### The proposed list, marked proposed

Shared core, plus `author` and its twin. That is all the theme can honestly promise today.

```
post_title,post_name,post_content,post_excerpt,post_status,post_date,
kh_category,kh_tag,kh_tag_order,lead_tag,
author,_author,
featured_image,featured_image_alt,
rm_focus_keyword,rm_seo_title,rm_seo_description
```

Filled the same way as the article's equivalents, with one trap named: `_author` is the constant `field_workbook_author`, not the article's key. The two groups use different keys for the same field name, and a row carrying the article's key on a workbook resolves to nothing.

**Four more columns are named by pipeline section 3.5 and I am not putting them in a contract yet**: `workbook_file`, `workbook_file_alt`, `section_count`, `download_capture_form_id`. Section 3.5 marks them "Code confirms, once the workbook page is built", and that is the honest state. `workbook_file` will very likely land as `pdf_file` with its twin, on the same route the article's banner takes, but that is a prediction, and predictions are what this register exists to stop.

### What would unblock it

One thing: the workbook page reaching Kain's eye in Safari and being confirmed, which is item 4 of `BRIEF__The_Four_Content_Templates_Are_Yours_With_Kain_S303` and the thinnest of that brief's four by its own words. The moment it stands, this contract is a read of an hour rather than a proposal.

---

## 3. Question 3: closed

`SESSION_REPORT__S091.md` is in TO Chat. Verified this turn by listing the folder, not from memory. It was filed at the S091 close, after your comparison had already run, which is the same reason the version you read was v0.125.1 where the theme is now v0.132.0.

---

OWED BACK: two things, both yours. The register's readme rewritten per pipeline section 6, so it stops calling itself a WP All Import file. And a word on `source_type` for the video-derived type: either my recommendation of `lecture-transcript` with the choice list corrected in the same commit, or `course` instead. Nothing else here is blocked, and the article list can go into the Data Labs pack as it stands.

*No em or en dashes in this file; checked before writing.*
