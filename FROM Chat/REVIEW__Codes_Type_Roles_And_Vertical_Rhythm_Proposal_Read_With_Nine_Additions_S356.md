# REVIEW: Code's proposal for the semantic type roles and vertical rhythm, read by Chat, with nine additions

**DOCUMENT TYPE:** review, from Claude Chat, Session 356. **Date:** Thursday 10 September 2026.
**What this is:** Kain pasted Code's five-step proposal (name the roles from the 48 combinations in use; Kain rules on one real page; Chat writes them into DSRD 7; Code builds them as tokens and sweeps the site; `css_gate.py` refuses a size that is not a role and a spacing value not on the scale) and asked Chat to review it objectively before the sitting that opens the next session. The proposal is sound and Chat agrees with all five steps and the sequencing. The nine additions below are what Chat would want in it before it decides how every page renders from here on. None changes the order; several change what a role is.
**Owning documents:** DSRD 7 (tokens; standing rule 8: read whole before rebuilt), DSRD 8 (component rulings), `production-css-files` and `component-library` (the gates and the lock), standing rule 16 (the render standard).

---

## 1. A role is a complete recipe, and the recipe has more lines than size, weight and line height

Code's definition: size, weight, line height, and the space that follows. Add to every role:

- **Family.** Como or Mulish (the body face is Mulish, S085; headings carry Como where the type scale says). A role names its face so no stylesheet has to.
- **Space above as well as below, and the collapse rule.** Vertical rhythm is asymmetric: a section heading wants more above it than below it (Kain's S109 ruling, the page title takes 24 above its reading text, is one instance). So each role carries `above` and `below`, and one rule decides what happens where two roles meet: the larger of the first's `below` and the second's `above` wins, never both. Without that rule the theme will add both and the rhythm doubles in places nobody can see why.
- **First and last in a block.** The first role inside a card, panel or column carries no space above, the last carries none below (Kain's standing ruling that no hairline sits at the top of a page is the same principle). Otherwise every container pads twice.
- **Tracking and case where the role uses them.** Labels and overlines (the 12/600 that appears 22 times is almost certainly this role) are uppercase with letter-spacing; that belongs in the role, not in the component.
- **The measure, for the body role only.** The reading width is a property of the body role: a character count per line (the accepted band is about 60 to 75 characters at the body size), from which the reading column's pixel width is derived. Code's own point that the reading-width change becomes one edit to the body role is exactly right, and this is the line that makes it so.

## 2. Every role has its values at three widths, not one

A role is one token, but a single size does not survive a phone. Each role carries its desktop, tablet and phone values (stepped, or fluid between two ends), and the sitting rules them at all three widths in one file, which is what standing rule 16's render standard already demands. Some roles do not scale (button, label, caption); say which.

## 3. The roles are derived from the three approved pages, and the cluster is a starting point, not the authority

The 48 combinations in use include the site's mistakes as well as its decisions. The authority is the three exemplar pages Kain approved in Safari this week (quote, article, book note, S108 to S110) and the nine-step type scale (S056). So: cluster the 48, propose the roles, then prove that the roles applied to those three pages reproduce them exactly. A role that would move an approved page is either wrong or is proposing a change, and a change is put to Kain as a change.

## 4. A role sits on the scale, and the set stays small

Every role's size is a step on the nine-step scale or the scale is amended in the same sitting; no role introduces a size by the back door. Twelve roles is about right. The rule for adding a thirteenth later: only for a rendered case no existing role serves, and it enters through the same sitting, the same document and the same gate. The gate's annotation list (the pill, the 56px help header) is the pressure valve for genuine one-offs; it is not a second type system.

## 5. The role set covers every element the body renderer emits

Content bodies arrive from records: H2, H3, paragraph, list, blockquote, the practice panel, the closing question, figure captions, tables where they occur. Every one of those maps to a role or the first gate run will show a gap on the first content page it reads. Name the map in DSRD 7 beside the roles: element to role, for each page type.

## 6. Accessibility is a test in the sitting, not an afterthought

The body role's line height is at least 1.5, paragraph spacing at least twice the body size, no body text under 16px on a phone, and the roles survive a user's text-spacing override (WCAG 2.2, text spacing). These are numbers the sitting checks once and the gate then holds; PRD Criterion 7 requires them at launch.

## 7. The type specimen page is the ruling surface and the regression reference

Build one page that renders every role with real copy at the three widths, in the theme, as a workbench page. Kain rules the roles on it and on the one real page; it is then the reference the sweep is measured against and the page every future change to a role is judged on. It is the roles' prototype in the S257 sense, and its build sheet is DSRD 7's role table.

## 8. The sweep's acceptance test needs a measuring instrument, not an eye

"Renders identically except where a value was off-scale" is the right test and it is not checkable by looking. Before the sweep, dump the computed font-size, line-height, weight, and margins of every text element on one page per family; after the sweep, dump again and diff. The diff is the list Kain sees, and every line in it is either an off-scale value corrected (named) or a mistake (reverted). Screenshots at three widths beside it.

## 9. Names are the durable part, so fix the naming rule now

Semantic names only (page-title, section-heading, sub-heading, lead, body, body-small, caption, label, link, button, and the rest), never a size or a weight in a name, and a name never changes once ruled: renaming is how a token system drifts. DSRD 7 holds the table as the decision record; the stylesheet holds the same names as custom properties; the gate refuses anything else.

## On Code's one question

Yes: bring the roles as a set for Kain to react to, on the terms above: rendered on the one real page and on the specimen page, tabbed, at three widths, with the three approved exemplars reproduced exactly, and Kain rules there. That is standing rule 16 applied, and it is the better route than deriving twelve roles from scratch in conversation.

## Sequencing, agreed with one addition

First sitting at the top of the next session, before the Knowledge Hub templates and before the reading-width change. The addition: Chat reads DSRD 7 whole before the sitting and brings the current type scale, spacing scale and the S109 rulings into the room, so the sitting starts from the record and not from memory (standing rule 8).

## Addendum, the same session: five things from a second opinion Kain sought, folded in

Kain put the same question to another assistant and asked Chat what in its reply was new. Most of it the plan already carries (audit the existing styles, a small complete set of roles, spacing by relationship with the heading sitting closer to what it introduces than to what precedes it, a reference page judged in context, pilot before rollout). Five things were not in the plan and belong in it:

1. **Decouple the visual role from the heading level.** A card heading may be an H2 on one page and an H3 inside a card; the HTML level stays correct for the reader's outline, the screen reader and the search engine, and the visual role is applied by class or token, never by element selector alone. Section 5's element-to-role map is therefore per context, not per tag.
2. **Two roles to name explicitly:** card heading (the six-card grids are a large surface and the render standard already treats cards as a family) and supporting text (the pale line, S280's AA-safe grey). Code's "a couple more" were probably these; name them now.
3. **Each role references a semantic colour token by name** (primary text, secondary text, text on dark), never a hex, so the same role reads correctly on the dark card and the cream panel without a second role. The colour tokens are DSRD 7's existing layer; the role only points at one.
4. **Named density contexts for spacing, not a second table.** The role carries its own rhythm (section 1), and a small set of named contexts, reading and card at least, may override it, so the same heading works in an article and in a compact card. The override is a named context on the container, never a per-page number. The sitting decides the contexts; the gate refuses a spacing value that is neither the role's nor a named context's.
5. **Edge cases on the specimen page:** the longest real title on the site, the longest card title, a list inside a card, and the whole page at 200 per cent browser zoom and with the user's text size enlarged. A role that only works at the ideal length is not a role.

One caution from the same source: the second opinion offered starting numbers (20 between paragraphs, 12 to 16 under a heading, 40 to 48 above a section heading, 48 to 64 between blocks). They are reasonable and they are not ours. The project has its spacing scale and its rulings (48 for the hairline, 24 above the page title, S109), and the sitting rules by eye on rendered pages. Numbers arrive from the sitting, never from a list.

And one consequence for the skills: once the roles are ruled, `achology-building` and `production-css-files` gain one line each, that every text style is a named role and every gap is the role's or a named context's, so Chat and Cowork build to the system too, not only Code.

OWED BACK: nothing to Code from this file; it is Chat's read for Kain and for the sitting.

*No em or en dashes in this file; checked before writing.*
