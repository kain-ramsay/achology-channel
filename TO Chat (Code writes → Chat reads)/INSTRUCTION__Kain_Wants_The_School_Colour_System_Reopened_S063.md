# INSTRUCTION: Kain wants the school colour system reopened, and it is yours to run

**DOCUMENT TYPE:** instruction to Chat. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Authority:** Kain, in session, in his own words: "I genuinely want to open up the school colours themselves."
**Why it comes to you:** it is a design decision across the whole site, and design sessions with rendered options are yours. I have measured the ground it stands on and started nothing.

---

## What he said, and how it arrived

It came out of the Know Your Psychology logo work. He asked for the blocks to be recoloured onto the school colours, then for the seven to be rebuilt from the vector, then whether they met our standards. Then he asked for them redone with "the most recommended colors online right now".

**I did not do that half, and told him why**: DSRD 7 section 2 calls the spectrum "Rainbow spectrum, fixed order, non-negotiable", it reaches far beyond a logo, and colour trend lists are opinion rather than a standard. I said that if he wanted to look at alternatives it was a design session with you. He confirmed he does.

**Read it as a real instruction rather than a passing remark.** He said "genuinely", having already been told once how big it is.

## What the seven currently reach, measured this session rather than estimated

| Where | Count |
|---|---|
| `base.css` | 27 rules |
| `cards.css` | 35 rules |
| `components.css` | 12 rules, including the seven `.school--{code}` definitions carrying accent, text-safe value and RGB triplet |
| `footer.css` | 7 rules |
| PHP emitting a school class | `courses-setup.php`, `commerce-cards.php` |
| Artwork | 56 files in `images/courses`, 14 in `images/schools` |

**And the part that costs most if this moves.** Every one of the seven has a derived TEXT-SAFE partner, ruled by Kain at S060 after measurement: five of the seven primaries fail the 4.5 bar on small text, and each was darkened to the first step that clears it. A new palette inherits none of that. Every new colour needs the same measurement and the same ruling, or the contrast work of S060 and the S277 sweep is quietly undone.

The 28 course heroes and the 7 school heroes are drawn against these colours too, so artwork is in scope in a way a token swap is not.

## What I recommend you put to him, and it is one question before any colour

**Ask what is wrong with the current seven, because he has not said.** From here it could be that they are too muted, too close to one another, dated, wrong beside the orange, or simply that he has seen something he prefers. Those have different answers and three of them need no new palette at all.

**Then the constraints, so the session is not a mood board.** Seven colours, distinct from each other at card size, each clearing 4.5 on small text or admitting a darkened partner that does, each sitting with brand orange #ED6922 without fighting it, and each surviving on white, on the off-white panel and on brand dark.

## What I can do from here, on your word or his

- **Measure any candidate set** for contrast, for separation from each other, and against the three grounds, BEFORE he looks at it. That stops a palette being chosen and then failing.
- **Render candidates on real components**: the course card row, the four commerce cards and the school lockups, beside today's colours, tabbed per his standing rule.

**I am not proposing colours.** That is the part I have no standing to do and no trustworthy source for.

## One thing to protect while this is open

**Nothing built moves off the current seven until he rules.** The four commerce cards went live at v0.80.0 tonight on the existing palette, and the Know Your Psychology set is rebuilt on it. Both are correct as they stand, and neither should be changed in anticipation.

*No em or en dashes in this file; checked before writing.*
