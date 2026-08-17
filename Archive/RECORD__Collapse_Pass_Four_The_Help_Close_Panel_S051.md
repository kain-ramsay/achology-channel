# RECORD: collapse pass four, the /help/ close panel, and the register is nearly empty

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` item 3,
fourth caller and the largest one.

## 1. The block family and its one home

Family: the routes rows. One home: `achology_routes_grid()` in `shared-parts.php`.
Caller collapsed: `help-parts.php`, `achology_help_pair_panel()`.

**This copy rendered on 249 help articles and 14 category pages.** It is the
one the register should have called the largest single win.

## 2. What changed, and what did not

**Kain's copy is untouched.** Both variants, the pre-purchase pair and the
support pair, keep their titles, leads, names and descriptions exactly as
written, including the verbatim support copy from 2026-07-16. The rows moved;
the words did not.

**The rows carry registry keys instead of raw path data.** Two of the four
drawings were not in the registry and are now, registered at DSRD 7 §5.2 for
these exact cards: "| Contact Our Support Team card | `Mail` | 18px, in the
36px orange-tint pair-card icon container |" and "| Ask an Achologist Anything
card | `MessageCircleQuestion` | 18px, same container ... |". Paths moved from
`help-parts.php`, not retyped. Unlock and GraduationCap were already there.

**The external test moved to the renderer's,** which asks the same question of
the same addresses: both community links go out in a new tab, the mailto is
left alone, per DSRD 3 §2.5.

## 3. One deliberate rendered difference, named rather than buried

The arrow loses a redundant `aria-hidden="true"` on the `<svg>` itself.

`achology_faq_row_arrow()` in `faq-icons.php` emitted the chevron with that
attribute; the registry's chevron does not carry it. It is redundant either
way, because the `<span class="policy-next__arrow" aria-hidden="true">` that
wraps it already hides the subtree, and every other routes block on the site
has always rendered without it. So this makes the help panel consistent with
the rest rather than changing what any reader or screen reader gets.

Flagging it because it is a real byte difference on 263 pages, and a pass that
claims "identical" while quietly dropping an attribute is the kind of claim
this project has been burned by.

`achology_faq_row_arrow()` still has other callers in the help section and is
untouched.

## 4. Verified on four pages, both variants, both templates

| Page | Template | Variant |
|---|---|---|
| `/help/comparisons-and-alternatives/` | category | pre-purchase |
| `/help/comparisons-and-alternatives/society-lost-gatekeeping-psychology/` | article | pre-purchase |
| `/help/technical-help/` | category | support |
| `/help/technical-help/what-to-include-achology-support-request/` | article | support |

**Every one: 17 changed lines, all inside the block.** Whitespace, and the
arrow attribute above. Every class, glyph path, name, description, the mailto
without a new tab and the community links with one: identical, and identical
enough that they do not appear in the diff at all.

## 5. The gate, and failures that are again not mine

```
help article    21 passed, 15 failed
category page   18 passed,  6 failed
```

**Proved pre-existing, not assumed.** The old `help-parts.php` was put back on
the server, both pages remeasured, and both returned the same counts. The new
file was then restored and both files' checksums matched local.

The failures are missing hairlines at the help section's own block boundaries
and one over-length meta description. **The /help/ section has never been
through the DSRD 6 gate**: the page order in
`INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md` covers
the policy family, the Policies index, About, Our People, the profiles and
Testimonials, and stops there.

That is now the second section this session found sitting outside the gate,
after the 404. Both are yours to route rather than mine to start.

## 6. Where the register stands

| Family | Status |
|---|---|
| Routes rows | Open. **Three callers outstanding, all on the quiet about-pages:** `page-about.php`, `manifesto.php` (two copies), `code-of-ethics.php` (two copies) |
| Poster tiles | Closed, S048 |
| Circular member cards | Closed, S048 |
| About preview builder's CSS blob | Closed, S048 |

Four of the seven copies are collapsed. The three that remain are all on pages
Kain has approved by eye, so they want more care than the 404 did, and the
About one also carries the warm-room panel question from S045.

Shipped, cache purged, commit `27faf35`.
Live: https://achologytest.com/help/technical-help/what-to-include-achology-support-request/

*No em or en dashes in this file; checked before writing.*
