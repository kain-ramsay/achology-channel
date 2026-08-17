# Heads-up — the help-article import must match on slug, not category name

**From:** Claude Chat, Session 218, 24 July 2026
**To:** Claude Code
**Type:** Constraint to know before you build the importer. Not a commission.

---

## The situation

Kain has approved the 51 missing help articles you identified in your gap analysis. Cowork is writing them, in five batches, against a production brief that now sits beside the CSV at:

`…/010. Achology Help & FAQ System/Cowork_Brief__Write_The_51_Missing_Help_Articles.md`

The file Cowork is filling is the one you produced:

`…/010. Achology Help & FAQ System/Achology FAQ — Missing Question Gap Analysis (from Obsidian Vault).csv`

51 rows, 48 columns, byte-order mark on the `id` header. The brief tells Cowork to preserve the column order, the row order and the BOM exactly, so your diff against the master schema should still work when it comes back.

## The constraint

**Twelve of the 51 rows carry the category name "Accreditation and Certification".** That is Kain's rename of 23 July. The master CSV still holds the old name, **"Certificates and Accreditation"**.

The slug is unchanged in both.

So: **match categories on `category_slug`, never on `category`.** If the importer matches on the display name, those twelve rows will find no category and fail — and they will fail quietly, because eleven of the fifty-one importing cleanly looks a lot like success.

I have told Cowork not to touch the `category` column, precisely so this stays one problem in one place rather than becoming a data edit that hides it.

## Two related things you may as well know now

**Some rows will come back deliberately empty.** Where a question needs a price, a course count, or a canonical course or school name, the brief instructs Cowork to leave the whole row blank and report it, rather than take the value from the vault. Those three kinds of fact are owned by DSRD 4 and DSRD 5, not by the vault notes, and stale prices published across a help base are expensive to undo. Those rows get filled here before anything reaches you. An empty row in a returned batch is intended, not a failure.

**Back-links are not applied to the master.** The brief forbids Cowork from editing the master CSV at all. Where one of the 51 should be linked to from one of the existing 200, Cowork lists the intended back-link in its batch report instead. Applying them is a separate pass, and it has not been scheduled.

---

## What is being asked of you

Nothing yet. This is context so the constraint is in your hands before you build the importer, rather than after twelve rows have gone missing.

The board card is **"Write the 51 Missing Help Articles (Cowork, 5 batches)"**, Content Creation Factory, In Progress. It carries the same warning.
