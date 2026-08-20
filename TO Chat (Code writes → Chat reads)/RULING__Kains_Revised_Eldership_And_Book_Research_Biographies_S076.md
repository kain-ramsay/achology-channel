> **DISPOSITION (Chat S297): read, and one live decision put to Kain at this session's close.** The ruling itself is a record of work already applied and deployed at v0.80.0; nothing in it needs action from Chat. The one open item is Benjamin Lockwood's `line` field, which still reads "distilling each catalogued book" while his rewritten `bio` drops "catalogued". Code correctly declined to edit copy Kain did not give him. Put to Kain at the S297 close with a recommendation to match the two. **This file stays in TO Chat only until he answers that one question.** The lower-case "achology students" correction on Jonathon's line is accepted as written; it matches the business name's capitalisation everywhere else and Kain can overturn it.

# RULING: Kain rewrote the six eldership biographies and Benjamin's, in session

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14. Not a page spec.
**From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Supersedes:** the six biographies in `BRIEF__The_Six_Eldership_Biographies_S296.md`, which were placed earlier the same day and are now replaced by the wording below.

---

## What happened

The S296 brief's six biographies were applied and deployed. Kain then read the rendered page in Safari and rewrote all six, plus Benjamin Lockwood's, giving the new wording directly in the sitting. Applied and deployed at v0.80.0.

**Two changes run through all six eldership entries:**

1. **Each opens on the person's full name**, not their first name. "Alec is a Master Achologist" becomes "Alec Wells is a Master Achologist", and so on for all six.
2. **"Personal development" is named explicitly** in the work each of them does, placed differently in each line rather than dropped in mechanically.

**Gabriele's also drops the bracketed (Gaby).** The S296 brief specified "Gabriele (Gaby) is a Master Achologist" with Gaby in brackets at first mention; his rewrite reads "Gabriele Tzeschlock is a Master Achologist". Her `name` field still reads Gabriele Tzeschlock and the array key is still `gaby-tzeschlock`, both unchanged.

**Benjamin Lockwood's** book-research biography drops the word "catalogued": "distilling each catalogued book" becomes "distilling each book".

## The six, as they now read

**alec-wells**
Alec Wells is a Master Achologist and one of Achology's community elders, with thousands of hours of personal development workshops and training behind him. He hosts events, mentors members through the practical side of their learning, and helps verify the record of practice other members build.

**andrew-nelson**
Andrew Nelson is a Master Achologist and one of Achology's community elders, having delivered thousands of hours of workshops and personal development training. He hosts community events and works alongside new Achology members as they figure out how to put their learning into practice.

**erika-nadeau**
Erika Nadeau, a Master Achologist and experienced Achology community elder, has conducted thousands of hours of workshops and training. She organises personal development events, mentors members in their practice, and helps verify their submitted learning activities as an accreditation verifier.

**gaby-tzeschlock**
Gabriele Tzeschlock is a Master Achologist and one of Achology's community elders, with thousands of hours of workshops and training to her name. She hosts community events, mentors members through their own personal and professional development, and helps verify the record of work they put forward.

**gary-kennedy**
Gary Kennedy is a Master Achologist, former priest, and one of Achology's community elders, having delivered thousands of hours of personal development workshops and training. He organises events, assists Achology members with their learning processes, and helps validate their record of practice.

**jonathon-frost**
Jonathon Frost is a Master Achologist and one of Achology's community elders, with thousands of hours of workshops and training behind him. He hosts personal development events, mentors members, and hosts regular weekly mentorship for Achology students who want to develop expert coaching skills.

## Benjamin Lockwood, as it now reads

Benjamin leads Achology's book research, distilling each book into a clear, honest overview of what it offers and where it falls short. He reads widely across psychology, philosophy, and personal growth, and writes for the curious reader who wants a book's core idea in five minutes, not a lecture. Every note is a fair, careful survey of an author's thinking.

## One mechanical carry-over, named rather than made silently

**Jonathon's line was pasted with "achology students" in lower case.** It is written as "Achology students", matching the S296 brief's own correction of the same word in the same sentence and the business name's capitalisation everywhere else on the site. **Overturnable by Kain**; nothing else in his wording is altered.

## One thing left alone, and it is now out of step

**Benjamin's `line` field still reads "distilling each catalogued book into a clear, honest overview."** The `line` is the one-sentence form the author signature block renders on his book notes, and Kain's rewrite covered the `bio` only. Rather than edit copy he did not give me, it is left as it is and raised with him. **The six eldership `line` fields are untouched**, per the S296 brief's own instruction.

## Two S296 instructions now closed by this

Both were carried out before the rewrite and stand: the unapproved-copy warning block is gone from `people-setup.php`, and Gabriele's photograph resolves (the lookup reads the unchanged array key, confirmed rather than assumed).

**Part Two of the S296 brief, the links field, was built and then removed** when the withdrawal was read. Nothing of it remains.

*No em or en dashes in this file; checked before writing.*
