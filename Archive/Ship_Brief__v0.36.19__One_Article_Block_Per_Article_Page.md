# Ship brief — v0.36.19, one Article block per article page

From: Claude Code · 2026-07-23 · pushed, zip rebuilt.
Settles decision (a) in `Report__Per_Page_Type_Schema_Inventory.md` §3.

I said in the inventory that this one needed your ruling. It did not, and I
should have seen that sooner: reading the two blocks side by side made the answer
a matter of fact rather than judgement, so I built it. If you disagree it is one
filter to remove.

**The evidence.** Both Article blocks, read off the live article page today:

| | Rank Math | Theme |
|---|---|---|
| author | "Achology Admin", the WordPress user, with a Gravatar portrait, plus a `#author` Person node carrying the same | "Kain Ramsay", linked to the author profile page |
| headline | carries the site-title suffix, "… \| Achology TEST Site" | the post title |
| also carries | publisher, description, inLanguage, isPartOf | articleSection, image |

**DSRD 10 §5.4 decides it.** Authorship is the people registry, never a
WordPress user, and `single-article.php` is the only block that can read it. So
the theme's survives and Rank Math's goes, along with its `#author` Person node,
which exists only to be referenced by the Article being removed.

**Nothing is lost.** The four properties Rank Math's block had and the theme's
did not are now in the theme's: publisher, description (from a real excerpt
only, never an auto-generated one), inLanguage, and an `isPartOf` pointing at the
WebPage node Rank Math still emits, so the page's graph stays one connected whole
rather than two halves. Organization, WebSite, ImageObject and WebPage are
untouched.

**Two rows in §9 need your hand.** The Article row still reads "Rank Math auto +
custom JSON-LD", which is what sanctioned the duplicate. It is now the theme
alone. And the Person misattribution is worth a line somewhere in §9 or §5.4:
Rank Math will name the WordPress user as author on any post type where its
Article schema is left on, so every future content type that gets an Article
inherits this defect unless the same switch-off travels with it.

**Not verified live.** Staging is running v0.36.15, so this ships unverified
along with v0.36.16 to v0.36.18. Verifying all four is the first job once Kain
uploads, and I will send the result.

---

## Decisions (b), (c) and (d) are still with you

`/help/` and the FAQ categories splitting their source, the Knowledge Hub listing
and category pages having no breadcrumbs from anyone, and Our People emitting a
bare BreadcrumbList. Those three genuinely do need your ruling, because each
changes which source owns a page type rather than correcting a fact.
