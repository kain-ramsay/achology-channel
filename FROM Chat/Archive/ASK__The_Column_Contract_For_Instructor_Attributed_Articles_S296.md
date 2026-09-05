# ASK: the exact column list for an instructor-attributed article import

**From:** Claude Chat, Session 296. **Date:** 20 August 2026.
**This is a question, not a commission.** Nothing is being asked to be built. Read-only.

---

## What is coming, so the answer can be the right shape

Kain has commissioned eighteen instructor-attributed articles, nine in Kain Ramsay's voice and nine in Prof. Gerard Egan's. First-person reflective pieces, 1,200 to 1,500 words each, teaching from inside the instructor's own methodology. The standard is DSRD 2 section 3.7.

They will arrive as one CSV for import through WP All Import, the same road the 249 help articles took.

## Why this is a question rather than a guess

The upload-CSV standard holds a defined column contract for the help section only. Instructor-attributed article sits in its register of content types still to be defined, and that register's rule is explicit: a content type's true column list is decided by the fields you actually built for it, so it cannot be invented on this side. Guessing it would put column questions to Kain that the build has already answered, which is the exact waste the standard exists to stop.

## What is being asked

**One: the exact column list** the `article` post type needs on import, in order, as you would want to receive it.

**Two: which columns are filled, which are blank by design, and which the import generates.** The help section's answer was that Rank Math owns the SEO title, description, canonical, social tags and schema, so those columns ship blank. If the same is true here, say so and they will ship blank.

**Three: the author field, which matters more here than anywhere else on the site.** The people registry's `achology_person_works()` finds a person's published work through the `achology_author` meta field, matched on their slug. So these eighteen rows carry `kain-ramsay` and `gerard-egan`, and if the field name or the matching value is anything other than that, the articles will not appear on either instructor's profile page and nobody will notice until somebody looks.

Please confirm the field name and the exact value format, read from the theme rather than recalled. There is a note in `people-setup.php` saying this key was once assumed confirmed when it was not, changed, and then reverted.

**Four: the category and tag columns.** Which taxonomy, matched on slug or on name, and whether an unmatched value fails the row loudly or silently. The help-section answer was to match on slug, because a category can be renamed while its slug holds.

**Five: anything the article template reads that a CSV must supply**, that the four questions above would miss. The author card, the related-reading blocks and the schema all pull from somewhere, and this side cannot see where.

## What happens with the answer

It is recorded as a defined contract in the upload-CSV standard, so the next article CSV is built to a looked-up standard rather than rediscovered. Then the eighteen rows are built to it and verified column by column before anything is handed over.

**No rows are drafted against a guessed contract in the meantime.**

*No em or en dashes in this file; checked before writing.*
