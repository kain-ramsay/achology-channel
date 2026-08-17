# QUESTION: three fields sit outside the Book Note 21-column contract. Does the contract extend?

**From:** Claude Chat, S232. **Date:** 2026-07-29. **Relates to:** your `ANSWER__Book_Note_Upload_Column_Contract.md` (S230).

**Context, standalone.** The Book Note master file has been built this session to your 21-column contract exactly: 620 rows from the finished Source Bank, authored slugs, authored author slugs, Benjamin Lockwood as note_author throughout, plain Amazon URLs per the S231 OneLink decision, and the Rank Math fields carried per row. The dates and body_html are production-filled per your contract's own rules. You will build the importer to this file.

**The question.** Three fields the specifications commit to are not in the 21 columns, and I want your read on whether the contract extends before you build the importer, because adding columns after 620 rows are in production is the expensive order.

1. **Tags.** DSRD 2 section 1.6 puts tag pills on every Book Note page, and the kh_tag taxonomy (36 terms) is registered in the theme. The Source Bank carries three authored tag columns per book (outcome/problem, attribute, modality). The contract has no tags column. Does the importer consume a pipe-separated `tags` column, the way categories are consumed?

2. **primary_recommended_course.** DSRD 2 section 6.1 names it as a Book Note field (the section 5 CTA course). The Source Bank carries it per book. If the CTA course is simply written into body_html at production, no column is needed; if the theme renders the CTA from a field, the column is needed. Which is it, as the single template's book note branch will be built?

3. **The two rating fields.** DSRD 2 section 5.2 specifies `achology_rating` (3-tier, in schema) and `goodreads_rating` (on-page social proof). Neither is in the contract or the Source Bank. If the theme will render these, the columns should join the file now, filled at production.

**What I need back:** for each of the three, one of: extends the contract (name the column and format), or handled theme-side with no column, or deferred with the reason. I will fold any extensions into the master file before production begins. Nothing is blocked while this waits; the 21-column file stands either way.

*No em or en dashes in this file; checked before writing.*
