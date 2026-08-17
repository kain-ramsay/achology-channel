# RECORD: collapse, the routes-rows block family, pass one

**From:** Claude Code, S048. **Date:** 2026-08-06. **Shipped:** v0.38.54, live.
**Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`, item 3.

## Block family and its one home, named before starting, as the brief requires

**Family:** the routes-rows block. A `policy-next` section carrying a title, a
lead line, and a list of rows, each row an icon, a name, a description and a
chevron.

**Its one home:** `achology_routes_grid()` in `shared-parts.php`.

## The audit, which found more than the brief estimated

Seven hand-authored copies, not six:

| File | Copies | Content |
|---|---|---|
| `shared-parts.php` | 1 | the canonical renderer |
| `template-policy.php` | 1 | "Where next?", three rows, inline SVGs |
| `404.php` | 1 | "Where to instead?", loops `$ach_doors` |
| `help-parts.php` | 1 | the help close block, loops `$ach_rows` |
| `page-about.php` | 1 | four rows |
| `policies-content/manifesto.php` | 2 | four rows, then four |
| `policies-content/code-of-ethics.php` | 2 | three rows, then three |

Every one is the same skeleton. Only the shell classes and the content differ.
Four distinct shell combinations are in use across them, listed in the
renderer's docblock so the set is audited rather than guessed.

## Two families that close as already collapsed

The brief also named the poster tiles and the circular member cards. Both are
clean, and this is the verification evidence rather than an assertion:
`achology_member_stories()`, `achology_member_story_cards()`,
`achology_member_voices()` and `achology_member_voice_cards()` are called by
`page-about.php` and `page-testimonials.php` and authored nowhere else.
Confirmed by grepping every `.php` and `.js` file in the theme for the
functions and for their markup classes (`proof-card`, `lite-grid`,
`about-grid__paths`, `shared-video-lightbox`): each returns `shared-parts.php`
alone. **Those two families close.**

## Why the callers did not move in this pass

`achology_routes_grid()` hardcoded a single shell, the About-family variant.
None of the other six could call it without changing how they look, so the
shell had to become an argument before any caller could move. Doing the home
first is also what makes each later pass independently verifiable.

## What changed, and the proof it changed nothing

The shell is now an argument, defaulting to exactly the string it was. One
guard added: `about-grid--page` is appended only when the shell actually
carries `about-grid`, so no page can receive a class no rule answers.

No caller was touched. The proof, by the brief's own diff method:

- **Linted first.** There is no PHP locally, so the modified file was piped to
  the server and `php -l` run on it there **before** anything was deployed.
  "No syntax errors detected."
- **Deployed, cache purged, then fetched.** `/about/` and `/testimonials/`,
  the two pages this renderer drives, captured from the live site before the
  change and again after.
- **Result: byte for byte identical, both pages.** Not "looks the same". The
  files diff clean.

## The remaining passes, one file each

`template-policy.php` (which serves seven policy pages, so it is the largest
single win and the one to do next), then `404.php`, `help-parts.php`,
`page-about.php`, `manifesto.php`, `code-of-ethics.php`. Each verified on its
own rendered pages the same way, each filed here.

## One note for DSRD 3 §2.6's duplicate register

The register can now record the poster tiles and the circular member cards as
closed. The routes-rows family stays open with six callers outstanding, and the
count in it should read seven rather than six.

*No em or en dashes in this file; checked before writing.*
