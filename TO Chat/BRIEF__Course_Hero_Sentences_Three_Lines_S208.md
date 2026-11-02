**For Chat. What this needs from you:** 28 course hero sentences, one per course, drafted to the Content Standard and signed by Kain, each no more than 185 characters with spaces. Kain asked for this today; Code supplies the limit and the check, the words are yours.

# BRIEF: the 28 course hero sentences, three lines at most (Code, S208, 2 November 2026)

**Kain's words, 2 November 2026:** "I do not want the short description of this course breaching beyond three lines ... Three lines must be the maximum ... Can you help me draft 28 course subtitle descriptions like this?"

**What the sentence is.** The one sentence under the course title in the course page hero (spec: DSRD 2 section 2.6, Course Hero Descriptions; today in the theme's data/courses.json as hero_description, 167 to 190 characters). It is the hero's only explanation of the course, read straight after the title and before the four figures and the Buy button. It is also the page's meta description source (signed spec, section 2), so it is what search results and AI assistants quote.

**The limit, measured, not guessed.** In the redesigned hero (Kain's pick, Article Band, Stronger) the sentence sits at 18 pixels in Mulish on a 560 pixel measure. Code measured all 28 current sentences on the real page in WebKit: every one is three lines at 560. **Write each new sentence to 185 characters or fewer, spaces included.** Code checks each against the real page before it lands and returns any that run to a fourth line.

**What makes it work for this page** (Code's notes from the hero design; the writing rules are the Content Standard's):
1. It says what the reader will understand or be able to do, in their terms, in the first half of the sentence.
2. No course name repeated (the title sits directly above it), no school name (the breadcrumb carries it), no price, figures or guarantee (the hero shows them beneath).
3. One sentence. No dashes (house rule). The full course name is never shortened elsewhere on the page (Kain, S180).
4. It stays true to the course's own lessons (data/lectures/{slug}.json, each lesson's question and description) and makes no promise of qualification or outcome the certificate block does not support (DSRD 9 section 24).

**Done when** 28 signed sentences, each 185 characters or fewer, are in a RULING in TO Chat, keyed by course number. Code then writes them into the course data, checks each on the real page at three lines, and puts the hero round to Kain with them in place.

*No em or en dashes in this file; checked before writing.*
