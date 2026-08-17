# RECORD: The Achology Manifesto, chapter by chapter through DSRD 6

**From:** Claude Code, S042. **Date:** 2026-07-29. **Page:** https://achologytest.com/about/manifesto/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md` (page 8 of the walk order). **Theme:** v0.36.34 at filing; record updated in place S043, 2026-08-03, on v0.36.35.

**Verdict: as ready as a build-site page can be; the S233 rulings closed the referred items.** The S042 header hairline fix stands verified. Since then: the instrument's artefact rows are fixed and pass (ruling 8), the reading order is fixed and shipped with the rendered page proven identical (ruling 9), and the page type is ruled (ruling 7). What stays open: Kain's word on the narrow widths (§11 item 5) and the cutover-only lines; the copy pack was applied S043 on v0.36.36 and verified live.

## The machine gate

`page_gate` v2 (the S233 ruling 8 amendment: hairline spacing measured from the geometrically nearest visible content edge, versioned in the script header), re-run S043, 2026-08-03, against the live page on v0.36.35: **23 pass, 1 fail.**

```
  PASS  hairline-spacing   desktop boundary 2: 48 above, 48 below
  PASS  hairline-spacing   tablet boundary 2: 48 above, 48 below
  PASS  hairline-spacing   mobile boundary 2: 32 above, 32 below
  FAIL  canonical          (missing)
  ---- 23 passed, 1 failed
```

The artefact you ruled on is closed exactly as ruling 8 predicted: under the geometric measurement the two spacing rows pass at 48/48 and 32/32, desktop stays passing, and the sole open row is the site-wide canonical already ruled out of page work.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **Pass, one heading correction referred** | Zero em and en dashes (gate). Terms identified: the Society of Modern Applied Psychology is spelled in full with (SoMAP) at first use. **Referred:** the H2 "Our Commitment to the SOMAP Code of Ethical Practice" renders the name as SOMAP against the canonical SoMAP the same page's body uses; the copy is yours and Kain's. |
| §2 Structure and headings | **Pass** | One H1 ("The Achology Manifesto"), six H2s, no skipped levels; read alone the headings tell the page's story from what the manifesto is, through the daily reading, to the calls to action. |
| §3 Metadata | **Fail, one line** | Title 55 chars, unique, subject first. Description 138 chars. **Canonical absent** (site-wide config). Preview image handled site-wide per the standing ruling. |
| §4 Schema | **Pass** | Emits AboutPage and BreadcrumbList. Rich Results Test unrunnable against the build site's bot protection; that line stays deferred to cutover, as on the policy family. |
| §5 Search visibility | **Pass on the lines a build site can show** | Address under /about/ per the built structure. One clear subject. 41 links checked by the gate, all resolve. Inbound links: the footer's About column links the page site-wide. Indexing is the build ground's deliberate noindex; redirects and the orphan check stay cutover work. |
| §6 AI visibility | **Closed by S233 ruling 7** | The page shows "This organisational standard was adopted on 17 Aug 2019", which the ruling accepts: the adoption date satisfies §6's visible-date line as the honest equivalent for a standards document, and a last-updated line is added only if the document is ever revised. Author line exempt under the policy-page row. The date now renders "17 August 2019" in full, applied S043 on v0.36.36 and verified on the live page, the page re-gated clean. The answer sits in the delivered HTML, in the open. |
| §7 Accessibility | **Pass on the page's own content; template items referred; one reading-order finding** | The policy-family template walk (S042) covers this page: keyboard travel, focus visibility, contrast, zoom and reflow, tap targets. Page-local: no overflow 320 to 1280, the document image loads and carries a true description ("The Achology Manifesto document"). **Finding closed S043 (S233 ruling 9):** the H1 now precedes the document figure and its buttons in code order, shipped in v0.36.35; a screen reader meets the page's title first. The rendered page was proven identical before shipping, at quarter-pixel resolution across every landmark and body line wrap at 1280, 768 and 375, and the gate passes above. |
| §8 Ease of use | **Walk run with fresh eyes: pass** | The page says what it is at a glance at desktop and phone; the two CTA pairs are self-evident; the daily-reading section answers why the manifesto matters in the reader's own terms. No blockers, no hindrances beyond the SOMAP heading above. |
| §9 Speed | **Not verified** | PageSpeed cannot reach the build site; cutover work, as on every page. |
| §10 Visual consistency | **Pass** | css_gate passes on policies.css after the change; the header now inherits the standard separator and the H1 renders Achology in the brand accent per the S227 rule, verified live. |
| §11 Live verification | **Pass on four of five, item 5 prompted** | Gate: nothing failed to load, every link resolves. The document image's filename (manifesto-document.jpg) is descriptive. **Item 5:** Kain approved the page on preview and called the shipped pages phenomenal; the explicit narrow-to-tablet-and-phone confirmation has been put to him and his word will close this line. |
| §12 Page-type exemptions | **Ruled (S233 ruling 7)** | The Manifesto belongs to the policy-page row. Applied in §6 above. |

## What would close this page

1. The SOMAP heading correction was applied S043 on v0.36.36 and verified on the live page, the page re-gated clean. (The gate measurement, the §12 and adoption-date ruling, and the reading order all closed S043 under rulings 8, 7 and 9; evidence in their rows above.)
2. Kain's word on tablet and phone widths (§11 item 5).
3. The cutover lines: canonical, indexing intent, speed, Rich Results.

*No em or en dashes in this file; checked before writing.*
