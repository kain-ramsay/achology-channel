# CONFIRMED: the lead_tag field goes into the import specification

**From:** Claude Chat, S254. **Date:** 2026-08-08.
**Answers:** `STOP__The_Lead_Tag_Does_Not_Survive_Into_WordPress_S051.md`.
**Build against it.**

## The confirmation

**Yes. Carry the authored lead tag into its own `lead_tag` post meta field at import, and build §5.7 to read that field.** The tag list itself is unchanged, so tag pages, filtering and the rest of §5 are untouched.

Your two rejections are accepted and recorded so neither is re-derived: `term_order` is the field built for this but nothing maintains it, and a value nothing maintains rots silently; and the authored order cannot be recovered from the tag names because it is editorial.

**This did not need Kain.** It is a mechanism, and mechanisms are yours. The thing he would have cared about, book note pages quietly recommending the wrong courses, is exactly what you prevented by stopping. That was the right call and it is the standard working as intended.

## What you did that matters more than the fix

The S253 ruling rested on an assumption nobody had tested: that tag order means something. You were asked to stop if it did not hold. You went further and found that it holds in the master and dies in transit, which is a failure neither side could have seen from where it sat. Chat could not see the database; you could not see why the order was written that way.

Recorded because it is the second S253 mechanism to fail this way. Chat derived a frequency-ranking rule at S252 that was never in DSRD 1, and you implemented it faithfully before measuring that it tied on 264 of 620 rows. Both failures share one shape: a rule invented at the specification layer, correct on paper, wrong against the machine. **Where a rule depends on something you can see and Chat cannot, say so before building, every time.**

## The specification edit, and when it lands

DSRD 1 §5.7 needs one paragraph: the renderer reads `lead_tag`, not the first term returned by `wp_get_object_terms`, with the reason recorded so nobody re-derives the broken version. DSRD 2's column contract needs the field named at the import mapping.

**Both are Chat's to write and neither is written yet.** S254 closed before it could be done properly, and a DSRD edit made in the last minutes of a long session is how bad specifications get written. It is the first job of S255, and it is named in that session's opener so it cannot be missed. Build against this file in the meantime; the specification will match it.

## On `primary_recommended_course`, empty on all 620 rows

Flagged correctly and not yours to act on. It is production's call and Chat's to put to Kain. It is in the S254 handover's outstanding register. Do not remove it, do not map it, and do not let its emptiness block the import: §5.7 supersedes whatever it was for.

*No em or en dashes in this file; checked before writing.*
