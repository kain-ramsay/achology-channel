**Needs from Code:** two fixes and one sitting for the Courses page (post 38604), from Chat's DSRD 6 chapters 6, 7 and 8, now written into the page's DSRD6_RECORD in the Courses Directory Page folder.

# NOTE: Courses page, what Chat's read of chapters 6 to 8 found

**From:** Claude Chat, S391, Tuesday 29 September 2026. **To:** Claude Code. Read from https://achologytest.com/courses/ in Kain's Chrome, desktop width.

1. **Course card student count has no name (chapters 7 and 8, site-wide).** `card__stat` shows the number beside an icon marked `aria-hidden`, so a screen reader reads "169,171" and nothing else. Chat's call, no visual change: add visually hidden text so it reads "169,171 students enrolled". Whether a visible word joins the number is Kain's, on the page, in the sitting below. This is the course card component, so it fixes every page that uses it.
2. **The goal picker's instructions appear three times** (the lead, "Choose the areas of your life, or career you want to understand better or improve.", and "Choose all the areas that matter to you, and we'll show you the courses that best match your interests."). Copy, so Kain rules it on the page. Show him the three lines together in the sitting.
3. **The Safari sitting for chapters 7 and 8.** Chat could not use a keyboard in the browser, so these are Kain's with you: the keyboard walk (every control reachable, focus always visible under the sticky header), hover and focus contrast on every interactive element, 200% and 400% zoom, and the whole page at phone width as the second evaluator. Write what he finds into chapter 8 of the record.
4. **Still yours, machine lines:** chapter 6 item 5 (the accessibility tree audit, once per template) and chapter 7's scan.

Site search missing from the trunk test is recorded against the Site search card, not this page.

*No em or en dashes in this file; checked before writing.*
