# REPORT: the tagging mechanism explained back, measured, and two conflicts found

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Answers:** `MECHANISM__Course_Tagging_And_How_A_Page_Picks_Its_Courses_S252.md`.
**Nothing built yet**, as instructed. This is the explain-back and the three reports.

## 1. The mechanism, in my own words

**The tag holds the relationship. The content holds tags. The course holds nothing.**

That last part is the piece I had backwards. I went looking for a tag field on a course, found none, and concluded there was no rule. There was never going to be a field there: a course is the destination, not the origin. The mapping lives in exactly one place, the tables at DSRD 1 §5.2, §5.3 and §5.5, and is read from there.

**A content attribute tag does nothing.** Research-Based, Practical Exercise, Deep Dive, Beginner-Friendly and Professional Practice describe the piece, not the reader's goal. They map to no course, they are dropped before ranking, and they are also not counted in the two-to-four limit a piece of content is allowed.

**How a page picks its courses:** take the page's tags, throw away the content attribute ones, look up each remaining tag's mapped courses in DSRD 1 §5, resolve every abbreviated name through DSRD 5 because DSRD 1 explicitly defers to it, count how often each course appears across those tags, and show the top N. Two on a Knowledge Hub content page, up to three on a tag landing page.

**Why the abbreviations are safe.** DSRD 1 states at the head of §5 that its tables use short names for readability and that this is a named exemption, with DSRD 5 as the source of truth. So the tables are a lookup key, never a name to display.

**What I got wrong and why it matters.** My stand-in picked the nearest course by school. That is a different mechanism, invented because I could not find this one, and it would have shipped a plausible-looking wrong answer on 598 pages. The rule was written before I started.

## 2. Your three questions, measured

**1. Do the 36 tags exist as real terms in WordPress?**

**Yes. All 36.** `wp term list kh_tag --format=count` returns 36 on the build site. The mechanism can run.

**2. Does the content carry tags, and on how many rows?**

**All 620 rows of the Book Note master carry tags.** Distribution:

| Tags on a row | Rows |
|---|---|
| 2 | 86 |
| 3 | 283 |
| 4 | 148 |
| 5 | 70 |
| 6 | 23 |
| 7 | 6 |
| 8 | 3 |
| 9 | 1 |

Every slug on every row resolves to a tag in DSRD 1 §5. Zero unknowns.

**3. What does the mapping yield on the one live book note?**

`mans-search-for-meaning` carries three tags:

| Tag | Mapped courses |
|---|---|
| find-purpose-and-direction | Clarity/Purpose/Effectiveness, Goal Setting, Life Coaching Certificate |
| build-mental-resilience | Mental Toughness, CBT for Mental Health, Mindfulness for MH |
| understand-your-mind | DiMAP, CBT Toolkit, Mindset Mastery |

**Nine courses, each appearing exactly once. A nine-way tie for first place.** The rank rule cannot pick two, or three, from that.

Checked by hand against the tables as you asked: the three tags share no course between them, which is why every count is one.

## 3. The tie problem, which is bigger than one page

I ran the rank rule across all 620 rows. **It resolves cleanly on 57% of them and ties on the rest.**

| Outcome | Rows |
|---|---|
| Clean top two | 356 |
| 6-way tie | 95 |
| 3-way tie | 77 |
| 9-way tie | 35 |
| 8-way tie | 21 |
| 5-way tie | 9 |
| 4-way tie | 7 |
| 10-way tie | 7 |
| 7-way tie | 7 |
| 12-way tie | 3 |
| 11-way tie | 2 |
| 13-way tie | 1 |

**264 of 620 book notes tie at the top.** The cause is structural, not accidental: a row with three tags that share no courses produces nine courses all on one, and three tags sharing nothing is the common case rather than the odd one.

**No tiebreak invented, as instructed.** Kain rules it once on these numbers. What he is choosing between is worth naming: any tiebreak on a nine-way tie is effectively picking two courses out of nine by a rule that has nothing to do with the reader, so the honest options are probably a deliberate secondary sort (student count, price, school) or accepting that some pages show a different pair than a human would choose.

## 4. Two conflicts found. Neither is mine to resolve.

**Conflict one: the tag slugs. The specification and the database disagree, and the content follows the database.**

DSRD 1 §5.6 says a slug is the tag name "lowercased and hyphenated, with ampersands dropped". Applied literally, `Find Purpose & Direction` becomes `find-purpose-direction`.

The theme registered `find-purpose-and-direction` at S044, turning the ampersand into "and", and all 36 terms are in the database under the theme's version. The master's 620 rows are tagged to the theme's version too.

**Three tags differ, and they carry 243 of the 620 rows:** `find-purpose-and-direction` (174 rows), `manage-stress-and-anxiety` (50), `start-and-grow-a-business` (19).

The database and the content agree with each other and disagree with the spec. My first measurement used §5.6 literally and reported those three as unmapped tags, which is how it surfaced. **Either §5.6's wording is corrected to say ampersands become "and", or 36 terms and 620 content rows are re-slugged.** The first looks obviously right to me but it is a DSRD change and it is yours.

**Conflict two: nine abbreviated names do not resolve yet.**

DSRD 1's tables use 29 distinct short names. The courses registry I built for the Book Note page carries the 20 the master uses. **These nine appear in DSRD 1 §5 but nowhere in the master, so they have no alias yet:** CBT Practitioner, Hypnotherapy, Life Coaching Blueprint, Mindfulness for MH, Mindset Mastery, NLP Master Practitioner, NLP Practitioner, Skilled Helper, Skilled Helper Practitioner.

**This one IS mine** and it is mechanical: each resolves to exactly one DSRD 5 course by inspection, and I add them to the registry's alias list. Flagging it rather than doing it silently because "Hypnotherapy" and "Skilled Helper" are the sort of shortening where I want the resolution on the record: Hypnotherapy Practitioner Course, and The Skilled Helper Training Course with Prof. Gerard Egan, as distinct from Skilled Helper Practitioner Course.

## 5. What I am waiting on before building

1. **The tiebreak ruling**, on the numbers above.
2. **The slug conflict**, spec or database.
3. **Confirmation on the count**, since you flagged it: DSRD 1 says two courses on a Knowledge Hub content page, and DSRD 9 §32.1 as amended this session says three at desktop for the Book Note page. You said you would reconcile once I reported what the mapping yields. It yields nine tied, so the count question is downstream of the tiebreak.

The nine aliases I will add regardless, since they are needed under any ruling.

**The stand-in stays live and wrong in the meantime**, on one test post, and I would rather say that plainly than quietly leave it. `achology_course_companions()` is picking by school on `mans-search-for-meaning` right now.

*No em or en dashes in this file; checked before writing.*
