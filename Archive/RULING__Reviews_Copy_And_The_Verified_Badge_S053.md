# RULING: Kain's Reviews page copy, locked, and one question back on a verified badge

**From:** Claude Code, Session 053. **Date:** 2026-08-10.
**Authority:** Kain, directly in session. Filed the same session per Harness Rule 14.
**Live:** theme v0.52.2, https://achologytest.com/reviews/

## 1. The archive's heading and supporting line, his words

- **h2:** The Complete **Achology** Reviews Archive
- **Lead:** Search our reviews, filter them down, and see what learners have said about their learning experience with Achology.

The heading carries the accent because it contains the word. DSRD 7 section 3, quoted from the canonical file this turn: "Wherever the word 'Achology' appears inside a heading, anywhere on the site, it is rendered in brand orange, wrapped in `<span class="policy-next__accent">`. No exceptions, no per-page judgement. This applies to headings only; body copy renders the word in the running text colour." So the h2 wraps it and the paragraph beneath deliberately does not.

## 2. The control bar's hint line, his words

**Search for terms a student might have used in their review (such as knowledge, theory, insight, self improvement, learning etc).**

Also ruled: it sits inside the grey bar rather than under it, as the bar's own last row, at 11px with 16px of air above it.

**With these three, every copy slot on the Reviews page is settled and no draft copy remains anywhere on it.** The `data-rv-draft` marker, which existed so unapproved copy could be found mechanically, now matches nothing on the page.

## 3. The four Global Impact figure labels, locked by him

| Figure | Label |
|---|---|
| 4,517 | **Verified Reviews** |
| 4.66 | **Average Rating** |
| 695,578 | **Number of Students** |
| 216 | **Countries** |

They replace the lowercase lines the block was built with. His capitalisation stands as typed; the label carries no text-transform, so nothing in the CSS is fighting it.

**The figures themselves are untouched**, per his standing S052 ruling: "do NOT update... once the site is live, we can sporadically do number updates, but definitely not now."

## 4. A question back: the verified badge needs a registered slot, and that is Chat's

Kain asked whether a verified badge could sit before each reviewer's name on the card. **There is no such mark in the system, and the two obvious candidates are both already spoken for.** DSRD 7 section 5.2 registers `BadgeCheck` to Certification and `ShieldCheck` to accreditation and the money-back guarantee. Putting either beside a reviewer's name would make one mark carry two meanings on the same site, which is exactly the drift the registry exists to prevent.

The same section requires a slot to be registered before it appears, and that registration is Chat's to write with Kain's approval, not Code's to take. **So this is a question, not a delivery.**

**Two options are rendered on the live page for his eye**, per the S258 render standard, on the same real cards with one variable changed:

- **a**, https://achologytest.com/reviews/?rv_badge=a: a mark before the name, 14px, brand orange, carrying "Verified student review" for screen readers. **The glyph is a stand-in**, the registry's plain circle-check, borrowed only so the idea can be seen. It is not a proposal that circle-check should mean this.
- **b**, https://achologytest.com/reviews/?rv_badge=b: the word Verified after the name, in the site's overline treatment (Como 11px/600 uppercase) and the AA-safe orange, since at 11px it is small text.

**What Chat is asked for, if Kain wants the badge at all:** a registered glyph for "verified reviewer" in DSRD 7 section 5.2, distinct from the certification and accreditation marks.

**The claim itself is already the site's**, so nothing new is being asserted: DSRD 1 section 2.1 names this page the "verified student reviews library".

**One cost to note.** The review card was signed as v1 this session. A badge on it lands as v2 with its prototype re-exported and its build sheet updated, which is small but real and would be done in the same session as his ruling.

*No em or en dashes in this file; checked before writing.*
