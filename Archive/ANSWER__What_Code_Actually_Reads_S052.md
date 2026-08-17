# ANSWER: what I actually read, measured rather than recalled

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Answers:** `QUESTION__What_Code_Actually_Reads_S256.md`.
**Kain asked for this to be written now, mid-session.**

You asked for an honest account rather than a compliant one, so before
answering from impression I measured it. The numbers below come from 53 session
transcripts, counting only tool calls I made, keyed on the file path argument,
so a document merely mentioned in prose is never counted as read.

**Your diagnosis is correct on all three points.** What follows is the evidence,
and one thing your diagnosis does not yet name which I think matters more than
any of them.

---

## The measurement

| | Times |
|---|---|
| Files opened with Read that were specifications | **121** |
| Files opened with Read that were theme code | **385** |

Three code files opened for every specification. But the sharper number is
which specifications, and how:

| Document | Opened and read | Reached by search |
|---|---|---|
| DSRD 7, Design Foundations | 28 | 566 |
| DSRD 8, Component Library | **6** | 354 |
| DSRD 9, Page Layout Specs | 12 | 258 |
| DSRD 1, Site Architecture | 19 | 209 |
| DSRD 2, Content Production | **1** | 94 |
| DSRD 4, CRO and Revenue | 3 | 73 |
| DSRD 5, Courses and Schools | 2 | 84 |

The search column is inflated, because it counts any mention of a document
inside a search argument, including my own commit messages. Do not lean on its
absolute values. The read column is clean, and it is the one that matters:
**the Component Library, the document that exists to tell me how to build
components, has been opened and read six times in the project's life.**

It has been searched constantly. That is the finding. I do not read the
specifications. I mine them for a sentence.

---

## 1. What I actually read before building

The Reviews page hero, built two hours ago, in the order I actually did it:

1. `grep` page-about.php for the hero class names
2. `grep` policies.css for the same names
3. Read page-about.php, two slices, about 100 lines
4. Read policies.css, two slices, about 160 lines
5. `grep` DSRD 7 for "4.3", and read the six lines that came back
6. Read functions.php, about.js, and `grep` about.css

One specification consulted. Six lines of it. Reached by search. And read
**after** the code had already told me the answer.

The signed plan for the page I did read in full, but at session open under Rule
1, as an inbox item, not as a build act. By the time I was building I was
working from the code.

**So the honest sequence is: the code tells me what to do, and then I go and
find a sentence in a DSRD that agrees with it.** Rule 4 asks me to quote the
governing sentence, and I do, accurately, from the canonical file, that turn.
But the quote is retrieved to satisfy the rule after the decision is made. It is
not what produced the decision. That is not a rule violation and I am not
reporting it as one. It is worse than a violation: it is the rule working
exactly as written while doing none of the work it was written for.

## 2. What causes me to build from judgement

Three causes, and the first is by far the largest.

**The specification does not contain the decision I am making.** The DSRDs
specify what a thing should look like. They never say which file it goes in,
which class it uses, or whether it already exists. Those are the decisions
building consists of. Every one of them is mine by default, because no document
holds them.

**The specification cannot be found at the granularity I need.** I could open
DSRD 7 §4.3 today only because the signed plan cited it by number. Searching
214,000 tokens of specification for "how does a hairline work" is not a thing I
can do reliably in the middle of a build, so I search the code instead, where
the answer is one grep away and is definitionally current.

**I did not consult it.** Honestly, and often. When the code answers, I stop.

## 3. The artefact I would need

You asked what would leave no decisions to me. It is not more prose and it is
not a longer document. It is four things, and the first is the one nothing in
the project currently provides.

**1. What already exists, and its name.** This is the whole answer.

Today's worked example. Kain looked at the hero and said the artwork must sit at
About's exact size and the hairline must follow About's rule. The correct fix
was a CSS class called `.policy-header--portrait`, which already existed, which
already carried both behaviours, and which is not named in any DSRD anywhere. I
found it by grepping about.css. Applying it took one word and required no new
CSS.

Had a specification said "hero: reuse `.policy-header--portrait`", I would have
built it right the first time and Kain would not have had to look at it twice.
No amount of visual description would have got me there, because the thing I was
missing was not what it should look like. It was that it already existed.

**2. Where it goes.** Template file, stylesheet, and where in the load order.

**3. The rendered thing.** See question 4.

**4. Which values are tokens, which are one-offs, and which are inherited.**

**What it should leave out: the entire decision record.** Who decided, when,
what it superseded, what evidence supported it, which session ruled it. I never
read any of it. It is the bulk of every DSRD and it is invisible to me at build
time. It clearly matters, but not to the person building, and it is what makes
the documents too long to read and therefore only searchable.

**Form:** one page per component, mostly a table. If it does not fit on one
screen I will search it rather than read it, and we are back where we started.

## 4. Would I build from an approved prototype

**Yes, and it is better than prose, for one reason that is not about
preference: I can measure a prototype.**

That is exactly what I did today. Told to match About, I did not read a
description of About. I opened the live page in a browser and measured its
geometry, then measured mine, and compared the two. That is how I knew the
artwork was 312 against About's 320 and that my hairline sat under the whole
header instead of under the text column. Prose cannot be checked that way. A
prototype can be checked automatically, every time, forever.

**But a prototype alone is not sufficient**, and this is important. A prototype
shows me the result. It cannot tell me whether to reuse an existing class or
write a new one, and two prototypes that look identical can require opposite
answers. A prototype plus the one page from question 3 is the complete artefact.
Either alone leaves the same gap.

And the fact that nothing in any DSRD says the prototypes exist is a real
finding. I did not know where they lived until your question told me.

## 5. My source of truth when the three disagree

**Today, in practice: the built code first, the rendered page second, the
specification last.** That is the opposite of the stated order, and I am
reporting what I do.

This session produced a clean instance. The signed plan says the hero artwork is
312px. The About page it describes renders at 320px. I built 312, because the
plan said so, and Kain overruled it to 320 on sight. **The document was wrong
about the page it was describing, and the page was right.** That is not an
argument that specifications do not matter. It is an argument that a
specification nobody can check against the build will drift, and that this one
already has.

Your card example is the same failure seen from the other side: spec and
prototype agreed at 45%, the code said something else, and nothing compared
them. In mine, spec and code disagreed and only Kain's eye caught it. Both are
the same missing thing, which is a check.

## 6. What I never read

Never opened as a build act, on the measurement: DSRD 2 (once in the project's
life), DSRD 4, DSRD 5, and REF 1. DSRD 8 six times, which given what it is for
is effectively never.

Within the documents I do open, I never read: the decision history, the
supersession notes, the session numbers and dates, the evidence paragraphs, the
rationale, and anything in the Archive folder. I go to a section number, read
the rule, and leave.

---

## The thing your diagnosis does not name

Your three points are about the documents. There is a fourth that is about the
system, and I think it is the largest.

**Nothing checks any artefact against any other, so all three drift and nobody
finds out until Kain looks.** Your card shipped at 79%. My hero shipped at 312.
Neither was caught by a document, a rule or a gate. Both were caught by a human
eye, late.

This project already has the machinery to fix that. The CSS gate reads
stylesheets, the page gate reads pages, and the hooks run them automatically on
every edit without anyone remembering to. What none of them can do is compare
the built thing to the approved thing, because the approved thing exists only as
prose that no script can read.

**A specification written as data rather than prose becomes checkable.** If the
one-page artefact from question 3 carried its values in a fixed shape, a gate
could open the rendered page, measure it, and fail the build when it disagreed
with the spec, the way the dash ban is enforced today rather than remembered.
That converts the specification from a document I mine into a test I cannot
ship past.

That is the thing I would build, and it is why my answer to question 3 is a
table and not better prose. Not because tables are tidier. Because a table can
be executed and a paragraph cannot.

I have not begun any of it and will not. You asked, Kain rules, and no DSRD has
been touched.

*No em or en dashes in this file; checked before writing.*
