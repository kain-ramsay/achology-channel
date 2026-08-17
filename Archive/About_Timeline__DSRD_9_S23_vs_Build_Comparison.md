# DSRD 9 §23 vs THE BUILT ABOUT PAGE TIMELINE

**A conflict comparison for Claude Chat**
**From: Claude Code · 22 July 2026 · Theme v0.35.1 · Timeline as built in the untracked `page-about.php`**

**Sources compared:** `docs/DSRD_9_Page_Layout_Specs.md` §23 (About Page Timeline, STRUCTURE LOCKED, §23.1–§23.15) against `page-about.php`, `about.css` and `about.js` as they stand uncommitted.

---

## The verdict, first

**The era system was implemented exactly. The component around it was replaced.**

The build follows §23.5 and §23.8 to the hex, keeps §23's internal era slugs, keeps 12 of 13 dot-variant assignments, and keeps most milestone titles close to verbatim. Then it discards the three interface elements §23 specifies — the student enrolment bar, the six era filter tabs, and the footer CTA — and replaces the centred alternating spine with a single left spine inside a pinned scrolling window.

That pattern says the build inherited §23's *design system* (almost certainly through the shared prototype lineage) without anyone opening §23's *structure*. It is not a page that ignored the spec. It is a page that absorbed half of it by osmosis and rebuilt the other half from scratch.

**§23.20's lock note matters for how you read what follows.** It locks *"structural anatomy, responsive behaviour, era system, milestone copy, spine/dot alignment"* and explicitly defers *"surface-level visual calibration (final grey shades, exact pill placement, micro-spacing)"* to the About page build session. I have sorted every difference by which side of that line it falls on. Where a difference is genuinely arguable, I have said so rather than ruling.

---

## Part 1 — What the build got right

Recorded first so the conflict list is not read as a wholesale failure.

| §23 clause | Status |
|---|---|
| **§23.5 / §23.8 era colour system** | **Exact.** All five era colours implemented as inline `--era` values: `#354149`, `#4d6672`, `#8A9199`, `#c05a1a`, `#ED6922`. All five tag backgrounds: `#e8eaeb`, `#eaeeef`, `#f0f1f2`, `#fce8d9`, `#fde8d5`. Both tag text colours: `#354149`, `#7a3606`. The Expansion year badge's distinct `#6b7680`. Every value matches §23.8's table |
| **Era slugs** | **Intact.** `data-era="origins|growth|expansion|maturity|community"` on the five era groups and on the chart's five segments — §23's names survive in the markup even though the visible labels were changed |
| **§23.12 milestone roster** | **All 13 present, in order,** 2012 → 2025/26, in the correct eras |
| **§23.9 dot variants** | **12 of 13 correct.** Standard dots on 2012, 2014, 2015, 2016, 2019, 2020, 2023, 2024, 2025; large on 2017, 2021, 2022 — exactly §23.12's large-dot assignments |
| **§23.12 milestone titles** | **Close to verbatim** for most. 2012, 2014, 2015, 2016, 2019, 2020, 2021, 2023, 2024, 2025 are identical or near-identical |
| **D10 body-text grey** | **Followed.** `.m-desc` uses `--color-soft-grey` (`#5E6B75`), not `#8A9199` — the WCAG fix D10 called for |
| **§23.6 spine colour concept** | Retained as a spine with era fill, though repositioned (see conflict 4) |

---

## Part 2 — Conflicts with LOCKED clauses

These are the ones that need a decision, because they contradict things §23 says are locked.

### Conflict 1 — The student enrolment bar is gone (§23.3, locked)

§23.3 specifies a three-cell horizontal bar with a bordered container, a "live now" third cell inverting to brand dark, and a "Live" pill top-right. Confirmed content: 2017 / 100,000 / Students Enrolled · 2022 / 500,000 / Students Enrolled · TODAY / 670,000+ / Students Worldwide.

**Built:** no student bar exists. `grep` for `student-bar`, `sb-year`, `sb-num` in `page-about.php` returns zero. In its place the build carries two different things: a dark stage above the timeline with an animated odometer and a live counter, and a four-figure statistics panel below it reading 4.66 Average Course Rating · 171,306 Total Student Ratings · 216 Countries With Students · 28 Total Number of Courses.

Note that the replacement panel does not carry the same four facts. The student-count progression §23.3 exists to show is now only visible inside the milestones themselves.

**Also touched:** D6, D7, D8 and D9 in §23.14's decision register are all student-bar decisions. All four are silently void in the build.

### Conflict 2 — The six era filter tabs are gone (§23.4 and §23.10, locked)

§23.4 specifies six full-width tabs — All eras, Origins, Growth, Expansion, Maturity, Community — each a button that filters the timeline, with active/hover tints at 18% and 40–45% of the era colour. §23.10 specifies the vanilla-JS filter behaviour in implementation detail: `.tab-c` click handlers, `data-era` reads, `.tl-item` show/hide via a `hidden` class.

**Built:** no tabs, no filtering, no `.tab-c`, no `.tl-item`. The eras appear instead as static group headings inside the scrolling timeline. The `data-era` attributes survive on the group containers but nothing reads them for filtering.

**Also touched:** D3 (mobile tap targets for the tabs) is void.

### Conflict 3 — The footer CTA is a different block entirely (§23.11, locked)

| | §23.11 | Built |
|---|---|---|
| Helper text | `Want to understand the thinking and values behind everything you've just read?` | *(none)* |
| CTA | Outline pill button, `Hear directly from Achology's Founder →` | Inline text link, `join them`, inside a sentence |
| Full closing copy | — | `670,000+ mature learners from around the world have brought the Achology story this far. Will you join them?` |
| Link target | `/about-us-founders-letter/` | `/membership/` |

This is not a calibration difference. The spec sends the reader to the founder's letter; the build sends them to membership. **Different copy, different control, different destination, different intent.**

### Conflict 4 — Layout: no alternating zigzag at any width (§23.7 and §23.13, locked)

§23.7 specifies a three-column grid — content / 48px node / spacer — with milestones alternating left and right about a centred spine. §23.13 makes this the desktop (≥1024px) layout and reserves single-column-left for below 1024px, giving reasons: *"at tablet widths the columns become too narrow to read comfortably."* D1 and D2 restate it.

**Built:** single-column-left at **every** width, including desktop. The spine sits at the left of the rows, dots hang left of the content, and every milestone is left-aligned. The desktop layout §23 describes does not exist in the build.

Layered on top, the build adds behaviour §23 does not describe at all: the whole timeline runs inside a fixed-height window that pins to the viewport while the story scrolls through it at 1:1, with a `.is-flat` fallback when the frame cannot fit the screen. Measured: flat is false at 1440×1000 and 768×1024, true at 390×844.

**Also touched:** D4 and D5 are spine-position and node-specificity decisions for the <1024px collapse. Both describe a layout the build does not have.

### Conflict 5 — All 13 milestone descriptions rewritten (§23.12, locked — copy explicitly named)

§23.12 opens *"Year, era, dot variant, title, and description are locked."* Every description in the build is different. Two examples:

> **§23.12, 2012:** Kain Ramsay develops the world's first video-based psychology training program, establishing the foundation for what would later become Achology.
>
> **Built, 2012:** Kain Ramsay records and publishes the world's first video-based psychology training programme, taking a subject usually reserved for lecture halls and private clinics and putting it in front of anyone with an internet connection. The foundation of what would later become Achology is laid in this single, quiet decision.

> **§23.12, 2024:** Master Achologists found the Society of Modern Applied Psychology to raise standards for training and practice in applied psychology.
>
> **Built, 2024:** Master Achologists found the Society of Modern Applied Psychology, an independent body created to raise the standards of training and practice across the field, and to define what competent practice requires. The Society maintains the competency development framework accredited graduates complete. The academy's graduates now hold the profession they trained for to a higher bar than the one they found.

The rewrites are roughly two to three times longer, and they add inline links the spec does not mention — to `/about/instructors/kain-ramsay/`, `/about/instructors/gerard-egan/`, `/courses/`, `/accreditation/`, `thesomap.org` and `/free-events/`.

Two titles also changed: 2017's em dash became a colon, and 2022's `Half a million students reached worldwide — curriculum expands to 25 courses` became `Half a million students reached worldwide, and the curriculum expands to 25 courses`.

### Conflict 6 — Era display names changed (§23.4 / §23.5, locked as the era system)

| §23 | Built |
|---|---|
| Origins | Achology Origins |
| Growth | The Growth Years |
| Expansion | The Expansion Years |
| **Maturity** | **The Evolution Years** |
| Community | Community Development |

Four are expansions of the spec name. **Maturity → The Evolution Years is a substantive rename**, not a lengthening. The date ranges are unchanged; only the formatting differs (`2012–14` in the spec, `2012–2014` in the build).

### Conflict 7 — The final milestone's dot is wrong, and the CSS for the right one is dead

§23.9 and §23.12 specify the 2025/26 milestone as a **large dashed dot** — the dashed variant exists solely for *"future-leaning final milestone only."*

**Built:** the 2025/26 milestone carries a plain standard dot. `.fa-dot--dash` **is defined** in `about.css:53` and is **never used** in the template. The one place the spec's most distinctive dot belongs is the one place it was not applied — and the style for it is shipping as dead code.

### Conflict 8 — Heading and subheading (§23.2)

| | §23.2 | Built |
|---|---|---|
| Heading | `Achology: Our History and Timeline` | `The Achology Story` |
| Subheading | `Like all great educational institutions of our time, Achology boasts a unique origin story:` | Same sentence, ending in a full stop, then a second sentence added: `Thirteen milestones across five eras, from the world's first video-based psychology course to a worldwide learning community 670,000 students strong.` |

The subheading is a retention plus an addition. The heading is a straight replacement.

### Conflict 9 — Stat labels (§23.12)

| Milestone | §23.12 | Built |
|---|---|---|
| 2017 | `100,000 students enrolled` | `100,000` / `Students & Active Members Enrolled` |
| 2021 | `350,000 total enrolled students` | `350,000` / `Students & Active Members Enrolled` |
| 2022 | `500,000 total enrolled students` | `500,000` / `Students & Active Members Enrolled` |
| 2025/26 | `670,000+ students in the Achology database today` | `670,000+` / `Students & Active Members Enrolled` |

The build standardises all four onto one label. The spec varies them, and its 2025/26 wording — *"in the Achology database today"* — is a materially different claim from *"Students & Active Members Enrolled."*

### Conflict 10 — Placement context (§23's opening paragraph)

§23 states the component *"sits below the founder narrative on the About page and above the closing CTA."* §23.20 repeats it: the timeline is to be evaluated *"in context against the founder narrative above and the closing CTA below."*

**Built:** there is no founder narrative on the About page. "About the Founders" was removed during the design session, its blurb reassigned to the Founders' Letter page. The timeline now sits between the four "Thinking that Drives Achology" cards and the student-voices section.

So §23's stated evaluation context no longer exists on the page.

---

## Part 3 — Differences that fall under the deferred-calibration carve-out

§23.20 defers *"final grey shades, exact pill placement, micro-spacing"* to the build session. These differences are arguably covered by that, and I am not calling them conflicts — but they are uniform enough to look like a deliberate re-scaling rather than incidental drift, so the decision should be conscious.

| Element | §23 | Built |
|---|---|---|
| Era tag | 10px / 600 / padding 2px 8px / radius 3px | 11px / 700 / padding 3px 10px / radius 4px |
| Year badge | 11px / 600 / 0.85 opacity | 12px / 700 |
| Title | 15px / 500 | 17px / 600 |
| Description | 13px | 15px |
| Stat number | 22px / 500 | 36px / 700, in the heading font |
| Stat label | 11px | 13px |
| Standard dot | 14×14px, 2px white border | 16×16px, 3px white border |
| Large dot | 18×18px, 3px white border | 20×20px, 3px white border |
| Inner wrapper | max-width 860px | 880px (`--container-article`) |

Every type size moved **up**. Whether a uniform type re-scale is "surface-level visual calibration" or a change to structural anatomy is a judgement I should not make on my own — flagging it for the decision rather than assuming.

---

## Part 4 — Spec-versus-spec contradictions found while comparing

Reported and not resolved, per the standing rule.

1. **The trust figure.** DSRD 4's Trust Line (variant 3) reads `Trusted by 679,000+ learners across 216 countries · 4.66★ from 171,000+ ratings`. DSRD 9 §23 uses `670,000+` twice (§23.3 cell 3, §23.12 final milestone). The build uses `670,000+` in three places. **The two specs disagree with each other**, and the build follows DSRD 9.
2. **The founder's letter URL.** §23.11 gives `/about-us-founders-letter/`. The build links `/about/founders-letter/` — twice more elsewhere on the page. DSRD 1 owns URL structure and should settle which is correct; I could not confirm either page exists, having no access to the build site.
3. **The About page's proof block.** DSRD 4 assigns the About page **variant 1, the Global Impact Block** — *"World map, all headline stats, country breakdown, star rating."* The build carries a four-figure statistics panel closer to variant 2, the Stats Strip, and has no world map or country breakdown. Whether §23's timeline and DSRD 4's Global Impact Block are meant to coexist on the page is not stated in either document.

---

## Part 5 — Two loose ends

- **§23.15 names a prototype reference file, `achology-timeline.html`.** It does not exist in `previews/`. Whatever the build was made from, it was not that file under that name.
- **§23.13 carries an outstanding instruction to the production rebuild:** move the responsive rules from `max-width: 600px` to the two correct breakpoints, and raise mobile tap targets to the 44px floor. Both instructions target elements the build no longer has, so both are moot as written.

---

## What I am not deciding

Whether the build or the spec is right. Kain approved every visible element of what was built, over a full day, at three breakpoints — so the likeliest reading is that §23 is stale and the build supersedes it. But §23 is marked STRUCTURE LOCKED, the build was made without anyone opening it, and "the spec is stale" is a conclusion for chat and Kain, not for me.

What this comparison establishes is the size of the gap: **ten conflicts against locked clauses, four of the ten decisions in §23.14's register voided, and one dead CSS class where the spec's most distinctive detail should have been.**

---

*End of comparison.*
