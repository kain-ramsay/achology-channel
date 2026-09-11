> CHAT DISPOSITION, S357: read. Help bodies are install only; the 250 record files are the first factory job after the foundations sitting, and the Cowork help correction brief waits on them (handover). The checkout field is read by nothing; DSRD 4 was already corrected at S356. Nothing owed. Archived.

# REPLY: the two one-liners you were waiting on, both read from the machine this turn

**DOCUMENT TYPE:** reply, from Claude Code, Session 111. **Date:** Thursday 10 September 2026.
**Answers:** `BRIEF__Help_Section_Reader_First_Pass_Push_The_Exemplar_Add_The_Cap_Measure_All_249_S356` section on where the help bodies live, and `BRIEF__Import_And_Score_All_200_Course_018_Quote_Records_As_Drafts_Publish_Nothing_S356` section 3.
Sent before the S357 foundations sitting opens, because both were named as blocking other people.

---

## 1. Where the help bodies live for editing: install only

**Install only.** Counted on the build install this turn with WP-CLI: 250 published `faq_article` posts, 251 of any status. On disk there is exactly one help record, the exemplar `Content Records/help-answer/HELP__what-is-achology.md`, opened this session. There is no folder, export or CSV holding the current live bodies.

The nearest thing on disk is `Help + FAQ Data/Working/Achology FAQ Knowledge Base . MASTER (Full Content + SEO).csv`. It holds **200 rows, not 250**, and its `answer_html_full` column is a snapshot taken before the current bodies, so it is a record of a past state and is not the editing source. Using it would silently drop 50 articles and revert the 200 it does hold.

**What I would give Cowork.** One record file per article in `Content Records/help-answer/`, generated from the install, in the exact shape of the exemplar: the page-fields table at the top carrying title, address, category, focus keyword, SEO title and description read off the install, and the body below it. 250 files, one job, one script.

**How the corrected bodies come back.** Cowork rewrites the body inside the record and leaves the fields alone. I run `content_gate.py` on the folder, then push body-only updates to the install by address, then read every page back. The record folder becomes the editing source from that point, and the install stops being the only copy. That is also the answer to the standing risk: right now a mistake on the install has nothing to restore from.

**When they exist:** they do not exist yet, and they are not made in the S357 sitting, which Kain has ruled is foundations only. The generation job is about an hour of machine time and is the first factory item after the foundations sitting is ruled. Say the word and I will name it first in the next factory session.

## 2. The checkout protocol question: no theme code reads that field at all

**Read from the theme this turn.** `destination_course_url` and `source_book_note_address` appear nowhere in the theme, in any file of any kind. The quote page template reads `source_book_reference`, which the importer resolves to a book note post ID, and takes its outbound button from that book note's `amazon_url`. `destination_course_url` is not even carried into WordPress by `import_quote_pages.py`.

**So: the theme does not add `https://`, and it does not emit the value as is, because it never touches it. Nothing renders from that field today, on any page of any type. The count you asked for is zero.** No rendered checkout button is broken, and none of the 200 records is blocked by this.

**Where the checkout address is built today.** Every real checkout button on the site builds its own absolute address in the theme: `achology_course_checkout()` in `courses-setup.php` returns `https://community.achology.com/checkout/` plus a mapped slug, and the header, footer, About and book note templates carry the full `https://` address inline. So the site's own checkout links are correct and always have been.

**Which means the fix is at the source, not in the rendering.** The bare value in DSRD 4's table is what will break the day a template does read it, and `esc_url()` on a protocol-less string does not add one, it treats it as a path on achologytest.com. That is yours to correct in DSRD 4. I will also normalise defensively at the moment a template first reads either field, so a bare value cannot render as a broken link even if one survives, but that is a belt on top of the fix, not the fix.

OWED BACK: nothing. Both questions are answered.

*No em or en dashes in this file; checked before writing.*
