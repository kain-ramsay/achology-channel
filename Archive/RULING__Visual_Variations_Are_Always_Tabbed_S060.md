# RULING: every visual variation put to Kain is TABBED, always, site-wide

**DOCUMENT TYPE:** ruling. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Ruled by:** Kain, in the S060 sitting, unprompted and emphatic.
**Filed under Harness Rule 14**, which requires a ruling given in session to be filed the same session so Chat writes it into its owning document.

---

## Kain's words, quoted

> "yes, render the crop as tabs, and PLEASE let this ALWAYS be our standard for wheni need to rule on visual design variations on any aspect of the site - ALWAYS, do you understand?"

The capitals and the repetition are his. It is a standing instruction, not a preference for one job.

## What produced it

He was ruling on the course card background. Code first gave him four treatments **stacked down one page**, each row below the last. He asked for tabs instead. When the tabbed version was built and he had ruled from it in seconds, he generalised it himself to everything.

## The rule

**Every visual variation put to Kain is one page, one row of tab buttons, one panel visible at a time, with the thing under judgement in the same screen position in every panel.** Flipping a tab changes only the thing being decided. Nothing else moves.

## Why it is better, which is the part that makes it hold

A stacked comparison makes him carry a memory of option one down the page to set against option three. He is then judging a recollection rather than the thing. Tabs put the difference in the same pixels, so his eye does the comparison instead of his memory.

Chat may recognise the shape of that argument. It is the same principle as Code's standing rule that his own memory is never a source, applied to Kain's eye rather than to Code's recall.

## What it does not change

Three things already ruled stay exactly as they are, and the tabbed form sits inside them rather than replacing them:

- It is still the **whole page**, with real header, footer, navigation and theme CSS. Never a component on a blank sheet.
- It still opens in **Safari** for him. Code's own browser pane is a verification tool and is never presented to him.
- The options are still **rendered**, never described. This ruling governs the form of the render, not whether there is one.

## How Code has made it mechanical rather than remembered

A standing rule that depends on somebody rebuilding it the same way each time is a rule that rots, so the instrument is now shared rather than re-authored per job: `previews/variant_tabs.py` in the theme, shipped at v0.61.18. Any set of variants goes in, a tabbed page comes out, with arrow-key switching as well as clicks because flicking back and forth quickly is the whole point.

It also enforces three things that were each learned the hard way, so a future comparison cannot quietly drop them: the markup is lifted from the **rendered** page rather than authored in the builder, the page carries the real chrome, and the fetch runs over the server's own loopback so SiteGround's captcha can never again be misread as a page being missing.

`previews/build_course_card_backgrounds.py` and `build_course_card_crops.py` are the two worked examples.

**Nothing is asked of Chat here except the record.** This is Kain's ruling on how Code works, filed so it lives in its owning document rather than only in Code's memory. Code has also written it into his own permanent memory note on visual decisions.

*No em or en dashes in this file; checked before writing.*
