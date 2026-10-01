# Job 1: school colour on text, contrast sweep

Scope: `*.css`, `*.php`, `*.js` in the theme root (the `previews/` HTML mock-ups and the `tools/`, `harness/` Python scripts were not treated as theme output). Contrast ratios computed with the WCAG 2.x relative-luminance formula in a throwaway script (not committed). Nothing in the repo was edited.

## Summary

| Verdict | Rows | School/pair cases |
|---|---|---|
| already safe | 4 (F1, F2, F3, F5a) | 23 (7 + 7 + 7 + 2) |
| straight swap | 1 (F5b) | 5 |
| not a straight swap | 1 (F4), a judgement | 7 |
| cannot tell | 1 (F4: the background and the ratio, not the verdict) | 7 |

F4 is counted in two lines because its verdict is a judgement while its ratio cannot be computed from the code.

Headline: every place the theme paints a school colour on text for a reader already uses the text-safe `--school-<slug>-text` token and passes on white. Two cases need attention. F5b: `.btn-secondary--school:hover` puts white on the raw primary, and five of seven fail. No markup in the repo's PHP or JS uses that class, so it is latent. F4: the pricing bundle school name sits on a gradient wash of its own colour, which this repo's own comments say should never happen.

## Token table

Defined in `base.css:144-157` (primary, secondary), `base.css:175-181` (text), `base.css:184` (accent fallback). Per-school `--school-accent`, `--school-text` and `--school-accent-rgb` are set in `components.css:23-29` on `.school--<slug>`.

| School | `--school-X-primary` | `--school-X-secondary` | `--school-X-text` (resolved) | `--school-accent-rgb` |
|---|---|---|---|---|
| nlp | #4D7258 | #3B5C44 | #4D7258 (alias of primary, `base.css:175`) | 77, 114, 88 |
| cbp | #8E944E | #73793A | #747940 (`base.css:176`) | 142, 148, 78 |
| lc | #B8704A | #9A5B38 | #A66543 (`base.css:177`) | 184, 112, 74 |
| pc | #A8697A | #8E5465 | #A16575 (`base.css:178`) | 168, 105, 122 |
| miw | #7E6298 | #664D7E | #7E6298 (alias of primary, `base.css:179`) | 126, 98, 152 |
| mh | #6278B0 | #4C6092 | #5E73A9 (`base.css:180`) | 98, 120, 176 |
| pgd | #4A96A8 | #357A8C | #3E7E8D (`base.css:181`) | 74, 150, 168 |

- `--school-accent`: `base.css:184` defines it as `var(--color-dark)` = #354149, a fallback. On `.school--<slug>` (`components.css:23-29`) it resolves to that school's **primary** hex above. `--school-text` has no root definition, so outside a `.school--*` element it is undefined and the `var(--school-text, fallback)` fallbacks apply.
- The `--school-<slug>-secondary` tokens are defined but nothing in CSS, PHP or JS references them (searched all of the theme root). `tools/school_colour_contrast.py` only prints text-token names.
- Raw hex copies of school colours in code: `header.css:286-292` (the `rgba()` triplets of the primaries, as 12% tile washes behind images; the tiles contain only `<img>`, no text, so not text findings) and the hex in comments at `components.css:23-29`. No raw school hex paints text anywhere.
- Foreground contrast on white (#FFFFFF), computed:

| School | primary on white | text token on white | secondary on white | white on primary | white on text token |
|---|---|---|---|---|---|
| nlp | 5.44 | 5.44 | 7.50 | 5.44 | 5.44 |
| cbp | 3.23 | 4.61 | 4.64 | 3.23 | 4.61 |
| lc | 3.85 | 4.60 | 5.35 | 3.85 | 4.60 |
| pc | 4.23 | 4.53 | 5.82 | 4.23 | 4.53 |
| miw | 5.14 | 5.14 | 7.17 | 5.14 | 5.14 |
| mh | 4.35 | 4.67 | 6.18 | 4.35 | 4.67 |
| pgd | 3.38 | 4.59 | 4.87 | 3.38 | 4.59 |

## Findings

"Large text" = at least 24px, or at least 18.66px and bold. All sizes come from `--text-12/14/18` in `base.css:204-207` (12px, 14px, 16px, 18px).

| ID | Component / selector | File:line | Token or hex used | Background the text sits on | Size / weight | Large? | Contrast | Verdict |
|---|---|---|---|---|---|---|---|---|
| F1 | Course card school line `.card--course .card__school-line`; bundle card academy line `.card--bundle .card__academy-line`; bundle course hour pill `.card--bundle .card__hour-pill`; Access-All-Areas checklist course-count `.card--aaa .card__course-count-pill` | `cards.css:1162` (size/weight 1130-1131); `cards.css:1547` (1538-1539); `cards.css:1697` (1695-1696); `cards.css:2081` (2079-2080, 12px/600) | `var(--school-text)` per school (fallbacks: soft-grey #5E6B75 at 1162; brand orange at 1547 and 1697; dark #354149 at 2081, used only when no `.school--*` ancestor) | White: `.card-product` background `var(--color-white)` (`cards.css:874`); the info panels and checklist rows set no background; the pill rules set `background: transparent` (`cards.css:1698`, `2082`) | 12px / 600 | No | nlp 5.44, cbp 4.61, lc 4.60, pc 4.53, miw 5.14, mh 4.67, pgd 4.59 (fallbacks on white: soft-grey 5.47, dark 10.48, brand orange 3.16) | already safe (all seven pass 4.5) |
| F2 | Bundle card summary strip text `.card--bundle .card__summary-strip .strip-text` | `cards.css:1752` (1750-1751) | `var(--school-text)` per school | White: strip is `background: transparent` over the white card (`cards.css:1716`) | 12px / 500 | No | Same seven values as F1 | already safe |
| F3 | Course and bundle "learn more" button label on hover `.card--course .btn--learn-more:hover`, `.card--bundle .btn--learn-more:hover` (hover/fine-pointer only) | `cards.css:957-958` (fill) with label `color: var(--color-white)` from `cards.css:922` (hover rule); size/weight `cards.css:904-905` | White text on `var(--school-text)` fill | `var(--school-text)` (same rule) | 14px / 600 | No (14px bold is below 18.66px) | nlp 5.44, cbp 4.61, lc 4.60, pc 4.53, miw 5.14, mh 4.67, pgd 4.59 | already safe |
| F4 | Pricing bundle school name `.pricing-bundle__name`; underlined on hover/focus via `.pricing-bundle__headlink` (the underline takes `currentColor`, no separate declaration) | `pricing.css:912` (size/weight 909-910); wash at `pricing.css:1087-1090`; hover underline `pricing.css:1945-1949`, `1958-1961` | `var(--school-text)` per school | cannot tell from the code (the head's own background is a gradient of `rgba(var(--school-accent-rgb), a)` over white, `a` = 0.13 at the bottom, 0.07 at 35%, 0 at the top, `pricing.css:1087-1090`; the name's vertical position inside the gradient depends on the rendered head height) | 18px / 600 | No (18px is below 18.66px) | cannot tell from the code. Bounds only: at a = 0 (white) 5.44 / 4.61 / 4.60 / 4.53 / 5.14 / 4.67 / 4.59; at a = 0.07: 4.96 / 4.32 / 4.25 / 4.16 / 4.70 / 4.31 / 4.28; at a = 0.13: 4.59 / 4.05 / 3.96 / 3.90 / 4.35 / 3.99 / 4.00 (nlp, cbp, lc, pc, miw, mh, pgd) | not a straight swap. Judgement: the same file's comment (`pricing.css:1056`) says the wash is "at its faintest where the words are", but the code does not prove the name sits at a < 0.07, and `cards.css:1680-1690` records a rule that school-coloured text never sits on a tint of its own colour with no second darker token step. Resolving it is a design decision |
| F5a | `.btn-secondary--school:hover` label (defined, no use found in any PHP or JS in the repo) | `base.css:794-797`; size/weight from `.btn` `base.css:701-702` | White text on `var(--school-accent)` = the school primary | `var(--school-accent)` (same rule) | 14px / 600 | No | nlp 5.44, miw 5.14 | already safe |
| F5b | Same selector as F5a | `base.css:794-797` | White text on `var(--school-accent)` = the school primary | `var(--school-accent)` | 14px / 600 | No | cbp 3.23, lc 3.85, pc 4.23, mh 4.35, pgd 3.38 | straight swap (judgement): the existing `--school-<slug>-text` shade of each of these five is the same hue and gives 4.53 to 4.67 against white, and `cards.css:957-958` already does this for the other buttons; no other rule needs to change |

## Not text, recorded so they are not re-checked

- SVG icons that take `currentColor` from `--school-text`: `cards.css:1172` (`.card--course .card__school-line .icon-school`) and `cards.css:1569` (`.card--bundle .card__academy-line .icon-school`). They are 12px icons, not text elements.
- Tick circles and ticks using `--school-accent`: `cards.css:1648`, `1661`, `1733`, `1744`, `2040`, `2052`. Decorative marks.
- Fills, bars and borders using the school colour with no text on them: `base.css:791` (border), `cards.css:929`, `1112`, `1521`, `1918-1924` (stripe gradient), `pricing.css:902`, `3537`, `3814`, `3994`; `footer.php:62` and `footer.php:104` (inline `style="background:var(--school-<slug>-primary)"` on empty spans, `aria-hidden`).
- Header menu tiles `header.css:286-292` hold images only.
- `.btn-secondary--school` at rest (`base.css:788-792`) sets the label to `--color-dark`; only the border is school-coloured.
- Fallbacks: if `--school-text` were undefined, `cards.css:1547`, `1697`, `1752` fall back to brand orange #ED6922, which is 3.16 on white at 12px. Nothing in the repo shows these rules rendering without a `.school--*` ancestor (`commerce-cards.php:254`, `401`, `courses-setup.php:513` all add the class), so this is not scored.
- No JavaScript file in the theme root sets or reads a `--school-*` value or a school hex.
