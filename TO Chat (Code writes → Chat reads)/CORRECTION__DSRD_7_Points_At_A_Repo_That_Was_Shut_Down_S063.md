# CORRECTION: DSRD 7 names a master library that was shut down months ago

**DOCUMENT TYPE:** correction. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Corrects:** DSRD 7 section 12.2, the Course and School Image Registry.
**Authority:** Kain, in session, told plainly: **"we shut down that repo months ago! The DSRD is stale."**
**Supersedes half of:** `NOTE__The_Lockup_Needs_A_Registry_Entry_And_The_Master_Library_Is_Missing_S063`, filed an hour ago, which reported the library as missing and asked whether it had moved. It had not moved. It is gone.

---

## The stale sentence

DSRD 7 section 12.2 opens its registry with:

> "Master library: `~/Documents/GitHub/website-assets/website-images/`. Every set exists in both PNG and SVG."

**That repository was shut down months ago.** There is no `GitHub` folder in `~/Documents` on this machine and nothing named `website-assets` anywhere beneath it.

**Both halves of the sentence are wrong, and the second half is the dangerous one.** "Every set exists in both PNG and SVG" is stated as a fact about a location that no longer exists, so it cannot be checked by anyone and it reads as a guarantee. Anything downstream that assumed an SVG master was available assumed it on the strength of that line.

## Where the masters actually are now, read from the disk this turn

There is no single library any more. The sets live where the work that uses them lives:

| Asset | Where it actually is |
|---|---|
| Course images, all variants, PNG and SVG | `03. Achology Website Pages / Academy + Courses Design Prototypes / Course Page / Page Images / Course Images (all variants)` |
| School images, all variants, PNG and SVG | `03. Achology Website Pages / Academy + Courses Design Prototypes / School Page / Page Images / School Images (all variants)` |
| Know Your Psychology lockups, and the vector master | `02. Website-Wide Assets / Know Your Psychology Logos` |
| Achology logos, favicons, the bubble, Como | `02. Website-Wide Assets`, one folder each |

So the registry's *contents* are sound and its *address* is not. Every set in the table still exists; the line telling a reader where to find them points at nothing.

## What I am NOT doing

**I am not editing DSRD 7**, per Harness Rule 8: corrections travel to Chat as instruction files. This is that file.

**I am not proposing a new single library either.** Consolidating four locations into one is a real decision with real consequences for every path already written down, and it is Kain's, not a tidy-up to be slipped into a correction.

## What section 12.2 needs, minimally

1. **The library line replaced** with the four real locations above, or with a statement that assets live beside the work that uses them, whichever matches how Kain intends to work.
2. **The "every set exists in both PNG and SVG" claim removed or verified.** It cannot be true of a folder that does not exist, and I have not checked format coverage set by set. If that guarantee matters to anything, it needs measuring rather than restating.
3. **A dated note that the repository was retired**, so the next person who finds an old path in another document knows why it fails rather than hunting for it. I would expect this path to appear elsewhere.

## The thing worth taking from this beyond the one line

**A specification that names a location cannot verify itself, and this one had gone stale silently for months.** Nobody was at fault: the repo was retired for good reasons and the document simply was not walked afterwards.

It is the same shape as the dead channel last night. **A path that no longer resolves looks exactly like a path nobody has needed lately.** If it is worth a check anywhere, it is worth one wherever a DSRD states a filesystem location as fact, and that is a small mechanical sweep rather than a judgement: every path in every DSRD, resolved or not resolved, once. I can run it and report, on your word or Kain's.

*No em or en dashes in this file; checked before writing.*
