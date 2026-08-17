**DISPOSITION (S280, Chat):** acknowledged. Helper and absent-portrait report shipped at v0.63.6; nothing blocks. The card wiring stays uncommissioned until the featured book note card's own sitting, and the report stands as the acceptance test for the book note column pass. Archived.

# REPLY: the book author portrait helper is built, and its absences are countable

**DOCUMENT TYPE:** reply, answering a confirmation. **From:** Claude Code, Session 061. **Date:** 17 August 2026. **Theme:** v0.63.6, deployed.
**Answers:** `CONFIRMATION__Book_Author_Portrait_Route_Approved_S278.md`, items 1 and 3. Item 2 is yours.

---

## Item 1: the helper

`achology_book_author_photo( $slug )`, in `knowledge-hub-setup.php`. It mirrors `achology_person_photo()` exactly, as the confirmation required: the stamped asset path when the file exists, `''` when it does not, so a missing portrait falls through to the DSRD 8 section 6.5 designed panel rather than breaking a card.

The route is `/images/book-authors/{author_slug}.webp`. The folder exists and carries its own note saying what goes in it and, more importantly, what does not.

**Proved on the live site rather than reasoned about**, all four branches:

| Given | Returns |
|---|---|
| a slug whose file exists | `.../images/book-authors/viktor-frankl.webp?v=0.63.6` |
| a slug whose file does not | empty |
| an empty slug | empty |
| `../../wp-config` | empty |

The last one is not decoration. The slug arrives from imported data, and a helper that concatenates it into a filesystem path without cleaning it is a path traversal waiting for a badly formed CSV cell. `sanitize_title()` neutralises it, and the test is recorded here so the guard is known to work rather than assumed to.

**The version stamp is on it from birth.** That is the S060 lesson applied forward rather than repeated: `achology_person_photo()` was the one image URL in the theme without a stamp, and the cost was Kain replacing eleven portraits, the new files serving correctly, and every browser keeping the old ones with nothing to indicate anything was stale.

**One thing I did not do, and it is deliberate.** Nothing is wired into a card. The confirmation commissioned the helper and the report; the featured book note card's portrait slot belongs to its approved prototype, which is yours. Say the word and the wiring is a small job, but it is a component change and it should travel as one.

## Item 3: the absent-portrait report

`tools/absent_book_author_portraits.py`. It reads every published book note on the live site, takes the slug each record actually carries, and prints what has a portrait, what does not, what carries no slug at all, and any file in the folder that no note asks for.

**It never derives a slug**, and that is the point rather than a shortcut. You ruled the slug into the import precisely because derivation fails silently on accents, initials and suffixes. A report that derived its own would be measuring a different set from the one the site looks up, and would go green while the site showed nothing.

**First run, tonight:**

```
book notes published:      1
distinct authors with one: 0
distinct authors without:  1
notes carrying NO slug:    0

MISSING
  viktor-frankl.webp    Viktor Frankl    1 note(s)
```

That is the whole live corpus today. The number becomes meaningful when your column pass lands and the 601 import.

## What I need from you

Nothing to unblock this. Two things worth knowing when the import runs:

1. **The report is the acceptance test for your column pass.** If `notes carrying NO slug` comes back above zero after the import, the column did not reach every row, and it will say so by count rather than by anyone spotting a blank card.
2. **The orphan list is the other direction.** Files produced under a slug that later changed show up as asked for by nobody, which is the failure that would otherwise sit undetected in a folder for months.

*No em or en dashes in this file; checked before writing.*
