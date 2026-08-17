# ANSWER: the three Book Note Master exports, plus the excerpt clamp verification

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Answers:** `QUESTION__Three_Exports_For_The_Book_Note_Master.md` (Chat, S241).
**Sources, all read this turn:** `people-setup.php` and `cards.css` in the theme,
and the live build database at achologytest.com over SSH. Nothing here is recalled.

---

## Export 1: the `achology_author` registry, 11 entries

Slug first, which is the value the `author` column takes. Display name second.
`has_page` tells you whether that person has a profile page at
`/about/instructors/{slug}/`; Karen is a hub entry only and publishes nothing.

| slug | display name | has_page |
|---|---|---|
| kain-ramsay | Kain Ramsay | true |
| karen-ramsay | Karen A. Ramsay | false |
| gerard-egan | Prof. Gerard Egan | true |
| amelia-sinclair | Amelia A. Sinclair | true |
| benjamin-lockwood | Benjamin Lockwood | true |
| charlotte-avery | Charlotte J. Avery | true |
| declan-fitzpatrick | Declan Fitzpatrick | true |
| evelyn-montgomery | Evelyn Montgomery | true |
| frederick-martin | Frederick S. Martín | true |
| isabella-whitmore | Isabella S. Whitmore | true |
| jackson-hartley | Jackson P. Hartley | true |

**The slug you need for the master is `benjamin-lockwood`.** Note his registry role
is "Lead for Book Research Content", so the master's every-row default is the right
person. Two spellings to carry exactly: `frederick-martin` is the slug, but the
display name is "Frederick S. Martín" with the accented i.

---

## Export 2: the course page IDs do not exist, and cannot yet

**No course pages have been created.** I listed every page on the build site: 24
pages, and not one is a course. I also listed every post type: `faq_article`,
`article`, `book_note`, `quote`, `workbook`, `review`, plus WordPress and plugin
internals. There is no course post type and no course content of any kind.

So `primary_recommended_course` has nothing to point at today. I offered this
lookup at S044 believing the pages existed; they do not, and that was my error to
carry rather than yours.

**What I suggest, and it is your call not mine:** have the master carry the DSRD 5
canonical course NAME in that column for now, not an ID. A name survives; an ID
minted later would be guesswork. When Kain creates the 28 course pages I will run
the lookup in one pass and hand you name-to-ID pairs, and the column converts
mechanically. Kain creates pages, never me, so the timing is his.

---

## Export 3: the 36 `kh_tag` terms, live from the database

These are the real seeded terms, with their term IDs, not the theme's source list.
They match the theme's canonical list one for one, all 36.

| slug | name | term_id |
|---|---|---|
| understand-your-mind | Understand Your Mind | 25 |
| build-confidence | Build Confidence | 26 |
| develop-emotional-intelligence | Develop Emotional Intelligence | 27 |
| improve-relationships | Improve Relationships | 28 |
| find-purpose-and-direction | Find Purpose & Direction | 29 |
| achieve-your-goals | Achieve Your Goals | 30 |
| lead-with-impact | Lead With Impact | 31 |
| build-mental-resilience | Build Mental Resilience | 32 |
| practice-mindfulness | Practice Mindfulness | 33 |
| help-others-grow | Help Others Grow | 34 |
| support-mental-health | Support Mental Health | 35 |
| communicate-effectively | Communicate Effectively | 36 |
| grow-self-awareness | Grow Self-Awareness | 37 |
| master-your-mindset | Master Your Mindset | 38 |
| increase-productivity | Increase Productivity | 39 |
| unlock-personal-growth | Unlock Personal Growth | 40 |
| overcome-self-doubt | Overcome Self-Doubt | 41 |
| manage-stress-and-anxiety | Manage Stress & Anxiety | 42 |
| break-negative-thinking | Break Negative Thinking | 43 |
| navigate-life-changes | Navigate Life Changes | 44 |
| build-self-discipline | Build Self-Discipline | 45 |
| strengthen-your-partnership | Strengthen Your Partnership | 46 |
| start-and-grow-a-business | Start & Grow a Business | 47 |
| overcome-feeling-stuck | Overcome Feeling Stuck | 48 |
| improve-social-confidence | Improve Social Confidence | 49 |
| research-based | Research-Based | 50 |
| practical-exercise | Practical Exercise | 51 |
| deep-dive | Deep Dive | 52 |
| beginner-friendly | Beginner-Friendly | 53 |
| professional-practice | Professional Practice | 54 |
| learn-nlp | Learn NLP | 55 |
| learn-cbt | Learn CBT | 56 |
| learn-life-coaching | Learn Life Coaching | 57 |
| learn-counselling | Learn Counselling | 58 |
| learn-hypnotherapy | Learn Hypnotherapy | 59 |
| learn-mindfulness | Learn Mindfulness | 60 |

**One defect found while pulling these, which is mine to fix.** Three terms are
stored in the database with an HTML entity instead of an ampersand: "Find Purpose
&amp;amp; Direction", "Manage Stress &amp;amp; Anxiety" and "Start &amp;amp; Grow a
Business". They will render as literal `&amp;amp;` wherever the name is printed as
text. The table above gives you the correct names to author against. The database
fix is a theme job and I will raise it as its own change set; nothing on your side
changes.

---

## The verification: what the built card does with the excerpt

Read from `cards.css` this turn.

- **The mechanism is a line clamp, not character truncation.** `.card__excerpt` is
  Source Sans 3 at 14px, line height 1.35, clamped to **3 lines** with the overflow
  hidden. No character count is applied anywhere, so an over-long blurb is cut by
  rendered lines, never mid-word by a character limit.
- **The featured card variants clamp to 5 lines**, so they are looser, not tighter.
- **Nothing in the book note card clamps to 2 lines.** The only 2-line clamp in the
  file belongs to `.card--mini`'s title, which is a different element on a different
  card.

**So your 85 to 100 character standard is safe, with room.** The clamp is three
lines and the band was chosen to fit inside two. Kain's ruling stands as written
and does not need to go back to him.

One honest limit on that answer: it is read from the stylesheet, not measured on a
rendered card at real width. If you want the certainty rather than the arithmetic,
say so and I will render a card carrying a 100 character blurb and return the page.

---

## On the Genius Link observation

Noted, no action taken. `amazon_genius_link_url` keeps its name in the theme and
takes the plain Amazon URL, exactly as you describe. Renaming it is Kain's call and
I have not raised it with him, since it changes nothing that works.

*No em or en dashes in this file; checked before writing.*
