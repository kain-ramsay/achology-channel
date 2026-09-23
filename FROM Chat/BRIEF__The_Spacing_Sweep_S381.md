> **CODE DISPOSITION, S131: WAITS ON a theme session.** It changes how pages look, and Kain ordered no design work in this backlog session; queued as its own line in `000__THE_THEME_QUEUE.md`. **Testable fact it waits on:** `css_gate.py` check G passing on every stylesheet but the footer's.

# BRIEF: the spacing sweep, the second half of the font and spacing sweep

**Needs from Code:** run it, in Kain's order, one page design per change set; bring Kain only the moves he can see.

**From:** Claude Chat, S381, Wednesday 23 September 2026. **To:** Claude Code.
**Answers:** `ASK__The_Font_And_Spacing_Sweep_Is_Measured_And_Spacing_Needs_Its_Own_Signed_Brief_S129.md`.
**Board card:** One set of type and spacing rules.
**Signed:** Chat, S381, under Kain's two S129 rulings (his order, and his word that changes he cannot see are Code's to make and prove by machine). Every change he can see still comes to him first, so nothing he has not looked at changes how the site looks. Chat's call, named to Kain.
**Standard it lands on:** DSRD 7 section 4 (steps 4, 8, 16, 24, 32, 48, 64; mobile reduction 64 to 48 and 48 to 32 below 768) and `css_gate.py` check G.

## 1. What moves

Every spacing value your S129 table counts under check G: the 194 off a step and the 148 hand typed, across the stylesheets named there. Margin, padding, gap, row-gap and column-gap. Nothing else: no size, colour, width, radius or layout change rides in this sweep.

- **A hand typed value already on a step** becomes its `--sp-*` token. Nothing on the page moves.
- **A value off a step** goes to the nearest step. An exact tie rounds **down**, the same as the type scale (DSRD 7 section 3.0).
- **Named values stay:** DSRD 7 section 5.1's button paddings, section 4.3's separator 48 and 32, section 4.5's registered widths and any value annotated with Kain's own ruling. Where an annotation is only near a value and is about a different property (your S129 finding 1), it does not protect the value.

## 2. Order

Kain's S129 order: the cards, the rest of the Knowledge Hub, the header and footer, About and its family, reviews and testimonials, help and the policy pages. One page design per change set.

## 3. What comes to Kain, and what does not (his S129 ruling, applied here by Chat)

Kain rules only what he can see. For every change set, run the computed style comparison of the real page before and after at 1440, 1024 and 375, which fails on anything moving other than spacing.

- **If no element's rendered position moves by more than 4px at any width:** ship it, and record the comparison. Do not show it to him.
- **If anything moves by more than 4px:** show him that page design's before and after in Safari, tabbed, one option on screen at a time in the same place, with only spacing changed. His yes ships it; his no leaves that value where it is with his words annotated beside it, which makes it a named exception.

## 4. Two things that ride along

1. **The gate's annotation test (your S129 finding 1).** Commissioned: tighten it so an annotation protects a value only when it names that value's property. Prove it with an acceptance case red on the five card sizes it wrongly passed and green on a correctly annotated value. Add it to the theme queue if you would rather run it in a theme session; either is fine.
2. **The footer** is not swept for spacing until its full review with Kain has run (his S129 words: "the footer is a complete mess and needs a full review"). Skip `footer.css` and say so in the change set's report.

## 5. Done when

`css_gate.py` check G passes on every stylesheet except the footer's, every visible move carries Kain's yes, and every value left off a step carries his words beside it.

## OWED BACK

One SHIP per page design (or one for several invisible ones), naming the counts moved, the comparison result, and any move put to Kain with his words.

*No em or en dashes in this file; checked before writing.*
