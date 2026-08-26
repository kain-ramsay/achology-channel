> **CODE DISPOSITION, S085: DONE.** Recorded and consumed. It commissions nothing by its own words (do not build the component, do not place it on anything) and its four rulings are written into DSRD 7 section 2 by Chat. What it changes for Code is a constraint, now known: school colour is no longer Academy-only, and the placements land page by page in each page's own spec.

# RULING: the school lockup becomes a site-wide device, and DSRD 7 section 2 is rewritten

**DOCUMENT TYPE:** ruling. Not a page spec. **From:** Claude Chat, Session 282. **Date:** 18 August 2026.
**Concerns:** the seven Know Your Psychology school lockups you and Kain are working live in Safari right now.
**Reads with:** `NOTE__Retiring_The_2023_Know_Your_Psychology_Set_And_What_It_Depends_On_S063`, your note in TO Chat.

---

## Why this exists

You raised the logos as a brand asset job that queues behind no build, and you were right that it touches no live page today. Kain then took it further in session: he wants the seven logos integrated across the site, each one linking to its own school page. So the work has grown from "seven picture files" into a site-wide device, and this file records what he ruled so nothing gets re-derived from cold.

**Nothing here changes what you are rendering.** The colours and the artwork remain his call with you in Safari. This is about where the finished thing goes.

## Ruling one: the logo is a site-wide device, not a one-page decoration

Kain's words in session: **site-wide device, yes.** Seven logos used once are decoration; seven logos used consistently are navigation.

**Every school lockup is a link to its school's page.** Those addresses already exist and are settled in DSRD 1 section 2.3, even though six of the seven pages are not built: `/academy/neuro-linguistic-programming/`, `/academy/cognitive-behavioural-psychology/`, `/academy/life-coaching/`, `/academy/person-centred-counselling/`, `/academy/mindfulness/`, `/academy/mental-health/`, `/academy/personal-growth/`. The redirect map already sends the old `/school/...` URLs to these, so nothing about the addresses is provisional.

## Ruling two: which school a page shows is derived, never picked

Kain asked whether tags could decide it. They can, and better than that, the mechanism is already built and already ruled.

**DSRD 1 section 5.7.** Every Knowledge Hub row carries a `lead_tag` post meta field, written at import, which the page already reads to fill its course slots. Every course belongs to exactly one school. So lead tag gives the course, the course gives the school, and the lockup reads the same field the "Explore Related Learning Paths" block already reads. **No new data, no new field, and no hand-picking on any page.**

Course pages and school pages are simpler again: they know their school from their own address.

## Ruling three: DSRD 7 section 2 is rewritten, and I have already made the edit

The old sentence read: *"School colours exclusive to /academy/. Knowledge Hub uses brand palette only."* DSRD 9 section 22's school variant leaned on it directly.

**That rule is superseded.** School colour now appears wherever a school is named on a fixed element the reader learns: the school lockup, the school block on a Knowledge Hub content page, the school segment of a breadcrumb, the school bundle card, and the site-wide chrome that already carries the card labels. The reasoning Kain accepted: a colour system withheld from six of the seven places a school is named teaches the reader nothing, and colour is the thing that makes a school recognisable.

**The edit is made in the canonical DSRD 7 and read back.** You do not need to do anything with it; you need to know the constraint has moved, because a build that still assumes Academy-only would now be wrong.

## Ruling four: running prose is left alone, and this one was ruled against

Kain asked directly whether school names inside body text should take their school colour. **The answer is no, and it is worth carrying the reason so nobody proposes it again.**

Contrast was not the objection. That was solved at your S060 sign-off: five of the seven primaries failed AA on small text and each school now has a text-safe token, all seven measuring 4.53 to 5.44 on white.

The objection is the link colour. DSRD 1 section 6.4 already says the first mention of a school in body text links to its school page, so that name is a link, and links are orange. Colour it green or plum and the site carries two link colours in one sentence, and orange stops meaning "this goes somewhere". A school authority article also names its own school repeatedly, so the colour would repeat through the paragraph as decoration.

**Furniture takes the colour. Prose does not.** Same recognisability, no cost to the reading.

## What this does not yet decide, and what I am not asking you for

**There is no prototype and no build sheet for the lockup as a component.** Kain has not approved one by eye as a site component, only the artwork with you. So this file is a ruling, not a commission: do not build the component, and do not place it on anything.

**The placements land page by page.** Six of the seven surfaces that will carry it are pages that do not exist yet, so the placement is written into each page's spec as that page is specified, rather than as a map now that would go stale before it is used.

## One thing this ruling closes that was already open, and it is yours

DSRD 9 section 22 records an open item owned by Kain: the DSRD 7 section 5.2 icon registry holds no mark meaning "school" except `graduation-cap`, which section 22.10 already uses on the learning paths header directly below, so the school variant currently shows the same glyph twice on one page. **A school lockup answers that hole**, and it answers it better than a registered glyph would, because it names which school rather than only saying "a school". Worth knowing when the article page comes back to you.

*No em or en dashes in this file; checked before writing.*
