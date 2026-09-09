# RULING: the page title takes 24 above its reading text

**From Code, S109. Date: Thursday 10 September 2026.**
**Given by Kain live in the sitting this morning, acted on in the same sitting,
shipped at theme 0.230.0.**
**Owning document: DSRD 7 section 4.3.**
**Board cards:** Quote page template; Book notes.

---

## What he was shown

The open line this closes was written at S108 and it named its own test: the
page title is 33 and a section heading is 24, so bigger type may want more air
than the 16 a section heading gives its text.

He was shown 16 against 24 photographed on the real quote page and the real book
note, one picture on screen at a time in the identical screen position, in a
viewer carrying no site stylesheet.

## His words

> "24 please"

## What the rule says now

The space under a heading is still decided by what follows it, not by which
heading it is. What changes is that the heading's own size moves it one step
when reading text follows:

| what sits under the heading | space |
|---|---|
| a label that belongs to the title, like the date line | 8 |
| reading text under a section heading | 16 |
| reading text under the page title | 24 |

**Nothing new enters the scale.** All three are steps of the spacing scale in
base.css.

## Where it landed

The quote page and the book note now give 24, each at the line in its own sheet
that carries this rule's name. The article keeps 8, because what follows its
title is the meta line, which is a label. The rule's full record at
`.kh-article__title` in knowledge-hub.css is rewritten to carry three values
rather than two, and its OPEN line is struck.

Measured on the live pages after the deploy, not declared: 24 on the quote page
and on the book note, 8 on the article, all four page titles still 33 and 700
in an h1.

## One thing for you, and it is a recommendation rather than a question

**This rule has no gate.** `page_gate.py` measures the page title's size and
weight and does not measure the space under it, which is exactly the gap that
let a hand-typed 32 sit on the help answer for fifty two sessions. The durable
form of a ruling is a gate.

**What I would build, if you agree it is the right shape:** the gate reads the
element immediately after the page title and requires 24 unless that element is
the template's own meta line, in which case it requires 8. It judges nothing
about the words: the templates are four and their meta lines are named classes,
so it is a lookup rather than an opinion. Say yes and it goes in with the next
theme change set; say it belongs somewhere else and I will put it there.

---

OWED BACK: the three values written into DSRD 7 section 4.3, and a yes or no on
the gate check.

*No em or en dashes in this file; checked before writing.*
