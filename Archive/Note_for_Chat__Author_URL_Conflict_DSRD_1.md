# Note for Chat — DSRD 1 puts author profiles at TWO different URLs

From: Claude Code · 2026-07-23 · re: permalink verification (Back End card)

Verifying the theme's URL structure against DSRD 1, everything matches (§1
rules, the whole /learn/ hierarchy in §2.4, /help/ in §2.5). One genuine
conflict — inside DSRD 1 itself, not a theme bug:

**The author/instructor profile page is specced at two URLs.**
- **§2.2** (About Section): `/about/instructors/{slug}/` — e.g.
  `/about/instructors/kain-ramsay/`, with the index at `/about/instructors/`.
- **§2.4** (Knowledge Hub) + **§3.1**: `/learn/authors/{author-slug}/` —
  "author hub page … cross-category, parallel to tags."

They describe the same page (biography + that author's works list). The
header AND footer nav (§13.1/§13.2 "Achology People → /about/instructors/")
and the theme build (`people-setup.php`, `template-author-profile.php`) both
use **/about/instructors/**. The `/learn/authors/` row in §2.4 reads stale.

Recommend: reconcile §2.4 and §3.1 to `/about/instructors/{slug}/` and drop
the `/learn/authors/` row — unless the intent was two separate pages (a Hub
listing AND an About profile), which the build does not assume.

Knock-on: this also decides which sub-sitemap author pages live in
(DSRD 10 §15 — sitemap-about vs sitemap-learn). No blocker for me; the theme
is self-consistent on /about/instructors/ today.
