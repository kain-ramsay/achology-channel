# PROPOSAL: twelve type roles and a width family of five, audited from what is built, with every number beside the ruled value it would replace

**DOCUMENT TYPE:** proposal, from Claude Code, Session 111. **Date:** Thursday 10 September 2026.
**Answers:** `BRIEF__Site_Wide_Container_And_Component_Width_Standards_Audited_Ruled_On_A_Reference_Page_S356` (its section 4, the proposal file owed before the sitting) and `REVIEW__Codes_Type_Roles_And_Vertical_Rhythm_Proposal_Read_With_Nine_Additions_S356` (its nine additions, each answered below where it lands).
**Nothing here is agreed.** Kain rules it on the reference page, one decision at a time, and this file is the paper the sitting works from.

**The reference page:** `previews/reference-page.html` in the theme, opened as a local file. It is deliberately not published. A preview that links the live stylesheets shows Kain his own browser cache, which is the S108 lesson; this one links the theme on this disk, so it is the current CSS by definition.

---

## 1. What was measured this session, and where

**The type half already existed:** `MEASURED__Every_Type_And_Spacing_Declaration_On_The_Site_S110` in this tray. 417 type declarations across 18 stylesheets, 48 real size-and-weight combinations, 16 used exactly once, 115 on a size the nine-step scale does not hold. Spacing: 1,158 declarations, 31 distinct raw values, 255 off the scale.

**The container half is new and is below.** Every `max-width`, `width`, `gap` and horizontal padding in the theme's stylesheets, comments stripped, plus every media-query width.

**The third measurement is new and is the one that matters most.** The three pages Kain approved in Safari at S108 to S110 were opened in WebKit at three widths and every text element's computed recipe was read off the rendered page: family, size, weight, line height, tracking, case, colour and the margins around it. That is the authority the roles are proved against, per the REVIEW's section 3. It is what turns a cluster of stylesheet values into a statement about pages he has already ruled on.

## 2. The container audit: value, where, and what it is

The container system is in far better health than the type system, and that is the headline. There are four container tokens, they are used consistently, and almost nothing competes with them.

| value | how it travels | uses | what it is |
|---|---|---|---|
| 1200px | `--container-page` | 8: `.page-container`, header inner, megamenu inner, footer inner, footer sub inner, and three course blocks | **RULING**, DSRD 7 section 4.1 |
| 1104px | `--container-hero` | 1: `.course-hero__inner`, plus the article and book note hero bands by their own rules | **RULING**, DSRD 7 section 4.1 |
| 880px | `--container-article` | 21: base, book note, course (7), help, Knowledge Hub (6), people (3), quote | **RULING**, Kain S085, on both widths rendered |
| 540px | `--container-quote` | 2: `.quote-container`, `.course-hero__reassure--quiet` | **RULING**, DSRD 7 section 4.1 |
| 944px | **no token.** Written once as `calc(var(--container-article) + 2 * var(--sp-xl))` in `people.css` | 1 | **RULING with no token**, DSRD 7 section 4.4. The value is right and the form is drift: a ruled width nobody can grep for |
| 540px again | typed raw on `.card--featured-quote .card__quote-text` | 1 | **DRIFT.** The same ruled number written a second time, so moving the token would leave this behind |
| 46ch, 42ch | book note hero lead | 2 | **BUILD DECISION.** A character measure, which is the right instrument, used in one place only |
| 62ch | `.pp-group__sub` | 1 | **BUILD DECISION** |
| 26ch | `.lite-quote` | 1 | **BUILD DECISION** |
| 500px | `.card--aaa` | 1 | **BUILD DECISION** |
| 920px, 1060px, 720px | three lightbox panels | 3 | **BUILD DECISION.** Three lightboxes, three widths, one job |
| 420px, 460px | the bubble watermark and the warm room wash | 3 | **DECORATION.** Not content widths and not in the family |

**The finding, in one line:** the site has five ruled widths and about ten one-off component widths, and the one-offs are all component chrome rather than reading measures. Nothing is competing with 880.

**Gutters.** `.page-container` carries 20 mobile, 32 tablet, 48 desktop, exactly as DSRD 7 section 4.1 states. The header and the footer each repeat those same three numbers hand-typed rather than reading a token: `padding: 0 20px`, `0 32px`, `0 48px`, three times each. Same values, second copy, and the gutters have no token to read. **DRIFT in form, not in value.**

**Grid gaps.** `--grid-gap` is 24 and is used 6 times. The spacing tokens are used about 90 times. Beside them sit raw gaps of 8 (22 times), 12 (9), 10 (9), 5 (8), 6 (7), 14 (7), 18 (5) and a dozen more. **This is where the width system is as unruly as the type system**, and it is the half the gate has never checked.

**Breakpoints.** 767, 767.98, 768, 1023, 1023.98 and 1024 are the ruled boundaries; 1040 is the named inset-panel mechanism; 880 and 879.98 are the ruled navigation switch. Then the exceptions.

**One correction owed to DSRD 7 section 4.5, and it is Chat's to make.** That section registers **five** approved stack-point exceptions. The theme carries **eight** annotated widths across four files: 640 four times (`people.css` three, `policies.css` one, all five registered), 599.98 three times (`about.css` registered; `people.css` and `reviews.css` both cite About's exception in their comments but are not themselves on the register), and 639 once in `help.css`, annotated in place as approved by Kain on 2026-07-29 and on no register anywhere. Three real values sit outside the document that is supposed to hold them all. None is a defect on the page; all three are a defect in the record.

## 3. What the three approved pages actually do, and where they disagree with each other

This is the part no stylesheet audit could show. Six places where one thing is set up two or three ways, on pages Kain has already approved.

| the thing | article | book note | help answer |
|---|---|---|---|
| page title | Como 33/700, 1.2, **8 below** | Como 33/700, 1.2, **24 below** | Como 33/700, 1.2, **0 below** |
| page title on a phone | **28** | **28** | **28** |
| opening paragraph | Mulish 18/600, **1.75**, 16 below | Mulish 18/600, **1.75**, 18 below | Mulish 18/600, **1.6**, 24 below |
| body paragraph | Mulish 16/400, **1.75**, **16 below** | Mulish 16/400, **1.75**, **18 below** | Mulish 16/400, **1.6** |
| section heading | Como **24**/600 in the writing, **21** on the blocks | Como **24**/600 | Como **20**/600 on the close |
| contents card head | Como **24**/600 | Como **21**/600 | not present |
| reading column | 880 | 880 | 880 |

**The reading column is the one thing all three agree on**, which is Kain's S085 ruling holding exactly as ruled.

**The phone row is a rule being broken by every page at once.** DSRD 7 section 4.1 states: "Type scale stays fixed across all breakpoints (per §3)." Every page drops the title from 33 to 28 below 639px. Either the sentence is wrong or three approved pages are, and that is decision 6 on the reference page.

**Five off-scale sizes on the article page alone**, each a real element a reader looks at: the contents list at Como 15/500, the contents meta at Como 13/400, the breadcrumb at Mulish 13/400, the author name at Como 15/600, and the guarantee pill at Mulish 11/600. The trial panel body, which reaches twelve templates, is Mulish 17/400.

## 4. The twelve roles

Each is a complete recipe, per the REVIEW's addition 1: family, size, weight, line height, the space above and the space below, tracking and case where it uses them, and a colour token by name rather than a hex. Every size is a step on the nine-step scale, per addition 4. The names are semantic and carry no number, per addition 9.

| role | face | size | weight | line height | above | below | case, tracking, colour |
|---|---|---|---|---|---|---|---|
| `page-title` | Como | 33 | 700 | 1.2 | 0 | 24 | primary text |
| `section-heading` | Como | 24 | 600 | 1.25 | 40 | 16 | primary text |
| `block-heading` | Como | 21 | 600 | 1.25 | 0 | 8 | primary text |
| `card-heading` | Como | 18 | 600 | 1.35 | 0 | 8 | primary text |
| `minor-heading` | Como | 16 | 600 | 1.3 | 24 | 8 | primary text |
| `label` | Como | 12 | 600 | 1 | 0 | 8 | uppercase, 0.08em, primary or soft |
| `button` | Como | 14 | 600 | 1 | 0 | 0 | does not scale |
| `lead` | Mulish | 18 | 600 | 1.75 | 0 | 18 | primary text |
| `body` | Mulish | 16 | 400 | 1.75 | 0 | 18 | primary text, measure below |
| `body-small` | Mulish | 14 | 400 | 1.5 | 0 | 12 | primary text |
| `supporting` | Mulish | 14 | 400 | 1.6 | 0 | 0 | soft grey, the AA-safe one |
| `caption` | Mulish | 12 | 400 | 1.5 | 0 | 0 | soft grey |

**Two existing roles stay by ruling and are not renamed:** `hero` (Como 42/700/1.15, the homepage) and `figure` (Como 28/700/1, the About statistics). **Two carve-outs stay and are named rather than tolerated:** the odometer above 48px (DSRD 7 section 3.0's named exception) and the eight policy-index watermark sizes.

**Where each number came from.** Every one is a value already rendered on a page Kain approved, except three, and those three are the decisions: the body's space below (16 on the article, 18 on the book note, one wins), the section heading's size (24, 21 or 20, one wins), and the lead's line height (1.75 or 1.6, one wins).

**The collapse rule, per addition 1.** Where two roles meet, the larger of the first role's `below` and the second's `above` wins, never both. The first role inside a card, panel or column carries no space above; the last carries none below. Without this the theme adds both and the rhythm doubles where nobody can see why.

**Two density contexts, per addition 4, and no second table.** `reading` is the article, book note, help and workbook body: `section-heading` takes its 40 above. `card` is any locked card or compact panel: every heading takes 0 above and 8 below. The context is a class on the container, never a number on a page. A spacing value that is neither the role's nor a named context's fails the gate.

**The element map, per addition 5, and it is per context rather than per tag, per addition 1 of the addendum.** The body renderer emits H2, H3, paragraph, list, blockquote, the practice panel, the closing question and figure captions. In `reading`: H2 to `section-heading`, H3 to `block-heading`, paragraph to `body`, list to `body`, blockquote to `lead`, the practice panel's heading to `minor-heading` and its body to `body`, the closing question to `lead`, a caption to `caption`. In `card`: a heading of any level to `card-heading`. The HTML heading level stays correct for the reader's outline and the search engine; the visual role is applied by class.

**Accessibility, per addition 6.** `body` at 16/1.75 clears the 1.5 line-height bar and the paragraph spacing bar (18 against a floor of half the body size). No role goes below 12px on a phone, and 12 is used only for `caption` and `label`, neither of which carries meaning a reader needs. The text-spacing override is a check on the reference page rather than a claim here.

**Three widths per role, per addition 2.** Only two roles change between screens under this proposal: `page-title` and `section-heading`, and only if Kain rules that type may scale at all (decision 6). Every other role holds one value at all three widths, which is what the site does today and what DSRD 7 section 4.1 states.

## 5. The width family of five

Kain's five names are the right shape. The numbers below are the audit's, with his ranges beside them.

| his name | his range | what exists today | proposed | why |
|---|---|---|---|---|
| reading container | 640 to 720 | **880, ruled S085** | **880 until he rules otherwise** | Decision 1 on the reference page. His own constraint: it changes only if both widths are rendered and measured in front of him, and they are |
| focused container | 480 to 640 | **540**, `--container-quote`, 2 uses | **540** | The number already exists, is inside his range, and is already a token. It gains a second name rather than a second value |
| article with sidebar | 1040 to 1160 | **1104**, `--container-hero` | **1104** | Inside his range, already ruled, already a token, and the article and book note heroes are built on it |
| standard page container | 1160 to 1280 | **1200**, `--container-page` | **1200** | Inside his range, ruled, and every page frame on the site uses it. Decision 8 puts 1160 and 1280 beside it anyway |
| wide container | 1360 to 1440 | **nothing** | **not created** | No page on the site wants it today. A container with no user is a value that will be misused later. It enters when a directory or comparison page needs it, on its own render |

**So the family is four containers, not five, and every one of the four is a number Kain has already ruled, sitting inside the range he proposed independently.** That is the strongest possible answer to his brief's own requirement that a proposal reconcile with the record rather than replace it: the record already agrees with him.

**The fifth width, 944, is not a container and is named as what it is:** panel chrome, the 880 column plus a 32px bleed each side, per DSRD 7 section 4.4. It gains a token, `--container-inset`, so it stops being a calc written once in one page's stylesheet.

**Component width behaviour, one rule per component**, per the brief's method step 4. Fill the parent: buttons in a stack, callouts, hairlines, full-bleed bands. Carry a maximum: forms and the practice panel at the focused container, the closing question at the reading container. Adapt inside a grid: every locked card, at its ruled tier, with 300px as the named minimum practical card width (the value already used by three card grids). Media: fills the reading container, never wider than the hero band. **No component takes an arbitrary fixed width**, and the ten one-off widths in section 2 each become one of these four or an annotated exception.

**Responsive rules.** The three tiers stay as ruled. Card grids stay 1, 2, 3. The 880 navigation switch stays. The 1040 inset-panel boundary stays. The three unregistered stack points in section 2 are put on the register rather than moved.

**Alignment, stated once.** Inside a section, the heading, its supporting line, its copy and its call to action all align to the leading edge of the container they sit in, and a full-bleed background carries its content in the same container as the block above it, so nothing steps sideways as the reader scrolls. The breadcrumb aligns with its page's leading edge, never the 1200 frame, which is already ruled at S090 and S337.

**The page map.** Help answer, article, book note, quote, workbook: page frame 1200, hero band 1104, reading container 880, inset panels 944. Course and school: page frame 1200, hero 1104, reading blocks 880. Listing and category hub: page frame 1200, intro at 880, cards in the grid. Policy, About and the quiet pages: page frame 1200, reading container 880. An exception is a rendered case Kain approves, recorded in DSRD 9 against the page, never a value in a stylesheet.

## 6. The gate, and what it costs

`css_gate.py` gains two checks on the same terms as its existing radius and colour checks: **size-is-a-role**, which fails a font-size that is not a role token, and **width-is-a-token**, which fails a width, gutter or gap that is not a family token, with the annotation route for named exceptions. Both rules already exist in DSRD 7 in writing. The site breaks them 370 times between them, because nothing has ever checked them and nothing said what a heading is for the rule to attach to.

**The sweep's acceptance test**, per addition 8: before and after, dump the computed font-size, line-height, weight and margins of every text element on one page per family, and diff. Every line in the diff is either an off-scale value corrected, named, or a mistake, reverted. Screenshots at three widths beside it. **No sweep runs before Kain has ruled on the reference page.**

## 7. What Kain rules, in order, on the reference page

1. How wide the reading column is: 880 as ruled, against 760, 720 and 680, with the characters per line measured on each.
2. The space between two paragraphs: 18 as built on the book note, against 16 as built on the article, against 24.
3. How big a section heading is: 24 in the writing and 21 on the blocks as built, against one size everywhere.
4. The opening paragraph's rhythm: three recipes today, one wins.
5. The contents card's heading: 21 or 24, one component, one size.
6. Whether the page title shrinks on a phone: 28 as built everywhere, against 33 as the written standard says.
7. Whether every off-scale size comes onto the nine agreed steps.
8. The page frame: 1200 as ruled, against 1160 and 1280.

Each is one tab row on one page, at desktop, tablet and phone, on the real rendered page with one stylesheet added last and nothing else touched.

OWED BACK: nothing until Kain has ruled. The rulings come back as RULING files the same session he gives them, and Chat writes them into DSRD 7 section 3 and section 4 and DSRD 9's maps.

*No em or en dashes in this file; checked before writing.*
