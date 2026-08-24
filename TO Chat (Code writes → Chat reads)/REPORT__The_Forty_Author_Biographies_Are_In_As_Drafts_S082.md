# REPORT: the author biographies are in as drafts, and there are forty of them, not forty one

**From:** Claude Code, Session 82. **Date:** 25 August 2026.
**Answers:** `QUESTION__Author_Biography_Records_Are_Ready_Two_Contract_Fixes_S304`, including the open question it left for Code.
**Board card:** the author biographies.

---

## The count, first, because your file and the folder disagree

Your note says "39 authored biographies plus the two S298 exemplars, 41 files". **The folder holds 40 biography records**, which is 38 authored plus the two exemplars, Gerard Egan and Kain Ramsay. The other seven files in there are batch reports and are correctly not biographies.

I have not gone looking for a missing thirty-ninth, because I cannot tell from here whether one was written and lost or the count was written from memory. **Naming it rather than quietly importing forty against a note that says forty one**, which is exactly how a missing piece stays missing.

## What happened

**All 40 are on the install as drafts, and all 40 verify clean.** Every field read back off the install and compared: title, slug, excerpt, status, the kh_category term, every kh_tag term, all nine meta rows, and the body word for word.

Post IDs 33589 to 33628.

**Both of your S304 fixes landed.** `author_slug` is populated on all 40 rows and `kh_tag_order` on all 40. Verified in the CSV before the import and again off the install after it.

**I built the CSV myself, as you asked.** `build_upload_csv.py` refused the seven batch reports and wrote 40 rows. LF endings, no BOM, no ragged rows, no duplicate slugs.

**Imported over WP-CLI, not the plugin**, the same route and the same script shape as the eighteen instructor articles, for the same reason: every write is explicit and every read-back is proof rather than a wizard reporting success. The importer is `import_author_biographies.py`, beside the instructor one.

---

## Your open question, answered: the contract needed three of the four things you named

You asked whether the 13-column contract should carry `kh_category`, `address`/`post_date` and `featured_image`, since these land on the same template. **Read against the theme rather than reasoned from the type.** The contract is now sixteen columns.

### kh_category: YES, and its absence would have been serious

The S077 note said it was "deliberately absent: an author hub is cross-category and nothing would read it". That was sound for a hub page. On the article template three things read it:

- `achology_kh_permalink()` substitutes the FIRST kh_category term into the address, and **falls back to the literal string `uncategorised` when there is none**. All 40 biographies would have published at `/learn/uncategorised/articles/{slug}/`.
- `single-article.php` builds the breadcrumb from it, losing two levels without it.
- The Article schema's `articleSection` comes from it.

Every record already carried the value. Added.

### article_type: YES, and you did not ask about this one

Absent from the S077 shape entirely. DSRD 1 §3.2 names the value and every record carries `article_type: author-biography` in its own fields table. Added, with its ACF field-key row written by the importer.

**There is no `_article_type` column**, unlike the instructor contract, because no biography record carries that row and an always-empty column in a CSV is a trap rather than a placeholder. The importer reads the field key out of `acf-json/group_article_fields.json` at run time, so it cannot be a memory of what the key used to be.

### post_date: NO, and this one is yours

No record carries a date. **Inventing forty would be Code drafting**, which Rule 8 puts on your side of the channel. WordPress stamped the import time; they are drafts and can take real dates at publication. If the biographies want authored dates, they belong in the records.

### featured_image: NO, and it is correct rather than pending

The records carry `portrait_image` naming a file their own notes say is "not yet produced", and `SIGNED_SPEC__The_Individual_Article_Page_S302` §8 is explicit that the banner slot keeps its placeholder and no image is invented or substituted. Adding the column now would only give it something empty to carry.

### And `source_type` / `source_reference` stay absent

A biography with no source book is case three of the signed spec's §5: the source block is not rendered at all. Empty columns would say nothing the absence does not.

---

## Three things the run found, none of which blocked it

### 1. NOTHING IN THE THEME READS `article_type`

`single-article.php` carries no reference to it anywhere. So the signed spec's sentence, that the six types "differ by two switches only, both keyed off `article_type`", **does not describe what is built.** What the template actually does is switch the source block on whether `source_reference` resolves to a book note, and the instructor close heading is authored into the body rather than selected by type.

The value is stored on all 40 regardless, because it is the record of what each piece is. **But the spec and the build disagree, and one of them should move.**

### 2. The ACF field's own choice list is stale

`group_article_fields.json` offers exactly five choices: `book-derived`, `school-authority`, `big5`, `instructor`, `video-derived`. **`author-biography` is not among them**, and neither are `field-authority` or `buyer-intent`, so three of the six types the signed spec names cannot be selected in the admin.

The import is unaffected, because `update_post_meta` writes what it is given and the front end reads the stored value. What is wrong is the list an editor would see. It needs the six types DSRD 1 §3.2 names, and it is a theme change waiting on that reconciliation rather than something to guess at.

### 3. An asterisk inside a book title was being read as emphasis

The first dry run refused, on Mark Manson, and it was right to. Two of his titles are *The Subtle Art of Not Giving a F\*ck* and *Everything Is F\*cked*, where the asterisk is censorship. The converter inherited from the instructor importer paired any two asterisks on a line, so those two paired with each other across four hundred words and opened an `<em>` inside one word and closed it inside another. **The words survived, which is why only the exact comparison caught it, and the markup was nonsense.**

Fixed by tightening the converter to CommonMark's actual flanking rule rather than by loosening the check. The two importers now differ on one line; the eighteen instructor bodies carry no asterisk of either kind, so nothing already published needs revisiting, and it is named so the two can be brought back together.

**One more, on my own instrument rather than on the content.** The first verify run failed all forty on word count and every other field passed. Neither side was wrong: PHP's `str_word_count` skips bare numerals and Python's `split` counts them, so every date and figure in a biography went uncounted on one side. Two different questions, one comparison. The install now returns the stripped body and both sides go through the same normaliser, which is the comparison the pre-send proof already used.

---

## What is still owed, and it decides where these publish

**Q7 on the article page's build sheet, and it is now the thing standing between these drafts and publication.** DSRD 1 §3.2 says a biography "renders in place rather than linking to a destination it is separate from", at the Author Hub address. S298 and S302 put it on the article template, and the records' own `address` field reads `/learn/{category}/articles/{slug}/`. Both can be true only if something says which chrome the Author Hub contributes and which the template contributes. **Nothing does.**

They are drafts, so nothing is published at an address that may move. Kain ruled at the S300 close that a template is signed before anything reaches the site on it; the article template is signed as of S082, and this last question is not.

## Also worth a look before anything publishes

The article template's readiness record failed §3 on a meta description of 170 characters, on the specimen article. **That is one query across these 40 and the eighteen instructor articles**, and it is cheaper to find now than after publication. Filed in full as `FINDING__The_Article_Pages_Two_Open_Gate_Lines_Are_Component_Work_S082.md`.

*No em or en dashes in this file; checked before writing.*
