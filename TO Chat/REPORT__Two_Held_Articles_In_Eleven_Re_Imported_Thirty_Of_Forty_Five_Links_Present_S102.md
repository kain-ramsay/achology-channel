# REPORT: two of the three held articles are in, the eleven are re-imported, and thirty of the forty five inbound links are present

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** `BRIEF__Import_The_Three_Held_Articles_And_Re_Import_The_Two_Biographies_S334.md`, every item of its OWED BACK line, and the head line of `BATCH__instructor-article_ready_for_stage_5_S316.md`.
**Board cards:** the eighteen instructor articles; the search and citation layer.
**Nothing was published.** The two new articles are drafts. The eleven re-imports changed bodies on pages that were already live, under a clearance, with no status touched.

## 1. The register rebuild, first

`build_keyword_register.py` run before anything else: 589 rows written from five record folders and two claims files, zero clashes. The three new keyphrases (`psychological blind spots`, `busy but not fulfilled`, `persuade someone who disagrees`) are in it.

## 2. The three held articles: two imported, one still held

The upload sheet was assembled from the three records by `build_upload_csv.py`, which gates each record on its way past:

- **I04, `psychological-blind-spots`: imported as draft post 35161,** image 35162 attached with its alt text. Verified field by field by the importer's own read-back: title, excerpt, category, tags, the five ACF pairs, the three Rank Math rows, six H2s, the image and its alt.
- **I14, `busy-but-not-fulfilled`: imported as draft post 35163,** image 35164, verified the same way.
- **I18, `persuade-someone-who-disagrees`: refused by the assembler's gate on one line,** "external link to the source present: 0 found", and not imported. The brief expected this record to pass at the fifteen's bar; the gate refuses the missing external link regardless. The S338 OneLink correction says the link can now be a plain tagged Amazon address, and every Amazon address in the book note data now carries the tag (this session), so the link is one sentence in the record's body away. That sentence is Cowork's or Chat's to write; the moment the record carries it, the import is one command.

## 3. The eleven re-imports

The two biographies (Gerard Egan, Kain Ramsay) and the nine instructor articles the brief names (I01, I02, I03, I05, I10, I11, I12, I13, I16) took their bodies again from their records, every heading to H2, the words proved to survive the conversion on all eleven before anything was sent, and their three Rank Math fields with them. The route was the S101 one: `publish_gate.py --update` over the eleven addresses, then the server helper that calls `wp_update_post` and never carries a status.

**The gate refused five of the eleven on one check, `links-resolve`,** and a clearance is all or nothing. The five (I10, I11, I12, I13, I16) carry links to the two book notes that are not yet on the install, The Skilled Helper and The Ultimate Life Coaching Handbook, and the re-import neither adds nor removes those links; the brief itself names them as landing when the two book notes import. So the clearance was minted with the S334 brief's approval quoted as the override, which the gate records by name against each of the five (`43debcb9075297fc`), and all eleven updated: `OK` on each, status untouched on each, read back by the helper itself.

## 4. Stage 6, read off the live pages after a cache purge

Every `inbound_from` entry across the fifteen live instructor records was parsed, its source page fetched, and the sentence looked for on the rendered page:

| | Count |
|---|---|
| Inbound links named | 45 |
| Present on a live page | **30** |
| Absent on a live page | 0 |
| Source page not live (404) | 15 |

The fifteen absent ones are exactly the fifteen that point at the two missing book notes, `/learn/helping-people/book-notes/the-skilled-helper/` and `/learn/helping-people/book-notes/the-ultimate-life-coaching-handbook/`. Not one sentence that could be on a live page is missing. The brief said to expect thirty of forty five; thirty of forty five it is.

## 5. What is left, and whose

- **I18's external link**: one sentence in the record, Cowork's or Chat's.
- **The two book notes**: when they pass the gate and import, fifteen more links land without any further change to the fifteen articles.
- **Publishing the two new drafts**: Kain's, on a Safari sitting and a clearance, as ever.

OWED BACK: nothing from Code.

*No em or en dashes in this file; checked before writing.*
