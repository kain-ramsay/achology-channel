> **DISPOSITION, S270 (Chat), 12 Aug 2026.** Superseded by the ruling filed beside it: Kain approved the nine step scale in Safari the same session this proposed it. Kept for the method record (the candidate scoring, and the honest note on the first scoring run rewarding no change). Archived.

# PROPOSAL: a nine step type scale, chosen from the evidence, shown to Kain on a real page

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Follows:** `REPORT__The_Typography_Census_S056.md`.
**Authority for producing it:** Kain, in session, after seeing the specimen page. His words: "I don't have any experience in this whatsoever. So I really need to trust you to steer my thinking and instruct me in this."
**Status: a proposal, rendered and waiting on his eye. Nothing in the theme is changed.**

---

## 1. Why this exists, and the honest bit first

The specimen page did what it was built to do: it proved what is there. **It was the wrong thing to ask Kain to decide from.** Nobody rules wisely on 122 rows, and he said so plainly. This is the decision aid that should have followed it: one page, twice, and one question.

**The commission expected the scale to be designed with him next session against real numbers.** That still holds; this does not pre-empt it. What it does is give him something to react to, which is how he works, rather than a blank page.

## 2. The proposed scale

**12px, 14px, 16px, 18px, 21px, 24px, 28px, 33px, 42px.**

Nine steps. Every size on the site moves to its nearest step, and **nothing may sit between steps**, which is the entire point: with no 15px step, nothing can quietly become 15px because one card needed it.

**Two sets of exceptions, both deliberate.** The odometer digits and the policy index watermark, everything above 48px, stay off the scale as named graphic exceptions. Forcing a 104px rolling digit onto a text scale would be silly, and the watermark's eight hand-tuned sizes exist to make different words fill the same space.

## 3. How it was chosen, and how the choosing was checked

Six candidate scales were scored against **what the theme actually declares**, weighted by how many declarations use each size. Four were textbook modular scales at ratios of 1.125, 1.15, 1.2 and 1.25; two were drawn by hand from where the declarations cluster.

**The first scoring run was wrong and produced a nonsense answer.** It rewarded "moves the site least", which a scale that changes nothing wins trivially. Its top candidate was a twelve step list including 10, 11, 12, 13 and 14 as separate steps, which is not a scale at all, it is the present sprawl with a name on it. A second candidate scored well while capping the site at 33px, which would have silently shrunk the 42px hero.

**So two rules were added that a list of numbers must pass before it is scored at all:**

1. **No two steps closer than eight percent**, because two steps a pixel apart solve nothing: a designer can still land on either.
2. **It must reach 42px**, so the largest real heading has a step rather than being capped.

One candidate is now rejected before scoring, and the results are honest. This is recorded because a metric that rewards doing nothing is the same failure as a test that cannot go red.

| Scale | Steps | Unchanged | Within 1px | Moves more than 1px |
|---|---|---|---|---|
| 1.15 from 16 | 13 | 55% | 97% | 10 declarations |
| minor third, 1.2 from 16 | 10 | 36% | 97% | 9 |
| major third, 1.25 from 16 | 9 | 29% | 91% | 27 |
| clustered from usage | 9 | 51% | 94% | 19 |
| **anchored on what is used most** | **9** | **46%** | **96%** | **12** |
| major second, 1.125 from 16 | 14 | 60% | 99% | **rejected, 13px and 14px too close** |

**The proposed scale is the anchored one**, and it is recommended over the marginally better fitting 1.15 scale because it does the same work in nine steps rather than thirteen. A scale nobody can hold in their head is a scale nobody follows.

**It is anchored on the four sizes the site uses most**, so 16px body text, 14px small text, 12px captions and the 42px hero **do not move at all**. Of 307 text declarations, 140 are already on the scale, 155 move by a pixel or less, and **12 move more than that**. Those 12 are the only places where a real decision is being made, and they are what Kain is actually looking at.

## 4. What he has been shown

**The link:** `https://achologytest.com/wp-content/themes/achology/previews/type-scale-comparison.html`

The privacy policy page, twice, side by side. Left is the live page exactly as it is. Right is the same page with one extra stylesheet appended that snaps every font size to its step. **Colour, spacing, weight and layout are untouched**, so anything he notices is the thing being judged and nothing else.

Measured rather than asserted: on the right hand page the title moves 32px to 33px, the lead paragraph 19px to 18px, and the footer headings 11px to 12px. **Body text and section headings do not move at all.** Read back from the rendered pages with `getComputedStyle`, not from the stylesheet.

**The question put to him is one question:** does the right hand page read better, worse, or the same?

## 5. What happens on each answer

**If he prefers it, or cannot tell the difference:** that is a pass. The scale becomes the standard, DSRD 7 section 3 is rebuilt by Chat as a scale rather than a list of 50 remembered styles, the nine values move into named tokens, and the theme is swept onto it **one page at a time with this same before-and-after each time**, under a signed sweep brief. Then the stylesheet gate enforces it, and a stray size fails before it ships rather than turning up in a census a year later.

**If he does not like it:** the scale is adjusted and re-rendered. Nothing is committed until he has seen a real page he is happy with.

## 6. The one question underneath, which is genuinely his

**13px and 14px are both heavily used, 45 and 47 declarations, and one of them has to go.** That single pair is the sprawl in miniature and no measurement can settle it: it is a judgement about whether those two are doing the same job. The proposed scale keeps 14 and folds 13 into it. If his eye says the opposite, the scale flips to keep 13 and the arithmetic is no worse.

## 7. What this does not do

**Nothing is changed.** The override stylesheet exists only in the previews folder, which `deploy.py` excludes from every deploy, and it is loaded only by the comparison page. The theme's own stylesheets are untouched.

**No sweep has started**, and none will without a signed brief, because it touches every page.

*No em or en dashes in this file; checked before writing.*
