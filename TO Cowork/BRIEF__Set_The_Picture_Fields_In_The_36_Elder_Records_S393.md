**Needs from Cowork:** set two fields in each of the 36 elder article records so Code can attach their pictures. Run it end to end; skip and log anything you cannot do.

# BRIEF: set the picture fields in the 36 elder records

**From:** Claude Chat, S393, Thursday 1 October 2026. **To:** Claude Cowork.
**Tray order:** first in the tray, before everything else (Kain is making the pictures now). Small and mechanical.
**Board card:** Our People.

## The job

In each of the 36 records in `Content Records/instructor-article/` (AN01 to AN06, AW01 to AW06, ER01 to ER06, GK01 to GK06, GT01 to GT06, JF01 to JF06) set:

- `featured_image` to the record's own slug followed by `.png` (for example `why-is-small-talk-important.png`). The full list is in `000__IMAGE_MAP__36_Elder_Article_Pictures.csv` in the Article Page's Page Images folder, subfolder `36 Elder Article Pictures To Make (S393)`; copy the `save_as` column exactly.
- `featured_image_alt` to a plain description of the picture that carries the record's own focus keyword once, 8 to 15 words, no quotation marks, no dashes. The picture shows an idea (the image map's `picture_idea` column), so describe it that way, for example "A quiet, warm abstract image about small talk" and never a person.

Change nothing else in any record. Then run the real gate on a sample of six (one per elder) and report the result.

## Done when

36 records carry both fields, a one-line check shows none is empty or doubled, and `REPORT__Elder_Picture_Fields_Set_S393` is in FROM Cowork ending in the status line.

*No em or en dashes in this file; checked before writing.*
