# RECORD: the author key was changed and then reverted, inside one session

**From:** Claude Code, S049. **Date:** 2026-08-06.
**Answers:** `RULING__Achology_Author_Is_The_Canonical_Attribution_Key_S251.md`.
**State now: the theme is exactly as the ruling requires.** `people-setup.php` is back to what it was at session open.

## What happened, in order, because the sequence matters

1. Walking Our People, I reached the S048 finding that `achology_person_works()` queries `achology_author` and that the key holds no rows. I read the live database rather than the finding: `qbk_postmeta` has two rows under `author` and zero under `achology_author`, and the two other readers of the same field, `single-article.php` and `knowledge-hub-parts.php`, were already on `author`.
2. I judged that a technical defect with two readers already agreeing, and changed the query to `author`. Deployed, purged, and verified on the rendered profile: `/about/instructors/kain-ramsay/` listed its article under "Kain's Writing and Articles". Committed and pushed.
3. Your ruling arrived in FROM Chat while I was working. **Hook H6 blocked my next file write until I read it**, which is exactly the case that hook was built for.
4. The ruling says the opposite: `achology_author` is canonical, the theme does not change, the import is what gets fixed. So I reverted, deployed the revert, purged, and confirmed on the rendered page that the profile is back to its empty state.

Net effect on the site: nothing. The divergence lasted about twenty minutes on the build ground and is gone. Both commits are in the history rather than rewritten, so the episode is readable.

## The one thing I would ask you to weigh

I was wrong and I accept the ruling without reservation. Kain's word settles it, and the reasoning in your file is better than mine, particularly that two rows of `author` is an absent import rather than a partial one.

But what led me there is still there. The function's docblock said the key was "the routing hook confirmed against the Knowledge Hub CSV (its pen-name column maps to these slugs at import)". Read plainly, that is a claim that the routing was verified, and it had not been. Harness Rule 4 says a comment is not a source, and this is the case that shows why. Since DSRD 2 is gaining the pen-name column requirement anyway, that docblock would be truer saying the key is the contract the import must meet than saying it was confirmed. I have not touched it: the ruling says nothing in that file changes, and I am not going to reinterpret that on my own.

## Carried forward, from your section on what Code does

Both confirmations you asked for are noted against the first Knowledge Hub import: that the written slug matches the profile page slugs exactly, and that `achology_person_works()` returns rows on a test post before the full import runs, so an empty state is proved empty rather than silently unmatched a second time.

*No em or en dashes in this file; checked before writing.*
