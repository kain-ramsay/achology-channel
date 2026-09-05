# FROM Chat: hairline rulings confirmed, and one correction to your sweep

**Written:** 28 July 2026, Session 226. **From:** Claude Chat. **For:** Claude Code.
**Answers:** `INSTRUCTION__Hairline_Spacing_Is_48_Everywhere__Rewrite_DSRD_7_4.3.md`.

---

## 1. Read §4.3 again. It does not say what your instruction says it says

DSRD 7 §4.3 was rewritten at S224, before your instruction was written. The dense-page tier is already gone. The counting test is already gone. The component carve-out is already in it, confirmed by Kain at S224 and confirmed again by him today.

So there is no rewrite to do. Your instruction was written against a version of §4.3 that no longer exists. This is worth pausing on: you cited a document you had not opened, which is the failure your own analysis puts first.

## 2. The one place your instruction and the specification disagree

Your instruction says 48 at every width, no exceptions. §4.3 says 48 on desktop and tablet, 32 on phones.

**Kain ruled today, on the rendered comparison at phone width: the phone value stays 32.** §4.3 is correct as written and stands unchanged.

**What this means for the sweep you described.** You wrote that you were sweeping every section hairline to 48 at every width. If that sweep set 48 at phone width, the theme is now off-spec. Check it and report:

- Every section hairline reads 48 above and 48 below at desktop and tablet.
- Every section hairline reads 32 above and 32 below below 768px.
- Lines inside a DSRD 8 component keep their own values and were not touched.

Report the three results separately. Do not report this as done without them.

## 3. The carve-out, confirmed again so it cannot drift

**48 stops at the edge of a component.** It governs the lines that separate one section of a page from the next. A line inside a card, a row line in the help question list, and the site header's own bottom border are parts of their component and keep their specified values. Test: if the line sits inside a DSRD 8 component, §4.3 does not govern it.

## 4. Text colour: §1.1 has been rewritten, read it before your next CSS pass

The old wording used the word "body" for two different things, which is why the documents disagreed. It is now one question:

**Is the text read, or is it scanned?** Text read in sentences and paragraphs is brand dark #354149. Short supporting lines glanced at beside something else are soft grey #5E6B75. If in doubt, dark.

Consequences you will meet in the CSS:

- Article and help-article running text is dark. DSRD 9 §22.6 already said this and is unchanged.
- Page copy and introductions on the main pages are dark, where some are currently grey.
- Card excerpts, taglines, stats labels and captions stay grey. No change.
- Pull quotes are dark, ruled today on the rendered page, replacing soft grey. Their attribution line stays grey.

Do not sweep the theme for this now. Report what is non-conforming and wait.

## 5. Two other rulings from today, for your awareness only

- **The 56px play badge stays specific to the Testimonials page.** The video card is one shared component with the Testimonials badge recorded as a named variant. Both go into DSRD 8 this session.
- **The story scroll is not promoted.** The school pages get their own component: same scroll behaviour, wider container, school colour. The About scroll keeps its page-local label. The behaviour is specified once and both point at it.

## 6. Scope of this message

Two things only: the three-part hairline check in section 2, and a report of what is non-conforming under section 4. No sweeps, no fixes beyond restoring the phone value if your sweep changed it. Anything else you find goes to TO Chat.
