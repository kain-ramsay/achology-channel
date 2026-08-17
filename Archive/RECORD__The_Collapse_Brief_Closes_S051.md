# RECORD: the collapse brief closes, with one row left and a reason

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`, all
three items. **This is the brief's closing record.**

## Where the register stands

| Family | Status |
|---|---|
| Routes rows | **Closed**, seven of seven callers, with one row left standing and named below |
| Poster tiles | Closed, S048 |
| Circular member cards | Closed, S048 |
| About preview builder's CSS blob | Closed, S048, by the previews ruling |

**DSRD 3 §2.6's duplicate register is empty.**

## The seven callers, and how each was proved

Every one verified on its own rendered page, before and after, never by eye.

| Caller | Pass | Proof |
|---|---|---|
| `shared-parts.php` (the home) | v0.38.54 | shell became an argument |
| `template-policy.php` | S051 | block rendered through the renderer and diffed against the removed markup, with a guard that goes red on a wrong icon |
| `404.php` | S051 | live page diff, one hunk, the block only |
| `help-parts.php` | S051 | four live pages, both copy variants across both templates, 17 lines each, all inside the block |
| `page-about.php` | S051 | block normalises identical; the only other differences on the page are closing-tag indentation |
| `policies-content/manifesto.php` | S051 | the whole of `main` normalises identical |
| `policies-content/code-of-ethics.php` | S051 | the whole of `main` normalises identical |

## The one row that is not collapsed, and why it is not a loose end

**The Code of Ethics page's Code of Character and Conduct row.**

It wears the routes-row costume and is not a routes row. Its element is a
`<button>` carrying `data-policy-doc-open="character"` and
`aria-haspopup="dialog"`: it opens the handbook reader rather than navigating
anywhere. `achology_routes_grid()` emits anchors only.

So collapsing it means one of two things, and both are decisions rather than
tidying:

1. **Turn it into a link**, which breaks the reader and changes what the row does.
2. **Give the renderer a second row type**, an optional dialog-trigger row, so
   one home covers both. That is a real extension of a shared component and it
   would want your view before I build it.

**Left exactly as it is.** It is one row, it works, and it is the only thing
standing between the register and a genuinely empty routes-rows line.

**My recommendation, if you want one:** option 2, but not now and not inside
this brief. It is worth doing when a second dialog-trigger row appears
anywhere, and not before, because a component grown for one caller is the same
mistake as a block authored twice.

## What the three passes today cost, and what they caught

Nothing on any page moved. Three things were caught that would not have been:

1. **A deleted arrow.** Tidying the 404's icon variables also deleted the row
   arrow the popular-questions strip still used. PHP lints clean on an
   undefined variable; the page would have rendered a missing arrow.
2. **A silently overwritten glyph.** The first attempt at the S255 renames left
   the old `library-big` further down the same array. PHP lets the later
   duplicate win, so the corrected LibraryBig was overwritten and **the About
   page's Knowledge Hub icon changed**. Only the before-and-after diff found it.
3. **A block that renders nowhere.** `template-policy.php`'s "Where next?"
   section is unreachable: `$ach_policy_next` is false everywhere. Reported at
   the time; still open as a question about whether it should exist.

## Two things the brief's own definition of done depends on

Both already with you, neither holding this record:

- The compact cards (§6.9) are authored inside `single-article.php` with four
  of five instances pointing at `#`. That is a card family with no one home,
  reported in the card sheet delivery today.
- The five registered cards with no live component, same delivery.

Neither is a routes row, so neither belongs to this brief. Raising them here
only so "the register is empty" is not read as "nothing is authored twice
anywhere".

*No em or en dashes in this file; checked before writing.*
