> **DISPOSITION, S270 (Chat), 12 Aug 2026.** The ruling is recorded on the typography board card and executed: the signed sweep brief (BRIEF__Type_Scale_Sweep_S270.md) is in FROM Chat. The scale's permanent home is DSRD 7 section 3, whose rebuild around it is queued to Chat and named in the S270 handover; DSRD 8's record lands with that rebuild. Archived.

# RULING: Kain approved the nine step type scale, on the rendered page

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Filed under Harness Rule 14**, which requires a ruling given in session to be filed the same session, quoting his words.
**Answers:** `PROPOSAL__The_Type_Scale_S056.md` and part 2 of `COMMISSION__The_Typography_Census_And_Its_Specimen_Page_S267.md`.

---

## 1. The ruling, in Kain's words

> "I think the right-hand one reads better (on your proposed scale)"

Given after opening the before-and-after comparison in Safari: the privacy policy page as it is today beside the same page with every type size snapped to the proposed scale.

**This is a Safari ruling on a rendered page**, the standard this project requires for anything judged by eye. It is not a ruling on a table of numbers.

## 2. What is approved

**The scale: 12px, 14px, 16px, 18px, 21px, 24px, 28px, 33px, 42px.**

Nine steps. Every text size on the site moves to its nearest step, and nothing may sit between steps.

**Two named exception sets, approved as part of the same render:** everything above 48px stays off the scale. That is the odometer digits and the eight hand tuned policy index watermark sizes, which are moving graphics and space fillers rather than text.

**The 13px against 14px question is settled by this ruling.** It was the one judgement no measurement could make, both being used almost equally, 45 declarations against 47. The page he approved is the one that **keeps 14px and folds 13px into it**. He was told before looking that his eye would decide it and that I would flip the scale if he disagreed. He did not.

## 3. The approved artefact, and where it is

Per the S258 fold-back, the rendered thing that was approved is recorded rather than only the ruling:

| File | What it is |
|---|---|
| `previews/type-scale-comparison.html` | The two column comparison he ruled from |
| `previews/type-scale-before.html` | The live page as it was |
| `previews/type-scale-after.html` | The approved state |
| `previews/type-scale-override.css` | The generated stylesheet that produced it, 167 declarations snapped |
| `previews/type-specimen.html` | The census specimen the scale was drawn from |

All are in the theme repository and version controlled. They are in `previews/`, which `deploy.py` excludes from every deploy, so they cannot leak into the theme by accident and are not disturbed by a deploy.

**Typography is a design foundation rather than a component**, so there is no component design folder to export a prototype into and no build sheet to update. Its home is DSRD 7 section 3, which is Chat's to write and never mine.

## 4. What this now needs from Chat

**1. Rebuild DSRD 7 section 3 as a scale rather than a list.** It currently registers 50 remembered styles; the theme declares 122. The nine approved steps replace the list of sizes, and each registered style names its step instead of carrying a loose number. The two exception sets are recorded by name.

**2. Decide where the weight rule goes**, because it does not exist anywhere and Kain asked for it. The census found five weights, and **108 declarations that set no weight at all**, nearly half the total, inheriting whatever they land in. That is a separate ruling from this one and has not been put to him.

**3. The responsive rule is still open.** 28 of the 32 real sizes are identical on a phone and a desktop. The register only states responsive behaviour for four styles. This ruling does not touch it.

## 5. What I am NOT doing, and why

**No sweep has started and none will without a signed brief.**

Harness Rule 3: a sweep runs only under a signed sweep brief from Kain arrived through FROM Chat, naming the bodies of work it covers, and there is no other route. **His approval of the scale is not that brief**, and I am not treating it as one even though he is the person whose signature it would carry. Moving 167 declarations across sixteen stylesheets touches every page on the site.

**What the brief needs to name**, so it can be written without another round trip: that the sweep runs one page at a time; that each page returns the same before-and-after comparison for his eye before it ships; that the nine values move into named tokens as part of it, because only three type values in the whole theme currently go through a token and a scale cannot be enforced through tokens that do not exist; and that the stylesheet gate gains its check only once the sweep is complete, since a gate against the current state would fail on everything.

**Nothing in the theme has changed.** The override exists only in the previews folder and is loaded only by the comparison page.

*No em or en dashes in this file; checked before writing.*
