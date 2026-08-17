**DISPOSITION (S280, Chat):** consumed at S279. This report drove the site-wide tint rule Kain ruled on the rendered cards, written into DSRD 7 section 2.1 with its second clause covering the hover finding. Its two open sites (the bundle card's hour pill and summary strip) were closed by the S279 bundle card corrections and travel in the bundle card brief. Archived.

# REPORT: the school colour text-safe sweep, every site found and its verdict

**DOCUMENT TYPE:** report, answering a commission.
**From:** Claude Code, Session 061. **Date:** 17 August 2026. **Theme:** v0.63.4 and v0.63.5, both deployed.
**Answers:** `COMMISSION__School_Colour_Text_Safe_Sweep_S277.md`.
**Board card:** "School Colour Text-Safe Sweep: Every School Colour Carrying Text Moves To Its AA Token" (Website Rebuild, Urgent and Important, Pre-Launch).

---

## The headline, before the detail

**Everything a visitor can see is now at AA.** Two sites moved, one live failure found and ruled on by Kain in the sitting, one exception recorded, and **two sites left open with the reason measured and written beside them in the code**. The two open ones are inside a component that renders on no page in the site, so they could not be ruled on and should not be closed by guesswork.

The card cannot honestly be marked Done. It can be marked done-except-two, and the two are small, named, and blocked on something that is not this sweep's to unblock. The commission's own words allow for this: "If the sweep genuinely cannot close in one sitting, that is a finding worth having, and it comes back through TO Chat with the reason and the measured size of the remainder."

## Job one: every site found

The theme was swept for `--school-accent`, `--school-{code}-primary`, `--school-{code}-secondary` and the hardcoded school hexes, on `color`, on SVG `stroke` and `fill`, and on anything else a reader reads. **178 school-colour references exist in the theme. Seven of them reach a text colour property.** Two were already on the token from S060; the other five are all in one component.

| Site | Component | Renders at | Ground | Verdict |
|---|---|---|---|---|
| `cards.css:1093` school line | Course card | Como 12px/600 | white card | **already moved**, S060 |
| `cards.css:1103` school icon | Course card | 12x12 mark | white card | **already moved**, S060 |
| `cards.css:1401` academy line | Bundle card | Como 12px/600 | white card | **MOVED**, v0.63.4 |
| `cards.css:1438` stats line | Bundle card | SS3 12.5px/400 | white card | **MOVED**, v0.63.4 |
| `cards.css:1496` hour pill | Bundle card | SS3 10.5px/600 | school colour at 10% | **OPEN**, see below |
| `cards.css:1529` summary strip | Bundle card | SS3 12.5px/500 | school colour at 8% | **OPEN**, see below |
| `cards.css:1480` checklist tick | Bundle card | 9px mark | inside a 12% circle | **exception**, decorative |

Checked and found not to be sites, so nobody re-checks them: the footer's seven school swatches and the header's seven navcard tiles are backgrounds behind no text; `.card--aaa` and `.card--membership` use no school colour at all; `.btn-secondary--school` carries `--color-dark` on its label at rest.

The tick at `cards.css:1480` is a ruled exception on DSRD 7 section 2.1's own words, "`--school-accent` for fills, bars and decorative marks", read from the canonical file this session.

## Job two: the straight swaps, applied

The academy line and the stats line, both on a white card, both carrying the failing primary. Five of the seven schools were under the bar there, from 3.23 to 4.35; the token clears all seven at 4.53 to 5.44. Applied at v0.63.4, `css_gate` PASS, deployed.

**Nothing visible changed, and that is a statement of fact rather than a hope.** See the finding below.

## The finding that shapes the rest: the bundle card renders nowhere

**No template in the theme emits `.card--bundle`.** It is a stylesheet with no live component. This is not a discovery so much as a confirmation: `page-cards.php` has been saying so on its own face since S255, under "Registered, but with no live component". S061 confirmed it two ways rather than trusting the code read: no template emits the class, and no published page in the live database contains it.

Two consequences, both material:

1. The two moved sites changed nothing anyone can see, so no approved appearance was touched.
2. **The two open sites cannot be ruled on.** Harness Rule 7 is explicit: "If a page cannot be rendered, the work waits until it can." Rendering the bundle card means building the bundle card, and both instruments refuse the shortcut for the same reason: `page-cards.php` is bound by its own commission to render every card "from its live component, never re-authored", and `variant_tabs.py` lifts real markup from a rendered page rather than authoring it. A card drawn by hand for a preview is not the card, and Kain would be ruling on my drawing. Building the component is a component build with its own review sitting, not a colour sweep's business.

## The two open sites, measured

Both carry their text on a tint **of their own school colour**. The seven text-safe tokens were derived against white, and they do not hold on a tinted ground, because a tint of the text's own colour lifts the ground toward the text and costs contrast on both sides at once.

| Site | Ground | Primary now | After the swap | Bar |
|---|---|---|---|---|
| Hour pill, 10.5px/600 | school colour at 10% | 2.93 to 4.77 | **4.03 to 4.77** | 4.5 |
| Summary strip, 12.5px/500 | school colour at 8% | 2.98 to 4.91 | **4.13 to 4.91** | 4.5 |

NLP and Mindfulness clear both grounds as drawn and need nothing. The other five clear neither, before or after.

**So the swap was not applied to them.** Applying it would have moved them from failing to still failing while making the code look swept, which is worse than leaving them visibly open: a site that looks compliant stops being looked at. Both rules now carry a comment naming the measurement and saying they are held for a ruling. The measuring instrument is in the repo at `tools/school_colour_contrast.py`, extended this session to measure against a stated ground rather than assuming white.

Settling them will need one of: a second darker step per school for use on tinted grounds (a new token set, and therefore a standard change that is Chat's and Kain's, not mine); dropping the tint so the existing token holds; or moving those two labels off the school colour entirely. All three are design decisions on a component Kain has never reviewed, which is why they belong to the bundle card's own sitting rather than to this sweep.

## What the sweep found that was live, and Kain ruled on it

Filed separately and in full as `RULING__Learn_More_Hover_Takes_The_Text_Safe_Fill_S061.md`, so this is the one line the harness asks for: hovering a course card's Learn More button filled it with the school primary behind a white label, failing on five of the seven schools on live pages. Kain ruled the corrected fill in Safari, it shipped at v0.63.5, and the fold-back wrote prototype v2 and the data file together in the same sitting.

**It is worth naming how nearly this was missed.** The commission asked for school colours landing on a text colour property, and this one never does: the colour is the fill and the label is white. Contrast does not care which of the two moved. The sweep found it only because the measurement was run on grounds as well as on text.

## Definition of done, line by line

| The card's words | State |
|---|---|
| Every site either moved or recorded as a ruled exception | **Five of seven.** Two moved, one exception, **two open**, both named with their measurements |
| The report lists every site found with its verdict | **Done**, the table above |
| `css_gate` passes | **PASS**, all 15 stylesheets, at both versions |
| The change is live in the theme and the version recorded | **Done.** v0.63.4 and v0.63.5, deployed, server and zip verified against local |

## What is asked of Chat

1. **Record the ruling** in DSRD 8 section 7, per the ruling file beside this one.
2. **DSRD 8 sections 8.4, 8.5, 8.6 and 8.10 are now out of step with the theme.** They specify the bundle card's academy line and stats in "school primary colour" and count six school colour touchpoints; two of those are now on the text-safe token and two are marked open. The theme is right and the document is stale, so this is Chat's correction to make, not mine to argue with.
3. **The two open sites want a home on the board.** They are not this card's remainder so much as the bundle card's inheritance, and they will be waiting the moment that component gets a sitting.
4. **One question, raised rather than assumed:** whether a tinted ground gets its own token step across the site, or whether the rule becomes that school-coloured text never sits on a tint of itself. The second is simpler and needs no new tokens. It is a standard, so it is Kain's through Chat.

*No em or en dashes in this file; checked before writing.*
