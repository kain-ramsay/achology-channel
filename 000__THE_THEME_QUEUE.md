# THE THEME QUEUE

**What this file is.** The one home for theme edits a factory session found and could not make. One line per item: what it is, why it must be a theme edit, and the session that found it. A theme session strikes the line when the item ships. Nothing else goes in here; it is a queue, not a brief, and an item needing more than a line points at a brief that travelled the normal road.

**Who strikes a line.** The theme session that ships the item, in the sitting that ships it. Nobody else, and never in advance.

Created at S097 on `RULING__The_Theme_Queue_Is_One_File_At_The_Channel_Root_S334.md`. Home written into Harness Rules 1 and 2 at Version 3.11.

---

## Open

- **Images carry no `srcset` or `sizes`, anywhere on the site.** Every visitor is served one file: too heavy on a phone, soft on a retina desktop. Theme edit: the responsive half of DSRD 7 section 12.3 has never been built. Found S097, measured S090 across three sample pages, 39 of 39 images.
- **Width and height carry the rendered size rather than the intrinsic one.** No layout shift, so it is a standards failure rather than a visible one. Theme edit: the attributes are written in the templates. Found S097, 35 of 39 on the same sample.
- **The largest above-the-fold image is lazy loaded and carries no `fetchpriority="high"`, on every page at every width.** DSRD 7 section 12.3 names this as the most common way a well optimised page still fails its speed target. Theme edit, and each one is small. Found S097.
- **About six of the theme's own icons carry neither `aria-hidden` nor an accessible name:** the breadcrumb separator, the footer chevrons, the stats and story-proof glyphs, the help popular badge. The same handful on every page. Theme edit: one attribute in about six places. Found S097.
- **The ACF article-type choice list is missing three of its six types.** `group_article_fields.json` carries five and needs `author-biography`, `field-authority` and `buyer-intent`, per DSRD 1 section 3.2's six-type register. Theme edit: the file is in the theme's `acf-json` folder. Named as a real bug in `RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md`. Found S097.
- **The testimonial background image set breaks the filename convention on upper case alone**, roughly seventy files in `images/testimonials/` (e.g. `Stacey-Q3-bg.jpg`). Theme edit: the files live in the theme, and nothing links to them yet, which is why Chat flagged it as cheap now, expensive once the testimonials page links to them. Found S101, `ASK__Rename_The_Testimonial_Background_Image_Set_S339.md`.

## Struck

*Nothing yet.*

---

*No em or en dashes in this file; checked before writing.*
