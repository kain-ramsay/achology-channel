# RULING: tags choose the hero course, and here are the eleven rows that need their tag order moved

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Filed under Harness Rule 14.**
**Answers:** `RULINGS__Hero_Course_Dead_Field_And_The_Glyphs_S255.md` §1.

## What was put to him

I measured before shipping, and brought him the consequence rather than the
mechanism: across all 620 master rows the hand-picked course and the lead tag
agree on 385 and differ on 235, and some of the differences read plainly wrong.
The example given was The CBT Toolbox, which would stop recommending the CBT
Toolkit and start recommending the Life Coaching Certificate, because that
row's first tag is `help-others-grow` rather than `learn-cbt`.

Put as one recommendation: ship it, and correct the ones that read wrong in the
tag order rather than in the code, so the rule stays single and the data
carries the correction.

## Kain's ruling, his word in full

> "hip it and fix them in the tags rather than in the code"

(His typing. "Ship it and fix them in the tags rather than in the code.")

## Shipped

`recommended_course` is out of the template and out of the field group. The
field group now carries 13 fields and neither editorial course field is among
them. The hero slot reads `achology_courses_for_content( $id, 1 )`, so it and
the cards below it come from one rule.

**The rendered book note is byte for byte identical**, because on that book the
hand-picked and derived answers already agreed. The "See related course" link
still points at `/academy/personal-growth/clarity-purpose-effectiveness/`.

That proves the wiring and proves nothing about the other 619, which is exactly
why the measurement exists and why the list below does.

Commit `8f15cb3`. Live: https://achologytest.com/learn/psychology/book-notes/mans-search-for-meaning/

## The eleven rows, and what to do to each

235 rows change. **Handing you 235 to eyeball is a chore, not a fix list**, so
this narrows to the rows where the new course is demonstrably wrong rather than
merely different: the book names a subject in its own title, the hand-picked
course was that subject's course, the derived one is not, **and the row already
carries the right tag further down**. Every fix below is moving a tag the row
already has to the front.

| Row | Would become | Move to the front | Which gives |
|---|---|---|---|
| `cognitive-behaviour-therapy` | DiMAP | `learn-cbt` | CBT Toolkit |
| `the-cbt-toolbox` | Life Coaching Certificate | `learn-cbt` | CBT Toolkit |
| `doing-cbt-david-tolin` | Self-Belief/EI/Assertiveness | `learn-cbt` | CBT Toolkit |
| `cognitive-behavioural-therapy-with-couples-and-families` | DiMAP | `learn-cbt` | CBT Toolkit |
| `counselling-skills-and-theory` | Life Coaching Certificate | `learn-counselling` | Counselling Skills |
| `person-centred-counselling-in-action` | Life Coaching Certificate | `learn-counselling` | Counselling Skills |
| `skills-in-person-centred-counselling` | Life Coaching Certificate | `learn-counselling` | Counselling Skills |
| `an-introduction-to-counselling` | Life Coaching Certificate | `learn-counselling` | Counselling Skills |
| `coaching-for-performance` | Mindfulness for Leadership | `learn-life-coaching` | Life Coaching Certificate |
| `the-mindful-way-through-depression` | DiMAP | `learn-mindfulness` | Mindfulness Practitioner |
| `the-mindfulness-and-acceptance-workbook-for-anxiety` | DiMAP | `learn-mindfulness` | Mindfulness Practitioner |

**The master is production's, not mine**, so I have not touched it. This is the
list, ready to apply.

## Two things worth saying about the other 224

**They are not all fine, they are all unproven.** My test only catches rows
where the subject is visible in the title and the right tag is already on the
row. A book whose subject is not in its title, or which lacks the tag that
should lead, will not appear above and may still read wrong. I would rather say
that than let eleven look like the whole answer.

**The pattern underneath is worth a look of its own.** Four of the eleven lead
with `help-others-grow` and three with `understand-your-mind`. Those two tags
are doing a lot of leading across the whole master, 170 rows and 24 rows
respectively at the front. If a modality tag such as `learn-cbt` is present, it
is almost always the more specific answer, and it is almost never first. That
looks like a tagging convention question rather than 224 individual decisions,
and it is production's to answer, not mine.

*No em or en dashes in this file; checked before writing.*
