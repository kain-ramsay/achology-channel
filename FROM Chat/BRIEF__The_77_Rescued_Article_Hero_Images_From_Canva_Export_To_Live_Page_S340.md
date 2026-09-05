> **CODE DISPOSITION, S102: WAITS ON Chat's "records ready" line after Cowork's retag run, for steps 4 and 5 (the media gate on the rendered pages and the import that attaches each hero).** Steps 1 to 3 are done this session, reported in `REPLY__Steps_One_To_Three_Of_The_Hero_Image_Brief_Are_Done_83_Of_83_S102.md`: 84 masters unpacked at 2200 by 1050, 83 renamed to their slugs (one matched on its keywords after Canva mangled the name), 166 WebP derivatives at 680 and 1360 wide in the theme's `images/knowledge-hub/articles/`, none over budget. At step 5 the importer uploads the 2x file as each attachment's original.

> **CODE DISPOSITION, S102: WAITS ON any PNG file existing in the Page Images subfolder of the Article Page design folder, which is Kain's Canva export landing; nothing starts before that by the brief's own words.** Superseded by the line above, later the same session. Read this session, the morning it arrived. Section 5's question is answered in the same session: the field-authority-article importer now exists and attaches each hero at import from the record's own featured_image field, so when the PNGs land the run is rename, convert, gate, import, in that order, and nothing is done twice. Named in `REPORT__The_Two_Missing_Importers_Are_Built_And_Registered_S102.md`.

# BRIEF: the 77 rescued-article hero images, from Kain's Canva export to the live pages

**From:** Claude Chat, Session 340, 5 September 2026.
**Approved by:** Kain, in session, 5 September 2026 ("yes" to the plan and to this brief).
**Status:** commissioned. Nothing to start until the PNG files exist in the folder named in section 3; Kain will say when they do, and Chat will relay it in the channel.
**Board cards:** the Salvage articles card (the rescued field-authority articles), and the Image and icon optimisation card (the machinery this run uses).
**PAGE GATE:** this is not a page build, so no page gate line. The acceptance test is the media gate (`media_gate.py`, all twelve checks) on every file, plus the page gate's image lines re-run on each article's record once its hero is attached.

---

## 1. What is happening, in one paragraph

The 76 rescued field-authority articles in `Content Records/field-authority-article/`, plus the frozen exemplar (the seven levels of human awareness), all name a featured image that does not exist. Kain is making all 77 himself in Canva, in his own Magic Media long-exposure style (orange, cream, taupe, black, grey and white, no words on the picture), the same style as the 15 help-category images and the 18 instructor article images already on the site. He works from one Canva file with one named page per article, exports all pages as PNG in one go, and drops them in one folder. Your job is everything after that: rename, convert, attach, verify.

## 2. The mapping file, and how Canva will name the exports

The one map is `ARTICLE_HERO_IMAGE_MAP_S340.csv`, in `Content Records/field-authority-article/` inside the Content Production Factory folder. Columns: `canva_page`, `slug`, `save_as`, `article_title`, `magic_media_key_words`.

Canva exports a multi-page design as one file per page, numbered in page order (its usual pattern is the design name followed by a page number). **The `canva_page` column is that page number.** Page 1 is not a rescued article: it is the instructor article image the file was copied from ("Why People Seek Help, and What They Actually Need From It"), and is ignored. Pages 2 to 77 map to the 76 records plus the exemplar, in the order the CSV gives.

Rename each export to its `save_as` value: `{post_name}.webp`, exactly as each record's `featured_image` field already reads. Every record was normalised to `{slug}.webp` at S335 and re-checked at S339, so the record and the map agree; if you find one that does not, stop on that one and say so rather than choosing.

The exemplar's record file is `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md`; its slug is `the-seven-levels-of-human-awareness`.

## 3. Where the PNGs will land

The Article Page folder's `Page Images` subfolder, inside the Knowledge Hub pages family of the website assets folder (the folder's own README, `000__HOW_THIS_FOLDER_WORKS.md` at the assets root, is canonical on the route; I created `Page Images` this session as it did not yet exist). The PNGs stay there as masters per DSRD 7 section 12.3: PNG is never a ship format. Only the WebP derivatives go into the theme.

Check each PNG is a real file and not an iCloud placeholder before you read it (the assets README, section 5).

## 4. The standard, and where it is written

Kain's export size is 1760 by 840, the same as the 18 instructor article images you already processed at your S097. **Follow that precedent exactly.** DSRD 7 section 12.1 still says "1200 by 630 JPG" for article banners; section 12.3 (later, S294) says WebP, and every record carries `.webp`. WebP wins by the later standard and by the records; Chat will correct section 12.1's format line at close. If your S097 run cropped or resized the 1760 by 840 export for the 680-wide slot or for the OG image, do the same here and say what you did in the report.

DSRD 7 section 12.3, applied per file:
- WebP, quality 82 (the working value; Kain has not ruled compression by eye, so do not change it).
- Two derivatives, 1x and 2x of the 680 slot, with `srcset` and `sizes` written by the template as it already does.
- Under 200KB at 2x, or recompress and re-export until it is.
- Real `width` and `height` attributes.
- The hero never lazy-loads and carries `fetchpriority="high"`.
- Descriptive filename: the slug, per section 2.
- Alt text: read from each record's `featured_image_alt` field, never written by you and never the filename. Every record carries one, written to the alt rules in section 12.3, and the content gate checks the focus keyword appears in it.
- Listed in the XML image sitemap.
- Emitted as `ImageObject` in the page's Article schema.
- The same image serves as the page's OG image (DSRD 7 section 15.3, Articles row).

Run `image_pipeline.py` and `media_gate.py` as built at your S090: twelve checks, both directions, on every one of the 77.

## 5. Attaching to the pages

The 76 records are not yet imported: the field-authority-article import route was commissioned at S338 (`BRIEF__Build_The_Missing_Import_Route_And_Export_The_220_S338`) and its state is yours to report. If the importer exists when the images land, attach each hero at import from the record's `featured_image` field. If it does not, land the WebP files in the theme's images folder under the slug names and report that the attach step waits on the importer, so nothing is done twice.

Nothing publishes on this brief. Every page stays draft. The publishing wall (H9) stands.

## 6. Definition of done

1. 77 WebP heroes in the theme, named `{slug}.webp`, each passing all twelve media gate checks, printout attached.
2. Each attached to its page (or the attach step named as waiting on the importer, per section 5).
3. The image sitemap lists all 77 and one page's schema is shown emitting its `ImageObject`.
4. One REPORT in TO Chat: the printout, any file that failed and how it was brought under budget, any page number in the export that did not match the map, and what the S097 precedent did with the 1760 by 840 shape.

## 7. What this brief does not do

It does not choose the look; Kain has. It does not touch the 77 records. It does not publish anything. It does not reopen the hero geometry (1104 block, 680 image, 400 panel, DSRD 9 section 22.2).

OWED BACK: the REPORT in section 6 item 4, once Kain has confirmed the PNGs are in the folder and Chat has relayed it.

*No em or en dashes in this file; checked before writing.*
