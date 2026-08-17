# RECORD: the asset folders are reorganised. Here is the new shape.

**Written S252 by Claude Chat. Date: 2026-08-07.**
**Answers your `ANSWER__Asset_Folder_Paths_S050.md`, and tells you the two paths you asked for.**

## The moves are done

`000. www.achology.com | All Website Assets` went from five top-level folders to three.

```
000. www.achology.com | All Website Assets/
   01. The Achology WordPress Theme        unchanged, same path, untouched
   02. Website-Wide Assets
   03. Achology Website Pages
```

`04. Single Page Template Assets` and `05. Website Images (High-Res MASTERS)` no longer exist. `03. Como The Achology.com Font` no longer exists. Kain deleted the two empty shells himself once everything was out.

## The two paths you asked for

**1. `book-note.css` line 26.** The bookshelf master is now at:

```
000. www.achology.com | All Website Assets/03. Achology Website Pages/Knowledge Hub Design Prototypes/Book Note Page/Page Images/Bookshelf Image | Book Notes.png
```

**2. `single-book_note.php` line 6.** Your assumption was right, the page folders kept their names inside the rename:

```
000. www.achology.com | All Website Assets/03. Achology Website Pages/Knowledge Hub Design Prototypes/Book Note Page/
```

Correct both when a change set legitimately touches those files. Nothing is broken meanwhile; they are comments.

## The rule the folder now runs on

Every file answers three questions, in order, and the first yes decides:

1. Does it belong to one page? It lives in that page's folder, inside `Page Images`.
2. Does it belong to the whole website? It lives in `02. Website-Wide Assets`.
3. Is it not a website asset? It leaves the folder entirely, for `007. Spreadsheets | Data | CSV Files`.

Where one template serves many items, the items' images live in that template's page folder. The 28 course images are in `Course Page/Page Images`, the school images in `School Page/Page Images`, the 12 portraits in `Our People Page/Page Images`.

The full record is at `000. www.achology.com | All Website Assets/000__HOW_THIS_FOLDER_WORKS.md`, which is that folder's README and the canonical description of it. Read it there rather than trusting this note, which is an announcement.

## Three things that concern you directly

**1. `qc_gate.py` moved.** It is now at `007. Spreadsheets | Data | CSV Files/Help + FAQ Data/Working/qc_gate.py`. You confirmed nothing calls it by path. Your three wired gates (`css_gate.py`, `page_gate.py`, `health_check.py`) live in the theme and did not move.

**2. `countries-110m.json` now exists, and it is not where your instruction says.** You flagged that `INSTRUCTION__Reviews_Page_Build_With_Kain.md` section 4 commissions it into a folder that was about to vanish. Good catch. The file was already present and has been moved to:

```
007. Spreadsheets | Data | CSV Files/Reviews Page Data/countries-110m.json
```

Read it from there. Do not fetch it again, and treat that instruction's section 4 destination as superseded by this note.

**3. Five portrait filenames were corrected.** The masters still carried the pre-S048 slugs. They now match the live profile URLs: `amelia-a-sinclair`, `charlotte-j-avery`, `frederick-s-martin`, `isabella-s-whitmore`, `jackson-p-hartley`. All twelve portraits are in `Our People Page/Page Images`.

## What was not deleted

Duplicates were resolved to one home and the spare copy archived rather than destroyed. The ten policy share images existed in both dissolving folders under identical names and byte sizes; the spare set is in `Policy Page/Archive`. The testimonial transcripts existed twice; the spare is inside the `007` folder. Zip files that duplicate the loose files beside them were moved into `Archive` subfolders, not removed.

*No em or en dashes in this file; checked before writing.*
