# SIGNED SPECIFICATION: create the 35 school and course pages as drafts

**DOCUMENT TYPE:** not a page spec for a design. This is a page-creation enumeration under Harness Rule 8, Version 3.3.
**From:** Claude Chat, Session 267. **Date:** 2026-08-12.
**Authority:** Kain, in session. He asked whether Code could set the pages up now, and whether the rule that forbids it should bend. It has been tightened rather than bent.
**Read The Harness at Version 3.3 first.** Rule 8's page boundary has changed and this is the first work under the new wording.

## What changed in the rule, so you know why this is now allowed

The old sentence said you never create a WordPress page. **It now says you create pages only from an enumeration in a signed specification: each one named by title, address, parent and template, created as a draft, and the count and full list reported back.** A page you create that is not on the list is a harness break, and so is a page on the list that does not appear.

That is a tighter guard than the old one, not a looser one. "Never create a page" could only be broken invisibly. "The two counts match" is checkable by anyone in ten seconds. **Thirty-five in, thirty-five out.**

## Why this is worth doing now, before the templates exist

A page's template is a setting on the page, changed later in one click. So the pages can exist now and be switched onto the real templates the day those are signed, with nothing wasted. What it saves is thirty-five pages of Kain's own clicking, which is the only reason the work was sitting undone.

## The structure, read from DSRD 1 section 2.3 this session

Courses nest inside their schools. A school lives at `/academy/{school-name}/` and a course at `/academy/{school-name}/{course-name}/`. **These are WordPress Pages using parent and child, never a custom post type**, because Pages give the nested address natively and a post type would need custom rewrite rules to fake it. That is settled and is not yours to revisit.

**Before creating anything, confirm the `/academy/` parent page exists and report its state.** Every one of the 35 hangs off it. If it does not exist, stop and ask rather than creating it, because it is a page in its own right with its own design.

**Do not touch `/academy/schools/`.** It is the existing seven-paths listing page, not a school, and its slug must never be used as one.

## The 7 school pages

Parent: `/academy/`. Template: the school page template. **Status: draft.**

| Slug under /academy/ |
|---|
| `neuro-linguistic-programming` |
| `cognitive-behavioural-psychology` |
| `life-coaching` |
| `person-centred-counselling` |
| `mindfulness` |
| `mental-health` |
| `personal-growth` |

## The 28 course pages

Parent: the school page above it. Template: the course page template. **Status: draft.**

| School parent | Course slugs |
|---|---|
| `neuro-linguistic-programming` | `diploma-modern-applied-psychology`, `beginners-guide-nlp`, `nlp-practitioner`, `nlp-master-practitioner`, `mindset-mastery-self-discovery` |
| `cognitive-behavioural-psychology` | `cbt-toolkit`, `cbt-practitioner`, `cbt-mental-health` |
| `life-coaching` | `life-coaching-certificate`, `life-coaching-blueprint`, `skilled-helper`, `skilled-helper-practitioner` |
| `person-centred-counselling` | `hypnotherapy-practitioner`, `counselling-skills-practitioner` |
| `mindfulness` | `mindfulness-practitioner-diploma`, `mindfulness-mental-health`, `mindfulness-leadership` |
| `mental-health` | `mental-health-practitioner-diploma` |
| `personal-growth` | `self-belief-emotional-intelligence`, `authentic-confidence`, `emotional-iq-social-skills`, `clarity-purpose-effectiveness`, `goal-setting-action-planning`, `communication-social-intelligence`, `hyper-focus-productivity`, `mental-toughness-resilience`, `healthy-marriage-relationships`, `entrepreneurship-business` |

**Count: 5 plus 3 plus 4 plus 2 plus 3 plus 1 plus 10 = 28.** If your own count of the rows above is not 28, stop and ask.

## The titles: copied from DSRD 5, never written by you

**The slug is given above. The title is not, and you do not invent it.** Open DSRD 5, find the course or school the slug refers to, and copy its canonical name exactly as written, per standing rule 1. That is copying a confirmed value, not drafting content, and Rule 8's content boundary is not engaged.

**Print the full 35-row pairing in your report: slug, the canonical name you matched to it, and the address the page ended up at.** That pairing is the thing Kain and I check, and it is the reason this is safe to hand over.

**Where a slug cannot be matched to exactly one entry in DSRD 5 with confidence, do not guess and do not pick the nearest.** Create the other pages, leave that one uncreated, and name it in your report as unmatched with what you found. One unmatched row costs a single line in a reply. A wrong course name on a sales page costs more than that.

## The two templates do not exist yet, and that is expected

Assign the correct template where one exists. Where it does not, leave the template unassigned and say so in your report; the pages get switched onto their templates in one pass once the designs are signed. **Do not create a placeholder template to have something to assign.**

## The rules for this job, stated plainly

1. **Draft only.** Nothing publishes. These pages have no copy yet and an empty published page on a live domain is exactly the problem the `/cards/` page turned out to be.
2. **Nothing else changes.** No menu, no navigation, no redirects, no copy, no settings.
3. **Create only what is listed.** Thirty-five.
4. **Report the count, the full pairing, and the `/academy/` parent's state.**

## The second, smaller job in the same commission

**Two admin menu entries**, one called Courses and one called Schools, each opening the Pages list filtered to that template, so Kain and Karen reach these the way they reach Book Notes and Quotes rather than hunting through a flat page list beside the policies.

This is an admin convenience only. It changes what the WordPress sidebar shows and changes nothing about the site, the addresses or the content. Build it when the templates exist and the filter has something to filter on; there is no value in it before then.

## And one question, which is a question and not a commission

**Report what internal linking work has actually been done across the 249 help articles.** There is an old brief for it in the archive, and reports of a link map pass and a link ceiling measurement, and I do not know from here which of that ran, on how many articles, and what the result was.

**Answer, do not act.** Kain wants to look at the whole picture and possibly build a deliberate strategy around it, aimed at building the authority of specific pages rather than just connecting articles to each other. That strategy does not exist yet and nothing should be linked or relinked until it does.

What is useful back: what ran and when, how many of the 249 it touched, how many in-body links exist now and how they are distributed, whether the mirror rule holds both ways, and any article carrying none. Counts, not opinions.

*No em or en dashes in this file; checked before writing.*
