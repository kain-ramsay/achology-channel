# RECORD: Testimonials, the DSRD 6 walk, page 6 of 6

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`,
the last page in its order.
**Page:** https://achologytest.com/testimonials/
**DSRD 6 read in full this turn**, version 5, before any chapter was judged.

**Verdict: not ready. Four chapters fail, one carries a question, and none of
the failures is page-local.** Every one belongs to a shared component, a shared
stylesheet, or copy, which is stated per chapter rather than left to be
inferred.

**Nothing on the page was changed.** Under the walk instruction's item 3 I fix
only what a written standard fails, and every failure below either has no line
to quote yet, or belongs to a component whose look Kain approved.

---

## The machine gate

`page_gate`: **38 passed, 4 failed, 2 carved out.**

The four are the `boundary-owner` rows on desktop boundaries 5 and 6, and
**they are resolved by your S255 ruling**, which I am quoting as the authority
for the chapter per your own instruction that a filed ruling stands until the
DSRD carries it:

> "**Policy Closing Panel** (`.policy-closing`) and **Policy Related Strip**
> (`.policy-related`): the closing-boundary pair, authored once in `about.css`,
> used on the policy template family, About, and Testimonials. Their desktop
> closing boundaries carry 48px margin-top and 48px padding-top, as built and
> approved on the rendered pages."

**The gate will keep printing those four until DSRD 8 carries the two names**,
because `component_classes()` reads DSRD 8 itself and finds nothing. That is
the gate being honest rather than wrong: it reports what the document says
today. When your DSRD 8 edit lands, they turn green with no code change. I have
recorded them below as passes on the ruling, and the gate printout as it stands.

---

## The chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| **§1 Copy standards** | **FAIL, one term certain, two more to rule** | Zero em and en dashes (gate). Body read top to bottom. **The fail: "Achologist".** Five uses, first is "Nine Achologists. Five Questions", with no identification anywhere on the page. §1 names it explicitly in its own list: "a member, the membership, the community, the academy, the pathway, a school, the directory, **an Achologist**, a credit". A stranger from a search result is left holding it. **Two more for your ruling rather than my judgement:** "member" and "membership" appear 12 and 4 times with no plain identification, and §1 names both in the same list, though "Member Testimonials" is the page's own subject so the §1 heading carve-out may cover the first; and "UK" appears once, in the member location "England, UK", the only acronym on the page. **Fixing any of these is writing, so Rule 8 puts them with you and Kain.** |
| **§2 Structure and headings** | **PASS** | One H1, five H2s, no skipped levels. Read alone they tell the page's story: Achology: In Their Own Words, then Nine Achologists. Five Questions, Five Aspects of the Achology Experience, Explore and Experience Achology for Yourself, Related Questions, and the closing enquiries panel. Order matches the built page and reads true. |
| **§3 Metadata** | **FAIL on the preview image; the rest pass** | Title 48 characters, unique, subject in the first words. Description 129 characters, unique, reads like a sentence a person wrote. Canonical absent and **carved out**, per §3's own S245 carve-out for the build ground. **The fail: the preview image is the site default**, `Achology-OG-Default-Image.png`. §3 item 4: "the branded image assigned to this page's type ... **Never a default, never missing.**" **Checked across the site before calling it:** the policy pages and the Manifesto carry bespoke images (`Achology-Privacy-Policy.jpg`, `Achology-Manifesto.jpg`), so a per-page image is the built practice, not an aspiration. **About carries the same default and its record did not fail on it**, which is why this comes to you as a question rather than a defect: either both pages want an image, or the default is a recorded exception and About's record and this one should say so identically. |
| **§4 Schema** | **FAIL, the page emits none at all** | **Zero JSON-LD blocks on the page.** Verified by fetching the served HTML and counting: `application/ld+json` occurrences, Testimonials **0**, About **2**. DSRD 3 §5.3 assigns this page type "WebPage \| Rank Math auto \| None needed \| None". Rank Math is running on the page, since it emits the title, description and Open Graph tags, but it emits no schema. **Diagnosed rather than guessed:** every comparable page's schema is emitted by the theme, not the plugin. `template-policies-index.php`, `template-our-people.php` and `taxonomy-faq_category.php` each `echo` their own `application/ld+json`, and `page-about.php` does the same. `page-testimonials.php` does not. So the "Rank Math auto" row is the provisional one §5.3 warns about: "treat every 'handles automatically' row as provisional until then." **What it should emit is not written anywhere**, so under the walk instruction's item 4 this stops here rather than my choosing between WebPage and CollectionPage. DSRD 10 §9 Standard 3 makes BreadcrumbList the theme's, which suggests the pattern, but suggesting is not specifying. |
| **§5 Search visibility** | **PASS on seven of eight, one deferred** | Address matches DSRD 1. One clear question. Indexing hidden on purpose (`nofollow, noindex`), correct for the build ground. Internal links present, 16 in the body, all resolving (gate: 48 checked, all resolve). Breadcrumb correct. Linked to, not orphaned: reached from the site header and from the About page's routes grid. Meaningfully unique: no other page answers "what do members say". **Deferred: the old-address redirect line**, which belongs to the redirect map and the live-site URL session, not to this walk. |
| **§6 AI visibility** | **PASS on the three that apply** | **Exempt from items 1 and 2** (author and date) under §12. The page is not Knowledge Hub content; it is a proof and routing page, and every §12 group other than Knowledge Hub content carries that same exemption, so the exemption holds whichever group it is filed under. That said, **§12 does not name Testimonials in any group**, which is a real gap in the table and is flagged below. Item 3, sources: the page's claims are members' own words, attributed by name and location, with nothing resting on an outside body. Item 4, the answer is in the delivered HTML: all nine transcripts sit in the served markup, not built by script, confirmed by reading the raw HTML rather than the DOM. Item 5, the accessibility tree: every one of the 17 images carries a description, none empty, none missing. |
| **§7 Accessibility** | **FAIL, two contrast items, both component-level** | Measured on the rendered page with **alpha properly composited**, which matters: my first pass reported three failures and two of them were my own measurement error, reading an 8% orange tint as solid orange. Corrected and re-run. **The two real ones:** the "Submit an Enquiry Here" button, white on brand orange #ED6922, 14px/600, **3.16 to 1** against the 4.5 required; and the member name "Jon Frost" and its eight siblings, #ED6922 on #F3F4F4, 14px/600, **2.87 to 1** against 4.5. **The button is not new:** 3.16 is the identical ratio already filed site-wide at S047 as `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md` for the "Start Your Trial" button. Same component, same fault, second location. **The member name appears to be new.** Both are colour decisions on components Kain approved by eye, so neither is mine to change. |
| **§8 Ease of use** | **PASS on the thirty-second checks; the full walk not run** | Krug's self-evidence and trunk tests run at desktop and phone: the page says what site it is, what page, where it sits, and what can be done; the question tabs read as clickable and use the visitor's own words. **Nielsen's ten-lens walk not run.** §8 requires fresh eyes and says "the walk is never run by the page's builder in the same sitting it was built". I did not build this page, so I am eligible, but a ten-lens walk done at the end of a very long session is the kind of pass that finds nothing because it was hurried. Recorded as not run rather than claimed. |
| **§9 Speed** | **NOT VERIFIABLE HERE** | §9's method note allows a page to pass on its type's representative result. PageSpeed Insights cannot fetch this page: the build ground is noindex and the host answers automated fetches with a challenge, the same reason recorded on every page in this walk. Images checked individually instead: all 17 load, none oversized for their slot. Deferred to the pre-cutover sweep DSRD 3 already requires. |
| **§10 Visual consistency** | **FAIL, `testimonials.css` does not pass its gate** | `css_gate` fails the file. The findings are hand-typed shadows (lines 97, 103, 111, 115, 120), two hand-typed `#000` at line 113, and two breakpoints at 720px and 719px which are not system boundaries. **These are pre-existing and are the same set already flagged as needing one question to Kain rather than annotation by me.** §10's three verdicts are collapse, name, or record an exception, and it says explicitly that annotating in a comment "is not one of the three". Every one of these is a look decision on a page he approved, so they go to him as one question, not as my annotations. |
| **§11 Live verification** | **PASS on three of five** | Everything loads: gate reports no failed asset, all 17 images return real bytes. Every link resolves: 48 checked, the six 404s are addresses DSRD 1 plans and nobody has built. Both external links carry `target="_blank"` and `rel="noopener"`; no internal link does. Every image carries a plain-words filename and a description. **Item 3, tracking: not assigned for this page type**, so there is nothing to fire and nothing to verify. **Item 5, Kain at tablet and phone: not yet done**, and it is his eye, not my measurement. |
| **§12 Page-type exemptions** | **QUESTION** | **Testimonials is named in no group in the table.** Not Knowledge Hub content, not a selling page, not in the About list, not a structural page as that row describes them. I applied the §6 author and date exemption anyway, because every group except Knowledge Hub content carries it, so the outcome is the same whichever it lands in and the ambiguity does not change a verdict. But the table should name it, or a later reader will make the call by judgement, which is what §12 exists to prevent. |

---

## What this needs, in the order that unblocks the page

1. **Name Testimonials in §12's table.** One row. Closes the only chapter whose verdict rests on my reasoning rather than a document.
2. **Rule the §4 schema.** What this page emits, and whether the theme emits it as it does on every comparable page. Then it is one function in `page-testimonials.php` and I build it.
3. **The §1 copy.** "Achologist" needs its identification, and the "member", "membership" and "UK" questions need a ruling. Yours and Kain's.
4. **The §3 preview image**, and the same answer applied to About, which carries the identical default.
5. **Kain's one question on `testimonials.css`**, the pre-existing shadows, colours and breakpoints, and his confirmation of the page at tablet and phone.
6. **Two contrast decisions for Kain**, the primary button at 3.16 and the member name at 2.87. The button is the site-wide one already filed at S047.

**Once DSRD 8 carries the two block names, the gate reads 42 of 42.**

## The re-verdict this record was also carrying

`ANSWER__Canonicals_Sweeps_And_Collapse_S245.md` §2 asked for the §1 chrome
re-verdict to be applied to Testimonials' record. **Applied: the chrome carve-out
closes nothing here, because this page's §1 failure is body copy, not chrome.**
The same was true of the Policies index, reported at
`RECORD__The_Three_Reverdicts_S051.md`. That file's third re-verdict is
therefore now delivered, and the S245 answer has nothing further owed on it.

*No em or en dashes in this file; checked before writing.*
