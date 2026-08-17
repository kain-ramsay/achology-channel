# RECORD: DSRD 1 §5.7 is built, and it needs one more field than the spec names

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `RULING__Course_Selection_Lead_Tag_Plus_Slug_Correction_S253.md` §5
items 1 to 3, and `CONFIRMED__Lead_Tag_Field_Goes_Into_The_Import_Spec_S254.md`.

## 1. What is built

`achology_courses_for_content()` now implements §5.7 as written: drop the
content attribute tags, fill the slots from the lead tag's mapped course list
in the order §5 writes it, top up from the next tag where the lead maps fewer
courses than there are slots, resolve abbreviations through DSRD 5.

The frequency rule is gone from the code, and the reason it was wrong is
recorded in the docblock so it is not re-derived.

`achology_course_companions()`, the school-based stand-in, is deleted. It had
no callers left and your instruction was that it comes out entirely.

**The nine aliases were already added at S050**, so item 1 needed nothing.
`achology_course()` resolves DSRD 1's abbreviations through them.

## 2. Verified on the live page, three states, each able to fail

The book note is the Frankl test post, id 10901.

| State | Course cards | Which |
|---|---|---|
| no field set | **0**, block absent | n/a |
| `lead_tag` only | **3** | Clarity/Purpose, Goal Setting, Life Coaching Certificate |
| `kh_tag_order` set | **3** | the same three, same order |

Those are exactly what DSRD 1 §5.2 maps to Find Purpose & Direction, in the
order §5.2 writes them, and they match your worked example for this book. The
page is left with `lead_tag` set so Kain can view the block; that post is on
the delete-at-import list either way.

**One correction to my own method, said plainly.** My first "block is absent"
check was run against `/learn/book-notes/mans-search-for-meaning/`, which is a
404. The real address carries the category. So that check measured nothing, and
all three were redone against the live page. Same fault as a green test that
cannot fail, caught this time because the result looked convenient.

## 3. The thing I need to tell you: `lead_tag` alone cannot do step 3

§5.7 step 3: "Where the lead tag maps fewer courses than there are slots, top
up from the next tag on the row, then the next, skipping any course already
shown."

**The next tag on the row is not recoverable from `lead_tag`.** It stores one
slug, and the tag list read back from WordPress is alphabetical, which is the
whole reason the field exists. So a renderer with only `lead_tag` implements
step 2 and cannot implement step 3.

**Measured before deciding anything**, across all 620 master rows, against
§§5.2, 5.3 and 5.5:

```
rows whose lead tag maps fewer than 3 courses (a short row at desktop):  2 of 620
rows whose lead tag maps fewer than 2:                                   0
the two tags responsible: overcome-self-doubt and strengthen-your-partnership,
which map 2 courses each and lead one row apiece
```

So it is rare. It is not nothing, and it will be commoner elsewhere: tag
landing pages take three (§6.1) and every tag leads its own page, including the
two above and `learn-hypnotherapy`, which maps a single course.

**What I built, which is a mechanism and therefore mine:** the renderer reads
`kh_tag_order` first, the authored slugs in order, and falls back to `lead_tag`.
Both work today, proved above. `lead_tag` stays exactly as you confirmed it and
§5.7 needs no rewrite.

**What I recommend, one decision:** have the import write `kh_tag_order` too,
since it is the same CSV column split rather than new production work, and it
lets §5.7 be implemented whole instead of in part. If you would rather carry
one field and accept a two-card row on those two book notes and on the thin tag
pages, say so and I will delete the fallback path; the code works either way
and nothing else changes.

## 4. What is still owed before this can ship for real

Nothing renders on any real page until the import runs, because no row carries
either field yet. The import mapping is DSRD 2 §6.1's and is on your list for
S255 along with the §5.7 paragraph, which I have read in its written form and
built against.

Commit `2feb30c`. Live: https://achologytest.com/learn/psychology/book-notes/mans-search-for-meaning/

*No em or en dashes in this file; checked before writing.*
