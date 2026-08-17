# Per-page-type schema inventory — what each page type actually emits, and from where

From: Claude Code · 2026-07-23 · theme v0.36.15
Answers: `Approved_Brief__Schema_And_Video_Build_Gate_Open.md` §5, and settles the
rows DSRD 10 §9 marks provisional.

**How this was produced.** Every page type below was fetched from the live
staging site and its `<script type="application/ld+json">` blocks parsed. Source
attribution is mechanical, not inferred: Rank Math tags its block
`class="rank-math-schema"` and emits one block holding an `@graph`; the theme
emits one untagged block per type. Where no live page of a type exists yet, the
row says so and reads the template instead. Nothing here is reasoning about what
Rank Math ought to do.

---

## 1. The finding that decides the provisional rows

**Rank Math emits nothing at all on a singular Page or a singular CPT post.**
Not the main type, not `WebSite`, not `Organization`. It emits its full graph on
the homepage, on archives, on taxonomy terms and on 404s, and nowhere else.

Measured, same crawl, same minute:

| Emits a Rank Math graph | Emits nothing from Rank Math |
|---|---|
| Homepage | `/about/` |
| `/help/` (the `faq_article` archive) | `/policies/` |
| FAQ category terms | Every policy page |
| `/learn/` listing and category pages | Our People |
| 404 | Author profiles |
| | FAQ articles |
| | Article singles |

This is stronger than Standard 1 assumed. Standard 1 says Rank Math emits
nothing on a template-rendered page whose editor is empty. What the site shows
is that it emits nothing on a singular page **whether or not the editor is
empty**: the policy pages, the FAQ articles and the one published article all
carry real content and still get nothing.

**So every "Rank Math auto" row on a singular page type is wrong**, and wrong for
a firmer reason than Standard 1 gives. Your two suspicions are confirmed:

- **School pages (7)** — Pages. Rank Math will emit nothing. The theme must own
  `WebPage` + `BreadcrumbList` there. Flip the row.
- **Listing and category pages** — mixed, and the split matters. See §3.

---

## 2. The inventory

Legend: **Theme** = untagged JSON-LD from a template. **RM** = Rank Math's
tagged `@graph` block. **None** = nothing emitted by anyone.

| Page type | Live URL crawled | What is emitted | Source | DSRD 10 §9 says | Verdict |
|---|---|---|---|---|---|
| Homepage | `/` | EducationalOrganization + WebSite + CollectionPage | RM | WebSite + Organization, RM auto | **Row is short.** RM also emits a `CollectionPage` as the page node. No breadcrumbs (correct, it is the root) |
| About | `/about/` | AboutPage, BreadcrumbList | Theme (v0.36.8 / v0.36.14) | Theme JSON-LD | Correct as written |
| About child pages | `/about/manifesto/`, `/about/code-of-ethics/` | AboutPage, BreadcrumbList | Theme | no row | **Missing row.** `template-policy.php` types children of `/about/` as `AboutPage`, everything else `WebPage` |
| Policies index | `/policies/` | CollectionPage, BreadcrumbList | Theme (v0.36.9 / v0.36.14) | Theme JSON-LD | Correct as written |
| Policy pages (7) | `/policies/privacy-policy/` | WebPage, BreadcrumbList | Theme | no row | **Missing row** |
| Our People | `/about/instructors/` | BreadcrumbList only | Theme | WebPage + Person per profile | **Row is wrong.** No `WebPage`, and no `Person` nodes for the profiles it lists |
| Author profile | `/about/instructors/kain-ramsay/` | Person, BreadcrumbList | Theme | Custom Person JSON-LD | Correct as written |
| Help hub | `/help/` | RM graph (Org + WebSite + CollectionPage) **and** theme BreadcrumbList | Split | not in the table | **Missing row, and a Standard 3 breach** |
| FAQ category | `/help/getting-started/` | RM graph (Org + WebSite + CollectionPage) **and** theme BreadcrumbList | Split | not in the table | **Missing row, and a Standard 3 breach** |
| FAQ article | `/help/privacy-and-legal/guest-speakers-policy/` | FAQPage, BreadcrumbList | Theme | Built into the template | Correct as written |
| Article single | `/learn/psychology/articles/the-power-of-self-awareness-in-personal-growth-test/` | RM graph (Org + WebSite + ImageObject + WebPage + Person + **Article**) **and** theme **Article** **and** theme BreadcrumbList | Split | "Rank Math auto + custom JSON-LD" | **Two `Article` blocks on one page. Standard 2 breach, and §9's own row sanctions it** |
| KH category hub | `/learn/psychology/` | RM graph (Org + WebSite + CollectionPage) | RM | CollectionPage, RM auto | Works today, but no breadcrumbs from anyone. See §3 |
| KH listing page | `/learn/psychology/articles/`, `/learn/articles/` | RM graph (Org + WebSite + CollectionPage) | RM | CollectionPage, RM auto | Same as above |
| KH tag page | `/learn/tags/confidence/` | 404 | — | CollectionPage, RM auto | **Not built.** Tag URLs do not resolve |
| KH author hub | `/learn/authors/kain-ramsay/` | 404 | — | CollectionPage, RM auto | **Not built.** Author-hub URLs do not resolve |
| Book note / Quote / Workbook singles | none published | — | — | Review+Book / CreativeWork / DigitalDocument, custom JSON-LD | **Specified, not built.** No `single-book_note.php`, `single-quote.php` or `single-workbook.php` exists; those posts would fall to `index.php`, which emits nothing |
| Course pages (28), School pages (7), Academy, Courses dir, Membership, Pricing, Accreditation, Webinars, Testimonials, Reviews | all 404 or redirect | — | — | various, RM auto | **Not built.** Every one is a Page, so §1's finding decides them: the theme will have to own them |
| 404 | any missing URL | RM graph (Org + WebSite + WebPage) | RM | not in the table | **Missing row.** Harmless, and correct that it carries no breadcrumbs |

---

## 3. The four things that need your decision

**a) Two `Article` blocks on the article page.** Rank Math emits a full `Article`
inside its graph and `single-article.php` emits its own. This is live now, on the
one published article, and §9's row explicitly asks for both ("Rank Math auto +
custom JSON-LD"). Under Standard 2 the row is now wrong. My recommendation: the
theme keeps its `Article` and Rank Math's is switched off for the `article` post
type, because the theme's block is the one that reads the people registry for
authorship. Same shape as the breadcrumb switch-off shipped in v0.36.14.

**b) `/help/` and the FAQ categories split their source.** Rank Math owns
`CollectionPage`; the theme owns `BreadcrumbList`. Standard 3 says breadcrumbs
follow the page's schema owner, so as built these two page types breach it. Both
run on templates with no editor at all, so Standard 1 points the same way: the
theme should own `CollectionPage` there too. Two rows to add, one small build.

**c) The Knowledge Hub listing and category pages have no breadcrumbs from
anyone.** Rank Math gives them a `CollectionPage` and no trail; the theme emits
nothing. DSRD 1 §9 specifies a trail for every one of them. Whichever way (b) is
settled should settle these the same way, since they are the same shape of page.

**d) Our People emits a bare `BreadcrumbList`.** No `WebPage`, and none of the
`Person` nodes §9's row promises. The `Person` nodes exist on the individual
profile pages instead. Either the row is describing the profile pages and should
say so, or the hub needs building out.

---

## 4. Two smaller things worth recording

**The organisation's name differs by source.** Rank Math's graph calls
`#organization` "Achology Transactions Ltd"; the theme's blocks call the same
`@id` "Achology". They never appear on the same page today, so nothing
contradicts itself in one document, but across the site graph one `@id` carries
two names. One of them should give way, and it is a wording decision, so it is
Kain's.

**The sitemap index carries three sub-sitemaps: `page`, `faq_article`,
`faq_category`.** The `article` CPT has one published post and no sub-sitemap, and
`book_note`, `quote`, `workbook` and `review` have none either. DSRD 1 §10
specifies four grouped sub-sitemaps. Not urgent while the content is unbuilt, but
it will not appear on its own when the content lands.

---

## 5. What I have not done

I have not changed any row in DSRD 10, and I have not built anything from §3 —
those are yours and Kain's to settle. What shipped this session is only what your
brief approved: the `VideoObject` group and output, and the two `BreadcrumbList`
blocks with Rank Math's breadcrumbs switched off on those two pages. One note on
that switch-off: Rank Math currently emits **no** `BreadcrumbList` anywhere on
the site, so the filter changes nothing today. It is there so that turning Rank
Math's breadcrumbs on later cannot silently produce a second trail.
