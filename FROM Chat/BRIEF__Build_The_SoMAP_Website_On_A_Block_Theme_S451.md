> CODE DISPOSITION, S203: WAITS ON Kain's pick of the SoMAP home page (A, B, C or D), the brief's one question; read in full by the S203 theme main session, nothing built.

*Brief from Chat to Code, Session 451, 2 November 2026. Written on Kain's yes ("Yes, send it"). It folds into 000__PLAN__The_SoMAP_Website_And_The_Credentials_Centre_S450 (project 0004, Society of Modern Applied Psychology) and, where the two disagree, this brief wins. Nothing is built until Kain has answered the one question at the end.*

# Build the SoMAP website on a ready-made block theme, with the Credentials Centre inside it

## What done looks like

A simple, clean SoMAP website on Kain's SiteGround account, on a new WordPress install, on a hidden build address, carrying the signed SoMAP articles and the Achology Credentials Centre as one section of the same site. Built in days, at minimal cost. No page-by-page design rounds like the Achology site: the look is decided once and every page inherits it.

## What changes from the S450 plan

1. **No custom theme.** Section 7 of the plan said a classic theme called somap, copied from Achology's. That is replaced by one well-built, ready-made block theme, chosen by Code, lightweight and free or low cost.
2. **The brand is applied once, as the theme's global styles** (theme.json or the Site Editor's styles): Newsreader for headings, Hanken Grotesk for text, both self-hosted from Google Fonts under the SIL Open Font Licence; Teal #0F4C5C main, Brass #B08D57 decorative only (lines, rules, badges, never text), dark band #0B2E36, wash #F2F6F6, ink #1B2428, soft text #566168, hairline #DCE4E5. Achology's nine-step type scale (12, 14, 16, 18, 21, 24, 28, 33, 42) and 8 pixel spacing apply. The record is the brand plan in 05. SoMAP Design System.
3. **The look is decided once.** Kain picks the home page from the four options on the mock-ups canvas (https://claude.ai/artifact/Ns6MEJE7wU25dsXSDSgSBF; Chat recommends option B, The standard). Every other page follows that choice, in the same header, footer, buttons and spacing. No other design round is needed, except the two certificate designs, which come to Kain as four rendered options each, as the plan says.
4. **The Credentials Centre stays as one small purpose built plugin**, exactly as section 7 of the plan has it (own database tables, PDFs made on the server, signed copies, sign in by emailed link). Certificates must outlive any change of theme, so the plugin owns the data and the theme only draws the pages.
5. **Layout is modelled on what professional bodies do well** (BACP, ICF, EMCC, BPS and similar): a plain top menu, a membership and standards section, and a "check a practitioner" search. Take their structure only, never their wording, pictures or code.

## Theme choice (Code's call, Chat's recommendation)

Chat recommends WordPress's own default block theme of the year (Twenty Twenty-Five, or its successor if one is current): free, maintained by WordPress itself, fast, with the Site Editor and theme.json styling built in, nothing to licence, nothing to outgrow. Code confirms the choice against what is current on the day, checks it loads no unneeded scripts, and writes one line saying why if it picks another. Do not use a page builder, a form plugin or a certificate plugin. Keep the plugin list to the Achology essentials the plan names (Rank Math, Kit, WP Mail SMTP, Wordfence, Complianz, Zero Spam, the SiteGround speed tool).

## Page types (from section 4 of the plan, unchanged)

Home; About; Advisory Board; Governance; Partners; Our standards; Code of Ethics; Code of Character and Conduct; How verification works; The register and a register entry; Credentials Centre; Verify a certificate; A certificate's page (/v/{code}/); Request a certificate; My certificates; Udemy claim pages and Resend; Reviewer queue (sign in only); Articles library and an article; Raise a concern; Questions; Contact; Policies; Not found. Build them as block patterns and templates: one library template, one article template, one plain page template, one policy template. The articles library is the only listing.

## Fix these two things inside the build

1. **Links to SoMAP pages that do not exist yet.** The 48 launch articles link to site pages such as /standards/, /standards/how-verification-works/, /register/, /verify/, /raise-a-concern/ and to articles not yet imported. Chat will give Code the full list of link targets pulled from the signed records. Every one must resolve on the build site before launch, and Code runs a link check across all imported articles that fails on any 404.
2. **/raise-a-concern/ returns a 404 today.** It is a page in the plan (the complaints form, sent to the ethics committee). Build it in the first day, with the form posting to the ethics committee address Kain supplies, and the wording of SoMAP's rule of not naming a member before a decision taken from the Professional Accountability stance.

## What Kain must provide (plan section 10, and the new items)

1. The three existing certificate designs and both pairs of signature images, as the original files if possible.
2. Karen's list of every certificate already issued (name, course, date, kind).
3. The SoMAP inbox address and the reviewers' email addresses.
4. Who controls the thesomap.org domain, so the move can be arranged (Pooka and Co if it is theirs).
5. A yes on the 28 course list in the June course mapping workbook.
6. The advisory board confirmed: names, roles, photos.
7. The page copy: Chat drafts from the current site and REF 1; Kain reads and changes.
8. The two Kit follow-up email sequences, drafted by Chat for Kain to approve.
9. His logo and favicon, which he is designing himself (until then the site carries the SoMAP wordmark in Newsreader).
10. SiteGround access for the new install (a Site Tools login or an invitation).

## Order Code builds in

1. **Install and brand.** New WordPress on SiteGround, hidden build address, the chosen block theme, the brand set once as global styles, fonts self-hosted, header and footer, the plain page, policy and 404 templates.
2. **Articles.** The library and article templates; import the signed launch articles through the Publish Ready Pipeline (stages 5, 6, 7); the link check; /raise-a-concern/, /standards/ and the other pages the articles link to, with Chat's drafted copy as placeholders for Kain to approve.
3. **Home page.** Built to Kain's pick from the four options.
4. **Credentials Centre.** Course list, certificate record, IDs and QR codes, the two certificate templates as PDFs, verify page and certificate page, signed copies.
5. **Members and reviewers.** Request form, reviewer queue, emails through Kit, My certificates, Udemy claim pages and resend.
6. **Register and import.** The register and its search, the legacy certificate import, the seven June acceptance tests, every page checked in Safari at phone and desktop.
7. **Move.** thesomap.org to the new site with redirects, when Kain says go.

Steps 1 to 3 give Kain a working site with articles and no Credentials Centre; that is a real launch if the Centre needs longer.

## Cost

The theme, the plugins listed and the build cost nothing beyond the SiteGround plan Kain already has. If Code finds anything that costs money (a licensed plugin, a theme upgrade, extra hosting), it stops and names the amount in the next brief back to Chat. Chat puts it to Kain.

## What Chat still owes Code

The list of link targets from the signed articles; the drafted page copy; the Kit sequences; the pack and stances for any later article questions.

## The one question for Kain

Which of the four home pages does he want (A, B, C or D)? Chat recommends B.

*No em or en dashes in this file; checked before writing.*
