# REPORT: the instructor article template passes all four points

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `BRIEF__One_Accessibility_Scan_On_The_Instructor_Article_Template_Not_Eighteen_S360.md`.

---

**Page tested:** `https://achologytest.com/learn/helping-people/articles/persuade-someone-who-disagrees/`, one of the 18, template shared across all.

**Method:** full accessibility-tree read plus targeted DOM checks, live browser, not a static read of the markup.

## The four points

**1. Every button and link is a real element, not a styled stand-in. PASS.** Every clickable surface on the page is a native `<a>` or `<button>`, or in one third-party case (the Complianz cookie-consent close control, not theme code) a div correctly given `role="button" tabindex="0"`. Checked every div and span carrying a pointer cursor site-wide on this page: all sit inside a real link or button as decorative children, none is an independent click target of its own.

**2. Every interactive control carries a name stating its purpose. PASS.** One link looked unnamed on first read: the small avatar link beside the author's name at the foot of the article. Checked its markup directly: `tabindex="-1" aria-hidden="true"`, deliberately pulled out of the tab order and the tree because it duplicates the adjacent named link "Kain Ramsay" pointing at the same page. The same pattern already documented and approved elsewhere in the theme for a duplicate link beside a named one. Every other link and button carries a real accessible name, either its own text or, where a link wraps only an image, that image's alt text.

**3. Roles and structure are true, nothing claims to be what it isn't. PASS.** One `h1`, every section heading beneath it an `h2`, no level skipped and no heading standing in for something that isn't one. Landmarks are single and correct: one `main`, one `banner`, one `contentinfo`.

**4. Nothing a visitor can do is invisible to the tree. PASS.** Checked every element marked `aria-hidden="true"` against whether it is still focusable or clickable without a matching `tabindex="-1"`. None found. Nothing hidden from the tree is still reachable by mouse or keyboard.

## Verdict

**Pass on all four, no template fault found.** No page-specific issue either, since the point checked here is the shared markup, not this article's own content.

---

OWED BACK: nothing on this. The board card closes on this line, alongside Kain's own Safari check.

*No em or en dashes in this file; checked before writing.*
