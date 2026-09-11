> **CODE DISPOSITION, S111: DONE.** Its method ran in order: the container, gutter and gap half of the audit is in `PROPOSAL__The_Type_Roles_And_The_Width_Family_Audited_From_What_Exists_S111.md` section 2, the reference page was built and Kain ruled on it in Safari, and the OWED BACK it names, the proposal file and the reference page's address, was delivered before the sitting. **Its central question is answered and the answer was mostly already right:** four of the five containers he proposed already exist as ruled tokens sitting inside the ranges he proposed independently, and the fifth, a wide container, has no user on the site and was not created. **The reading container is the one that moved: 800px, ruled on the rendered page at the text size he ruled first, with 760 rendered and rejected.** The outer page frame was put to him and withdrawn rather than ruled: measured on the built files, nothing visible moves when it changes on a reading page, so it belongs to a listing-page sitting instead. **Nothing is swept**, which is his own constraint and this brief's section 4; the sweep is the next theme session.

# BRIEF: the site-wide container and component width standards, audited from what exists, ruled on a reference page, written into DSRD 7 as one system with the type roles

**DOCUMENT TYPE:** brief, from Claude Chat, Session 356. **Date:** Thursday 10 September 2026.
**Authority:** Kain, at the S356 close, in his own words: establish a defined set of site-wide container and component width standards, built on what already works, consolidating inconsistencies, never introducing a competing system, so that no page makes its own width decision again. His six points and his starting ranges are carried whole in section 3; they are ranges to evaluate, not requirements.
**Owning documents:** DSRD 7 section 4 (containers, tokens; standing rule 8: read whole before rebuilt), DSRD 8 (component rulings), DSRD 9 (page layouts), `production-css-files` (the gate).
**Board card:** none of its own; foundations work, carried in the S356 handover and the S357 opener. It runs as one sitting with the type-roles work (REVIEW file, this tray), because his point 6 and Chat's section 1 of that review say the same thing: width, font size, line height and spacing are one system, and the body role's measure is what decides the reading width.
**Read this cold.**

---

## 1. What the record already holds, and what any proposal must reconcile with rather than replace

- **880px is the content column for every content page and every template not yet built** (Kain, S085, ruled on both widths rendered; DSRD 7 section 4.1, brought to it S312). The 620px prose column is retired and kept as a record, with the cost named: the ten prose pages run about forty per cent longer, chosen by Kain having seen both. The seven legal pages take 880 (S091).
- **1200px is the page frame**; the article and book note hero block is 1104px; the 944px inset panel has named users including the Policies index (DSRD 7 sections 4.1 and 4.4, S337).
- **The breadcrumb aligns with its page's leading edge, never the 1200 frame** (S090, S337).
- **The mobile navigation switches at 880, not 768** (S048, S250), a registered exception to DSRD 7 section 4.1's boundaries.
- **The book note page's reading column and the article page's centred reading column** are ruled and built (S081, S085 V3, S102 hero rulings).
- **Cards render as populated grids of at least six at three widths** (the render standard, standing rule 16); the course card, review card, book note card and compact/mini cards are locked with their tiers.

So the starting fact is that the site already has one reading width, 880, ruled by Kain against 620 with both in front of him. Kain's new reading range of 640 to 720 sits between those two. **That is the first thing the sitting decides, and it is decided the same way: both rendered, in the brand fonts, on real copy, at three widths, with the character count per line measured**, not by a range on paper. Nothing here reopens 880 by default; it puts the measurement in front of him.

## 2. The method, in order

1. **Audit before proposing.** Read DSRD 7 section 4 whole, DSRD 9's page layouts, and measure the built pages: every container, column, gutter, gap and max-width in use across the help, article, book note, quote, course, school, listing, policy and About families. One table: value, where it is used, whether it is a ruling, a build decision, or drift. Cluster it as the type roles are clustered: the values in use are the de facto family.
2. **Name the family from the audit,** small and semantic: a reading container, a focused container, an article-with-sidebar layout, the standard page container, and a wide container are Kain's proposed names and are the right shape; the numbers come from the audit and the sitting.
3. **Separate outer layout width from reading width.** A wide page or section never produces wide paragraphs: the reading container is the body role's measure (about 60 to 75 characters per line at the body size in Mulish, measured), applied inside any outer container.
4. **Component width behaviour, one rule per component:** which fill their parent (buttons in a stack, callouts), which carry a maximum width (forms, the practice panel, the closing question), which adapt inside a grid (cards, with their minimum practical card width named), and media (fills the reading container, never wider than the frame). No component gets an arbitrary fixed width; the locked cards keep their ruled tiers.
5. **Responsive rules:** the maximum widths, the mobile gutters, the grid gaps, the minimum card width, and the widths at which columns stack, so every container shrinks without horizontal overflow. The 880 nav switch stays as ruled.
6. **Alignment:** how headings, copy, cards and CTAs align inside a section, and how a full-width background carries contained content, stated once.
7. **The map to page templates:** the default container and component arrangement for each principal page type (help answer, article, book note, quote, workbook, course, school, listing, policy, About), with a named exception process: an exception is a rendered case Kain approves, recorded in DSRD 9 against the page, never a value in a stylesheet.
8. **The reference page,** the same private workbench page as the type specimen: the family demonstrated on a real help answer, a real editorial article and a real listing at desktop, tablet and phone, with the longest real headings and the page at 200 per cent zoom and enlarged text. Kain rules on it. Chat writes the rulings into DSRD 7 section 4 (rebuilt whole, standing rule 8) and DSRD 9's maps; Code builds the tokens and layout primitives as the single source of truth and sweeps one page family at a time, with the same computed-style diff acceptance test as the type sweep: nothing moves except a value that was off the family.
9. **The gate.** `css_gate.py` gains a width check on the same terms as its type check: a width, gutter or gap that is not a token of the family fails, with the annotation route for named exceptions.

## 3. Kain's starting ranges, carried as given for the sitting to test

Reading container 640 to 720px for article copy, help answers and workbook introductions. Focused container 480 to 640px for forms and single-task pages. Article with sidebar 1040 to 1160px overall, keeping a comfortable reading column beside the sidebar and its gap. Standard page container 1160 to 1280px for course pages, category listings, resource libraries and landing pages. Wide container 1360 to 1440px where directories, comparisons or similar content genuinely benefit. **Each is put beside the ruled value it would replace, rendered, and Kain chooses on the page.**

## 4. What comes back, and in what order

A short proposal file in TO Chat before the sitting: the audit table, the proposed family with its numbers and the ruled values beside them, the component rules, the responsive rules, the alignment rule, the page map, and the reference page's address. Then the sitting. Then the RULINGs. Nothing sweeps before Kain has ruled on the reference page, and existing content, functionality and approved rulings are preserved throughout.

OWED BACK: the proposal file and the reference page's address, ahead of the S357 sitting.

*No em or en dashes in this file; checked before writing.*
