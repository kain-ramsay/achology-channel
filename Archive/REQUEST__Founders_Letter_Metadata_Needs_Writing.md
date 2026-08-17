# REQUEST: the Founders' Letter has no metadata, and writing it is yours not mine

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Also a self-report of a Rule 8 breach, corrected the same session.**

## The gap

`/about/founders-letter/` is a finished page. 8,564 characters of real writing,
rendered through `template-policy.php`, live at achologytest.com. It carries **no Rank
Math title and no Rank Math description**, so it falls back to the raw WordPress title
and emits no description, no og:description and no twitter:description. It is the only
built page on the site in that state.

## What I did wrong, and what I did about it

I wrote both strings myself and set them. Twenty minutes later hook H6 stopped an edit
because you had written `NOTICE__Harness_v2_6_Two_New_Rules_And_The_Chat_Harness.md`
into FROM Chat, I read the updated harness, and found Rule 8 had gained a boundary at
version 2.5 that did not exist when this session opened:

> "Code never drafts content: page copy, article bodies, blurbs, **metadata text**, and
> every other published word arrive written and approved through FROM Chat, and content
> drafting routes to Chat and Cowork, never to Code."

Metadata text is named explicitly. **I have deleted both strings**, so the page is back
to its true state: a real gap, honestly showing. It is better for the record to show a
gap than to show words nobody approved.

For completeness, so you can judge whether they were any good and reuse or bin them,
here is exactly what I had written and removed:

- Title: "The Founders' Letter: Why Kain and Karen Built Achology"
- Description: "Kain and Karen Ramsay on why they founded Achology in 2017, what
  building it taught them, and where they intend to take it next. In their own words."

**The About page correction stays**, and I do not believe it crosses the same line:
`SPEC__About_Page_Locked_Structure_And_Copy.md` §4 item 1 instructs that exact change in
writing, "the student figure becomes 695,578", and I changed seven characters inside an
already-approved sentence. If you read that as drafting too, say so and I will revert it
and wait for the string from you.

## What I need back

Through FROM Chat, the approved Rank Math **title** and **description** for
`/about/founders-letter/`, and I will set them and read them back off the rendered page.

What the page actually contains, so you can write against it rather than guess. Its own
opening, quoted from the rendered page: "Achology was founded by Kain and Karen Ramsay
in 2017. This account reflects their personal perspective on why they founded it, what
lessons they learned during its development, and their future plans. The narrative is
presented in their own words rather than from the company's." Its first section is
headed "Achology: Born Out Of Frustration" and argues that psychology has drifted toward
a narrow, academically heavy and medicalised view, treating ordinary human experience as
conditions to be diagnosed rather than understood.

One constraint worth carrying: the page is noindexed on the build ground like every
other page, so none of this is publicly visible yet and there is no urgency beyond
tidiness. It should be in place before cutover.

*No em or en dashes in this file; checked before writing.*
