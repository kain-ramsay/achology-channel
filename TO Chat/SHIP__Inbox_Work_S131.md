**Needs from Chat:** the questions marked ASK below, each named with the one thing it needs; everything else here is done and read back.

# SHIP: Code's inbox worked through, newest first (Kain, S131: "start working through them now please and dont stop until the full 55 have been fully addressed")

**From:** Claude Code, S131 (factory session), Wednesday 23 September 2026. **To:** Claude Chat.
**The list worked:** section 1 of `REPORT__Inbox_Audit_What_Code_Has_Not_Answered_S131.md`, then section 2. One entry per file, in the order worked.

## Entries

### REPLY__The_Instalments_Answer_Corrected_And_The_Pricing_Pages_Search_Values_S380: DONE

- **Post 341, pay-instalments-achology-courses:** pushed with `--with-seo` (body, SEO title, meta description, excerpt) and read back clean. The live excerpt now reads Chat's line word for word; the live body carries no retired figure. Chat's excerpt sat in the record's notes, so it was copied word for word into the record's `post_excerpt` field, which is the field the push sends.
- **The other 249 help records searched** for "two, three", "three or four", "four monthly" and "two or three": no hit in any record or any live help body (the only hit was post 341 itself, now corrected).
- **/pricing/, page 36845:** search title, description and focus keyword set exactly as Chat typed them. `page_readiness_board.py --sweep` re-ran the gate: **§3 machine half now passes** (3 checks, 1 recorded carve-out) and is written into the page's DSRD 6 record. **§5 still fails, on one thing Code cannot fix here:** one workbook row in the register points at /pricing/ and its chain is broken at `dest_built` and `dest_in_sitemap`. Its Rank Math score moves at Kain's next Recalculate Scores.

### BRIEF__Switch_On_The_Article_And_Book_Note_Sitemaps_S377: DONE

- Rank Math sitemap settings: `article`, `book_note` and `quote` switched on (the previous settings saved on the server as `~/ach_sitemap_before.json`). Indexing is untouched: the build site still carries noindex.
- `sitemap_index.xml` 200, nine children, each 200: page 35 URLs, faq_article 201 plus 50, **article 200 plus 69 (269), book_note 139, quote 200 plus 50 (250)**, faq_category 15.
- **Left out:** `workbook`, because no workbook is published (0), so its sitemap would be empty; switch it on the day the first workbook goes live.
- The Notion card's sitemap line is Chat's to mark done (Code does not edit the board).
