> CODE DISPOSITION, S203: DONE. The button family shipped on every page of the build site as 0.707.788 on Kain's yes, 87 of 87 layout checks at zero; see TO Chat/DONE__Sweep_The_Button_Family_Across_The_Build_Site_S453.md.
> CODE DISPOSITION, S208: WAITS ON the theme main session (the button family sweep is its job; read in full by the course page design session, which builds nothing into the theme).
> CODE DISPOSITION, S209: WAITS ON the theme main session reaching it in the queue's order, after the page sign-offs and the policy family ruling; read in full.
**For Code, the theme main session. What this needs from you:** build Kain's button family into the theme once, then roll it onto every page of the build site, prove every page in WebKit, and show Kain the rolled-out pages in the one shared Change Viewer before anything is deployed. One DONE owed back.

# BRIEF: sweep the button family across the build site (Chat, S453, Monday 2 November 2026)

**DOCUMENT TYPE:** signed sweep brief under The Harness, Rule 3, answering ASK__A_Sweep_Brief_To_Roll_The_Button_Family_Across_The_Site_S208. Kain said yes to this session writing the standard home and this brief, and his go to the build stands in his own words: "Yes, build then".

## The scope, in Kain's words

"every single button and every single link and every single tab across the entire site falls under this", and "I said everything, and everything means everything." The sweep covers every page of the build site and every button, text link, link in the writing, navigation link, tab, pill, icon button, open and close toggle and form field on it, including the header menu and its panels, the footer link columns, breadcrumbs, card and row links, the controls inside the closed mobile menu and the lightboxes, and the six controls once kept out (the header Sign In, the help Listen button, the Was This Helpful controls, the cookie consent pair, the form fields, dropdowns and submits, and the course card's View and Enrol buttons).

## The family, by reference

The standard is DSRD 7 section 5.1, The Button Family, written today, with its homes in section 5.2.4 (icon slots), section 5.3 (radius), section 5.5 (form fields and the two closed link paragraphs) and section 17.1 and 17.2 (page numbers and the View all link). Quote it from there under Rule 4, never from this brief. The approved prototype is your own preview folder button-standard-s208: PICKS.md and its stylesheets. Where DSRD 7 and the preview stylesheets differ, the preview wins and you tell Chat so the DSRD is corrected.

Two lines to hold above all: the orange disc points the way, and the fire frame marks what is chosen or reached for. **School colours are the one exception** (pick 14, "Please don't contradict this one part"): every school-coloured line, link or control keeps its school's colour, with the family's shape and behaviour. **The cookie Accept and Reject stay pixel-identical to each other**, both wearing one family member, because the law asks it.

## The order of work

1. **Theme tokens first.** Add the family's values to base.css as tokens (the fire frame, Glowing Ember and its hover step, the pill radius, the 46 height, the disc sizes), and set `--radius-button` and `--radius-input` to the pill. **Gate commission (Chat's, under DSRD 7 section 5.3):** `css_gate.py` allows the four radius tiers only; it now allows the pill (999) for buttons, inputs, tabs, pills, icon buttons and toggles, and 24 for the tall enquiry box, and nothing else new.
2. **Components second.** Build each member once as a shared theme component on those tokens: main button (with the hero size), second choice button, Mini Disc text link, links in the writing, navigation links, tab row, pill row, icon button, toggle mark, form field. Give each a row in the Component Registry's shared features table through its birth gate and send Chat the class names; Chat retires the link hover wash row there and DSRD 8 section 43 for links in the writing when your DONE lands. Remove each page's own copies of these controls as you switch them, so nothing can drift again.
3. **Page by page third.** Map every one of the 106 kinds in census.json to its member and switch them over, one body of work at a time, in this order: the header, footer, mobile menu and cookie banner (they are on every page); then the commerce pages (home, Courses, the course pages, Pricing, the school pages); then About and the founder and policy family; then the Knowledge Hub (front page, subject and topic pages, the list kinds, article, book note, quote article, workbook, author biography, search); then Help and Enquiries; then everything left. Any kind no pick covers is a question to Kain as a round of four options, never a guess.

**Derived artefacts (Rule 3):** this replaces controls, not files or records, so nothing is orphaned. What depends on the old look and must be checked rather than discovered later: every signed page's DSRD 6 record, the frozen preview pages in the previews folder that show the old buttons, and the build sheets in the Component Design Prototypes folder that carry a button value. Each signed page's record takes one new line for this change, naming Kain's S208 ruling, rather than a fresh full gate, because the button family is the only change on that page. Build sheets with a superseded button value take the same one line.

## How each page is proved

Re-run your census on every page in WebKit at a desktop, a tablet and a phone width (1268, 768 and 390, plus 1070 where the first census ran), the same instrument that found the problem: every control reads its member's values and none of the old ones is left. Check hover, keyboard focus and pressed states, the dark bands, and the open mobile menu and lightboxes, which the first census could not reach. Run the page gate on each page; contrast is checked on every state, hover included (white on the Glowing Ember band keeps 4.55:1). A page is "changed, not verified" until its three widths pass.

## Kain's look, before anything is deployed

**Nothing is deployed to the build site until Kain has seen the rolled-out pages in the one shared Change Viewer**, Before as the build site is now and After with the family, Computer and Phone, his one Safari tab reused. Show him the home page, Courses, a course page, Pricing, About, the Knowledge Hub front page, a list page, an article and the search page, and add any page where a question below was settled. When he says yes, gates, version bump, deploy, the zip, and the ship brief, as usual.

## Open questions for Kain (visual, so his; put each to him as four rendered options in the Change Viewer, Rule 7)

Chat has not decided these and neither may Code. Each is one round, with Code's recommendation named.

1. **The header Sign In.** Its compact size is retired. Which member does it wear in the fixed-height header (the main button or the second choice button), and at what height there?
2. **The help Listen button and the Was This Helpful Yes and No.** Which member each wears (Kain retired their exceptions; the picks do not name their member).
3. **The cookie consent pair.** Which one member both Accept and Reject wear, identical.
4. **The course card's View and Enrol.** Which members they wear on the card, and how Enrol, an external buying button with no disc, shows its outbound marker (DSRD 7 section 1.0's course card exception was written for the old plain buttons).
5. **The chevrons the picks do not name:** the header menu's dropdown chevron and the dropdown field's chevron. Do they stay, or take the toggle mark?

Anything else no pick covers joins this list as its own round.

OWED BACK: one DONE into TO Chat, carrying the theme version, the census rerun at all three widths showing no old control left, the gate printouts, the Change Viewer link, Kain's words on each open question and on the rolled-out pages, and the list of DSRD 6 records and build sheets that took their one line. Or the one question that stops you.

*No em or en dashes in this file; checked before writing.*
