# PLAN: the Reviews page, /reviews/

**From:** Claude Chat, S240. **Date:** 2026-08-04.
**For:** Claude Code, to build and to design on screen with Kain.
**Status:** structure, copy, data and standards are settled here. The visual treatment of each block is settled by Kain on the rendered page with Code.

**SUPERSEDED IN PART, S262.** The page was built, designed live and approved whole by Kain at Code's S053. Sections 3, 7 and 8 are superseded on the points marked at each (Code confirmed only those three); the S053 page spec in the Verified Student Reviews Page folder is the signed record, and the DSRDs were rewritten from it at S262 (DSRD 9 §29, DSRD 8 §14, §21, §22, DSRD 7 §5.5). Read those, not this, for the page's truth. This file stays as the plan of record for how the build was commissioned.

**How this one differs from the usual signed spec.** Kain ruled at S240 that the design of this page happens in Claude Code with him at the browser, not in Chat. So this document is the complete plan, not a finished visual specification: everything that can be decided away from the screen is decided here and is not to be reopened, and section 11 names exactly what Kain settles with you on the rendered page. Chat writes the outcome back into the DSRDs once he has approved it.

---

## 1. What this page is for

It exists to get a prospective student who is checking Achology out to carry on to the course or school they were already considering. One action, one reader. The action is continue to the course or school page, not buy. The reviews remove doubt; the course page closes.

Second job, which never reorders the page: be the page that answers "is Achology any good" for search engines and AI assistants. That needs real indexable review text, depth, and per-review markup.

Source: DSRD 9 s29.1. The nine reader changes the page must carry are at DSRD 9 s29.3 and are not restated here.

---

## 2. The frame, identical to the About page

The page is built on the same frame as /about/, because it is the same kind of page: a long, static, bespoke page whose words and figures are baked into the template rather than typed into the editor.

- **Template:** `page-reviews.php`, picked up automatically by the page whose slug is `reviews`. Same pattern as `page-about.php`.
- **Wrapper:** `<main class="policy-page policy-page--reviews">` inside `.page-container` then `.article-container`, exactly as About.
- **Reading column:** 880px (DSRD 7 s4.1). Full-width blocks bleed to 944px by the inset-panel mechanism (DSRD 7 s4.4), which switches on at 1040px.
- **Chrome:** real site header (DSRD 8 s18) and real footer (DSRD 8 s19). No page-local chrome.
- **Block separators:** DSRD 7 s4.3 without exception. A hairline at every block boundary, 48px above and below at desktop and tablet, 32px on phone, the space owned by the element carrying the line, every neighbouring block contributing zero. No hairline above the first block or below the last.
- **Stylesheet:** `reviews.css`, enqueued for this page only, after `policies.css` whose frame the page borrows. Same arrangement as `about.css`.
- **Assets:** the hero artwork lives in the theme at `images/reviews/`. The world map data file is being fetched to `04. Single Page Template Assets/The Review Page/countries-110m.json` under a separate brief.

---

## 3. Block order, top to bottom

**SUPERSEDED S262 (Kain's S053 rulings):** block 5, the standout reviews, is removed from this page entirely, and block 7 is the About gateway plus the enquiries panel, not the Where-next panel. The as-built order is DSRD 9 §29.4.

This is also the phone order. Wider viewports may group side by side but never reorder.

| # | Block | Status |
|---|---|---|
| 1 | Site header | DSRD 8 s18, LOCKED, no work |
| 2 | Breadcrumb | Home > Student Reviews. `components.css` breadcrumb, exactly as About |
| 3 | Hero | Build to the About hero pattern, section 4 below |
| 4 | Global impact block | One component: narrative, map, countries, figures. Section 5 |
| 5 | Standout reviews | Section 6 |
| 6 | The archive: control bar, count, grid, batching | Section 7 |
| 7 | Where next panel | DSRD 8 s13, LOCKED, reuse. Section 8 |
| 8 | Site footer | DSRD 8 s19, LOCKED, no work |

---

## 4. Block 3: the hero

**Built exactly as the About page hero**, which is `.policy-header.policy-header--doc`: artwork floated right at 312px inside the 880px column, text as a `flow-root` column beside it, the header carrying the block hairline with 48px padding below and 48px margin below the line.

| Element | Value |
|---|---|
| Artwork | `.policy-doc` figure, 312px at desktop. Square, transparent, house hero art style, matching the Testimonials hero motif. Kain supplies the final image; a vector stand-in exists at The Review Page folder |
| H1 | `.policy-title`, Como 32px/700/1.2. **"Achology Student Reviews"**, with "Achology" wrapped in `<span class="policy-next__accent">` per the standing orange Achology rule (DSRD 7 s3) |
| Lead | `.policy-lead`, Source Sans 3 19px/500/1.55, brand dark. **"Since 2014, we&rsquo;ve gathered thousands of reviews across our various courses from students in 216 countries. All reviews are real, including the handful of negative ones. This should help you decide whether studying with Achology is the right option for you."** Kain's own wording, typed in Code's S052 session and live at v0.42.7, superseding the sentence this plan first carried. He revised it twice: the closing sentence tells the reader what the page is for, and "thousands" (rather than the second version's "tens of thousands") agrees with the 4,517 written reviews the figures panel states one screen below, so the two statements of one fact no longer disagree. The apostrophe is set as `&rsquo;` to match the About hero, which is the same slot on the same frame. |
| Action | One `.btn .btn-secondary` with a Lucide `ArrowDown`, **"Read the Reviews"**, smooth-scrolling to the archive block, reduced motion honoured. Same mechanism as About's "Read the Achology Story" |

Below desktop, follow the About page's own responsive behaviour for this header: the two-column mini header at 1023px and under, and the stacked header with the artwork behind the text at 599.98px and under, that width being an approved exception already named in DSRD 7 s4.5.

---

## 5. Block 4: the global impact block, ONE component

**Ruled by Kain, S240: the proof figures and the world map are one component, not two.** This is DSRD 4 s14.2 Variant 1, the V2B Dark Band direction, which was always one connected unit: a dark narrative band flowing into the map with a frosted country panel on the right.

The component is built once and shared by the homepage, the About page and this page (DSRD 4 s14.2). This page is its first build.

**Contents:**

- **Narrative and headings: settled by Kain, S053, his own words, live at v0.45.2.** The intro above the panel: h2 `.gi-intro__title` **"A Global Overview of Our Student Impact"**; lead `.gi-intro__lead` **"Since launching our first online course in 2014, we&rsquo;ve learned from our reviews. Positive and negative, we&rsquo;ve learned from them all."** Inside the dark band: h3 `.gi__heading` **"A Global Learning Movement"**; band line `.gi__lead` **"At Achology, Our Students Span the Entire Globe"**. Recorded in `RULING__Global_Impact_Copy_S053.md`; apostrophes as `&rsquo;` matching the hero on the same frame.
- **The map:** generated from real geographic land data so every coastline is accurate. Source file `countries-110m.json`, the Natural Earth 110m TopoJSON, public domain, being fetched under a separate brief. Baked into the theme as a static graphic. **No live fetch at runtime.** Projection shifted left so the panel overlays ocean rather than land.
- **Markers:** the top five countries marked in brand orange. Kain has asked for the markers to feel alive: a slow pulse at rest and a response on hover, both removed under `prefers-reduced-motion`. Treatment settled on screen.
- **Country panel,** right, frosted: United States 202,893; India 115,244; United Kingdom 59,547; Canada 40,646; Australia 29,696. Figures from DSRD 4 s14.1, copy exactly.
- **The figures, inside this same component:** 4,517 written reviews; 4.66 average rating; 695,578 students; 216 countries. These are the four the page carries. Treatment to follow the About page's `.story-proof` dark stage panel language, which is the built precedent for figures on a dark ground: icon, figure, label, hairline rules between items.
- **Honest framing, Kain's revision, S053, live at v0.45.2:** **"129 countries have documented student populations, 87 of them are too small to attribute individually, 216 countries, total."** This supersedes the plan's original wording.

---

## 6. Block 5: standout reviews

- Source: the hand-picked **Featured** flag in the live Notion Review Bank, data source `collection://24b47674-bb62-4992-bdc7-0d1a10183f76`.
- Rendered in the **locked review card** (DSRD 8 s14). **The S239 featured scaling is withdrawn by Kain at S240: the standouts render at normal card size.** DSRD 8 s14.5's last paragraph is superseded on that point and Chat updates it once this is agreed.
- The set includes critical reviews. The page's claim is the whole record, so a 4-star review that names a real fault belongs here.
- Section header follows the site's section-header pattern: 36px orange-tint icon container with an 18px Lucide icon, H2 beside it, supporting line beneath.

---

## 7. Block 6: the archive

**SUPERSEDED S262 (Kain's S053 rulings):** the grid is masonry, two columns at desktop and tablet (not three), the batch is 50 (not 24), and the default order is striped across the star bands (not newest first). DSRD 9 §29.6 decisions 11 to 13 and DSRD 8 §22.

**Control bar** (DSRD 9 s29.6 decision 8). One compact bar: keyword search first, then Theme, Course and Rating dropdowns. Beneath it a plain hint line teaching by example. Above the grid a live results count whose number is real.

The eight visible theme labels, benefit-led, rendered and not objected to at S239, to be confirmed by Kain on the built page and then recorded in DSRD 4 s14.4: Coaching and helping; Practical application; Relationships; Career growth; Self-awareness; Confidence; Wellbeing; Purpose. Teaching quality and value stay internal.

**The grid.** All 4,517 reviews, unedited, in the locked review card. **Masonry, two across at desktop, two at tablet, one at phone, 24px gap (Kain, S053, on rendered options; supersedes "three across at desktop").** Platform-era reviews display verbatim, including the 60 naming Udemy and the roughly 526 addressing the instructor in the second person (DSRD 9 s29.6 decision 4). Both tiers show, including the 3.0 to 3.5 star band (decision 2).

**Batching (settled S053).** Batches of 50 appended in place on a real link, so every review is reachable with scripting off and no reader meets a row of page numbers. Was Code's call at build; ruled by Kain at 50.

**Default order (Kain, S053).** Striped across the star bands rather than newest first, so the 4, 4.5 and 5 star reviews mix down the page and the critical band is spread through the archive rather than sorted to the end. A filtered view returns to newest first.

**Data rules.** The reviews now live in WordPress, imported at S053; Notion was the source, not a live dependency. First name plus surname initial applied at import; the surname never enters WordPress. No per-review country. Each card's footer links to that course's DSRD 1 landing page URL, baked at import.

**Production prerequisite.** One AI pass over the reviews writes two new WordPress fields, `review_title` and `review_theme`. Each title is drawn from that reviewer's own words, lightly trimmed, never invented, to the ten exemplars Kain froze at S258. Kain edits any title he does not like directly in WordPress. Code's export for the pass is `reviews-for-tagging-S053.csv` in the Reviews Page Data folder; the return file carries `review_key`, `review_title`, `review_theme` and nothing else.

---

## 8. Block 7: where next

**SUPERSEDED S262 (Kain's S053 ruling):** the Where-next panel does not appear on this page; the About gateway and the enquiries panel close it instead. DSRD 9 §29.4.

DSRD 8 s13 `.policy-next` panel, reused, no new build. Three rows, each carrying the page's one job, which is to send the reader onward to the thing they were already weighing up:

1. **Browse All 28 Courses**, `/courses/`
2. **Explore the Seven Schools**, `/academy/schools/`
3. **Watch Video Testimonials**, `/testimonials/`

Panel title and lead copy to be settled with Kain on the rendered panel. Icons from the DSRD 7 s5.2 registry; any new slot is registered before it appears.

---

## 9. Schema, the open question

No star rich snippets are available for self-hosted reviews about one's own organisation, so the plan cannot be "mark up the reviews and hope". Code decides what this page emits, states it, and the answer is recorded in DSRD 10 by Chat. Constraint stated so nobody proposes a rich result that Google will not grant.

---

## 10. The definition of done

The page is complete when it passes **DSRD 6**, with the per-chapter record returned through the channel, and when Kain has approved every block by eye on the rendered page.

Standing constraints that apply throughout: every visual decision is made by Kain looking at it, never by reading about it; no em or en dashes in any output; every value is a token, a named DSRD value, or an annotated one-off; the class-name audit and the CSS gate run before anything is called ready.

---

## 11. What is settled here, and what is not

**Settled, do not reopen:** the page's job; the block order; the one-component ruling for the map and figures; the About-page frame and hero pattern; standouts at normal card size; the copy quoted in sections 4 and 5; every figure quoted; the data and import rules; the review card itself (DSRD 8 s14, LOCKED).

**Open, to be settled by Kain on the rendered page with Code:** the hero artwork's final image; the map's marker animation (the hover state has not yet been shown to Kain); the control bar's appearance; the eight theme labels' final wording; the archive's three copy slots (heading, supporting line, hint line). **Settled since this plan was written:** the global impact block's narrative and panel copy (Kain, S053, section 5 above); the batching mechanic (Code's call at S053: batches appended in place on a real link, every review reachable with scripting off).

*No em or en dashes in this file; checked before writing.*
