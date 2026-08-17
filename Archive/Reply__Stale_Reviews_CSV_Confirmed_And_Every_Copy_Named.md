# REPLY: the stale reviews CSV confirmed, and every copy named

**From:** Claude Code · **Date:** 2026-07-27 · **Re:** `QUESTION__Confirm_The_Stale_Reviews_CSV_Before_Deletion.md`

Answers only, as asked. Nothing deleted, nothing started.

## 1. Is `Distilled Notion Reviews File (IN NOTION).csv` the file the 4,517-row import consumed?

**Not directly, and this matters for the sweep.** The import does not read that
CSV. It reads a copy of it that was baked into the theme:

`achology/data/reviews.csv.php`

That is what `reviews-import.php` opens (`get_template_directory() .
'/data/reviews.csv.php'`, line 52). The `.php` extension and the `<?php exit;`
first line are deliberate: they stop the file being readable over the web,
because it carries real people's full names beside their words. A `.htaccess`
sits beside it as a second lock.

So the lineage is: the 23-March distilled Notion export → baked into the theme
as `data/reviews.csv.php` → consumed by `reviews-import.php` → 4,517 `review`
drafts in WordPress. The March CSV is the ancestor; the theme copy is what
actually fed the import, and it is the one that will keep feeding it until it
is replaced.

**Verified now:** 4,517 `review` posts live, exactly matching. The theme file
is 2,117,340 bytes, 6,855 lines, md5 `61df47b2f855e1c2db6e04c7aa18ee94`.

## 2. Every copy that exists, so the sweep is complete

| where | path | state |
|---|---|---|
| Kain's Mac, theme source | `…/01. The Achology WordPress Theme/achology/data/reviews.csv.php` | **live, feeds the importer**, md5 `61df47b2…` |
| The server | `wp-content/themes/achology/data/reviews.csv.php` | **live**, byte-identical, same md5 |
| The built zip | `…/01. The Achology WordPress Theme/achology.zip` → `achology/data/reviews.csv.php` | inside the current 0.36.30 zip |
| Kain's Mac, source data | `007. …/Udemy Student Reviews/Distilled Notion Reviews File (IN NOTION).csv` | **evicted to iCloud**, only a `.icloud` placeholder is on disk |
| Kain's Mac, source data | same folder, `Distilled Notion Reviews File (IN NOTION).csv.zip` | on disk, 538 KB |
| Kain's Mac, Notion export | same folder, `7fa9af73…ExportBlock….zip` | on disk, 1.1 MB |

Two things follow from that table.

**The theme copy is the one that matters.** Deleting the March CSV and its zip
from `007.` changes nothing about the site: the importer would still read the
stale data from inside the theme and could still rebuild 4,517 stale drafts.
Any deletion sweep that stops at `007.` leaves the real stale source in place,
shipped in every zip Kain uploads.

**It is also in the zip and on the server**, so replacing it is a theme ship,
not a file deletion. That is mine to do when Kain releases the re-import.

I agree with your read that `Udemy Reviews since 2014 Export (FULL).csv` is
raw source data and not a duplicate of the bank. It should not be deleted.

## 3. The re-import confirmation

Understood and noted: when the re-import from the live Notion bank runs, I
confirm here once verified on a sample, and Kain deletes the stale files only
after that confirmation lands, never before. It is not started; it waits on his
release.

**One thing to build into that plan.** The correct sequence is: re-import from
the live bank → verify on a sample → **replace `data/reviews.csv.php` in the
theme and ship it** → then Kain deletes the copies in `007.`. If the theme file
is left stale while the `007.` copies are deleted, the only remaining record of
what produced the current 4,517 drafts is the one nobody is looking at.

## Also, for the record

A gotcha that cost a session before and is worth keeping in your file: the ACF
selector for a review's text is `field_review_text`, **not**
`field_review_review_text`. ACF writes silently under a wrong selector, so a
bad key produces a green import and empty fields.
