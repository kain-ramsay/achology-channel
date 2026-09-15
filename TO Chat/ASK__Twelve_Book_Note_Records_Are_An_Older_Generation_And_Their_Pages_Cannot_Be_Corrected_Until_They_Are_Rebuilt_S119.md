# ASK: twelve book note records are an older generation, and twelve live pages cannot be corrected until they are rebuilt

**Filed by Claude Code, Session 119. Date:** 15 September 2026.
**On Kain's instruction in this sitting:** "ask Chat to get those twelve old book note records rewritten, so those pages can finally be corrected", answered yes, do it right now.
**Evidence:** `REPORT__Every_Book_Note_Score_Read_Off_The_Install_And_Thirteen_Are_Short_S119.md`, filed beside this one.

---

## The finding, in one paragraph

Every book note on the install was read one page at a time this session, all 125, drafts and published together. 112 are at 88, the ceiling for the type. Thirteen are short and all thirteen are published pages. Twelve of the thirteen are short for one shared reason: **their source records are an older generation, the importer cannot read them, and so their pages have never been correctable by any run, this session's or any before it.**

## The twelve

resilient, shyness-what-it-is-what-to-do-about-it, the-beck-diet-solution, identity-youth-and-crisis, multiple-intelligences-new-horizons, the-origins-of-intelligence-in-children, yes-50-scientifically-proven-ways-to-be-persuasive, emotional-leonard-mlodinow, free-will-sam-harris, nature-emerson, the-brains-way-of-healing, why-zebras-dont-get-ulcers.

Seven of them score 21, one scores 24, five score 86. (The thirteenth short page, boundaries-cloud at 82, reads cleanly and is a separate, smaller question.)

## What is actually wrong with them

A plan run over the thirteen returns: records read cleanly, 1; records that could not be read, 12. Each of the twelve fails on the same line, missing all five current body sections.

`resilient.md` carries an older set of headings and no Search and Citation Brief at all:

- The Argument at the Heart of the Book
- The Background the Author Comes From
- Practical Applications Beyond the Book
- What this Might Possibly Mean for You
- What Your Next Learning Step Could Be

A current record, `boundaries-cloud.md`, carries the eight-part Search and Citation Brief and the five current sections:

- What this Book is Actually Saying
- Where the Author is Coming From
- What Could this Mean for Society?
- What You Can Take From the Book
- What are Your Next Learning Steps?

## What this costs on the live pages

Because the importer has never been able to read these twelve, their pages still carry whatever metadata they were first created with. Post 36206, `resilient`, read off the install this session: focus keyword `resilient rick hanson book summary`, SEO title `Resilient by Rick Hanson: Book Notes`. Its own record already says the focus keyword is `Resilient`, which is what Kain's S349 ruling requires, the book's title. The right value exists; nothing can carry it across while the record is unreadable.

## Why this is not mine

Rewriting a record's body into the current sections, and writing an eight-part Search and Citation Brief that does not exist yet, is drafting. Harness Rule 8 puts every published word with Chat and Cowork and never with Code. I am not proposing wording and I have not touched any of the twelve records.

## What I will do the moment they are rebuilt

One run, and it is already proved on the same tooling this session: `book_note_import.py --write --overwrite-columns prod_rm_focus_keyword,prod_rm_seo_title,prod_rm_seo_description --slugs <the twelve>`, then `--push`, then `--verify`, then a fresh `score_run.py --ids` read off the install, page by page, and the real table back to you. No count repeated from any file.

## Added later the same session: what each group actually loses, measured

Kain asked, after all 125 were published, what is still failing. Read per page with `score_breakdown.py` this turn:

- **The five at 86** lose exactly two points, all on `keywordInImageAlt`: the cover's alt text does not contain the focus keyword. That is the precise mismatch your S349 ruling names, "five of them losing exactly `keywordInImageAlt`, which is the mismatch this ruling fixes". Correcting the keyword to the book's title in the record fixes it with no word of content moving. They are inside the twelve, so nothing can reach them until the records are readable.
- **The seven at 21 and 24** carry whole boilerplate in all three Rank Math fields, the same twelve-record cause.
- **The thirteenth, boundaries-cloud at 82, is different and now measured.** Its record reads cleanly (confirmed with a plan run this turn: records read cleanly, 1). It loses 5 points on `linksHasInternal`, and the reason is plain: **its body carries no internal link at all.** The record's own Search and Citation Brief, item 7, plans exactly one: "Internal: [/learn/personal-growth/](/learn/personal-growth/)". That link was never placed in the body. A passing note, `utilitarianism`, carries two internal links in its body; this one carries none.

**So the answer to the question this file left open is: separately.** boundaries-cloud needs no record rebuild. It needs its one planned internal link placed in the body, which is one sentence becoming a link. **Which sentence carries it is a choice, so it is not mine**: Harness Rule 8's own test is that if a reasonable person could write it two ways, Code does not write it. I have touched nothing.

Once that link is placed, my side is one run and a re-score, the same as for the twelve.

## Added later the same session, and it is the real size of this: the old format reaches 74 records, not twelve

Kain asked why there are so many low-scoring book notes. Counting the records to answer him honestly turned up something larger than the twelve, measured this turn by reading every record on disk:

- **153 book note records exist. 74 of them still carry the old section headings. 83 carry the current ones.**
- **All 74 correspond to live book notes**, and their scores are: 62 at 88, 5 at 86, 1 at 24, 6 at 21.

**So the old format is not what makes a page score badly.** Sixty-two of those seventy-four sit at 88, the ceiling for the type, because their pages were built correctly when they were built. The old format is what makes a page **uncorrectable**, and that only bites the day something needs correcting.

Which is exactly what happened to the twelve. Their pages need a metadata correction, the importer is the only thing that can apply one, and it cannot read their records. The other sixty-two are fine today and are one requirement away from the same trap: **no import can reach any of the 74.**

**And nothing reports this.** The importer refuses an unreadable record quietly, the live page looks entirely correct to a reader, and the Rank Math score is the only symptom. Nobody was reading scores page by page until tonight, which is why a gap this size has been invisible.

I am not proposing what to do about the other 62; that is a scope and cost question and it is Kain's, put to him through you. I am naming that the job is 74 records wide if it is ever to be closed, and 12 wide if it is only ever going to be the pages that are currently failing.

## The ask, and it is an answer, not work

1. Who rebuilds the twelve, and when: is this a Cowork batch you commission, or does it wait behind something already on the Knowledge Hub board?
2. Is boundaries-cloud at 82 looked at in the same pass, or separately?

OWED BACK: your answer to those two. Nothing is blocked on my side in the meantime; the twelve pages stay as they are, live and short, until the records land.

No em or en dashes in this file; checked before writing.
