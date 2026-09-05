> **CHAT DISPOSITION, S343: ARCHIVED.** The fixed sentence is written into DSRD 9 section 32.3's standfirst row and its consequence into 32.9 item 1. The noun Achologist is recorded as a named exception to DSRD 6 section 1's front-door rule (Kain's yes, S343): the exception is this one sentence, not the word.

# RULING: Kain changes the plan; every book note's standfirst ends "Essential reading for all Achologists", whatever its rating

**From:** Claude Code, Session 102, relaying Kain. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed in chat, and he asked that Chat be told in these terms.
**His words, quoted exactly as typed:** *"For simplicity, just use Essential reading for all Achologists. Please let chat know that this is a change on what we planned for, but is now what i want."*
**Context he was answering:** after v0.167.19 and v0.167.20 the standfirst ended with one sentence per step of the rating scale ("Essential reading for all Achology members" on the eight Essential Reading notes, "Highly recommended reading for all Achology members" on thirty-six, "Recommended reading for all Achology members" on twenty-one), and Code told him so and offered the word if he wanted them read differently. This is that word.
**Shipped as** theme v0.167.21, commit `2ebb162`, `deploy.py` three proofs (server identical to local, zip 700 files matching the theme, server reporting 0.167.21), pushed, opened for him in Safari. Filed under Harness Rule 14.
**Board card:** Knowledge Hub page designs.

## What the page does now

Every one of the 65 live book notes ends its standfirst with the same sentence, in the standfirst's own type: **"Essential reading for all Achologists."** It is a fixed line and no longer reads the record's `achology_rating`. The badge (v0.167.18 and v0.167.19) still renders only on the top step, so the badge is now the rating's only visible mark on the page, on the eight Essential Reading notes; the fifty-seven Recommended and Highly Recommended notes show no rating at all, and say "Essential reading" in the sentence like the rest. The record field, the master column and the importer are untouched; the data is still there and still drives the badge.

## What this changes on the plan, said plainly because he asked for it to be

1. **DSRD 9 section 32.9 item 1** ("`achology_rating` renders in the hero as `Achology rating · {value}`, in the editorial scale's own words and never as stars", approved by Kain on the rendered page at S250) is superseded in every part but one. The label went at v0.167.17, the words per step went tonight, the ticks went at v0.167.19, and the stars stay on his badge. What survives is that the rating decides whether the badge appears. The item is yours to rewrite from his words above and the two RULING_AND_SHIP files for v0.167.18 and v0.167.19.
2. **The editorial scale's three steps are no longer distinguishable on fifty-seven pages.** The record carries them, the badge marks the top one, the page says nothing about the other two. If the scale is meant to be read anywhere on the site (a hub card, a list, a filter), that is a new decision, not one this ruling made; named so nothing is built on the assumption that the page still carries it.
3. **DSRD 9 section 32.3's standfirst row** gains the fixed last sentence, and "Achologists" is a word the copy standards may want to register (it is his, from tonight; `house-copy-standards` and DSRD 2 are yours to check for a ruling on the noun).

Nothing else on the page moved: the badge's position and sizes, the author line, the buttons and the hero's spacing are as at v0.167.19.

## Read back after the deploy

`a-guide-to-rational-living` (Essential Reading): standfirst ends "...building lasting emotional resilience. Essential reading for all Achologists." with the badge in the bottom right corner. `what-do-you-say-after-you-say-hello` (Highly Recommended): standfirst ends "...think, feel and behave. Essential reading for all Achologists." with no badge. Stylesheet served at ver 0.167.21.

OWED BACK: the section 32.9 item 1 rewrite and the section 32.3 rows, yours; a word on the noun "Achologists" if the copy standards have one. Nothing from Kain: this is his ruling, recorded.

*No em or en dashes in this file; checked before writing.*
