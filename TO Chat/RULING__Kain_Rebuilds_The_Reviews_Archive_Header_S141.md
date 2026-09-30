**Needs from Chat:** write these rulings and Kain's two lines of copy into their owning documents (DSRD 9 section 29.6 for the Reviews archive controls; the Reviews page copy record for the wording). For the factory session.

# RULING: the Reviews archive header is rebuilt, with Kain's wording

**From:** Claude Code, S141 (factory, theme edit on Kain's word in the sitting), Wednesday 30 September 2026. **To:** Claude Chat.

## Kain's words, in the S141 sitting

- Asked for "best design proposals for improving the look and functionality" of the archive heading, lead and search box. Four rendered options (one search line, rating chips, ratings at a glance, today's tidied): "I actually really like option C, ratings at a glance ... this is a great opener for the reviews that follow ... there's quite a lot of white space".
- Four spacing variants of C; he chose C3, "search across the top", adding: "put some basic instructions in brackets after search" and "make sure all the text aligns ... search and course and ratings ... can't be sitting clean with the edge of the search box, they've got to be in a little bit ... same with the sentence underneath ... we need a rule for tidying that". Then asked for the hint sentence back under Course and Rating.
- **His exact text, given in the sitting:**
  - Label: "Search (for any word a student might have used in their review)"
  - Hint: "Search for terms that a past student might have used in their review (such as knowledge, I learned, insights, understanding, good, bad, or learning)."

## What shipped, theme v0.707.11 (/reviews/)

- One panel: the search line (field and button) across the top; course, rating and the hint on the left; "Reviews by rating" on the right, five rows each with its bar and real count, each row a link that filters to that rating (keeping search and course) and lands on the results. Counts read from the bank by `achology_review_rating_chart()`, cached against the bank's size; live today 2,897 / 541 / 621 / 223 / 234 (published only).
- **The alignment rule (Kain's):** every label and caption starts where the writing inside its box starts, --sp-md in. Labels now plain Mulish 14, no capitals. Archive title 28, lead soft grey, as on the approved render.
- **Two fixes of the S141 evaluator's blockers:** the form lands on #reviews-archive (a search no longer reloads at the top); "Show more reviews" is back (a cached view never set the page count, so only 50 of 4,516 reviews could be reached).
- Tested live: search "coach" lands on the archive, 327 results; the 4.5 row filters to 541 and marks itself current; show-more present in both.

## A number Chat may want to rule (again)

The published counts sum to 4,516 with 4.5 at 541, matching the page's "4,516"; their average is about 4.62 against the page's 4.66. Kain's S052 "do not update the numbers" ruling stands; the gap is named for Chat, not changed.

## Later the same sitting (v0.707.13 to v0.707.17)

- **Reviews header lead, Kain's final text:** "Since launching our first course in 2014, we've learned from thousands of reviews that students have shared about our courses. Yes, some are better than others, but they can all help you decide whether studying with Achology is the right choice for you."
- **Map section heading, Kain's text:** "Achology Reaches Learners Across 216 Countries". **Its sentence:** "There's a good chance someone in your city has reviewed Achology in the last few months." Both pages carrying the block; the old "Our Reviews" link on Testimonials went with the old sentence.
- **Second header button, Kain's idea:** "Watch Testimonials", monitor-play glyph, to /testimonials/. **"Read the Reviews" primary** on Kain's yes, per DSRD 7 section 5: "one primary solid and one secondary or ghost, never two of the same style".

## Still owed on the Reviews card

The closing enquiries panel onto `.policy-closing`; the header nudge's "Explore Access All Areas" (site-wide, its own change set); Kain's last Safari look; the §8 re-walk and the record.

OWED BACK: the dated lines and the copy in their owning documents.

*No em or en dashes in this file; checked before writing.*
