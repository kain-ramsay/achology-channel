# DONE: the five book note headings rewritten across the 99 published records

**From:** Claude Cowork, the session following S360. **Date:** Monday 14 September 2026.
**Answers:** `BRIEF__Rewrite_The_Five_Book_Note_Headings_Across_The_Ninety_Nine_Published_Records_S360.md`.

---

## 1. The published set, confirmed before touching anything

Read the live `book_note` list off the install's own REST API (`achologytest.com/wp-json/wp/v2/book_note`, paginated, ordered by slug), not off any record's own `post_status` field. That field turned out unreliable in both directions: 108 records carry `post_status: publish` in their own fields table, but 9 of those are not yet on the install; conversely at least 17 records carry `post_status: draft` in the fields table while sitting live on the install. The REST read returned exactly **99 slugs**, matching Code's S114 count. Every one of the 99 has a matching file in `Content Records/book-note/`, and every one of the 99, read fresh, carried the five old headings word for word and in order before any edit. No file in scope was skipped.

## 2. The edit: 99 of 99, confirmed by read-back

`book_note_record_headings.py` was stale, exactly as the brief warned: its own `HEADINGS` table still targeted the S314 five as the ruled wording. Read DSRD 9 section 32.7 fresh this session; it now carries Kain's S115 five, recorded there S360. Updated the script's `HEADINGS` table and its docstring to the new five (data only, copied verbatim from the section, printed on every run so it can be checked), then ran its own correction logic, scoped to only the 99 confirmed slugs above so the run could not touch anything outside this brief's scope.

**99 records corrected, 495 headings replaced (5 per record).** Every one read back afterward: all five headings present, in order, at the correct `###` level, matching Kain's wording exactly:

1. The Argument at the Heart of the Book
2. The Background the Author Comes From
3. Practical Applications Beyond the Book
4. What this Might Possibly Mean for You
5. What Your Next Learning Step Could Be

Nothing beneath a heading moved. No file skipped, no stray wording found.

## 3. The gate, as expected

Every one of the 99 was re-gated after its edit. All 99, without exception, print the same expected mismatch:

```
FAIL  section headings, verbatim and in order        found 5
```

This is the mismatch the brief told me to expect, not a fault in the edit: `content_gate_standards.json` still holds the old five until Code's next step. Nothing else about this failure line varies across the 99; it was not spot-checked, it was read on every one.

## 4. Drafted-but-unpublished records still carrying the old five, named and not touched

51 records in `Content Records/book-note/` are not yet on the install and were left alone, exactly as the brief asked. All 51 still carry the old five. 36 of them at the standard `###` level under `## Body`:

a-new-guide-to-rational-living, a-path-through-the-jungle, before-happiness, bittersweet, born-for-love, come-together, critique-of-practical-reason, daring-to-trust, embracing-uncertainty, further-along-the-road-less-travelled, have-a-little-faith, keeping-the-love-you-find, leader-effectiveness-training, meditations-for-mortals, mothers-who-cant-love, necessary-endings, notes-on-a-nervous-planet, on-the-tranquility-of-mind, open-when, originals, quit, running-on-empty-no-more, shift, stoicism-and-the-art-of-happiness, surrounded-by-psychopaths, talking-to-crazy, teacher-and-child, the-advantage, the-art-of-the-good-life, the-happiness-project, the-high-5-habit, the-jealousy-cure, the-quick-and-easy-way-to-effective-speaking, the-stoic-challenge, the-tao-of-fully-feeling, the-way-to-love.

**Worth naming separately, found while checking this:** 15 more carry the same old five, word for word, but at `##` level (the same level as `## Body` itself, one level too shallow) rather than `###`. This is a structural fault the body-span reader cannot see past, on top of the wording question this brief is about, so a future sweep of these 15 needs a heading-level fix as well as a wording fix:

authentic-happiness-seligman, awaken-the-giant-within, childhood-and-society, civilization-and-its-discontents, counseling-the-culturally-diverse, difficult-conversations-patton, the-open-society-and-its-enemies, the-power-of-now, the-problems-of-philosophy, the-republic-plato, the-road-less-travelled, the-six-pillars-of-self-esteem, the-time-paradox, thinking-fast-and-slow, utilitarianism.

None of these 51 were edited. Editing them is not commissioned here.

---

OWED BACK: nothing on this brief. The theme, the gate standard and the importer are Code's next step, on the brief's own sequencing; this brief's job was the 99 record bodies and the report.

*No em or en dashes in this file or in any of the 99 edited records; checked before writing.*
