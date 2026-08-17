# DELIVERY: the Global Impact component, built and approved, for specification

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Commissioned by Kain in session:** "this kinda gray block is phenomenal... I
need you to pass this over to Claude Chat as a component that gets literally
built and specked out as one of our actual components because this block within
itself is absolutely phenomenal, and I'm gonna wanna use this in different
places throughout the website."

**Live and approved by his eye at theme v0.44.9:** https://achologytest.com/reviews/

**What this file is.** Everything a build sheet needs, in the shape my S052
answer asked for: what exists and its name, where it lives, the values, and
tokens separated from one-offs. The decision record is deliberately not here.
This is the second component to be carried across under the S257 system, after
the book note card.

---

## 0. The precedence problem, which is real and is yours to settle

S257 ruled: the approved prototype is the signed record, the sheet matches the
prototype, the code matches the sheet.

**This component has no prototype and cannot have had one.** It was designed
live on the rendered page with Kain across roughly twenty rounds this session,
which is the method the S240 instruction file set for this page. There was never
a file for him to approve by eye; the page itself is the thing he approved.

So the precedence chain has nothing at its top, and I am not going to invent
one. Two honest routes, and the choice is Kain's:

1. **The rendered page becomes the prototype**, exported from the live page at
   v0.44.9 into the component's design folder as its v1 signed record. Truthful,
   because that is literally the artefact he approved.
2. **The build sheet becomes the top of the chain for this component**, with the
   precedence reading sheet then code, and the page link standing as the record.

I recommend the first: it keeps one rule for every component rather than a
special case, and the export is mechanical. But note the trap either way, since
it is the exact failure S257 exists to end: **the moment the sheet exists, this
file stops being the record.** Do not leave both live.

---

## 1. What it is

A dark full-bleed panel carrying four things as one unit: a world map with
proportional markers, a frosted country panel, a narrative line, and four
headline figures. DSRD 4 §14.2 Variant 1, the V2B Dark Band direction. Kain
ruled at S240 that the map and the figures are one component, not two.

**Named for reuse, not for this page.** Every class is prefixed `gi`, not
`reviews`, because DSRD 4 §14.2 says it "is built once as a component and shared
by all three placements", the others being the homepage and About. It currently
lives in `reviews.css` because that is the only page carrying it; **it should
move to a shared stylesheet at the first reuse**, and it will move whole.

---

## 2. Where it lives now

| Thing | Where |
|---|---|
| Markup | `page-reviews.php`, inside `.article-container` |
| Styles | `reviews.css` section 2, enqueued for `reviews` only, after `about.css` |
| Map generator | `tools/build_world_map.py` |
| Map graphic | `images/reviews/world-map.svg`, 53KB, committed, generated |
| Country data | `data/student-countries.json` |
| Marker artwork | `images/achology-bubble-mark.webp`, the brand mark itself |
| Figure classes | `.story-proof*` in `about.css`, reused not copied |

---

## 3. Structure

```
section.gi-block                     clear: both (clears the hero float)
  header.gi-intro                    section header, on the white ground
    h2.gi-intro__title
    p.gi-intro__lead
  div.gi                             the dark panel
    div.gi__stage                    grid: 1fr / 260px
      div.gi__map                    absolute, inset 0, overflow hidden, z 0
        div.gi__map-inner            the map's own box, aspect 2.5
          img.gi__map-img
          span.gi__marker            x34, absolutely positioned
            span.gi__marker-dot      the bubble
      div.gi__narrative              align-self: end, z 1
        h3.gi__heading
        p.gi__lead
      aside.gi__countries            frosted panel, z 1
        ul.gi__country-list > li.gi__country
          span.gi__country-name + span.gi__country-count
        p.gi__honest
    div.gi__figures                  border-top rule
      div.story-proof                About's classes, reused
```

---

## 4. Values

**Tokens throughout unless named as a one-off below.**

| Element | Value |
|---|---|
| Panel | radius 16px, padding `--sp-xl`, `overflow: hidden` |
| Panel bleed | `margin-inline: calc(-1 * var(--sp-xl))` at min-width 1040px, DSRD 7 §4.4 |
| Panel background | `linear-gradient(135deg, #3E4E5A 0%, var(--color-dark) 48%, var(--color-dark-footer) 100%)` |
| Stage | grid `1fr 260px`, gap `--sp-xl`, `align-items: start`, no min-height |
| Map opacity | 0.20 |
| Map projection | equirectangular, world cut at 115W, viewBox 84N to 60S |
| Marker box | `width: r*2`, `height: r*1.573`, offset `-0.786r / -1r` |
| Marker sizing | area proportional to students; radius 3.3px to 28.6px |
| Marker opacity | 0.94 |
| Bloom | two per marker, `r*2.6`, radial gradient white 0.24 / 0.10 / 0, second offset +1.6s |
| Pulse | `gi-pulse` 3.2s ease-in-out, scale 0.9 to 1.24, opacity 0.94 to 1 |
| Bloom animation | `gi-bloom` 3.2s ease-out, scale 0.3 to 2.4 |
| Stagger | per-marker delay, golden-ratio stepping through the 3.2s cycle |
| Narrative | `align-self: end`, `width: max-content`, `max-width: 100%`, margin-bottom 0 |
| Heading | Como 20px/600/1.3, white |
| Narrative line | Source Sans 16px/1.6, white at 0.72, margin-top `--sp-sm` |
| Country panel | width 260px, radius 12px, padding `--sp-lg`, white 0.08, border white 0.14, `backdrop-filter: blur(6px)` |
| Country row | flex, space-between, padding 8px 0, border-bottom white 0.12, last none |
| Country name | Source Sans 14px, white 0.8 |
| Country count | Como 15px/700, white |
| Honest line | Source Sans 12px/1.5, white 0.55, margin-top `--sp-md` |
| Figures | margin-top and padding-top `--sp-xl`, border-top white 0.14 |
| Figure numerals | `--color-orange` |
| Section header | H2 Como 24px/600/1.25 dark; lead Source Sans 16px/1.6 dark, margin-bottom `--sp-xl` |

**The one-offs, both annotated in place:**

1. `#3E4E5A` in the panel gradient. Not a new value: it is the exact one About's
   `.story-proof` already carries, reused so the site's two dark stage panels
   are the same dark.
2. Radius 16px rather than `--radius-card` 12px. DSRD 7 §4.4 permits it for
   large stage panels per §5.3, and 16 is what `.story-proof` already uses.

**Three numbers that are geometry, not taste:** the marker box's 1.573 ratio is
the brand mark's own proportion (763 by 600); the map's 115W cut is derived, see
section 6; the golden-ratio stagger is deterministic so a rebuild is identical.

---

## 5. Data

**Country counts:** `data/student-countries.json`, 35 countries, read from
Kain's Udemy dashboard captures of 2026-08-10 filed in the Verified Student
Reviews Page assets folder. 34 are plotted; Singapore has no geometry in the
110m source and is deliberately not placed.

**A live inconsistency Kain has ruled on, and it must not be "fixed":** the
country panel and the figures still carry DSRD 4 §14.1's older numbers
(202,893 for the United States, 216 countries) while the map's data is his fresh
capture (204,910, 217). His ruling, S052: "do NOT update... once the site is
live, we can sporadically do number updates, but definitely not now." Record it
as deliberate in the sheet, or the next person to see it will tidy it.

---

## 6. The map generator, which is the part most worth documenting

`tools/build_world_map.py` decodes the Natural Earth 110m TopoJSON and writes
the SVG plus the marker markup. Nothing is fetched at runtime. Four things in it
are hard-won and should survive into any sheet:

1. **Markers are computed centroids of each country's largest landmass**, from
   the same file that draws the coastlines, so a marker cannot drift off its
   country. Largest landmass rather than whole country because the United
   States' true centroid, with Alaska and Hawaii averaged in, lands in the
   Pacific.
2. **Rings are emitted whole and the viewBox crops.** Clipping points and
   joining the survivors draws chords across the map; it rendered as black bars.
3. **Rings split where they cross the cut**, tested on rolled longitude. Without
   it a hairline runs the full width of the world at the equator.
4. **The cut at 115W is derived, not chosen by eye.** It is what puts the whole
   Pacific under the frosted panel while keeping all five headline countries in
   view: they run 3.7% to 69.3% of the width and the panel occupies the right
   27.5%. Re-derive it if the panel's width changes materially.

**The fill is a literal white, never `currentColor`.** The SVG loads through an
`<img>`, which is a separate document, so `currentColor` resolves against the
SVG's own root and the map rendered solid black.

---

## 7. Behaviour and accessibility

- Every marker carries `title` with its country and count.
- `.gi__map` is `aria-hidden` and the img `alt=""`; the SVG carries its own
  title. The country panel carries the same information as text.
- `prefers-reduced-motion`: blooms removed outright rather than left as static
  rings, bubble returns to rest. The information survives, the motion does not.
- Below 768px: stage becomes one column, map opacity 0.12, figure rules hidden,
  figures two-up.

---

## 8. Settled, and open

**Settled by Kain's eye this session, do not reopen without him:** the bubbles
as markers and their 10 per cent size increase; the white blooms and their
softness; blooms under the bubble; all markers pulsing out of phase; map at 20
per cent; the re-centred projection; narrative at the foot aligned to the
frosted panel's base; the heading-to-line gap; both pieces of copy.

**Open, and mine to flag rather than settle:** the block has no hover state on
the markers, which the S240 plan asked for ("a response on hover") and Kain has
not yet been shown; the component is still in `reviews.css` and needs a home
before its second placement; and there is no build sheet, which is what this
file is for.

*No em or en dashes in this file; checked before writing.*
