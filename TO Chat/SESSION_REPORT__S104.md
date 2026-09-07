# SESSION REPORT: S104, a factory session

**From:** Claude Code, Session 104, factory session. **Date:** 6 to 7 September 2026.
**Assembled from the version control log for both repositories**, per Harness Rule 13, with hand-added lines marked.

Kain opened this as the publishing session on the 85 article drafts. Its two conditions were missing, so it ran the redirect work instead, then the salvage heroes, then the answers arrived and the publishing ran after all. It became the longest sitting on this project, and Kain closed it himself on the reasoning that Code was deep in context and should review with fresh eyes. That judgement is his and it is the right one.

---

## Finished

**The install went from 66 published articles to 196.** All 115 rescued field-authority articles, the last two of the eighteen instructor articles, and all twelve of Karen's. One draft remains, the frozen exemplar, which Kain took back to draft himself.

**The redirect chain register run fresh, and `redirect_one_hop.py` built** (`1aa9b73`). 235 of 1,051 destinations carry all five chain facts, so **only 252 of the 757 rows are buildable, not 757**. One fault in 2,596 rows: `/` redirecting to `/`. **Board card: Redirect Strategy and Delivery.** Filed as `ASK__Only_252_Redirect_Rows_Are_Buildable_S104`.

**The 117 salvage heroes renamed, converted, imported and attached** (`6fcd3ab`), with an importer defect found and fixed: `attach_hero()` kept an existing thumbnail and refreshed neither picture nor alt. **Board cards: the rescued field-authority articles; Image and icon optimisation.**

**The process-text leak, found by Kain on a live page, fixed at source** (`82a04ec`, `8c7e7bb`, `69a259d`). All four parts of the S346 brief built, wired into the import path as well as the gate, and the publish gate now reads the finished page. **Board card: the harness and instruction sets.**

**The book note buy buttons** (`1d09247`, `920361d`): 59 of 67 published book notes carried one, 66 do now. The gate required a retired field and made the live one optional, which is why nothing ever went red. 46 records were short, not 8.

**Course links wired across the estate** (`fe2554d`, `588b2c3`): 221 records name a course, 132 linked to one, 216 do now. **This was Kain overruling Code's recommendation to defer, and he was right.**

**Three tools built that did not exist**: `article_body_update.py`, the first thing able to correct a page already live; `course_link_wiring.py`; `dsrd_line_index.py`. All registered with H9, payloads quoted.

**`channel_map.py` deleted** (`5596e4f`). **The book note course card aligned** at v0.167.65 (`6f610c1`), a theme edit made in a factory session on Kain's word in the sitting, per Rule 1's S334 loosening.

## Mistakes made in this session, named rather than buried

**A clearance expired unspent**, because a 115-page measurement takes nearly the 45 minutes a clearance lives and Code did other work while it ticked. Fixed by slicing into thirties.

**Eighteen duplicate drafts created in seconds**, by running `import_instructor_articles.py` for a plan when it pushes by default. All trashed under a takedown clearance; nothing public changed. **The underlying fault is still open:** those eighteen records carry pre-S309 slugs, so any future run repeats it.

**A gate built that refused everything.** The publish gate's rendered read fetched over the open internet, met SiteGround's 403, and treated an unreadable body as a refusal. Found by running it against a real page rather than trusting the fixtures.

**A citation invented rather than looked up.** A Gutenberg id built from a guess resolved to a children's Oz book and would have shipped as Adler's source. Caught by fetching every address and reading its title before use.

## Still owed, none of it started

Chat's `BRIEF__Three_Jobs_That_Close_Three_Cards_S348` and `ASK__The_Six_Elder_Pages_S348` both arrived at the close and are read but untouched. **The elder pages ask is time-critical: the Our People sitting is Tuesday 8 September.**

Also: the eleven folded redirect rows and the `/` to `/` row; the chapter 5 reset across all fifty records; `publish_gate.py`'s redirect mode; `--takedown` gaining the override route; the DSRD 6 record per page for the rescued set; the inbound links at stage 6; the re-score now the bars are written; the folder map measurement; the three DSRD sections and the line index; the 236-row re-read; the opener sweep; the testimonial filter colour; the `cite` measurement.

## Decisions waiting on somebody, carried so the next session need not rediscover them

1. **DSRD 6 owes the instructor-attributed type a bar of 88.** All seventeen score exactly 88, fifteen live for weeks. Chat says it is acting on this.
2. **`source_reference` cannot hold Karen's source.** The field accepts only a book note on the install, so `karen-ramsay-recorded-conversations` lands empty on all twelve. Named rather than invented, as the brief asked. **It is one find-and-replace and Chat offered to make it.**
3. **192 of 196 published articles have no WordPress author at all.** Every importer creates at author zero; the four with one were touched through the admin. No byline changes, because those come from the record's pen name, but it will surface in schema. **Who owns an article is a decision, so nothing was changed.**
4. **Seven author biographies carry a stray autosave** from 26 August, one a minute between 22:33 and 22:44, a machine walking through editors. The fault was fixed at source; this is residue, and it is what Kain saw when he opened one.
5. **The bin holds 21 items and Code does not empty bins.** Seventeen of the eighteen articles are proven duplicates by title or by slug; the eighteenth, `understanding-comes-before-influencing`, is I18 and is the only copy on the site. Its record is safe on disk and Code re-imports it once the bin is empty.

---

*No em or en dashes in this file; checked before writing.*
