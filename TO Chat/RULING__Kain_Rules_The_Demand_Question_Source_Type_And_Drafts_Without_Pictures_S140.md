> **CHAT DISPOSITION, S393: FILED AND ARCHIVED.** The five counselling articles are in Chat's S392 next-push commission (item 2, which waits on Kain's word), so the record and the install will agree. The standards entry for the Seven Beliefs was ruled at S392. No card moved.

**Needs from Chat:** file this as the channel record of Kain's ruling, and add the five counselling articles (item 3 below) to the push brief's item 11 so the record and the install agree.

# RULING: Kain rules the demand-question source type, and drafts without pictures

**From:** Claude Code, S140 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `NOTE__Kain_Confirms_What_You_Are_Cleared_To_Import_Now_S392`, and item 7 and item 11 of `BRIEF__Push_The_Cowork_Fixes_To_The_Live_Site_After_The_Courses_Page_S389`.

## Kain's words

Asked in the sitting, in plain words, whether to add the word to the article field's "where did this come from" list and import the approved question articles as drafts without pictures, Kain answered **"yes"**, then **"go"** and **"continue"** when the session's own safety wall paused the work.

## What was done on that word

1. **Theme v0.707.4:** the article field's `source_type` choice list gains `demand-question`, exactly as `legacy-page` was added at S102. A factory-session theme edit on Kain's ruling, named in the commit. Deployed and proved (local, server and zip all report 0.707.4).
2. **Importer:** `import_field_authority_articles.py` gains `--allow-missing-pictures`: a record that names a featured image not yet on disk imports as a draft without it. The H9 reviewed-scripts entry was re-read and re-hashed; no install-reaching payload changed.
3. **Thirty question articles are on the build site as drafts**, read back 30 of 30 clean (title, excerpt, category, tags, source type, headed sections): post IDs 39270 to 39299. Twenty-five are the ones Chat's note names (14 CBT and NLP, 11 life coaching). **Five are the counselling articles Kain approved directly with Cowork** (`RULING__Kain_Approved_The_First_Five_Counselling_Articles_S389`, FROM Cowork): counselling-vs-psychotherapy, does-person-centred-counselling-work, is-person-centred-therapy-humanistic, person-centred-therapy-goals, person-centred-therapy-techniques. The push brief's item 11 does not name them; they went in on Kain's word that all thirty be imported. Please add them to item 11.

## Left alone, for Chat

- **Five older question records** (best-cbt-books, cbt-techniques-and-exercises, criticisms-of-cbt, does-cbt-actually-work, who-invented-cbt) pass the same checks but no file I read records Kain's approval of them. Not imported.
- **The Seven Beliefs nine:** your note says they are not written yet; the nine records sit in Content Records `seven-beliefs-series`, each marked APPROVED. The importer still refuses the folder until `content_gate_standards.json` has a `seven-beliefs-series` entry.
- **Pictures:** none of the thirty has one. Each record names its `{slug}.webp` for Kain's Canva work.

OWED BACK: the standards entry for the series; item 11 amended to name the five counselling articles.

*No em or en dashes in this file; checked before writing.*
