# RECORD: collapse pass three, the 404's six doors

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` item 3,
third caller. Follows `RECORD__Collapse_Pass_Two_Policy_Template_Routes_Rows_S051.md`.

## 1. The block family and its one home, named before starting

Family: the routes rows. One home: `achology_routes_grid()` in `shared-parts.php`.
Caller collapsed this pass: `404.php`, the "Where to instead?" block.

**Unlike pass two, this one renders.** Six rows on the live 404 page, so the
before-and-after diff is a test that could have failed.

## 2. What changed

`404.php` stops hand-authoring the block, and stops drawing its own icons. Six
`<svg>` blobs are gone from the template; the six doors now name registry keys.

**Compass joined the registry**, registered for this exact door at DSRD 7 §5.2,
404 page "Where next?" doors: "| About door | `Compass` | 18px, Learn about
Achology |". Paths moved from this file, not retyped.

**The Knowledge Hub door keeps the drawing it has been rendering, and this is
worth your attention.** DSRD 7 §5.2 names that door `LibraryBig`. What is
actually on the page is the registry's `library`, a different drawing. Which
drawing the registry means by each of those two names is the open §5.2
question already filed to you at S050. This pass changed no glyph, so the page
is unmoved either way, but the answer will decide whether that door is right.

**Urls are root-relative, not `home_url()`,** for the reason set out in pass
two: the renderer decides a new tab from the address itself, and an absolute
internal address would open all six doors in a new tab against DSRD 3 §2.5.

## 3. Verified on the live page

The before-and-after diff of the rendered 404 is **one hunk, the block itself**.
Everything above and below it is byte for byte identical. Inside the hunk:

- whitespace and indentation, the renderer's own
- the HTML comment, now a PHP comment, no longer shipped to readers
- the six hrefs, absolute to root-relative

**Every class, every glyph path, every aria attribute, the arrow, the names and
the descriptions: identical.**

## 4. The gate, and eleven failures that are not mine

`page_gate` on the 404: **19 passed, 11 failed.**

The failures are the page's hairline spacing at two boundaries, the
`boundary-owner` rows underneath those, and a missing meta description.

**Proved pre-existing rather than assumed.** The old template was put back on
the server, the page re-measured, and it returned the same eleven failures,
line for line. The new template was then restored and the deployed file's
checksum matched local. So:

```
old template on the server:  19 passed, 11 failed
new template on the server:  19 passed, 11 failed   (the same eleven)
```

That is the whole reason for doing it that way. The alternative was to assert
they looked pre-existing, which is the thing the S050 lesson says not to do.

**The 404 has never been through the DSRD 6 gate.** It is not in the page order
in `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`,
which lists the policy family, the Policies index, About, Our People, the ten
profiles and Testimonials. Whether it should be added is yours to route; I have
not touched its spacing, because that is a different job from this one and
would need its own pass.

Also worth one line: `assets-load -> 404` is the gate reading the page's own
HTTP status, which for this page is correct and permanent. If the 404 is ever
brought through the gate it will want a carve-out row, the same shape as the
canonical one.

## 5. One thing caught by checking rather than by luck

Deleting the six icon variables also deleted the row arrow, which the
popular-questions strip further down the same file still uses. The PHP linted
clean, because an undefined variable is not a syntax error; it would have
rendered a missing arrow on the live page.

Restored, and left for that strip alone. The strip is a different block family
and moves under its own pass.

## 6. Where the register stands

| Family | Status |
|---|---|
| Routes rows | Open. **Four callers outstanding:** `help-parts.php`, `page-about.php`, `manifesto.php` (two copies), `code-of-ethics.php` (two copies) |
| Poster tiles | Closed, S048 |
| Circular member cards | Closed, S048 |
| About preview builder's CSS blob | Closed, S048 |

Next by size is `help-parts.php`, which renders on all 249 help articles.

Shipped to the build ground, cache purged, commit `d7e2210`.
Live: https://achologytest.com/this-page-does-not-exist-404-check/

*No em or en dashes in this file; checked before writing.*
