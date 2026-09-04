# ASK: book_note_import.py hits the same register gap as item 1 of the S099 ASK, and its unhardened form was worse

**From:** Claude Code, Session 100. **Date:** 4 September 2026. **Session type:** factory.
**Under:** Harness Rule 5 and The Shared Rules section 3. Kain's ruling this sitting is the articles backlog and nothing else; this is filed rather than decided here.
**Board cards:** the harness card; the 75 not-live book notes.

## The fact, read this turn

`h9_reviewed_scripts.json`'s own `_how_to_add_one` says: satisfy yourself a script "cannot create or publish a post". The register's own note on `import_instructor_articles.py` says plainly that sentence does not cover a script that creates, even as a hardcoded draft, and that widening it is yours, not mine. That question is already filed, open, in `ASK__Four_Things_Are_Blocked_And_None_Of_Them_Is_Mine_To_Decide_S099.md`, item 1.

`tools/book_note_import.py` is the script named in this session's own plan to clear the 75 not-live book notes. It lives inside the theme's `tools` folder, so `reviewed_scripts()` can actually find it (unlike the instructor importer, which is inert today). Reading its full install-reaching payload this session, as the register requires, found it fails the bar in a way the instructor importer does not:

    f"--post_status={row['post_status'] or 'publish'}",

This is not hardcoded. It is read from the row, and defaults to `publish` where the row is empty. Checked against the actual records rather than assumed: some book note records on disk genuinely carry `post_status: publish`. Run as written, `--push` would create AND publish real pages for those, with no Rank Math score and no `publish_gate.py` clearance. That is the exact thing the H9 publishing wall exists to stop, and it is a step past the instructor importer's case, which creates only drafts.

## What I did about it, and what I did not

I hardcoded the status to `draft`, matching the pattern already read and ruled safe for `import_instructor_articles.py`: no input can make it publish. Committed to the theme repo, `9cfc40c`. This is a technical safety fix and mine to make.

I did not add an entry to `h9_reviewed_scripts.json`. Hardened or not, it still creates, and the register's own sentence still does not cover that case. Adding the entry anyway would be deciding the S099 question myself rather than waiting for your ruling on it, which is the one thing Rule 5 says not to do.

**The sha256 of the hardened file, for whenever you rule item 1:** `f1742f3074ce977033bcecdf106c828fb2b4f144fea34106b1c5d03e54ef9a8c`

## What this actually blocks

Not only the push. `h9_publishing_wall.py`'s ground B scans the whole file's text for a write marker before deciding whether the wall lets it run at all, so even `--plan` and `--write`, which touch no install and only read records and write the local master spreadsheet, are blocked by the same lookup until the script is registered. The 75 book notes cannot move at all, plumbing or otherwise, until item 1 is ruled.

**Unblocked by:** the same ruling as S099 item 1, both halves, now covering two scripts rather than one. **Testable fact:** `reviewed_scripts()` returning `book_note_import.py` for the hash above.

---

OWED BACK: a ruling on S099's item 1. Nothing else in this file needs a separate answer.

*No em or en dashes in this file; checked before writing.*
