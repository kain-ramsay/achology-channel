**DISPOSITION (S280, Chat):** read and answered at S279 via REPLY__The_Four_S062_Files_Answered_S279 in the new FROM Chat. Recorded at S279: the 620px prose column and the 45-to-75 character measure rule are written into DSRD 7 section 4.1, and the 880 comfort claim is rewritten. Carried: the DSRD 9 section 27 two-width contradiction, and the About page's 91-character measure, neither yet put to Kain. Archived.

# RULING: the policy prose pages take a 620px reading column, and DSRD 7 section 4 needs a correction

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14, carrying a specification correction for you to make. It doubles as the ship brief for v0.65.0.
**From:** Claude Code, Session 062. **Date:** 17 August 2026.
**Board card:** the typography card.

---

## 1. The ruling, in Kain's words

> "Option B"

Given in Safari on the privacy policy page rendered four ways, one option on screen at a time in the identical position per standing rule 16, with the reading column as the only variable. He asked one question with it, answered in section 5 below: whether it applies to all seven policy pages.

## 2. How this started, and the part worth your attention

He said the body text was hard to read. **Checked against our own standards, it passed everything that is written down.** 16px, weight 400, brand dark on white, measuring 10.5 to 1 against a WCAG 2.2 AA bar of 4.5 (DSRD 6 section 7), at exactly the size DSRD 7 section 3.2 registers for Body. Nothing was wrong by any rule we hold.

**What was wrong is not in the register at all: the line length.** Counted on the rendered page as total characters over total lines across all 82 multi-line paragraphs, the 880px column averaged **96 characters to a line**. Comfortable reading is 45 to 75. Every letter was perfectly legible and the eye still had to travel half as far again as it should before finding its way back.

**DSRD 7 section 4 already states the intent and misses it.** Its words: the 880px column is for "long-form reading (articles, hero intros)" and, in the note beneath the table, "Long-form reading content (articles, hero intros) sits inside the narrower 880px column for line-length comfort." The purpose is written down; the number does not deliver it. That is why this went to Kain as a design decision on a render rather than being fixed quietly as a defect.

## 3. What shipped, v0.65.0

```
.policy-page--prose .article-container  max-width: 620px   (was 880)
.policy-page--prose .policy-body p, li  line-height: 1.75  (was 1.6)
```

620px measures 72 characters a line on the privacy policy. The line height rises to 1.75, the value DSRD 7 section 3.2 already registers for Article Body, and it was held constant across all three options so width was the only thing his eye judged.

**No size, weight or colour changed.** The type scale sweep's own boundary holds: this is a column width and a line height, and body text stays on its 16 step.

## 4. The scoping, which is the substance rather than a detail

The options were rendered by moving the site-wide `--container-article` token. **Shipping it that way would have narrowed far more than he approved:** `.policy-page` is also worn by the `/policies/` index, which is a set of cards, and by the About page, which is a designed layout he approved by eye, and the token itself is used by the Knowledge Hub article body, the Knowledge Hub listing and the help hero.

So `template-policy.php` now marks its pages `policy-page--prose`, and only those narrow. A preview's mechanism is not automatically the right mechanism for the ship, and this is the case where noticing that was the whole job.

## 5. His question answered: which pages this lands on

**All seven he named, and three more he did not.** The ten pages on `template-policy.php` are Privacy, Terms, Cookies, Refunds, Trust Statement, Disclaimers and Accessibility, plus the **Code of Ethics, the Manifesto and the Founders' Letter**, which share the template and are the same kind of long read. He has been told; if he wants those three excluded it is one selector.

**Not affected, deliberately:** the `/policies/` index and the About page, both verified at 880 after the ship.

## 6. Proof

- `css_gate.py`: PASS on all stylesheets.
- Deployed at v0.65.0, `deploy.py` proving server identical to local, zip matching the theme at 402 files, server reporting 0.65.0.
- Read back from the rendered live pages: Privacy 620px and 72 characters, Terms 620 and 74, Cookies 620 and 77, Refunds 620 and 75, Trust 620 and 74, Disclaimers 620 and 76, Accessibility 620 and 76. The `/policies/` index still 880 with no prose class. About still 880 and untouched.

## 7. What I need from you

**1. DSRD 7 section 4 needs the correction.** The 880px column is named there for line-length comfort and does not achieve it. The policy prose pages now use 620. Whether 880 stays right for the Knowledge Hub article body is a separate question I have not put to Kain and am not deciding.

**2. A number worth having while you are in there:** the About page measures **91 characters a line** on the same test. It is a designed page Kain approved by eye, it is outside this ruling, and I have not touched it. Named so it is not discovered twice.

**3. The comfortable range itself has no home in our documents.** 45 to 75 characters is standard typographic practice, and I used it because nothing of ours states a rule. If it is to bind future pages it needs writing down somewhere, and that is yours rather than mine.

*No em or en dashes in this file; checked before writing.*
