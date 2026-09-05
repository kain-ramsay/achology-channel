# RULING: `achology_author` is the canonical attribution key. The import fills it.

**From:** Claude Chat, S251. **Date:** 2026-08-06.
**Closes:** `FINDING__No_Article_Can_Attribute_Itself_To_A_Profile_S048.md`.
**Authority:** Kain, in session, S251.

## The finding, in one paragraph

`people-setup.php` builds each profile page's "writing and articles" list with
`achology_person_works()`, which queries posts carrying the person's slug in the
meta key `achology_author`. Queried on the live database at S048: `achology_author`
returns zero rows. The key that exists is `author`, carrying two rows, both
`kain-ramsay`. So every one of the ten profile pages renders its empty state, and
would keep doing so forever whatever gets imported later, because the query it
runs can never match.

## The ruling

**`achology_author` is the canonical key.** It stays as it is in the theme. Nothing
in `people-setup.php` changes.

The fix belongs to the import, not to the theme: every Knowledge Hub content type
that carries a pen name writes that pen name's slug into `achology_author` at
import. The two existing `author` rows are legacy and are migrated to
`achology_author`, not preserved alongside it.

**Why this way round rather than renaming the key in the theme.** The theme is
the thing ten pages already depend on, and the docblock's assumption is the one
the whole profile-page design rests on. Two rows of `author` is an absent import,
not a partial one, so there is no body of data to preserve. Changing the key in
one function would leave the field name meaning nothing to a reader; changing the
import leaves the site self-describing.

## What this obliges

1. **The column contract for every Knowledge Hub upload CSV carries the pen-name
   column, and its import mapping writes `achology_author`.** This is now a
   required column, not an optional one. Recorded in DSRD 2.
2. **The two legacy `author` rows are migrated** to `achology_author` with the
   value `kain-ramsay`, and the `author` key is retired.
3. **The book note upload CSV must carry it**, since Benjamin Lockwood's profile
   page is one of the ten and book notes are his work. Named in the book note
   developer brief.

## What Code does with this

Nothing yet, beyond knowing it. There is no bulk write to run while there is no
attributed content to write. The obligation lands the moment the first Knowledge
Hub import runs, and it is carried in that import's brief rather than as a
standalone job.

Two things worth confirming back through the channel when the first import is
built:

- that the slug written matches the profile page slugs exactly, as recorded in
  `RECORD__Pen_Name_Bios_And_Slugs_S048.md` (for example `benjamin-lockwood`,
  not `Benjamin Lockwood`)
- that `achology_person_works()` returns the expected rows on a test post before
  the full import runs, so the empty state is proved to be genuinely empty rather
  than silently unmatched again

*No em or en dashes in this file; checked before writing.*
