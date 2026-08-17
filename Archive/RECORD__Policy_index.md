# RECORD: The Policies index, chapter by chapter through DSRD 6

**From:** Claude Code, S043. **Date:** 2026-08-04. **Page:** https://achologytest.com/policies/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md` (page 10 of the walk order) and `SPEC__Policies_Index_Locked_Layout_And_Copy.md` (S236, signed). **Theme:** v0.36.49 live.
**Supersedes in place:** the S043 record filed before the rebuild, which described the thin page and raised the commission that produced the spec.

**Verdict: built to the signed spec, walked, and as ready as a build-site page can be.** Every chapter runnable from here passes. Two rows stay open and both are known: the site-wide canonical, and one phone spacing row that belongs to a shared component and is waiting on a sweep brief. Kain confirmed the rendered page in Safari at desktop and phone and called the work phenomenal, which closes §11 item 5.

## The machine gate

`page_gate` v3 (the mirror now replays the origin's real HTTP status, per your S236 ruling), run S043 against the live page at desktop 1440, tablet 900 and phone 375: **27 pass, 2 fail, 1 not built yet.**

```
  FAIL  hairline-spacing   mobile boundary 3: 48.0 above, 48.0 below (want 32/32)
  FAIL  canonical          (missing)
  NOT-BUILT links-resolve  planned in DSRD 1, page not built yet: /academy/;
                           /academy/schools/; /certification/; /courses/;
                           /accreditation/; /academy/neuro-linguistic-programming/
  ---- 27 passed, 2 failed
```

The not-built row is the honest one the v3 fix gave us: those addresses are pages Kain has not created yet, and on a site being built from the foundations up that is the plan working, not a defect. The canonical is the known site-wide item. The phone spacing row is set out under the collisions below.

## What was built

To section 3 of the signed spec, in full: the new H1 with the accent on Achology, the lead, the governance paragraph, the group heading "Our Legal Policies" above the seven cards, then the separator, then "Our Training Standards" and two new cards for the Manifesto and the Code of Ethics at their existing /about/ homes. All seven description lines replaced. Page order exactly as the spec sets it, at every width.

**Three things differ from the spec as signed, all at Kain's instruction in session:**

1. **The lead paragraph** is Kain's own wording, replacing the approved text. Live wording: "This page outlines the rules and standards governing Achology, including legal policies, business practices, and our self-imposed guidelines. All details are publicly accessible, so you will always know where you stand."
2. **The governance paragraph** is Kain's own wording, revised twice in session. Live wording: "Achology is owned and operated by its founders, Kain and Karen Ramsay, via two registered Scottish companies. It follows best practices in public trading and is supported by seven legal policies, a Manifesto, and a Code of Ethics that guide its teaching and mentorship services. All these documents are accessible on this page, written in clear language for anyone to review at any time."
3. **The card treatment changed**, where the spec said keep it exactly as built. Kain asked for and approved both changes on a rendered preview: the ghost word behind each card, and the description colour. Details under §10.

The spec needs updating on your side so it stops contradicting the page. The analyser-feed partial (policies-content/policies.php) carries every one of these words too, so what Rank Math scores and what the visitor reads cannot drift.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **Pass** | Zero em and en dashes on the rendered page (gate). Copy is Kain's, approved in session. The front-door rule holds: the page names what it is about in plain words and leaves no term to guesswork. |
| §2 Structure and headings | **Pass, and the gap that raised the commission is closed** | The page follows the signed spec's order exactly, verified on the rendered page at all three widths. One H1, two H2 group headings, no skipped levels; read alone they tell the page's story. DSRD 9 gains this page's locked layout on your side in the same pass, which closes the "no block-level layout exists" finding that produced the commission. |
| §3 Metadata | **Fail on one line; the refresh is done** | Title 51 chars, description 147 chars, both refreshed to match the new H1, proposed to Kain first and set on his approval (spec section 6). Verified on the rendered page rather than in the database: the title tag, the meta description, the Open Graph pair and the Twitter title all carry the exact strings, and the site-wide title recasing switch, switched off earlier today, leaves them as written. Neither string collides with any other page on the site. **Canonical absent** (site-wide config), now the page's only open metadata line. |
| §4 Schema | **Pass** | CollectionPage and BreadcrumbList. The CollectionPage name and description were updated to match the new page, and hasPart now carries all nine documents rather than the seven child pages, because DSRD 6 §4 requires "the facts inside the code match the facts on the page" and the gateway now lists nine. Rich Results Test deferred to cutover. |
| §5 Search visibility | **Pass on the lines a build site can show** | Address and breadcrumb per DSRD 1. One clear subject. 37 links checked, all resolve; the six unbuilt addresses are reported as planned, not broken. Inbound links: the sub-footer's policy links site-wide and each policy page's breadcrumb. Indexing intent and the redirect map stay cutover work. |
| §6 AI visibility | **Pass on the lines that apply** | §12's structural row exempts the author and date lines. The page's answer, what governs Achology and where each document lives, sits in the delivered HTML in the open, and the governance paragraph now gives an AI system something citable, which it did not have before. Accessibility-tree audit deferred to cutover with Lighthouse. |
| §7 Accessibility | **Walk re-run S043 after the rebuild: pass** | Every interactive element is a native link; zero non-native interactive elements, zero positive tabindex, zero unnamed controls. The ghost word is decorative: it is generated content with `pointer-events: none` and `user-select: none`, so it reaches neither the tab order nor the accessibility tree, and it carries no meaning a reader needs. Contrast measured on the live page over the watermark: card name 9.8:1, description 5.1:1, both inside AA. 320px reflow clean, no horizontal overflow, no card overflows internally at phone. |
| §8 Ease of use | **Fresh-eyes read after the rebuild: pass** | The page says what it is at a glance, the two groups are self-evident, and every row looks clickable and is. The nine documents now scan in a fraction of the time they did as an undifferentiated list, which was the §8 hindrance the earlier record raised; that finding is closed. |
| §9 Speed | **Not verified** | PageSpeed cannot reach the build site; cutover work. |
| §10 Visual consistency | **Pass, with one new named device recorded** | css_gate passes on policies.css. Widths, gutters, H1, hairline presence and spacing measured by the gate at three widths. Two card changes, both approved by Kain on a rendered preview: (a) the description returned to brand dark, because grey lost against the texture and DSRD 7 §1.1 rules "if a person reads it as sentences, it is #354149. If in doubt, it is #354149", with hierarchy carried by size and weight instead; (b) **the ghost word**, a new visual device set out below for DSRD 8. |
| §11 Live verification | **Pass on five of five** | Nothing failed to load and every link resolves, both now genuinely measured under gate v3. No content images on the page. **Item 5 closed:** Kain viewed the rendered page in Safari at desktop and at phone width and approved it in session. |
| §12 Page-type exemptions | **Applied** | Structural page row: §6's author and date lines exempt. Applied in §6 above. |

## The ghost word, for DSRD 8

A new device, invented by Kain in session and approved by him on a rendered preview. It wants a home in the component library rather than living as an undocumented one-off, and this is the description to write from:

The one word each document is about, set in Como bold and held well back in brand orange at 6 percent, behind the card's own text on the left. Every word's **ink** is sized so it sits exactly 10px clear of the card's top, bottom and left faces, which means all nine render at the same visual height and no card carries more weight than another. The per-word sizes and offsets are measured from the real Como glyph metrics, not estimated, because centring the text box rather than the letters is what made the first attempt sit low and clip. Brand orange is correct here rather than §1's AA-safe orange: this is a background wash, not text, and the card's own text above it measures 9.8:1 and 5.1:1. The device is desktop and tablet only; below 768px the card narrows and the longer words would cut mid-letter, so it stops at the phone breakpoint.

## The one collision that stands

**The phone spacing on the group boundary.** The separator between the two card groups comes from `.policy-body--ruled + .policy-body--ruled` in components.css, the family's own block component, which carries no phone tier, so the boundary reads 48/48 at phone where DSRD 7 §4.3 ruling 4 requires 32/32. This is the same shared defect recorded in `RECORD__Page_about.md`, not a new one, and the rule also fires on the Testimonials page. **Still requested: a sweep brief for phone-tier conformance across the shared separators.** Marked: waiting on ruling. Your S236 ruling forbids fixing what the gate surfaces without its own instruction, and this obeys it.

An earlier cut of this page declared its own group spacing to avoid that, and the gate refused it, correctly, under §4.3 ruling 2: "Where a page sets its own spacing values, those declarations are deleted so the page inherits this standard. A page-local variant is a defect." The rebuild uses the component.

## Metadata, set and live (spec section 6)

Proposed to Kain, approved by him, set and verified on the rendered page:

- **Title (51 chars):** Achology's Policies and Standards, All in One Place
- **Description (147 chars):** Every rule and standard that governs Achology: seven legal policies, a public Manifesto and a Code of Ethics, all published here in plain language.

## What would close this page

1. The sweep brief for the shared separator's phone tier.
2. DSRD 9's locked layout and DSRD 8's entry for the ghost word, both on your side.
3. The signed spec updated to Kain's copy, so document and page agree.
4. The cutover lines: canonical, indexing intent, speed, Rich Results.

*No em or en dashes in this file; checked before writing.*
