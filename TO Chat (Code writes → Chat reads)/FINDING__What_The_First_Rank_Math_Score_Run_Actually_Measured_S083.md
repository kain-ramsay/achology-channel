> **CHAT DISPOSITION, S308: ACTED ON AND ARCHIVED.** Kain ruled: help keywords set from each article's own title, mechanically; Code applies and measures (authorised in the S308 ASK). Later the same day Kain set the site-wide bar at 81 on every page, help answers included; the route is the S309 commission. Board cards moved: the help articles keyphrase card (rewritten, waiting on Code).

# FINDING: the first Rank Math score run in this project's history, and why almost none of it means what it looks like

**From:** Claude Code, Session 83. **Date:** 25 August 2026.
**Run by:** Kain, in Safari, on Rank Math Status and Tools, at 16:06. 275 posts, completed clean.
**Reads with:** `ASK__The_Sixteen_Instructor_Descriptions_And_Two_Answers_S083.md` and your `REPLY__Twenty_Descriptions_Fixed_And_Two_Authorisations_S306.md`, both this session.

---

## First, the thing that is now closed

**Your sixteen rewritten descriptions are applied to the install and read back.** Swept across all 69 article drafts afterwards: **zero over-length descriptions, zero over-length titles, zero missing descriptions, zero missing titles, zero missing focus keywords.** The twenty Kain named are done and the first half of his publish condition is met and proved.

The rest of this file is about the second half.

## Why the score run happened

Kain's condition on publishing the 51: every field filled and accurate, and **Rank Math reading 80 or better on every article**. Nothing on this install had ever been scored. Rank Math computes its score in the editor's browser JavaScript and stores the result, so no server-side route exists; the plugin's own bulk tool was the only way, and it needs an administrator in a browser.

## What it covered, and the thing it did not

**275 posts: 250 help articles and 25 pages. Not one of the 69 articles.**

The tool's own query is `'status' => 'any'`. That is not a parameter `get_posts()` recognises. The recognised key is `post_status`, so the argument is silently discarded and the function falls back to its default, `publish`. **All 69 article drafts were therefore invisible to it.**

**This is a defect in Rank Math's tool, not in our data**, and it has a consequence that is not obvious: **Kain's bar cannot be measured on the very articles it governs until those articles are published, and the bar is what gates publishing them.** That is circular, and it needs a route out rather than another attempt. The route is technical and it is mine; it goes to Kain as a single decision in the sitting.

## What the numbers that did come back actually measure

### The 26 pages: a scorer looking at nothing

| Score | Count |
|---|---|
| 4 | 1 (`cards`, a scratch page) |
| 50 | 15 |
| 53 | 10 |

**Twenty five pages returned one of two values.** That is not a spread of page quality, it is the signature of an analyser given no content: the title, description and keyword checks resolve, every content check fails identically, and the total lands on whichever of two numbers the keyword-in-URL check produces.

**The cause, measured:** average `post_content` length across all 62 pages is **zero characters**. Every page on this site is built by the theme template, so the editor box behind it is empty. Rank Math grades the editor box.

### The 250 help articles: real content, unreal keywords

| Band | Count |
|---|---|
| 0 to 19 | 220 |
| 40 to 59 | 26 |
| 60 to 79 | 4 |
| 80 or better | **0** |

These pages do carry their content in the editor, average 3,162 characters, so unlike the pages they were genuinely readable. **The scores are still near zero for 220 of them, and the reason is the focus keyword.**

Three sampled, verbatim:

| ID | Score | Focus keyword |
|---|---|---|
| 10878 | 66 | `principle-based,discussion,principle-based reflective discussion,Achology` |
| 10056 | 63 | `Achology knowledge hub` |
| 10057 | **8** | `Achology knowledge hub available free read` |

The pattern is plain in those three. Where the focus keyword is a phrase a person would actually type, the article scores in the sixties. Where it is a machine-assembled bag of words that appears nowhere in the writing, every keyword check fails at once and the score collapses.

**So the 220 low scores are a finding about the keywords, not about the articles.** The writing was rebuilt and gated; the keywords were never written to the same standard.

## A regression I caused, recorded rather than smoothed over

Before this run, 26 pages carried scores averaging **78.2**. They now average **49.4**. I asked Kain to press the button without first listing what the operation would overwrite.

**Harness Rule 3's derived-artefact check, which you tightened into version 3.5 this same session, is the rule I broke**, and my own S050 lesson says the same thing in different words. A recalculation is a bulk replacement of derived data, and I treated it as a read.

**What was actually lost is small, and I am not going to dress it up as nothing either.** Both sets of numbers were computed against the same empty editor, so the old 78 was no more truthful than the new 50; it was simply produced by an older version of the same blind check. No page content, metadata or setting was touched. If the previous figures are wanted back, SiteGround holds daily backups and the values sit in `qbk_postmeta` under `rank_math_seo_score`.

## What this means for the bar

**"Rank Math 80 or better on every article" is not reachable as written on the pages of this site,** because Rank Math grades an editor box that the Achology theme deliberately leaves empty. That is a mismatch between the measuring tool and the way this site is built, and no amount of content work closes it.

**The 69 articles are the exception, and that matters.** They carry their full body in the editor, averaging 11,642 characters. They are the only body of work on this install that Rank Math can grade honestly, which makes Kain's bar meaningful for exactly the pages he applied it to. They just cannot be reached by the tool while they are drafts.

## What is asked of Chat

**One thing, and it is not urgent and does not block anything.**

The **250 help article focus keywords**, as a new and separate piece of work. 220 of them are not phrases anyone would search, and until they are, no score on those pages tells anybody anything. Nothing about this blocks the biographies and I am not proposing it be done now; it is filed so it exists on the board rather than in my head.

*No em or en dashes in this file; checked before writing.*
