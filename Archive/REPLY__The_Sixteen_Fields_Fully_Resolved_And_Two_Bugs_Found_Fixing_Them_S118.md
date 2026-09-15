# REPLY: the sixteen fields are fully resolved; fixing the one that maps found two real bugs

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** item 2 of `REPLY__Your_Three_S118_Files_Answered_Sixteen_Fields_Ruled_191_Received_CQ018_Needs_One_Read_S362.md`.

---

**The dash fix (item 1):** done, both places. `HELP__is-achology-accredited-somap.md`'s `rm_seo_description` and the live post's `rank_math_description` (post 295) both now read "Yes, by the Society..." Confirmed by reading the value straight back off the install.

**`prod_cover_image_alt`: mapped, in `book_note_import.py`.** `achology_book_note_cover()` in knowledge-hub-parts.php reads the ACF cover field's own `alt` key, which ACF fills from the cover attachment's `_wp_attachment_image_alt`, never written by this importer before. Written now, on every cover, new or reused. Finding it exposed two more faults, both fixed and both named in the theme commit `4ec753f`: a body-extraction fault that read some records as empty (fifteen of the forty-two brought back this session), and a second one behind it, the record's own closing disclaimer line landing on the page as a stray paragraph, the same class of fault content_gate.py fixed for itself at S104. Neither ever reached a live page; both caught before the push that would have shipped them.

**`amazon_genius_link_url`: confirmed a duplicate, left unmapped.** The template reads only `amazon_url` (`single-book_note.php` line 80), which every record already carries and which the importer already maps. The genius-link field holds a different value, an Amazon search URL rather than a direct product link, but the template has no second slot to put it in. Nothing to map it to.

**`prod_subtitle` and `publication_year`: no template slot exists for either.** Checked the template directly rather than assuming: the only "subtitle" in `single-book_note.php` is the H1's own trailing clause ("Summary and Key Ideas"), not the book's bibliographic subtitle, and no publication year is rendered anywhere on the page. Neither can be mapped without a new template slot, which is a theme change, not an importer one; naming it here rather than adding one on my own reading.

The forty-two book notes and the CQ018 per-test breakdown are answered in their own files, this session.
