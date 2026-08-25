# FINDING: the site header has never been checked against its record, and the section header was never built

**From:** Claude Code, Session 84. **Date:** 25 August 2026.
**Found because Kain asked one question in the sitting:** why is the book note page not reflecting the components we confirmed?

It was a fair question and the answer was worse than the question assumed. Both findings below came out of asking the new component gallery which confirmed components that page actually renders, which is the first time anything in this project could be asked that.

---

## The ground: four components carry a record, and that is all

`course-card`, `review-card`, `section-header`, `site-header`. Nothing else in the theme has a data file, so nothing else has an executable build instruction under the S273 ruling.

Of those four, the book note page renders two: the site header and the course card. The review card belongs to the Reviews page and its absence is correct.

## Finding 1: the section header was approved, filed, and never built

`BRIEF__The_Section_Header_Component_Is_Approved_And_Filed_S282` says it plainly, and it was right: `base.css` carries `icon-section-header` and `icon-section-header-container` and has for a long time, but **the header block itself has never existed in the theme.** Confirmed tonight by the census: there is no `section-header` class family in any of the fourteen stylesheets.

**So the book note page writes its own.** `single-book_note.php` hand-builds the pattern for "Explore related learning paths" out of `kh-section__header`, `kh-section__titles`, `kh-section__title` and `kh-section__subtext`, with the two icon classes inside it. A different set of classes doing the approved component's job, on a page that shipped.

**This is not a fault to shout about**, because the brief said not to build it yet: "build the component into the theme to the data file, when the first page needing it is specified and signed. It is not urgent on its own. It has no page yet." The book note page turns out to need it and to have needed it for a while. **The question for Chat: does the book note page's `kh-section` header become the section header component, or is it a second thing?** I have not decided that and it is not mine to.

## Finding 2, and this is the serious one: the gate was skipping the site header

The site header's record names its specimen page, `https://achologytest.com/about/`. **It writes it at the top level of the file. The course card and the review card write theirs inside the `gate` block.** `component_gate.py` read only the gate block, found nothing, and printed the site header under "NOT MEASURED, no specimen page to open".

**So the component that appears on every page of this site has never once been compared against its approved record, and the gate has been green about it the whole time.** That is the green-check-on-an-unchecked-thing failure this project has now met four times, and this one hid behind a nesting detail in a JSON file.

**Fixed tonight**, and the fix is two things rather than one:

1. The gate now looks for a specimen in both places. A record that names one anywhere is a record that wants to be checked, and skipping it on where the key sits is choosing not to look.
2. **The not-measured line was one quiet sentence that read like a footnote.** It is now the loudest thing the gate prints: a banner, then one record per line with its reason beside it. The size of the gate's blind spot is the most important number it produces and it was being whispered.

## What the site header showed the moment it was measured, and it is not good

It opens its specimen page now. **All 41 of its recorded values come back UNCHECKED**, because the record carries values and no selector-and-property bindings.

The review card's own data file warned about exactly this in writing, and it is worth quoting back because it predicted this:

> "A recorded value cannot be compared against a built page unless the record also says WHERE in the page that value lives. COMPONENT_DATA__course-card.json carries values and no selectors, so a gate reading it can compare nothing and would pass green on everything, which is the exact failure the gate exists to prevent."

So the site header's record is **not executable**: 41 values, zero enforceable. The header's bar height, its sticky position, its logo switch at 768px, its nav type and colours, all recorded and none checked.

**I have not written the bindings.** A binding asserts which element in the page carries which value, and a wrong one produces a green check on the wrong thing, which is worse than no check. The site-wide header sitting is first in the running order of the four chrome sittings that were unparked at S302, and its data file gets written in that sitting under the S273 ruling. **That sitting is now the thing standing between this component and any enforcement at all**, which raises its priority rather than changing its owner.

## The whole gate's coverage, stated so the number is on record

Seven records name no usable specimen and are measured against nothing: six card build sheets and the section header, whose specimen honestly reads "NOT YET BUILT". Of the records that do open a page, the course card and the review card are genuinely enforced. Everything else prints as unchecked rows.

**That is the real answer to Kain's question.** The book note page reflects the components we confirmed about as well as our machinery can tell, and our machinery could tell far less than anyone thought.

## One thing shipped alongside

Four waivers were written for Kain's Literata ruling: the book note card's sheet still says Source Sans 3 on four rows and the theme now says Literata. **This is the one class of waiver where the code is right and the sheet is behind**, so the sheet is what gets corrected, not the theme. They wait on your DSRD 7 section 3 rewrite and they are written down rather than left silent.

OWED BACK: nothing. Two questions raised, neither blocking: whether the book note page's `kh-section` header becomes the section header component, and the header sitting's priority.

*No em or en dashes in this file; checked before writing.*
