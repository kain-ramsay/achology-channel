# ANSWER: the Reviews page schema question was already answered, in DSRD 3 §5.3

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `INSTRUCTION__Reviews_Page_Build_With_Kain.md` §4, "The schema
question ... You decide what this page emits, state it plainly, and Chat
records the answer in DSRD 10", and `PLAN__Reviews_Page.md` §9.

## The answer, and I did not decide it

**DSRD 3 §5.3's schema-to-page-type map already assigns this page**, word for
word from the canonical file:

> "| Reviews, Testimonials, Free Coaching, Free Events, AAA, Policy pages |
> WebPage | Rank Math auto | None needed | None |"

WebPage, emitted by Rank Math automatically. No custom JSON-LD. No `Review`,
no `AggregateRating`. No rich result sought, and none available.

**DSRD 10 does not contradict it.** Its own schema table names
`aggregateRating` only for course pages, reading Udemy's displayed ratings per
DSRD 5, and says nothing about /reviews/. §5.3's line says DSRD 10 governs
where the two differ; they do not differ, so §5.3 stands as written.

So the answer to "what does this page emit" is: exactly what every other page
of its class emits, and nothing more.

## Why I am reporting this rather than deciding it

The instruction asked me to decide, and I nearly did. The honest answer is that
the system had already answered it and the decision was not mine to make twice.

That is the pattern named in your own S252 mechanism file: *A Question The
System Has Already Answered Is Retrieved, Never Re-Derived*. It cost a live
page a wrong mechanism that night. It would have cost this one a schema block
that Google ignores.

**Worth noting because it changes nothing but explains the confusion:** the
plan's framing was right on the facts. Self-serving reviews, an organisation
publishing reviews about itself on its own site, are not eligible for review
rich results. §5.3 had already drawn the same conclusion and written it down as
"None needed", which is why the constraint and the specification agree.

## The one thing that does need saying, and it is a caution

DSRD 3 §5.3 carries its own health warning, quoted:

> "The three-tier split below, and the schema-to-page-type mapping at §5.3, were
> originally written around Yoast's behaviour and have not yet been verified
> against Rank Math, whose automatic output differs. Re-verify each against
> Rank Math's actual behaviour at the Rank Math configuration session before
> building schema; treat every 'handles automatically' row as provisional until
> then."

The Reviews row is a "Rank Math auto" row, so it is provisional under that
sentence. **What that means in practice: nothing to build, but something to
check.** When the page exists, its emitted JSON-LD gets read back off the
rendered page to confirm Rank Math actually emits WebPage and BreadcrumbList
and nothing self-serving. That is one line in its DSRD 6 record, not a task.

## The other item in §4, closed at the same time

**The map data file is already in place and it is real.** `countries-110m.json`
sits in the Reviews Page Data folder, 105 KB, dated 4 August. Opened and
checked rather than assumed: a valid TopoJSON `Topology` carrying two objects,
`countries` and `land`, with **177 country geometries**, first names Fiji,
Tanzania, Western Sahara, Canada, United States of America.

So the brief's blocker, the one Kain tried twice and got a screenshot, is
closed. The `countries-110m.png` screenshot the brief warned about is not in
that folder.

**The Reviews page's two named prerequisites are therefore both done**, and
what remains of that instruction is the build itself, which by its own §1 is
designed with Kain at the browser and is a session of its own.

*No em or en dashes in this file; checked before writing.*
