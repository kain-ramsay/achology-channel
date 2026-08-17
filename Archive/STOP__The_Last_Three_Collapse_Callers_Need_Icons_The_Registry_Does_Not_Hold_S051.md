# STOP: the last three collapse callers need glyphs DSRD 7 §5.2 never registered

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Concerns:** `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` item 3,
the three remaining routes-rows callers.
**Status: waiting on ruling.** Nothing built, nothing changed. Four of the seven
copies are collapsed; these three are stopped before starting.

## The rule I am stopping against

DSRD 7 §5.2, the registry's own governing sentence:

> "All icon slots in the design system use named Lucide icons from this
> registry. Improvised freehand SVG icons are prohibited. If a new icon slot is
> created, a Lucide icon must be selected and added to this registry before it
> appears in any prototype or template."

Collapsing a caller means its rows stop carrying raw path data and start naming
a registry key. That is only possible where the glyph has a name. Four times
today it did: CalendarDays, Compass, Mail and MessageCircleQuestion were each
registered at §5.2 for the exact slot they appear in, so each one moved into the
theme's registry under its registered name and the pages did not change.

**On the last three callers that stops working, in two different ways.**

## Problem 1: page-about.php's four row glyphs are not registered at all

The "The Thinking that Drives Achology" panel carries four rows, each with a
hand-drawn `<svg>`:

| Row | The drawing, in plain terms |
|---|---|
| The Achology Manifesto | a book with text lines |
| Achology's Code of Ethics | a set of scales |
| Policies and Legal Documents | a document with lines |
| Foundational Principles | a pen line, which IS the registry's `pen-line` |

**Three of the four appear in no §5.2 slot.** I read every subsection of the
registry: there are entries for the /help/ blocks, the code-of-ethics pair, the
quote card, the stats lines, the card utilities, both section-header sets, the
breadcrumb, the header bar, all three dropdowns, pagination, and the About
page's hero action and back-to-top at S237. **There is no entry for this
panel.**

So this is a pre-existing breach of the sentence quoted above, found rather than
caused: the glyphs appeared in a template without being registered. I am not
naming them myself, because choosing a Lucide name for an existing drawing is
exactly the judgement Rule 5 forbids, and a wrong name here is worse than none:
it would look registered.

**What I need:** those three slots registered at §5.2 with their Lucide names.
Then the collapse is mechanical and I can prove the page byte-identical.

## Problem 2: manifesto.php and code-of-ethics.php collide with the Library name

Both files' second panel carries the "Browse All of Our Courses" row. §5.2 says
of it, at the code-of-ethics entry: "the second card keeps the manifesto close's
Browse All of Our Courses route (`Library`, already registered)".

**Three different drawings are in play under two names**, and I can only report
that, not resolve it:

| Where | The drawing |
|---|---|
| the registry key `library` | a tall shelf: one rounded rect, a vertical rule, a leaning volume |
| the registry key `library-big` | two horizontal rules, four verticals, a bordered block |
| what manifesto.php actually renders | four leaning strokes, and nothing else |

The third is in neither key. So collapsing either file means adding a drawing
under a name, while `Library` and `LibraryBig` already disagree with each other.
**This is the same §5.2 question I filed at S050** and it has now blocked real
work twice, which is the argument for answering it rather than carrying it.

There is a second consequence worth stating: the 404's Knowledge Hub door,
which I collapsed earlier today, calls the key `library` while §5.2 names that
door `LibraryBig`. I kept the drawing that was on the page and changed nothing,
and said so in that record. Whichever way the naming lands, that door may need
a glyph change, and that would be a visible change on a page, so it is Kain's
eye and not a tidy-up.

## What I propose, which is one decision rather than three

**Register the seven slots in one pass**: the three About rows, and the naming
of `Library` against `LibraryBig` against the four-stroke drawing. I will supply
whatever you need from the theme side, including the exact path data of every
drawing currently rendering, so the naming is done against what is on the page
rather than from memory.

Then the three remaining collapses run back to back, each proved byte-identical
on its own rendered page, and DSRD 3 §2.6's routes-rows row closes.

## Meanwhile

I have not touched any of the three files. The register stands at four of seven
collapsed, and the three that remain are all on pages Kain approved by eye,
which is the other reason not to improvise on them.

*No em or en dashes in this file; checked before writing.*
