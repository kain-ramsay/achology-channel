**Needs from Chat:** close the share image line in both specs (About and Testimonials), as your note said you would once the images were set.

# REPORT: the About and Testimonials share images are set

**From:** Claude Code, S140 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `NOTE__About_Page_Share_Image_S391`.

- **Both images made and set.** Kain's two masters (`og-page--about.png`, `og-page--testimonials.png`, 1350 by 709) were resized to 1200 by 630 and saved as WebP at quality 75 (DSRD 7 section 12.3): 28,612 and 31,070 bytes, inside the 120KB OG budget. The WebP files sit beside the masters in each page's Page Images folder.
- **Set as each page's own Rank Math Facebook and Twitter image:** /about/ (post 184) uses media item 39344, /testimonials/ (post 10058) uses 39345. Both went through the theme's media door, and the cache was purged.
- **Read back on the live pages in a browser:** `og:image` and `twitter:image` name the new files, `og:image:width` reads 1200 and `og:image:height` 630 on both. Before this, no page on the install carried its own share image.
- **One name difference:** WordPress collapsed the double hyphen, so the files on the install are `og-page-about.webp` and `og-page-testimonials.webp`, not `og-page--about` and `og-page--testimonials`. The masters keep the double hyphen.
- **Each page's DSRD 6 record** carries a dated §3 share image line in its machine half. I changed no chapter's state: both pages' §3 rows still read "not run" in the chapter table, and §3's other runner has not run.

OWED BACK: the two spec lines.

*No em or en dashes in this file; checked before writing.*
