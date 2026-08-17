# RECORD: Achology Code of Ethics, chapter by chapter through DSRD 6

**From:** Claude Code, S042. **Date:** 2026-07-29. **Page:** https://achologytest.com/about/code-of-ethics/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md` (page 9 of the walk order). **Theme:** v0.36.34 at filing; record updated in place S043, 2026-08-03, on v0.36.35.

**Verdict: as ready as a build-site page can be; the S233 rulings closed the referred items and the copy pack covers every copy failure.** The S042 header hairline fix stands verified. Since then: the instrument's artefact rows are fixed and pass (ruling 8), the reading order is fixed and shipped with the rendered page proven identical (ruling 9), and the page type is ruled (ruling 7). The §1 SoMAP failure, the spaced-hyphen sentence, the adopted-on wording and the browser title were all corrected per the copy pack, applied S043 on v0.36.36 and verified on the live page, the page re-gated clean. Still open: Kain's word on the narrow widths (§11 item 5) and the cutover-only lines.

## The machine gate

`page_gate` v2 (the S233 ruling 8 amendment: hairline spacing measured from the geometrically nearest visible content edge, versioned in the script header), re-run S043, 2026-08-03, against the live page on v0.36.35: **23 pass, 1 fail.**

```
  PASS  hairline-spacing   desktop boundary 2: 48 above, 48 below
  PASS  hairline-spacing   tablet boundary 2: 48 above, 48 below
  PASS  hairline-spacing   mobile boundary 2: 32 above, 32 below
  FAIL  canonical          (missing)
  ---- 23 passed, 1 failed
```

The artefact is closed exactly as ruling 8 predicted: the two spacing rows pass at 48/48 and 32/32 under the geometric measurement, desktop stays passing, and the sole open row is the site-wide canonical already ruled out of page work.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **Fail on the acronym rule; one dash finding** | Zero em and en dashes by character (gate), but "Our code of ethics - also referred to as our ethical framework - asks two things" uses spaced hyphens as dashes, which the house standard replaces with commas or colons. **The failure:** the page says "issued by SoMAP" and the full name, the Society of Modern Applied Psychology, appears nowhere on the page; DSRD 6 §1 requires the full canonical name at or before first use. The Code of Character and Conduct is correctly written in full at every mention. The copy is yours and Kain's; both items are in the report. |
| §2 Structure and headings | **Pass** | One H1 ("Achology Code of Ethics"), seven H2s, no skipped levels; the headings alone carry the page's argument from what the framework is, through the two codes, to the training and the calls to action. |
| §3 Metadata | **Fail, one line** | Title 58 chars, unique, subject first (its title-case "Of" and "For" noted in the report). Description 148 chars. **Canonical absent** (site-wide config). Preview image handled site-wide. |
| §4 Schema | **Pass** | Emits AboutPage and BreadcrumbList. Rich Results Test deferred to cutover, as everywhere. |
| §5 Search visibility | **Pass on the lines a build site can show** | Address under /about/ per the built structure. One clear subject. 42 links checked by the gate, all resolve. Inbound links: the footer's About column site-wide, and the Manifesto page cross-links it. Indexing is the build ground's deliberate noindex; redirects and orphan check stay cutover work. |
| §6 AI visibility | **Closed by S233 ruling 7** | The shown adoption date satisfies §6's visible-date line as the honest equivalent for a standards document; a last-updated line is added only if the document is ever revised. Author line exempt under the policy-page row. The missing "on" and the full-month date format were corrected per the copy pack, applied S043 and verified live. The Rogers quotation is attributed to its source (On Becoming a Person, 1961). |
| §7 Accessibility | **Pass on the page's own content; template items referred; one reading-order finding** | The policy-family template walk (S042) covers this page. Page-local: no overflow 320 to 1280, the handbook image loads and carries a true description. **Reading-order finding closed S043 (S233 ruling 9):** the H1 now precedes the handbook figure and its two buttons in code order, shipped in v0.36.35 with the rendered page proven identical at quarter-pixel resolution at all three widths. The page-01.webp filename stands exactly as ruled in the copy pack: renamed only when the image is next touched. |
| §8 Ease of use | **Walk run with fresh eyes: pass** | The two-codes distinction, the training section and the CTA pairs all read self-evidently at desktop and phone. No blockers; the spaced-hyphen sentence is the one stumble. |
| §9 Speed | **Not verified** | PageSpeed cannot reach the build site; cutover work. |
| §10 Visual consistency | **Pass** | css_gate passes on policies.css after the change; the header inherits the standard separator and the H1 renders Achology in the brand accent per the S227 rule, verified live. |
| §11 Live verification | **Pass on four of five, item 5 prompted** | Gate: nothing failed to load, every link resolves. **Item 5:** Kain approved the page on preview and after upload; the explicit narrow-to-tablet-and-phone confirmation has been put to him and his word will close this line. The filename finding is recorded under §7. |
| §12 Page-type exemptions | **Ruled (S233 ruling 7)** | The Code of Ethics belongs to the policy-page row. Applied in §6 above. |

## What would close this page

1. The copy pack for this page (SoMAP in full, the spaced hyphens, the adopted-on wording, the browser title) was applied S043 on v0.36.36 and verified on the live page, the page re-gated clean. (The gate measurement, the §12 and adoption-date ruling, and the reading order all closed S043 under rulings 8, 7 and 9; evidence in their rows above.)
2. Kain's word on tablet and phone widths (§11 item 5).
3. The cutover lines: canonical, indexing intent, speed, Rich Results.

*No em or en dashes in this file; checked before writing.*
