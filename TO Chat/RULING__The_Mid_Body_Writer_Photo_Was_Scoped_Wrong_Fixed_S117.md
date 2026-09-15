# RULING: the mid-body writer photo was firing on the wrong article types. Fixed and deployed.

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Found by Kain**, reading "Who Was Albert Ellis?" live and seeing Charlotte J. Avery's photograph in the middle of the writing.

---

## What was wrong

`single-article.php`, the S116 change that put the writer's photo into the body: Kain's ruling that session named "the instructor articles and also Karen's articles" only. The code built that session checked only whether the article's `author` field resolved to a real person, which is true of every article type that carries a byline, not only the two Kain named.

**167 published pages carried it before this fix: 51 author-biography pieces, 116 field-authority pieces.** Each was showing a photograph of Benjamin Lockwood, Charlotte J. Avery, Evelyn Montgomery or Declan Fitzpatrick, the editorial team, inserted into the middle of writing that was not theirs to illustrate that way.

## The fix

One condition added: the block now checks `article_type === 'instructor-attributed'`, which is the value both the instructor articles and Karen's twelve share, and no other type carries. Theme version 0.426.0, deployed and confirmed against the server.

## Verified on the live site, not assumed

- `learn-about-the-psychologist-dr-albert-ellis` (the page Kain found): the mid-body photograph is gone. Charlotte J. Avery's name and photograph remain only in the footer signature card, which is correct on every article regardless of type and always has been.
- `what-makes-a-good-leader` (Karen, instructor-attributed): the mid-body photograph is still there, unchanged.
- `aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology` (author-biography, a second affected page): confirmed clean.

## What this does not touch

The footer signature card, on every article, showing who wrote it. That is correct and separate, and nothing about it changed. Book note author portraits are unaffected: a book note's author field names the book's real author, which is a different, correct use of the same shared drawing function.

---

OWED BACK: nothing. Recorded here so DSRD 9 section 22.7 (or wherever S116's ruling was written home) can note the correction.

*No em or en dashes in this file; checked before writing.*
