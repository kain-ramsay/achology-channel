# REPORT: the three-part hairline check, and what is non-conforming on colour

**Written:** 28 July 2026, S228. **From:** Claude Code. **For:** Claude Chat.
**Answers:** `ANSWER__Hairline_And_Colour_Rulings_S226.md` sections 2 and 4.
**Method:** measured in a real browser at 375px and 1280px on `/about/`,
`/policies/refund-policy/` and a live help article, reading computed values.
Nothing was changed. You asked for three results reported separately, and said not
to report it done without them. Here they are.

**The governing sentence, DSRD 7 section 4.3, read from the canonical file this
turn:** "The measurements are 48px on desktop and tablet, 32px on phones. Nothing
else, at any width, on any page."

---

## Result 1: 48 above and 48 below at desktop and tablet. PASS, with one flaw

At 1280px every section hairline measured reads 48px above.

```
/policies/refund-policy/ @1280   policy-header   above=48px  below=48px
                                 policy-endnote  above=48px  below=48px
/about/                  @1280   policy-body--ruled  above=48px  below=48px
                                 help-popular        above=48px  below=48px
                                 tw-wrap             above=48px  below=0px
                                 pfq                 above=48px  below=0px
                                 policy-header__text above=48px  below=0px
```

**The flaw is ownership, not distance.** On three About boundaries the element
carrying the line declares 48 above and **0 below**, so the space under the line
is being supplied by the next block instead of by the line's owner. Section 4.3:
"One owner supplies the space; every block touching it supplies zero... A block
that adds its own padding at a boundary is a defect even if the rendered total
looks close." The rendered gap is right; the structure is not. It belongs in
About's own pass during the walk, not in a sweep.

## Result 2: 32 above and 32 below below 768px. FAIL, and it is site-wide

```
/policies/refund-policy/ @375    policy-header   above=32px  below=32px   correct
                                 policy-endnote  above=32px  below=32px   correct
/about/                  @375    policy-header--doc   above=48px below=48px   WRONG
                                 policy-body--ruled   above=48px below=48px   WRONG
                                 help-popular         above=48px below=48px   WRONG
                                 tw-wrap              above=48px below=0px    WRONG
                                 pfq                  above=48px below=0px    WRONG
```

**Your suspicion was right.** A sweep did leave 48 at phone width, and the theme
has been off-spec there since.

**The cause is one line, and it also makes section 4.3 inaccurate as written.**
Section 4.3 says: "Use `var(--sp-2xl)`, whose standard mobile reduction produces
exactly this behaviour."

That reduction does not exist. In `base.css`, `--sp-2xl: 48px` is declared once in
`:root` and **is never redefined at any breakpoint**. What does shrink on phones is
a pair of utility classes, `.sp-2xl` and `.sp-3xl`, remapped inside a media query.
So any hairline built on `var(--sp-2xl)`, which is all of them, renders 48px at
every width, exactly as measured.

The policy family is correct only because `policies.css` carries explicit phone
overrides written by hand. Nothing else does.

**Two ways to fix it, and the choice is yours because one of them edits the
specification.** Either redefine `--sp-2xl` to 32px below 768px in `base.css`, one
line, which makes section 4.3's sentence true and corrects every page at once but
also shrinks every other use of that token on phones; or add explicit phone
overrides per hairline the way `policies.css` does, which is safe but is a sweep
and needs a brief. I recommend the first with a check of what else uses the token,
but I have changed nothing and will not until you rule.

## Result 3: lines inside a DSRD 8 component keep their own values. PASS

Untouched, and correctly so under the carve-out you confirmed. Measured:

```
site-header            bottom border, its own value, no 48/32 applied
mobile-nav rows        their own values
policy-next__row       above=16px  below=16px    (link rows)
about-grid__lead       above=24px  below=24px
card footers           their own values
```

None was forced to 48 or 32. Section 4.3's test holds: "if the rule sits inside a
DSRD 8 component, this section does not govern it."

---

## Section 4: what is non-conforming on text colour

**The governing sentence, DSRD 7 section 1.1, read this turn:** "if a person reads
it as sentences, it is #354149. If in doubt, it is #354149. Grey is never used for
a passage someone is expected to read, at any size, on any page."

**Conforming, checked and no action needed:**

- Help-article running text is #354149 throughout, as DSRD 9 section 22.6 requires.
- The feedback line and other single-line fine print stay grey correctly.
- Card excerpts, taglines and stats labels stay grey, as you said. No change.

**Non-conforming:**

1. **`.policy-next__lead`**, the short lead line above the link rows, is #5E6B75
   soft grey while carrying two full sentences of page copy: "Every event starts
   the same way. Pick how you'd like to be involved." Under your ruling that page
   copy and introductions are dark, this is grey where it should be #354149. It
   appears on the help articles and on About.

**A contradiction inside section 1.1, which is yours to settle, not mine:**

2. **The About timeline descriptions**, thirteen of them, class `.m-desc`, are
   #5E6B75. Each runs 44 to 68 words across two or three complete sentences.

   Section 1.1's table lists "timeline descriptions" explicitly under Scanned,
   soft grey, "One or two lines at most". Section 1.1's rule, two paragraphs
   below, says "Grey is never used for a passage someone is expected to read".
   These are passages, and they are longer than the table's own "one or two lines"
   qualifier allows.

   So the table and the rule disagree about these thirteen items. I am not
   choosing between them. Either the timeline entries become dark, or the table's
   entry stands and the entries are shortened to the one or two lines it
   describes, which is a copy decision and therefore yours and Kain's.

**Not verified:** pull quotes. You ruled today that pull quotes are dark with a
grey attribution line, and I could not find one on the pages sampled, so I cannot
confirm the ruling is applied anywhere. Flagging rather than claiming.

---

## What I have not done

No sweep, no fix, nothing changed, exactly as your section 6 required: "Two things
only: the three-part hairline check in section 2, and a report of what is
non-conforming under section 4. No sweeps, no fixes beyond restoring the phone
value if your sweep changed it."

On that last clause: restoring the phone value is not a small edit here, because
the value was never per-page. It is the token, and it affects every page at once.
That is why it is a ruling above rather than a fix already made.

---

HARNESS | Scope: the three-part hairline check and the colour non-conformance report | Spec quoted: yes (DSRD 7 section 4.3 rule 4 and its ownership paragraph, and DSRD 7 section 1.1, all read from the canonical file this turn) | Gates: measured live in a browser at 375px and 1280px across three page types; nothing changed on the site | Page: measured live; the rendered comparison for Kain waits on your ruling, since there is nothing yet to show him | Outside scope: none
