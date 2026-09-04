# ASK: DSRD 6 and DSRD 2 disagree on what the help-category image is

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Found while:** preparing to roll out the fifteen real category images (all fifteen checked present this session, `NOTE__The_Fifteen_Category_Images_Exist_Checked_S338.md`).

---

## What was checked

DSRD 6 §5, item 11 (S337): "the 15 category images produced to DSRD 7 section 12.3 and set **as the featured image**."

DSRD 2 §2.24, item 4, the individual FAQ article spec: "No featured image."

These say opposite things, and neither has been corrected to match the S337 ruling that added the exception.

## What is actually built, and why

The pilot page (post 218) carries its image **inline in the body**, not as a WordPress featured image. `help.css`'s own comment names the reason: `contentHasAssets` and `keywordInImageAlt`, two of the machine checks, are read from the editor content, and a template-set featured image earns neither. Building it as a true featured image would mean the page's own score never actually credits it.

## The question

Which of the two documents is wrong, and should be corrected: DSRD 2's "no featured image" for this type, or DSRD 6's "set as the featured image" language, which the live build cannot honestly satisfy the way it is worded? Or is "featured image" in DSRD 6 §5 meant loosely, covering an inline body image, and the wording there is what wants tightening?

Not blocking: the 220-CSV job and the sitewide UKRLP-line-plus-image rollout continue on the pilot's already-proved inline-body shape either way, since that is what actually scores. This is a request to fix the documents so they stop disagreeing, not a hold on the work.

---

OWED BACK: which document is corrected, and its new wording.

*No em or en dashes in this file; checked before writing.*
