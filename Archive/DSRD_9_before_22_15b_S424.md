# ACHOLOGY.COM — Design Spec Document (Page Layout Specs)

*Single source of truth for every confirmed Achology.com page layout: category hub, listing page, individual article page, About page timeline, and the course-page accreditation block. Design foundations are in DSRD 7. Component anatomy is in DSRD 8. Production implementation notes for all page templates are in the Production Implementation Notes document. DSRD 6 — The Page-Readiness Standard — is the go-live gate that confirms each built page matches its locked layout in this document (DSRD 6 §2), commanded open by standing rule 15.*

## Document-Level Standards

Three standards govern every page layout specified in this document. All are held canonically in the vault and in DSRD 2 §0; this document expresses them structurally, never restates them. Each applies to every layout specified or unlocked from its adoption onward; locked layouts (§20–§24) are checked against them at their next unlock, not reopened for them.

**The product-framing layer.** A selling-page layout carries the slots its product's positioning record fills, so the chosen frame is expressed structurally rather than re-decided per page: the header names what the product is in the record's chosen market category; a who-it-is-for placement carries the best-fit student; comparison and alternatives sections are laid out to perform the record's honest alternatives map; and each quantified proof point sits beside the value claim it supports. The record itself is held in DSRD 4 (per DSRD 2 §0.1); this document owns only its structural expression.

**The per-page message lens.** Every page layout expresses the StoryBrand (SB7) message lens in its section order: the header answers the grunt test at a glance (what is offered, how it helps the reader, what to do next); empathy appears before proof; where a page carries a plan, it is visible before the direct call to action; and call-to-action placement matches the page's buyer-readiness stage. The lens and its part mapping per page type are held in the vault and in DSRD 2 §0.2.

**The ethical-influence layer.** A page layout places its influence elements where the reader's state needs them, so the trust sequence is expressed structurally rather than improvised per draft: proof and expertise placements (student numbers, ratings, instructor track record) sit early in the section order, where the reader is still deciding whether this is credible; genuine stakes and the direct call to action sit late, where the reader is deciding whether to act; the strongest claim's placement carries its honesty-against-interest pairing beside it — the genuine limit or fair alternative laid out before the claim, not after; the first ask in the section order is the small, voluntary step (a download, a sample, a saved quote) before the enrolment decision; and no layout carries a pressure device — countdown machinery, stock counters, or urgency banners — unless the scarcity behind it is genuine and its source named. Every influence element a layout slots exists because the smuggler test passed at specification; the pass itself is held in the vault and in DSRD 2 §0.3.

**The composition standard.** Every page layout in this document is derived before it is designed: the page type's job is named as one action by one reader, the reader's arrival and required states are established, the changes between them are listed in the reader's own language, ordered by dependency, and each is assigned a block. A layout's `Page Structure (top to bottom)` list is the output of that derivation, and each entry names the change its block carries, so a later reader can test any block against the job it does rather than against taste. The derived order is also the mobile order — wider viewports may group blocks side by side but never reorder them. The derivation runs once per page **type**, never per instance; where a single instance needs a block the others do not, it is specified as a named optional slot in the type's layout. The methodology is held in the vault and run by `page-composition`; this document owns only the resulting block maps.

A layout locked before this standard was adopted (§20–§24) is checked against it at its next unlock, and any block found to carry no change is reported to the director as a finding, never removed unilaterally.

---

## 20. Category Hub Page Layout (LOCKED S220; RE-CHECKED AGAINST THE CURRENT FOUNDATIONS, S313)

### 20.0 The S153 to S154 redesign: direction D, the editorial front (Kain, Code's S153 and S154 theme sittings; recorded by Chat, S414)

**Status (rewritten S423).** Kain chose every part below from rendered options and **approved the page as a whole at Code's S155 theme sitting** ("it's going to be time for you to build these seven pages"). Code built it for all seven categories at 0.707.161 (S157) and refined it in Safari with Kain to 0.707.213 (S158). This section, with section 20.0c, is the page's layout, and **sections 20.1 to 20.8, 20.10 and 20.13 below are superseded** and kept as the record. Where section 20.0c and the list below differ, section 20.0c is the later ruling and wins. The approved prototype and its build sheet, with every value, are in the Category Hub Page folder; this section records what Kain ruled and why, and names no file inside the folder (standing rule 24). The folder also holds the two research files the directions came from.

**Why it was redesigned.** Kain, looking at the built page in Safari: "I don't know what I'm here for." He asked for research into the best category pages on major publishing sites, then "direction first, best effort design and structural layout, and then we get into molecular details last." The five Part 2 questions of the S378 reconciliation are parked until the layout is settled.

**The direction (D, the editorial front, chosen from four).** Kain: "we can't offer anyone a guided path ... editors picks ... is an easy front door into other articles." No section per content type, and no empty sections.

**Top to bottom, as ruled:**
1. **The head: a dark band, not a hero.** The brand dark band, full width, 480 deep. Left: the trail; "Knowledge Hub Category" in small text above the title (Kain's addition); the title at 42 over a faint Achology bubble mark; one sentence saying what the page is for (the purpose line, section 20.0a); then one bar of four links with icons, Articles, Book Notes, Quotes and Workbooks, each opening the grid on its kind. Right, seven of twelve columns: eight authors from the subject's own book notes, one large and six small, each with the book of theirs the Knowledge Hub holds, no heading over them, sitting 48 from the trail's top line and 48 above the band's foot. Kain: "I am now very, very happy with the Hero Banner. That looks perfect."
2. **The categories bar (S154, "follows you").** A slim dark strip straight under the band: the label "Categories", then all seven categories spread evenly, the current one in light orange with a white Achology bubble behind it at 6 per cent. It pins under the site menu as the reader scrolls. No "All" link. Kain: "They're not subjects, they're categories"; every label says Categories.
3. **The lead row.** The latest article across two thirds, its words centred. Beside it, in the last third, **The Editor's Picks**: a soft panel (#F7F7F6, radius 12, 20 inside) with a quill before the heading and Kain's line under it, "A selection of our editor's favourite reads.", one line on desktop. Four picks, each a small picture with its title in Como 14, two lines at most; no "Article" label and no author name.
4. **The grid.** On a full-width grey plate, a one-line bar: a search box (drawn only, until the site search page exists) beside a joined bar of icon filters, the chosen one dark. Under it a dense four-column grid of 48 cards, newest first, every article and book note labelled with its kind, the four column feet levelled. Book note tiles on this page show the cover as a real book on a soft studio floor (S154, option 5 of eight). Then, 48 below, the link "Explore More Knowledge Hub Articles" to the Articles listing.
5. **The topics,** 48 above the footer. The subject pills at the foot are gone; the categories bar carries them.

**Hairlines (Kain, S153: "as a minimal, as a basic standard").** One site hairline, 48 above and 48 below, between every part; section headings lose their own under-line. This ends the S313 exception 3 for this page once the redesign is built.

**Four departures from DSRD 7, ruled by Kain on rendered options, scoped to this page:** the trail to the title is 32, not the article hero's 48; under the last line of the band to its foot is 64, not section 4.3 rule 3's 48; the title is 42 (the type scale's homepage hero size); and a small label sits above the title, which the article page ruled out at S150.

**Empty kinds are hidden.** Where a category holds no quotes or no workbooks, its link and filter do not show (Kain, S154: "hidden please").

**The cards on this page follow the site-wide card rule** in DSRD 8 (S154): word count and reading time, never a pen name.

**Still open:** Kain approved the whole page at S155 and Code built the tablet and phone layers at S157; what remains open is listed at the foot of section 20.0c (S423).

### 20.0a The purpose line, seven subjects (Chat, S414; RETIRED S158)

**Retired (Kain, Code's S158 sitting; written S423).** The seven lines below are replaced on all seven pages by one subheading in Kain's own words: "All articles in this category are consolidated in one place, making it easier for you to find your next read." The seven are kept as the record.

One sentence under the title saying what the page is for, not what the subject is (Kain, S153). One frame for all seven so the band reads the same everywhere, under 120 characters, two lines in the band's column. "Articles and book notes" rather than all four kinds, because a subject with no quotes or workbooks hides them (section 20.0), and the line must never promise what the page does not hold.

- **Psychology:** Our articles and book notes on how people think, feel and behave, all in one place, so you can find your next read.
- **Helping People:** Our articles and book notes on helping other people well, all in one place, so you can find your next read.
- **Mental Wellness:** Our articles and book notes on looking after your inner world, all in one place, so you can find your next read.
- **Motivation:** Our articles and book notes on what drives you and keeps you going, all in one place, so you can find your next read.
- **Personal Growth:** Our articles and book notes on growing through self-awareness and wise choices, all in one place, so you can find your next read.
- **General Interest:** Our articles and book notes on wider ideas for living a wise and self-directed life, all in one place, so you can find your next read.
- **Wisdom for Life:** Our articles and book notes on thinking clearly and living well, all in one place, so you can find your next read.

### 20.0b Who chooses the Editor's Picks (Chat's call, S414; Kain may overturn it)

**The picks are articles only (Kain, Code's S158 sitting: "yes"; written S423).** A book note's upright cover cannot sit in the panel's landscape thumbnail without its title being cut. The empty-field fallback is the four newest articles after the lead. Code replaced every book note in the seeded picks on the build site at S158 and kept the original lists in `RULING__Subject_Page_Audit_Fixes_S158` so any can be put back.

The picks are chosen by hand, never by a rule, because the panel's own line promises "our editor's favourite reads". Each subject page carries a field for its four picks that Kain or Karen can change in the page editor (owner operation, section 5 of the Project Instructions). Chat proposes the first four for each subject; Kain sees them on the built page and keeps or swaps them. If the field is ever empty, the panel shows the four newest articles after the lead article, so the page never shows a gap.

### 20.0c What Kain ruled after S154: the page as built for all seven (Code's S155, S157 and S158 theme sittings; written S423)

Each line names the sitting. Every value is in the build sheet in the Category Hub Page folder (its "Decided in S155" and "Decided in S157" rows); the frozen prototype still shows the S154 wall, and its fold-back is owed (the close-out sitting).

**The Editor's Picks panel (S154 close).** Titles in Como 14, two lines at most, centred against each picture; the soft panel (#F7F7F6, radius 12, 20 inside); a quill before the heading, no square, as tall as the heading's letters; heading "The Editor's Picks" and the line "A selection of our editor's favourite reads." in Kain's words.

**The categories bar (S154 close).** A white Achology bubble behind the current category, the small one, centred, at 6 per cent. On a tablet and a phone the seven names scroll sideways beside their label (S157).

**The grid, item 4 above, as now built:**
1. **The kinds are mixed (S157).** Each kind keeps its own newest-first order and the two are interleaved: the kind a category holds fewer of takes at least one place in every row of four where it has enough, spread evenly down the wall in a fixed rotation (third, first, fourth, second place). The same on every load, never random.
2. **Quotes are on the wall (S157).** A category's wall shows the quotes filed in it plus every quote sharing one of its topic tags; the five content attribute tags never count. No quote is moved and no address changes. At most one quote a row, and **no author takes more than two quotes on a wall, the authors taking turns** (Kain: it must not read as "the Kain Ramsay show").
3. **A quote tile is the quote's own baked card picture (S157)**, with the card body under it: the label "Quote Article" and "{n} Words · {n} Minute Read". Only a quote whose picture is baked is used.
4. **Every card's label carries its kind's icon (S157)**, 16 pixels, link orange, before the label.
5. **45 to 48 cards a wall (S157).** An oldest card is left out only if that levels the four column feet by 24 pixels or more.
6. **One Know Your Psychology card (S157),** the generic KYP logo stretched across a white card at one fixed size, linking to the Knowledge Hub home page, placed only where a column's free space holds it at that size, at most one, never squeezed in.
7. **Columns: four on a desktop, three on a tablet, two on a phone (S157).**
8. **The search box reads "Search the Knowledge Hub" (S157);** it searches nothing until the site search page exists.
9. **The tabs above the grid show true totals (S158),** the Quotes tab counting every quote that belongs to the category under rule 2. **No foot buttons under the wall (S158):** the S154 "Explore More Knowledge Hub Articles" link and the S158 per-kind buttons are both removed.

**Empty kinds (S157).** A kind is hidden only where the category truly holds none. Quotes show on every wall under rule 2. Workbooks have no wall tile yet.

**The topic block, item 5 above, as now built (S158).** One block of tags, the same on all seven pages: 31 topics, then the five kinds of article as "Research-Based Articles", "Deep Exploration Articles", "Beginner-Friendly Articles", "Practical Exercise Articles" and "Professional Practice Articles" under "Or read by kind". Every tag 56 tall, one corner, one gap; every row runs edge to edge at every width; equal widths in a row; cream for topics, tinted orange for the kinds; the bubble clipped inside its tag on hover. Heading "Explore the Achology Knowledge Hub by Topic" (S155, Kain's words), with no under-line. This replaces the S155 feature and nine picture tiles and the S158 warm-fade tiles. The per-category topic lists of DSRD 2 section 1.3.3 no longer drive this block; they still drive the quote pool.

**The bottom panel: a learning path, destination first (S155).** The dark card with the diploma in front of a student at his computer, and a grey panel headed "Take Your Learning Further" with the line "Whether you're exploring a topic for the first time or ready to delve into human psychology, Achology offers a clear next step in your learning.", on a stone mountain with a very faint path. Its four steps and the dark card's three ticks are Kain's words (build sheet). Step two links to the workbooks page; step three to the courses page; **step four's course is chosen by hand per category** in an editable field (a practitioner course that counts towards the Achologist title), falling back to the first course of the category's course block. Psychology is set to DiMAP.

**Speed (S157 and S158).** Book covers on the wall draw WordPress's own 200 by 300 copy, with automatic sizes off on this page only; each wall's built data is saved and cleared whenever a piece, category or tag changes.

**Still open, each with who closes it:**
- Chat places or rules DSRD 4 section 5.1's workbook offer for category hubs, now that step two of the learning path links to the workbooks page.
- Chat proposes step four's course for the six other categories, and the dark card's button words for a course that is not a diploma (Code drafted "Explore the Course").
- Chat confirms the three kind names Kain did not name (Beginner-Friendly, Practical Exercise, Professional Practice) and whether "Deep Exploration" replaces "Deep Dive" beyond this block.
- Chat rules, for the listing page, whether a category's quote list includes quotes that share its topics.
- The S159 page gate: Code fixes six template faults (picture sizes, face descriptions, lazy loading, hidden icons, cover formats); five items wait on a ruling, the hairlines, the 42 title, the breadcrumb spacing and the "Categories" label's contrast with Kain's eye, and acronyms in card titles with Chat (`REPORT__Subject_Page_Gate_S159`).
- The close-out sitting: the seven DSRD 6 records, Chat's Rank Math words, and the prototype fold-back.
- Chat records the quote card on the wall (rules 2 and 3 above) in DSRD 8 section 6.0.
- After the page closes, Kain and Chat decide which of its parts become their own components (the categories bar, the Editor's Picks panel, the levelled card wall, the real-book tile).

**Why this section was re-checked, and the one finding that is not a tidy-up.** It was locked before the nine-step type scale (DSRD 7 §3.0, Kain S056), the hairline block-separator standard (DSRD 7 §4.3, Kain S224), the supporting-line grey ruling (S280), the signed card system, and the body face (Kain, Code S085). Locked is not the same as current. Every correction below is conformance to a standard Kain has already ruled, on the same ground as the S280 pass.

**The finding, and Kain's ruling on it (S313).** This page has four block boundaries and draws a line at none of them, where DSRD 7 §4.3 ruling 1 says every boundary on the site carries one. It was put to him rendered: the same page twice, tabbed, with the line as the only variable. **He ruled the page as it is, with no lines.** It is now a named exception at DSRD 7 §4.3, exception 3, scoped to this page alone, on the ground that each section already opens with the section header's own hairline and a second line ninety pixels away makes the page read as ruled paper. **The boundary is still marked; it is marked by the section header.**

**Two things deliberately not corrected, and named rather than left looking settled:** the tablet and phone sizes in §20.14, which belong to the responsive rule DSRD 7 §3.0 records as still open and Kain's on a render; and the prototypes, which are pre-Mulish and are re-cut under the S311 ruling.

The category hub page is the main landing page for each of the 7 Knowledge Hub categories (e.g. /learn/psychology/). One shared template, populated ×7. Each page surfaces 5 items per content type (1 featured + 4 standard) across 4 content sections (Articles, Book Notes, Quotes, Workbooks), plus a tag browsing strip. Locked prototype: `category-hub-psychology-v9.html`.

### 20.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§20.3)
3. Hero section (§20.4)
4. Category pill strip (§20.5)
5. Articles section — featured LEFT (§20.6, featured card DSRD 8 §6.5)
6. Book Notes section — featured RIGHT (§20.6, featured card **DSRD 8 §6.8**). *(Pointer corrected S313: this read §6.2, which is the standard book note card. §6.8 is the featured book note card, ruled and filed at S261. The same stale pointer was corrected once already at S268 in §22, and it had not been swept here.)*
7. Quotes section — featured LEFT (§20.6, featured card DSRD 8 §6.6)
8. Workbooks section — featured RIGHT (§20.6, featured card DSRD 8 §6.7)
9. Tag browsing strip (§20.8)
10. Rainbow stripe + footer (DSRD 8 §19)

### 20.2 Vertical Rhythm

| Transition | Gap | Value |
|-----------|-----|-------|
| Header bottom to breadcrumb | 48px | var(--sp-2xl) |
| Breadcrumb to 'Category' overline | 12px | Hero padding-top |
| 'Category' overline to H1 | 4px | Tight label-title pair |
| H1 to counts subtitle | 10px | Supplementary data |
| Counts subtitle to intro copy | 16px | var(--sp-md) |
| Intro copy to category pills | 24px | var(--sp-lg) |
| Category pills to the first section | **48px, no line (Kain, S313)** | DSRD 7 §4.3, exception 3 |
| Section to section | **48px, no line (Kain, S313)** | DSRD 7 §4.3, exception 3 |
| Section header to card grid | 20px | Below the section header's own hairline, which is inside the DSRD 8 §23 component and keeps its own values under §4.3's carve-out |
| Last section to footer | 64px | var(--sp-3xl) |

**The boundaries carry no hairline, and that is Kain's ruling rather than an omission (S313).** It was put to him on two whole rendered pages, tabbed, with the line as the only variable, and he took the page without lines. **Each section already opens with the section header's own rule**, so a separator as well puts two lines within about ninety pixels of each other and the page reads as ruled paper. It is registered at DSRD 7 §4.3 as exception 3 and scoped to this page alone; the gate reports it as a named carve-out, never a silent pass.

**One row did change: the pills-to-first-section gap was 40px**, which is not a value on the 8px spacing scale at all. It becomes 48, the page's own dominant rhythm, with no line.

*Hero internal spacing keeps its asymmetric 4/10/16px progression, untouched: those are gaps inside one block, not boundaries between two, and §4.3 does not reach them.*

### 20.3 Breadcrumb Component

- **Format:** `Home` icon `ChevronRight` Learn `ChevronRight` [Category Name]. *(Corrected S378: this read "Home icon, Home, Learn". The house icon is the Home link and no word follows it; the trail was signed as built by Kain at S090, DSRD 8 §25.)*
- **Home icon:** Lucide `Home`, 13px, mid grey (#8A9199), inline with first breadcrumb segment (DSRD 7 §5.2)
- **Separator:** Lucide `ChevronRight`, mid grey (#8A9199). Replaces ' > ' text character for cross-browser consistency (DSRD 7 §5.2).
- **Font:** Mulish, the 12 step, 400 (Caption style, per DSRD 7 §3.2). *(Corrected S313 from 13px, which is not a step; the approved S056 override maps 13 to 12.)*
- **Colour:** **Soft grey #5E6B75 on the links, mid grey #8A9199 on the separators.** Current page (category name) is brand dark (#354149), not linked. *(Corrected S313: the 2026-07-13 contrast audit moved every breadcrumb link site-wide to soft grey because a link is text a reader reads, and left the separators on mid grey because they carry no meaning. This row still read mid grey throughout.)*
- **Links:** 'Home' links to `/`, 'Learn' links to `/learn/`
- **Spacing:** 48px below header bottom edge (var(--sp-2xl))

*Provides a visual anchor at the start of the breadcrumb trail. Same 13px size as stats icons on cards — consistent icon scale across the design system.*

### 20.4 Hero Section

**Layout:** White background, left-aligned text. No search bar in the hero (category hubs are browsing pages, not search pages; the site search stays reachable from the header on every page, DSRD 1 §7.4, S366).

**Overline:**

| Property | Value |
|----------|-------|
| Text | 'Category' |
| Font | Como 11px/600 |
| Transform | Uppercase |
| Letter-spacing | 0.08em |
| Colour | Mid grey (#8A9199) |

**H1 (Category Name):**

| Property | Value |
|----------|-------|
| Font | Como, the 33 step, 700 (H1 Page Title, per DSRD 7 §3.1). *(Corrected S313 from 32px, which is not a step; the same correction §22.4's H1 took at S302 and §21.2's took this session.)* |
| Colour | Brand orange (#ED6922) |
| Line-height | 1.2 |

*Orange H1 ties visually to the active category pill below (D11). Strong wayfinding signal — the visitor immediately knows which category they're in.*

**Counts Subtitle:**

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | **Soft grey (#5E6B75).** *(Corrected S313 from mid grey: these counts are links a reader reads and clicks, and DSRD 7 §1.1 forbids mid grey for anything a reader needs. Same correction as §21.2's count line.)* |
| Content | '[X] Articles · [X] Book Notes · [X] Quotes · [X] Workbooks' |
| Links | Each count links to its content type listing page (e.g. /learn/psychology/articles/) |

*Counts appear at two levels: hero subtitle (all 4 content types at a glance) and section headers (individual counts where they matter). Making hero counts clickable adds utility with zero visual cost (D15, D16).*

**Intro Copy:**

| Property | Value |
|----------|-------|
| Font | Mulish, the 16 step, 400. *(Corrected S313 from 17px per the approved S056 override, which maps 17 to 16.)* |
| Colour | Brand dark (#354149) |
| Line-height | 1.6 |
| Max-width | 880px |

*880px max-width ensures 3-sentence intros consistently land at ~4 lines on desktop. All 7 category intros confirmed at 60–70 words for uniform hero height across category hubs. See §20.9 for confirmed copy.*

**Hero spacing (D17):**

| Transition | Gap |
|-----------|-----|
| Overline to H1 | 4px |
| H1 to counts subtitle | 10px |
| Counts subtitle to intro copy | 16px |

*Asymmetric 4/10/16 rhythm — each gap noticeably wider than the last.*

### 20.5 Category Pill Strip

Horizontal row of 7 pills, one per Knowledge Hub category. Provides direct category-to-category navigation below the hero.

| Property | Value |
|----------|-------|
| Layout | Horizontal flex, gap 8px, wraps on mobile |
| Active pill | Brand orange (#ED6922) background, white text |
| Inactive pills | Off-white (#F3F4F4) background, brand dark (#354149) text |
| Hover (inactive) | Background shifts to brand orange at 10% opacity |
| Font | Como, the 12 step, 500. *(Corrected S313 from 13px, which is not a step.)* |
| Padding | 8px 16px |
| Border-radius | 20px |
| Links | Each pill links to /learn/{category}/ |

*Category pills solve a gap the mega menu does not: the Knowledge Hub dropdown has content-type tiles (Articles, Book Notes, etc.) but no category links. Pills give visitors direct category-to-category access without returning to the mega menu (D3).*

### 20.6 Content Type Sections

Four sections, each with an icon-led section header (§20.7) and a grid of 5 cards (1 featured + 4 standard).

**Grid Pattern (D9):**

- 5 items per section: 1 featured (2-column span) + 4 standard (1-column each)
- Grid: 3 columns desktop, 2 tablet, 1 mobile. Gap 24px.
- Row 1: featured card + 1 standard card. Row 2: 3 standard cards.
- Featured cards alternate left/right down the page (zigzag):

| Section | Featured Position | Featured Card Type |
|---------|------------------|-------------------|
| Articles | LEFT (columns 1–2) | Featured article card (DSRD 8 §6.5) |
| Book Notes | RIGHT (columns 2–3) | Book note horizontal layout (DSRD 8 §6.2) |
| Quotes | LEFT (columns 1–2) | Featured quote card (DSRD 8 §6.6) |
| Workbooks | RIGHT (columns 2–3) | Featured workbook CTA card (DSRD 8 §6.7) |

*Zigzag alternation prevents four identical grids and creates visual movement down the page. Each featured card reflects its content type personality: editorial horizontal (articles), cover-led horizontal (book notes), elevated typography (quotes), dark CTA (workbooks) (D9, D10).*

**Standard cards** use the corresponding DSRD 8 §6 card design: article card (DSRD 8 §6.1), book note card vertical (DSRD 8 §6.2), quote card (DSRD 8 §6.3), workbook card (DSRD 8 §6.4).

**Content ordering:** Newest first — permanent rule (DSRD 7 §17.3). Featured card is always the most recently published item in that content type for the current category.

### 20.7 Section Header Component

Reusable component used above each content type grid and the tag browsing strip on category hub pages.

**Layout:** Horizontal flex, items centred vertically. Icon + title group on left, 'View all →' CTA on right.

**Icon Container:**

| Property | Value |
|----------|-------|
| Size | 36px × 36px |
| Background | `rgba(237,105,34,0.07)` (brand orange at 7% opacity) |
| Border-radius | 10px |
| Icon | 18px SVG, outline stroke, brand orange (#ED6922), centred |

**One page departs from that box, and only above the phone: the article page (Kain, at Code's S082, on a screenshot).** His words: the header was completely disjointed, and the top of the top line of text and the bottom of the bottom line must align within the icon box sitting before it. **A 36px box against a 50.6px two-line text block cannot align by any placement**, so on that page the box is stretched to the row's own height, its width written as the same sum, 50.65, with a **24px** mark inside it.

**Above the phone only**, because below it the supporting line wraps further and a square box would reach 90px. **Scoped to the article page**, so the same header on the category hubs and the listing pages still carries the 36px box. Whether the site-wide pattern follows belongs to the section header component's own sitting, and is not decided here.

**Section Icons (see DSRD 7 §5.2 Icon Registry for canonical Lucide names):**

| Section | Lucide Icon |
|---------|-------------|
| Articles | `Newspaper` |
| Book Notes | `NotebookPen` |
| Quotes | `Quote` |
| Workbooks | `FilePen` |
| Tags | `Tags` |

**Title:**

| Property | Value |
|----------|-------|
| Font | Como 22px/600 (section header custom size) |
| Colour | Brand dark (#354149) |
| Count | In parentheses after title. Mulish 14px/400, mid grey (#8A9199). E.g. 'Articles (142)' |

**Subtext:**

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | Mid grey (#8A9199) |
| Gap | 2px below title |

*Subtext is category-specific and content-type-specific — 28 unique lines total (7 categories × 4 content types). See §20.10 for confirmed copy.*

**View All CTA:**

| Property | Value |
|----------|-------|
| Font | Como 14px/600 |
| Colour | Brand orange (#ED6922) |
| Format | 'View all [Content Type]' + Lucide `ArrowRight` (DSRD 7 §5.2) |
| Hover | Arrow nudges right 3px (per DSRD 7 §5.1 ghost button) |
| Position | Right-aligned, vertically centred with title |

**Hairline:**

| Property | Value |
|----------|-------|
| Border | 1px solid #EEEDED |
| Position | Below section header |
| Padding-bottom | 16px (above hairline) |
| Grid gap below | 20px (hairline to first card) |

### 20.8 Tag Browsing Strip

Follows the four content type sections. Uses the same section header component (§20.7) with the Tags icon.

**Section header copy:**
- Section title: "Explore by Topic"
- Section subtext: "Browse related topics across the Knowledge Hub"

| Property | Value |
|----------|-------|
| Tags per category | Psychology 12; every other category 8–10 — the count that wraps the strip to two clean rows on desktop |
| Layout | Wrapping flex row, gap 8px |
| Pill font | Como, the 12 step, 500. *(Corrected S313 from 13px, which is not a step.)* |
| Pill padding | 8px 16px |
| Pill border-radius | 20px |
| Pill background | White |
| Pill border | 1px solid #EEEDED (light grey at rest) |
| Pill text | Brand dark (#354149) |
| Pill hover | Border-colour switches to brand orange (#ED6922). Background remains white. |
| Links | Each pill links to /learn/tags/{tag-slug}/ |

*Tags are drawn from the confirmed 36-tag taxonomy (DSRD 1 §5). Psychology's twelve are 10 outcome/problem + 2 content attribute, and every category carries exactly two content-attribute tags (D5, D18). The seven confirmed strips are DSRD 2 §1.3.3's.*

### 20.9 Confirmed Hero Intros (7 Categories)

All 7 category hero intro texts are 3 sentences each, ~60–70 words. Consistent length ensures uniform hero height across all category hubs.

**Psychology:**

Psychology explores how people think, feel, behave, and make sense of the world around them. The articles, book notes, quotes, and workbooks in this category unpack the ideas, patterns, and principles that shape human experience. From classic psychological theories to practical everyday insight, this collection is here to help you better understand yourself, other people, and what it means to be human.

**Helping People:**

Helping people well calls for empathy, good judgment, practical people skills, and an understanding of what others genuinely need in life. The articles, book notes, quotes, and workbooks in this category explore the principles and practices that support human development. From communication and connection to coaching and mentoring, this collection is here to help you become more effective with people.

**Mental Wellness:**

Mental wellness comes from fortifying your inner world with honesty, humility, and greater self-awareness. The articles, book notes, quotes, and workbooks in this category explore the habits, perspectives, and practices that support emotional balance and resilience. From managing stress to building stronger mental foundations, this collection is here to help you care for yourself wisely and live with greater stability.

**Motivation:**

Motivation is about understanding what drives action, sustains effort, and keeps people moving forward with purpose. The articles, book notes, quotes, and workbooks in this category explore the mindset, discipline, and clarity that support meaningful progress. From overcoming inertia to staying focused on what matters, this collection is here to help you build momentum and follow through with intention.

**Personal Growth:**

Personal growth begins with self-awareness and deepens through reflection, wise choices, and consistent action over time. The articles, book notes, quotes, and workbooks in this category explore the attitudes, habits, and inner disciplines that support lasting personal development. From building confidence to growing in maturity and clarity, this collection will help you become more intentional in how you live.

**General Interest:**

General Interest brings together ideas and resources that support Achology's wider purpose of helping people live wise and autonomous lives. The articles, book notes, quotes, and workbooks in this category explore themes that do not fit into any one single category. From thought-provoking perspectives to enlightening philosophical ideas, this collection is here to help you reflect deeply and learn broadly.

**Wisdom for Life:**

Wisdom for Life explores the timeless principles that help people think clearly, live responsibly, and respond well to life. The articles, book notes, quotes, and workbooks in this category gather insights that support better judgment, perspective, and self-knowledge. From everyday challenges to deeper questions of meaning, this collection is here to help you live with greater awareness, maturity, and good sense.

### 20.10 Confirmed Section Subtexts (28 Lines)

One line per content type per category. These sit below the section heading in each content type block (§20.7).

| Category | Section | Subtext |
|----------|---------|---------|
| Psychology | Articles | Clear, thoughtful articles on psychological ideas and the forces that shape human experience. |
| Psychology | Book Notes | Useful notes from psychology books on how the mind, behaviour, and human nature really work. |
| Psychology | Quotes | Timeless psychology-based quotes on thought, emotion, behaviour, identity, and human nature. |
| Psychology | Workbooks | Practical workbooks for exploring psychological ideas and applying them in your everyday life. |
| Helping People | Articles | Grounded articles on relationships, communication, and the people skills for supporting others. |
| Helping People | Book Notes | Useful notes from books on building influential relationships, earning trust, and helping people. |
| Helping People | Quotes | Thought-provoking quotes on helping others with empathy, wisdom, presence, and awareness. |
| Helping People | Workbooks | Practical exercises for bolstering how you coach, mentor, or respond to other people's needs. |
| Mental Wellness | Articles | Thought-provoking articles on emotional well-being and habits that support a calmer inner life. |
| Mental Wellness | Book Notes | Enlightening notes from mental wellness books on resilience, self-care, and emotional balance. |
| Mental Wellness | Quotes | Encouraging quotes on self-knowledge, awareness, emotional IQ, and finding inner balance. |
| Mental Wellness | Workbooks | Practical exercises for building inner-resilience, self-awareness, and healthier mental habits. |
| Motivation | Articles | Enlightening articles on what drives action, builds momentum, and keeps purpose alive daily. |
| Motivation | Book Notes | Useful notes from motivational books on purpose, discipline, consistency, and follow-through. |
| Motivation | Quotes | Thought-provoking quotes on purpose, effort, persistence, and staying the course with resolve. |
| Motivation | Workbooks | Practical exercises for clarifying your priorities, strengthening self-discipline, and taking action. |
| Personal Growth | Articles | Insightful articles on self-awareness and the self-disciplines that enable lasting inner growth. |
| Personal Growth | Book Notes | Useful notes from personal growth books on character, confidence, and living with intention. |
| Personal Growth | Quotes | Reflective quotes on self-knowledge, wiser choices, and growing through life with intention. |
| Personal Growth | Workbooks | Practical workbooks to help you self-reflect honestly, choose wisely, and grow sustainably. |
| General Interest | Articles | Wider-ranging articles on ideas that support wiser living, deeper reflection, and perspective. |
| General Interest | Book Notes | Useful insights from books that offer fresh perspectives, insight, and much to think about. |
| General Interest | Quotes | Thought-provoking quotes on life's meaning, perspective, and the art of living life reflectively. |
| General Interest | Workbooks | Practical exercises for encouraging deep self-reflection and engaging with life's big ideas. |
| Wisdom for Life | Articles | Thoughtful articles on living wisely and meeting life with maturity, integrity, and perspective. |
| Wisdom for Life | Book Notes | Enlightening notes from books on meaning, character, discernment, and the art of living well. |
| Wisdom for Life | Quotes | Timeless quotes on wisdom, perspective, self-awareness, and living in a fully responsible way. |
| Wisdom for Life | Workbooks | Practical exercises for applying practical life principles and wisdom to life's everyday decisions. |

### 20.11 Decision Register (18 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Hero: white background, left-aligned, no search bar | No hero search bar; the header search serves every page (DSRD 1 §7.4, S366). Category hubs are browsing pages, not search pages. |
| D2 | Section headings: plain content type names with subtext for all 4 sections | Unified rhythm across all sections. 28 lines of subtext copy confirmed in-session. |
| D3 | Category cross-navigation: horizontal pill strip below hero | Mega menu has content-type tiles, not category links. Pills give direct category-to-category access. |
| D4 | Workbooks section: featured CTA card (2-col span) for free workbook + standard cards | Keeps section rhythm consistent while giving email capture the prominence it needs. |
| D5 | Tag browsing strip: wrapping pill row, 8–12 per category, editorially curated | Tags already locked in DSRD 1 SS5. No new planning needed. Visual treatment resolved in prototype. |
| D6 | Content ordering: newest first (PERMANENT). Popularity metric KILLED. | Primary discovery is Google, LLM citations, and tag/category URLs. Popularity metric adds complexity with negligible benefit. |
| D7 | Listing page sort: Newest (default) + A-Z as secondary option | Cheap to build, useful for visitors looking for a specific title. |
| D8 | Vertical rhythm: 48px section-to-section, 40px pills-to-first-section, 20px subtext-to-grid | Spacious-over-busy. 48px is the dominant rhythm. Hero internal spacing tighter (4/10/16px asymmetric). |
| D9 | Alternating featured cards: Articles LEFT, Book Notes RIGHT, Quotes LEFT, Workbooks RIGHT | Zigzag prevents four identical grids. Each featured card reflects its content type personality. |
| D10 | Featured card treatments: article=horizontal editorial, book note=§6.2 horizontal, quote=wider+22px, workbook=dark CTA | Each content type has its own visual personality at the featured level, not just a bigger version of the same card. |
| D11 | Hero overline 'Category' in mid grey, H1 category name in brand orange | Strong wayfinding signal. Orange ties visually to the active category pill below. |
| D12 | Hero intro max-width expanded from 720px to 880px | Ensures 3-sentence intros consistently land at ~4 lines on desktop. |
| D13 | Home icon added to breadcrumbs (13px house outline, mid grey) | Visual anchor at start of breadcrumb trail. |
| D14 | Icon-led section headers with 36px tinted container, title+count+subtext grouped, hairline below | Creates editorial structure. Each content type has a distinct icon. Counts in parentheses after title. |
| D15 | Counts appear at two levels: hero subtitle (all 4) + section headers (individual) | Hero gives scale at a glance. Section headers give specifics where they matter. |
| D16 | Hero subtitle counts are clickable links to listing pages | The data is already there — making it clickable adds utility with zero visual cost. |
| D17 | Hero spacing: overline-to-H1 4px, H1-to-subtitle 10px, subtitle-to-intro 16px | Asymmetric rhythm (4/10/16) reinforces hierarchy. Each gap noticeably wider than the last. |
| D18 | Psychology tag strip: 12 tags (10 outcome/problem + 2 content attribute) | Broadest category gets the most tags. Wraps to clean two rows on desktop. |

### 20.12 Confirmed Search Descriptions and Page Titles (7 Subjects; Kain, S381)

The meta description of each subject page, written by Kain at S381 on Chat's drafts from the §20.9 intros. Each is under 155 characters and opens on the subject's name or its keyword. Set in Rank Math's own description field on each `kh_category` term, never in the WordPress term description (the theme reads that as a fallback intro). Workbooks are left out until the first workbook publishes; add them then.

| Subject | Search description |
|---|---|
| Psychology | Psychology articles, book notes and quotes on how people think, feel and behave, from classic theories to practical insight into human behaviour. |
| Helping People | Enlightening articles, book notes and quotes on the topic of helping people, communication, coaching, mentoring, and positively influencing others. |
| Mental Wellness | Mental wellness articles, book notes and quotes on self-awareness, managing stress and building resilience, so you can develop yourself wisely. |
| Motivation | Motivation articles, book notes and quotes on what drives action, how to overcome inertia, stay focused, and how to follow through with intention. |
| Personal Growth | Personal growth articles, book notes and quotes on self-awareness, confidence, maturity and the habits that help you live life more effectively. |
| General Interest | General interest articles, book notes and quotes on the big ideas that fit no single category, from thought-provoking perspectives to philosophy. |
| Wisdom for Life | Wisdom for life: articles, book notes and quotes on thinking objectively, living responsibly and meeting life's everyday challenges with good sense. |

**The seven page titles (Kain, S381, on Chat's drafts: "Yes, they are perfect!").** Set in Rank Math's SEO title field on each `kh_category` term, replacing the default "%term% Archives". Each opens on the subject's name and stays under 60 characters with " | Achology" added.

| Subject | Page title |
|---|---|
| Psychology | Psychology: How People Think, Feel and Behave |
| Helping People | Helping People: Coaching and Communication |
| Mental Wellness | Mental Wellness: Managing Stress and Resilience |
| Motivation | Motivation: Why We Act and How to Follow Through |
| Personal Growth | Personal Growth: Confidence and Better Habits |
| General Interest | General Interest: Big Ideas Worth Thinking About |
| Wisdom for Life | Wisdom for Life: Think Clearly, Live Responsibly |

### 20.13 Prototype Reference Files

Desktop prototype: `category-hub-psychology-v9.html` — ninth iteration, locked at V9. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. Psychology category used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

Responsive prototype: `category-hub-responsive-review.html`. Full three-breakpoint design locked. Covers all phone and tablet behaviour specified in §20.14. Lightweight version: `category-hub-responsive-review-lightweight.html`.

### 20.14 Phone and Tablet Responsive Behaviour (LOCKED)

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

**Page container padding**

| Breakpoint | Padding |
|-----------|---------|
| Desktop (≥1024px) | 0 48px |
| Tablet (768–1023px) | 0 32px |
| Mobile (<768px) | 0 20px |

**Hero section**

| Element | Tablet | Mobile |
|---------|--------|--------|
| H1 (category name) | 28px | 26px |
| Intro copy | 16px | 15px, max-width 100% |
| Counts subtitle | 14px | 13px |

**Category pill strip**

Wraps to multiple rows at all narrow widths. No horizontal scroll. Gap 8px maintained.

**Section header**

At desktop and tablet: title group left, "View all →" CTA right — inline on the same row.
At mobile (<768px): "View all →" CTA drops to a new row below the title group, indented 48px to align with title text (past icon + gap).

**Card grid collapse**

| Breakpoint | Columns |
|-----------|---------|
| Desktop (≥1024px) | 3 columns |
| Tablet (768–1023px) | 2 columns |
| Mobile (<768px) | 1 column |

**Featured cards (spanning behaviour)**

At desktop: featured card explicitly placed at columns 1–2 (LEFT) or 2–3 (RIGHT). Standard card fills the remaining column.

At tablet (2-column grid): featured card spans both columns (full width). Standard card from row 1 drops to row 2 and pairs with the next standard card. Featured-RIGHT cards use CSS `order: -1` to pull to the top of the grid.

At mobile (1-column grid): all cards full width, stacked vertically. Featured cards appear first in source order or via `order: -1` on RIGHT-positioned featured cards.

**Featured article card (§6.5) — horizontal collapse**

At tablet: stays horizontal (image left, content right). Image width reduces to 38%.
At mobile: flips to vertical (image top 200px, content below). Image fills full width.

**Featured book note card (§6.2 horizontal) — horizontal collapse**

At tablet: stays horizontal. Cover panel width reduces to 36%.
At mobile: flips to vertical (cover panel top 200px, content below).

**Featured workbook CTA card (§6.7) — horizontal collapse**

At tablet: stays horizontal. Image area width reduces to 36%.
At mobile: flips to vertical (image area top 180px, content below).

**Featured quote card (§6.6) — no horizontal element**

Vertical at all breakpoints. Simply spans full width at tablet and mobile.

**Tag browsing strip**

Wraps naturally at all breakpoints — no horizontal scroll. Same 8px gap maintained.

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

---

## 21. Knowledge Hub Listing Page Layout (LOCKED S220; RE-CHECKED AGAINST THE CURRENT FOUNDATIONS, S313)

Single shared template covering 32 pages: 28 category-specific (7 categories × 4 content types, URL pattern `/learn/{category}/{content-type}/`) and 4 cross-category (URL pattern `/learn/{content-type}/`). Confirmed at prototype V10.

**Why this section was re-checked and what it means.** It was locked before four things the site now runs on: the nine-step type scale (DSRD 7 §3.0, Kain S056), the hairline block-separator standard (DSRD 7 §4.3, Kain S224), the supporting-line grey ruling (S280), and the body face (Kain, Code S085). **Locked is not the same as current.** Every correction below is conformance to a standard Kain has already ruled, taken on the same ground as the S280 pass: no new visual choice was made here, and none was his to make twice. The corrections are made in the section body, which is where this document's own note at §21.10 says the operative specification lives.

**Three things are deliberately NOT corrected here, and each is named rather than silently left.** The tablet and phone type sizes below sit off the nine-step scale, and **the responsive rule is one of the two type rulings still open** (DSRD 7 §3.0): re-deriving them here would be taking a decision that is Kain's on a render. The prototype is pre-Mulish and is re-cut under the S311 ruling. And nothing in this section has been seen rendered since these corrections, so it goes to Kain's eye in Safari before it is called done.

### 21.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§21.3)
3. Mini hero (§21.2)
4. Content-type pill strip + sort toggle — unified control bar (§21.4)
5. Hairline transition (§21.5)
6. Card grid (§21.6)
7. Numbered pagination (DSRD 7 §17.1)
8. Rainbow stripe + footer (DSRD 8 §19)

### 21.2 Mini Hero

- **H1:** "[Category] [Content Type]" (e.g. "Psychology Articles") — Como, the 33 step, 700, brand orange #ED6922, line-height 1.2. *(Corrected S313 from 32px, which is not a step on the nine-step scale; the same correction §22.4's H1 took at S302.)*
- **Count:** "[X] [Descriptive Label]" — Mulish 14px/400, **soft grey #5E6B75**, margin-top 6px. Labels per content type: "In-Depth Articles", "Original Book Notes", "Enlightening Quotes", "Practical Workbooks" (see DSRD 7 §17.1). *(Colour corrected S313 from mid grey: this is a supporting line under a heading, which is exactly what Kain's S280 ruling moved to the soft grey, and DSRD 7 §1.1 forbids mid grey for anything a reader needs.)*
- **Intro:** 1 sentence — category-specific from §20.10 subtexts, or cross-category text from DSRD 2 §4.3. Mulish, the 16 step, 400, brand dark #354149, line-height 1.6, max-width 880px, margin-top 18px. *(Corrected S313 from 17px per the approved S056 override, which maps 17 to 16.)*
- **No overline** — category name is part of the H1
- **Hero container:** max-width 1200px, padding 20px 48px 0. The 880px intro measure sits inside it, which is the pattern DSRD 7 §4.1 already names for the category hub: the frame is 1200, the prose inside it is 880

### 21.3 Breadcrumb

Reuses §20.3 breadcrumb component.

- **Category-specific pages:** `Home` icon `ChevronRight` Learn `ChevronRight` [Category] `ChevronRight` [Content Type]
- **Cross-category pages:** `Home` icon `ChevronRight` Learn `ChevronRight` [Content Type]
- *(Corrected S378: both rows read "Home icon, Home, Learn". The house icon is the Home link, per the trail Kain signed as built at S090, DSRD 8 §25.)*

### 21.4 Content-Type Pill Strip + Sort Toggle (Unified Control Bar)

- **Layout:** flex row, justify-content space-between, align-items centre
- **Left group:** content-type pills (Articles, Book Notes, Quotes, Workbooks) — each links to `/learn/{category}/{content-type}/`
- **Right group:** sort toggle pills (Newest, A-Z)
- **All pills share:** Como, the 12 step, 500, 8px 16px padding, 20px border-radius. *(Corrected S313 from 13px, which is not a step; the approved S056 override maps 13 to 12.)*
- **Content-type active:** brand orange bg, white text
- **Content-type inactive:** off-white #F3F4F4 bg, brand dark text
- **Content-type hover:** brand orange at 10% opacity bg
- **Sort active:** brand orange bg, white text
- **Sort inactive:** off-white #F3F4F4 bg, **soft grey #5E6B75** text. *(Corrected S313 from mid grey: a pill label is a control label a reader reads, and the 2026-07-13 contrast audit already made exactly this correction to the inactive pagination pills.)*
- **Sort hover:** brand orange at 10% opacity bg, brand dark text

### 21.5 Hairline Transition

- 1px solid #EEEDED
- Max-width 1200px, centred
- **48px above and 48px below on desktop and tablet, 32px and 32px on phones (corrected S313).** This is a boundary between two page-level blocks, so DSRD 7 §4.3 governs it: one measurement, every page, every block boundary. It previously carried 24px above and 20px below, which §4.3 ruling 2 names outright as a defect rather than a variant, because a page-local spacing value is what that standard exists to remove. The element carrying the line owns the whole measurement, and the blocks either side contribute zero

### 21.6 Card Grid

- **Columns:** per DSRD 7 §17.1 — 3 desktop (≥ 1024px), 2 tablet (768–1023px), 1 mobile (< 768px) (per DSRD 7 §4.1)
- **Gap:** 24px (var(--grid-gap))
- **Card type per content type:** article card DSRD 8 §6.1, book note card DSRD 8 §6.2 (vertical), quote card DSRD 8 §6.3, workbook card DSRD 8 §6.4
- **No featured cards** on listing pages — featured cards are category hub (§20) only

### 21.7 Hero Vertical Rhythm

| Transition | Spacing |
|-----------|---------|
| Header bottom → breadcrumb | 48px (var(--sp-2xl)) |
| Breadcrumb → H1 | 20px |
| H1 → count | 6px |
| Count → intro | 18px |
| Intro → pill strip | 24px (var(--sp-lg)) |
| Pill strip → hairline | **48px (corrected S313, DSRD 7 §4.3)** |
| Hairline → first card row | **48px (corrected S313, DSRD 7 §4.3)** |

*The two hairline measurements were 24px and 20px. They are the one place this page set its own values against a site-wide standard ruled after it was locked, and §4.3 ruling 2 requires the page to inherit rather than keep a local variant. Every other row above is untouched: they are internal hero rhythm, not block boundaries, and §4.3 does not reach them.*

### 21.8 Prototype Reference Files

Desktop prototype: `listing-page-psychology-articles-v10.html` — tenth iteration, locked at V10. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. Psychology Articles used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

Responsive prototype: `listing-page-responsive-review.html`. Full three-breakpoint design locked. Covers all phone and tablet behaviour specified in §21.9. Lightweight version: `listing-page-responsive-review-lightweight.html`.

### 21.9 Phone and Tablet Responsive Behaviour (LOCKED)

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

**Page container padding**

| Breakpoint | Padding |
|-----------|---------|
| Desktop (≥1024px) | 0 48px |
| Tablet (768–1023px) | 0 32px |
| Mobile (<768px) | 0 20px |

**Mini hero**

| Element | Tablet | Mobile |
|---------|--------|--------|
| H1 | 28px | 26px |
| Count | 14px | 13px |
| Intro copy | 16px | 15px, max-width 100% |

*Type scale reductions mirror the category hub hero pattern (§20.14). H1 stays Como/700; count stays Mulish/400; intro stays Mulish/400. Only size reduces.*

**Four of these six sizes sit off the nine-step scale (26, 13, 16 is a step, 15), and they are deliberately not corrected here (S313).** The responsive rule is one of the two type rulings DSRD 7 §3.0 records as still open, waiting on its own rendered options for Kain's eye. Re-deriving them on paper would take a decision that is his, so they stand as built and are named here as owed to that ruling rather than left looking settled.

**Control bar — unified pill strip + sort toggle (§21.4)**

At desktop and tablet: single flex row, space-between. Content-type pills left, sort toggle right. No changes from desktop spec.

At mobile (<768px): two rows.
- Row 1: content-type pills (Articles, Book Notes, Quotes, Workbooks) — flex-wrap allowed, 8px gap
- Row 2: sort toggle (Newest, A–Z) — right-aligned via `justify-content: flex-end`
- Gap between rows: 10px

*At 375px viewport the full pill strip and sort toggle cannot fit in a single row. Two rows preserves all controls without truncation or horizontal scroll. Tablet (768px+) fits comfortably in a single row.*

**Card grid collapse**

| Breakpoint | Columns |
|-----------|---------|
| Desktop (≥1024px) | 3 columns |
| Tablet (768–1023px) | 2 columns |
| Mobile (<768px) | 1 column |

*Standard cards (§6.1–6.4) are all vertical-stack layouts — no internal reflow needed at any breakpoint. They simply fill the grid column width.*

**Pagination**

At desktop and tablet: full numbered row. 40×40px pills, 10px border-radius, 6px gap. Como 14px/500.

At mobile (<768px): compact truncated. Pill size maintained at 40×40px. Page range shows: ← [first] ··· [current−1] [current] [current+1] ··· [last] →. Ellipsis rendered as `···`, styled at mid grey, pointer-events none.

*At 375px with 20px gutters (335px usable), the compact 7-element row fits within the available width. Full numbered range would overflow.*

**Spacing reductions at mobile (DSRD 7 §4.1 token reductions)**

| Transition | Desktop/Tablet | Mobile |
|-----------|---------------|--------|
| Header bottom → breadcrumb | 48px (var(--sp-2xl)) | 32px |
| Pagination above | 48px (var(--sp-2xl)) | 32px |
| Footer above (last content → rainbow stripe) | 64px (var(--sp-3xl)) | 48px |

*All other listing page spacing values (hero internal rhythm, pill strip gaps, hairline margins, card grid gap) are unchanged across breakpoints.*

### 21.10 Decision Register (5 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Mini hero type scale reduces at tablet (H1 28px, intro 16px, count 14px) and mobile (H1 26px, intro 15px, count 13px) | Mirrors §20.14 category hub hero pattern exactly. Maintains visual hierarchy at narrow widths. |
| D2 | Control bar at mobile: two rows — content-type pills row 1, sort toggle row 2 right-aligned, 10px gap | Single-row space-between layout breaks below 768px. Two rows keeps all navigation controls visible and accessible without horizontal scroll. Tablet keeps single row. |
| D3 | Pagination at mobile: compact truncated (first · current±1 · last with ellipsis). 40×40px pill size maintained. | 40×40px pills fit the compact range within 335px mobile usable width. Truncation follows the first/current±1/last pattern — always shows anchors (first + last) and immediate context (current ±1). |
| D4 | Spacing reductions: header→breadcrumb 48→32px, pagination above 48→32px, footer above 64→48px at mobile | Follows locked DSRD 7 §4.1 sp-2xl and sp-3xl mobile reduction rules. No bespoke overrides — system tokens handle it. |
| D5 | Standard cards (§6.1–6.4) require no internal reflow at any breakpoint | All four standard card types are vertical layouts. They collapse cleanly via grid column reduction. No internal layout decision needed — confirmed by prototype review. |

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

---

## 22. Individual Article Page Layout (LOCKED)

**THE THREE READING PAGES, S149 AND S150 (Kain, live with Code in Safari, theme 0.707.110 to 0.707.120; recorded by Chat S405 from RULING__The_Reading_Pages_Sitting_S149 and RULING__The_Hero_Label_In_The_Date_Line_S150, channel Archive).** These bind the article, the book note (section 32) and the quote page (section 40) alike, and where they and an older line in any of the three sections disagree, these govern. The values live in the design folders' prototypes and build sheets (Code's fold-back, Rule 14); this note records the rulings.

1. **The contents box is the rail (0.707.110).** Heading Como 24, 600, the dark, no spaced capitals; a count line Mulish 12 soft grey, 4 under it; section names Mulish 14, 400; numbers Como 12 orange (book notes and quote pages only; articles carry none); a hairline down the list's left edge in the site hairline; the current section an orange stretch on the rail with its name orange at 600; sections read draw soft grey. The pill rows are gone. Supersedes the contents card in section 22.5a. Kain turned down a grey card ("just creates even more crush").
2. **The mark behind the contents (0.707.110).** One large Achology bubble at 7%, tilted, half off the block's foot to the right, cropped by the block. Tab 3 of four: "I absolutely love it ... happy to lock that in".
3. **The date line is one standard on all three pages:** Mulish 14, 400, white at 85%, links included. Supersedes the S115 book note override of 16 and 500.
4. **The type link in the date line (S150, 0.707.120; supersedes S149's "Visit Knowledge Hub").** The orange label above the hero title is removed on all three pages. The date line ends with the type's link to its list, same tab, the date line's link style: "Articles at Achology" (/learn/articles/), "Wise Quotes at Achology" (/learn/quotes/), and on book notes View on Goodreads then "Book Notes at Achology" (/learn/book-notes/). Tab 1 of four. Supersedes the S130 label above the title.
5. **One hero for the three pages, from 1280 wide (0.707.115).** Title 16 above the summary, summary at 1.6 leading, date line 16 under it; the picture runs from the breadcrumb's line to the date line's (the article picture and quote square crop to fill; the book cover keeps its shape, sized from the height; supersedes the quote page's S146 lift of 35); the breadcrumb is held to the words' width on their left edge. Below 1280 the heroes keep their earlier layouts; that band is still open.
6. **The consistency audit (0.707.111).** Book note links take the article's quiet underline (32% orange, 3 below, full on hover). On book notes and quote pages the panel's line beside the contents is the site hairline with 48 either side (supersedes S115's 32; articles keep no line there, S148). The panel's grey #E1E5E5 becomes the site hairline (contents lines, open and close ring, share circles).
7. **Author article titles (0.707.112).** The question at 700, the series ending after it ("His Biography, Ideas and Life Works") at 500, the book note's own pair. Verified on 51 of 51.
8. **The quote page's Download, Share and Copy row (0.707.110).** Gap 32 (was 24); dividers in the site hairline (supersedes S146's mid grey, section 40 item 2); Download no longer bold.
9. **Related Further Reading** is gone from quote pages at every width, phones and tablets included, as Kain ruled at S146.

**Kain's verdict on the three, S405 in Chat:** apart from the editorial sweep, the article, book note and quote page templates are "good to go".

**THE S150 SITTING, WHOLE-DOCUMENT PASS (Kain, live with Code in Safari, Code's S150, theme 0.707.121 to 0.707.135; recorded by Chat S408 from RULING__The_Hero_Picture_Speech_Bubble_And_Line_S150, RULING__Author_Articles_Open_The_Panel_With_Their_Own_Picture_S150, RULING__Author_Article_Portrait_Takes_The_S147_Treatment_S150, RULING__The_Rest_Of_The_S150_Sitting and REPLY__Book_Note_Closing_Line_Live_S150).** The label ruling above (item 4) belongs to the same sitting. These continue the numbering and govern where any older line in sections 22, 32 and 40 differs; each older line they touch carries a pointer to them. Widths below are Code's own: the sitting worked from 1200 wide up, and item 5 above says 1280 for the one hero. The two figures are not reconciled by any record read this session; which is right for the hero is Code's to state in his next ruling file, and the band below the stated width is still open (item 10 below).

10. **The hero picture is cut to a speech bubble, with a line behind it (0.707.121).** Kain, on the band's ground: "so neat ... really impressive"; on the picture over it: "just dropped ... dumped there. It's like no effort has gone into designing this". Four rendered tabs on all four page types (into focus, mounted print, layered orange line, speech bubble), then "I actually really like the speech bubble ... the speech bubble with the layered line, like an integration of both." Round three, after he asked for the book note's line and the other pages' line to be standardised: "That's actually much, much neater." As built, from 1200 wide up: on the article, the author article and the quote page the picture is cut to the Achology speech bubble outline (the mark's outer shape, no inner letter), 216 wide at the right of its column, the book note's book footprint. On all four pages a thin orange line in the same bubble shape sits behind the picture or the book, the same size and shifted 40 left and 24 down; the gap from the words to the line is the same column gap on every page. The book note's book is unchanged and its line follows the book's own size (verified on four book notes including a taller cover). Everything stays inside the band (the S146 rule). **The three loose Achology bubbles behind the hero picture are removed** on the quote page, the book note and the article. This supersedes the S146 three-bubble ruling (section 40 item 1), the S147 one (section 32 item 3) and the S148 one (section 22.14 item 1). The author photograph's three bubbles in the writing are a different thing and stand (section 32 item 13; section 40 item 5). **Below 1200 wide the hero is still open**, and was named by Code as the next job of the sitting; Chat takes whatever he rules as one later edit.
11. **Author articles open the side panel with their own picture (0.707.122).** Kain: "especially on the articles, as I kind of scroll down the page, on the book authors articles, we have the Know Your Psychology block above the table of contents. It would be great if that could just be the article image. Because the table of contents isn't as broad as what many of the other articles are." On an author article (a title ending "His, Her or Their Biography, Ideas and Life Works", 51 of 51 on the build site) the band that opens at the top of the panel once the hero scrolls away showed the article's own picture, 256 square, above the contents; every other article kept the S148 Know Your Psychology picture there. **The panel's order was then superseded by item 13 below**: the picture now rests at the panel's foot, and Know Your Psychology has left the panel on every article. This narrows section 22.14 item 5 and then ends it.
12. **The author's portrait in an author article takes the book note's treatment (0.707.125).** Kain, on the photo floated left beside the second paragraph: "give that the same treatment that you would do with any other image across the other articles. In that position". The book note and the quote page already gave the picture in that position his S147 choice (tab 3 of four): the photo 224 wide and a 32 strip on its right holding three Achology bubbles, large at the top corner, medium at the photo's foot, turned, small between. Author articles now carry the same, at the same values (section 32 item 13), from 768 wide up; on a phone the photo keeps its plain, centred look.
13. **One side panel on articles, author articles and quote pages (0.707.128 to 0.707.132).** Kain: "keep the table of contents floating at the top right ... as soon as the hero banner is out of view through scroll the image ... rises in", and on articles: "the image maybe gets locked to the bottom of the right-hand bar ... it sits in the bottom corner of the viewing screen ... until it hits that hairline". As built, from 1200 wide on screens 760 tall or more: the contents at the top, ending at their last item, then the site hairline with 48 under it; the page's own picture at the foot of the screen once the hero has gone, never closer than the 48 under the hairline, and left out where it cannot fit. On articles and author articles that picture is the speech bubble and its line, 216 wide. **Know Your Psychology leaves the panel on every article** (this supersedes section 22.14 item 5 and the Know Your Psychology lines in the S112 round above, the side column paragraph and its table row, so far as the panel is concerned). On quote pages Kain: "replace the know your psychology logo with the book or the course image ... then the view the book on Amazon link must change and become View this Course on Achology": the panel carries the quote's source cover, the book's for the 75 book quotes and the course's for the 201 course quotes; the author's picture leaves the panel ("we can lose the author image"; it stays in the hero); book quotes keep "View the Book on Amazon" and course quotes take "View this Course on Achology" to the course page; Know Your Psychology leaves the quote panel's foot. The quote page's cover has no decoration behind it (Kain: "for books and courses that pop in ... they don't have background decoration") and is the book note panel's cover exactly, 256 by 357 with the book's own shadow (Kain: "I did not ask you to make them different I just said keep them the same").
14. **Subtitles: two lines on articles, author articles and quote pages, three on book notes (0.707.127).** Kain: "put in place a rule that restricts the subtitle of each article from crossing over onto three lines ... it's just kind of skewing the images", then on book notes: "because books are naturally deeper images it's okay, in fact it would actually be preferable if all subtitles carried over on three lines". From 1200 wide the article and quote page subtitle runs the words' whole column (800) instead of the S112 measure of 55ch; measured in the real font, all 390 articles and 276 quote pages now take two lines (237 ran to three before). Book notes take a 768 measure, the width that lands most on three. **The two lines are balanced (0.707.133).** Kain: "a rule ... that would make it more likely for the two lines to be as equal in length as possible"; the browser's balanced wrapping on the article and quote page subtitle (677 and 674 pixels on the mindfulness article).
15. **The book note stays as it is (Kain, S150): "as one stated rule ... the book note must remain as it is and it cannot change".** He then changed it on his own word twice, items 16 and 17 below, and the closing line at item 19.
16. **The book note panel's cover and button sit at the foot of the screen (0.707.135).** Kain, on the Boundaries book note: "the buy book button is positioned incorrectly on the right side panel (it should sit on the bottom via scroll)". The book note keeps its own panel otherwise; only the cover and its button sit at the foot of the screen, as on the quote page.
17. **The book note's five headings are replaced again (Kain, S150; the new five are at section 32.7).** Theme live from 0.707.133, page by page; the 150 bodies are not yet changed.
18. **Boundaries (boundaries-cloud), on Kain's report and his "yes" to download.** The cover file was the wrong book's (Boundaries in Dating). It is now the current edition's cover (994 by 1500, from its Amazon listing) and the image's sizes were regenerated. Still owed with the publishing clearance: a new file name for the cover (browsers keep the old picture for a year under one address) and the Amazon link and ISBN moved to the current edition, 0310351804 (the 2008 edition's address answers Page Not Found). The record's `source_book_author` reads "Henry Cloud" only; the book is by Henry Cloud and John Townsend, and the record is corrected to both when the 150 bodies move.
19. **The book note standfirst's closing line (Kain, S407; built 0.707.133).** "Keep reading to decide if this book deserves a spot on your shelf." It replaces the S102 fixed sentence at section 32.3 and section 32.9 item 1. Across all 150 book notes, measured in the real font at the 768 measure: 112 run to three lines, 29 to two, 8 to four and 1 to five. The nine past three are Man's Search for Meaning, Money Master the Game, The Science of Being Well, Boundaries, Open When, Before Happiness, The Stoic Challenge, Critique of Practical Reason and Mothers Who Can't Love. The line count is Kain's eye in Safari, not decided here; it turns on the summaries' length, not the theme.

**Carried by Code, not done at S150:** the hero below 1200 wide; the fold-backs of the three design folders into prototype and build sheet (Rule 14); the Listing page and Category hub faults; and Kain's yes or no on the Know Your Psychology picture at the article foot on tablets and phones, and whether Know Your Psychology should come back at the foot of the article panel.

Single-column editorial layout for individual Knowledge Hub articles (e.g. /learn/psychology/articles/self-awareness/). One shared template across all ~500 articles. Prototype file: `article-page-self-awareness-v2.html`.

**THE S148 SITTING GOVERNS WHERE IT DIFFERS (Kain, live with Code in Safari, S148; written S404).** Eight rulings took the quote page's and book note's components onto the article page; they are recorded in §22.14 and govern any line below that says otherwise.

**FIVE SUPERSESSIONS TAKEN AT S268, on Kain's approval.** This section was locked before each of the rulings below, and in every case the later ruling governs. The corrections are made in the section body, which is where this document's own note at §22.12 says the operative specification lives. The page's own signed spec is being written in the Article Page folder under Knowledge Hub Design Prototypes, and seven further items on this page are open with Kain.

| # | What this section said | What now governs | Where the later ruling lives |
|---|---|---|---|
| 1 | Two course cards, in a two-column grid | Three at desktop, two side by side at tablet, two stacked on a phone | DSRD 1 §3.4, which records that its own row said two until S253 and was corrected. §32.1 of this document already carries the same three-at-desktop ruling for the book note page (Kain, S252) |
| 2 | Courses tag-matched from the same category | The page reads its `lead_tag` field and fills the slots from that tag's mapped course list, topping up from the next tag and skipping duplicates. Never from the category, never by hand | DSRD 1 §5.7, ruled S253 and tightened S255 |
| 3 | Compact cards at DSRD 8 §6.8 | The compact card is DSRD 8 §6.9. §6.8 is the featured book note card. The same stale pointer in DSRD 2 §1.5 is corrected in the same pass | DSRD 8, read S268 |
| 4 | The author name links to "the author page" | The byline names the Achology pen name or instructor who wrote the piece and links to their profile at `/about/instructors/{slug}/`. The source author is a different person with a different page at `/learn/authors/{slug}/` | DSRD 1 §3, which distinguishes the two senses of author explicitly |
| 5 | The signature block carries a one-line bio | The bio comes from the people registry in the theme, never written into a page and never carried in an upload file | The same rule already ruled for the book note page at DSRD 2 §1.6 |

**THE PAGE IS SIGNED, AND A SECOND ROUND OF SUPERSESSIONS CAME WITH THE SIGNING (Kain, at Code's S082, on the rendered live page in Safari, one variable at a time).** His words before the final tidy: "I am 100% happy with this template page now." Where a section below carries an S082 ruling, that ruling governs and the older text beneath it is kept as a record rather than deleted, so a reader meeting the old shape in an old file can recognise it.

| What changed | Where it is written |
|---|---|
| The foot is reordered: the course row above the reading row, and the page closes on the site's own enquiries panel | §22.1 |
| The category pill's stylesheet rules, still shipping after the pill went at S080, are deleted | §22.4 |
| The contents and share card, every value in it, and the 36% width fault it exposed | §22.5a, new |
| The author signature block's off-white band is withdrawn on this page | §22.7 |
| Related Further Reading becomes a list of links, with new copy in Kain's own words | §22.8 |
| Explore Related Learning Paths takes new copy in Kain's own words, and becomes Discover Related Learning Paths | §22.10 |
| The Where next panel comes off this page, with the back-link consequence measured | §22.10a |
| The section header's icon box stretches to its two-line text, on this page only | §20.7 |
| Five icon keys registered, and the heading-mark size and colour rules | DSRD 7 §5.2.1 |
| The course card's picture box takes the artwork's own ratio rather than a fixed height | DSRD 8 §7.1 |

**Two machine lines on this page's readiness record still fail, and neither belongs to this template.** Both are component work: a meta description written into the specimen article's own content record, and a contrast rule failing on nodes inside the course card and the site header. They are recorded at DSRD 8 §7.7 and are not this page's to close.

**A THIRD ROUND OF SUPERSESSIONS, FROM CODE'S S108 TO S110 SITTINGS WITH KAIN IN SAFARI (folded S357).** The page changed shape at S110. Where a subsection below carries an S108 to S110 note, that note governs and the older text is kept as a record. The one block standard for every article-type page (Kain, S109: "one design standard that we can apply to all block components in all article type pages") governs this page, the book note, the quote page, the help answer and every Knowledge Hub template still to be built; it is recorded in full immediately below this table and summarised here: the top of the page carries the trail, the title, one plain sentence at reading size, the reading bar, then the writing, and nothing else; a picture earns its place only by telling the reader something the words cannot; the reader reaches the first sentence without scrolling; every block sits in the reading column, one gap owned once, three text sizes, no repeated string above the writing, one job one component drawn once, nothing empty, heading then content then one action.

| What changed | Where it is written |
|---|---|
| The page opens on the Knowledge Hub hero band (`kh-hero`, DSRD 8 §28), not on a breadcrumb over a title on white; the band holds the trail, an overline, the title, the standfirst, the writer line and the article's picture at the right, all on the 880 column | §22.3, §22.4 |
| The 1104 hero width is retired on this page; the whole page has one left edge at 880 | §22.2, §27 |
| The featured image is the band's ground and an object in it; the 880 by 420 banner is gone | §22.5 |
| The meta line is the shared reading bar (DSRD 8 §26): writer, date, reading time, joined at the left, no word count, no Listen control on this type | §22.4 |
| The S082 contents and share card is replaced by the S110 contents card (DSRD 8 §27), floated right beside the writing with the share row as its footer | §22.5a |
| The section divider is a quarter finer and thirty per cent shorter | §22.2, S085 ruling 6 |
| The space under the page title is 8 where the reading bar follows, 24 where reading text follows | DSRD 7 §4.3 |

**The one block standard for every article-type page (Kain, Code's S109 sitting; the file is `RULING__One_Block_Standard_For_Every_Article_Page_S109`). Governs the article, the book note, the quote page, the help answer and every Knowledge Hub template still to be built.** Kain's words: "I simply want one design standard that we can apply to all block components in all article type pages", and "i am so tired of trying to guess with you". Four things he settled first, each a yes: the job of the top of the page is that a reader decides in a few seconds whether the piece is for them; the top carries where they are, what this is, one plain sentence saying what they get, then the facts that say what it costs them, then the writing; a picture earns its place only by telling the reader something the words cannot; a reader reaches the first sentence of the writing without scrolling.

*Part one, the top of every article-type page, in this order and nothing else above the writing:* the trail, in the reading column, aligned with the title; the title at the page-title step, on white or in the band, never on a picture; one sentence at reading size and reading colour, never caption-sized and never grey; the facts, which is the reading bar; then the writing. The page's own picture sits beside those words, never behind them, and only where it says something (the cover on a book note, the card on a quote page; nothing on a help answer or an article whose picture is decoration). Test: at a laptop's first screen, unscrolled, the first sentence of the writing is readable.

*Part two, the eight rules every block obeys:* (1) one column, every block in the reading column, spanning the page only where Kain has ruled that one by name; (2) one gap, owned once, the same value everywhere, every hairline 48 above and 48 below; (3) three text sizes, the page title, the block heading, the reading text, nothing between; (4) a picture earns its place or is not there; (5) no block repeats what the page has already said, no label repeating the trail, no second name beside the title; (6) one job, one block, drawn once, the same job on two page types is one component; (7) nothing to show means nothing drawn, no empty frame or placeholder; (8) every block runs heading, then content, then its one action. The tests: a block outside the column names its ruling; the gap between any two blocks measures the ruled value with one side declaring zero; no rendered size is off the scale; no string appears twice above the writing; two page types drawing one job share one class; no rendered block is empty. **The gate takes rule 2 first (Chat's call, S357):** the one-gap test is the fault that produced the S109 sitting and the one the existing rows do not yet measure; rule 3 is already held by `css_gate.py`. **Rule 3's three sizes are now named numbers (Kain, Code's S111 foundations sitting; recorded S357): the page title at 33 (28 on a phone), every heading at 24 whether it sits inside the writing or opens a block, and the reading text at 18 on 1.75, in a column of 800 with 16 between paragraphs.** DSRD 7 §3.1, §3.2, §4 and §4.1 hold each value; this page and every reading page reads them from there. Bringing the four built page types into line with part one is a sweep, started only on a signed brief; the reading bar on all four (S109) was its first part, and the S111 values landed on the article, the book note and the help answer at Code's S112.


**A FOURTH ROUND OF SUPERSESSIONS, FROM CODE'S S112 SITTING WITH KAIN IN SAFARI, ONE CHANGE AT A TIME ACROSS A FULL DAY (folded S358). Theme 0.377.0.** The S111 sweep was started and the article page turned into a redesign. Kain at the close: *"This page is unique. I've never seen an article page anything like this before."* **Where the third round above and this round disagree, this round governs**, and the third round's text is kept as the record of what stood when it was written. The largest reversal is the page's grid: S110 put everything on one 880 left edge, and S112 puts the whole page back on a two-column grid.

**The grid, which is the ruling that matters most.** One set of vertical lines governs the banner, the writing and the foot. The hero's words sit directly above the writing and share its width; the hero's picture sits directly above the side column and shares its width. **Content area 1104 (`--container-hero`), reading column 800 (`--container-article`), gutter 48, side column 256 (`--container-rail`).** All tokens; the rail is new at S112 and is derived rather than chosen, so the day the reading column moves the rail moves with it (DSRD 7 §4.1).

**The furniture left the reading column.** The contents card and the share row used to sit inside the writing, and inside it they had only two possible shapes, both wrong: floated, they cut the line beside them to 47 letters against the article's 87; full width, they blocked the top of the page. They now sit in a column of their own beside the writing, which takes no width from it.

**The side column, top to bottom:** **(S150 note: the picture, the Know Your Psychology mark and the panel's order below are superseded by the note at the head of section 22, items 11 and 13; Know Your Psychology has left the article panel.)** the article's picture, square, appearing as the banner leaves; the contents; and the Know Your Psychology mark held to the foot of the screen and linking to `/learn/`. Those three travel as one panel the height of the screen. Below them, at the foot of the column, the six related-reading links and one way out. The type in that column is one typeface, three sizes, one leading per size, and one label treatment for both lists.

| What changed at S112 | Where it is written |
|---|---|
| The page returns to the 1104 grid with an 800 reading column and a 256 rail; the S110 one-left-edge-at-880 ruling is superseded | §22.2 |
| The hero joins that same grid. Widening one without the other had put the writing 152px left of the hero | §22.4 |
| The byline leaves the hero. The author stays in the page's structured data and at the foot | §22.4, §22.7 |
| The standfirst takes a measure of 55 letters and a size of 21, the step above the body | DSRD 7 §4.1, the measure rule |
| The two cards inside the writing stop floating and move to the rail | §22.5a |
| The contents card becomes a panel: no fill, no border, no padding, heading down a step | §22.5a, DSRD 8 §27 |
| The share row moves from the panel to beside the author, then into the author's own row: small, square, aligned on his bottom line | §22.5a, §22.7 |
| The author card loses its sentence and stacks the role under the name, **on every hub page type** | §22.7 |
| An orange line divided the writing from the rail, then became a grey hairline running the full height of the writing, **because orange should mean one thing** | §22.2 |
| The Know Your Psychology mark joins the rail, becomes the generic artwork, then the full-width panel image, then pins to the foot of the screen and links to `/learn/` | §22.10 |
| Related Further Reading moves into the rail as a labelled shelf of six, dressed in styles the column already had | §22.8 |
| The background marks are switched off on this page. Kain's own approved design, switched off in one line, not deleted | DSRD 7 §14.1 |
| The dark course card comes off the page entirely | §22.10 |
| The course block takes Kain's new words: **"Want to Take Your Interest Further?"** over **"Explore related courses and deepen your understanding with insights you can use in everyday life."** | §22.10 |
| The trial panel takes Kain's new words, given earlier the same day | DSRD 8, the trial panel |
| The page now ends: writing, author with the share marks on his own line, two courses drawn from the article's own tags, footer | §22.1 |

**The template is signed and the specimen page is not publishable, and those are different things (Code, S112).** `page_gate.py` returned 40 passed and 12 failed on the rendered page. The failures are almost all content, not layout: a dead link, four acronyms used before being spelled out, a keyword at 0.30 per cent against a 1.0 floor, no DSRD 6 record on file, and a Rank Math score older than the page. Recorded here so the template's approval is never read as the page's readiness.

**One rule, two hosts (Code, S113).** Forty seven selector lines inside the S112 rebuild's media block in `knowledge-hub.css` read `:is(.kh-article__body, .bn-body)`. **The rail's rules exist once and reach both page types**, so a future ruling on the rail reaches the book note without anybody remembering to copy it. §32 records that the book note's reading area **is** the article's, not a copy of it.

### 22.1 Page Structure (top to bottom)

**SUPERSEDED AT THE FOOT BY CODE'S S112 SITTING (folded S358).** The page now ends: article body, author signature block with the share marks on his own line, the course row of two drawn from the article's own tags, footer. The contents card, the share row and Related Further Reading are no longer items in this vertical order at all: they sit in the side rail beside the writing (see the fourth round above). The list below is kept as the record of the S082 order.

**Reordered by Kain at Code's S082, on the rendered page in Safari, and signed there ("I am 100% happy with this template page now"). This order supersedes the one below it and is the operative list.**

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§22.3)
3. Hero (§22.4)
4. Featured image (§22.5)
5. Article body (§22.6)
6. Author signature block (§22.7)
7. Hairline, 1px #EEEDED, 48px margin top and bottom
8. Explore Related Learning Paths, the course row (§22.10)
9. Hairline, 1px #EEEDED, 48px margin top and bottom
10. Related Further Reading (§22.8)
11. Source Block (§22.9)
12. The closing enquiries panel (DSRD 8 §16), the site's own shared component with its copy unchanged from the pages already running it
13. Rainbow stripe and footer (DSRD 8 §19)

**What the reorder changes, named so nothing is lost.** The two halves of the foot are inverted: the course row now sits above the reading row rather than below it. **The source block stays beside Related Further Reading**, because this section has always treated those two as one zone and Kain's order did not name it; that placement was Code's call and is overturnable on sight. **The Where next panel is off this page** and §22.10a records what that costs. The hairline before the closing panel was asked for in the same sitting and is item 12's own top edge.

*The superseded order, kept as a record: author signature, hairline, Related Further Reading, source block, hairline, Explore Related Learning Paths, the Where next panel. Item 12 of that list was added S282 to correct it against §22.10a; both are now history.*

### 22.2 Content Column Width

**SUPERSEDED BY CODE'S S112 SITTING (Kain, live in Safari; folded S358). The page is two columns on one grid, not one column at 880.** Content area 1104, reading column 800, gutter 48, side rail 256. The hero's words share the reading column's width and the hero's picture shares the rail's, so banner, writing and foot obey one set of vertical lines. **A grey hairline runs the full height of the writing, dividing it from the rail.** It was an orange line first and Kain changed it, on the reasoning that orange should mean one thing on this site. The 880 figure everywhere below this paragraph reads 800 from S357 and the one-left-edge ruling reads as the record of what stood between S110 and S112.

*The S110 text, kept as the record:*

**Unified 880px column for the reading.** All the page's reading sits in a single 880px max-width column: the hero's information panel, the article body, and all post-article sections. No width transitions within the reading. **The 1104 exception below is retired (Kain, S110, on the rendered page: "bring the breadcrumbs and the container into the 880 size. So essentially the entire article and this container is all at one left edge"). Everything inside the hero band, the trail included, now begins on the 880 column; the band itself still runs the full width of the screen.** *The retired text, kept as the record:* the hero block and the breadcrumb were the ruled exception and sat at 1104px, pulled 112px outside the column, so that the logo, the breadcrumb, the hero block and the title all began at the same point (Kain, S085 ruling 4; approved on the rendered page at three widths at Code's S096). That was correct while the page had a wide picture block to align to; it has none now. *This paragraph read "Only the breadcrumb sits at 1200px page container width" until S337. The 1200 was never what the build did; corrected first to the reading column and then, within the same session, to 1104 on reading this page's own hero ruling.*

*Single column width eliminates visual jitter. The reader's eye never has to readjust to a wider or narrower container mid-page.*

*880px is no longer this page's own choice. It is the container width for every content page on the site, ruled by Kain at S085 and held at §27, and it is not put to him again on any template.*

**The S085 hero standard, recorded here at S337 now that Kain has confirmed it on the real page.** Eight things were ruled across a long sitting at Code's S085, and Code's own filing said plainly that none of them should reach a document until Kain had seen them in the theme rather than in a captured preview with injected CSS, because "he cannot make accurate design decisions from an inaccurate representation". **That confirmation is Code's S096 sitting**, where Kain saw the built page at desktop, tablet and phone and said "Thats perfect Claude, yes, i'm totally happy with this". What the rulings say, and where each one now lives:

| S085 ruling | Where it stands |
|---|---|
| 1. The hero block is 1104, the reading column stays 880 | **Superseded S110**: the article took the shared `kh-hero` band and everything in it sits on the 880 column (§22.2). The book note had already moved to 880 at Code's S102 (§32.2). The S081 top grid this ruling shaped is deleted from the theme, superseded rather than wrong, with the reasons written at the rules that carried it |
| 2. The hero block's shape is the standard, not its contents | Live. Both pages carry a rectangular block holding a picture and an information panel, with the reading beneath; only the split differs, because a book cover is portrait and an article banner landscape |
| 3. The article banner is 680 image, 400 panel, 24 gap, title on the whole 1104 line | **Superseded S110**: the banner is gone; the page opens on the shared band (§22.4) |
| 4. The breadcrumb sits on the hero block and aligns with the logo | **Superseded S110** on this page: the trail sits inside the band on the 880 column (§22.3, §27) |
| 5. The meta line's contents | **Superseded in placement, not in contents**, by Kain at Code's S088: it moved out of the hero to the head of the writing (see §22.4). Its word count comes from the body and its read time from that count, so the two cannot drift. **Superseded again at S109 and S110:** the line is the shared reading bar (DSRD 8 §26), under the title inside the band; on this page it carries the writer, the date and the reading time joined at the left, with no word count, because the contents card carries the count |
| 6. A section divider on the same line as every heading, filling the space to its right | Live, built as `achology_heading_dividers()`. **Amended S110 (Kain: "reduce the decorative lines thickness by 25%. Also, shorten its total length by 30%")**: the line is 0.75 rather than 1, and it stops 30 per cent short of the room the heading leaves, by a spacer inside the rule measured on the rule's own basis so it is exactly 30 on every heading; it hides itself where the room left is under 138. Outside feedback proposed removing it altogether and Kain kept it, finer and shorter. The glyph that once opened it was typed into every H2's text and is drawn by the stylesheet since S108. It draws on the article, the book note, the quote page and the help answer. **This does not contradict D1 in §22.11**, which removed a *standalone* divider sitting between zones. A rule on a heading's own line and a rule in the gap between blocks are different objects; D1 removed the second and ruling 6 added the first |
| 7. The course card narrows to 350, the Know Your Psychology mark inside it to 280 | Live |
| 8. The book note hero takes all of the above | Live; §32 carries the book note page |

**One thing in that S085 file was withdrawn by Code himself and is worth keeping, because the lesson outlives the detail.** He had reported the article page's pinned title and contents links as a fault and stripped the inline widths in his preview. They are not a fault: they are `knowledge-hub.js` implementing Kain's own heading balancer, which splits a two-line heading so about 65 per cent sits on the top line. It ran once at load against the real width, so widening the column with injected CSS afterwards left the old pin in place and made a working behaviour look broken. **The stale number was an artefact of the instrument, not a property of the page**, and a ruled behaviour of Kain's was stripped to make an overlay look right.

### 22.3 Breadcrumb

**Inside the hero band, on the 880 reading column, sharing the page's one left edge (Kain, S110, on the rendered page; theme 0.290.0). Measured after deploy: trail, title, summary, writer line and body all start at 280 on desktop, 32 on tablet and 20 on mobile.** The band restates the trail's colours for its dark ground, as components.css already did; the component itself stays sealed.

*Superseded, kept as the record:* it reused the §20.3 breadcrumb component, **on the hero block at 1104px, aligned with the logo** (Kain, S085 ruling 4). It read "at 1200px page container width" until S337. It was never at the 1200px page frame. §27 carries the site-wide rule.

*The breadcrumb width conflict carried on the board card was closed the wrong way, and that is now corrected. §27 was amended at S281 to read "The breadcrumb is the exception on every page type: it sits at the 1200px frame", citing this row, §22.2, DSRD 7 §4.1 and the built theme, and the four were declared in agreement. **They were not: the build has never put the trail at the frame on any page.** Kain ruled at Code's S090, on three whole live pages in Safari, that the build is right and the documents are wrong. Corrected here and at §27 at S337. The lesson worth keeping is that four sources were read as agreeing without any of them being measured against the rendered page.*

- **Format:** `Home` icon `ChevronRight` Home `ChevronRight` Learn `ChevronRight` [Category] `ChevronRight` Articles `ChevronRight` [Article Title]
- **Current page:** Article title is brand dark (#354149), not linked
- **Spacing:** 48px below header bottom edge (var(--sp-2xl))

### 22.4 Hero

**Superseded at S162 and S163 by §22.15 (the Soft Light hero).** Everything below in this subsection is kept as the record of what stood before.

**The page opens on the Knowledge Hub hero band, `kh-hero` (DSRD 8 §28), ruled by Kain at S110: "apply exactly the same hero styling to the article page. It's what we have to the book note page."** The band runs the full width of the screen; everything in it sits on the 880 column. It holds, in this order: the trail; an overline naming the page type and category; the title at the 33 step; the article's own written summary as the standfirst (the same summary every listing card already carries; nothing drafted); the writer line, which is the shared reading bar, directly under the summary; and the article's picture as an object at the right of the column, the same picture washed almost out as the band's ground. The columns stack below 1024, picture below the words. The reading bar's hairline comes off inside the band, because the band's bottom edge is that line; the body supplies the 48 beneath. The overline repeats the category, which Kain deleted as a pill at S080 because it cost a line; in the band it costs no line and matches the book note, and it goes if he reads it as the pill returning. His words on the band: "it's kinda perfect. It's exactly what we're looking for. It's simple."

*Superseded, kept as the record:* 880px column. Left-aligned text. No search bar, no background colour.

**The category pill is gone (Kain, S080), and its stylesheet rules went with it at S082.** No template has emitted it since S080, and fourteen declarations plus a hover state were still being sent to every reader until the S082 tidy pass deleted them, proved by serving the before and after stylesheets to the same page and comparing every computed style at nine widths. The table below is kept as a record of what it was, and nothing renders it.

**Category Pill (REMOVED S080; rules deleted S082):**

| Property | Value |
|----------|-------|
| Font | Como 12px/600 |
| Transform | Uppercase |
| Letter-spacing | 0.08em |
| Colour | Brand orange (#ED6922) |
| Background | Brand orange at 8% opacity |
| Padding | 4px 12px |
| Border-radius | 20px |
| Link | `/learn/{category}/` |

**H1 (Article Title):**

| Property | Value |
|----------|-------|
| Font | Como, the 33 step, 700 (corrected S302: this row read 36px, which is not a step on the nine-step type scale Kain ruled at S056 and is not what the theme renders; `base.css` sets `h1` to `--text-33` at 700. The scale governs and nothing may sit between its steps) |
| Colour | Brand dark (#354149) |
| Line-height | 1.2 |
| Margin-top | 16px below category pill |

**Meta Line: SUPERSEDED at S109 and S110 by the shared reading bar (DSRD 8 §26).** One component on all four Knowledge Hub page types, `achology_reading_bar()`, under the title inside the band. On this page it carries the writer (photograph, Written by, the author's name), the date and the reading time, joined at the left, with nothing at the right and no word count. The quote page's S108 exception below is superseded with it: the narrator's credit has gone from the bar, so the writer's name is back on every type. The two paragraphs and the table beneath are kept as the record.

**Meta Line (MOVED OUT OF THE HERO, Kain at Code's S088, on the rendered page: "place this above the opening paragraph title, within the main article container").** The strip now sits at the head of the writing, above the opening paragraph title, inside the main article container, on both the article and book note pages. The book note's meta line carries no "Achology Publications". The hero placement below is superseded; shipped in theme v0.118.0.

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | Mid grey (#8A9199) |
| Format | '22 March 2026 · Kain Ramsay · 8 min read' |
| Separator | ' · ' (middle dot with spaces) |
| Author name | 500 weight, linked to the writer's profile at `/about/instructors/{slug}/`, brand orange on hover (corrected S268; the row read 'linked to author page', which does not distinguish the byline from the source author's hub at `/learn/authors/{slug}/`, per DSRD 1 §3) |
| Placement | Head of the writing, above the opening paragraph title, within the main article container (Kain, S088; supersedes 'Margin-top 8px below H1' in the hero) |

**One registered exception, the quote page (Kain, S108, ruled on the rendered page).** On a quote page the meta line carries no author name. His words: "So that names aren't competing with names, we just move Frederick's name out of the article info bar and just leave his name in the article author card underneath the article." The writer is still credited, in the signature card at the foot.

*Why the exception is needed.* The quote page is the one page carrying two names within a few lines of each other: the listen bar's "Read by Declan Fitzpatrick" sits directly above the strip, so the reading credit and the writing credit collide. The article page keeps its author, because it has no clash to resolve. The exception is the quote page's alone and does not travel.

### 22.5 Featured Image

**SUPERSEDED at S110.** The article's picture is the hero band's ground, washed almost out, and an object at the right of the band's 880 column (§22.4). It carries `alt=""` in both places: it is atmosphere, unlike the book note's cover, and a screen reader announcing one decorative image twice is worse than not announcing it; its authored alt stays on the attachment for every place the picture is information. No picture block sits above the writing. The table below describes a block that no longer exists and is kept as the record.

| Property | Value |
|----------|-------|
| Width | 880px (full content column) |
| Height | 420px |
| Border-radius | 12px |
| Object-fit | cover |
| Prototype | CSS gradient placeholder (per achology-prototypes skill) |
| Margin-top | 24px below meta line |

*In production: composite banner image (author portrait + book cover) from the image production system (DSRD 7 §12).*

### 22.5a The Contents And Share Card (ruled across Code's S082, each value on the rendered page)

**SUPERSEDED at S110 by the contents card, DSRD 8 §27 (Kain: "I like A, the Editorial index please claude").** The card now floats right beside the writing at the book note's own numbers (300 wide, 40 across, 32 beneath, bleeding into the gutter above 1040, full width on a phone), so it stays available as the reader scrolls; its label reads ARTICLE NAVIGATION PANEL, its heading Table of Contents, its line under the heading the section count and the word count, its toggle a round plus and minus, and the share row sits inside it as its footer under a rule. The S081 top grid that held this card is deleted from the theme. Everything below is the S082 record.

The card in the page's top grid, carrying the Table of Contents and the Share this Article controls beside the opening of the writing. Every value below was settled in one sitting, one variable at a time, on the real page in Safari.

**Its width is 36% of the column, and it had never been there.** Asking for it to be narrowed found a fault rather than a preference. The top grid ran `1.45fr 1fr`, and its own comment claimed that gave about 320, the width the card had been ruled to. Measured: 880 less the 24px gap is 856, and 856 over 2.45 is **349**. The card had been 32px wider than its ruled width since the grid was built, and the arithmetic was never checked against a render. **The grid is `1.7fr 1fr`, which lands at 317, against 36% of 880 being 316.8.**

**A mark sits before each heading, on the same line as the words.** Built first as a rule above the heading carrying the Achology bubble, which was the wrong reading of what Kain asked for, and corrected in the same sitting on his words: place them on the same line before the actual text. The bubbles are replaced by real registry marks, `list-ordered` before Table of Contents and `share-2` before Share this Article (DSRD 7 §5.2), both at 0.85em and both in the AA-safe orange.

| Element | Value |
|---|---|
| Table of Contents heading | Como, the 24 step (up one from 21), with 24px of air beneath it |
| Share this Article heading | Como, the 18 step, keeping its 16px beneath |
| Contents numbers | 14px, the title's own size (up from 12), with **tabular figures** so every title starts at the same point down the list |
| Share circles | 28px (down from 32, so the card could narrow), on the 10 per cent orange wash |
| Marks inside the circles | 14px and 16px (down from 16 and 18) |
| Every mark and label in the block | The AA-safe orange #B8460F. One orange in the block |

**Why the numbers moved, in Kain's words:** the two are not currently aligned with each other and this is visually obvious. They were already on the same baseline. **Two sizes on one line read as a misalignment whatever the baselines do**, which is the general lesson and not a fact about this card.

**Why the share circles were quieted by size rather than colour.** They were tried white with bubble-orange marks and rejected on sight ("revert back to what they were please"), so the wash and the AA-safe orange came back and the marks inside came down instead. **On that pale ground the AA-safe orange already sits close to the 3:1 floor DSRD 6 §7 gates against**, so lightening it would have bought subtlety by failing the scan.

**One idea that lived for one version, recorded so it is not proposed again as new.** Kain asked for the opening five words of the article to be set larger in the heading face, saw it rendered, and ruled the same sitting: undo this completely. The function, its call and its stylesheet rule came out together.

### 22.6 Article Body

| Property | Value |
|----------|-------|
| Font | Mulish 17px/400 |
| Line-height | 1.75 |
| Colour | Brand dark (#354149) |
| Width | 880px content column |
| Margin-top | 32px below featured image |

**Heading Styles:**

| Element | Font |
|---------|------|
| H2 | Como 24px/600, brand dark, margin-top 32px, margin-bottom 16px |
| H3 | Como 20px/600, brand dark, margin-top 24px, margin-bottom 12px |

**Blockquote:**

| Property | Value |
|----------|-------|
| Border-left | 3px solid brand orange (#ED6922) |
| Padding-left | 20px |
| Font-style | Italic |
| Colour | Soft grey (#5E6B75) |

**In-body links:** Brand orange, underline on hover.

**Which body sections carry a heading (ruled S292, Kain).** The article's six sections do not all carry an H2. The Opening Hook and the Close run **unheaded**: the hook is the intro paragraph directly under the H1, and the close is a short forward-looking wrap. The four middle sections, The Idea, Why It Matters, Going Deeper, and Putting It Into Practice, each carry their own reader-facing H2, with reader-facing H3s allowed inside Going Deeper.

The reasoning, recorded so the question is not reopened from cold: a heading above the hook makes the reader read a label before the sentence written to catch them, and a heading above the close announces the ending. The trade accepted is a four-item on-page contents list rather than six. *(The clause that used to follow this sentence imagined the article page one day gaining the travelling shelf; the shelf was retired at S085 and the article page carries its contents list in the top grid instead, §22.5a.)*

This settles an open build note that had stood in the `book-derived-article` skill, which stated the behaviour in prose, then declared it unconfirmed, then deferred it to this section, which did not cover it. The skill now carries the same ruling and the build note is deleted.

**The six-section shape above is the book-derived article's, and it does not govern every article type (ruled S302, Kain).** The four middle sections it names, The Idea, Why It Matters, Going Deeper, and Putting It Into Practice, are the book-derived template's own sections. The S292 ruling was written into this page-level section as though it governed the page rather than the type, and an instructor-attributed article read against it appears to fail a standard that was never its own. It does not: the instructor article's structure is the Hook-Book-Look-Took arc as a reflective essay (DSRD 2 §3.7 and the `instructor-article` skill), whose understanding movement may run to more than one reader-facing H2, so five to seven headed sections is the correct output rather than a deviation.

**The instructor-attributed article's close carries its heading.** Rendered for Kain at S302 on I13 at the full 880px column, both ways, with everything else on the page held still. He ruled the heading kept. So the unheaded-close rule above holds for the book-derived article and is reversed for the instructor article, and the reasoning behind each is different: a book-derived article's close is a short forward-looking wrap that a heading would announce, where an instructor article's close is a distinct reflective task the reader is being handed, which earns its own heading and its own place in the on-page contents.

**Its heading text is fixed: "What Could You Do With These Ideas?" (ruled S302, Kain).** It is the same wording on every instructor article, replacing "What to Do With This" wherever that stands. A question addressed to the reader rather than a label describing the section, which is what the section actually does.

### 22.7 Author Signature Block

**The off-white band is withdrawn on this page (Kain, at Code's S082, ruled on four renders of the whole page in tabs: the band gone, the card at half width, the block removed entirely, and the page as it was).** His words: "The band goes, a simple and clean solution. Much better!!" The ground, the 10px corner and the 20px padding come off; the portrait, name, role and bio all stay, and the portrait comes to 44px. The block went from 92px tall to 47 without losing anything in it.

**Extended to the book note page and moved onto the component (Kain, at Code's S088, on the rendered page: "look the band on the book note template too please claude, so we can consistency across all templates").** The band is withdrawn everywhere the block renders. Only two pages carry it, so the rules moved onto the component in people.css; the two pages no longer differ. This supersedes the scoping paragraph that stood here from S082, which read the withdrawal as this page only.

*The superseded card treatment, kept as a record of what was withdrawn: off-white ground var(--color-off-white) #F3F4F4, 10px border-radius, 20px padding, 52px avatar.*

| Property | Value |
|----------|-------|
| Background | None on this page (withdrawn S082) |
| Border-radius | None on this page (withdrawn S082) |
| Padding | None on this page (withdrawn S082) |
| Layout | Flex row, 16px gap between avatar and text |
| Margin-top | 32px below last body element |

**Avatar:**

| Property | Value |
|----------|-------|
| Size | 44px circular (corrected S082 from 52px, with the band) |
| Background | Brand dark gradient |
| Fallback | Author initials (Como 18px/600, white) |
| Border-radius | 50% |

**Text Group:**

| Element | Style |
|---------|-------|
| Author name | Como 15px/600, brand dark, linked to the writer's profile at `/about/instructors/{slug}/`, brand orange on hover (corrected S268, same ground as §22.4) |
| Bio line | Mulish 13px/400, soft grey (#5E6B75), single line, **read from the people registry in the theme** (S268). It is never written into a page and never carried in an upload file, the same rule already ruled for the book note page at DSRD 2 §1.6 |

**The mid-body writer photograph: instructor-attributed articles only (Kain, at Code's S116; scope corrected at Code's S117, written here S362).** Kain ruled at S116 that the writer's photograph also appears inside the body, mid-writing, on the instructor articles and on Karen's twelve, and on nothing else. The S116 build tested only whether the `author` field resolved to a real person, which every bylined article does, so 167 published pages (51 author biographies, 116 field-authority articles) briefly carried an editorial pen-name's portrait mid-body. Kain found it live on the Albert Ellis biography. Code fixed it at theme 0.426.0: the block now fires only where `article_type` is `instructor-attributed`, the value both instructor articles and Karen's twelve share and no other type carries. Verified live on one page of each kind. The signature block above is untouched by any of this: it renders at the foot of every article regardless of type, and always has.

### 22.8 Related Further Reading

**WHERE IT NOW SHOWS, AND THE SIDE PANEL'S RULES (Kain, live with Code in Safari, S146 and S147; recorded by Chat S401 from RULING__The_Quote_Page_Sitting_S146, RULING__The_Contents_Rail_S146, RULING__The_Quote_Page_Design_Principles_For_Every_Hub_Page_S146 and RULING__The_Book_Note_Page_Sitting_S147, channel Archive).** The quote page carries no Related Further Reading at any width (theme 0.707.82): Explore More Quote Articles does that job there, and Kain ruled two blocks offering the same action side by side make no sense. The book note carries none at any width either (0.707.90): Explore More Book Notes does that job there. **The article keeps it.** On every article-type page the side panel travels the whole article: its last item comes to rest 48 above the first hairline that closes the reading, measured from its last item, never its screen-high box; every contents highlight is the same width, the section names still folding by the S081 rule (0.707.67); the column's vertical edge carries on down to the hairline the panel rests on; the panel's square picture shares the cover column; and a link in a side list has one hover rule, colour only (underlines belong to links inside running text). Where the panel stands beside a row-based block, its list matches the rows line for line. One side effect is open, named in §32: the "all articles from this book" line (S361) rode inside this list and no longer shows on book notes.

Between the two hairlines, **below the course row** (§22.1, reordered S082). Section header plus a list of links. Positioned above the source block (§22.9) within the same zone.

**The compact card row is gone (Kain, at Code's S082, on the rendered page).** It is now a plain list of links, **three columns of three at desktop, two columns of three at tablet, and four links only on a phone**, verified at all three widths. Nine, six and four.

**What that supersedes, and one question it kills rather than answers.** The card row and its S302 count of three both go, because a list of names is not a compact card and adjusting the count would have been answering a question that no longer exists. **The three-or-two question the S081 sitting left open is dead**, and so is the measured fault that reopened it, every real title truncating at three cards, which cannot happen in a list.

**Section Header:** Reuses §20.7 section header component, with the icon box stretched to the two-line text on this page only (see §20.7).

| Property | Value |
|----------|-------|
| Icon | Lucide `Compass` (DSRD 7 §5.2), 24px inside the stretched container |
| Title | 'Related Further Reading' — Como 22px/600, brand dark |
| Subheading | **'Click on the links below for more reading on this fascinating topic.'** — Mulish 14px/400, mid grey. Kain's own words, written in the S082 sitting and copied character for character. It supersedes the registered line, which said "cards" after the cards had gone |

**Link List:**

| Property | Value |
|----------|-------|
| Layout | Three columns of three at desktop, two columns of three at tablet, four links only on a phone (Kain, S082, verified at all three widths). Supersedes the two columns of four he ruled at S081 the day before |
| Row spacing | A grid row gap, never padding on the links themselves. **The padding was the fault:** 10px on each link ran the block's box past its last line of text, so the white above the closing hairline read as 58 where every other block reads 48, and the same 10px pushed the first link 30px from its heading against a registered 20. The box measured clean and the page looked wrong, which is why only Kain's eye caught it |
| Content | Mixed: articles, book notes and quotes together (ruled by Kain, S272). Selection stays tag-driven. Supersedes 'tag-matched articles from the same category', which contradicted the cross-linking register at DSRD 1 §6.1 and §6.2 |
| Gap below | 24px before the source block |

**A way back and a way forwards sit beneath the nine links (Kain, at Code's S088, on the rendered page).** Two links in his own labels: **'More Articles in this Category'** and **'Browse the Whole Knowledge Hub'**, with the `arrow-left` icon (DSRD 7 §5.2) on the way back. **No hairline between the nine links and the two arrows**, his words: "please lose the hairline between the 6 links and the forward and back arrows." The nine-link count itself was ruled in the same S088 sitting: he first said the foot gave too many options, corrected a proposal of three or none to six, saw six rendered, and ruled nine; the complaint was four competing blocks, not the links. Shipped in theme v0.118.0.

*The superseded card row, kept as a record: compact cards per DSRD 8 §6.9, three at desktop, two side by side at tablet, two stacked on a phone, 16px gap, ruled S302 and rendered at three, four and six with real titles.*

### 22.9 Source Block (three cases, ruled S302; two variants ruled S268 superseded)

**Ruled by Kain at S302, on the three cases rendered as complete bottom blocks with real content.** The block answers one question, where this article came from, and there are exactly three answers:

| The article came from | The block shows |
|---|---|
| **A chapter of a book** (book-derived articles, author biographies with a source book) | The book, linking to its book note. Anatomy below, unchanged |
| **A lesson from a course** (video-derived articles) | The course the lesson came from, linking to the course page. Overline reads "From this course" |
| **Neither** (everything else: field-authority, buyer-intent, instructor-attributed, author biographies with no source book) | **Nothing. The block is not rendered at all.** The reader goes from Related Further Reading straight to the hairline and the course row |

**The school variant is removed (Kain, S302).** §22.9 carried a school variant from S268, on the reasoning that an article with no source book would otherwise carry no link to its own school. Kain ruled that an article that comes from a course points at a course, and that a school is not a thing a reader buys or enrols in: sending them to a school page sends them to a directory. **This also closes the icon registry gap** the S268 ruling left open, where the school variant and the course row directly below it would both have shown the graduation cap: with no school variant there is no second glyph.

**Why the third case renders nothing rather than a substitute (ruled S302, on two rendered options).** The alternative shown was lifting the lead-tag's first course out into its own block above the row. Rendered, the same course appeared twice within one screen, because the Explore Related Learning Paths row (§22.10) is already filled from the same lead tag by the same rule (DSRD 1 §5.7). **The row alone does the work.** An article with no source is not missing anything: the reader still gets three tag-matched courses immediately below.

**This is what the deleted fallback was hiding.** Until S302 the template rendered a hardcoded example book, Tasha Eurich's *Insight*, whenever `source_reference` did not resolve, so every third-case article showed another author's book as though it were deliberate. The fallback is deleted and this ruling is what stands in its place.

Horizontal card below Related Further Reading, within the same hairline-bounded zone. **The approved prototype for the book case is `RULING__Article_Source_Block_State_B_S268.html` in the Article Page folder under Knowledge Hub Design Prototypes.**

**Two states were rendered and rejected at S268 and remain rejected.** An instructor variant repeated the person the §22.7 signature block introduces a few centimetres above.

**Shared anatomy, both variants**

| Property | Value |
|----------|-------|
| Background | Off-white (#F3F4F4) |
| Border-radius | 12px |
| Layout | Flex row: image panel left, content right. Stacks below 768px, panel full width above the text |

**Book Cover (left), book variant:**

| Property | Value |
|----------|-------|
| Width | 140px |
| Background | Brand dark (#354149) |
| Content | Book cover image, centred |
| Prototype | CSS placeholder with brand dark bg |

**Content (right), book variant:**

| Element | Style |
|---------|-------|
| Overline | 'Book Note' — Como 11px/600, uppercase, brand orange, 0.08em letter-spacing |
| Title | Book title — Como 17px/600, brand dark, linked to book note page |
| Author | 'by [Author Name]' — Mulish 13px/400, soft grey |
| Description | 1–2 sentence summary — Mulish 14px/400, brand dark, line-height 1.6 |

**Watermark:**

| Property | Value |
|----------|-------|
| Icon | Lucide `BookMarked` (DSRD 7 §5.2) |
| Opacity | 0.05 |
| Position | Decorative, within content area |

*Links reader to the book note page, which has the complete "All articles from this book" and "All quotes from this book" collections (DSRD 2 §1.6).*

### 22.10 Explore Related Learning Paths

**Above the second hairline and directly beneath the author signature block** (§22.1, reordered S082). Section header plus course card grid.

**Section Header:** Reuses §20.7 section header component, with the icon box stretched to the two-line text on this page only (see §20.7).

| Property | Value |
|----------|-------|
| Icon | Lucide `GraduationCap` (DSRD 7 §5.2), 24px inside the stretched container |
| Title | **'Ready to Take Your Learning Further?'** — Como 22px/600, brand dark. Kain's own words, live with Code at Code's S147, theme 0.707.93, on every reading page (recorded S403). The chain: 'Explore Related Learning Paths' (S082 original) → 'Discover Related Learning Paths' (S082) → 'Want to Expand Your Understanding?' (S088) → 'Want to Take Your Interest Further?' (S112, recorded in the §22 table above) → the S147 words |
| Subheading | **'Explore related courses to deepen your knowledge and build on the insights introduced in this article.'** — Mulish 14px/400, mid grey. Kain's own words, S147, copied character for character, read back live on a book note and an article. **The sentence is identical on the article, book note and quote pages, deliberately:** Kain kept "this article" for book notes and quote pages at S147, as he had refused Code's 'book note' edit at S088 ("please accept the copy i gave you"). Supersedes the S112 line 'Explore related courses and deepen your understanding with insights you can use in everyday life.' and the S088 line 'If you liked this article, these course options could be the next step in your learning journey.' |

**The count-in-the-copy warning is retired with the S082 line.** The superseded subheading stated the count of two out loud; the S088 sentence states no number, so the copy and the card count can no longer contradict each other. The two-card count below is unchanged.

**Course Card Grid:**

| Property | Value |
|----------|-------|
| Card type | Full DSRD 8 §7 course cards |
| Count | **Two at every width (ruled by Kain, S302, on the real signed course card rendered at two and three inside the 880px column, with DSRD 5 figures).** Two side by side at desktop and tablet, two stacked on a phone. Supersedes the three-at-desktop count corrected in from DSRD 1 §3.4 at S268 |
| Why two | Two reasons, both seen rendered. **Room:** the course card carries a school line, an 18px title, a three-item stats row, a price with its guarantee pill and two buttons, and at a third of 880px the title and the button pair break up. Half the column holds all of it. **Relevance:** most lead tags map fewer than three courses. `learn-life-coaching` maps two, `learn-hypnotherapy` maps one (DSRD 1 §5.5), so the third slot is usually topped up from a less relevant tag, making it the weakest recommendation on the page by construction. Two also reads as a choice rather than a menu |
| Relationship to §22.8 | The reading block below is a list of links rather than a row of cards (rewritten S082), so the two no longer compete for the same shape. The earlier three-against-two comparison between them is history |
| Note on DSRD 1 §3.4 | §3.4's three-at-desktop count is the course card's grid **on the 1200px frame**, and it stands there. The article page is the exception, because its course row sits inside the 880px reading column (§22.2). The COMPONENT_DATA file for the course card records `columns_desktop_min_1024: 3` for the same reason and is not contradicted: that is the component's own default grid, not this page's |
| Layout | Grid within 880px, at the DSRD 7 §4.1 tiers |
| Gap | 24px |
| Selection | The page's `lead_tag` field, filled from that tag's mapped course list per DSRD 1 §5.7, topping up from the next tag and skipping duplicates (corrected S268; this row read 'tag-matched courses from the same category', which predates §5.7) |

### 22.10a Closing "Where next?" Panel (RULED OFF THIS PAGE, Kain S082; the S272 ruling below is superseded)

**The Where next panel is off the article page.** Kain reordered the foot at Code's S082 and the page closed on the site's enquiries panel (DSRD 8 §16). **At S088 the trial panel replaced the enquiries panel on both content pages**, as one shared block, ruled by Kain on the rendered page; his word for what he wanted was "token", and the copy and picture are his. The enquiries panel itself is unchanged and still closes About, Reviews, Testimonials and the Founders' Letter. **Our People and the sixteen instructor profile pages left that list at Code's S097** (theme v0.161.0, on Kain's instruction given on a screenshot of the block): both now close on the trial panel too, which is the same `achology_warm_room()` component carrying different words, so the shape, the column and the boundary above it did not move. His reason, recorded because it generalises: a person's profile ends better on an invitation in than on a support desk, and the enquiries route is already in the footer of every page on the site. The S088 sitting also set the foot standard in his own words: three blocks under the body on every content page (the two course cards, Related Further Reading, the trial panel), with the page types differing at the hero and nowhere else; the grey "Next possible steps after this Book Note" block is retired, its copy preserved in the S088 channel ruling. This section is kept as the decision record, because the panel's row 1 carried a rule and the rule's fate needs to be readable rather than inferred.

**What that cost, measured before it was called a cost.** Row 1 was recorded here as closing the source-author back link DSRD 1 §6 requires of every article, quote and book note, which this page had nowhere else. **That row has never rendered on any article on the site.** It wants the source author, which DSRD 1 §3 defines as a different person from the byline, and no field on an article carries one; §3.4 says the label is assigned at production and nothing does it. The rule was already unmet, so removing the panel does not make it more so. **Where the back link lives when the field exists stays an open question on the page's build sheet**, which already owns exactly that question and is the right home for it. It was not answered by guessing.

*The superseded S272 specification, kept as a record.*

Below the course cards, closing the page. The locked layout ended the page on the course card grid; Kain ruled on two rendered options of the whole page foot and took the panel. The Book Note page closes the same way after his S249 ruling, for the same reason: a foot of card grids alone reads as junk, three named rows do not.

| Property | Value |
|----------|-------|
| Component | The "Where next?" panel, DSRD 8 §13, plain off-white variant (not the §13.5 image backdrop the Book Note page uses) |
| Width | The 880px article column |
| Top margin | `--sp-3xl` 64px from the course card grid, the component's own default |
| Rows | Three, in this order: **1.** everything from the article's source author, linking that author's Knowledge Hub hub page. **2.** the article's topics. **3.** the free community tier. |
| Row 1's purpose | It closes the source-author back link DSRD 1 §6 requires of every article, quote and book note, which this page had nowhere else |
| Copy | **Approved by Kain, S282**, rendered in the page foot at 1200, 768 and 390. Title: `Where next?` Lead: `Three places to take this idea next.` Row 1: `Everything from {Author}` / `Book notes, quotes and articles drawn from their work.` Row 2: `Explore this article's topics` / `Follow the ideas in this piece across the Knowledge Hub.` Row 3: `Join the Achology Gateway` / `Free access to the events calendar, the coaching board and the community discussions.` |
| Approved prototype | The Article Page folder, under Knowledge Hub Design Prototypes. **Filed S282**: the S272 ruling named this folder and no prototype was in it. |

### 22.11 Elements Removed

The following elements were evaluated and intentionally excluded from the article page template:

| Element | Decision | Rationale |
|---------|----------|-----------|
| Tag pills | D3: removed entirely | Tags serve low-intent browsing — better placed on listing pages and category hubs where the browsing mindset is active |
| "More From This Book" section | D4: removed | This content belongs on the book note page, which already has "All articles from this book" and "All quotes from this book" as confirmed components (DSRD 2 §1.6). Source book callout links readers there. |
| Standalone section divider | D1: removed | Tag pills (with hairline border-top) and source book callout (off-white background) provide sufficient visual separation through colour shift alone. Hairlines used as zone separators instead. |

### 22.12 Decision Register (10 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Section divider removed | Colour shifts (off-white, hairlines) provide sufficient separation without a standalone divider |
| D2 | Unified 880px reading column | Single column width eliminates visual jitter. The hero block and breadcrumb are the ruled 1104px exception (S085, confirmed S096); corrected S337, this cell read "Only breadcrumb sits at 1200px". |
| D3 | Tag pills removed entirely | Tags serve low-intent browsing — better on listing pages and category hubs |
| D4 | "More From This Book" removed | Belongs on book note page. Source book callout links readers there. |
| D5 | Source Book + Related Further Reading merged into one zone | Reduces post-article sections from four to two hairline-bounded zones |
| D6 | Related Further Reading positioned above source book | Section header + compact cards first, source book callout below. 24px gap. |
| D7 | "Next Learning Steps" renamed to "Explore Related Learning Paths" | Subheading: 'Find practical learning opportunities that build on the ideas explored in this article.' |
| D8 | Author in two positions: meta line + signature block | Meta line for quick attribution. Signature block for identity and bio at end of article. |
| D9 | Lucide selected as icon library | ISC licence, free commercial use, consistent stroke weight. See DSRD 7 §5.2. |
| D10 | Icon registry task created | All 58 icons selected and registered in DSRD 7 §5.2. |

### 22.13 Prototype Reference File

Locked prototype: `article-page-self-awareness-v2.html` — second iteration, locked at V2. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. "Self Awareness" article used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

*Note: Locked prototype covers desktop only. Mobile/tablet responsive behaviour (single column, full-width images) applies per DSRD 7 §4.1.*

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

### 22.14 The S148 Article Page Sitting (Kain, live with Code in Safari, S148, theme 0.707.99 to 0.707.108; written S404 from `RULING__The_Article_Page_Sitting_S148`)

Kain's direction: carry over the components already approved on the quote page and the book note page, with their rules; nothing new designed. Each line below governs where an earlier line of §22 differs. Page used: `/learn/general-interest/articles/is-mindfulness-evidence-based/`.

1. **Bubbles behind the hero picture:** the quote page's three, at its sizes, from 1024 wide up (0.707.99). **Superseded S150 (0.707.121): the three loose bubbles are gone and the picture is cut to a speech bubble with a line behind it; see the note at the head of section 22, item 10.**
2. **The foot takes the quote page and book note structure** (0.707.101): under the signature, a list of six (or three, or none) articles from the same category, in the quote page's markup and S130 rules, with a contents entry. **Related Further Reading (§22.8) is off the article page at every width.** The side panel runs down to the list's closing hairline.
3. **The list's words are Kain's own** (0.707.103): heading "Browse More Achology Articles", with "Achology" in orange; line "Each article answers a popular question people ask online, helping you choose what to read next."
4. **No section numbers on articles** (0.707.104), neither in the contents list nor above the headings: an article's sections are not steps. Book notes keep theirs (§32).
5. **The side panel opens with the Know Your Psychology picture** (0.707.106), linked to the Knowledge Hub home page, with no hairline under it, in place of a second copy of the article's own picture. The picture at the panel's foot is removed. The "Visit the Knowledge Hub" button tried at 0.707.105 came out with it. **Superseded S150 (0.707.122, then 0.707.128 to 0.707.132): Know Your Psychology has left the article panel altogether, and the article's own picture, the speech bubble and its line, rests at the panel's foot; see the note at the head of section 22, items 11 and 13.**
6. **The contents list scrolls inside its own box** when longer than the screen (0.707.105), so the panel never runs past the foot of the screen; with item 5 the panel fits a 900-tall laptop screen whole.
7. **Quote pages are unchanged** by this sitting (checked live by Code).
8. **An article with no picture of its own takes its course's picture in the writing** (0.707.108): the S130 rule the instructor articles follow (course cover, the full course name, "Bestselling Achology Course") with the quote page's S147 bubbles, at the second paragraph of the second section. Author biographies and instructor articles keep their own pictures. This is the Achology Content Standard's named exception (p) to Part 13 rule 1 (Kain, S404). The course name on the picture follows the Standard's Part 9 rule 1 and Part 13 rule 3: its link sits on the course's short name.

**Owed by Code (Rule 14 fold-back):** the Article Page folder's prototype and build sheet brought to this state in a theme session. **Not general:** none of these eight changes a token or a site-wide rule, so DSRD 7 is untouched.

---

### 22.15 The Soft Light hero and its page changes (Kain with Code, theme sessions S162 and S163, 13 October 2026; built 0.707.234 and 0.707.235; written S423 from RULING__Hero_Direction_Soft_Light_Picked_S162, RULING__Hero_And_Section_Title_Simplifications_S162, RULING__Tablet_And_Phone_Hero_S163 and SHIP__Hero_Soft_Light_S163)

**This subsection governs the article, book note and quote page.** Where §22.4, §32.3 or §40 say otherwise, this wins; their older text stays as the record. The workbook takes the same family with its own differences (§37.6). It replaces the S161 hero standard's dark band and speech bubble (RULING__One_Hero_Standard_For_The_Four_Content_Types_S161 section 2); that ruling's lengths (title 50 to 60 characters, subtitle 150 to 170) and its 984 frame stand. Kain's words: "A. Soft light. We found it ... It brings them all together ... One hundred percent."

**1. One hero, direction A, Soft Light (`achology_kh_hero()`).**
- The band is warm cream (`--color-warm-cream`) with a hairline foot. Title in Como, brand dark, its ending one weight lighter; subtitle in brand dark; facts in orange link colour.
- The article's picture and the quote page's portrait dissolve into the band with no frame and no speech bubble, laid in with multiply, at about half strength, faded in from the right and from below, drawn far enough right that nothing dark sits behind the subtitle (worst-case contrast behind the subtitle 6.1 to 8.6 from 1024 up; 4.5 is the minimum).
- The book note stands its cover (the book component, straight, never tilted) on a faint bookshelf that fades into the cream from the right.
- **The quote page's hero is the article's** (Kain: "just lose the quote completely. And just let the banner be the banner. Same as the article."): the faded portrait, with no quote, slip or card in the band. The quote appears once, in the card under the band.
- **What lives in a hero:** breadcrumb, title, subtitle and the date line. Article: the faded picture. Book note: the cover, and "View on Goodreads" in the date line. Quote: the faded portrait. Nothing else: no author line, no audio player, no share buttons, no type label, and no buttons at any width.

**2. The date line ends on the word count (`achology_facts_line()`, shared with the Help answer's reading bar).** Article: "1 October 2026 · 7 Min Read · 1,294 words". Book note: the same, with "View on Goodreads" before the count. Quote: "24 September 2026 · 4 Min Read · 700 words". The count is the contents panel's own number, read and never typed. "Articles at Achology", "Book Notes at Achology" and "Wise Quotes at Achology" leave the line; the breadcrumb still links to each type's list.

**3. The frame (Kain approved, S162: "I 100 per cent approve the container width").** The content frame is 984: the reading column 680 at 18, a 48 gap, and the floating side panel 256, which stays. The page container is 1080 (984 plus two 48 gutters). See §27's S423 amendment.

**4. Section titles and the contents panel.** *(The contents panel part is superseded by 22.15a item 1, S163; the section title bubbles stand.)*
- No numbers anywhere: the small orange numbers above section titles on book notes and quote pages are removed, and so are the contents list's 01, 02 numbers.
- A faint Achology bubble mark (about 12 per cent strength, 60 by 46) stands behind the first word of every section title, centred on it and reaching a little out past the writing's left edge, on all three types. Built as a server-side wrap of each title's first word; a title that opens with a tag is left as it is.
- The contents panel loses its "8 sections · 1,294 words" line, its bottom hairline, its rail and its watermark. The entry being read carries a small faint bubble (about 30 wide) behind its first word, kept inside the panel, in place of the orange bar (option "Behind", chosen by Kain from four rendered).

**5. The foot runs full width with no side panel (Kain, S162).** *(Partly superseded by 22.15a items 3 and 4, S163: the panel runs down to the two paths again, and the foot is the two paths.)* The side panel ends where the reading ends, its last item (the Amazon button on book notes and quote pages) at the reading's foot. The author row, "Explore More ..." and "Ready to Take Your Learning Further?" with its course cards then run the whole 984. This reverses Kain's S146 ruling that the quote page's panel floats down to the closing hairline; the small number above "Explore More ..." goes too.

**6. Tablet and phone (Kain, S163: "yes").**
- 1024 to 1099: the desktop hero with its object column narrowed from 312 to 260, so the words keep about 640.
- Below 1024, one column: the breadcrumb; then the picture in its own row (200 tall on a tablet, 168 on a phone), dissolving into the cream on every side, or on a book note the cover on its faint shelf; then the title, subtitle and date line. Nothing is drawn behind the words below 1024 (contrast 10.1).
- Phone: title 28, subtitle 18, gutter 20. Tablet: gutter 32, and the band's top space 48 (§26).
- Below 1200 the book note's Amazon and author-site buttons, and the quote page's Amazon or course button, sit in the side panel's strip under the contents, where from 1200 up they already sat.

**7. The listen bar is off every quote page** (Kain, decision K10, S422), measured gone at five widths at 0.707.234. Help answers still carry it until Code's backlog line 26 is done.

**8. Two page gate lines, settled by Chat at S423 (reversible; Kain may overturn).** breadcrumb-below: a recorded exception for these three heroes (§26). content-width: 1080 is added to the gate's widths as a standard, because it is Kain's own S161 and S162 frame (§27).

**Open, for Kain's next step (Code's S163 note):** from 1024 to 1199 the hero's words start at the page gutter while the writing starts further in; the first item of his alignment audit of the other components on these pages.

### 22.15a The side panel, contents and foot, and the reading lines (Kain with Code, theme session S163, 13 October 2026; built 0.707.236 to 0.707.240; written S423 from RULING__Side_Panel_And_Foot_S163, SHIP__Side_Panel_And_Foot_S163 and RULING__Contents_Lines_And_Foot_Conversation_S163)

Governs the article, book note and quote page. Where 22.15 says otherwise, this wins. Approved state: `previews/panel-s163` in the theme folder.

**1. The table of contents is the Drawn Bubble** (Kain: "option one, the drawn bubble, is really, really nice ... let's lock that in", the orange a bit more subtle). The contents sit in a true Achology speech bubble (cream, with the logo's curved tail). Its outline draws itself in soft orange as the reader moves through the writing; a white card glides to the section being read; sections already read turn soft grey. The S162 small bubble behind the current entry is gone. The section title bubbles in the writing stay (Kain: "it breaks the page up ... it just makes the page warmer"). The heading "Table of Contents" and the mark are centred on one line at 22px, filling the bubble's inner width (0.707.239).

**2. Both reading lines are 1px and identical** (Kain: "both lines need to be the same"; 0.707.240): the line under the site menu (Kain S147, was 2px) and the line drawn round the contents bubble, the same orange, the same fill as the reader scrolls.

**3. Articles carry their course's cover and button in the panel.** The course is the first of the row the page's own tags fill, so it matches the foot's course path; the cover is drawn as the book note's; the button is the quote page's own "View this Course on Achology". An article with no matched course keeps its picture.

**4. The side panel runs down to the hairline above the two paths, on all three types** (Kain: "the right-hand column could just extend right down to the hairline"). The author row and "Explore More" sit in the 680 reading column beside the panel. This partly reverses 22.15 item 5 (the S162 full-width foot) and restores Kain's S146 rule on all three types.

**5. The foot is the two paths, in place of the two course cards** (Kain: "option one, two paths, is absolutely stunning. This finishes the page off absolutely perfectly"). The workbook thank-you page's block is now one shared piece (`achology_two_paths()`) on both pages. On a content page the course's first point ends at its count ("175 instructional tutorials."). The count is read from each course's curriculum file, never typed, on both pages.

**6. Open, not built: "The Conversation."** Kain chose "The Conversation" from five designs (`previews/paths-s163`) as the next form of the two paths: the course and the community as two speech bubbles, words drafted by Claude for him to tweak. Still to settle with Kain: what is fixed and what is read automatically, the one page-type word, which course shows when a page has no matched course, and whether the lesson count and ratings appear. Code renders four presentations first. Until it is signed, item 5 stands, and this subsection gains its standard when it is.

## 23. About Page Timeline — "The Achology Story" (STRUCTURE LOCKED)

The About Page Timeline tells Achology's story across 13 milestones from 2012 to 2025/26. It is section 5 of the About page, sitting below "The Thinking that Drives Achology" cards and above "In Our Students' and Members' Words". The component is built from five elements stacked vertically: a heading and lede that ride inside a pinned frame, a dark stage carrying an odometer, an era chart and a live counter, a fixed-height window through which the 13-milestone timeline scrolls, a terminus line, and a four-figure statistics panel beneath the window. Era is the organising principle — five named eras walk visually from brand dark to brand orange, mirroring the company's trajectory.

**Lock status note:** This section describes the component as built and approved with Kain on 22 July 2026, in `page-about.php`, `about.css` and `about.js` at theme v0.35.x. The built page is authoritative. Structural anatomy, scroll behaviour, the era system, milestone copy, spine and dot alignment are LOCKED. Where this specification and the built template ever disagree, the template is correct and this section is the thing to fix.

### 23.1 Outer Wrapper & Container

- **Inner wrapper:** max-width 880px (`--container-article`), centred horizontally
- **Background:** #ffffff (white)
- **Body font stack:** 'Mulish' with a system sans fallback stack (per DSRD 7 §3; the previous serif fallback retired with the face at S085)
- **Body text colour:** #354149 (brand dark); descriptive body copy uses soft grey #5E6B75 (per D10)
- The component extends the policy page frame (`.policy-page`, `.page-container`, `.article-container`), and its styles load from `about.css`, enqueued only on `/about/` after `policies.css`

### 23.2 Header Block

The heading and lede sit **inside** the pinned frame, so they remain on screen while the timeline scrolls beneath them.

- **Heading:** "The Achology Story"
- **Lede:** "Like all great educational institutions of our time, Achology boasts a unique origin story. Thirteen milestones across five eras, from the world's first video-based psychology course to a worldwide learning community 695,578 students strong."

### 23.3 The Dark Stage

A dark panel directly above the window. It repaints continuously as the reader scrolls, always reflecting the milestone currently at the reading line.

Four elements:

| Element | Behaviour |
|---|---|
| **Odometer** | Digit strips animating the enrolled-student figure for the current point in the story. At rest: `5,000` |
| **Era chart** | A hand-authored inline SVG with five era segments, 13 milestone dots and a moving era flag |
| **Era name and dates** | Repaints to the current era. At rest: `Origins`, `2012 to 2014` |
| **Live counter** | Labelled `Students & Active Members Enrolled` |

The stage replaces the three-cell student enrolment bar specified before this rewrite. The student-count progression it existed to show is carried by the milestones themselves (2017, 2021, 2022, 2025/26) and by the odometer.

### 23.4 The Pinned Window

The timeline runs inside a fixed-height window that holds still on screen while the story scrolls through it.

- **Pin mechanism:** `position: sticky` on the frame
- **Track movement:** the timeline track translates upward one pixel for every pixel of page scroll — the story moves through the window at 1:1
- **Reading line:** 96px inside the window. As each milestone crosses it, that milestone is marked reached and the dark stage repaints to its year
- **Window height:** `clamp(260px, calc(100vh - 703px), 510px)` at desktop; `calc(100vh - 674px)` at tablet
- **Flat fallback:** where the frame cannot fit the screen, `about.js` adds `.is-flat` and the whole block lies flat as a plain scrolling list. Measured at build: flat is false at 1440×1000 and 768×1024, true at 390×844

There are no era filter tabs and no filter behaviour. The eras appear as static group headings within the scrolling track, and `data-era` attributes remain on the group containers as structural markers only.

### 23.5 Era Colour System

Five named eras. Colours walk from brand dark (Origins) through slate-grey hybrids (Growth, Expansion) into burnt orange (Evolution) to full brand orange (Community) — visually mirroring the company's arc from origins to community. Set inline in `page-about.php` as `--era` values and consumed by `about.css`.

| Era slug | Display tag | Dates | Era colour |
|---|---|---|---|
| `origins` | Achology Origins | 2012 to 2014 | #354149 |
| `growth` | The Growth Years | 2015 to 2017 | #4d6672 |
| `expansion` | The Expansion Years | 2019 to 2020 | #8A9199 |
| `maturity` | The Evolution Years | 2021 to 2023 | #c05a1a |
| `community` | Community Development | 2024 to 2026 | #ED6922 |

Internal slugs remain `origins | growth | expansion | maturity | community` in the markup; the visible tag for the `maturity` era reads "The Evolution Years".

### 23.6 Timeline Spine

- **Width:** 2px
- **Colour:** #ED6922 (brand orange), 0.35 opacity
- **Position:** left of the milestone rows at every width, aligned with the dot column
- **Length:** spans the full height of the timeline track

### 23.7 Milestone Block Anatomy

Every milestone is a single left-aligned row: dot on the spine at the left, content to its right. There is no alternating layout at any width.

**Content elements (top to bottom inside each milestone):**

| Element | Style |
|---|---|
| Era tag (uppercase pill) | 11px / weight 700 / padding 3px 10px / border-radius 4px |
| Year badge | 12px / weight 700 |
| Stat number (landmark milestones only) | 36px / weight 700 / heading font |
| Stat label (follows stat number) | 13px / soft grey #5E6B75 |
| Title | 17px / weight 600 / brand dark #354149 |
| Description | 15px / soft grey #5E6B75 (`--color-soft-grey`) |

### 23.8 Per-Era Milestone Styling

| Era | Dot fill | Year badge | Tag background | Tag text | Stat colour |
|-----|----------|-----------|----------------|----------|-------------|
| Origins | #354149 | #354149 | #e8eaeb | #354149 | — |
| Growth | #4d6672 | #4d6672 | #eaeeef | #354149 | #4d6672 |
| Expansion | #8A9199 | #6b7680 | #f0f1f2 | #354149 | — |
| Evolution | #c05a1a | #c05a1a | #fce8d9 | #7a3606 | #c05a1a |
| Community | #ED6922 | #ED6922 | #fde8d5 | #7a3606 | #ED6922 |

### 23.9 Dot Variants

Two dot styles signal milestone significance.

| Variant | Size | Border | Used for |
|---|---|---|---|
| Standard | 16×16px | 3px solid #ffffff | Default milestone |
| Large | 20×20px | 3px solid #ffffff | Landmark milestones — 2017, 2021, 2022 |

All dots are filled with their era colour (per §23.8) and have border-radius 50%. There is no dashed variant.

### 23.10 Terminus Line

The timeline closes on a single sentence rather than a helper line and button.

- **Copy:** "695,578 mature learners from around the world have brought the Achology story this far. Will you join them?"
- **Link:** "join them" → `/membership/`

### 23.11 Statistics Panel

Four figures in a panel below the window.

| Figure | Label |
|---|---|
| 4.66 | Average Course Rating |
| 175,162 | Total Student Ratings |
| 216 | Countries With Students |
| 28 | Total Number of Courses |

### 23.12 The 13 Confirmed Milestones

Year, era, dot variant, stat, title and description are locked as built. Inline link targets are shown in brackets.

#### 2012 — Origins (standard dot)
- **Title:** The world's first video-based psychology course, published on Udemy
- **Description:** [Kain Ramsay → /about/instructors/kain-ramsay/] records and publishes the world's first video-based psychology training programme, taking a subject usually reserved for lecture halls and private clinics and putting it in front of anyone with an internet connection. The foundation of what would later become Achology is laid in this single, quiet decision.

#### 2014 — Origins (standard dot)
- **Title:** The Achology learning platform was first founded with 12 courses included
- **Description:** The Academy of Modern Applied Psychology opens with 12 on-demand courses, built on the conviction that psychological education belongs to anyone prepared to study it seriously, whatever their background. What began as a single course becomes a platform with a curriculum, a clear direction and a name.

#### 2015 — Growth (standard dot)
- **Title:** Curriculum expands to 17 interlinked psychology-based e-learning courses
- **Description:** The curriculum deepens into 17 interlinked e-learning courses, each designed to reinforce the others rather than stand alone, so understanding compounds with study. Students no longer simply buy a course; they enter a coherent body of work with a grounded, deliberate order to it.

#### 2016 — Growth (standard dot)
- **Title:** Live ONLINE skill and competency development training workshops begin
- **Description:** Achology begins running live, real-time online group workshops for skill and competency development, connecting students across time zones who had until now studied alone. It is the first expression of the principle that comes to define the academy: psychology is learned in dialogue, with and through other people.

#### 2017 — Growth (large dot)
- **Stat:** 100,000 / Students & Active Members Enrolled
- **Title:** A landmark year for Achology: global scale, platform growth & partnerships
- **Description:** Achology passes 100,000 enrolled students, begins building its own bespoke learning management system, and launches an exclusive Skilled Helper course with [Prof. Gerard Egan → /about/instructors/gerard-egan/], one of the field's most respected voices. In five years, a single Udemy course has grown into a global teaching platform with infrastructure and a faculty of its own.

#### 2019 — Expansion (standard dot)
- **Title:** Diploma in Modern Applied Psychology launched (Achology's flagship course)
- **Description:** The [Diploma in Modern Applied Psychology → /courses/] launches and gains global popularity, offering a structured route through psychological principles, from first theory to practised competence. DiMAP gives the academy its centre of gravity: one flagship course that carries the whole approach and sets its standard.

#### 2020 — Expansion (standard dot)
- **Title:** COVID-19 pandemic accelerated the acceptance of online learning worldwide
- **Description:** The pandemic moves the world's classrooms online, and demand for flexible, remote learning rises sharply as millions seek ways to keep studying. Achology's platform, built for exactly this kind of learning years before it became necessary, demonstrates that it can meet the moment at scale, without loosening the standards it had set.

#### 2021 — Evolution (large dot)
- **Stat:** 350,000 / Students & Active Members Enrolled
- **Title:** Community learning system upgraded, with better tools for discussion and practice
- **Description:** Achology's collaborative learning environment receives significant upgrades, giving students better tools for discussion and practice. Scale arrives in the same season: 350,000 students are now enrolled, and the community becomes the place where what they study is practised with other people.
- **Corrected S364 (Kain's ruling).** This entry said Achology was "recognised with CPD accreditation" from the CPD Standards Office and that its standards were "now independently examined". Kain confirmed the 2021 accreditation happened but was a paid product from a privately owned company that examined and guaranteed nothing, and that Achology is not accredited by it today. The claim was removed so the timeline does not overclaim (PRD criterion 8); the inline link to /accreditation/ went with it. The 2024 SoMAP entry carries the real verification story. Briefed to Code through FROM Chat at S364.

#### 2022 — Evolution (large dot)
- **Stat:** 500,000 / Students & Active Members Enrolled
- **Title:** Half a million students reached worldwide, and the curriculum expands to 25 courses
- **Description:** The student database passes a landmark half-million students as the curriculum expands to 25 courses, including 8 in-depth practitioner-level training programmes designed for those intending to work with others. Taken together, the academy now teaches at almost every level, from a first curiosity about human behaviour through to serious, accountable professional practice.

#### 2023 — Evolution (standard dot)
- **Title:** Launch of Achology version 2 community portal with new 28-course curriculum
- **Description:** An AI-supported, platform-wide upgrade delivers the version 2 community portal and a new 28-course curriculum, the most substantial rebuild the academy has undertaken. The learning experience is reconstructed around the evolving needs of a growing, global membership rather than patched at the edges, with every course reviewed, resequenced and brought into a single coherent structure.

#### 2024 — Community (standard dot)
- **Title:** The Society of Modern Applied Psychology founded, raising integrity standards in the field
- **Description:** Master Achologists found the [Society of Modern Applied Psychology → https://thesomap.org, new tab], an independent body created to raise the standards of training and practice across the field, and to define what competent practice requires. The Society maintains the competency development framework accredited graduates complete. The academy's graduates now hold the profession they trained for to a higher bar than the one they found.

#### 2025 — Community (standard dot)
- **Title:** Achology makes a full migration to Circle.io, finding its permanent online home
- **Description:** Achology completes a full migration to Circle, giving its learning system, its events and its community a single, permanent and properly integrated home after years spread across separate platforms. For the first time, everything the academy does lives in one place, with the functionality needed to scale internationally and the stability to support members through years of study rather than weeks.

#### 2025 / 26 — Community (standard dot)
- **Stat:** 695,578 / Students & Active Members Enrolled
- **Title:** An Eldership team established, and FREE learning is made available to the public
- **Description:** An eldership team of senior Achologists is established to guide the community and safeguard the standards it has built, and [free group discussions and skill events → /free-events/] are opened to the general public, with no membership required. It is the earliest expression of the wider social impact that future generations of Achology graduates will carry into the world, and a statement of what the academy believes learning is for.

### 23.13 Responsive Behaviour

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

The layout is single-column-left at every width. What changes across breakpoints is the pinned window, not the milestone layout.

| Breakpoint | Behaviour |
|---|---|
| Desktop (≥1024px) | Window pinned. Height `clamp(260px, calc(100vh - 703px), 510px)` |
| Tablet (768–1023px) | Window pinned. Height `calc(100vh - 674px)` |
| Mobile (<768px) | `.is-flat` applies — the block lies flat as a plain scrolling list, no pin, no window |

Verified at build across all three: desktop 1440, tablet 768, phone 390.

### 23.14 Decision Register

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision |
|---|---|
| D1 | The built page supersedes the previously locked structure. The pinned scrolling window, single left spine, dark stage, terminus line and statistics panel replace the centred alternating spine, student enrolment bar, era filter tabs and founder's-letter CTA. Kain's ruling, S213, on the built and approved page of 22 July 2026. |
| D2 | Body text grey throughout the timeline is #5E6B75 (~5.4:1 contrast, passes WCAG AA), not #8A9199 (~3:1, fails). This remains a system-wide brand-palette question — other locked components likely use #8A9199 where #5E6B75 belongs; the text-colour roles in DSRD 7 §1 should be locked and existing components audited before more page templates are built. |

### 23.15 Source of Truth

The built template is the reference: `page-about.php`, `about.css` and `about.js` in the theme repository. There is no separate prototype file for this component; the design was iterated in `previews/about.html` and extracted into theme files in the same session.

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

---

## 24. Course Page — Standard Accreditation Block (CONTENT + PLACEMENT CONFIRMED)

One standard block, identical across all 28 course pages. Added S186. Carries the recognition and CPD trust content deliberately removed from the nine-question block (S185; DSRD 2 §3.8).

**Shortened to four lines on the course page (Kain's ruling, S320).** The three elements below all stay, stated as briefly as they can honestly be stated: the two certificates, one line saying that buying a course does not confer accredited status, and SoMAP plus the UKRLP registration. The fuller treatment, including the can-and-cannot list the live school page carries well, stays on the school page and the accreditation page. On a page where someone is deciding to buy, a long recognition block stops clearing the objection and starts arguing with the sale.

**Its position changed at S320.** It is now block 7 of nine, and the standalone CPD Journey Context block that used to precede it is retired from the course page, its one necessary line absorbed into element 2 below. The full course-page block order is DSRD 2 §2.6 and the governing record is the agreed shape document in the Course Page design folder. Visual anatomy is designed and locked in DSRD 8 when the course-page build begins; this section fixes content, placement, and behaviour only.

### 24.1 What the Block States (3 Elements, Fixed Order)

1. **The accreditation relationship.** Achology's certification is independently verified by The SoMAP (the Society of Modern Applied Psychology), Achology's third-party accreditation verification partner. Achology is also a UKRLP-registered training provider (PRN 10099815).
2. **The two certificates, stated honestly (corrected S364 on Kain's ruling).** Completing the course earns a Certificate of Course Completion. Completing that course's required skill development sessions as well earns the course's Certificate of Achievement. The Certificate of Achievement is per course; it is not a member level. The member levels (Achologist to Master Achologist) are the accreditation pathway and are explained on the accreditation page. The block never implies the course purchase alone confers accredited status. *Until S364 this element said the Certificate of Achievement was earned through the CPD pathway, progressing from Achologist to Master Achologist; Kain ruled that wrong.*
3. **Routes out.** One primary internal link to `https://achology.com/accreditation/` (the full pathway explanation); one secondary external link to `https://thesomap.org` (opens in a new tab, per the site-wide external-link standard, DSRD 3).

### 24.2 Placement

**Superseded S320.** It previously sat between the CPD Journey Context block and the Three-Tier Pricing Comparison block. Under the nine-block course page it is **block 7**, sitting between Members Talking (block 6) and Three Ways To Buy (block 8), so it still completes the recognition story immediately before the page's final decision point. The CPD Journey Context block no longer exists on this page.

### 24.3 Standardisation

Identical on all 28 course pages: same wording, same links, no per-course variation. Copy is written once at the course-page copy stage to house-copy-standards (base voice, no em-dashes); any change is a single-source change applied site-wide.

### 24.4 Source References

Decision: S185 (DSRD 2 §3.8). SoMAP name and role: PRD criterion 6; DSRD 9 §23.12. Certification routes: DSRD 2 §2.16. UKRLP PRN 10099815: DSRD 2 §2.16 / DSRD 3 schema table.

---

## 25. Quiet Text-Led Pages — Reading Column Rule (LOCKED, Kain 2026-07-16; amended S281)

Every quiet text-led page (the seven legal policies, the policies index, /about/code-of-ethics/, /about/manifesto/, and any future calm reading page) places ALL of its content — page header, body, closing panels, and the breadcrumb — inside its reading column, centred within the 1200px page container. **The breadcrumb is not an exception, per §27 as corrected at S337 on Kain's S090 ruling.** This paragraph named it as the exception and put it at the 1200px frame until then.

**Which reading column, resolved S085.** This section read "the 880px article column" for all ten of these pages until S281, when it was amended to record the 620px prose column Kain ruled at Claude Code's S062 for seven of the ten. **Kain retired that column at S085: all ten pages on this template use the 880px reading column.** The question of which seven he had named is closed with it, and nothing is owed from Code on that list. §27 holds the ruling, and the reason the 620px column is recorded there rather than deleted.

**The alignment consequence, stated so it is a decision and not an accident:** the header and footer chrome (logos, nav) sit at the 1200px page container's edge; the reading column is centred and narrower, so the content's left edge does NOT align with the logos. This is by design — reading comfort owns the column, the chrome owns the frame. Content never chases the chrome edge, and no page may left-align its reading column to the logo.

Template mechanics: `page-container > article-container` (template-policy.php, single-faq_article.php and siblings). Nothing about this rule is per-page; a page either is a quiet text-led page and uses the column, or it is not.

---

## 26. Header-to-Content Spacing Rule — SITE-WIDE (LOCKED, Kain 2026-07-16)

The first content row of EVERY page (the breadcrumb where one exists, otherwise the page's first element) sits exactly **48px (`--sp-2xl`) below the site header** on desktop and tablet, easing to **32px (`--sp-xl`) below 768px**. No page invents its own value.

This generalises the spacing already locked for the Knowledge Hub (§20.2, §22.3) to every page type. Aligned on 2026-07-16, when an audit found four different values in production CSS:

| Page type | Was | Now |
|-----------|-----|-----|
| Knowledge Hub (hub, listing, article) | 48px (locked) | 48px — unchanged, the reference value |
| Policy template (7 legal pages, index, quiet about-pages) | 64px | 48px (policies.css §1) |
| /help/ (landing, category, article) | 32px | 48px (help.css) |
| Author profiles (.ap-crumb) | 44px (magic number) | 48px (people.css) |

Mechanics vary per template (page padding vs breadcrumb margin) — the RESULT is what is locked: 48/32 from header bottom to first content row. Any new page type inherits this rule on arrival.

**Recorded exception, S423 (Chat, from Code's S163 page gate run; Kain may overturn): the Soft Light hero on the article, book note and quote page (§22.15).** The gate's breadcrumb-below line (48 to the next thing) does not apply to these heroes. On the desktop the picture or cover's top meets the breadcrumb's foot (the roof Kain locked at S161), and the gap from the breadcrumb to the title is 48. On a tablet and phone the picture row sits between the breadcrumb and the title. The top space above the breadcrumb is still 48 on desktop and tablet. The workbook thank-you page carries the same kind of carve-out (Kain, S160).

---

## 27. Page Width Rule — Reading Column vs Showcase Frame (LOCKED, Kain 2026-07-16; third width added S062, corrected S281; third width retired by Kain S085)

**AMENDED S386: the reading column is 800px, not 880px.** The token `--container-article` has been 800 since the article page sitting at Code's S112, and every page built on it, articles and all policy pages included, renders at 800. Kain ruled at Code's S135, asking for one standard for every policy page decided by eye and never revisited: "Yes, 800 for all policy pages is settled for good." The build was right and this section was wrong. **Wherever this section says the reading column is 880px, read 800px.** The sentence test, the two-width rule and the showcase frame at 1200px are unchanged. The page gate (`page_gate.py`, `CONTENT_WIDTHS`) accepts 800.

**AMENDED S423: a third page container, 1080, for the Knowledge Hub reading pages.** Kain approved the 984 content frame at Code's S161 and S162 sittings ("I 100 per cent approve the container width"): the article, book note and quote page sit in a 984 frame (reading column 680 at 18, a 48 gap, side panel 256), inside a 1080 page container (984 plus two 48 gutters). This is his ruling on rendered pages, which is the only way this section allows a new width. It governs those three page types and the workbook page when built; every other reading page keeps 800. The page gate's `CONTENT_WIDTHS` takes 1080 (Code, from FROM Chat at S423). See §22.15.

The site has **two page content widths**, and one test decides which a block gets: **if it is sentences, it sits in the 880px reading column; if it is cards or imagery, it uses the full 1200px frame (`--container-page`).**

**880 is the container width for every content page on the site, and it is not put to Kain again.** Ruled by him at Claude Code's S085, in session, on the rendered book note sitting, choosing Route C. His words: "we must have consistency across all knowledge hub article pages ... container width cannot be questioned again across the other quote and workbook pages that we havent worked on yet ... 880 is the standard, exactly the same as what the help articles and policy pages should be." That covers every template not yet built, the quote page and the workbook page included: they are specified and built at 880 from the start, and width is never offered as a page-level choice. A third width does not return by judgement, and no builder reopens this.

| Width | Token | What uses it |
|---|---|---|
| 1200px | `--container-page` | The showcase frame: card grids, imagery, and page chrome. **Not the breadcrumb:** the trail aligns with its own page's leading edge, which is the content column on every page (the hero case retired: the book note at S102, the article at S110; see the bullet below) |
| 880px | `--container-article` | The standard reading column: Knowledge Hub articles, /help/ articles and category pages, the quiet about-pages |

**The 620px prose column is superseded, and it was not an accident.** Kain ruled it at Claude Code's S062, in Safari, on four rendered options, for seven of the ten pages on the policy template, and it was a readability standard for the densest prose on the site. His S085 ruling retires it: those seven pages move to 880px, which makes their lines about forty per cent longer. It is recorded here rather than deleted for two reasons: so a reader meeting 620 in an old file or an unswept stylesheet knows what it was and that it no longer governs, and so the change reads as a decision Kain took rather than a fault being corrected. Code shows him one policy page at 880 on the rendered page before sweeping all seven, which is the normal practice for a visible change and not a reopening.

**`--container-quote` (540px) is not a page width.** It is the text measure inside the featured quote card, a component value that happens to be registered in `base.css` beside the page containers. It is named here only so a future reader counting tokens does not mistake it for a fourth page width.

**The correction made at S281, and why it was needed.** This section read "exactly two content widths" and "no third width may be introduced" until S281. That was true when written and stopped being true at S062, when Kain ruled the 620px prose column by eye. The document had not caught up with a decision he had already made properly, which is the only kind of contradiction worth fixing quietly: nothing about the site was wrong, only the record of it. The absolute prohibition is replaced by the real rule, which is that a new width is his ruling on rendered options and never a builder's judgement. **S085 closes the sequence:** Kain retired the 620px column himself, so the site is back to two content widths, this time by his ruling rather than by a document's assumption.

- **Reading pages** — /help/ articles, /help/ category pages (a question list is text you read), the seven legal policies, the policies index, the quiet about-pages, Knowledge Hub articles: header, body and lists live in the page's 880px reading column (§25 mechanics: `page-container > article-container`). **The breadcrumb is not an exception to the frame rule and never was, and it has two cases.** Where a page has no hero block, the trail **aligns with that page's own content column**: measured by Code at S090 on the Privacy Policy at 1280 (left 330, width 620, matching the writing beneath it) and on the Policies index, About and Reviews at 1440 (all left 280, width 880, all matching). **Where a page carries a hero block the trail sits inside it, on the same content column: the book note since Code's S102 (§32.2), the article since S110 (§22.3). The 1104 case is retired on both, so the trail aligns with the content column on every page, and there is one case, not two.** **The content column itself is 800 from Kain's S111 ruling (DSRD 7 §4.1), and every 880 written in this document as the reading column is read as 800 from S357; the number in the older lines is the record of what stood when they were written.** *The retired text, kept as the record:* where a page carried the ruled hero block, the trail sat on it, at 1104px, aligned with the logo (Kain, S085 ruling 4; approved on the rendered page at three widths at Code's S096), which was the article page and the book note page. **In neither case is it at the 1200px page frame.** Kain ruled it at S090 in his own words: "yes, it holds, please correct the document." **This bullet, and several other sentences in this document, said the trail was the exception on every page type and sat at the 1200px frame.** That reading was written at S281 to resolve an apparent conflict and it resolved it the wrong way: the build never did it on any page. Corrected S337. What makes each page read as one column is exactly this alignment, and on the two hero pages the thing it aligns to is the hero block rather than the reading.
- **Showcase pages** — card-grid pages such as the /help/ landing, the Learn hub grids, course/bundle card layouts: the grid and its chrome use the 1200px frame. Centred hero TEXT on these pages still reads at the column width (880px), because it is sentences.
  - **Our People was listed here until S300 and is not a showcase page.** The built and approved page sits in a reading column, and the sentence test agrees with the build: the page is biographies. **Corrected S398: that column is 960px on this page, a page-level token reset ruled by Kain by eye at Code's S145, matching Reviews, About and Testimonials (§33.5); it is not the 800 standard reading column and not a third site-wide width.** Its card sections are two-across *inside* the column, not a frame-width grid (§33.5, §33.8). Corrected when §33 was written from the built page; the page itself never changed.
- **Closing CTA panels** (`.help-contact` and kin) share the width of the page they close (amended same day, Kain 2026-07-16): the reading column on reading pages (/help/ articles and category pages), the full frame on showcase pages (the /help/ landing).

Aligned on 2026-07-16, when an audit found three widths in production:

| Block | Was | Now |
|-------|-----|-----|
| /help/ article, policies, about-pages | 880px (locked, §25) | 880px — unchanged, the reference |
| /help/ category page (breadcrumb, hero, question list) | 1200px frame | 880px column (taxonomy-faq_category.php) |
| `.help-hero` centred text (landing + category) | 820px one-off | 880px column (help.css) |

The round-7 locked alignment survives by construction: category-page list rows keep their left edge on the breadcrumb ruler line, because breadcrumb and list moved into the column together. Clicking from a category page into an article no longer shifts the text edge. Any new template applies the sentence test on arrival; theme v0.29.0.

---

## 28. 404 Page Layout (STRUCTURE LOCKED)

The 404 page serves any URL matching nothing. It is a wayfinding page, not an error page (Kain, 2026-07-19): its job is to route a lost visitor onward, so nothing on it announces a fault. It is built from four elements stacked vertically in the reading column — breadcrumb, page header, a six-door "Where next?" panel, and a Popular Questions block — and nothing follows them but the footer.

**Lock status note:** This section describes the page as built in `404.php` at theme v0.35.x. Structural anatomy, copy, the six doors and their destinations, the two deliberate absences, and the three scoped styling rules are LOCKED. The Popular Questions source is ruled at §28.8 (live query, S247); the build fix is with Claude Code.

### 28.1 Frame and Inherited Styling

The page has **no stylesheet of its own**, no inline `<style>` block, and no `style` attribute anywhere. It borrows two stylesheets.

- **Root element:** `<main id="main" class="policy-page policy-page--404">` → `.page-container` → `.article-container` (the 880px reading column, per §25 and §27)
- **From `policies.css`:** the whole `.policy-page` frame — §1 shell, §2 breadcrumb, §3 header, §9 "Where next?" rows — plus a §12 block scoped to `.policy-page--404`
- **From `help.css`:** the question-door component
- **Watermark:** the 420px three-bubble mark, attached by `components.css` §3 to `.policy-header::before` (per DSRD 7 §14.1)
- **Icons:** Lucide, stroke 1.75, from the registry in DSRD 7 §5.2 — House, Compass, GraduationCap, BookOpen, LibraryBig, Tag, ChevronRight, CircleQuestionMark

### 28.2 Breadcrumb

Two items, per DSRD 1 §9.

- A link to the home page whose content is the Lucide House icon, `aria-label="Home"`
- A ChevronRight separator, `aria-hidden="true"`
- Current-page text, plain, not a link: **"Page not found"**

### 28.3 Page Header

Three stacked lines. This element hosts the bubble watermark.

- **Overline:** "Find your way"
- **H1:** "Oops! You're on a page that no longer exists."
- **Lead:** "Don't worry! We want to help you find what you're here for. Whatever led you to this page, and wherever you were headed, getting access to all of Achology is just a click away. Everything else is where it should be."

### 28.4 "Where next?" — Six Doors

A heading, a lead line, then six full-width link rows using the `.policy-next` component (`policies.css` §9). Each row is an icon on the left, a two-line text block — bold name over grey description — and a ChevronRight on the right. Rows are driven by a `$ach_doors` array; every href is built with `home_url()`.

- **H2:** "Where to instead?"
- **Lead:** "Here are some popular pages that people visit."

| # | Name | Description | Links to | Icon |
|---|---|---|---|---|
| 1 | Go to the homepage | Start from the front door | `/` | House |
| 2 | Learn about Achology | Who we are and what we stand for | `/about/` | Compass |
| 3 | Explore Achology's schools | Seven schools of applied psychology | `/academy/schools/` | GraduationCap |
| 4 | Browse Achology's courses | All 28 courses in one place | `/courses/` | BookOpen |
| 5 | Browse the Knowledge Hub | Articles, book notes, quotes and workbooks | `/learn/` | LibraryBig |
| 6 | Explore Achology pricing | What membership includes, and what it costs | `/pricing/` | Tag |

### 28.5 Popular Questions

The `/help/` popular block (`help.css`), reused wholesale. A header row of a circular badge holding a CircleQuestionMark glyph beside an H2, then four question rows — bold question title over a one-line grey excerpt, each with a ChevronRight.

- **H2:** "Popular Questions"

| # | Question | Excerpt | Links to |
|---|---|---|---|
| 1 | Where should I start with Achology? | Where you start depends on your situation and goals. | `/help/getting-started/where-should-i-start-with-achology/` |
| 2 | What makes Achology different from other online learning platforms? | Courses sit inside a live community, so skills are practised with real people. | `/help/achology-basics-and-identity/what-makes-achology-different/` |
| 3 | What are the seven schools of Achology? | Seven learning paths, one for each tradition of applied psychology. | `/help/achology-basics-and-identity/seven-schools-of-achology/` |
| 4 | Do I need prior qualifications to study at Achology? | No prior qualifications, psychology credentials, or academic background are required. | `/help/getting-started/prior-qualifications-needed-achology/` |

**Nothing follows this block** — no search box, no closing CTA, no images beyond the CSS watermark. Then the footer.

### 28.6 Scoped Styling Rules

Three rules only, all in `policies.css` §12, all scoped to `.policy-page--404`. Everything else is inherited unchanged.

| # | Rule | Why |
|---|---|---|
| 1 | `.policy-next { margin-top: 0; }` | Zeroes the panel's own 64px so the header's 48px governs |
| 2 | `.policy-header { padding-bottom: 43px; }` | An optical correction: a box-true 48px reads as roughly 53px against the panel's exact 48px below. 43px of padding puts the ink-to-line distance at 48px. Not a drifted token — 404 only |
| 3 | `.help-popular` gets 48px top margin, a 1px hairline top border and 48px top padding | The about-pages' scoped separator never reaches this block |

### 28.7 Two Deliberate Absences

Both are locked, and both are documented in the template itself.

**No search box.** The theme has no search template, so a search would land on the `index.php` fallback — a worse dead end than this page. This absence stands until a search template exists; when one is built, revisit this section rather than adding a box ad hoc.

**No "404" or "error" wording in visible copy.** Nothing on the page reads as the site being broken. Those strings appear only in the docblock and the class name. This is what "wayfinding page, not an error page" means in practice, and it governs any future copy change here.

### 28.8 Popular Questions Source (RULED S247)

The four questions in §28.5 were hardcoded at v0.35.x, with nothing in the template marking them as provisional. This is the pattern the `/help/` landing decision of 2026-07-03 explicitly rejected, because re-slugged articles leave baked links rotting; the sibling template `archive-faq_article.php` follows that decision correctly with a live query.

**Ruled (Kain, S247): the block is served by the same live query the `/help/` landing uses.** The four hardcoded links are removed and the questions are picked up automatically, per the 2026-07-03 decision. The provisional-marking fallback considered at S213 is dropped. The fix travels to Claude Code in the S247 brief. The block's visual layout is locked and does not change.

*Production implementation notes for this page are in the Production Implementation Notes document.*

---

## 29. Reviews Page Layout (APPROVED AND BUILT, Kain by eye, Code S053)

The reviews page is the written record: the 4,517 curated written reviews held in the Notion Review Bank and shipped in-theme as `data/reviews.csv.php`. One page, one instance, live at /reviews/. It is **not** the testimonials page (§30), which carries prerecorded member video.

Composed at S221 through `page-composition`, against the Document-Level Standards above; then designed live in Safari with Claude Code and approved whole by Kain on the live page (Code S053, theme v0.55.1): "this page is absolutely perfect." The signed record is the frozen approved page with the page spec beside it, both in the Verified Student Reviews Page folder under Proof + Funnel Design Prototypes; where that record and this section disagree, the record is correct and this section is the thing to fix. Approved is not done: the DSRD 6 gate, the schema decision and the Rank Math metadata remain with Code (§29.7). Rewritten S262 from the S053 page spec.

---

### 29.1 The job

**This page exists to get a prospective student who is checking Achology out to carry on to the course or school they were already considering.**

One action, one reader. The action is *continue to the course or school page* — not *buy*. The reviews page removes doubt; the course page closes.

**Subordinate job:** to be the page that answers "is Achology any good" for search engines and AI assistants. This adds requirements — real indexable review text, depth, and per-review markup — but it never reorders the page. Where the two jobs would disagree on order, the primary job decides.

---

### 29.2 The reader's arrival state

Built from the reviewers' own language across the 4,517-row review set. Percentages are of that set. Assumptions are labelled as assumptions, per the composition standard.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They are mid-decision, not browsing — they searched "Achology reviews" or followed a link from a course or pricing page | **Assumption.** No analytics exist for a page not yet built. Confirmed after launch from Search Console query data |
| A2 | Many have no psychology background and describe themselves as beginners | Evidenced — beginner and "new to this" language recurs across the set |
| A3 | Many are weighing Achology against other courses they have already taken | Evidenced — 148 reviews (3.3%) explicitly compare against other courses or training |
| A4 | A large share want to help other people professionally — coaching, counselling, helping | Evidenced — the largest outcome theme in the set at 671 reviews (14.9%) |
| A5 | Some are testing this against formal academic study | Evidenced — 95 reviews (2.1%) reference university, degree, accreditation or formal training |
| A6 | Some already know the courses from Udemy | Evidenced — 60 reviews (1.3%) name Udemy directly |
| A7 | They doubt an online, self-paced psychology training is legitimate | **Assumption — the weakest-evidenced line here, and deliberately marked.** Every review is written by someone who already bought, so the doubting non-buyer is absent from this evidence by definition. Confirmed only from support questions or a live exit survey |

---

### 29.3 The required state, as changes

Each change is one sentence in the reader's voice. This list is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now know this is a large body of review, not a handful." |
| C2 | "I now know it stretches back over a decade, so this isn't a recent push." |
| C3 | "I now know these are people all over the world, not one small pocket." |
| C4 | "I now believe these are real students, because I can see names, dates, courses and criticism." |
| C5 | "I now know I can narrow this down to the thing I actually care about." |
| C6 | "I now know what people with my concern actually said." |
| C7 | "I no longer worry the good reviews were hand-picked, because I can read the critical ones." |
| C8 | "I now know I can check any of this myself rather than take a summary on trust." |
| C9 | "I now know exactly where to go next." |

**Completeness check run:** the routing/teaching check (five questions — where am I, what is here, is this the right place for me, why should I trust it, where do I go next). This page routes and evidences; it does not sell, so the four selling frameworks were not the applicable test. The check surfaced C8, which the evidence alone had missed: a reader who cannot verify a claim independently treats the whole page as marketing.

---

### 29.4 Page Structure (as built and approved, S053)

The order as approved on the live page. This is also the mobile order: wider viewports may group blocks side by side but never reorder them.

| # | Block | Change it carries | Component status |
|---|---|---|---|
| 1 | Sticky header | site furniture | DSRD 8 §18 (LOCKED) |
| 2 | Breadcrumb: Home > Student Reviews | site furniture | DSRD 1 §9 |
| 3 | **Hero** | orientation; copy is Kain's own words (S052) | `.policy-header--doc` with `.policy-header--portrait` |
| 4 | **Global impact block** | C1, C2, C3 | One component `.gi`: intro, world map, markers, country panel, four figures. Decision history DSRD 8 §21; built |
| 5 | **The archive**: intro, control bar, live count, masonry grid, batching | C4, C5, C6, C7, C8 | Decision history DSRD 8 §22; review card DSRD 8 §14; control bar values are the DSRD 7 form-control standard; built |
| 6 | **Gateway** | C9 | `achology_routes_grid()`, reused from About; nine rows, not ten (S054 ruling, below) |
| 7 | **Enquiries panel** | C9 | `achology_warm_room()`, DSRD 8 §16, reused from About |
| 8 | Site-wide footer | site furniture | DSRD 8 §19 (LOCKED) |

**As rebuilt in Code's S141 and S142 sittings (Kain's rulings, recorded S393).** Four things about this table moved, and each is his.

1. **The reading column is 960** (theme 0.707.6). Kain chose C of four rendered widths (800, 880, 960, 1104) on the page itself: "yes, go with C please". Two review cards sit across, each about 470 wide at 1440 (452 at 1024), which keeps his S053 two-across ruling and ends the reviewer names cutting short. It is one scoped rule in `reviews.css`, annotated as a one-off; the site-wide article column stays 800. About and Testimonials were widened to the same 960 at 0.707.18 (one rule in `components.css`) so the shared gateway can only render one way.
2. **Block 4 is the dot world and block 5's header is rebuilt.** Decision history at DSRD 8 §21.3 and §22.2. The archive's batch is 32, not 50.
3. **Block 6 is the rebuilt Ten Ways gateway** (DSRD 8 §36, `achology_site_gateway()`), which replaced `achology_routes_grid()`. The S054 exclusion of the Watch Member Testimonials row below was set at this page's call site before the rebuild; Code states in his fold-back whether the page still omits that row.
4. **Block 7 is the FAQs block**, not the enquiries panel (DSRD 8 §37, `achology_faq_block()`). Its heading is "FAQs About the Achology Learning Experience" and it carries eight help answers (IDs 329, 406, 403, 281, 336, 350, 342, 269) with the registration credit line beneath. The Member stories block (the Five Aspects videos) is removed from Reviews and stays on Testimonials; the hero's Watch Testimonials button is the route there. The hero's primary button is Read the Reviews.

**The page was signed off by Kain in Code's S142 sitting** ("this page is actually pretty much perfect"). Code built its last structural edits over the page gate intake lock on Kain's direct instruction, and said so in his report. The closing brief carries a DOCUMENT TYPE line reading "not a page spec" (S392), which the intake wall reads; it carries no PAGE GATE line because it adds no block, value or copy.

**Two block changes from the S221 composition, both Kain's rulings at S053.** One: the standout reviews block is removed from this page, not deferred. His words: "I know that we might have agreed on some standard reviews, but I don't think they need to be incorporated into this page. I think what we have in this page is more than enough." The Featured flag and the standouts treatment stay specified for the course-page and school-page review blocks, which is where he pointed them. Two: the page closes on the About gateway and the enquiries panel, not the DSRD 8 §13 "Where next?" panel the composition named.

**The gateway carries nine of the shared set's ten rows (Kain, ruled directly in Code's S054 session; recorded here S265).** The Watch Member Testimonials card is excluded from this page: Kain saw it live, had not approved it, and ordered it off. The exclusion is implemented at the page's own call site in `page-reviews.php`; the shared `achology_site_routes()` set is untouched, because that ten-row set also feeds the About gateway and editing the set to satisfy one page would silently change another (DSRD 3 §2.6). Shipped and verified live at v0.60.6: the card is absent from `/reviews/` and still present on `/about/`. How the row got there is recorded as a lesson rather than a fault: nobody chose it; the page rendered the shared set and inherited the row. A page rendering a shared row set inherits every future addition to that set unapproved.

**The trust masthead of the S221 composition dissolved rather than being built.** C1 and C2 are carried by the global impact block's intro and figures; no separate masthead exists.

**The review card is the atomic unit of the archive.** It carries C4 by itself, every time it appears. Per DSRD 4 §14.4 it shows: review text, review title, star rating, first name plus surname initial, the word Verified, review date, and course. No per-review country.

**The archive's mechanics (ruled S053):** masonry grid, two columns at desktop and tablet, one below 600px, constant 24px gaps, plain CSS grid as the no-script fallback; batches of 50 appended in place on a real link, every review reachable by following links; default order striped across the star bands in proportion to their size, computed at import, a filtered view returning to newest first. The reasons and verification live in the signed record; DSRD 8 §14.5 and §22 carry the component-side record.

---

### 29.5 Both closing tests — run and reported

**Test 1 — every block carries a named change.** Passed for blocks 3–7. Blocks 1, 2 and 8 are site furniture present on every page; they are declared here as carrying no page-specific change rather than removed, matching the treatment in §20.1. No block was found that carries no change and no justification. Re-run S262 against the as-built order: still passes.

**Test 2 — every change has a block.** Passed. C1–C9 are each assigned above, and no change is carried off-page. Re-run S262: the standout block's removal moved C6 wholly onto the archive, whose search, filters and full text carry "what people with my concern actually said" directly.

---

### 29.6 Decisions closed (S221 and S239)

**1. Theme tags are visible on this page, and on this page only.** DSRD 4 §14.4 holds that theme tags are an internal routing label never shown to the reader. That rule was written for reviews appearing *as social proof on other pages*, where the tag works invisibly to pull matching quotes onto the right page. The reviews page is the one place a reader browses reviews as the content itself, where 4,517 unfiltered items is a wall nobody reads. §14.4 gains a scoped exception naming this page; the rule stands unchanged everywhere else. *Kain, S221.*

**2. All 4,517 reviews are shown, including the 3.0–3.5 star band.** The distilled set is tiered "Displayable" (4,060 rows, 4.0–5.0 stars) and "Insight" (457 rows, 3.0–3.5 stars). The tier boundary is exactly the star rating and nothing else — it is not a quality judgement. Showing only the Displayable tier would put a wall of 4- and 5-star reviews under a stated 4.66 average, with nothing on the page explaining why the average is not 5. The 3-star reviews are among the most considered writing in the set. Both the page's credibility and its value to an AI assistant asked whether Achology is any good depend on the critical reviews being present and findable. *Kain, S221.*

**3. Star rating is a filter control, not just a display value.** Follows from decision 2: a reader who can deliberately choose to read the 3-star reviews is being invited to check rather than asked to trust. This is what carries C7.

**4. The platform-era reviews show unedited (Kain, S239; typographic normalisation permitted, Kain, S262).** The 60 reviews naming Udemy and the ~526 addressing the instructor in the second person display verbatim: no trimming, no rewording, no exclusion. The page's claim is "every review since 2014, unedited", and the platform mentions are provenance, proof the record is real. This closes S221 open item O5. Amended S262 on Kain's ruling: typographic normalisation is permitted across all 4,517 reviews, meaning sentence-initial capital letters, a terminal full stop where a sentence carries none, and whitespace, and nothing else. Words are never added, removed or changed, acronyms in reviewers' own words stand at every mention (the DSRD 6 s1 carve-out), and the amendment exists so the record reads as cared-for text rather than a words dump while staying every reviewer's own words. The normalisation runs as a scripted pass with a dry-run report and a sample for Kain's eye before anything is applied (commissioned S262).

**5. The review card is locked (Kain, S239).** Full anatomy in DSRD 8 §14, every value approved by eye on rendered cards carrying live bank data. Includes the review title (the reviewer's own words, lightly trimmed; production rule in DSRD 8 §14.5) and the course signpost footer with each course's DSRD 1 URL baked at import.

**6. Standouts are chosen by size (Kain, S239).** The Featured set renders in the locked card scaled per the §6.6 featured-quote language; exact values in DSRD 8 §14.5. This closes the standout-treatment question deferred at §29.8. The standout source is the hand-picked Featured flag in the live bank, data source `collection://24b47674-bb62-4992-bdc7-0d1a10183f76`, verified live at S239 (closes O2).

**7. The map band is commissioned (Kain, S239).** The page carries DSRD 4 §14.2 Variant 1 beneath the trust masthead; the placement and the accurate-geography requirement are recorded at DSRD 4 §14.2 (closes O3).

**8. The archive control bar (Kain, S239).** One compact bar: keyword search first, then Theme, Course, and Rating dropdowns, with a plain hint line beneath teaching by example, and a live results count line above the grid whose number is real. Values travel in the signed page spec.

**Decisions ruled at S053, on the live page (recorded S262). These complete and partly supersede the list above.**

**9. The standout reviews block is removed from this page** (§29.4). Supersedes decision 6's placement here; the Featured flag, the standout source and the treatment stay specified for the course-page and school-page review blocks. The scaling half of decision 6 had already been withdrawn by Kain at S240: standouts render at normal card size wherever they appear.

**10. The map band became the global impact block.** Decision 7 commissioned DSRD 4 §14.2 Variant 1; what was built and approved is one component (`.gi`) carrying intro, map, markers, country panel and four figures together. Decision history at DSRD 8 §21.

**11. The grid is masonry, two across.** Constant 24px gaps, each card snapping under the shortest column. Supersedes the plan's three-across equal-height grid: on this data, equal heights put a 256px review inside a 1046px card, and Kain rejected both the stretched grid and per-card heights.

**12. The batch is 50**, appended in place on a real link, so every review stays reachable with no scripting. Was Code's 24.

**13. The default order is striped across the star bands**, each band laid across the whole archive in proportion to its size, newest first within its band, computed at import. This is how decisions 2 and 3 survive mixing: the critical band appears throughout rather than sorting to the end. A filtered view returns to newest first.

**14. Every control bar value is settled.** Kain ruled at S053 that no candidates remain and the page is final; the values became the site's first form-control standard, written at DSRD 7 (S262).

---

### 29.7 Still open, and the page's remaining definition of done

| # | Open item | Where it goes |
|---|---|---|
| O1 | Which themes surface as visible filter labels, and their exact wording. Working set rendered and not objected to at S239 (eight, benefit-led: Coaching and helping; Practical application; Relationships; Career growth; Self-awareness; Confidence; Wellbeing; Purpose; teaching quality and value stay internal). The Theme dropdown and the review card titles are unbuilt until the Cowork tagging pass supplies `review_theme` and `review_title` values; the renderers already accept them. Closes by eye at that point, then records in DSRD 4 §14.4 | Kain's eye when the tagging pass lands; DSRD 4 §14.4 |
| O2 | CLOSED S239: see §29.6 decision 6, and its S053 supersession at decision 9 | — |
| O3 | CLOSED S239: see §29.6 decisions 7 and 10 | — |
| O4 | The schema plan, given no star rich snippets are available for self-hosted reviews about one's own organisation. **Not owned by this document**: schema ownership was settled at S219 and per-page-type schema lives in DSRD 10. With Code to decide and state | Code, next session; DSRD 10 |

The page's remaining definition of done, held by Code: the DSRD 6 gate with its per-chapter record, the schema decision (O4), and the Rank Math metadata (title, description and og:type answered by Chat at S261, in Code's inbox).

---

### 29.8 The design session happened live in Safari

Every question this subsection once deferred was settled by Kain's eye on the live page across Code's S052 and S053 sittings, under the standing rule 16 Safari surface. The settled answers live in the signed record and the component entries: the masthead dissolved (§29.4), the review card at DSRD 8 §14, the control bar as the DSRD 7 form-control standard, the map inside the global impact block (DSRD 8 §21), mixed star bands by the striped order (§29.6 decision 13), and batching as load-more on real links (decision 12).

---

### 29.9 Components this layout commissioned, as they resolved

| Component | Resolution |
|---|---|
| Review card | Built and locked. Prototype and build sheet in the Card System folder; decision history DSRD 8 §14 |
| Trust masthead | Dissolved at S053 into the hero and the global impact block; never built |
| Filter bar | Built. Prototype and build sheet in the Form Controls folder under Component Design Prototypes; its values are the site's form-control standard at DSRD 7 |
| Country map (Variant 1) | Superseded: built as the map band inside the global impact block, DSRD 8 §21 |
| Global impact block | Built (not in the S221 list; emerged in the Safari sittings). Decision history DSRD 8 §21 |
| Review archive | Built. Decision history DSRD 8 §22 |

*Recorded for `component-library`.*

---

## 30. Testimonials Video Page Layout (COMPOSED — NOT YET LOCKED)

The testimonials page carries prerecorded member video: 46 videos, ten named members answering the same five questions on camera (nine answered all five; one answered Q4 only). Source of truth is the Notion "Testimonial Videos" database (`9beec85f-6eaf-49e5-be77-273b19351632`); the 46 Vimeo URLs live there and are not copied around. It is **not** the reviews page (§29), which carries written review.

Composed at S221 through `page-composition`, against the Document-Level Standards above. Nothing here is a visual decision — appearance is deferred (§30.8). **This map was written before Claude Code's build landed, so it can serve as the yardstick that build is audited against (rule 13).**

---

### 30.1 The job

**This page exists to get a hesitating visitor — one already being pointed here from a course, membership or sales page — to commit to studying with Achology.**

One action, one reader. Unlike the reviews page, this page **closes** rather than routes. It is the highest-trust human proof on the site and the page a course or sales page links out to when a visitor is nearly there but unsure. The action is *commit* — begin the enrolment or membership step the referring page was offering.

**Subordinate job:** to be indexable proof for search and AI assistants, via transcripts and per-video schema. This earns real E-E-A-T but never reorders the page. Where the two would disagree, the primary job — closing a hesitating visitor — decides.

*Note the deliberate contrast with §29. Reviews removes doubt and hands off; testimonials removes doubt and asks for the decision. That is why the two proof pages are composed separately rather than sharing one structure.*

---

### 30.2 The reader's arrival state

These visitors are further down the path than reviews-page visitors — they have been sent here by another Achology page, not found by a cold "reviews" search. Arrival is inferred from that referring context and from the member answers themselves; assumptions are labelled.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They are near a decision and were sent here to help them make it — a course, membership or sales page pointed them here | **Assumption**, but a strong one: this is the page's stated role in DSRD 4 (course pages and the membership page link to `/testimonials/`). Confirmed after launch from referral-path data |
| A2 | They have read the claims already and now want to see whether real people say the same unprompted | **Assumption** from the page's position late in the funnel |
| A3 | They doubt that a self-paced online psychology community delivers what a structured or in-person one would | Inferred — the member answers repeatedly address exactly this doubt (Q3 is about the value of a collaborative peer-learning environment) |
| A4 | They wonder whether people "like them" belong here | Supported — the ten members span countries (Scotland, Chile, Netherlands, N. Ireland, England, Italy) and walks of life; the international spread is real, consented data |
| A5 | They are wary of scripted, cherry-picked testimonial reels | **Assumption**, and the one the whole page design answers: unscripted people answering the same fixed questions is the counter to it |

---

### 30.3 The required state, as changes

Each change is one sentence in the reader's voice. This is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now understand what this page is: real members, unscripted, all answering the same honest questions." |
| C2 | "I now see and hear a real person, immediately — not a logo or a star rating." |
| C3 | "I now know what someone like me would say to a person standing exactly where I am." |
| C4 | "I now believe the community itself, not just the courses, is where the value is." |
| C5 | "I now know what people actually gained, in their own words." |
| C6 | "I now see these are real, different, named people from all over — not actors, not a type." |
| C7 | "I now trust this is unscripted, because ten people answer the same question and none of it is polished the same way." |
| C8 | "I now know the exact step to take, and I'm ready to take it." |

**Completeness check run:** the page **sells**, so the four banked selling-frameworks were the applicable test — not the routing check used for reviews. Findings, and how the structure answers each:
- *Problem named / stakes visible (SB7):* the reader's hesitation is the problem; the page never states it aloud but answers it — leading with Q4 (§30.4) puts their own unspoken question first. **Present.**
- *Value understood (Value Equation):* C4 and C5 carry the dream outcome and its likelihood in members' own words. **Present.**
- *Objections and risk answered (Cialdini):* C7 answers the "this is staged" objection through unscripted convergence; social proof is the page's entire mechanism. **Present.**
- *Position clear against alternatives (Dunford):* C4 positions the collaborative community against self-paced-alone and against formal/in-person study — the alternatives A3 names. **Present.**
- The check **surfaced C1** — without a framing intro the reader meets a wall of video with no idea why the same faces recur; the frame is what makes the repetition read as honesty rather than filler.

---

### 30.4 Page Structure (top to bottom)

The derived order. This is also the mobile order — wider viewports may group side by side but never reorder. **Leading with Q4 is a derived decision, not a preference:** Q4 ("what would you say to anyone thinking about studying with Achology?") is the exact question in the hesitating reader's head (A1, A2), so C3 must land before the fuller picture, and ten people converging on it is the page's strongest single move.

| # | Block | Change it carries | Component status |
|---|---|---|---|
| 1 | Sticky header | — site furniture | DSRD 8 §18 (LOCKED) |
| 2 | Breadcrumb | — site furniture | DSRD 1 §9 |
| 3 | **Framing intro** | C1 | **New — short copy block** |
| 4 | **Hero video** (single, opens the page) | C2 | Video player + transcript; see §30.9 |
| 5 | **Q4 section** — "what would you say to anyone thinking about studying with Achology" | C3 | Question-headed video group |
| 6 | **Q1 section** — how have you benefited | C5 | Question-headed video group |
| 7 | **Q2 section** — the main lesson that added most value | C5 | Question-headed video group |
| 8 | **Q3 section** — value of a collaborative peer-learning environment | C4 | Question-headed video group |
| 9 | **Q5 section** — the five things you value most about the community | C4, C5 | Question-headed video group |
| 10 | **Primary CTA** | C8 | Existing CTA pattern — inherits the referring page's offer |
| 11 | Site-wide footer | — site furniture | DSRD 8 §19 (LOCKED) |

**Carried by the whole, not one block:**
- **C6** (real, different, named people) is carried by every video showing its person's name and country — country **is** shown here (unlike §29), because these are named people who consented on camera. It is a property of the video group, not a separate block.
- **C7** (unscripted) is carried structurally by the five-question spine itself: the same question answered ten different ways is the proof. No block asserts "these are unscripted" — the format demonstrates it.
- **Transcripts** sit beneath every video (C5's indexable form and the accessibility win). Deliberately **not** a mini-article per video — 46 near-duplicate texts would be thin content; the transcript is supporting text on the one rich page.

**The CTA repeats without a new change (rule 9).** The job's action — commit — may be placed wherever a reader becomes ready: a quiet instance after the Q4 section for the reader already convinced, and the primary instance at block 10. Same action both times, never a different exit.

---

### 30.5 Both closing tests — run and reported

**Test 1 — every block carries a named change.** Passed for blocks 3–10. Blocks 1, 2, 11 are site furniture, declared as carrying no page-specific change (as §20.1, §29.5). No block carries no change without justification.

**Test 2 — every change has a block.** Passed. C1–C5 and C8 map to blocks; C6 and C7 are carried by the video group and the question spine respectively, named above rather than given a block of their own — because inventing a "these are real / these are unscripted" block would *assert* what the format already *demonstrates*, which is weaker.

---

### 30.6 Decisions and recommendations at S221

**1. Section order: Q4 → Q1 → Q2 → Q3 → Q5.** Derived (§30.4), and matching Code's own recommendation in the agreed plan. Q4 leads because it is the reader's own question; Q1/Q2 give the fuller benefit picture; Q3/Q5 carry the community-value change (C4) that answers the reader's deepest doubt (A3), placed later where they are weighing commitment.

**2. Country is shown per video.** Consented on-camera data about named people — no integrity problem, and the international spread is an asset (C6). This is the deliberate opposite of the reviews-page rule (§29, no per-review country) and the difference is sound: there the country would be an inferred guess about a private person; here it is a fact the person gave.

**3. No mini-article per video.** 46 short near-duplicate texts is thin content Google penalises. Transcripts live as supporting text on the one page. *Recommended.*

---

### 30.7 Still open — carried, and the ones Code is mid-build on

| # | Open item | Where it goes |
|---|---|---|
| O1 | The hero video pick, and any "Featured" picks. **No selection exists** — the Featured flag is unused across all 46. *Recommended:* the hero is a strong Q4 answer, so the very first thing the reader sees is someone answering their own question | Decide with Kain |
| O2 | The transcript pipeline, proven on **one** video before scaling to 46. Vimeo may already hold auto-transcripts; else the audio is transcribed. **This is a build task — likely what Code is on now** | Claude Code; confirm which route |
| O3 | Whether the ten per-person "member story" articles are built later. The page is complete without them; the door is open once transcripts exist. *Recommended:* defer — ten rich articles later, not now, and never the 46 thin ones | Backlog-with-trigger (trigger: transcripts complete) |
| O4 | How the 46 videos' data reaches the theme at build, Notion staying source of truth. Ties directly to O5 — the schema field source and the display data source should be **one** decision, not two | Decide with Kain; route to DSRD 10 |
| O5 | **VideoObject schema field source.** Code flagged (note 2026-07-22) that the theme holds only Vimeo ID + poster — no per-video title, description, upload date or duration, all of which Google requires. The printed question on each thumbnail can serve as `name`. *Recommended:* one ACF field group (title, description, upload date, duration, Vimeo ID, poster) mirroring how Person and FAQ-audio schema already work, fed from the Notion export — so display data and schema data arrive by the same route. **This is the real decision behind O4** | Decide with Kain; DSRD 10 §9 gains VideoObject rows |

---

### 30.8 Deferred to a design session

- How the hero video sits above the five sections without dwarfing them
- How a question-headed group of up to ten videos is laid out — grid, row, or stack — without becoming a wall
- How a transcript sits beneath its video: open, collapsed, or on demand
- How name + country presents on each video
- The click-to-play poster treatment (plumbing mirrors the About videos — Vimeo, click-to-play so the page stays fast; Code's domain)

---

### 30.9 New components this layout commissions

| Component | Needed by | Status |
|---|---|---|
| Question-headed video group | Blocks 5–9 | New. But **check the About page member-stories block first** (`.about-proof__strip`, `.proof-card*`, `.about-video-lightbox*`, DSRD 8 §12.2) — it is the first built instance of testimonial video + Vimeo lightbox and is flagged there as a reuse candidate for exactly this page. Promote it, don't build a second |
| Hero video | Block 4 | New — may be the same player as the group, sized up |
| Transcript block | Beneath every video | New |
| Framing intro | Block 3 | New — copy block, likely no new component |

*Recorded for `component-library`. The member-stories reuse candidate is the key note: this page is the second use that promotes it (DSRD 8 §12.3 procedure). No visual decisions taken here.*

---

## 31. Policies Index Page Layout (LOCKED, Kain S236)

The Policies index at /policies/ is the gateway into every document that governs Achology. Its job: get a visitor who is checking whether Achology can be trusted to open the policy that answers their question. It routes; it never sells. It is a quiet text-led page under section 25 (the 880px reading column) and section 27 (the sentence test), rendered through the policy template family. The card treatment is the built page's existing pattern and is the authority; this section locks the block order and what each block is for.

### 31.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 section 18)
2. Breadcrumb: Home icon, chevron, "Policies" (DSRD 1 section 9)
3. H1 plus lead paragraph: says what the page is at a glance
4. Governance paragraph: the quotable answer to how Achology governs itself (who owns it, what rules bind it, that everything is published openly)
5. Hairline
6. Group heading "Our Legal Policies", then the seven policy cards in this order: Privacy Policy, Terms and Conditions, Cookie Policy, Refund Policy, Trust Statement, Disclaimers, Accessibility Statement
7. Hairline
8. Group heading "Our Training Standards", then two cards: The Achology Manifesto (links to /about/manifesto/) and Code of Ethics (links to /about/code-of-ethics/)
9. Rainbow stripe plus footer (DSRD 8 section 19)

This is also the mobile order. Nothing else appears on the page: no closing CTA panel and no sales content, because the page's job ends when the reader picks a document.

### 31.2 Card anatomy

Each card carries the document name, one plain description line saying what the document covers and when a reader would need it, a chevron right, and the ghost word behind the text (the one word the document is about, specified at DSRD 8 §12.6; desktop and tablet only). The whole card is the link. The card's visual values are the built page's locked pattern; where this section and the built page ever disagree on a visual value, the built page is correct and this section is the thing to fix. Verified against the shipped page (theme v0.36.49) at S238: the built order matches 31.1 exactly.

### 31.2a The card band: the cards bleed to 944 (RULED, Kain S090, on the whole rendered page in Safari)

**The nine cards take the DSRD 7 section 4.4 inset panel width, 944px**, the 880 reading column plus a 32px bleed each side, with matching 32px inner padding. Nothing was designed for this: it is the locked mechanism applied to a page that did not yet follow it, and the Policies index is now a named user of it in DSRD 7 section 4.4.

**Kain asked for it in his own words:** "on the Achology's Policies and Standards page, please apply our principle that lets cards sit outside the container be applied to the different policy cards." **He approved it looking at the whole page in Safari:** "Yes, it does. Its possibly the best looking policies page I've ever seen."

**What it fixed, measured before and after on the live page.** Every heading and paragraph on the page starts at 280 at desktop. Each card also started at 280 and carried 24px of its own padding, so the words inside a card began at 305: **the page had two left edges 25px apart.** The card now reaches 32px further out on each side and holds 32px inside, so its words land back on 280.

| Width | The card | The page's writing | Sideways scroll |
|---|---|---|---|
| 1440 | left 248, width 944 | h1 at 280; card text at 281 | none |
| 1039, just under section 4.4's boundary | left 80, width 880 | h1 at 80, width 880, flush | none |
| 390 | left 20, width 350 | flush with the h1 | none |

**The 1040 boundary is section 4.4's own and was not chosen here.** Below it the bleed is off, so nothing changed on a phone or a tablet. Shipped v0.120.0 to v0.121.0 and read back on the live page at all three widths.

### 31.2b The header copy, given whole by Kain in session (S090)

Both paragraphs are his own words, placed verbatim in the template and read back off the live page. The page carries no excerpt, so the template default is what every visitor reads.

> This page outlines the rules, policies and standards that govern Achology, including our legal policies, business practices, and the timeless principles we hold ourselves (as a training organisation) to. All our policies are transparent and publicly accessible, so you always know where you stand with us.

> Achology is owned and run by its remaining original founders, Kain and Karen Anne Ramsay, through two registered companies in Scotland, UK. Achology adheres to best practices for public trading and is supported by seven legal policies, a Manifesto, and a Code of Ethics that oversee its online teaching and mentorship activities. All these documents are available on this page, written in clear language for anyone to review at any time, whether or not you are an Achology member: someone who has joined the private learning community at community.achology.com.

**One punctuation substitution, made openly and told to him in session.** His second paragraph arrived with an em dash before "someone who has joined". His own S222 ruling at DSRD 2 section 3.0 bans it anywhere in Achology copy with no exception, and the gate refuses a file containing one, so it is a colon, which that same sentence already used. Not one word changed, and he can overturn it.

**Two outbound links, in the second paragraph only, at his instruction.** "two registered companies in Scotland, UK" goes to the Companies House record for SC697126, opened and read back before shipping, its heading reading ACHOLOGY TRANSACTIONS LTD.; "best practices for public trading" goes to tradingstandards.uk, the Chartered Trading Standards Institute, which the Disclaimers page already links for this exact idea. Both carry `target="_blank"`, `rel="noopener"` and a visually hidden "opens in a new tab".

**Two things found by reading the page back rather than by any gate.** The links first shipped in the browser's default blue with a heavy underline, because `.policy-header__copy` sits in `.policy-header` rather than `.policy-body` and was therefore outside every link rule on the page; it had never carried a link, so nothing had ever exposed that. The locked site-wide body-link treatment was extended to it verbatim in v0.120.3, with no new value chosen. **And DSRD 7 section 1.0 asks for a visible outbound marker on external links, which no policy page carries.** The only sized marker in the theme is the book note's, and inventing a second is a visual decision and therefore Kain's, on a render, under standing rule 16. **That is the one thing still open on this page.**

### 31.3 Copy ownership

The approved copy (H1, lead, governance paragraph, both group headings, and all nine description lines) is recorded in the signed spec `SPEC__Policies_Index_Locked_Layout_And_Copy.md` (S236, channel; updated S238 to the as-built copy after Kain replaced the lead and governance wording in the build session) and lives in the theme's policy content partial as built. Ruled S236: the gateway lists all nine governing documents, the two standards documents keeping their /about/ addresses.

---

## 32. Book Note Page Layout (ARRANGEMENT RULED S085; HERO RULED S102; REBUILT ONTO THE ARTICLE'S LAYOUT AT S113; TAKES THE QUOTE PAGE'S STRUCTURE AT S147)

**S149 and S150: the three reading pages share the rail, the date line, the type link and one hero. Read the note at the head of section 22 first; it governs where it touches this section. The S150 sitting changed this page in four places: the hero's bubbles (item 10 there), the panel's cover and button at the foot of the screen (item 16), the five body headings (§32.7) and the standfirst's closing line (item 19; §32.3, §32.9 item 1).**

**THE BOOK NOTE TAKES THE QUOTE PAGE'S STRUCTURE (Kain, live with Code in Safari on Words That Change Minds, Code's S147; recorded by Chat S401 from RULING__The_Book_Note_Page_Sitting_S147, channel Archive). Theme 0.707.83 to 0.707.92.** Where this note and an older line below disagree, this note governs.

1. **Explore More Book Notes** sits after the signature's hairline, the quote page's block, markup and S130 rules: six, three or none; two columns from 768; other book notes in the same category, newest first. A sixth contents entry names it. Its line, in Kain's words: "Each Book Note highlights a book's key ideas, helping you to decide which one to read next." Each line opens with the book's own cover, 56 wide, then the book's title, then "A book by {author}" in grey (0.707.92, Kain's new layer of transparency: the books are not presented as written for Achology; the wording is Code's first draft, live for Kain's correction).
2. **No Related Further Reading at any width** (§22.8). The side panel, with the cover, travels to the hairline closing Explore More Book Notes and rests 48 above it. From 1200 up, on screens 760 tall or more, the cover and the Amazon button lock to the foot of the screen.
3. **Three Achology bubbles behind the hero cover,** the quote page's sizes, from 1200 up, trimmed by the band so nothing scrolls sideways. **Superseded S150 (0.707.121): the three bubbles are gone; a thin orange speech bubble line sits behind the book, following the book's own size, shifted 40 left and 24 down; see the note at the head of section 22, item 10.**
4. **Numbered section headings:** each heading in the writing carries the contents' number (01 to 05) as a small orange label, hidden from screen readers (0.707.87).
5. **The reading progress line is a site standard (0.707.89):** a 2px brand-orange line on a hairline-grey track over the header's bottom hairline, on articles, book notes and quote pages, and on workbooks when the workbook page is built (§37).
6. **A STANDING RULING, never reopened:** the reading column's width and the body text size are the same on every content type and are not changed. Kain, S147: "we can't go playing around with font size ... this is standardized across the entire website ... no changes here at all, must remain as it is." Measured at 1440: 800 wide at 18px on the book note and the quote page alike. For the same reason a drop cap and a tint of the book's colour are set aside: both touch the type scale or the brand colours.
7. **Ratings as a visual: dropped.** Kain's v0.167.21 ruling makes the Essential Reading badge the rating's only visible mark; the Goodreads score is never shown.
8. **Open with Kain:** whether the "all articles from this book" line moves into Explore More Book Notes; and whether the three shapes that need new words per book note (a key ideas box under the opening, one pull quote per long section, numbered takeaway cards) are commissioned. Code builds the shapes only once words exist.
9. **The list covers fail three image lines** (the size suffix in the filename, JPG, no srcset), joining the hero cover's existing JPG and budget fails. WebP copies of every book cover belong to the Image and Icon Optimisation card (Chat, S401).

**THE LATER S147 RULINGS AND THE DESIGN SIGN-OFF (Kain, live with Code in Safari, Code's S147, theme 0.707.93 to 0.707.98; recorded by Chat S403 from RULING__The_Goodreads_Link_And_Course_Block_Words_S147 and RULING__The_Book_Note_Is_Finished_And_The_Quote_Course_Picture_S147, channel Archive).** These were made after the sitting file above was archived and amend the note above where they touch it.

10. **The book note page is finished, as a design.** Kain at 0.707.96: "this booknote page is ... finished now, Claude. Um, one hundred percent." This closes the page's design sittings (the second Safari look and the open items at §32.9 are closed by his word). It is his design sign-off, not a closed DSRD 6 record: the record still carries its machine lines (keyword density, acronyms, image formats on the media library covers, the record's own not-run chapters).
11. **View on Goodreads in the date line (0.707.93).** The third fact after the date and the reading time, in the date line's grey, orange on hover, opening the book's own Goodreads page in a new tab, built from the book's ISBN (the schema's sameAs). A book without an ISBN shows nothing (142 of 150 published book notes hold one). No Goodreads score is shown anywhere and a third-party score never enters the page's own rating markup; item 7 above stands. Chosen by Kain as a link only, tab 1 of four, "as just another layer of credibility".
12. **The section numbers sit above the headings (0.707.94).** Item 4 above is amended: the small orange label sits on its own line, 8 above the heading words, never beside them. Kain, on the beside version: "That's just not what we agreed."
13. **The author photograph in the writing carries the hero's three bubbles in miniature (0.707.95 to 0.707.98).** Book notes only, portraits only, from 768 up; on a phone the photo keeps its plain, centred look. First tab 1 of four at 0.707.96 ("very, very strong ... it really brings the page to life"), then refined at 0.707.98 to tab 3 of four when Kain saw the bubbles had shrunk the picture and pushed it down: the picture 224 wide with its top the figure's top, on the paragraph's first line, the figure 256 wide, the bubbles in the 32 strip at its right (96, 48 turned at the picture's foot, 22 between), the caption the picture's width. The values live in the Author Photo component's build sheet (prototype v2); this section records the ruling only.
14. **The course block's words on every reading page (0.707.93), Kain's text:** "Ready to Take Your Learning Further?" over "Explore related courses to deepen your knowledge and build on the insights introduced in this article." He kept "this article" for book notes and quote pages too. §22.10 carries the words; this line records that the ruling was made on the book note.
15. **A named page-gate exception.** The block-heading check flags "Book" and "Note" as mid-sentence capitals in Kain's approved line under Explore More Book Notes (item 1 above, "Each Book Note highlights ..."). His capitals stand, "Book Note" being a name. Recorded here as the exception; the gate reads it as a note on this page.

16. **The section numbers are one orange on all three reading pages (Kain, live with Code in Safari, Code's S149, theme 0.707.109, tab 1 of four; recorded by Chat S405 from RULING__The_Section_Numbers_S149, channel Archive).** Kain: "The small numbers before each section heading are inconsistent in colour and format across all three templates." On book notes and quote pages the small number above each heading and the contents' numbers are the label orange (`--color-orange-link`). The contents' last entry, Explore More, carries its number above its heading too. Articles carry no numbers, unchanged from §22.14 item 4. A fault fixed on the way: the book note numbers had drawn dark grey, not the orange approved at S147, because a colour name set only inside the side panel resolved to nothing outside it. §40 item 7 carries the quote page's half.

**THE BOOK NOTE TAKES THE ARTICLE'S LAYOUT, BLOCK BY BLOCK (Kain, live in Code's S113 sitting on the rendered pages; folded S358). Theme 0.381.0.** His instruction: *"Could I ask you first to be really thorough, please? Do literally a section by section comparison of the book notes page up against the article page."* Both pages were then walked block by block in a live browser at 1440 and **every edge read off the rendered page rather than out of a file**. Nine differences were found, eight closed, one put to Kain and answered at S358. **Where this round and anything below it disagree, this round governs**, and the older text is kept as the record.

**The reading area of this page IS the article's, not a copy of it.** Forty seven selector lines inside the S112 rebuild's media block in `knowledge-hub.css` read `:is(.kh-article__body, .bn-body)`, so the rail's rules exist once and reach both page types. A future ruling on the rail reaches this page without anybody remembering to copy it. The page therefore inherits DSRD 9 §22's fourth round whole: the 1104 grid, the 800 reading column, the 48 gutter and the 256 side rail.

| # | The difference found | What now governs |
|---|---|---|
| 1 | The reading bar sat at the top of the writing, a screen below the title | It sits in the hero directly under the lead, where Kain put the article's at S110 |
| 2 | The bar still carried the writer's photograph and name, on a page whose author card at the foot already carries both | Removed, on Kain's S112 ruling for the article. The argument is passed empty; the component itself is untouched |
| 3 | The lead was a step below the body: 16 over a 46-letter measure, against the article's standfirst at 21 over 55 | Both now render 693px. **This overturns Kain's own S249 approval of 46**, and says so in the stylesheet: his S112 ruling is the later word on the same question |
| 4 | There was no way to share a book note at all | A share row at the foot, landing at 716 to 968, the article's own position exactly |
| 5 | The side panel drew a second share row, so the marks appeared twice | The call passes `panel`, which is what the article has passed since S112 |
| 6 | Related Further Reading printed twice: six in the rail and nine at the foot, four of them the same books | The full-width block is off, on the article's own S112 ruling. The rail shelf of six is the only one |
| 7 | The foot sat on a different left edge entirely: three left edges on one page, the foot at 320 while everything above had moved to 168 | All five foot edges now read the article's set: 168, 168, 716, 168, 168 |
| 8 | The $7 membership panel was still drawn here | **Off, on Kain's word in the sitting ("yes").** This was the last content page still drawing it, so the two page types now end identically: writing, author with the share marks on his own line, two courses, footer |
| 9 | The cover did not follow the reader. The article's picture opens at the top of the rail once the hero scrolls away; the book note's cover left with the hero and never came back | `achology_article_aside()` takes an optional picture and the book note hands in its cover. **The cover variant keeps 2:3 at 256 by 384 rather than being cropped square**, because cropping a jacket to a square cuts the title off the one picture whose job is to show it. A caller passing nothing is untouched |

**The band's ground: ruled and closed (Kain, S358).** The article's hero band is the article's own picture washed almost out, so every article's banner takes its colour from its own subject. **The book note's band keeps the shared bookshelf photograph**, the same file on all of them. Kain was asked whether the book note should take its ground from the book's own cover instead and ruled no: *"the article page rules are different."* Two page types, two deliberate rules. The drawn book cover work is unblocked by this and does not change the band.

**One property had to be repeated, and the reason is recorded so nobody deletes it.** `.bn-body { display: flow-root }` earlier in `book-note.css` carries one class and so does the shared `:is()` selector, so the later sheet won on source order and the grid's `display` never landed while its columns did. One line of `display: grid` sits in `book-note.css` for that reason alone. **Found by measuring the deployed page, not by reading the file.**

The individual Book Note page, at `learn/{kh_category}/book-notes/{slug}`. One template serves all 598 notes. Every value below was approved by Kain by eye, on a rendered full page, across the S249 and S250 design sessions.

**Status, changed at S343, on Kain's S102 evening sitting with Code (5 September 2026).** The hero is ruled. Kain looked at the built page at desktop, tablet and phone in Safari through thirteen ships (theme v0.167.14 to v0.167.26) and approved the hero and its Essential Reading badge as built at v0.167.26, in his words: "Thats perfect work claude - thank you!!!" (`RULING__Kain_Approves_The_Book_Note_Hero_And_Badge_As_Built_At_v0_167_26_S102`). What he ruled is written into §32.3 (the hero, its stack and its three responsive tiers), §32.4 (the badge repeated at the head of the last section) and §32.9 item 1 (the rating's only mark on the page is now the badge). The headline pattern he set the same evening is already at §32.8. **Still open after the sitting:** the reading zone's vertical rhythm and block margins (§32.4), the Share this Article block, the primary button's destination (§32.3), the Goodreads line's home, and the contents-list highlight (§32.9 item 8). Those remain the second-look sitting's.

**Status, changed at S085.** Kain ruled V3 on the rendered sitting at `achologytest.com/book-note/book-note-sitting.html`: the travelling shelf is retired and the page takes the article page's own pattern at 880px. **The arrangement is ruled; the layout and the spacing inside it are not.** His words were exact: "V3, both, although we need to talk through improving the final layout and spacings". So this section is no longer a complete go-live spec. The structure rows below carry V3; the vertical rhythm, the block margins and how the two moved blocks sit against the writing are a Safari sitting with Code on the real page, and none of it is written here until that sitting has run. The foot of the page was not reached in the same sitting and is unruled. The copy and metadata formulas (§32.7, §32.8) are untouched by all of this and stand as locked. The approved page and its developer brief live together in the Book Note Page folder, under Knowledge Hub Design Prototypes in the Achology Website Pages folder; where the page and this section disagree, the page is correct and this section is the thing to fix.

**The page's job (Kain, S249):** hand the reader the heart of one book, help them decide whether to read it, and offer an Achology.com course as the practical next step. Two next steps, not one.

### 32.1 Page structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Hero, full bleed (§32.2)
3. Reading zone: one 880px column, no shelf (§32.4). Two blocks sit inside the writing, in the article page's own places: a Table of Contents at the top, and one course card after the first section, filled by the tag rule at DSRD 1 §5.7 and never hand-picked (Kain, S085, V3)
4. Author signature block (as DSRD 9 §22.7, band withdrawn S088)
5. The courses block: **the words at §22.10 ("Ready to Take Your Learning Further?" since Code's S147; "Want to Expand Your Understanding?" from S088 to S112)** over the one sentence Kain gave for every content page (§22.10), **two course cards, filled by the tag rule at DSRD 1 §5.7**. *The S252 ruling below (three cards at desktop, two below) is superseded by S088's three-block foot standard, on which the course row is the two cards; kept as the record.*

   | Tier | Columns (DSRD 8 §7.0, unchanged) | Cards (S252, SUPERSEDED S088) |
   |---|---|---|
   | Desktop, 1024px and up | 3 | 3 |
   | Tablet, 768 to 1023px | 2 | 2 |
   | Phone, below 768px | 1 | 2, stacked |

   The third card is withdrawn below 1024px in CSS. Without that, three cards leave an orphan on a two-column tablet row and a three-deep stack on a phone.

   **DSRD 8 §7.0's columns need no amendment.** Its 3 / 2 / 1 was already correct and already built in `cards.css` as `.product-section__grid`; no template had ever used it. The S050 build wrote its own two-column grid instead, rendering each card at 540px against a card designed at roughly 368px, which is the stretching Kain saw. The row now takes the specified grid untouched: 352px at desktop, 406px at tablet, 335px at phone, with no horizontal scroll at any width.

   *Recorded as a defect report as well as a ruling, because half of this needed no ruling at all: an open specification needed applying.*
6. Related Further Reading, nine links, with the way back and the way forwards beneath and no hairline between (§22.8, Kain S088)
7. The closing trial panel (DSRD 8 §16, the trial variant; §22.10a) **was taken off this page at S113**: Kain's "yes" in Code's sitting, on the same ground as the article at S112, because the footer carries the same $7 offer fifty pixels below it, and the built page sets `'trial' => false` accordingly. **Corrected S394 on the drift sample, which found this item and §32.6 still describing the panel as live.** *The "Next possible steps" panel that stood here is retired, §32.6.*
8. Rainbow stripe and footer (DSRD 8 §19)

**The foot is the S088 standard, corrected here at S341.** Kain's words at S088: three blocks under the body on every content page, the two course cards, Related Further Reading and the trial panel, with the page types differing at the hero and nowhere else. Code's S102 read of the built page against this section (`REPORT__DSRD_9_Section_32_Read_Against_The_Built_Book_Note_Page_S102`) found the build carrying exactly that foot while this section still described the S249 foot: three cards, two hairlines and the retired panel. The document was wrong and the page was right, per this section's own head note. Items 4 to 8 above now read as built. **One thing the read found that no ruling names: a "Share this Article" block inside the writing.** It is recorded here as present on the built page and unruled; whether it stays is for the second-look sitting.

**The S249 "Nothing else" ruling stands in spirit and is superseded in letter.** Kain ruled at S249, on the rendered page, that the article card grid, the quote card grid and the related book note cards were removed: the page was offering twelve options at its foot and reading as junk. At S088 he set the three-block foot above, which Related Further Reading's nine links are part of. **DSRD 2 §1.6 predates this ruling and is corrected to match.**

### 32.2 Container: no exception, 880px like every other content page

**SUPERSEDED BY S113 (folded S358): the page is the article's two-column grid.** Content area 1104, reading column 800, gutter 48, side rail 256, exactly as §22.2 now reads, because this page's reading area is the article's own rules rather than a copy of them. The 880 single column below is the record of what stood between S085 and S113.

**The 1200px exception is retired (Kain, S085).** It was granted at S249 only to give the travelling shelf a second column, and V3 retires the shelf. The page's writing now runs in the single 880px column at §22.2, with no width transitions, exactly as the article page does. §27 holds the ruling and the standard.

The hero stays full bleed with its own inner grid (§32.3). **The breadcrumb bar and the hero grid both sit on the 880px column (`--container-article`, `margin-inline: auto`), the same two declarations the reading column carries (Kain, S102 sitting, theme v0.167.14; his words: "bring the breadcrumbs and all of the heros content into the same width of container that the rest of the page sits in"; his eye after the ship: "the hero looks much better like this").** Measured on the deployed page at 1440: breadcrumb, hero grid and reading column all at x 280, 880 wide; at 1024 all three at x 72. *Until S343 this sentence placed the breadcrumb on the hero block at 1104px, aligned with the logo (Kain, S085 ruling 4; §27), and before S337 at the 1200px frame.* The band and its wash stay full width.

**What this settles beyond this page.** The book note page and the article page are now the same shape: same width, same two supporting blocks, in the same places. The Knowledge Hub reads as one design rather than a family of near-relations, and the quote page and the workbook page inherit that pattern rather than being offered their own version of it.

### 32.3 Hero

**Six values below disagree with the built page, and none is ruled here (S341).** Code read every hero value off the rendered page at 1440px at his S102 (`REPORT__DSRD_9_Section_32_Read_Against_The_Built_Book_Note_Page_S102`): the grid's first column renders 256px not 288; the grid gap 64px not 48; the grid's top padding 32px not 48 (with 48 on the hero itself above the breadcrumb); the hero's bottom padding 48px not 64; the overline 12px not 11; the standfirst and the body 16px not 17. The photograph, the wash character for character, the H1, the cover's ratio, radius and shadow, and the rating in words all match. Which side is right is a visual decision and is taken only by Kain's eye on the real page, so it goes to the book note page's second-look sitting in Safari with Code (the Book note page template: second look card), not onto this paper. The values below stand as written until that sitting, per this section's head note. **Amended S343.** Kain's S102 evening sitting was his eye on the whole hero at three widths, and he approved it as built at v0.167.26, so the page he approved carries the built values on all six (cover 256, gap 64, grid top 32, hero bottom 48, overline 12, standfirst 16). Code framed the sitting as ruling only what Kain raised, so the six are not recorded here as ruled; **the tables below now carry the built values as measured, each marked, and the second-look sitting confirms them on the page rather than re-deciding them from this paper.** Chat's reading at S343, overturnable.

**Corrected S410 (Chat, while writing the page's build sheet):** two values in this subsection were superseded at Kain's S116 sitting with Code (recorded at DSRD 8 section 31) and the S150 approved prototype carries the S116 values: **the hero badge is deleted whole** (the badge appears once, in the last section, section 32.4), together with the standfirst's 42ch cap and the button row's 152 clearance; and **the phone cover is capped at 240 wide, not 320**. The S102 text below is kept as the record; where it describes the hero badge or the 320 cover, the page and the sheet (`BUILD_SHEET__The_Book_Note_Page.md`, Book Note Page folder) govern.

**Four more rulings on this hero, S132 (Kain, in Safari with Code, options rendered as Harness Rule 7 asks). Recorded in full at DSRD 8 §28; named here rather than restated, per standing rule 24.** Desktop: the cover now starts level with the top of the breadcrumb, so the breadcrumb and the words share the left column and the cover owns the right column from the band's top edge (theme 0.659.0), which changes the grid description below. Tablet and phone: the breadcrumb runs on one line, the book sits lower, and the Amazon button sits directly under the cover rather than beside the words (theme 0.660.0). No Know Your Psychology mark on book notes; it stands unchanged on articles and quote pages (theme 0.661.0). The desktop cover stays 256px, confirmed rather than changed. A fault found in the same sitting, not a ruling: the cover's spare height was stretching the breadcrumb's box, so a flexible fourth grid row now takes the surplus (theme 0.661.1). **The property tables below have not yet been re-measured against these five changes; that re-measure is Code's, next time this page is opened in a factory session.**

**And the S115 refinements to this hero (Kain, Code's S115 sitting, theme 0.406.0 to 0.411.0; recorded in full at DSRD 8 §28, folded S382; pointer added S385).** The date line takes the author line's size and weight; the heading is composed from the book and the author's name with the stored title untouched, and the separate author line under it goes; the folded-heading rule is corrected for it and an author's name never breaks across two lines; a heading of three lines or more never ends on a stranded word; the lighter half of the heading begins after the colon; the closing paragraph steps down one size. **Read the "Author line" row in the table below with this in mind:** the separate author line is gone from the hero, the author now sits in the heading.

Full bleed. Background: `images/bookshelf-book-notes.webp`, `background-position: center 22%`, `background-size: cover`. This is Kain's own photograph (its master lives in the Book Note Page folder's `Page Images`), chosen by him at S249 over an invented eight-tone colour palette, on the principle that the page should carry brand imagery rather than colours conjured for it.

One gradient wash over the image, an annotated one-off per DSRD 7 §4.5:

`linear-gradient(100deg, rgba(53,65,73,.93) 0%, rgba(53,65,73,.86) 46%, rgba(53,65,73,.62) 100%)`

The rgb values are brand dark #354149. Corrected in session from two different hand-typed colours that were neither brand dark nor each other; the correction is the reason the value is written out here in full rather than described.

**The fade is the book note's, not the family's (Code, S108; recorded S357).** It lets the shelves show beside the title. The quote page takes the same band with no fade, because it puts content (the quote card and the More Quotes column, DSRD 8 §30) in the bright corner, and photographed, white text sat on pale spines. The article page's band takes its ground from a token with this photograph as the fallback, and uses the article's own picture (§22.4).

**The same image and wash appear again behind the closing panel (§32.6),** deliberately, so the page is topped and tailed with one motif. Kain's design decision.

| Property | Value |
|---|---|
| Container | Breadcrumb bar and hero grid at 880px, `--container-article`, centred (Kain, S102, v0.167.14). The band and its wash stay full bleed |
| Grid columns | Cover, then 1fr. The cover measures 256px on the built page at 768 and up (this paper held `--bn-cover-w` 288px; built value, see the note above). **Two columns hold down to 768** (Kain, S102, v0.167.23: "snap all of the text to sit next to the book image"); at 767 and under the grid is one column, cover above the writing |
| Grid gap | 64px on the built page (this paper held `--sp-2xl` 48px; built value) |
| Grid padding-top | 32px on the built page, with 48 on the hero above the breadcrumb (this paper held 48; built value) |
| Hero padding-bottom | 48px on the built page (this paper held `--sp-3xl` 64px; built value) |
| Breadcrumb padding-top | `--sp-lg` 24px |
| Phone cover, 767px and under | Centred in the column, capped at 320px wide, 2:3 (Kain, S102, v0.167.24 and v0.167.25; supersedes the S086 256 cap). At 390 it measures 320 by 480 at x 35, 15 clear each side. Named by Code, not acted on: the uploaded covers are small (this page's is 316px wide) and have never been through the pipeline's book-cover slot, so they read soft on a retina screen at any size; a cover run for the factory, not a theme edit |

The cover: 2:3 aspect ratio, `--bn-cover-radius` 4px, `--shadow-cover`. Both are named values new at S249 and are defined with the component at DSRD 8.

The stack to its right, in order, each with its margin-bottom:

| Element | Type style (DSRD 7 §3) | Colour | Margin-bottom |
|---|---|---|---|
| Overline `Book note category · {Category}` (wording Kain, S102, v0.167.15) | Como Overline, 600, 0.08em, uppercase; 12px on the built page (this paper held 11) | #F5A05C | `--sp-md` 16px |
| H1, `{Book}: Summary and Key Ideas` (§32.8) | Como **H1 Page Title 33px/700**, line-height 1.15, **and no letter-spacing** (corrected S355) | white | `--sp-sm` 8px |
| Author line, `Book Authored by {author}`, linked; renders only when the record names an author (Kain, S102, v0.167.16) | Mulish 16px/500 (Kain, S086: "the same sized font please"; this paper held Lead Paragraph 19px/500) | white 70%, 1px underline at 3px offset, hover #F5A05C | `--sp-lg` 24px |
| Standfirst: `post_excerpt`, then one space, then the fixed sentence **`Keep reading to decide if this book deserves a spot on your shelf.`** on every note whatever its rating (Kain, S407; built 0.707.133; replaces the S102 sentence "Essential reading for all Achologists.", Kain, v0.167.21) | Mulish Article Body, line-height 1.75; 16px on the built page (this paper held 17); max-width 46ch, **42ch on a badged desktop page** so its last lines clear the badge | white 85%; the fixed sentence in the standfirst's own type and colour | `--sp-xl` 32px |
| Button row: the two buttons, and on tablet and phone the badge as the row's last member (below) | DSRD 7 §5.1, padding 12px 24px, radius 10px, flex gap `--sp-md`; on a badged desktop page the row keeps 152px clear on the right, a second button wrapping onto its own row | see below | none |

**No rating label, no scale words and no ticks anywhere in the hero (Kain, S102, v0.167.17 to v0.167.21).** The words "Achology rating" left the page at v0.167.17 on his spoken word ("lose the words Achology rating on the page"). The per-step sentences ("Highly recommended reading for all Achology members" and its siblings) lived for one ship and were replaced by the single fixed sentence at v0.167.21 on his typed word: "For simplicity, just use Essential reading for all Achologists." He named this as a change on the plan and asked that Chat be told so. The record field, the master column and the importer still carry `achology_rating`; on the page it now decides one thing only, whether the badge appears (§32.9 item 1). **S407 note: the single fixed sentence of v0.167.21 was itself replaced by Kain at S407 with "Keep reading to decide if this book deserves a spot on your shelf." (built 0.707.133); the sentence quoted above is kept as the record of the S102 ruling.**

**The Essential Reading badge (Kain's own design; S102, v0.167.18 to v0.167.26).** A 1080px square transparent PNG Kain designed himself: a hexagonal seal, orange border on brand dark, the Achology mark over "Book Notes", an orange band reading "Essential Reading" with a check, five yellow stars beneath. Its master is in the Book Note Page folder's `Page Images`; it went through the image pipeline at the square slot, 128 and 256 wide, into the theme's `images/knowledge-hub/`. **It renders only where `achology_rating` is `essential-reading`** (eight of the 65 live notes at S102); the other two steps show no badge and no other mark. Alt text is empty on purpose: the standfirst states the fact in words and the badge is its visual seal. The five stars stay on Kain's word (v0.167.19: "keep the badge as it is"), which supersedes the "never as stars" half of §32.9 item 1.

| Tier | Where the badge sits | Size |
|---|---|---|
| Desktop, 1024px and up | Absolutely positioned in the hero grid's bottom right corner, its foot on the grid's foot and its right edge on the container's right edge (v0.167.19). The standfirst caps at 42ch and the button row keeps 152px clear so nothing runs under it | 128px |
| Tablet, 768 to 1023px | The button row's last member, static, pushed to the row's right edge by an auto margin, the Amazon button centred against it: the container's bottom right corner (v0.167.26, superseding v0.167.23's placement beside the button) | 96px |
| Phone, 767px and under | The same placement as tablet, at the right end of the button row under the centred cover (v0.167.24). Where a note has two buttons they wrap and the badge takes the right end of the last row | 88px |

Measured on the deployed page at v0.167.26: at 1440 the badge sits at x 1032 to 1160 with its foot on the cover's foot; at 768 its right edge is 0 from the grid's right edge, its foot 0 from the grid's foot, and the button's centre is on the badge's centre; at 390 the same corner at 88. No horizontal overflow at any width.

**The primary orange button is `Learn About this Author`** and links to the author's own website (`author_website_url`). **The secondary outline button is `Get this book at Amazon`.** Kain's ruling, S249: the author is the prominent call to action in the banner. Both are external and take DSRD 7 §1.0 in full.

**No affiliate disclosure sentence.** Removed at S249: the button label says it. **No page-count or reading-time line.** Removed at S249: no fields exist and no columns are being added for one line.

The author link resolves to `/learn/authors/{author_slug}/`; the button resolves to `author_website_url`. Both are new CSV columns ruled at S249. The slug is never derived from `source_book_author`, because names like "Bessel van der Kolk" and "Viktor E. Frankl" do not sanitise predictably.

**`author_website_url` is withdrawn, ruled by Kain S336, and this leaves the primary button without a destination.** Code found at S090 that the field is read by the template, guards that button, and is held by no column in the master and no field in any book note record. It has therefore never been populated on any live book note. Kain ruled at S336 that it is deleted rather than sourced: filling it is 620 books by hand and again for every book added, and Achology now has 51 author biographies of its own, so an external site is the weaker destination as well as the dearer one.

**Where the primary button points instead is not settled here, deliberately.** The obvious answer, the Achology author hub, duplicates the author-name link a few lines above it in the same hero, and the hero is a rendered page Kain approved at S250. It is a visual decision on his own approved work, so it goes to a Safari sitting on the book note page with the options rendered tabbed (standing rule 16), and nothing in this hero changes until then. **Until it is ruled, the hero stands exactly as built**, which costs nothing, because the button has never had a destination.

**`goodreads_url` is withdrawn in the same ruling and is derived instead** from the ISBN the master already carries, at `https://www.goodreads.com/book/isbn/{isbn}`, so the Goodreads rating stops printing as a claim with no source. The guard becomes the ISBN rather than a stored URL, and a book with no ISBN prints its rating unlinked, exactly as today. Two checks were sent to Code before either change is built: whether that Goodreads route still resolves, tested on three real ISBNs, and how many master rows carry an ISBN at all.

**The page title is one size on every Knowledge Hub page (ruled by Kain, S108; recorded S355).** His question, asked with three page types open in Safari at once: is the article heading the same size font in each type of post? It was not. The quote page and the article page set the title at the 33 step; the book note set it at 42. **Every Knowledge Hub page type sets its H1 at the 33 step**, whatever the page looks like around it: the quote page, the article, the book note, and the workbook page when it is built.

**The tracking goes with the size, and this is the part a document usually misses.** The `-0.01em` belongs to the 42 step, where it stops large capitals drifting apart. At 33 the H1 step carries none. Keeping the tracking would leave this page's title set differently from the other two while appearing to match, which is worse than the original fault because it looks fixed.

**Why the fault existed.** The scale in `base.css` names the 33 step "H1 Page Title" and the 42 step "Hero Heading". They are two different roles. The book note has a page title that happens to sit inside a hero band, and it had taken the band's setting rather than its own. **Nothing in the written record would have surfaced this**: each page's own spec was internally consistent, and only putting them beside each other showed it.

**It is enforced rather than remembered.** `page_gate.py` checks every page's H1 against its `H1_SIZE` constant, so the rule reaches the workbook template before that template is written. Code found at S108 that the constant had read 32 since S056, when Kain's own ruling moved the scale to 32 to 33 and `base.css` was corrected but the gate was not; a real 33 missed a stale 32 by exactly the 1.0 tolerance and passed. **A check that passes the right answer for the wrong reason also passes the wrong answers either side of it.** Corrected to 33.

**One thing this does not settle:** whether the book note's hero should still be a hero at all, now that its title is the same size as an article's. That is a visible design question, so it is Kain's on a rendered page.

### 32.4 Reading zone

One 880px column (`--container-article`), no grid and no second column (Kain, S085, V3). The vertical rhythm, the block margins, and how the Table of Contents and the course card sit against the writing are deliberately not written here. They are Kain's on the rendered page at the spacing sitting with Code, and recording them now would put half a decision on the page as though it were a whole one.

The left column renders `post_content` at DSRD 7's Article Body style: Mulish 17px, line-height 1.75, brand dark #354149. H2s are Como 24px/600 with 32px above and 16px below. A blockquote takes the registered Pull Quote style: Mulish 18px/400 italic, line-height 1.6, 3px brand orange left edge, 20px padding-left. No new type styles were created for this page.

**The badge appears a second time, at the head of the last section (Kain, S102, v0.167.22; his eye: "great").** On an Essential Reading note the same badge is inserted directly after the H2 of heading 5 (§32.7), found by the same `sanitize_title()` id the contents list and the anchors read, and floated right so the section's first lines run round it: 128px square, the writing's 40px gutter on its left, 16px beneath, and a 4px top margin so its top sits on the top of the first line's type rather than its line box (measured: a difference of 0 at 1440 and at 390). On a phone it is 96px with a 24px gutter, leaving the lines beside it at least 230px of the 350 column. `loading="lazy"`, alt empty, for the same reasons as the hero badge. Kain's typed instruction: "place the badge up against the right side of the container in the final section 'What are Your Next Learning Steps?' and just align the top of the badge with the top of the top line of text."

### 32.5 The travelling shelf (RETIRED, Kain S085)

**The shelf is gone.** The narrow column that carried the book cover, the `Get this book at Amazon` button, the `See the related course` button and the contents list down the right of the page is retired with the 1200px container that existed to hold it.

**Its contents are not redistributed by this document.** The contents list becomes the Table of Contents at the top of the writing (§32.1), and it stays hardcoded in the template rather than parsed from the body, which the locked five headings (§32.7) still make possible. Where the buy decision and the course now sit is part of the spacing sitting, not a paper decision taken here.

**Two arrangements were built, seen and passed over**, recorded so they are not proposed again: the cover and Buy button in a box out in the left margin (V4), and the same box inside the writing with the words wrapping around it (V5).

**One consequence outside this document, now closed (S313).** The shelf's own anatomy at DSRD 8 §20, and the three-tier responsive spec at DSRD 8 §20.4 written around it, were orphaned by this ruling. Both are now marked retired and void in that document, kept whole as the decision record so a reader meeting the `.shelfp` class family in an old stylesheet or prototype knows it is dead rather than missing. **One token goes with them:** `--bn-shelf-w` 264px is dead and leaves `base.css` when Code next opens it; the three hero tokens beside it stand.

### 32.6 The closing panel (RETIRED S088; the trial panel that replaced it came off at S113)

**Retired by Kain at S088, on the rendered page**, with the three-block foot standard (§32.1, §22.10a): the page closes on the shared trial panel, DSRD 8 §16's trial variant, whose copy is Kain's (second paragraph ruled S341). **Superseded at S113: the trial panel itself then came off this page, as it came off the article at S112 (Kain, "yes"), so the page now ends on the author signature, the two courses and the footer, as the S113 comment in the built template records (see §32.1 item 7).** The "Next possible steps after this Book Note" panel below was the only block of the four that existed on one page type, and it went for that reason. Its copy is Kain's own words and is preserved here and in `RULING__The_Content_Page_Foot_Is_One_Standard_S088` so it is recoverable. *Corrected S341 on Code's S102 read; this subsection described the panel as live until then.*

*The superseded S249 specification, kept as a record:*

The DSRD 8 §13 "Where next?" panel, used as specified, with one approved change: **its background is the bookshelf image and the §32.3 wash instead of `--color-off-white`,** so its title renders white and its lead white at 78%. The three row cards stay white and untouched, so the component's own contrast is unaffected. Annotate the background in place naming Kain and S249.

The copy is Kain's own words, verbatim, and is not edited:

**Title:** Next possible steps after this Book Note
**Lead:** Three ways to deepen the integration of ideas inside the Knowledge Hub.

| # | Row name | Row description | Destination | Icon (DSRD 7 §5.2) |
|---|---|---|---|---|
| 1 | Browse the Articles that have been inspired by this book | Each article focuses on a core idea from this book and explores it thoroughly. | the book's own article set | `BookOpen` |
| 2 | Explore our interpretation of Quotes taken from this book | We do quotes differently. We reflect on them carefully and discuss them in full. | the book's own quote set | `Quote` |
| 3 | Read the other Book Notes we have written in this category | We might inspire your next book buying decision, or simply inspire you, period. | `/learn/{kh_category}/book-notes/` | `LibraryBig` |

**Row names carry no counts, deliberately:** a hardcoded "five articles" is wrong the day a book has four.

**Rows 1 and 2 resolve to the two per-book listings, ruled S251:** `/learn/{kh_category}/book-notes/{slug}/articles/` and `/learn/{kh_category}/book-notes/{slug}/quotes/`. Both are registered in DSRD 1 §2.4 and both render through the DSRD 2 §1.4 listing template with the filter changed from category to source book. The gap that stood here is closed; nothing invents an address.

### 32.7 The five body headings (LOCKED; SUPERSEDED S115, RECORDED S360; SUPERSEDED AGAIN S150, RECORDED S408)

**The five headings now in force (Kain, S150, live with Code in Safari; agreed with Kain in the sitting ("yes") from his own proposal, with two fixes; recorded by Chat S408 from RULING__The_Rest_Of_The_S150_Sitting item 6).** Every book note carries these five H2s, in these words, in this order. No H3s. No sixth section.

1. What This Book Is Saying
2. The Author’s Background and Perspective (“Authors’” on a book with more than one author; five on the build site)
3. What Could This Book Mean for Society?
4. What You Could Learn From the Book
5. What Might Your Next Learning Steps Be?

**How they stand in the build, at S150 (Code):** the theme carries the new five (live from 0.707.133) with an S150-only fallback that keeps the old list on any page whose body still carries the old headings, so no contents link breaks; the import check (`tools/book_note_import.py`) and the heading tool (`tools/book_note_headings_S314.py`) carry the new five. **The 150 book note bodies are not yet changed.** They wait on a publishing clearance: the S150 run of `publish_gate.py` was measuring 403 pages (the host firewall refused the Chrome 120 identity the tools presented; fixed in commit 0dc5d3b) and was stopped, and Code's S151 stopped it again before it finished. When the clearance runs and the bodies carry the new five, the fallback is removed. Until then the page and the install disagree on purpose, and that is not drift. The book note master records and the `book-note` skill carry the new five from S408.

**The S115 five below, now superseded, kept as the record.** The text from here to the end of this section describes the S115 ruling and everything before it.

The S115 five, in these words, in this order:

1. The Argument at the Heart of the Book
2. The Background the Author Comes From
3. Practical Applications Beyond the Book
4. What this Might Possibly Mean for You
5. What Your Next Learning Step Could Be

**All five superseded at once, Kain, live in Code's S115 sitting in Safari, on the rendered book note page (`RULING__Kains_Five_Book_Note_Headings_S115`).** He judged the earlier five as read out loud: "some of them just read a little bit arrogant ... a little bit presumptuous rather than inviting. I'd like them to read just in a slightly more inviting and broader, yet more compelling frame." He wrote these five himself over four passes, each measured in the rendered contents panel rather than judged on the page alone: they hold to the same working limit as before, about 38 characters at the panel's 256px width (the fourth heading is the longest at 38). **The fourth heading arrived carrying a question mark, the only one of the five to; put to him rendered, he ruled "drop the question mark", so all five read as statements.** This reverses part of S314's own change below, which had added question marks to headings 3 and 4; nothing is inconsistent, it is simply a later ruling on the same two headings. Two readings were put to him and kept on purpose rather than missed: "Might Possibly" in heading 4 is a hedge stated twice, raised three times and kept each time; "Learning Step" in heading 5 carries the assumption the reader is on a course, one of his three original objections, and he put it back deliberately in his final pass.

**The order this supersession runs in is the reverse of S314's, and deliberately.** S314 moved the install and the drafted records together, in one pass. This time nothing changes in the theme, the importer's locked headings list, or `content_gate_standards.json` until every one of the 99 currently published book note records carries the new five in its body, because `content_gate` refuses a record whose body does not hold exactly the locked five in exactly this order; changing the theme or the gate first would fail all 99 at once. The records move first (Cowork, sequenced by Chat, briefed S360), then the five strings in `single-book_note.php` and the gate standard (Code), then a re-import or in-place update of the 99 (Code). Until the records carry the new five, this section's headings and the live install's disagree on purpose, and that is not drift.

**The five superseded by this ruling, kept as the record, exactly as S322 kept heading 5's earlier wordings below.**

| Wording | Ruled | Superseded by |
|---|---|---|
| 1. What this Book is Actually Saying | Kain, S314 | S115 |
| 2. Where the Author is Coming From | Kain, S314 | S115 |
| 3. What Could this Mean for Society? | Kain, S314 | S115 |
| 4. What You Can Take From the Book | Kain, S314 | S115 |
| 5. What are Your Next Learning Steps? | Kain, S088 (the fourth wording that sitting; corrected into this section S322) | S115 |

**Heading 5's own earlier history, kept exactly as S322 recorded it, since it was ruled four times before S115 made it five for five.** It was ruled four times on one day at Code's S088 sitting, and the fourth wording (the row above) was the live one until S115. Kain judges a heading by seeing it on the real rendered page in Safari, never by reading it here, so each wording was built and deployed before it was replaced. That is the method rather than churn. The other four headings are unchanged from S314.

**Where the live wording is read from.** Code's `RULING__Heading_Five_Was_Ruled_A_Fourth_Time_And_Never_Filed_S089` reads it from three places in the build that agree: the importer's locked headings list, the template's section list, and the theme commit of 31 August 2026 carrying it.

**The superseded wordings, kept as the record.** Each was live and built before it was replaced.

| Wording | Ruled | Superseded by |
|---|---|---|
| Where you could take this next | Before S314, sentence case throughout | S314 |
| Where Could Further Exploration Lead You? | Kain, S314 | The S088 sitting |
| What's Left For You to Explore? | Kain, in the S088 sitting | The fourth wording, an hour later in the same sitting |

**One further wording was live inside the S088 sitting and is not written here**, because no file read this turn records its exact words. Code's S089 ruling states heading five was ruled four times that day; three of the four are above and the fourth is the live one.

**Why this section carried the wrong heading between S320 and S322, recorded rather than quietly fixed.** Two Code ruling files in the same channel folder disagreed about which wording was live, the older one was read, and this section was corrected to the third wording while the build already carried the fourth. Nothing in the build was ever wrong. **A ruling file states a value at the moment it was written; where two disagree, the build is read and the later file wins.**

**Changed at S314 on Kain's ruling.** The previous headings used sentence case throughout and heading 5 read "Where you could take this next." Kain moved to title case and rewrote heading 5 deliberately: the open question form leaves the reader with an open loop rather than an instruction, which he wants on every book note. Headings 3 and 4 also gained question marks. The change applies to every book note going forward and to the 51 already drafted, corrected in the same pass Code and Kain use to confirm the book note template in Safari.

**The install and the records move together.** Sixty five book notes are live. One carries the ruled wording; the rest move on Kain's word. The drafted records in the Content Records folder are corrected to the live wording in the same pass, because a rebuild from uncorrected records reverts the install, which is what happened to the biography titles at S306.

**The state of those records, read by Code at S089 and recorded here rather than assumed.** All 108 record files in the book note folder of Content Records carry the original sentence case headings, and not one carries any later wording. So the sweep is the whole set at once, to the wording above, and not a partial correction from S314.

They arrive inside `post_content` from the CSV; the template does not render them. They are locked because the Table of Contents and its anchors depend on them being identical across 598 pages. The list moved out of the retired shelf at S085 (§32.1, §32.5) and the dependency moved with it, unchanged.

**These supersede the internal production names** in DSRD 2 §3.1 and in the `book-note` skill (A Spoiler for the Book, Author's Perspective, Societal Application, Personal Application, Provocative CTA), one for one in order. The skill's own build note named this as an open page-design point; S249 closes it.

### 32.8 Titles and metadata (SEO title and H1 by Kain's S102 pattern; keyword and description by stage 0, Kain S341)

**The Rank Math SEO title takes one pattern: `{Book}: Summary and Key Ideas | Achology`** (Kain, in Code's S102 sitting, 5 September 2026, on four options rendered in text on the same book; his words: "go with number 1 please"; filed as `RULING__Kain_Chooses_The_Book_Note_Title_Pattern_Summary_And_Key_Ideas_S102.md`). The book's name comes first because it is the focus keyword and the title must carry it verbatim. Two mechanical tiers: where the full pattern runs past 60 characters the ending `| Achology` drops (`{Book}: Summary and Key Ideas`, 12 of the 65); where even that passes 60, the shortest tier is `{Book}: Summary`. Where a book carries a long subtitle, the `{Book}` slot carries the keyword's own form of the name, which is what the record's keyword already is. Applied to 62 of the 65 published notes at S102; three (`free-will-sam-harris`, `emotional-leonard-mlodinow`, `nature-emerson`) waited on a keyword decision, taken at S342 (their keywords take the form `{book} by {author}` so a natural title can carry them verbatim; recorded in the keyword register and filed to Code the same session).

**How this sits with the S341 ruling below, corrected the same evening.** S341 retired the fixed S249 formulas for the title, the title tag and the description in favour of each note's own stage 0 demand check. Kain's S102 rulings narrow that twice: the SEO title takes the pattern above, and, ruled later the same evening on three rendered samples in Safari, **the page headline (`post_title`, the H1) takes the same pattern without the `| Achology` ending**, `{Book}: Summary and Key Ideas`, a question-mark title taking no colon, applied by Code to all 65 and read back (`RULING__Kain_Sets_One_Headline_Pattern_For_The_Book_Notes_S102.md`; his words: "yes, the page headline, which is what will show up in search in the knowledge hub, ie, what each article is actually called"). What the stage 0 check still decides is the focus keyword and the description. Recorded this way by Chat at S342 as the reading that lets Kain's rulings stand together; overturnable.

*What S341 ruled, kept in place because it still governs the description and the keyword (its title and H1 clauses are superseded by the two S102 rulings above):*

**Every book note's title, title tag and description are decided by its own stage 0 demand check, never by a formula** (Kain, S341, on Code's S102 read of the built page and his report that none of the 65 published notes replaces an old page). The reason: a title fixed in advance cannot be a question people actually ask, and the site's standing rule is that every title is a proven question (standing rule 14; the rank-math-90 skill's stage 0; DSRD 2 §0.0). The 65 published notes, drafted at S086 before stage 0 existed, carry the bare book title as H1 and `{book title} book summary` as focus keyword on 62 of them; all 65 take a fresh demand check, commissioned to Cowork at S341, and each title and keyword follows what its check finds. What the check must produce is the rank-math-90 skill's, not this section's.

*The superseded S249 formulas, kept as a record because "Understanding" was chosen from thirty candidates and the reasoning may be wanted again:*

**H1 formula:** `Understanding {Book Title}: Key Ideas`. This is `post_title`. "Understanding" was chosen by Kain from thirty candidates because it holds true across all 598 books, claims no credential, passes no verdict on the book, and is short enough to leave the book title loudest. "A Guide to Understanding" was considered and rejected: it is the phrase the study-guide sites own.

**Title tag ladder.** The longest rung that fits 60 characters wins. No brand suffix. Run mechanically at CSV build; no human chooses per book.

1. `{Book Title} by {Author}: Summary, Insights and Key Ideas`
2. `{Book Title} by {Author}: Summary and Key Ideas`
3. `{Book Title}: Summary and Key Ideas`
4. `{Book Title}: Summary`

"Summary" stays on every rung because it is the only word in this field with real search demand. The competitive finding behind the formula (S249): SparkNotes, SuperSummary, Four Minute Books, Growth Summary and Daily Stoic all use book title plus "Summary" or "Key Lessons", and none of them claims a discipline. Search Console cannot inform this: the live property covers only the 192 help URLs.

**Meta description formula:** `A considered reading of {Author}'s {Book Title}: what the book argues, where {Surname} was coming from, and what you can take from it.`

### 32.9 Open items: seven of the nine closed; two reopened at S085

Seven of the nine items listed here at S249 are closed. Two of them, numbers 8 and 9, were closed against the travelling shelf and reopened when Kain retired it at S085. **This section is no longer a complete go-live spec**; see Status at the head of §32.

| # | Item | How it closed |
|---|---|---|
| 1 | Where the two ratings appear | **Superseded S102, written S343.** `achology_rating` now decides one thing on the page: whether Kain's Essential Reading badge renders, in the hero and again at the head of the last section (§32.3, §32.4), on the top step only. The label `Achology rating`, the scale's words per step and the ticks are gone from the page (v0.167.17 to v0.167.21); the five stars are on Kain's own badge by his design and his word (v0.167.19). Every standfirst ends with the one fixed sentence whatever the rating (the S407 sentence "Keep reading to decide if this book deserves a spot on your shelf."; the S102 one is superseded). **Consequence, named so nothing is built on the old assumption:** the scale's three steps are no longer distinguishable on the 57 Recommended and Highly Recommended pages; the record carries them, the page says nothing. Whether the scale is read anywhere else on the site (a hub card, a list, a filter) is a new decision, not made by this ruling. *The S250 wording, kept as the record: renders in the hero as `Achology rating · {value}`, in the editorial scale's own words and never as stars.* `goodreads_rating` rendered in the travelling shelf as `Rated {value} on Goodreads`, an external link; **with the shelf retired at S085, where that line now sits is part of the spacing sitting and is not written here** |
| 2 | The fallback when `book_cover_image` is empty | A template-generated brand dark panel carrying the book title in Como, so the hero never breaks. S250 |
| 3 | The OG image | DSRD 7 §15.1's existing Book Note template is adopted unchanged. S250 |
| 4 | Whether the second course card is tag-generated | Superseded S255. Every course card on the page is filled by the tag rule at DSRD 1 §5.7, and `primary_recommended_course` is retired: it was never populated on any of the 620 master rows and §5.7 postdates it. The note's fifth section names whichever course the rule puts in card one. Closed S250, superseded S255 |
| 5 | The course section's subline | Set verbatim at S250: `Thought-provoking courses that expand on the concepts in this book.` **Superseded S088:** Kain gave one heading and one sentence for both content pages and refused the one edit Code made to it ("please accept the copy i gave you"), so the book note carries the article page's sentence, deliberately (§22.10). Code's S102 read confirms the build carries it |
| 6 | The author bio line | Pulled verbatim from the people registry (`people-setup.php`), never written into a page. The invented line is removed. S250 |
| 7 | What the closing panel does at launch | Dissolved rather than answered at S250, then **void at S088**: the panel is retired (§32.6) |
| 8 | Whether the contents list highlights the section being read | **Reopened S085.** It was built as scrollspy against a shelf pinned beside the text, and the shelf is retired. Whether a Table of Contents at the top of the writing highlights anything at all is part of the spacing sitting |
| 9 | Tablet and phone | **Superseded S085; the hero's tiers ruled S102.** The three-tier spec at DSRD 8 §20.4 was written around the shelf. With one 880px column at every width, the page inherits the article page's own responsive behaviour for the reading zone. The hero's own three tiers were ruled by Kain in Safari at S102 and are written at §32.3: two columns hold to 768, one column with a centred 320 cover under it, and the badge's three states |

**The one dependency that stood outside the nine** is also closed: rows 1 and 2 of the closing panel now have addresses (§32.6, DSRD 1 §2.4, S251).

*Production implementation notes for this page will be in the Production Implementation Notes document once the build runs.*

---

### 32.10 The hero from S162 and S163

The book note takes the Soft Light hero and its page changes in §22.15 and §22.15a (S163: the Drawn Bubble contents, the panel down to the two paths, the two paths foot) whole. Its own differences: the cover (the book component, straight, never tilted) stands on a faint bookshelf fading into the cream; "View on Goodreads" sits in the date line before the word count; below 1200 the Amazon and author-site buttons sit in the side panel's strip under the contents. Where §32.3 says otherwise, §22.15 wins.

## 33. Our People Page Layout (APPROVED AND BUILT, Kain by eye, Code S062 and S076)

The Our People page introduces every person who writes and teaches for Achology: the management team, the guest instructor, the community eldership, and the editorial squad. One page, one instance, live at `/about/instructors/`. It is **not** an Author Hub (DSRD 1 §2.4), which covers the external authors the Knowledge Hub writes *about* and lives at `/learn/authors/{slug}/`. Two different pages doing two different jobs, and DSRD 1 §2.2 carries the distinction in writing because it has been confused before.

Designed live in Safari across Claude Code's S062 and S076 sittings and approved whole by Kain by eye, under the standing rule 16 Safari surface. Every value below was read from the built theme at v0.81.0 and reported by Code at his S076; none of it is invented for this document. Where the built page and this section disagree, the built page is the ruling and this section is the thing to fix.

**This section was written after the page, at S300, and that is recorded rather than smoothed over.** It was owed from S062 and never started, and the board card was marked Done while this half was unwritten. A page approved by eye with no written layout is a page nobody can audit and nobody can rebuild.

---

### 33.1 The job

**This page exists to make a visitor who is weighing Achology up trust the people behind it enough to carry on into the academy or the Knowledge Hub.**

One action, one reader. The action is *carry on* — not *buy*. The page removes the "who actually are these people" doubt; the course, school and article pages do the rest.

**Subordinate job:** to be the destination every Knowledge Hub byline resolves to (DSRD 1 §3, writing author). This adds one requirement — every pen name and instructor whose name appears on the site appears here — but it never reorders the page.

---

### 33.2 The reader's arrival state

No analytics exist for a page that is not yet public, so most lines here are assumptions and are marked as such, per the composition standard. The evidenced lines are read from the site's own link map, not from behaviour.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They arrived from the footer's "Achology People" link or from a byline on a Knowledge Hub piece | Evidenced from the link map: DSRD 1 §13.2 column 1, and the byline rule at DSRD 1 §3 |
| A2 | Where they came from a byline, they want one person, not fourteen | Evidenced — the byline names a person and links here |
| A3 | They are mid-decision about Achology itself, not about a single course | **Assumption.** Confirmed after launch from Search Console and internal referrer data |
| A4 | They expect a corporate team page and are ready to be unimpressed by one | **Assumption** |
| A5 | They do not know the difference between an Achology instructor and an author the Hub writes about | **Assumption**, and the reason DSRD 1 §2.2 carries the distinction |

---

### 33.3 The required state, as changes

Each change is one sentence in the reader's voice. This list is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now know who runs this, and they are named people rather than a brand." |
| C2 | "I now know a recognised authority in this field teaches here." |
| C3 | "I now know there is a body of experienced people around it, not one man." |
| C4 | "I now know who writes the content I have been reading." |
| C5 | "I can read as much or as little of any of them as I want." |

Ordered by dependency: who leads, then who vouches, then who surrounds, then who writes.

---

### 33.4 Page structure (top to bottom)

Four people sections, in this order. **The order is the page's meaning**, and it changed at Code's S076 on Kain's instruction: the eldership moved above the editorial squad.

| # | Block | Heading | Who | Change carried | Treatment |
|---|---|---|---|---|---|
| 1 | Breadcrumb | — | — | orientation | 1200px frame (§27) |
| 2 | Page header | *none* | — | orientation | title, intro, the Read the Founders' Letter button, and the picture; its own phone treatment. Added S384 from Code's S102 pre-sitting report: this row was missing, though the block has been on the built and approved page throughout |
| 3 | Management team | Achology Management Team | Karen A. Ramsay, Kain Ramsay | C1 | rows (§33.6) |
| 4 | Guest instructor | *none, by Kain's S062 ruling* | Prof. Gerard Egan | C2 | grey panel (§33.7) |
| 5 | Community eldership | Achology Community Eldership Team | six elders | C3 | cards (§33.8) |
| 6 | Editorial squad | The Achology Editorial Squad | eight pen names | C4 | cards (§33.8) |
| 7 | Closing trial panel | *carried in the component* | everyone | invitation in | `achology_trial_panel()`, DSRD 8 §16 |

**Block 7 was added at S337, after Code shipped it at his S097 (theme v0.161.0).** This table listed five blocks and named no closing block at all, so the page's own structure section was silent on how it ends. It ends on the trial panel: the same block every article, book note and help answer closes on, in the same `achology_warm_room()` component the enquiries panel used, so the shape, the reading column and the 48px hairline above it are unchanged and only the words, the picture and the button destination differ. Ruled by Kain at Code's S097 on a screenshot of the block, in his words: replace this with the same block we place at the bottom of all articles. **The same applies to the sixteen instructor profile pages**, which took the change in the same act, and §22.10a carries the site-wide list of what the enquiries panel still closes.

**Volume falls as the page descends** (Kain, S062). The people who lead the academy are read, the guest instructor is met, the eldership and the editorial squad are scanned. That is why one page carries three treatments rather than one, and it is C5 expressed structurally rather than written into copy.

**The sections are addressed in CSS by position, not by classes of their own**, because the template builds them from a list and their order is the meaning: `nth-of-type(-n+2)` is the rows, `nth-of-type(2)` is the guest panel, `nth-of-type(n+3)` is the cards. **If a fifth people section is ever specified, that block is what has to be revisited, deliberately.** (Block 7 above is the closing panel, not a people section, and sits outside those selectors.) Recorded here so a later builder does not add a section and find two treatments silently wrong on a page nobody thought they had touched.

---

### 33.5 Width and spacing

**AMENDED S398: the page's content sits in a 960px column, not the 880 (read 800) reading column.** Kain ruled it by eye at Code's S145 (4 October 2026), shown four tabs of the page (800 as it was, 960, 1104 full width, 1104 with the groups three across) and choosing 960, the same column he ruled for Reviews, About and Testimonials at S141 and S142. Built in theme 0.707.63 as a token reset on this page only (`.pp-page { --container-article: 960px }` in `people.css`), so the header, the groups, the closing panel and the guest panel's outward step move together; measured live at 1920, 1440, 1280, 1024, 768 and 390, centred at 960 where the screen allows and narrower below, no overflow. The breadcrumb sits in the same column, per §27 as corrected at S337. *Until S398 this sentence read "the 880px reading column"; until S337 it put the breadcrumb at the 1200px frame.* Header-to-content spacing is §26's site-wide 48px desktop and tablet, 32px below 768px. Neither is restated in values here; both are read from their own sections.

**The seventeen individual Our People pages take the same 960px column (Kain, Code S146, theme 0.707.65).** Kain's words: "Please make all of the 'our people' individual pages the same container width as the main our people page." Done as the same one-line token reset on the individual page template; measured live on all 17 pages at six widths, no sideways scroll. Recorded here at S398 from Code's RULING S146.

**A correction to §27 follows from this and is made rather than left standing.** §27's showcase-pages bullet listed Our People among the card-grid pages using the 1200px frame. The built and approved page uses the reading column, and §27's own sentence test agrees with the build: this page is biographies, and biographies are sentences. The bullet is corrected and the page is unchanged. Named as Claude's call at S300, overturnable by Kain.

---

### 33.6 Treatment 1 — the rows (sections 2 and 3)

| Element | Value |
|---|---|
| Grid | One column, `row-gap: 0` |
| Separator | Drawn **between** rows (`li + li` border-top), never around them, so a rounded hover is not cut by a line at its foot |
| Card | `padding: 24px`, `margin: 0 -24px`, `border-radius: 12px`, hover fill `--color-off-white` |
| Portrait | **128px** circle |
| Name | **24px**, weight 600 |
| Role | **16px**, `--color-orange-link`, `margin-top: 4px` |
| Biography | **16px**, `line-height: 1.7`, `--color-dark`, shown in full, never clamped |

**The role line is one size across both row sections**, ruled by Kain at S062: the guest panel's subline had to match Karen's and Kain's, so theirs grew from 12px and his shrank from 18px, meeting at 16px, which is a step on the approved scale.

---

### 33.7 Treatment 2 — the guest panel (section 3 only)

Sits inside treatment 1 and adds a tint. Built to DSRD 7 §4.4's full-bleed panel rule; nothing here is invented for this page.

| Element | Value |
|---|---|
| Background | `--color-off-white` |
| Corner | `border-radius: 12px` |
| Padding | **32px** |
| Ceiling | At **1040px and above**, `max-width: calc(880px + 2 × 32px)` = **944px** — the reading column plus a 32px bleed each side |
| The row inside | Contributes **no padding of its own**. One set of padding, not two |
| Heading | **None.** With one person in the panel a heading repeats the line beneath it, so his name takes its size instead, at **28px** |
| Hairline | The row's hairline is removed; the panel's own edge is the boundary |

**The caution that has to travel with this panel, because it was got wrong once and Kain caught it on the rendered page:** the panel is centred by the page's auto margins, so widening its ceiling is the whole mechanism. Setting `margin-inline` instead replaces those auto margins and slides the panel 112px left while still measuring the correct width. **Measuring width alone does not catch it. Position has to be checked too.**

---

### 33.8 Treatment 3 — the cards (sections 4 and 5)

Ruled by Kain at S296, in Code's S076 sitting, on a rendered before-and-after comparison.

| Element | Value |
|---|---|
| Grid | **Two columns**, `gap: 24px` (`--grid-gap`), collapsing to one column at **1023px and below** |
| Card | White, `1px solid --color-hairline`, `border-radius: 12px` (`--radius-card`), `--shadow-card`, `padding: 28px 24px 24px`, `height: 100%` |
| Hover | `--shadow-card-hover` and `translateY(-3px)`, both withdrawn under `prefers-reduced-motion` |
| Row arrow | Hidden on cards |

**The card's internal layout:**

```
grid-template-columns: auto minmax(0, 1fr)
column-gap: 16px      row-gap: 2px      align-items: start

  portrait  | name          <- 72px circle, spans rows 1 and 2
            | role
  biography (full width, row 3, margin-top 16px)
```

- Portrait **72px**, `grid-row: 1 / span 2`
- Name **21px**, row 1, `align-self: end`
- Role row 2, `align-self: start`
- Biography spans **both columns**, row 3, **no clamp**
- `.pp-card__text` takes `display: contents`, so its three children become items of the card's own grid. **No markup change, source order untouched, so a screen reader reads it exactly as before**

**Two across, not three.** Three cards in the 880px column give each 277px, which breaks the longer names onto two lines and the roles onto three, and the rows stop lining up. Rendered both ways before choosing.

**Why the card layout changed, recorded because the spec should hold it.** The portrait used to sit *above* the name in a column, which left the biography whatever height remained and clamped it to three lines — so all fourteen cards stopped mid-sentence on an ellipsis. Kain saw it and asked for the name and role to sit level with the top of the portrait, as one design across every card. **It is not a new arrangement:** it is the phone layout he approved at S062, promoted to every width, so the change *deleted* the 767px block that used to hold it rather than adding a second design. The page now has one card shape where it had two and a rule to switch between them. Measured on the rendered page at 1440px, before and after: the biography needed **105px** and was given **63px**; it now gets all 105, and the card is **247px** tall against **287px**. More words in less height.

---

### 33.9 The one stack-point exception this page carries

`.pp-card` wraps at **640px**, which is **approved stack-point exception 4 of 5** under DSRD 7 §4.5 as amended at S252, approved by Kain. Named here so a later audit reads it as a ruling rather than as an arbitrary breakpoint.

---

### 33.10 Tokens

This page introduces no new tokens. 12, 14, 16, 18, 21, 24 and 28px are `--text-*`. Spacing 16 / 24 / 32 / 48 is `--sp-md` / `--sp-lg` / `--sp-xl` / `--sp-2xl`. Card grid gap is `--grid-gap` (24px), card corner `--radius-card` (12px), reading column `--container-article` (880px).

---

### 33.11 Decision register

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Ruled |
|---|---|---|
| 1 | Volume falls as the page descends: three treatments on one page, not one | Kain, S062 |
| 2 | The guest panel carries no section heading; his name takes 28px instead | Kain, S062 |
| 3 | The role line is one size, 16px, across both row sections | Kain, S062 |
| 4 | `.pp-card` wraps at 640px — stack-point exception 4 of 5 | Kain, S252 (DSRD 7 §4.5) |
| 5 | The card's portrait sits level with the name and role; the biography spans the card and is never clamped | Kain, S296, on a rendered before-and-after |
| 6 | Two cards across, not three | Kain, S296, rendered both ways |
| 7 | The eldership section sits above the editorial squad | Kain, Code S076 |
| 8 | The links field is withdrawn: none of the six elders has a link to give | Kain, S296 |
| 9 | The acronym rule does not apply to a role line, anywhere on the site | Kain, Code S076 — filed as `RULING__The_Acronym_Rule_Does_Not_Apply_To_Role_Lines_S076.md`, and written into DSRD 6 §1 at S299 |
| 10 | Benjamin Lockwood's `line` field stays as written | Kain, S299 — raised at Code's S076, closed. Do not reopen from cold |
| 11 | The page and the sixteen profile pages close on the trial panel, not the enquiries panel | Kain, Code S097, on a screenshot of the block. Shipped as theme v0.161.0; written into §33.4 and §22.10a at S337 |
| 12 | Isabella S. Whitmore's and Jackson P. Hartley's role lines both read "Buyer Questions Specialist" | Kain, S337. Both read "TAYA Copywriting Specialist" before. Code raised Isabella's only; Jackson was found carrying the identical line in DSRD 2 §2.14 and ruled the same way in the same turn, because the two write the same thing. **This does not touch decision 9.** The change was made because no visitor knows the phrase behind the letters and spelling it out would not help them either, so it is a plain-language change and not an acronym-rule change. Kain refused the matching change to his own role line and closed it to both sides: his reads "CTO" and stays "CTO", and it is not raised again |
| 13 | The page's column is 960px, a token reset on this page only; the 800 column was too narrow on a wide screen | Kain, Code S145, by eye in Safari on four tabs. Written into §33.5 and §27 at S398 |
| 14 | The seventeen individual Our People pages take the same 960px column | Kain, Code S146 (theme 0.707.65). Written into §33.5 at S398 |
| 15 | Kain rewrote four pieces of the page's copy himself in the Safari sitting: the header paragraph ("Every Achology project is guided by specialists..."), Karen A. Ramsay's paragraph (final form opens "Karen shapes the learning environment's direction, keeping it honest, human, and caring as it grows."), Kain Ramsay's paragraph and Prof. Gerard Egan's paragraph. The theme's people registry is the strings' only home (decision 9 precedent); the exact words stand in Code's `RULING__Kain_Edits_The_Our_People_Words_S146.md`, TO Chat Archive | Kain, Code S146 (header at 0.707.64, paragraphs at 0.707.65). Recorded at the S398 close; DSRD 2 §2.14's bio shape is unchanged |

---

### 33.12 Still open, and the page's remaining definition of done

| # | Open item | Where it goes |
|---|---|---|
| O1 | The DSRD 6 per-chapter record for this page. Approved by eye is not the same as gated | Code, with the record returned through the channel |
| O2 | Whether the person card earns its own DSRD 8 entry. It is used on two sections of one page and has no decision-history entry today; its values live here | `component-library`, next time the library is walked |

**The links field, if it ever returns:** the shape was reasoned through and built before Kain withdrew it. It is recorded in `BRIEF__The_Six_Eldership_Biographies_S296.md` Part Two and is not rebuilt from scratch.

---

### 33.13 The signed record

The page was ruled in Safari, so the signed record is Code's export of the approved page with its build sheet beside it, in the Our People page folder. Per standing rule 24 this section names the folder and stops; the folder's own README says what is inside it. Where that record and this section disagree, the record is correct.

*Production implementation notes for this page live in the Production Implementation Notes document.*

---

## 34. Tag Landing Page Layout (SHAPE RULED S313; LOOK RULED, Kain S390; RECONCILED AGAINST DSRD 2 §1.8 THE SAME SESSION)

One shared template covering the 36 tag landing pages at `/learn/tags/{tag-slug}/` (DSRD 1 §2.4; the 36 slugs are locked at DSRD 1 §5.6). **It had no layout specification anywhere until this session.** The anchor document carried it as a deferred open question and the board card carried it as the one page type with nothing written, deliberately last in the order so the gap held nothing else up.

**One correction to how this section was written, kept at the top because it is the more useful lesson.** It was first drafted without DSRD 2 §1.8 open, and that section had specified this page's contents long before. Four choices here contradicted it. Three were reconciled in the same session, one went to Kain rendered, and §1.8 now carries the supersessions in place. **Content is DSRD 2's and layout is DSRD 9's, and neither is written without the other open.**

| What §1.8 said | What governs now |
|---|---|
| Mixed-type content cards, one set | Four labelled groups. **Kain's S313 ruling supersedes it** |
| Course cards near the top | Course cards at the foot. **Kain's S313 ruling**, on the two positions rendered |
| Filter by content type and by category | No filters. Follows from the grouping: the groups are the filter |
| Pagination, 24 per page | None. Follows from the grouping: four capped groups have nothing to paginate |
| Related tags, 3 to 5 that co-occur | **Unchanged, and it closes an open item this section had wrongly left open** |

### 34.1 The job, and what makes it different from a listing page

**A listing page answers "show me one kind of thing from one subject area." A tag landing page answers "show me everything the site holds on this one idea, wherever it sits."** That difference decides the whole layout. A listing page is filtered to one content type and one category; a tag page is filtered to neither, and cuts across all four content types and all seven categories at once.

So the §21 listing template does not serve it. Two of that page's own blocks have no meaning here: its content-type pill strip links to `/learn/{category}/{content-type}/` addresses that a tag page has no category for, and its H1 names a category and a content type it does not have. **This is a page in its own right, and it reuses §21's parts rather than its shape.**

**One thing it has that no listing page has: it sells.** DSRD 1 §6.1 assigns the Mapped Courses Callout to tag landing pages, and §5.7 gives it up to three course cards, filled from the page's own tag through the tag-to-course mapping, **never chosen by hand**. A tag page therefore recommends the courses that teach the exact thing the reader is reading about, which is the strongest commercial fit of any Knowledge Hub page type.

### 34.2 Page Structure (top to bottom)

**Ruled by Kain, S313, on two whole rendered pages, tabbed, with the grouping as the only variable.** He took the grouped page over the single mixed grid.

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§34.3)
3. Hero: H1, count, intro (§34.4)
4. Sort toggle (§34.5)
5. Hairline
6. **Articles group** (§34.6)
7. **Book Notes group** (§34.6)
8. **Quotes group** (§34.6)
9. **Workbooks group** (§34.6)
10. Hairline
11. **Discover Related Learning Paths, three course cards (§34.7). At the foot, after all four groups: Kain's S313 ruling on the two positions rendered whole, superseding DSRD 2 §1.8's near-the-top placement.** The trade he weighed: near the top every reader sees them, at the foot only readers who reach the end do, and those readers are warmer
12. Hairline
13. Related Topics (§34.8)
14. Rainbow stripe and footer (DSRD 8 §19)

**Why grouped rather than one mixed grid.** The alternative was a single grid, newest first, with content-type pills filtering it in place. Both were built as whole pages on the same tag with the same twelve pieces and put to Kain side by side. **The grouped page won.** The reason it wins is worth recording because it is the same reason the category hub is grouped: a reader arriving on a tag has come for a subject, not for a stream, and four labelled groups let them go straight to the kind of thing they want. A mixed grid makes them scan past three kinds of card to find the fourth, and the count of each kind is invisible until they have scrolled the lot.

**What the ruling costs, named rather than hidden.** A group with nothing in it does not render, so a thinly covered tag shows two groups instead of four and the page is shorter. That is correct behaviour rather than a fault: an empty labelled group advertises an absence. **But a tag close to the 36-tag governance floor could render with a single group of two cards**, which reads as a stub. The governance rule at DSRD 1 §5.1 already guards this from the other end, retiring or merging any tag under ten pieces after six months, so the two rules meet. This is named here so nobody meets a thin tag page and treats it as a layout failure.

### 34.3 Breadcrumb

Reuses the §20.3 breadcrumb component. Trail per DSRD 1 §9: `Home > Learn > Tags > [Tag Name]`. The tag name is the current page, brand dark, not linked. 48px below the header.

**`Tags` is a real link and its destination is the all-tags index page**, which is one of the two index pages still to be specified. **Until that page exists the segment renders as plain text rather than a broken link**, per DSRD 1 §6.4 rule 5: a link is written only where the target exists.

### 34.4 Hero

| Element | Value |
|---|---|
| H1 | The tag name exactly as DSRD 1 §5.6 registers it. Como, the 33 step, 700, brand orange #ED6922, line-height 1.2 |
| Count | The real number of pieces carrying this tag, across all four types and all seven categories. Mulish 14px/400, soft grey #5E6B75, 6px below the H1 |
| Intro | One or two sentences describing what this topic covers and that it is drawn from across the whole Knowledge Hub. Mulish, the 16 step, 400, brand dark, line-height 1.6, max-width 880px, 18px below the count |
| Container | 1200px, the prose inside it at 880px, the pattern DSRD 7 §4.1 already names for the category hub |

**No overline and no category pill strip.** The page belongs to no category, which is the point of it, and an overline reading "Tag" tells a reader nothing the breadcrumb has not already said.

**The intro copy exists and is approved. It is DSRD 2 §1.3.4, the 36 confirmed tag descriptions, approved by Kain at S238.** Sentence case with proper nouns only capitalised, every one written to a 138 to 148 character band so all 36 render at a uniform visual length, 155 the hard ceiling, counts machine-verified before approval. **They already do double duty as each tag page's meta description and the visible line beneath its heading**, which is exactly this field. Nothing is owed and nothing is written fresh.

**Recorded because it cost time this session.** This section first said the copy was owed and its home could not be located. It was in the content document all along, under tag curation, where content copy belongs. **The failure was looking in the wrong document rather than a gap in the project**, and the correction is written here rather than quietly made so the same search is not run again from cold. **A stand-in line was used in the render Kain ruled on, and he was told so at the time**; the shape he ruled does not depend on the words, and the approved line replaces the stand-in at build.

### 34.5 Sort Toggle

The §21.4 control bar's right-hand group only: two pills, `Newest` and `A to Z`, right-aligned. Same values as §21.4 in every respect, including the S313 colour correction to the inactive pill.

**The content-type pills are not on this page.** They were on the option Kain did not take, where they filtered a mixed grid. With the content grouped, the groups themselves are the filter and a second set of controls doing the same job is clutter.

### 34.6 The Four Content Groups

Each group is a §20.7 section header followed by a card grid. **The section header component is used exactly as the category hub uses it**, with its own hairline beneath the title, its live count in parentheses, its supporting line, and its `View all` control on the right.

| Property | Value |
|---|---|
| Order | Articles, Book Notes, Quotes, Workbooks. Fixed, every tag page, never re-ordered by volume |
| Icon | Per content type, from the §20.7 register: `newspaper`, `notebook-pen`, `quote`, `file-pen` |
| Title | The content type name, with the live count for this tag in parentheses |
| Supporting line | One line per type, 12 to 25 words per DSRD 7 §3.3 |
| Cards | The standard card per type: DSRD 8 §6.1, §6.2, §6.3, §6.4. **No featured cards**, which are the category hub's alone (§21.6 holds the same rule) |
| Grid | 3 desktop, 2 tablet, 1 phone, 24px gap, per DSRD 7 §4.1 |
| Items shown | The most recent per type, with the rest reached through `View all` |
| Empty group | Does not render. No header, no empty state, nothing |
| Boundary between groups | 48px, no hairline, on the same ground as the category hub's exception (DSRD 7 §4.3, exception 3): each group already opens with the section header's own rule |

**Where `View all` goes is an open question, named rather than guessed.** A content type filtered to a tag has no address today: the site has `/learn/{category}/{content-type}/` and `/learn/{content-type}/`, and neither carries a tag filter. Either the control links to the cross-category listing for that type, which loses the tag and is therefore a worse answer than it looks, or a new address is needed. **Not decided here.** Until it is, the control does not render, per the same rule the breadcrumb follows.

**How many items each group shows is open too.** The category hub shows five per section, one featured and four standard, but that page has featured cards and this one does not. **It is a decision on the rendered page with real content, not a number chosen on paper**, and it is Kain's at the same sitting that settles the spacing.

### 34.7 Discover Related Learning Paths

Section header plus **up to three course cards**, DSRD 8 §7.

**The courses are never chosen by hand.** DSRD 1 §5.7: this page's own tag is its lead tag, and the slots fill from that tag's mapped course list in the order §§5.2, 5.3 and 5.5 write it. Where the tag maps fewer than three courses, the page shows fewer; it does not top up from another tag, because on this page type there is no second tag to top up from.

**Three slots here, against two on an article page**, and the difference is deliberate: this page runs in the 1200px frame rather than an 880px reading column, so three course cards sit at the same width the course card was approved at rather than being squeezed.

**Content attribute tags map to no courses** (DSRD 1 §5.1, §5.4). On those five tag pages, this whole block does not render. Named because five of the thirty six pages behave differently and a builder meeting the first one should know it is correct.

### 34.8 Related Topics

Section header plus a wrapping row of tag pills, the §20.8 pill treatment exactly. Links to other tag landing pages.

**Which tags appear is settled, and this section was wrong to call it open.** DSRD 2 §1.8 component 9 already specifies it: **three to five tags that most often co-occur with this one**, a derivation applied by machine, never a hand-picked list per page. Found on the S313 reconciliation.

### 34.9 Pagination

**None on this page, and it follows from the grouping rather than being its own decision.** DSRD 7 §17.1 lists tag landing pages among the pages it governs, and DSRD 2 §1.8 component 8 specified 24 per page; both were written when this page was assumed to be one flat listing. **With four capped groups there is nothing to paginate**, and depth is reached through each group's own `View all`, once that control has an address. DSRD 7 §17.1 is owed the correction; DSRD 2 §1.8 took it at S313.

### 34.10 What is settled and what is open

**Settled by Kain at S313:** the page is grouped by content type rather than a single mixed grid, the three course cards sit at the foot rather than near the top, and the block order at §34.2 follows from both.

**Settled by reconciliation against DSRD 2 §1.8 the same session, no ruling needed:** no content or category filters, no pagination, and Related Topics derived from co-occurrence.

**Open, each one named rather than filled in:**

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | ~~The 36 tag description lines for the hero intro~~ | **CLOSED S313.** They exist and are approved: DSRD 2 §1.3.4, ruled by Kain at S238. See §34.4 |
| 2 | How many items each group shows | Kain's eye, on the rendered page with real content |
| 3 | ~~Where each group's `View all` links to~~ | **CLOSED S390, decided by Chat as a structural call.** No `View all` control renders on a tag page, because no tag-filtered address exists and linking to the cross-category listing would drop the tag. Each group instead shows up to six cards (two rows of three), so a reader can see more without leaving the topic. The control returns only if a tag-filtered listing address is ever built. Six is a starting value; Kain confirms it by eye at the spacing sitting (item 2) |
| 4 | ~~Which tags fill Related Topics~~ | **CLOSED S313.** DSRD 2 §1.8 component 9: three to five by co-occurrence |
| 5 | The vertical rhythm and every internal spacing value | Kain's at the spacing sitting on the rendered page, the same way the book note page's are held open at §32 |
| 6 | Phone and tablet behaviour | Follows the §21.9 pattern, confirmed on a render, not written here |

**Three things stand between this specification and a built page: items 2, 3 and 5**, and two of the three close at one rendered sitting with Kain.

*The render Kain ruled on is the tabbed two-option file produced at S313; its card copy was written for the render and is not real content, which he was told before he ruled. The ruling is about the page's shape, which does not depend on the words.*

---

## 35. All Tags Index Page Layout (SHAPE RULED S313; LOOK RULED, Kain S390)

One page at `/learn/tags/` (DSRD 1 §2.4, address added S313). **It had no address and no layout until this session.**

### 35.1 Why the page exists

**Two reasons, and the first is structural rather than editorial.** Every tag landing page's breadcrumb reads `Home > Learn > Tags > [Tag Name]` (DSRD 1 §9), and until S313 the `Tags` segment pointed at nothing, because no page lived there. A breadcrumb segment with no destination is either a dead link or a lie about the site's shape. This page is what closes it.

**The second is the reader.** Thirty six topics are the site's cross-cutting discovery layer (DSRD 1 §5), and a reader could only ever reach one by being handed it from a piece they were already reading. There was no way to see what the site covers and choose.

**One page, not two.** This section replaced a two-page plan. **The all-authors index was killed by Kain at S313**, because there is no author page type to index: he ruled at S306 that biographies publish as ordinary articles and no author hub exists or will. It had survived on the board from before that ruling. DSRD 1's breadcrumb table, indexing register and sitemap list were all struck of author hub rows in the same pass.

### 35.2 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb: `Home > Learn > Tags`, the §20.3 component
3. Hero: H1, count, intro (§35.3)
4. Hairline
5. **Outcomes**, 16 topic cards (§35.4)
6. **Problems**, 9 topic cards
7. **Approaches**, 6 topic cards
8. **Kinds of Reading**, 5 topic cards
9. Rainbow stripe and footer (DSRD 8 §19)

**The four families are DSRD 1 §§5.2 to 5.5, renamed for readers and not in the taxonomy.** Outcome tags become **Outcomes**, problem tags **Problems**, modality tags **Approaches**, content attribute tags **Kinds of Reading**. The taxonomy's own names are internal; a reader meeting "modality tags" as a heading learns nothing. **The internal names do not change and this is a display rule only.**

**Boundaries between families carry no hairline**, 48px of white, on the same ground as the category hub's exception (DSRD 7 §4.3, exception 3): each family opens with a section header carrying its own rule.

### 35.3 Hero

| Element | Value |
|---|---|
| H1 | `Browse by Topic`. Como, the 33 step, 700, brand orange |
| Count | The live number of registered tags. Mulish 14px/400, soft grey, 6px below |
| Intro | Two or three sentences naming the four families and what each one is for. Mulish, the 16 step, 400, brand dark, max-width 880px, 18px below |
| Container | 1200px frame, 880px prose inside it |

### 35.4 The Topic Card (ruled by Kain, S313, on two whole rendered pages, tabbed, with the card against a plain list as the only variable)

**He took the cards.** Each topic is a card carrying its name, one sentence saying what the topic is about, its live piece count, and a control into its tag landing page.

| Property | Value |
|---|---|
| Grid | 3 desktop, 2 tablet, 1 phone, 24px gap, per DSRD 7 §4.1 |
| Title | The tag name exactly as DSRD 1 §5.6 registers it. Como, the 16 step, 600, brand dark |
| Description | One sentence. Mulish 14px/400, soft grey, line-height 1.5 |
| Count and control | Separated by a hairline inside the card. The count in Mulish 13px soft grey on the left, the control in brand orange on the right |
| Link | The whole card links to `/learn/tags/{slug}/` |
| Shell | The §6.0 card family shell: 12px radius, hairline border, `--shadow-card` |

**What the ruling costs, named rather than hidden.** The list showed all 36 topics in about one screen. **The cards take roughly four.** Kain chose the longer page knowingly, on both rendered in front of him, and the reason the cards win is that this page's job is to help someone who does not yet know what they want. A name alone serves the reader who already knows; a name plus a sentence serves the reader who does not, and that is who arrives here.

**It also creates a real dependency, and this is the important consequence.** The card is only worth its extra length if the sentence on it is good. **Thirty six description lines are now load-bearing on this page**, where on the list they were optional.

**That copy exists and is approved: DSRD 2 §1.3.4, the 36 confirmed tag descriptions, ruled by Kain at S238.** It is the same copy §34.4 uses on the tag landing page's own hero, so the two pages share one piece of writing rather than two, and a change to a description changes both pages at once.

**One thing to check on the render rather than assume.** Those lines were written to a 138 to 148 character band, for a meta description and a full-width line beneath a heading. **On a card at a third of the frame that is roughly four lines of text**, which may be more than a browsing card wants to carry. Whether the card shows the description whole, clamps it, or takes a shorter form written for this one slot is Kain's on the rendered page. **Nothing is shortened on paper**: the approved copy is used as it stands until he says otherwise.

**A card is not built without its sentence.** The approved copy exists, so this is a guard rather than a live risk: where a description is ever missing, the topic still renders, with its name, its count and its control, and no placeholder text. A card carrying invented copy is worse than a card carrying none.

### 35.5 What is settled and what is open

**Settled by Kain at S313:** the page exists, it lives at `/learn/tags/`, it groups the topics into four reader-facing families, and each topic is a card rather than a line.

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | ~~The 36 description sentences~~ | **CLOSED S313.** DSRD 2 §1.3.4, approved by Kain at S238. See §35.4 |
| 2 | Whether the card carries the full approved line, clamps it, or takes a shorter form | Kain's, on the rendered card. The approved line is used whole until he rules otherwise |
| 3 | ~~The four family names as reader-facing headings~~ | **CLOSED S390, decided by Chat.** Outcomes, Problems, Approaches, Kinds of Reading. Kain sees them in place on the rendered page and can change any of them then; they were not put to him as words on their own |
| 4 | ~~Each family's supporting line~~ | **CLOSED S390, decided by Chat, 12 to 25 words each per DSRD 7 §3.3.** Kain sees them in place on the rendered page and can change any then. Outcomes (17): "The changes people come to psychology for, and the ideas and skills that help them get there." Problems (16): "Everyday difficulties people bring to psychology, and the ideas and skills that help with each one." Approaches (18): "The methods and schools of thought behind applied psychology, explained so you can see how each one works." Kinds of Reading (19): "The kinds of reading the library offers, whatever the subject, so you can choose how you want to learn." Worded without naming individual tags; not yet checked against DSRD 1 §5.6 |
| 5 | ~~Whether the families are ordered as above or by size~~ | **CLOSED S390, decided by Chat.** Meaning-first order stands (Outcomes, Problems, Approaches, Kinds of Reading). Size order would move with every new tag; this one never does |
| 6 | Vertical rhythm and internal spacing | Kain's at the spacing sitting on the rendered page |
| 7 | Phone and tablet behaviour | Follows the §21.9 pattern, confirmed on a render |

**Not a complete go-live specification.** The shape is ruled and the copy exists; the finish is not settled. Every remaining item closes at one rendered sitting with Kain.

**LOOK RULED, Kain S390 ("yes"), on both pages rendered whole at 1280, 834 and 390 in Chat's side panel.** The topic card is registered new in its build sheet and goes to DSRD 8 on Code's build. Piece counts, quotations and workbook cards in the render were stand-ins and were named as such. The count under each topic card is Mulish 12 where section 35.4's table said 13, to sit on the nine step scale (DSRD 7 section 3.0). Still open: the four family icons (not registered), and the spacing sitting.

*The counts in the render Kain ruled on were invented and he was told so before he ruled; the real counts come from the database at build time.*

---

## 36. Pricing Page Layout (APPROVED, BUILT AND PUBLISHED: Kain with Code in Safari, S121 to S128; recorded S380)

**Where the page's truth lives now.** Kain built this page block by block with Code in Safari across eight theme sessions (S121 to S128), starting from his own design package, and published it at S127 (page 36845, `/pricing/`). Per standing rule 19 and the S257 precedence, **the approved prototype in the Pricing Page folder is the signed record**, exported by Code after every ruling; this section is the decision history only. Sections 36.1 to 36.3 below still stand (the job, the arrival state, the changes). Sections 36.4 to 36.6 are the S365 derivation, kept as history and superseded by 36.7 onward. Prices, savings, names and checkout addresses are read from DSRD 4 and DSRD 5 at build, never from the package and never from here (Kain, S365).

**History of the S365 derivation.** Kain supplied a full prototype and handover pack for this page, in the Pricing Page folder, and ruled that it replaces the block order below. Two things below still stand because the package agrees with them: the Courses list is a short price list, not 28 full cards, and every price and checkout link is copied from DSRD 4.

One page, one instance, at `/pricing/` (PRD Pr1.19). Composed at S365 through `page-composition`, against the Document-Level Standards above. **Structure only.** Kain ruled at S257 that the page's look waits until the bundle, Access All Areas and membership cards are signed in their Safari sitting with Code, because the page is mostly those cards; this section fixes what the page carries and in what order, which does not change when the cards' look does. Prices, savings and checkout URLs are read from DSRD 4 section 1 at build, never from here. The page's design folder is the Pricing Page folder under Homepage + Commercial Design Prototypes.

### 36.1 The job

**This page exists to get a visitor who is weighing Achology up to choose the way of buying that fits them, and go to its checkout or its own page.** The four ways are one course, one school bundle, everything (the Access All Areas Pass), and membership; the free membership tier (DSRD 4 section 1.6's Free Membership) is the way in for anyone not ready to pay.

### 36.2 The reader's arrival state

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They broadly know what Achology is and are now asking what it costs | **Assumption.** They arrive from the header, a course page's Three Ways To Buy block, or a help answer that routes cost questions here (DSRD 2 section 2.24 item 7). Confirmed after launch from analytics |
| A2 | They are comparing ways to pay more than comparing courses | **Assumption,** grounded in the page's own job; the course comparison is the courses directory's job (DSRD 2 section 2.3) |
| A3 | Price, refunds and "is there a cheaper way in" are live worries | Evidenced: price and refund are two of the seven spine questions on every course page (DSRD 2 section 3.8) |
| A4 | Many read on a phone | **Assumption.** Confirmed after launch |

### 36.3 The changes, in the reader's voice

1. "I can see the four ways to buy, and roughly what each costs and includes."
2. "I believe these prices are for something many people value."
3. "I can find the price of the exact course or school I'm thinking about, and act on it."
4. "I know what membership gives me and what it costs after the $7 month."
5. "I see Access All Areas as the best value if I am serious, and the fastest route to Master Achologist" (DSRD 4 section 9.2).
6. "I know I can start free before I pay anything" (required wherever the $7 trial appears, DSRD 4 section 11).
7. "I no longer worry about losing my money or being locked in."
8. "I know whether I can pay in instalments."
9. "I know buying a course does not by itself make me accredited" (the honesty-against-interest pairing; PRD criterion 8).
10. "My remaining questions about upgrading, the $7 trial and cancelling are answered."

### 36.4 Page Structure (top to bottom; this is also the mobile order)

| # | Block | Change carried | Component |
|---|---|---|---|
| 1 | **Page heading** with the Trust Line beneath it | 2 | Trust Line, DSRD 4 section 14.2 variant 3, figures from the figure register |
| 2 | **Four ways in, side by side:** one course, one school, everything, membership; each a one-line statement of what it includes (courses, and months of community) and a "from" price, each linking down to its block below. Under the four, one line: not ready to pay, start free, to the free membership signup | 1, 6 | **New block, to be designed** |
| 3 | **Price lists, two tabs:** Courses, then School bundles. The Courses tab is a **short price list** (ruled by Kain, S365): each of the 28 courses as one row carrying its name, its price and the two actions (Learn More to the course page, Enrol Now to its Circle checkout), grouped under the three learning routes (DSRD 4 section 2, a partition of 28). The School bundles tab carries the seven bundle cards | 3 | Courses tab: **new component, the course price row, to be designed and signed.** Bundles tab: bundle card, DSRD 8 section 8 |
| 4 | **Product section block:** Monthly, Annual, Access All Areas, in that order, under its heading. The Monthly card sits with the start-free line beside it | 4, 5, 6 | Product section block, DSRD 8 section 11 |
| 5 | **Questions, opening in place:** can I upgrade; what happens after the $7 trial; can I cancel; what if it is not right for me (the course guarantee, the Access All Areas guarantee, and no refunds on subscriptions, stated plainly); can I pay in instalments; does buying a course make me accredited (one line, linking to the certification page) | 7, 8, 9, 10 | Question list pattern as used on the course page (DSRD 2 section 2.6 block 9) |

**The action repeats without a new change:** each product carries its own buy button where the reader meets it. No other exit is offered.

### 36.5 The two closing tests

**Every block carries a named change:** yes, all five. **Every change has a block:** yes, all ten.

**Removed against DSRD 2 section 2.8's earlier list:** the separate "What's included at each tier" block. Its change is carried by block 2 and by each card's own contents, so a separate block would say it a third time.

### 36.6 What is settled and what is open

**Settled by Kain at S365:** the Courses tab is a short price list, not the 28 full course cards, because on a phone 28 cards put the membership and Access All Areas cards far down the page, and the full cards already live on the courses directory. This supersedes DSRD 4 section 3.1's Tab 1 wording.

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | The look of the whole page, blocks 2 and 3 included | Kain's, by eye, after the bundle, Access All Areas and membership cards are signed (S257) |
| 2 | Whether the Courses tab keeps DSRD 4's school and topic filter now it is a short list | Kain's, on the rendered list |
| 3 | The instalment answer's wording | Waits on Code confirming the real Circle and Stripe terms (the same fact DSRD 2 section 2.6 block 8 waits on) |
| 4 | The Access All Areas guarantee's terms | DSRD 4 section 1.3 says 100% money back but names no window; confirmed before the answer is written |
| 5 | All copy | Written with Kain, per standing rule 19 |

**Not excluded by oversight:** the $399 DiMAP Course Upgrade (DSRD 4 section 1.1b) is not on this page; it is not among the products PRD criterion 3 requires the site to sell.

### 36.7 The page as built and ruled (top to bottom; the mobile order)

Read from Code's S121 to S128 session reports and the ruling files they name. Kain's own verdict governs the register: "this is just a pricing page. It's not a sales page" (S128).

| # | Block | Change carried (36.3) | Ruled |
|---|---|---|---|
| 1 | **The top panel:** the opening band with Kain's price-tag artwork, his own heading copy and three statement segments; the Chooser, four choice cards in his own words (one course, one school, everything, membership), each with its own colour on the price; his three guarantee statements, each linked to the help answer that proves it | 1, 7 | S121, S122 |
| 2 | **The course index:** nine course rows showing on load and a View All 28 Courses control that opens the rest (confirmed by Kain, S381, as the page he wants; the filed S123 ruling's "all 28, no expand control" is superseded), each row showing its full price and what it costs a month on one line; three category tabs in Kain's labels; an All Payment Options menu (replacing the budget filter and the 84-figure price grid); no search box | 3, 8 | S123, S124, S126 |
| 3 | **The schools grid:** seven artwork cards, courses on the face of each card as ruled hairline rows, the struck price as a faint diagonal, the same payment options menu, and the **Access All Areas Pass as the eighth card** (the seven schools listed with a bar in each school's colour, Kain's own drawing and three lines); all eight open on the reader's choice | 3, 5, 8 | S124, S125, S126, S128 |
| 4 | **The membership block**, arranged Under: Kain's heading and line, two actions, his inclusion lines (four removed at S128 as selling copy), and the free tier strip | 4, 6 | S126, S128 |
| 5 | **Questions:** the help article's own closing card, listing six real answers from the two price categories of the help section, in place of written answers on the page | 7, 8, 9, 10 | S126 |
| 6 | **The ending:** four doors, as the top panel's own cards, each pointing out to its product's page | the action | S126 |

### 36.8 The rulings, where each is recorded

Every ruling is filed as its own RULING file in the channel Archive, and folded by Code into the prototype. **S121:** the opening band; Kain's heading copy; one text line (site-wide, now DSRD 7 section 4.4a); four options minimum (The Harness). **S122:** the Chooser as the layout; his copy for the four choice cards; the cards' colour and design; the card line type with two copy changes; the opening band's artwork to the words' height; nine rulings on the top and the search bar. **S123:** the course index and the monthly figures; eleven rulings on the course block (including DSRD 7 section 5.5's form control type); the S121 separator width reversed (DSRD 7 section 4.4a). **S124:** the artwork card for the seven schools; ruled rows inside the card; his words for the school bundles heading; the card head and course list tightened; the banner audited and its gap closed; Payment Options replacing the budget box and price grid; the school cards taking the payment options menu. **S125:** the pass as the eighth card; the struck price as a faint diagonal; one footer on the school card with the seal; the footer as one set of three; the membership as a marked row on every school bundle; the plan menu renamed Pricing Options; quiet, with the plan control in his sentence; his replacement line for the schools block. **S126:** Ribbon for the pass drawing and Lift for the block of eight; the membership block Under; the questions block replaced; the four doors ending; the page approved as good enough to build. **S127:** eighteen rulings in one file; money for the saving and one width for its two lines; grouped for the page's rhythm; quiet for the peak and the pass button renamed; the page confirmed as drawing right as a real page. **S128:** the AA-safe control orange (`--color-orange-action` #C85015) on the last three controls and every primary button site-wide; the school cards open on the reader's choice; four membership lines removed.

### 36.9 What is open on this page

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | The DSRD 6 record: §2, §3 and §5 failed and §1, §6, §7's hand half, §8 to §11 not run at S128 | Code runs them once the search values Chat sent at S380 are typed in; Chat runs the reading chapters |
| 2 | The four pages it links to do not exist: `/courses/`, `/academy/schools/`, `/access-all-areas/`, `/membership/` | Their own cards |
| 3 | The Circle and Stripe confirmations: currency and tax, included membership renewal, refund terms per product, instalment terms and rounding | Code, from the live checkout |
| 4 | Whether the free Circle tier carries a schema offer, and its name | **Closed S381 (Chat):** yes, an Offer named "Free Membership" at 0.00, DSRD 4 section 1.6's product name |
| 5 | Whether the page prints a visible breadcrumb, and DSRD 1 section 9's rows for the top-level commercial pages | Kain, by eye on the rendered page, tabbed, in his next Safari sitting with Code (asked S381) |
| 6 | Kain's line under the closing block | **Closed S127 (found S381):** Kain sent his own heading and line at S127 ("Our Curriculum is Designed to Help You Understand - You!"), built as typed; recorded in `pricing-parts.php` at the block |
| 7 | The course index | **Closed S381:** Kain confirmed the live page (nine rows and View All 28 Courses) is what he wants; row 2 of section 36.7 corrected |
| 8 | The membership card's inclusion list and this page's list differ | **Closed S381:** on purpose. Kain, S128: "this is just a pricing page. It's not a sales page." The page carries four lines, the cards the full list |

---

## 37. Workbook Page Layout (STRUCTURE WRITTEN S366; BAND AND CAPTURE RULED, Kain in Code's S152 sitting; CONTENT REBUILT, Kain with Chat, S411)

**S411 reconciliation, read first.** Kain rebuilt the page's content with Chat at S411, under `page-composition`, in DSRD 2 section 1.7, which now owns the job, the arrival state, the five changes, every section's standard and the approved Ladder of Inference words. Code's S152 sitting ruled the band, the three buttons, the side panel and the email card (DSRD 8 section 39). Where 37.1 to 37.5 below differ from those two, they are superseded and kept as the S366 record. The page order is now:

1. Sticky header (DSRD 8 section 18).
2. **Hero (band):** breadcrumb; H1 to DSRD 2 section 1.7's title standard; subtitle to its subtitle standard (two lines at most); the date line; the "Get Your Free Workbook" button; the workbook cover on the right inside the container.
3. **What Is [the idea]?**
4. **How This Workbook Helps You Learn**, with two or three inside pages of the workbook shown as pictures.
5. **What [the idea] Is Used For.**
6. **Where This Workbook Comes From**, with the course image left-aligned to the container, its top level with the first line of the second paragraph (Kain, S411).
7. **The email card** (DSRD 8 section 39 item 4): email only, the workbook emailed, never downloaded.
8. **Side panel:** the contents pinned at the top; the cover and the unframed email box at the foot (DSRD 8 section 39 item 3).
9. **"Browse More Achology Workbooks"** (Kain, S411), in place of the related workbooks shelf and of S152's "Browse More Achology Articles"; placeholders until more workbooks exist.
10. Two course cards (section 22.10), as every content page.
11. Rainbow stripe and footer (DSRD 8 section 19).

No Related Further Reading and no Know Your Psychology mark (S152). **After the form:** the reader lands on the thank-you page, one page for every workbook that knows which was requested (DSRD 2 section 1.7). Its layout is ruled in the S159 sitting (Kain with Code): one column at 960, a cream hero with three steps, a bridge of blocks before the two paths, the two paths as one split panel with identical cards, and the About page's gateway block at the foot. The full ruling and the order of blocks are in DSRD 2 section 1.7 (the thank-you page, S159).

**Open:** the email card's words and the consent box (Kain with Code, Chat's recommendation in DSRD 2 section 1.7); how the inside pages are shown; the Kit wiring and its cookie question (DSRD 3 section 6.5, settled by the S381 plain form).

**The S366 record follows.**

**Added S401 (Kain's site standard, Code's S147):** the workbook page carries the reading progress line every content page carries (§32, item 5), and the reading column's width and body text size are the same as every other content type (§32, item 6).

One template serves every workbook landing page, at `/learn/{category}/workbooks/{slug}/` (DSRD 1; PRD Pr1.4). Written S366 from DSRD 2 §1.7 (the components) and §3.4.2 (the body), onto the content page standard the article and book note now share (§22, §32, Kain S112 and S113). **Structure only.** Kain rules the look on Code's rendered page in Safari (his S366 instruction for new page work), with any choice shown as options, tabbed. First real content: the Karpman Drama Triangle workbook record (Cowork, S347).

### 37.1 The job

Hand the reader one free workbook for practising an idea they already half know, in exchange for their email, and show them where to learn it properly.

### 37.2 The reader's arrival state

Arrives from search on a "free" plus topic phrase, or from the companion article. Knows the idea by name, wants to do something with it, is wary of handing over an email for nothing.

### 37.3 The changes, in the reader's voice

1. "This is the exercise I was looking for, and it is free." (hero, cover)
2. "I can see what I would actually be doing." (body, What's inside)
3. "Giving my email is worth it." (the capture block)
4. "If I want the full idea, I know where it is." (companion line, source book, courses)

### 37.4 Page structure (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18)
2. **Hero**, the content page hero (§22, as the article): breadcrumb, H1 (the workbook page's own title, carrying "free", DSRD 2 §1.7), category and tag pills. **The workbook cover sits in the hero** where the book note carries its jacket.
3. **Reading zone**, the article's own (§22 fourth round: 1104 grid, 800 column, 256 side rail). The body is DSRD 2 §3.4.2's five parts, in order.
4. **What's inside**, the list of the workbook's sections (DSRD 2 §1.7 item 7), placed straight after the body's second part, "What the exercise asks of you".
5. **The capture block**, directly after the body's capture line (§3.4.2 part 4): Kit form, email field and one button, released download on submit (DSRD 3 §3.1, placed by shortcode, never auto-inserted). **It also sits in the side rail**, under the cover that follows the reader (the §32 row 9 mechanism), so the form is in reach at every scroll point. One form, two placements. Design is Kain's on the render.
6. **Source book callout**, only when the workbook comes from a named book (§1.7 item 9), one line with the book note link.
7. **Side rail shelf:** 2 to 3 related workbooks from the same category or tags (§1.7 item 10), in the rail's shelf position, replacing Related Further Reading on this page type.
8. Share row at the foot, the article's position.
9. **Two course cards**, the words at §22.10 ("Ready to Take Your Learning Further?" since Code's S147), filled by the tag rule (DSRD 1 §5.7), as every content page.
10. Rainbow stripe and footer (DSRD 8 §19).

**No author block.** The body is the base voice with no pen name (DSRD 2 §3.4.2). **No trial panel**, matching the article and book note after S113.

### 37.5 What is settled and what is open

**Settled by this section:** the block order above, which follows DSRD 2 §1.7 and the S113 content page standard. It supersedes §1.7's own foot (its "Explore Related Learning Paths" is the two course cards; its schema line belongs to DSRD 3).

**Open, all for Kain on the rendered page:** the hero with a workbook cover in it; the capture block's look in the body and in the rail; the related workbooks shelf. **Open before the first form goes live, not before the render:** whether Kit's script waits for cookie consent (DSRD 3 §6.5); it is decided when Code wires the live form.

---

### 37.6 The hero from S162 (Kain with Code, theme session S162)

The workbook is part of the Soft Light family (§22.15): warm cream band, its cover standing straight on a faint bookshelf fading into the cream, and the email box (white field, burnt-orange button) and privacy line in the hero. **Its banner has no date line for now** (Kain: "take it out for now, then we'll figure out where we're going to place that once we get back to designing this actual page"): no date, reading time or "Practical Workbooks". Where that line lives is open, for the workbook page's design. The workbook has no theme template yet; the rest of §22.15 applies when it is built, unless Kain's workbook sitting rules otherwise. **The thank-you page's two paths block (S163)** is now the shared `achology_two_paths()` used by the content pages too; its course lesson count is read from the course's curriculum file, never typed (it read 175, the DiMAP's count, for every course before).

## 38. Site Search Results Page Layout (COMPOSED AND APPROVED, Kain in Chat's side panel, S375)

One template serves the site search results page, the page every search box on the site lands on (DSRD 1 §7, rewritten S366: one search, the whole site). It has two states, results and no results, and Kain approved the look of both on the S375 renders, tabbed, at desktop, tablet and phone widths (standing rule 16). The two approved prototypes are in the Search Results Page folder inside Knowledge Hub Design Prototypes; that folder's README names them. The page is `noindex, follow` (DSRD 1 §10). Its address is WordPress's own search address, `/?s={term}`, served by a `search.php` template (Chat's call, S375, because a query is not a permanent URL and DSRD 1 §1's rules govern permanent URLs only; overturnable).

**How search behaves is not in this section.** Scope, weighting, exact-name-first, synonyms, misspellings, the dropdown preview and the no-results log all live at DSRD 1 §7 and are not restated here. This section owns only how the page is laid out.

### 38.1 The job

Get someone who typed a word or two to click the one page they meant.

### 38.2 The reader's arrival state

Arrives from any search box on the site (header, /learn/ hero, /help/, the 404) having just typed something. **Assumption, labelled:** most searches are one to three words, often a course name, an abbreviation (CBT, NLP) or a problem word (Baymard's 2026 search benchmark on query types; Achology's own no-results log does not exist until launch, DSRD 1 §7.5). They expect the search-engine shape: their words at the top, a list below.

### 38.3 The changes, in the reader's voice

1. "That is what I typed, and I can fix it here." (the field, pre-filled)
2. "I can see how many there are." (the count line)
3. "I can narrow this to the kind of page I want." (the pills and the sort)
4. "I can tell which one I meant, and why it matched." (the result row: type label, title, snippet)
5. "There are more if I need them." (pagination)

No results: 1. "Nothing was found, and I have not missed it." 2. "It might be my spelling, and here is the fix." 3. "I can browse instead." 4. "I can take something away anyway." 5. "I can ask a person."

Both tests run (page-composition, rule 10): every block below carries one of these changes, and every change has a block.

### 38.4 Page structure, results state (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18), carrying the site search field per DSRD 1 §7.4.
2. **No breadcrumb.** A results page is not a place on the site map (DSRD 1 §9 mirrors the URL hierarchy, and this page has none).
3. **The search field**, pre-filled with the query, in the 880px measure at the 1200 frame's left: the DSRD 7 §5.5 field (44px, Mulish 14, 10px radius, hairline border, search glyph inset 16px) with the §5.1 primary button at the field's height as its Submit, reading "Search". 48px below the header, per DSRD 7 §4.3 ruling 5.
4. **The count line**, 16px below the field: "{N} results for "{term}"", Mulish 14, soft grey #5E6B75, the number and the word "results" at weight 600 in brand dark. Singular "1 result".
5. **The control bar**, 24px below the count, the listing page's own unified bar (§21.4): left, the type pills All, Articles, Book Notes, Quotes, Workbooks, Help, Courses, Pages; right, the sort pills Most Relevant, Newest. Same pill values as §21.4 (Como 12/500, 8px 16px, 20px radius; active brand orange with white text; inactive off-white). The Category filter DSRD 1 §7.2 names is carried by the type pills' second row only when a Knowledge Hub type is selected; on All it is not shown, because help answers, courses and pages have no Knowledge Hub category (Chat's call, S375; overturnable). Phone: two rows per §21.9.
6. **Hairline**, 48/48 (32/32 on phones), DSRD 7 §4.3.
7. **The results**, one column, 880px measure, 16px between rows. **Approved: option B, the full-width row with a snippet** (Kain, S375, from two tabbed options; option A, the mini card grid, is kept in the prototype as the loser). Each row is the locked mini card (DSRD 8 §6.9) stretched to the column: 96px thumbnail left, then the type label (Como 11/600 uppercase, AA-safe orange #B8460F), the title (Como 16/600, brand dark, two-line clamp), and one new element, **the snippet**: Mulish 14/400, line-height 1.5, soft grey, two-line clamp, 6px under the title, the matched excerpt with the matched words in weight 600. No watermark at this width. The row is one link to the page.
   - **Type labels and thumbnails by page kind.** Article, Book Note, Quote, Workbook: exactly §6.9. Three new kinds, proposed by Chat and approved on the render: **Course** (thumbnail: the course's school colour, DSRD 5, with the `graduation-cap` glyph in white), **Help** (off-white thumbnail with the `circle-question-mark` glyph in brand orange), **Page** (off-white with `file-text` in brand orange; used for school, commercial and policy pages). These three labels are added to the mini card's label set in DSRD 8 §6.9 at the next unlock, and this line is that section's pointer until then.
   - Rank order is SearchWP's relevance (DSRD 1 §7.1); this section does not group results by kind.
8. **Numbered pagination**, DSRD 7 §17.1 and §21.9 (compact on phones), 48px above (32 on phones), 10 results per page.
9. Rainbow stripe and footer (DSRD 8 §19), 64px above (48 on phones).

### 38.5 Page structure, no-results state (top to bottom; also the phone order)

Blocks 1 to 3 as above, then:

4. **The not-found line**, 24px below the field (the page-title spacing, DSRD 7 §4.3): "We couldn't find anything for "{term}"" as the page's H1, Como 24/700 (the one H2 size, DSRD 7 §3.1, used here as the H1 because the page title is a sentence, not a name; Chat's call, overturnable on the Safari read). Kain's S366 words.
5. **The hint line**, 16px below, Mulish 18 body: **"Did you mean {corrected term}? Or try a shorter phrase."** when SearchWP can supply a correction (the corrected term is a link that runs the corrected search), otherwise **"Check the spelling, or try a shorter phrase."** Added on Kain's yes at S375, from Nielsen Norman's no-results guidelines and Baymard's finding that readers ignore spelling advice but click a corrected word.
6. Hairline.
7. **Browse by subject**: block heading "Browse by subject" (Como 24/600) with its supporting line, then the seven category cards, the locked card from the category hub (DSRD 8, as §20 uses it), in a 4/2/1 grid. The seven names come from DSRD 1 §4.
8. Hairline.
9. **The workbook offer**: the site's workbook lead-magnet capture (DSRD 4 §5; the Kit form, DSRD 3 §3.1), one heading, one line, one button.
10. **The ask line**, 24px below: "Can't find it? Ask us and a real person will point you the right way." with "Ask us" linking to /enquiries/. Added on Kain's yes at S375 (Baymard: a human door on the page readers are most likely to leave from). The wording is Chat's and Kain may change it.
11. Rainbow stripe and footer.

No controls bar and no pagination in this state. No humour anywhere on it (Nielsen Norman, guideline 3; DSRD 1 §7.3).

### 38.6 What is settled and what is open

**Settled by this section:** both block orders, the result row (option B) and every value above that is copied from a locked section. **Settled by Kain's eye at S375:** the shape of both states.

**Open, for Code's Safari sitting, not for Chat:** the header search control and the dropdown preview (DSRD 1 §7.2 and §7.4; the theme holds the header, so standing rule 16 puts that render in Safari; the S321 brief commissions it). **Open on a fact from Code:** whether SearchWP on the install supplies a spelling correction and phrase synonyms (`ASK__What_SearchWP_On_The_Install_Can_Actually_Do_S366`); the build does not wait on it, because block 5 has its fallback line.

**Stand-ins in the prototypes, named so nobody reads them as decisions:** the snippet text in every row (the real one is the page's excerpt), the workbook offer's words (DSRD 4 §5 owns them), the category card drawn as a plain tile (the locked card replaces it at build), and Mulish standing in for Como on titles (Como was not available in Chat's environment at S375).

**Corrected S378:** the "locked card from the category hub" named in block 7 of 38.5 does not exist. The category hub has no category card (its subject navigation is the pill strip, §20.5). The subject card is registered new in §39.5, where the Knowledge Hub front page needs it, and block 7 here takes that card once Kain has approved it.

---

## 39. Knowledge Hub Front Page Layout (COMPOSITION AGREED, Kain S378; LOOK RULED, Kain S390)

One page at `/learn/` (DSRD 1 §2.4; PRD Pr1.8). Its contents were listed in DSRD 2 §1.2; it had no layout here until S378. **This section holds the composition only** (page-composition, rule 11): the job, the reader, the changes and the block order, agreed by Kain in words at S378. How each block looks is ruled by his eye on a render, and recorded here when it is.

### 39.1 The job

Get someone who arrives at /learn/ to pick one way into the library and go to it. **Subordinate job:** take a free workbook.

### 39.2 The reader's arrival state

**Assumption, labelled:** arrives from the header's Learn link or the mega menu, or from the "Learn" crumb on any Knowledge Hub page. Knows Achology is a school; does not yet know what the library holds or how it is organised. A smaller share arrives from a search engine on the Knowledge Hub's name. No evidence yet; the first real evidence is the page's own analytics after launch (DSRD 3 §6.4, Rank Math Analytics).

### 39.3 The changes, in the reader's voice

1. "I know where I am."
2. "This is Achology's free library, and I know roughly what is in it."
3. "I know who writes it, so I can trust it." (the gap the completeness check found, S378)
4. "I can find what I already have in mind."
5. "I can pick my subject."
6. "I can follow a goal or a problem I have, across subjects."
7. "It is alive, and I can start reading something now."
8. "I can get something free to practise with."

The completeness check for a routing page (page-composition, rule 6) was run: where am I (1), what is here (2), is it for me (5, 6), why trust it (3), where next (4 to 8). Both tests run: every block below carries a change, and every change has a block.

### 39.4 Page structure (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18).
2. **Breadcrumb**, Home > Learn, the §20.3 component. Change 1. *DSRD 2 §1.2 listed it last; every other page puts it first, so it moves to the top here (S378). DSRD 2 §1.2 is corrected to match.*
3. **The top block**: H1, one line on what the library is, the four counts across the whole Hub (articles, book notes, quotes, workbooks, each linking to its cross-category listing, as the §20.4 counts do), one line naming who writes it, and the site search field (the §38 field, DSRD 7 §5.5, per DSRD 1 §7.4). Changes 2, 3 and 4. Words owed: the H1, the line, the trust line.
4. **Subjects**: section header (DSRD 8 §23) and seven subject cards, one per DSRD 1 §4 category, each linking to /learn/{category}/. Change 5. **New component, §39.5.**
5. **Topics**: section header and a strip of topic pills (the §20.8 pill), each linking to /learn/tags/{slug}/, with a link to the all topics index (§35). Change 6. Which topics it carries is owed (DSRD 2 §1.2 says "curated outcome and problem tags"; no list is written).
6. **Latest articles**, **latest book notes**, **latest quotes**: three sections, each a section header with its View all link (to the cross-category listing) and one row of the standard card (DSRD 8 §6.1, §6.2, §6.3), newest first, auto-filled, no curation. Change 7.
7. **The free workbook offer**: the same workbook capture block §38.5 block 9 uses (DSRD 4 §5; the Kit form, DSRD 3 §3.1), so the site has one. Change 8. *DSRD 2 §1.2 called it a banner; one shared block replaces a second design.*
8. Rainbow stripe and footer (DSRD 8 §19).

### 39.5 New component: the subject card

Registered S378. Seven of them on this page; the same card replaces the plain tile in §38's no-results state. Carries, per DSRD 2 §1.2: the subject's name (DSRD 1 §4), one short line on the subject, and its content counts. **The short line (Kain, S378): the first sentence of each subject's own hero intro (§20.9), word for word.** Kain wrote the intros himself at Chat session 27; no new copy is written for the card. The card's line reads from the same source as the hub hero, so the two can never drift. Look not decided; ruled by Kain on a render, then filed to the component library with its prototype and build sheet.

### 39.6 What is settled and what is open

**The words (Kain, S378, approved as drafted by Chat):**
- **H1:** The Achology Knowledge Hub
- **Top line:** Free articles, book notes, quotes and workbooks on psychology and how people live, from Achology, an online school of applied psychology. Pick a subject, follow a topic, or search for what you have in mind.
- **Trust line:** Every piece is sourced, and edited and approved by a named person at Achology. Read how we write. ("Read how we write" links to /policies/how-we-write/, DSRD 1 §2.6.)
- **Topic strip, 12, in this order:** Manage Stress & Anxiety, Overcome Self-Doubt, Break Negative Thinking, Overcome Feeling Stuck, Navigate Life Changes, Build Self-Discipline, Build Confidence, Improve Relationships, Find Purpose & Direction, Grow Self-Awareness, Help Others Grow, Achieve Your Goals. Chat's pick, unevidenced: the problems a first-time visitor most often brings plus the broadest goals. **Kept by Kain at S378, with a review:** an AnswerSocrates check was tried and cannot rank topics against each other (each term is scaled to its own peak), so the strip is reviewed after launch against the site's own search log (DSRD 1 §7.5) and Rank Math Analytics (DSRD 3 §6.4), and reordered from what readers actually type and click.
- **Section headings:** Browse by Subject, Explore by Topic, Latest Articles, New Book Notes, Latest Quotes. **Supporting lines (DSRD 8 §23.4; Kain, S378):** Browse by Subject: "Seven subjects, each with its own articles, book notes, quotes and workbooks." Explore by Topic: "Follow one goal or problem across every subject.", with a "See all 36 topics" link to /learn/tags/. The three latest rows reuse the approved cross-category listing intros (DSRD 2 §4.3) for articles, book notes and quotes, word for word.

**Settled (Kain, S378, in words):** the job, the changes and the block order above. **LOOK RULED, Kain S390 ("yes"), on the whole page rendered at 1280, 834 and 390 in Chat's side panel, reusing the locked header, footer, breadcrumb, section header, pill and the three card types, with the subject card new.** The approved file and its build sheet are in the page's design folder. The subject card is registered in the build sheet and goes to DSRD 8 on Code's build. Counts, quotations and the workbook offer's words in the render were stand-ins and were named as such. **Open, for Kain's eye on a render:** nothing further on the look. **Open, words:** none. **Open, one fact:** how many articles, book notes and quotes exist at launch, which decides whether each latest row shows three or six cards; read from the launch content set before the render.

---

## 40. Quote Page Layout (TEMPLATE APPROVED BY KAIN, "100% approved", Code's S146; recorded by Chat S401)

**S149 and S150: the note at the head of section 22 governs where it touches this section (the rail, the date line, the type link, one hero, the Download row, and from S150 the hero's speech bubble, the one side panel and the subtitle).**

The quote page is built on the content page standard the article and book note share (§22, §32, the one block standard at §22). Until S401 its rulings lived only in DSRD 8 and the quote page's design folder; this section is its page-level home. Recorded from RULING__The_Quote_Page_Sitting_S146 and RULING__The_Quote_Page_Design_Principles_For_Every_Hub_Page_S146 (channel Archive). Kain approved the template whole at S146; the Kain's-eye half of chapters 10 and 11 is written in its DSRD 6 record, and the machine halves and chapters 1 to 9 stay open, so the page reads "built, gate open".

1. **The hero picture** is a square on the 256 cover column, from just above the label to the date line, inside the band's padding, so its right edge is the side panel's right edge. Three Achology bubbles sit behind it (large 180 behind its top right, medium 96 by its lower left, small 44 and faint beside its top left), desktop only, 1024 and up (theme 0.707.68 to 0.707.70). Below 1024 it stacks at 16 by 9 with no bubbles. **The pictures are blurry on purpose; never flag their softness as a fault.** **Superseded S150 (0.707.121): the three loose bubbles are gone, and from 1200 wide the picture is cut to a speech bubble 216 wide with a thin orange line in the same shape behind it; see the note at the head of section 22, item 10.**
2. **Download, Share and Copy** are separated by a 1px upright mid-grey line, 16 tall, centred in the 24 gap (0.707.66). Where the browser cannot share, the line falls only between the two buttons left.
3. **No Related Further Reading at any width** (§22.8, 0.707.82): Explore More Quote Articles does that job. The side panel travels the whole page and rests 48 above the hairline closing Explore More, and that hairline runs on across the right column, drawn by the panel, never by widening the hairline (the course cards widened at 0.707.79 when the hairline itself was widened, and were put right at 0.707.81).
4. **The reading progress line, the reading column's width and the body text size** follow the site standard at §32, items 5 and 6.
5. **The course picture in the writing carries the three bubbles in miniature (Kain, Code's S147, theme 0.707.97 and 0.707.98; recorded by Chat S403 from RULING__The_Book_Note_Is_Finished_And_The_Quote_Course_Picture_S147).** Kain: "it might be good for us to assign a very, very similar treatment to the image which appears halfway down the quote article." The course cover in the writing (a subject picture that keeps its own shape) takes the book note author photo's treatment, refined at 0.707.98 to tab 3 of four: the picture 224 wide with its top the figure's top, the figure 256 wide, the bubbles in the 32 strip at its right (96, 48 turned at the picture's foot, 22 between), the caption the picture's width; the medium bubble hangs from the caption so it meets the foot of a picture of any shape. Quote pages only, from 768 up; on a phone the picture keeps its plain, centred look. Measured live at 1440, 768 and 390: picture top 0 from the figure top, caption 16 below, no sideways scroll. The values live in the Author Photo component's build sheet (prototype v2); this item records the ruling.
6. **The course block's words** are the S147 words at §22.10 ("Ready to Take Your Learning Further?"), with "this article" kept on the quote page by Kain's choice.
7. **The section numbers (Kain, Code's S149, theme 0.707.109; recorded by Chat S405).** The same orange labels as the book note (§32, item 16), above each heading and in the contents. The contents' first entry, The Quote, is the quote card and has no heading, so the headings read from 02, matching their entries; Explore More carries its number above its heading. Verified live by Code on Trust Is The Key Ingredient: four headings numbered 02 to 05, five contents entries, all orange.
8. **The side panel and the subtitle (Kain, Code's S150, theme 0.707.127 to 0.707.132; recorded by Chat S408).** The panel carries the quote's source cover (the book's for 75 book quotes, the course's for 201 course quotes), at the foot of the screen once the hero has gone, with no decoration behind it, the book note panel's cover exactly (256 by 357, the book's own shadow). Book quotes keep "View the Book on Amazon"; course quotes take "View this Course on Achology". The author's picture and Know Your Psychology leave the panel. The subtitle takes two lines, balanced. The record is at the head of section 22, items 13 and 14.

9. **The in-text picture needs a section of three paragraphs or more (Kain, Code's S156 sitting, theme 0.707.156; recorded by Chat S418 from RULING__In_Text_Picture_Needs_Three_Paragraphs_S156).** Kain, on the first Lane B quote page read in Safari: "the problem is there's only two paragraphs in that section, which means it creates massive white space on the page". The picture still sits at the top of the second paragraph (item 5; section 22 item 12; the S116 rule), but only in a section of three paragraphs or more. The section the page names is tried first, then up to two after it; the first with three paragraphs or more takes the picture. Where none has three, the named section keeps it, so no page loses its picture. One function serves the quote page, the article and the book note (`achology_book_author_portrait()` in `knowledge-hub-parts.php`), so the rule binds all three. Measured by Code: 276 quote pages already have three paragraphs in the first section and are unchanged; the 17 Lane B drafts have two, and each takes the picture in its second section.

The general design rules this sitting produced, which bind every page, are recorded in DSRD 7 (S401). The side panel's rules are at §22.8.

### 40.1 The hero from S162 and S163

The quote page takes the Soft Light hero and its page changes in §22.15 and §22.15a (S163: the Drawn Bubble contents, the panel down to the two paths, the two paths foot) whole. **Its hero is the article's:** the faded portrait, with no quote, slip or card in the band; the quote appears once, in the card under the band. The listen bar is off this page (Kain, K10, S422; built 0.707.234). The side panel runs down to the hairline above the two paths (S163, §22.15a item 4), restoring Kain's S146 ruling; the foot is the two paths. Below 1200 the Amazon or course button sits in the side panel's strip under the contents. Where anything above in §40 says otherwise, §22.15 wins.

