**Needs from Chat:** write these rulings into their owning documents (DSRD 4 section 14.2 for the Global Impact Block's map; the block's heading wherever its copy is recorded). For the factory session.

# RULING: the Global Impact Block is the dot world, and its heading is reworded

**From:** Claude Code, S141 (factory, theme edit on Kain's word in the sitting), Wednesday 30 September 2026. **To:** Claude Chat.

## Kain's words, in the S141 sitting

1. **The heading:** "reframe that to Achology reviews, what our learners have to say", confirmed as the block heading (not the page H1) when asked. Shipped as "Achology Reviews: What Our Learners Have to Say".
2. **The brief for the map:** "a visually spectacular map ... evidently transparent what the purpose of the map ... is", then after round one: "more contained, probably the same size as what already exists ... more informative ... credibility earning ... it needs to tell a story that we have this many students from this many countries ... incorporate the numbers into the image not outside of it and explain what the numbers actually are", and type and spacing "within our font and spacing rules".
3. **The choice:** "I think I like option B ... it looks very, very, very nice", of four rendered options (glow, dot world, arcs from the UK, today's cleaned up), each on the whole page.
4. **The one change:** move the map and the five labels down to sit centred between the heading row and the honest line.
5. **The go:** "Yes, go ahead and build that, Claude ... that looks really, really good."

## What shipped, theme v0.707.7

- The land as a grid of fine dots, lit orange where students live, brightest where most: `images/reviews/world-dots.svg`, baked by the new `tools/build_world_dots.py` from the theme's Natural Earth land and the same 34 country centroids and counts the S052 markers used. No live fetch.
- The five countries the frosted panel listed are now labels on the map, each "{n} students" (Kain's panel figures, unchanged). On a phone they become a list under the map.
- A key, "Students per country, Fewer to More". Two words of it ("Fewer", "More") and its title are Code's labelling of the legend, named here so Chat can confirm or replace them.
- The narrative (Kain's S052 lines, word for word) heads the panel; the honest line is unchanged; the figure bar stays inside the panel, with --sp-lg either side of its rule.
- Panel ground: the flat footer dark, as in the approved option. Gaps around the map measured 34 and 36 at 1200.
- Measured live at 1200, 768 and 390 on /reviews/ and /testimonials/: no label outside the panel, no sideways scroll. The block appears on those two pages only (About carries no Global Impact Block; an earlier line of Code's to Kain said three, corrected).

## Replaced and removed

The S052 bubble markers and their bloom, and the frosted country panel with its globe and people glyphs. Their CSS went with them (git holds it).

## Owed by Code (Rule 14 fold-back)

The approved state exported into the Global Impact Block's design folder as the next prototype version with its build sheet. Not done in this change set; carried in the S141 session report as not finished.

## Second ruling, same sitting: the block's type and depth (v0.707.8 to v0.707.10)

**Kain's words:** "the fonts just seem a little bit all over the place ... not particularly balanced ... there's quite a lot of dead space ... the bar on the bottom, with three different layers, that's just, it's not quite right either", then, of four rendered options and two refinements: "I prefer the one compact bar option ... look at the padding or spacing from the edge of the block inwards ... the font could be a little bit smaller ... centralized ... a little vertical hairline in between each of the four ... the sentence ... positioned to the right hand column as a mini disclaimer ... in the bottom corner", and on the render: "Yeah, that's perfect, Claude. Please put it live."

**What shipped:** one type rule for the block (Como for the heading and every number, Mulish for every word; heading 24, lead 16, figures 28, labels and captions 12, sentence case); inside padding --sp-2xl; figure bar without icons, each figure centred over its label with a hairline between; country labels one line, number only (the key says what it counts; "students" kept for screen readers); the honest line in the map's empty bottom-right ocean, dropping just under the map's corner where the map is narrower than 880 (Testimonials, tablet). Panel 598 tall at 1200 on /reviews/ (was 685 at v0.707.7). Measured live at 1200, 768 and 390 on /reviews/ and at 1200 and 390 on /testimonials/: no label off its pin or outside the panel, no sideways scroll.

## A number Chat may want to rule

The old marker tooltips said the United States had 204,910 students; the panel (and now the labels) say 202,893. The same gap runs through the five. The labels keep the panel's figures, per Kain's S052 "do not update" ruling on the numbers. Which set is the record is Chat's to confirm.

OWED BACK: the dated lines in the owning documents; the key's wording confirmed or replaced.

*No em or en dashes in this file; checked before writing.*
