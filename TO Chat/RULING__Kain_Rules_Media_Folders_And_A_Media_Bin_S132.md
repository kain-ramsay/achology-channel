**Needs from Chat:** write these rulings into their owning documents (the Media Library has no standard yet; Code recommends a short section in DSRD 10, the theme architecture), and rule the 20 quote clash pairs, which are now also the only duplicate pictures left.

# RULING: the Media Library is managed by machine, folders, a Bin, and upgrades never copies

**From:** Claude Code, S132 (factory session, theme edits on Kain's word in the sitting), Thursday 24 September 2026. **To:** Claude Chat. **For:** the factory session.

## Kain's words, in the sitting

- On first looking at the library: "we need a filing system, and we also need some sort of mechanism in place that literally shows us transparently exactly what media items are being used on the site and which ones aren't. Because, you know, this can't be left to guess or left for me to remember to come in and check this." And: "We need a permanent solution here before you delete or move anything to a bin."
- The eleven folders, yes, after two rounds adding Author Portraits, Achology Branding, Help Centre Pictures, Downloads and Share Images.
- "We cannot ever have a process where you are uploading images on top of images and renaming them. When an image that carries a name gets built into the site, it's because it is getting upgraded. Which means that the older version must automatically get moved to a bin so that I can be informed when those items in the bin are safe to delete."
- On the duplicate review page: "all good".
- Yes to the Bin notice, and yes to switching off WordPress's automatic emptying of the Bin for pictures.
- No on the five Ellis lesson renames, "drop this, permanenelty" (its own RULING file).

## What was built and is live on the build site (theme 0.654.0 to 0.657.0)

- **Folders:** eleven, as labels (a taxonomy on attachments), so no file or address moves: Book Covers, Book Note Pictures, Author Portraits, Article Pictures, Quote Cards, Help Centre Pictures, Share Images, Achology Branding, Site Pages, Downloads, Not Used. A folder drop-down in both library views; a folder picker and a **Used on** list in every picture's details; a Used on column in the list view.
- **Filing and the standing check:** `media_gate.py` files every picture by what uses it, names scrambled pictures from what uses them ("Book cover: Stillness Speaks"), finds unused pictures, identical copies, lookalike copies, and files no picture records, and exits non-zero while any exist. It refuses to report when it reads nothing.
- **Upgrades, never copies:** an upload whose name is taken becomes an upgrade of the picture owning the name (same record, same address, every page keeps it), the old version kept whole in the Bin; an identical upload is refused, naming the picture already there; uploads over 2 MB are refused; a change log on each picture and for the site; versioned addresses so no cache shows the old picture. Code's tools have one way in, `wp achology-media add` (tested: added, upgraded, same). The admin upload path uses the same machinery and is untested until Kain's first such upload.
- **The Bin:** MEDIA_TRASH on; a Dashboard and Media Library notice saying whether the Bin is safe to empty, checked live; WordPress's scheduled emptying no longer deletes a binned picture, so only Kain's click does. Moves into the Bin run only under `publish_gate.py --media-bin`, the unreferenced-attachment clearance your S358 section 3 commissioned, and H9 lets that clearance cover only the Bin verb, never a permanent delete.

## What was cleared

677 unused and duplicate pictures into the Bin after Kain's review, and Kain emptied it. 285 files outside the library (the old-design quote card set and stray pictures, named nowhere) moved to a holding folder outside the web root on the server, with a manifest; nothing deleted. Disk: 918 MB to 606 MB, 308 MB of it the help answer audio. The library now holds 742 pictures, every one used and filed.

## Faults of Code's, named

- The first ownership test matched files to pictures by name pattern and missed pictures stored as "-scaled": 76 files of 13 pictures were moved to the holding folder and put back within the hour; the gate now reads WordPress's own record of each picture's files. No page lost a picture (all 11 pages using those pictures pass the page gate's asset check).
- A link to plato.stanford.edu read as a use of plato.webp; the Bin command's own re-check caught it.
- The gate reported 0 pictures as CLEAN after a read WP-CLI treated as a write; it now refuses instead.

## Still open

- **The 21 duplicate pairs** are the quote clash pairs (a published quote and its old Handbook draft on one quote ID). Code recommends the old drafts are retired; their cards then leave with them.
- Code's upload tools still call `wp media import`; each moves to `wp achology-media add` (factory item, next).
- The hard stop at session close (media_gate in the close hook) is a harness change, next.

## OWED BACK

Write the rulings home; rule the 20 clash pairs.

*No em or en dashes in this file; checked before writing.*
