**DISPOSITION (S275, written at archive):** read at the S275 close; informational, no ruling needed from Chat beyond acknowledgement. Theme version carried into the S275 handover as v0.61.3 at this point in Code's sitting. Board cards moved: none (all four commits already sit on the Schools and Courses side tabs card per Code's own note). The Site Health noindex warning this file flags went onto the Hosting and Go-Live card via the companion CUTOVER file.

# ADDENDUM to SESSION_REPORT__S059: three admin changes made after it was filed

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Extends:** `SESSION_REPORT__S059.md`, which you have already read and archived. A new file rather than an edit to an archived one, since the report was consumed.
**Theme:** v0.61.1 to **v0.61.3**, three further commits, all pushed and deployed.

---

## What was added, from the log

| What was finished | Board card |
|---|---|
| **The admin sidebar ordered**, `dd02c78`, v0.61.2. Kain's ruling in session | Schools and Courses side tabs |
| **Posts and Comments hidden**, same commit. Kain's ruling in session | Schools and Courses side tabs |
| **Hairline rules between the groups**, `1bf9cfc`, v0.61.3. Kain's ruling in session | Schools and Courses side tabs |

## The ordering, and why it is not alphabetical

Kain asked whether the sidebar could be alphabetical or grouped. **Alphabetical was put to him and rejected on its merits:** it separates Schools from Courses and files Courses next to FAQ Articles, so the two things Achology sells end up in different parts of the list.

The order now groups by what a thing is, with what he and Karen open constantly above what they open rarely:

Dashboard, rule, **Schools and Courses**, rule, **Articles, Book Notes, Quotes, Workbooks, FAQ Articles**, rule, **Reviews**, rule, **Pages and Media**, rule, the plugins.

**Why it needed doing at all, for the record.** The sidebar had grown by accretion: every content type chose its own `menu_position` as it was built (faq_article 20, the four Knowledge Hub types 21 to 24, reviews 25) and the two academy tabs I added earlier this session collided with that range. So Schools and Courses landed between FAQ Articles and Book Notes. The ordering filter replaces the whole scheme, and anything not named in it keeps its place at the foot rather than vanishing, so a plugin installed tomorrow appears rather than disappearing.

## Posts and Comments: hidden on a measurement, not an impression

**The site has zero published posts**, counted this session, and no template renders a post or a comment thread. Both were holding prime sidebar space above content types used daily.

**Hidden, not unregistered.** The post type stays registered and both screens stay reachable by address. Nothing is destroyed, nothing needs migrating, and deleting two lines brings them back.

## The hairlines: why the theme registers its own

WordPress ships exactly three separators and this order has five boundaries. Reusing the three would have left two groups running into each other, which is the thing the rules exist to stop, so the theme registers five of its own.

On the styling, since it is a visual decision and Kain asked for subtle: WordPress's own separator is a one-pixel line at 13 percent white, which reads as a scratch rather than a division at this menu's length. The rule now has real air either side and stays quiet, so the space does the grouping and the line only confirms it. Same reasoning as a hairline on the site.

**Verified**: the five rules register and land exactly at the five boundaries, read back from the server. **The line weight itself is Kain's eye and he has it in front of him**; anything he changes will follow as a correction.

## One thing worth a board note, from a Site Health check he asked for

Site Health reports seven recommended items. **One of them must never be actioned on the build ground: "Search engines are discouraged from indexing this site."** That is `blog_public = 0`, confirmed this session, and it is deliberate. It is the same fact behind `RULING__Noindex_Sitemap_Fails_Are_Build_Ground_Exceptions_S272`.

The risk is that it reads as a defect to anyone opening that screen, so it is worth carrying on the cutover card rather than left to be "fixed" by whoever notices it first. The rest are host-level or launch-time and none is urgent; the detail went to Kain directly.

*No em or en dashes in this file; checked before writing.*
