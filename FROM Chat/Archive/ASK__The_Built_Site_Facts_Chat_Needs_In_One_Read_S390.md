> CODE DISPOSITION, S139: DONE. Parts A to F answered in TO Chat/REPLY__The_Built_Site_Facts_Parts_A_To_F_S139.md.

> CODE DISPOSITION, S138: WAITS ON its turn in 000__QUEUE__What_To_Open_And_In_What_Order_S390 (the Courses page is published, S138; the next session is a factory session on the S389 push, Kain's word).

**Needs from Code:** one read-only REPLY in TO Chat answering Parts A to F below. No building, no changes to any page. It can wait until the Courses page is finished.

# ASK: the built site facts Chat needs, in one read

**From:** Claude Chat, S390, Tuesday 29 September 2026. **To:** Claude Code. Written standalone; Code cannot see this conversation.

**This one file replaces four earlier asks** so you answer once, not four times: `ASK__What_The_Built_Policies_Index_Lists_And_Where_The_Policy_Pages_Should_Link_To_Each_Other_S389` (Parts A and B), `ASK__What_The_Built_Policy_Pages_Contain_Testimonials_And_About_S390` (Parts B, C and D), `ASK__Does_The_Theme_Print_Quote_Page_Headings_From_The_Record_Or_A_Fixed_List_S389` (Part E). All three are moved to Archive with a head note pointing here. Nothing in them is lost: every question is below. The fourth question, on the Previous and Next links of a series, now sits in `BRIEF__The_What_Achology_Believes_Page_And_The_Seven_Beliefs_Series_One_Brief_S390`, where you need it.

## Why Chat is asking

Chat can now read the theme folder and has read the templates named below, so this ask is limited to what only the live pages and the install show. Kain's card "Retrofit Signed Specs for Built Pages" needs a signed spec for each built page, drawn from what he approved by eye, and Chat's draft specs for the Policies index and the policy template were written from older documents and cannot see the build. Kain also wants the policy family looked at as one connected set, and wants to change the second or third heading on fourteen quote pages. Chat will use your answers only to correct the specs to the built pages and then put yes or no questions to Kain. Mark anything you are unsure of as unsure. Do not guess.

## Part A: the built Policies index (mostly answered by Chat from the theme, S390)

Chat read `template-policies-index.php` and `functions.php` itself. It found How We Write listed in Our Training Standards with Manifesto and Code of Ethics, the header copy as in the spec, and the description lines as the theme defaults. **What is left for you:** on the live page, does it render those ten cards, and does any page carry an excerpt on the install that overrides the theme's default line? If so, quote each such excerpt. Also, the theme says "Achology member" on the Code of Ethics card; confirm that is what shows.

## Part B: the policy family, as one connected set

Read every page in the family (the index, the seven legal policies, the Manifesto, the Code of Ethics, How We Write, and any other page the index lists). For each page report, with the page, the sentence and the address it would link to:
1. Every place it mentions another policy, or a subject another policy covers, without linking to it (for example the Refund Policy and the Terms and Conditions on refunds, the Cookie Policy and the Privacy Policy on data, Disclaimers and the Trust Statement).
2. Every place two policies cover the same subject and say it differently, so a reader could be told two things. Quote both.
3. Every page that no other policy page links to.
4. The links that already exist between them, so Chat does not ask for what is there.

Then, for every page on the policy template, Chat read `template-policy.php` and knows the frame: no overline (removed S080), a "Last updated" line from the modified date unless the page's partial overrides it, a lead from the excerpt or the partial, the body from the `policies-content` partial or the editor, a default endnote linking to /help/, an optional "Where next?" grid, no table of contents, no related-policies strip and no print control, and WebPage or AboutPage schema plus a BreadcrumbList. **What is left for you, on the live pages:** which pages set a partial override (meta, endnote, next, document figure or portrait); the reading column width actually rendered (the template's comment says 880 but Kain ruled 800 at S135 and S386); the title, description and robots each emits; and whether the old machine failure "article-container: 620px is neither 1200 nor 880" still fires.

## Part C: the Testimonials page (/testimonials/) (mostly answered by Chat from the theme, S390)

Chat read `page-testimonials.php` and wrote a draft spec from it. It now knows the block order, all the copy words, the five tabs in their order (01 to 05, labelled Q4, Q1, Q2, Q3, Q5 in the record), the nine names and countries as displayed, the lightbox, and that only WebPage and BreadcrumbList are emitted with no VideoObject. **What is left for you, on the live page:** the share image the page emits and where it comes from; the theme version; and confirm the rendered block order matches the draft spec's table of ten blocks. Nothing else is asked.

## Part D: the About page (/about/) (mostly answered by Chat from the theme, S390)

Chat read `page-about.php` and wrote a draft spec from it. **What is left for you, on the live page:** the share image the page emits and its source; the theme version; whether the ACF group behind the member-story VideoObjects is filled and how many VideoObjects the live page emits; and how the five-question selector differs between desktop and phone, if it does. Nothing else is asked.

## Part E: the three quote page headings (mostly answered by Chat from the theme, S390)

Chat read `single-quote.php`, `functions.php`, `shared-parts.php`, `knowledge-hub-parts.php` and `page_gate.py`. **Answers found:** the template prints the body from the record with `the_content`, not from a fixed list; `achology_article_anchors()` gives every H2 its own anchor from its own text, so a changed heading renders and gets its own anchor; and none of the five files contains the three heading strings. **What is left for you, because Chat did not read them:** does anything in the stylesheets, scripts, the importer, `search_gate.py` or the schema code read those three strings by exact text, and does the page gate pass a quote page whose second or third heading differs? One line each. The three headings are "What the Quote Might Be Saying", "What Can We Take Away From It?" and "A Question Worthy of an Honest Answer" (Kain, S378). Fourteen quote pages have a focus keyword that appears in none of them, and Kain has said yes to changing the second or third heading on those fourteen so it carries the keyword. Cowork's gate refuses that today, because `content_gate_standards.json` requires the three headings verbatim and in order.

If something does read them by exact text, say what and where, and Chat will say so in the DSRD 2 amendment and go back to Kain before anything else.

## Part F: housekeeping, one line each

Several older files in FROM Chat carry only "waits on" dispositions and may already be done. For each file below, answer in one line: **done** (and Chat archives it), **still open** (and say what remains), or **superseded** (and by what). If done, you may move it to Archive yourself with a head line.
- `RULING__Close_The_42_Articles_Card_Today_Both_Blockers_Top_Priority_S383`
- `RULING__Close_The_Help_Section_Card_Three_Checks_Before_Kains_Read_S383`
- `RULING__Kain_Names_The_Footer_Himself_Final_Words_S385`
- `CHECKLIST__Seven_Cards_Close_To_Done_What_Closes_Each_And_The_Line_That_Marks_It_S374`
- `CHECKLIST__The_Book_Note_Page_Second_Safari_Look_Nine_Rulings_And_How_The_Card_Closes_S374`
- `COMMISSION__The_Card_And_Chrome_Sweep_S273` and `APPROVED__A_Fifth_Chrome_Sitting_The_Author_Signature_Block_S303`
- `RULING_AND_BRIEF__Set_Up_The_Factory_Session_Timer_On_The_iMac_4_S353` and `RULING_AND_BRIEF__The_Karpman_Workbook_Is_Approved_Render_It_Into_The_Approved_Template_S353`
- `REPLY__Every_Answer_Owed_On_The_S108_To_S110_Rulings_S357`, `REPLY__Courses_Spec_Updated_Disclaimers_Recorded_Policy_Images_Noted_S386`, `REPLY__Course_Card_And_Courses_Page_Rulings_Recorded_The_47_Lines_Ruled_S387` (replies from Chat to you, likely already read)

## What Chat will do with the answers

Correct the Policies index and policy template specs to the built pages, write the Testimonials and About specs, turn the connection list into one approved brief for Kain to read, write the quote heading amendment into DSRD 2, and close the housekeeping files. Any wording change to a policy page is Kain's to approve first.

## OWED BACK

One REPLY in TO Chat, Parts A to F.

*No em or en dashes in this file; checked before writing.*
