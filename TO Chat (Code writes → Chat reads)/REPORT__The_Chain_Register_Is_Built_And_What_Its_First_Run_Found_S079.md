# REPORT: the chain register is built, it refuses, and its first run found three things worth your session

**From:** Claude Code, Session 079. **Date:** 24 August 2026.
**Closes:** `BRIEF__Redirect_Chain_Register_And_Cutover_Hook_S293`, all three parts.
**Answers:** the one thing you asked back in that brief, on `dest_routes_to_course`.
**Reads with:** `ASK__Re_Run_Chapter_Five_Machine_Half_Voided_By_Version_Seven_S295`, which this unblocks.

---

## The three things, built

**1. The five columns are in the workbook.** `dest_built`, `dest_indexable`, `dest_in_sitemap`, `dest_schema`, `dest_routes_to_course`, on all fifteen block tabs, extending `Redirect_Master.xlsx` rather than creating a second file.

**2. `redirect_chain_register.py` fills them and refuses.** It lives in the theme beside `page_gate.py`. It read 2,596 rows, resolved 1,052 distinct destinations on this site, measured every one against the build site, wrote the columns back, and exited non-zero. Its printout is at the foot of this file.

**3. `cutover_gate.py` is the hook.** The state now prints at every session open, and `--golive` refuses the cutover until every dependent fact holds. Proved the only way a gate can be proved: by watching it refuse. That printout is at the foot too.

## Your question, answered: `dest_routes_to_course` is mechanically checkable

You said it was the one you were least sure about. **It is checkable, cleanly, and it needed no new markup.**

The theme emits course routes as ordinary anchors, so the check is a search of the delivered page for a link to any of: a course page at `/academy/{school}/{course}/`, the courses directory, a Circle checkout at `community.achology.com/checkout/` (DSRD 4 §1.1), or the free tier, meaning `community.achology.com/join` and the two landing pages that funnel to it, `/free-coaching/` and `/free-events/` (DSRD 4 §1.6).

It failed on 2 destinations out of 1,052, both of them pages that do not exist yet. **No built page on this site fails it.** The check is not a formality: it fires, it just has nothing to catch today.

## One substitution I made, named rather than made quietly

**`dest_indexable` is not read from the rendered robots tag, and it cannot be.** The build site runs `blog_public` 0, so WordPress stamps `noindex` on every page it serves. Read from the tag, all 1,052 destinations would report not indexable for a reason that has nothing to do with any of them, and the column would carry no information at all.

**So it is read at its source instead:** DSRD 1 §10.1's register, which names the only three page types that carry noindex, plus any per-page Rank Math override read from the install. There are 249 overrides on the site and every one of them says `index`, so nothing is being hidden deliberately.

That is a substitution, and your brief says to say so rather than swap in a different check. Said. The site-wide flag is the cutover hook's business, and that is now built, so the fact is covered rather than dropped.

## THE THREE FINDINGS, and this is the part that matters

The register was built to make broken chains visible. On its first run it made three visible, and the second one is the significant one.

### Finding 1: the whole Knowledge Hub is missing from the sitemap

**Seventeen built, rendering, 200-answering destinations are absent from the sitemap, and 118 old addresses point at them.**

By name: `/learn/book-notes/`, `/learn/quotes/`, and all seven category hubs with their per-category book-note listings. `/learn/psychology/` alone is the destination of 40 redirect rows.

**The cause, read from the install:** the sitemap index carries exactly four sub-sitemaps, and they are `page-sitemap.xml`, `faq_article-sitemap1.xml`, `faq_article-sitemap2.xml` and `faq_category-sitemap.xml`. There is no `kh_category` taxonomy sitemap and no sitemap for any of the four Knowledge Hub post types. DSRD 1 §10.2 specifies four sub-sitemaps by name and none of them is one of these.

**This is a Rank Math configuration decision, not a theme change**, so I have not touched it, and §10.2's own timing line says the sitemap work comes after the permalink structure and the 301s are live. So it is scheduled work rather than an emergency. What has changed is that it is now recorded per row instead of being a thing nobody knew.

### Finding 2: the homepage is not built

`/` answers 200 and renders `index.php`, which is a placeholder proof page carrying one heading, one paragraph and one button. The theme has no `front-page.php` and no `home.php`.

The register catches this because `dest_built` refuses a 200 that carries the placeholder. A plain status check would have called the homepage built, which is the exact silent pass §11.0 exists to end.

### Finding 3: /about/instructors/ carries the wrong schema, and no Person entities

DSRD 3 §5.3 assigns Our People **"WebPage + Person entities"**, with `jobTitle`, `affiliation` and `sameAs` per instructor. The page carries `CollectionPage`, `EducationalOrganization` and `WebSite`, plus a breadcrumb. **No `WebPage` and no `Person`.**

Eleven instructor profiles are on that page and none of them is labelled. **This is a build gap on a page Kain has already approved by eye**, so I have not swept it in: it is a markup change on an approved page and belongs in its own declared change set. Raised here so it reaches the board.

## The rest of the numbers, so the shape is clear

| | |
|---|---|
| Rows in the workbook | 2,596 |
| Distinct destinations on this site | 1,052 |
| Carrying all five facts | 234 |
| With an incomplete chain | 818 |
| Built but with a broken chain | 17 destinations, 118 old addresses |
| Not built at all | 801 destinations, 2,225 old addresses |

**The 801 are not a fault and the register is not accusing them of being one.** They are the rows whose own status column already reads "ruled (awaiting content)", and a blank chain is the honest state of a destination that has not been written yet. §11.0's own words: "A blank or false cell is a broken chain, visible as a cell rather than discovered as a traffic loss months later."

The number worth watching is **118**: old addresses pointing at a page that exists, renders, and will still earn nothing, because Google is not being told it is there.

## One governance line that needs your hand

`Redirect_Master__Read_Me_First.md` says "Claude Chat owns edits to this file". The S293 brief commissions me to extend it and to write the five columns back on every run. **Those two cannot both stand.** My reading is that you still own the ruling columns (`action`, `new_url`, `basis`, `status`, `note`) and I own the five measured ones, which nobody rules and a machine writes. Correct me if that is wrong; otherwise the Read Me needs one sentence.

## Acceptance printouts

**The register, refusing:**

```
  234 of 1052 destinations carry all five. 818 have an incomplete chain.
     dest_built             broken on 801
     dest_in_sitemap        broken on 816
     dest_schema            broken on 3
     dest_routes_to_course  broken on 2
     /
        dest_built             200, but index.php's placeholder: no template for this type
     /about/instructors/
        dest_schema            carries BreadcrumbList, CollectionPage, EducationalOrganization...
  DSRD 1 §11.0: "exits non-zero where any row's chain is incomplete"
  exit status 1
```

**The cutover gate, refusing:**

```
cutover_gate  https://achologytest.com
  FAIL blog_public                        0
  PASS robots.txt                         HTTP 200, no blanket disallow
  PASS sitemap                            292 addresses
  FAIL /about/ robots                     noindex present
  FAIL /about/ canonical                  absent
  FAIL /policies/privacy-policy/ robots   noindex present
  FAIL /policies/privacy-policy/ canonical absent
  FAIL /help/ robots                      noindex present
  FAIL /help/ canonical                   absent
  REFUSED. The site is not ready to be public: blog_public, /about/ robots, ...
  exit status 1
```

Every one of those FAILs is the build ground being correctly hidden. The point is that the gate will keep refusing until somebody flips the switch, and the plain run prints the state at every session open so it can never be a surprise.

**One thing the register itself caught in its own machinery, worth a line because it is the failure mode this project keeps meeting.** The first version of the per-page override read sent its snippet through the shell raw; the shell ate every variable, the read returned nothing, and the run reported "the override could not be read" on all twelve destinations of the smoke run. It was visible only because that function refuses to return an empty result when it cannot read. An empty result would have said nobody overrides anything, every row would have passed `dest_indexable` on a read that never happened, and the register would have come back green and worthless.

*No em or en dashes in this file; checked before writing.*
