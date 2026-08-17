# RECORD: collapse pass two, the policy template's routes rows, and a correction to the register

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` item 3, second caller.
**Register row:** DSRD 3 §2.6, Routes rows, "Six callers still outstanding: `template-policy.php` (next, and the largest single win because it serves seven policy pages)".

## 1. The block family and its one home, named before starting

Family: the routes rows. One home: `achology_routes_grid()` in `shared-parts.php`.
Caller collapsed this pass: `template-policy.php`, the "Where next?" section.

## 2. What changed

`template-policy.php` stops hand-authoring the section and calls the renderer.
Two supporting changes in `shared-parts.php`, both forced by that call:

**CalendarDays joined the icon registry.** It was the only one of the three
glyphs the registry did not hold, so the third row had nowhere to draw from.
It is registered for this exact slot at DSRD 7 §5.2, "Where next?" Rows, Quiet
About-Pages: "| Come to a free event | `CalendarDays` | First website use,
previously Circle-only (below) |". The paths are the ones the template's own
copy already carried, moved rather than retyped.

**The tone class is now omitted when empty.** `components.css` answers
`.about-grid .ic-tint` and its three siblings and nothing else, so a bare shell
carrying `ic-tint` would put a class on the page that no rule answers. The
renderer's `tint` default is untouched, so every caller that predates this
renders identically.

**The row urls are root-relative, not `home_url()`.** The renderer decides a new
tab from the address itself, and `home_url()` returns an absolute https address,
which would have sent the two internal rows out in a new tab against DSRD 3
§2.5: "All external links across the site open in a new tab (`target="_blank"`
with `rel="noopener"` ...). Internal links open in the same tab."

## 3. The verification, and why the obvious one would have been worthless

The register's method is "capturing them before and after and diffing byte for
byte". Done, on all eleven pages that use this template, before and after
deploy: the only line that differs on any of them is a Complianz plugin JSON
blob, and it differs identically on `/policies/`, which uses a different
template and cannot be affected by this change. Zero theme output moved.

**That test could not have failed, and on its own it proves nothing.** The
block renders on no page at all (section 4). So the block itself was rendered
through the renderer and diffed against the markup removed, taken from git
rather than retyped, with a guard that feeds the renderer a wrong icon and
confirms the diff goes red:

```
GUARD (a wrong icon must show as different): red as it should be
RESULT: DIFFERENT
-<!-- Where next? ... -->                                     (comment, now PHP, no longer shipped)
-<a class="policy-next__row" href="https://achologytest.com/learn/articles/">
+<a class="policy-next__row" href="/learn/articles/">
-<a class="policy-next__row" href="https://achologytest.com/free-events/">
+<a class="policy-next__row" href="/free-events/">
```

Three differences, all intended and all named above. Every element, class,
glyph path, aria attribute, and the external row's `target` and `rel` are
identical.

`page_gate` on `/policies/privacy-policy/` and `/about/manifesto/`: 28 passed
and 23 passed, 0 failed, 0 for review, dashes 0 em and 0 en on both.

## 4. The correction the register needs

**This block renders on no page.** `$ach_policy_next` is initialised false at
`template-policy.php` line 68 and nothing anywhere sets it true: `manifesto.php`
and `code-of-ethics.php` both set it false explicitly, and no other partial
mentions it. Confirmed on the live pages before any change: zero
`policy-next__row` on all seven legal policies.

So the register's note that this caller is "the largest single win because it
serves seven policy pages" is wrong. It serves none. The copy was still a copy
and DSRD 3 §2.6 still called it a defect, so collapsing it was right, but the
ordering rationale needs correcting and the remaining callers reprioritised:
`404.php`, `help-parts.php`, `page-about.php`, `manifesto.php` (two) and
`code-of-ethics.php` (two) all render on live pages, and this one did not.

**One question, not for me:** the section is now unreachable copy that no page
can show. Whether `$ach_policy_next` was meant to be switchable and was never
switched on, or whether the section should go, is a decision, so it waits.
Nothing is being proposed here.

## 5. Where the register stands after this pass

| Family | Status |
|---|---|
| Routes rows | Open. **Five callers outstanding:** `404.php`, `help-parts.php`, `page-about.php`, `manifesto.php` (two copies), `code-of-ethics.php` (two copies) |
| Poster tiles | Closed, S048 |
| Circular member cards | Closed, S048 |
| About preview builder's CSS blob | Closed, S048, by the S245 previews ruling |

Shipped to the build ground and the cache purged. Commit `ebef9a0`. No theme
version bump: no asset changed, so nothing needed cache-busting, and a version
stamp lands in every asset url and would have swamped the before-and-after
diff this pass depended on. Say if the convention is that every deploy carries
one and I will bump on the next pass.

*No em or en dashes in this file; checked before writing.*
