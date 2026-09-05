# COMMISSION: the typography census, rendered as one specimen page for Kain's eye

**DOCUMENT TYPE:** not a page spec. This is a commission.
**From:** Claude Chat, Session 267. **Date:** 2026-08-12.
**Authority:** Kain, in session at the close of S267. He asked whether font weights and heading rules had ever been established, and whether you are following any. The rules exist and he had not seen them. What does not exist is any check that the theme obeys them.
**Same method as the component census, deliberately.** That worked, and the reason it worked is that the code counted itself.

## The problem, stated once

DSRD 7 section 3 registers **48 named type styles**: 24 in Como, 24 in Source Sans 3, each with its size, weight and usage. Kain ruled many of them himself by eye. **Nothing anywhere has ever compared that list against what the theme actually declares.**

That is the identical shape to the component census, which found 304 class families where the document named 42. The expectation here is the same: more values live in the stylesheets than are registered, and nobody knows the number.

**And the registered set itself is a list rather than a system.** The sizes run 42, 36, 32, 30, 28, 26, 24, 20, 19, 18, 17, 16, 15, 14, 13, 12.5, 12, 11, 10.5. Twelve and a half and ten and a half are not steps on a scale; they are values that arrived because one card needed them. Five weights are in use with no rule anywhere saying what any of them means. Most rows carry no line height. Almost none states its behaviour below 768px. Those four gaps are what Kain rules on once he can see the truth.

**This commission does not fix any of that.** It measures, and it renders the measurement for his eye. The scale, the weight rule, the line height bands and the responsive rule are designed with him next session, against real numbers.

## Part 1: the count

**Harvest from the theme's own stylesheets, not from any document.** Every `font-size`, `font-weight` and `line-height` actually declared, wherever it is declared, including inside media queries and inline in templates if any exist there.

For each distinct value, return:

1. **The value itself.**
2. **How many declarations use it**, and in which stylesheets.
3. **Which class families carry it**, so it can be traced to something on the site.
4. **Whether it matches a registered style in DSRD 7 section 3**, and which one. Match on the whole style, size and weight and line height together, not on size alone: a registered 17px at weight 600 and an unregistered 17px at weight 500 are two different things and must not collapse into one row.
5. **Whether it appears only inside a media query**, which is how the responsive gap becomes visible.

**Report the totals plainly:** distinct sizes, distinct weights, distinct line heights, how many of each are registered, and how many are not.

**One warning from your own census experience:** a value written by a variable rather than typed literally still counts, and a value that resolves through a token should be reported as the token and its resolved value together, so a size does not hide inside a name.

**And the same honesty that made the component census useful:** where you cannot trace a value to a class family, print that it could not be traced rather than leaving the row looking complete.

## Part 2: the specimen page, rendered for Kain

**The count alone is not the deliverable.** Kain rules typography by looking at it, so the count becomes one rendered page he can open in Safari.

**What it shows.** Every distinct type style the theme actually uses, shown once, set in real Achology words at the size it is genuinely used at, not in filler. A heading style shows a real heading from a real page. Body shows a real paragraph. A card title shows a real card title. Never sample text nobody decided.

**How it is organised.** Two sections, and the split is the whole point:

- **Registered.** Styles that match DSRD 7 section 3, each labelled with its registered name.
- **Not registered.** Everything else, each labelled with where it renders and how many declarations use it.

Inside each section, order by size, largest first, so near-duplicates land next to each other. **That adjacency is what lets Kain see in one look that two styles two pixels apart are doing the same job**, which is the same trick that made grouping the 304 families answerable.

**Three widths in the one file**, desktop, tablet and phone, so a style with no responsive behaviour shows that by being identical in all three.

**Label each specimen with its actual numbers**, size, weight and line height, small and quiet, beside the sample rather than instead of it.

**Return it as a live page link** he can open in Safari, per Rule 7, alongside the count.

## What Kain rules from it, so you know what the page has to make visible

1. **Which unregistered styles earn a place**, and which are accidents to be removed.
2. **Which registered styles are duplicates of each other** pretending to be different jobs.
3. **What each weight means on this site**, which is the rule that has never existed and the one he asked for by name.
4. **What happens on a phone**, for the styles that currently say nothing.

The page does not have to answer any of those. It has to make each of them obvious to look at.

## What comes after, so the shape is clear

Once he rules, DSRD 7 section 3 is rebuilt as a scale rather than a list, and then **the check becomes mechanical, which is the actual point of all of this**: every font size and weight declared in the theme must match a registered value, and anything else fails in your stylesheet gate rather than shipping. That is the same closure as the build against sheet gate and it is not commissioned yet, because a gate against a list this loose would fail on everything.

## What this is not

**Not a redesign.** Nothing changes on any page. No value is corrected, removed or unified in this commission. If a style is plainly wrong you name it and leave it.

**Not your judgement on what should go.** You measure and you render. He decides.

*No em or en dashes in this file; checked before writing.*
