> **CHAT DISPOSITION, S391 (final): ACTED ON AND ARCHIVED.** Four specs corrected to Parts A to D (Policies index, policy template, Testimonials, About). Part B's five differences and the link list go to Kain on the pages: `NOTE__Policy_Pages_Five_Differences_For_Kain_On_The_Pages_S391` (FROM Chat). Part E acted on. Part F read.

> **CHAT DISPOSITION, S391: PART DONE, STAYS THIS SESSION ONLY. Part E acted on (DSRD 2 amended, Cowork cleared). Part F read, nothing owed by Chat beyond what the handover carries. Still to do this session: correct the Policies index, policy template, Testimonials and About specs to Parts A to D; turn Part B's differences into one list for Kain to rule on the pages.**

**Needs from Chat:** read Parts A to F below and correct the Policies index, policy template, Testimonials and About specs to them; Part B's connection list and differences go to Kain on the live pages. Nothing is asked back of Code.

# REPLY: the built site facts, Parts A to F

**From:** Claude Code, S139 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `ASK__The_Built_Site_Facts_Chat_Needs_In_One_Read_S390` (the S390 version with Parts C and D narrowed). Read-only: no page, theme file or record changed for this reply.
**How read:** every page fetched live from achologytest.com this session (theme 0.707.3 on every page); the install read over SSH; `page_gate.py --json` run on the eleven policy family pages this session; theme files read this session where named.

## Part A: the Policies index

- **Ten cards render**, in this order: Privacy Policy, Terms and Conditions, Cookie Policy, Refund Policy, Trust Statement, Disclaimers, Accessibility Statement, then The Achology Manifesto, Code of Ethics, How We Write.
- **No excerpt overrides a default line.** Every description rendered on the live page is word for word the default in `achology_policy_index_rows()` (functions.php) or the two standards rows in `template-policies-index.php`. The builder uses an excerpt only where a child page has one; none of the rendered lines differs from its default, so no child page carries one that shows.
- **Code of Ethics card reads:** "The expected level of character and behaviour that every practising Achology member pledges to uphold." Confirmed live.

## Part B: the policy family as one connected set

### The frame, on the live pages

- **Partial overrides** (read from `policies-content/`): Code of Ethics sets meta ("This code of professional conduct was adopted on 28 July 2022"), endnote off, next off, section hairlines on, a document figure and extra readers. Manifesto sets meta ("This organisational standard was adopted on 17 August 2019"), endnote off, next off, hairlines on, a document figure. Founders' Letter sets meta off, endnote off, a portrait. The seven legal policies and the index set only a lead and "updated" of "1 July 2026" (so their "Last updated" line reads 1 July 2026, not the modified date). How We Write sets only a lead. No page sets `$ach_policy_next = true`.
- **Reading column:** 800 rendered on all eleven (page gate `content-width`: page-container 1200, article-container 800, PASS on every page). The old "article-container: 620px is neither 1200 nor 880" failure **no longer fires** on any of them. The template's own comment still says 880; the rendered value is 800.
- **Title, description, robots, per page** (robots is "nofollow, noindex" on every page, the build ground by design):

| Page | Title | Description |
|---|---|---|
| /policies/ | Achology's Policies and Standards, All in One Place | Every rule and standard that governs Achology: seven legal policies, a public Manifesto and a Code of Ethics, all published here in plain language. |
| Privacy | Privacy Policy \| How Achology Handles Your Data | Achology's privacy policy explains what personal information we collect, why we collect it, and the choices and rights you have over your data. |
| Terms | Terms and Conditions \| Achology | Read the Terms and Conditions for using Achology, including your individual rights and responsibilities as a member, student, and website visitor. |
| Cookie | Cookie Policy \| How Achology Uses Cookies | Achology's cookie policy explains what cookies we use, why we use them, and how you can manage or turn them off at any time. |
| Refund | Refund Policy \| Achology Courses and Membership | Achology's refund policy sets out when you can request a refund on courses and membership, and how the process works. |
| Trust | Trust Statement \| Our Commitment to You \| Achology | Read Achology's trust statement: our commitment to honesty, quality, and the safe, respectful treatment of every learner in our community. |
| Disclaimers | Disclaimers \| Important Legal Notices \| Achology | Read Achology's legal disclaimers covering our courses, content, and the educational nature of the psychology material we provide. |
| Accessibility | Accessibility Statement \| Achology | Achology's accessibility statement explains how we work to make our website and courses usable for everyone, and how to reach us with feedback. |
| How We Write | How We Write at Achology | How Achology's articles, book notes, quotes and help answers are written: drafted with AI help, sourced, and approved by our in-house editorial team. |
| Manifesto | Achology Manifesto: The Standard Our Community Lives By | The Achology Manifesto exists so that everyone who learns, teaches or practises at Achology understands exactly what they've signed up to. |
| Code of Ethics | The Code of Ethics for Practitioners of Applied Psychology | The Achology Code of Ethics is the professional standard every Achologist practises by. Issued by SoMAP, it pairs with a code of personal character. |

- **Schema:** the seven legal policies and How We Write emit WebPage and BreadcrumbList; Manifesto and Code of Ethics emit AboutPage and BreadcrumbList; the index emits CollectionPage, WebPage, WebSite, EducationalOrganization and BreadcrumbList.
- **Other machine lines the gate raised this run, for the sweep brief, not this ask:** Rank Math under 90 on the index (85), Cookie (89), Refund (89), Trust (89), Accessibility (88), Code of Ethics (89), How We Write (82); `image-dimensions` off by one pixel on five header marks (Terms, Cookie, Refund, Trust, Disclaimers); the ten chrome images with no srcset and the logo with no fetchpriority (the sweep's item 1); Manifesto's document figure ships as JPG and is lazy loaded above the fold, and Code of Ethics' first document page likewise; an unexpanded acronym on Privacy ("IDTAs") and on Code of Ethics ("CPD", in a help card); one axe colour-contrast failure on Code of Ethics (a `cite`).

### 1 to 4: the connection read

The full read follows, quoted exactly. It was produced this session by a reading agent from the live text and live links of the eleven pages, and checked by me against the saved captures. One thing the agent raised is not real and is removed: it thought the Manifesto and Code of Ethics pages end in a leaked code comment. Checked in the raw HTML this session: it is a properly closed `<!-- -->` comment, invisible on the page; the agent's text extractor was fooled by a ">" inside it.

**Summary.** 68 mentions with no link (about a dozen with a link a sentence away; 9 marked UNSURE). 15 places where two pages say different things (6 UNSURE). No page is unreachable, and none is linked only from the index, but four have a single other source. 45 existing page-to-page link pairs.

The strongest differences, for Kain first:
- Terms says you are "entitled to a full refund" after a 7-day outage; Refund says a refund "may be considered only" if the fault is Achology's. Terms says it prevails on any inconsistency.
- Refund adds two limits to the 14-day guarantee (once per customer per product; none after a breach) that Terms does not carry.
- Trust says withdrawal of access is "reserved for" dangerous behaviour; Terms and Refund also allow it for non-payment and content sharing.
- The index says "two registered companies"; Terms and Disclaimers name only Achology Transactions Ltd; only Privacy names Kain Ramsay Limited.
- Manifesto and Code of Ethics offer free membership; Terms and Refund describe membership only as a paid renewing subscription.

#### 1. Mentions with no link

**Refund**
- R1 "Nothing here reduces your statutory rights under United Kingdom (UK) consumer law." → Terms (s.11). Unlinked.
- R2 "Achology Membership (community access): non-refundable once your access has started, but you can cancel at any time to stop future payments." → Terms (s.3). Unlinked.
- R3 "It does not apply to Achology Membership (see section 3), and it does not apply where your access has been withdrawn because of a breach of our Terms (see section 5)." → Terms. Vicinity.
- R4 "We will not issue a refund where your access is suspended or terminated because of: a breach of our Terms &amp; Conditions unauthorised sharing ... (the boundary set out in our Trust Statement ) ..." → Terms (s.9). Terms unlinked; Trust linked.
- R5 "Disagreeing with an idea, or finding a topic uncomfortable, is not a fault and is not grounds for a refund." → Trust (s.2) or Disclaimers (s.4). Unlinked.
- R6 "A refund may be considered only where both of the following apply: your access to purchased content is suspended for 7 consecutive days or more, and the cause is attributable to us ..." → Terms (s.8). Unlinked.
- R7 "Where required by law, you may be entitled to a remedy if digital content is faulty, not as described, or not fit for purpose." → Terms (s.11). Unlinked.
- R8 "All refund decisions are made in accordance with this refund policy, our Terms &amp; Conditions, and applicable law." → Terms. Vicinity.
- R9 "Refunds are made in United States (US) dollars, the currency in which you paid." → Disclaimers (s.10). Unlinked.

**Terms**
- T1 "They explain your rights and responsibilities as a customer, how access to our training materials works, and the conditions relating to refunds and cancellations." → Refund. Unlinked.
- T2 "Educational recognition awarded within Achology's framework only, not a licence or statutory qualification." → Disclaimers (s.6). Unlinked.
- T3 "Achology's online learning and discussion environment, including peer interaction spaces." → Trust (s.5). Unlinked.
- T4 "Where necessary, we may contact you by telephone, email, or post using the contact details you provide when placing an order." → Privacy. Unlinked; Terms never links Privacy.
- T5 "Achology certifications reflect educational achievement within our framework only and do not confer legal or professional authority outside of it." → Disclaimers (s.6). Unlinked.
- T6 "Our 14-day money-back guarantee We offer a full 14-day money-back guarantee on all products except community membership." → Refund. Unlinked.
- T7 "Once access has been granted, Community subscriptions are non-refundable, although you may cancel at any time to prevent future payments." → Refund (s.3). Unlinked.
- T8 "To cancel your contract or request a refund, please contact us using one of the following methods: ..." → Refund (s.9). Unlinked.
- T9 "By placing an order, you confirm that you have read, understood, and agreed to the Refunds Policy in addition to these Terms." → Refund. Vicinity.
- T10 "Achology is not responsible for your devices or for maintaining their functionality, security, or compatibility with our digital content." → Disclaimers (s.11). Unlinked.
- T11 "Our products are provided for personal and educational use only." → Disclaimers (s.1). Unlinked.
- T12 "These sessions are practice-only learning activities." → Disclaimers (s.7) or Trust (s.5). Unlinked.

**Trust**
- TS1 "... Achology does not provide emotional regulation, crisis management, therapy, or psychological treatment." → Disclaimers (s.2). Vicinity.
- TS2 "Education increases responsibility; it does not remove it." (in the learner-responsibility list) → Code of Ethics. Unlinked; Trust never links Code of Ethics or Manifesto.
- TS3 "... While Achology moderates community spaces to uphold standards of respect and integrity, we do not assume responsibility ..." → Code of Ethics. UNSURE.
- TS4 "Achology makes no guarantees regarding: personal transformation emotional outcomes professional success income, status, or recognition ..." → Disclaimers (s.5). Unlinked.
- TS5 "We commit to: teaching honestly setting clear boundaries acting in good faith correcting errors when identified ..." → How We Write. Unlinked.
- TS6 "Achology's relationship with its learners is based on mutual respect between autonomous adults." → Manifesto. UNSURE.

**Disclaimers**
- D1 "Achology.com is owned and operated by Achology Transactions Ltd, a company registered in the United Kingdom." → Terms (s.1). Unlinked.
- D2 "Completing an Achology course demonstrates study and applied competency within our own certification and accreditation framework, which is explained openly on this website, ..." → Terms (s.3); UNSURE, may be /accreditation/ (outside the family, not built). No link.
- D3 "They are not medical care, psychological therapy or crisis support, and they are not a substitute for any of those things." → Trust (s.3, s.4). Unlinked.
- D4 "Achology Transactions Ltd operates in line with United Kingdom consumer protection law." → Terms (s.11). Unlinked.
- D5 "How you interpret, apply, or respond to what you learn is your responsibility." → Trust (s.1, s.3). Unlinked.
- D6 "Offence is a subjective response and does not indicate wrongdoing, harm, or fault on the part of Achology." → Trust (s.2). Unlinked.
- D7 "Achology makes no guarantees regarding: personal change or development ..." → Trust (s.6). Unlinked.
- D8 "Achology certifications: reflect educational achievement within Achology's framework only ..." → Terms (s.3) or Trust (s.4). Unlinked.
- D9 "Achology does not employ, supervise, regulate, or vouch for practitioners who have completed our courses, and their clients are not Achology's clients." → Code of Ethics. Unlinked.
- D10 "Achology: does not supervise peer interactions ..." → Trust (s.5) or Terms (s.12). Unlinked.
- D11 "... is not responsible for external privacy practices or policies ..." → Privacy (s.17) or Cookie (s.6). Unlinked.
- D12 "Many of the articles, guides and workbook resources on achology.com are written with the help of artificial intelligence (AI) writing tools, ..." → How We Write. Vicinity.
- D13 "Achology's services and content are designed for adults aged 18 and over." → Privacy (s.1). Unlinked.
- D14 "Our prices are shown in US dollars." → Refund (s.8). Unlinked.
- D15 "They're our own reading of each book, not the author's, ..." → Cookie (s.6, Amazon affiliate) or How We Write. UNSURE. The affiliate commission is disclosed only on Cookie.

**Privacy**
- P1 "Achology is the trading name of Achology Transactions Ltd." → Terms (s.1). Unlinked.
- P2 "Our services and content are designed for adults aged 18 and over." → Disclaimers (s.10). Unlinked.
- P3 "... post, upload, or submit content (including articles or blog posts) within the community; ..." → Terms (s.5). Unlinked.
- P4 "Consent : where required by law, such as for certain marketing communications or non-essential cookies." → Cookie. Unlinked in that section.
- P5 "Payment data is handled securely and, where applicable, processed by third-party payment providers rather than stored directly by us." → Cookie (s.6). UNSURE.
- P6 "When you follow these links or are redirected to another website, you are subject to that third party's privacy and cookie practices." → Cookie. Vicinity.
- P7 The closing "work together" sentence leaves out Accessibility and How We Write, which Disclaimers' framework table includes.

**Cookie**
- C1 "We do not use advertising or ad-targeting cookies on achology.com, and we do not sell data collected through cookies." → Privacy (s.7). Unlinked.
- C2 "Non-essential cookies (the analytics cookies above) are set only if you consent through the cookie banner ..." → Privacy. Unlinked.
- C3 "Email sign-up forms : our email list runs on Kit ..." → Privacy (s.7). Unlinked.
- C4 "Book links : some book recommendations on our Knowledge Hub, ... link to Amazon through affiliate links." → How We Write or Disclaimers. Unlinked.

**Accessibility**
- A1 "Achology.com is an online applied psychology training academy operated by Achology Transactions Ltd, trading as Achology." → Terms (s.1). Unlinked.

**How We Write** (links no family page except its breadcrumb)
- H1 "Before publication, every article is approved by our in-house editorial team under standards set by the senior management team." → Disclaimers (s.9). Unlinked.
- H2 "Human review helps ensure that our content is factual and evidence-based, with claims supported by evidence where available." → Disclaimers (s.9). Unlinked.
- H3 "This process helps ensure it accurately reflects Achology's policies, accreditation processes, and organisational teaching standards." → /policies/ (plus Manifesto and Code of Ethics). Unlinked.
- H4 "We can correct any page, workbook, article, or policy page." → /policies/. Unlinked.
- H5 "Let us know if you spot an error on any of our pages." → Trust (s.7). UNSURE.

**Manifesto** (links no /policies/ page)
- M1 "Our Code of Ethical Practice, developed by the Society of Modern Applied Psychology ( SoMAP ), ..." → Code of Ethics. Vicinity.
- M2 "Get FULL Access for $7 If $7 is within your budget, get a full 30-day trial Achology membership" → Refund (s.3) or Terms (s.3). Unlinked.
- M3 "Each course comes with lifetime access, and the opportunity to study at your pace" → Terms (s.3). Unlinked.
- M4 "The role of an Achologist is plain: act with integrity ..." → Code of Ethics. UNSURE.

**Code of Ethics** (links no /policies/ page)
- E1 "... before engaging in any form of professional practice or working with clients." → Disclaimers (s.6) or Trust (s.4). Unlinked.
- E2 "The difference is what separates trained Senior and Master Achologists from traditional therapists, counsellors and coaches: ..." → Disclaimers (s.2). UNSURE.
- E3 The help cards "Is Achology therapy, counselling, or coaching? None of the three." and "What does my Achology certificate actually prove? ..." point to help answers, not to the policy pages → Disclaimers or Trust.
- E4 "Each course comes with lifetime access ..." → Terms. Same as M3.

**Index**
- I1 "... supported by seven legal policies, a Manifesto, and a Code of Ethics ..." → the cards below. Vicinity, no action needed.

#### 2. Same subject, said differently

1. **Outage refund.** Terms s.8: "... You may also end the contract and receive a full refund if: there is a material error in the price or description of the product you ordered; or we suspend access to the purchased products for technical reasons for a continuous period of 7 days or more." Refund s.6: "A refund may be considered only where both of the following apply: ... and the cause is attributable to us, ..." Refund also leaves out the material-error ground. Terms says it prevails on any inconsistency.
2. **Who the 14-day guarantee excludes.** Refund: "This guarantee applies once per customer per product." and "... it does not apply where your access has been withdrawn because of a breach of our Terms (see section 5)." Terms: "This 14-day guarantee does not apply to Community subscriptions." Terms has neither of Refund's extra limits.
3. **What access can be withdrawn for.** Trust: "Withdrawal of access is reserved for behaviour that genuinely endangers or exploits others: predatory conduct, harassment, or unlawful activity." Terms s.9: "We may end this contract if you materially breach these Terms, including where you: fail to make a payment ... or breach clause 4 (Prohibition on Recording or Sharing Content)." Refund s.5 adds "misuse of the platform or learning materials". UNSURE whether Trust means community access only.
4. **Which company.** Index: "... through two registered companies in Scotland, UK ..." (the link goes to one company). Terms: "Achology is the trading name of Achology Transactions Ltd (ATL), ..." Disclaimers: "Every course, school bundle and membership sold on this website is created, published and delivered by us." Privacy: "Group and joint controllers : Including Kain Ramsay Limited, where relevant to providing access to courses, events, or related educational services."
5. **Free or paid membership.** Manifesto: "Join Achology today for free ..." Code of Ethics: "... free with a basic Achology membership ." Terms: "Achology Membership is a renewing subscription." Refund: "The monthly plan is $7 for the first 30 days and then the standard monthly rate (currently $34.50 per month)."
6. **$7 "trial".** Manifesto: "get a full 30-day trial Achology membership". Refund and Terms: it renews at $34.50 and "membership is non-refundable." UNSURE: may be an omission rather than a conflict.
7. **Lifetime access.** Manifesto and Code of Ethics cards: "Each course comes with lifetime access, ..." Refund: "Where lifetime access applies, ..." Terms: "... the length of access (where applicable), ..."
8. **Who the Code of Ethics binds.** Index: "... every practising Achology member pledges to uphold." Code of Ethics: "... asks two things of every Achology member and student alike, without exception: ..." Manifesto: "... sets expectations for all members, ..."
9. **Practitioners (UNSURE).** Disclaimers: "Achology does not employ, supervise, regulate, or vouch for practitioners ..." Code of Ethics: "... a required part of the accreditation process for every Master Achologist to maintain their status." Terms: "Achology may ... set or revise ongoing education or maintenance requirements ..."
10. **Moderation (UNSURE).** Trust: "... While Achology moderates community spaces ..." Disclaimers: "Achology: does not supervise peer interactions ..."
11. **Content approval and AI scope.** How We Write: "... every article is approved by our in-house editorial team ..." then later "... then reviewed and approved by Achology's management team." Disclaimers: "Every page is reviewed and approved by our in-house editorial team ..." On scope, How We Write says "Every page" and later "most"; Disclaimers says "Many".
12. **Refund contact routes.** Terms gives telephone, email and contact form; Refund gives email and online only; Privacy has no phone; Cookie gives email and online; Accessibility gives email, phone and form.
13. **Analytics as personal data (UNSURE).** Cookie: "... anonymous-style analytics ..." Privacy: "Technical and usage data : Information collected through cookies ..."
14. **Resellers (UNSURE).** Disclaimers: "... no other organisation is entitled to sell Achology training ..." Privacy: "... third-party marketplaces or platforms through which you have purchased Achology courses or events; ..." Disclaimers elsewhere: "... Udemy or Skillshare, where many of our courses were once available."
15. **Coaching (UNSURE).** Code of Ethics card: "Is Achology therapy, counselling, or coaching? None of the three." Manifesto: "... in the art and craft of teaching, coaching and mentoring, ..." Index: "... its online teaching and mentorship activities."

**Checked and consistent:** the 14-day window with no reason needed; membership non-refundable once access starts; 3 months free membership with a course, then $34.50 a month; the statutory cooling-off waiver; consent for non-essential cookies; age 18 and over; prices and refunds in US dollars; what a certificate means; the cross-references to Terms sections 8, 9 and 12 land on the right sections; data retention appears only on Privacy.

#### 3. Pages with few inbound family links

- No page has zero inbound links, and none is linked only from the index.
- Four have one source besides the index: Accessibility (Disclaimers, 1 link); How We Write (Disclaimers, 3); Manifesto (Code of Ethics, 1); Code of Ethics (Manifesto, 1).
- The index is linked from all eight /policies/ pages (breadcrumb, plus a body link on Accessibility and Cookie). Manifesto and Code of Ethics do not link it.
- Outbound gaps: How We Write links only to its breadcrumb; Manifesto and Code of Ethics link only to each other; no /policies/ page except the index links to Manifesto or Code of Ethics; Terms never links Privacy, Cookie, Accessibility or How We Write.

#### 4. Existing links (from, to, count)

| From | To | Count |
|---|---|---|
| /policies/ | each of the ten cards | 1 each |
| privacy-policy | /policies/ 1, cookie-policy 3, terms-and-conditions 1, refund-policy 1, disclaimers 1, trust-statement 1 | |
| terms-and-conditions | /policies/ 1, refund-policy 2, trust-statement 3, disclaimers 2 | |
| cookie-policy | /policies/ 2, privacy-policy 2, terms-and-conditions 1 | |
| refund-policy | /policies/ 1, terms-and-conditions 3, disclaimers 2, trust-statement 3 | |
| trust-statement | /policies/ 1, disclaimers 3, terms-and-conditions 2, refund-policy 2 | |
| disclaimers | /policies/ 1, terms-and-conditions 3, trust-statement 2, refund-policy 4, privacy-policy 2, how-we-write 3, cookie-policy 1, accessibility-statement 1 | |
| accessibility-statement | /policies/ 2, terms-and-conditions 1, privacy-policy 1 | |
| how-we-write | /policies/ 1 | |
| /about/manifesto/ | /about/code-of-ethics/ 1 | |
| /about/code-of-ethics/ | /about/manifesto/ 1 | |

The /policies/ counts include the "Policies" breadcrumb.

## Part C: Testimonials (/testimonials/)

- **Share image:** `Achology-OG-Default-Image.png` (uploads 2026/06), which is Rank Math's site-wide default Open Graph image (`rank-math-options-titles` → `open_graph_image`, read on the install this session). The page sets none of its own.
- **Theme version:** 0.707.3.
- **Block order:** matches the draft spec's ten-block table. Rendered in `<main>`: the header (H1 "Achology: In Their Own Words"), the answers block (`tm-answers`), the global impact block (`gi-block`), "Five Aspects of the Achology Learning Experience", the site gateway (`policy-next--pair`), Related Questions (`help-popular`), the closing enquiries panel (`warm-room`); sticky header, breadcrumb, rainbow stripe and footer sit outside `<main>` as locked chrome.
- **Schema emitted:** WebPage, WebSite, EducationalOrganization, BreadcrumbList. No VideoObject, as Chat read.

## Part D: About (/about/)

- **Share image:** the same Rank Math site-wide default, `Achology-OG-Default-Image.png`; the page sets none of its own.
- **Theme version:** 0.707.3.
- **Member-story VideoObjects:** the live page emits **none**. The schema is built by `achology_about_videos()` from the ACF group in `about-setup.php`, which drops any row missing one of Google's required properties; the page's comment reads "Until Kain and Karen fill the group in, this emits nothing", and the live page confirms nothing is emitted. Schema emitted: AboutPage, WebSite, EducationalOrganization, BreadcrumbList.
- **The five-question selector, desktop against phone** (`about.css` section 6): from 1024px up it is two columns, the five questions in a 300px left column and the open answer spanning all five rows on the right, the last question bottom-aligned to the answer's last line, the open question marked with a small pointer. Below 1024px there is no grid: each answer sits directly under its own question in source order. Every answer is in the delivered HTML at every width (DSRD 3 section 2.4); the selector only moves a class.

## Part E: the three quote page headings

- **Stylesheets and scripts:** nothing reads the three strings. A search of every `.css`, `.js`, `.php` and `.py` file in the theme and its tools this session found them only in a comment in `single-quote.php` (line 118, describing the S356 ruling), never in code.
- **The importer** (`import_quote_pages.py`) and the other factory scripts: no reference to the strings.
- **`search_gate.py`:** no reference.
- **Schema code:** no reference; the quote page schema reads the record fields, not the headings.
- **Does the page gate pass a quote page whose second or third heading differs?** Yes: `page_gate.py` contains none of the strings and checks heading levels and anchors, not wording.
- **The only thing that reads them by exact text is `content_gate_standards.json`** (Cowork's content gate), as Chat already found, plus the quote page SKILL, DSRD 2, DSRD 10, the Cowork Production Harness and the approved prototype as documents.

## Part F: housekeeping

- `RULING__Close_The_42_Articles_Card_Today_Both_Blockers_Top_Priority_S383`: **still open.** Remains: `page_gate.py` measuring a banded page's first row, then the 42 re-swept (item 3 of this session's order).
- `RULING__Close_The_Help_Section_Card_Three_Checks_Before_Kains_Read_S383`: **still open.** Remains: DSRD 6 records on the 250 help answers and the three confirmations in one reply (item 4 of this session's order).
- `RULING__Kain_Names_The_Footer_Himself_Final_Words_S385`: **still open.** Waits on a theme session building option A with Kain's words; /courses/ now exists (published S138), /enquiries/ is still not built.
- `CHECKLIST__Seven_Cards_Close_To_Done_What_Closes_Each_And_The_Line_That_Marks_It_S374`: **still open.** It is the list the seven cards close against; items 4 and 5 still need a home named by Chat.
- `CHECKLIST__The_Book_Note_Page_Second_Safari_Look_Nine_Rulings_And_How_The_Card_Closes_S374`: **still open.** Items 1 and 3 to 7 wait on a Safari sitting; 2, 8 and 9 are built.
- `COMMISSION__The_Card_And_Chrome_Sweep_S273` and `APPROVED__A_Fifth_Chrome_Sitting_The_Author_Signature_Block_S303`: **still open.** Both wait on theme sittings with Kain.
- `RULING_AND_BRIEF__Set_Up_The_Factory_Session_Timer_On_The_iMac_4_S353`: **still open**, waits on Kain at the keyboard. `RULING_AND_BRIEF__The_Karpman_Workbook_Is_Approved_Render_It_Into_The_Approved_Template_S353`: **still open**, item 7 of this session's order.
- `REPLY__Every_Answer_Owed_On_The_S108_To_S110_Rulings_S357`: **still open**, builds 1 to 5, 8 and 9 wait on the foundations sitting. `REPLY__Courses_Spec_Updated_Disclaimers_Recorded_Policy_Images_Noted_S386`: **done**, no longer in FROM Chat (archived earlier). `REPLY__Course_Card_And_Courses_Page_Rulings_Recorded_The_47_Lines_Ruled_S387`: **still open**, the course card's S136 and S137 export into its component folder is owed (item 8 of this session's order).

OWED BACK: nothing from Chat to Code on this reply.

*No em or en dashes in this file; checked before writing.*
