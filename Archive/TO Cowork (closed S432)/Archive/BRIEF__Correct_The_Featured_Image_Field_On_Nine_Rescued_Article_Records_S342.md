# BRIEF: correct the featured_image field on nine rescued-article records, one value each

**From:** Claude Chat, Session 342. **Date:** 5 September 2026.
**Authority:** Kain's S340 approval of the hero image brief covers this; the nine fields were meant to read `{slug}.webp` at S335 and S339 and do not. Kain said yes to the channel batch this session.
**Run under:** the Cowork Production Harness (Version 17); Rule 5 (never open the master file); Rule 7 (your outbound tray is FROM Cowork). A metadata run: no body is opened.
**Answers:** Code's `REPORT__Seventy_Four_Rescued_Articles_Are_Drafts_With_Their_Heroes_Eighteen_Wait_S102.md`, section "Nine records name a picture that exists, under the wrong name". Code has already imported 74 of the rescued articles as drafts with their pictures; these nine were refused by the importer because the record names a file that is not on disk under that name.

## The job

In `Content Records/field-authority-article/`, on exactly these nine records, set `featured_image` to `{slug}.webp`, where `{slug}` is the record's own `post_name`. The picture already exists on disk under that name; only the field is wrong.

| Record | The field reads today | Set it to |
|---|---|---|
| a-guide-to-breaking-bad-habits | /wp-content/uploads/kh/articles/a-guide-to-breaking-bad-habits.jpg | a-guide-to-breaking-bad-habits.webp |
| compassions-test-insights-from-the-good-samaritan-experiment | NEEDS PRODUCTION: hero image of a figure pausing on a path (...) | compassions-test-insights-from-the-good-samaritan-experiment.webp |
| delayed-gratification-insights-from-the-marshmallow-test-study | marshmallow-test-delayed-gratification.jpg | delayed-gratification-insights-from-the-marshmallow-test-study.webp |
| from-roots-to-revolution | PLACEHOLDER, to be assigned in production per DSRD 2 image spec | from-roots-to-revolution.webp |
| how-immediacy-shapes-engaging-and-impactful-conversations | [PLACEHOLDER, image not produced in this drafting session (...)] | how-immediacy-shapes-engaging-and-impactful-conversations.webp |
| karpman-drama-triangle | karpman-drama-triangle.jpg | karpman-drama-triangle.webp |
| the-importance-of-self-awareness | the-importance-of-self-awareness-hero.jpg | the-importance-of-self-awareness.webp |
| the-origins-of-humanistic-psychology | humanistic-psychology-origins-hero.jpg | the-origins-of-humanistic-psychology.webp |
| understanding-your-core-values | [PLACEHOLDER, to be assigned in production per DSRD 2 image spec] | understanding-your-core-values.webp |

Where a record's field carries prose image direction (the Good Samaritan and immediacy records), move that prose into the record's `notes` field before replacing it, exactly as the S335 normalisation did; nothing written is deleted. `featured_image_alt` is not touched. Nothing else in any field table moves.

## How to know it worked

Run `content_gate.py` on each of the nine after the edit and attach the nine printouts to your batch report; each must still read GATE: PASS on every line. Then one DONE file to FROM Cowork naming the report, in the same shape as `DONE__Retag_And_Keys_Run_S341.md`. Code's `--push` then imports the nine; it creates only what is missing.

## What this brief does not cover

Nine other records have no picture and no map row: `a-guide-to-building-inner-resilience`, `character-traits-of-a-life-coach`, `starvation-insights-from-ancel-keys-the-minnesota-experiment`, `the-4-stages-of-human-evolution`, `the-psychology-of-self-improvement`, `timeless-lessons-from-the-life-and-works-of-hans-j-eysenck`, `understanding-the-cognitive-load-theory-experiment`, `what-is-counselling-psychology-a-search-for-a-definition`, and the skipped empowerment-dynamic record, which stays skipped. Those pictures are Kain's to make in Canva and the map rows are Chat's to write when he does; nothing for you there.

*No em or en dashes in this file; checked before writing.*
