# STOP: /academy/ does not exist, so nothing was created. The 35 row pairing is done and waiting.

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `SPEC__Create_The_35_School_And_Course_Pages_As_Drafts_S267.md`.
**Status: no page was created. Zero in, zero out.**

---

## 1. The stop, and it is the spec's own instruction

The spec says:

> "Before creating anything, confirm the `/academy/` parent page exists and report its state. Every one of the 35 hangs off it. If it does not exist, stop and ask rather than creating it, because it is a page in its own right with its own design."

**It does not exist.** Not as a page in any status, not as a post of any type, not as a rewrite rule, and not as anything that resolves. Four ways of looking, all on the live build site this session:

| What was looked for | Result |
|---|---|
| A page with the slug `academy`, any status including draft and trash | none |
| A post of any type with the slug `academy`, any status | none |
| A rewrite rule mentioning `academy` | none |
| `https://achologytest.com/academy/` fetched from the server | **404** |

For completeness, since the whole tree hangs off it: `/schools/` and `/courses/` are also 404.

The full page list is 26 pages, and the top level ones are About, Policies, Testimonials, Achology Reviews and Cards. There is no academy branch of any kind.

## 2. A second thing the spec assumes that is also not there

The spec says:

> "**Do not touch `/academy/schools/`.** It is the existing seven-paths listing page, not a school, and its slug must never be used as one."

**`/academy/schools/` does not exist either.** It returns 404 and there is no page behind it. DSRD 1 section 2.3 lists it as "Centralised schools page, seven paths, one mountain", so it is specified, but it has never been built.

I have obeyed the instruction, which cost nothing since there is nothing there to touch. It is reported because the spec described it as existing, and a brief written on the belief that a page exists may have been written on other beliefs of the same kind.

## 3. What this leaves as the question for Kain

`/academy/` is a page in its own right with its own design, which is exactly why the spec forbids me creating it. So the question is his:

**Does he want `/academy/` created now as an empty draft purely to be the parent, with its design done later, or does the whole set of 35 wait until the Academy landing page is properly specified and built?**

Both are defensible and it is not my call. Creating an empty draft parent is reversible and unlocks 35 pages of his clicking today; waiting keeps the tree from existing until the page that heads it has been designed. **If he says create it, I would need the same enumeration for it that Rule 8 requires of the 35: its title, copied from a document rather than written by me, and its template.** DSRD 1 section 2.3 gives it a purpose ("Academy landing page") but I could not find a canonical title for it anywhere, and inventing one is drafting.

The moment that comes back, the 35 are one scripted pass. Everything else is done and is below.

## 4. The 35 row pairing, complete, zero unmatched

Every slug in the spec matched exactly one entry in DSRD 5. **No slug was left unmatched and none needed a guess.**

The names below are copied out of DSRD 5 by the script, not typed by me, so a transcription error cannot survive into this table.

### The 7 schools, parent `/academy/`, template: none exists yet

| Slug | Canonical name, DSRD 5 section 2 | Address it will take |
|---|---|---|
| `neuro-linguistic-programming` | The School of Neuro-Linguistic Programming (NLP) | /academy/neuro-linguistic-programming/ |
| `cognitive-behavioural-psychology` | The School of Cognitive Behavioural Psychology (CBP) | /academy/cognitive-behavioural-psychology/ |
| `life-coaching` | The School of Life Coaching and Professional Helping | /academy/life-coaching/ |
| `person-centred-counselling` | The School of Person-Centred Counselling and Psychology | /academy/person-centred-counselling/ |
| `mindfulness` | The School of Mindfulness, Applied Insight and Wisdom (MIW) | /academy/mindfulness/ |
| `mental-health` | The School of Mental Health, Wellness and Emotional Resilience | /academy/mental-health/ |
| `personal-growth` | The School of Personal Growth and Development (PGD) | /academy/personal-growth/ |

### The 28 courses, parent as shown, template: none exists yet

| Slug | Canonical name, DSRD 5 section 1 | Address it will take |
|---|---|---|
| `diploma-modern-applied-psychology` | Diploma Course in Modern Applied Psychology (DiMAP) | /academy/neuro-linguistic-programming/diploma-modern-applied-psychology/ |
| `beginners-guide-nlp` | A Beginner's Guide to Neuro-Linguistic Programming (NLP) | /academy/neuro-linguistic-programming/beginners-guide-nlp/ |
| `nlp-practitioner` | Neuro-Linguistic Programming (NLP) Practitioner Training | /academy/neuro-linguistic-programming/nlp-practitioner/ |
| `nlp-master-practitioner` | Neuro-Linguistic Programming Master Practitioner Course | /academy/neuro-linguistic-programming/nlp-master-practitioner/ |
| `mindset-mastery-self-discovery` | Mindset Mastery: The Ultimate NLP-Based Guide to Self-Discovery | /academy/neuro-linguistic-programming/mindset-mastery-self-discovery/ |
| `cbt-toolkit` | The CBT Toolkit: Core Principles and Real-World Applications | /academy/cognitive-behavioural-psychology/cbt-toolkit/ |
| `cbt-practitioner` | Cognitive Behavioural Therapy (CBT) Practitioner Course | /academy/cognitive-behavioural-psychology/cbt-practitioner/ |
| `cbt-mental-health` | Cognitive Behavioural Therapy for Mental Health and Wellness | /academy/cognitive-behavioural-psychology/cbt-mental-health/ |
| `life-coaching-certificate` | Life Coaching Certificate Course (Beginner to Advanced) | /academy/life-coaching/life-coaching-certificate/ |
| `life-coaching-blueprint` | Life Coaching Blueprint: The Complete Process and Practices | /academy/life-coaching/life-coaching-blueprint/ |
| `skilled-helper` | The Skilled Helper Training Course (with Prof. Gerard Egan) | /academy/life-coaching/skilled-helper/ |
| `skilled-helper-practitioner` | Skilled Helper Practitioner Course (Advanced to Expert) | /academy/life-coaching/skilled-helper-practitioner/ |
| `hypnotherapy-practitioner` | Hypnotherapy Practitioner Course (Beginner to Advanced) | /academy/person-centred-counselling/hypnotherapy-practitioner/ |
| `counselling-skills-practitioner` | Counselling Skills Practitioner Course (Beginner to Advanced) | /academy/person-centred-counselling/counselling-skills-practitioner/ |
| `mindfulness-practitioner-diploma` | Mindfulness Practitioner Diploma Course (Beginner to Expert) | /academy/mindfulness/mindfulness-practitioner-diploma/ |
| `mindfulness-mental-health` | Mindfulness for Mental Health, Personal Growth and Inner Peace | /academy/mindfulness/mindfulness-mental-health/ |
| `mindfulness-leadership` | Mindfulness for Highly Efficient Management and Leadership | /academy/mindfulness/mindfulness-leadership/ |
| `mental-health-practitioner-diploma` | Mental Health and Wellbeing Practitioner Diploma Course | /academy/mental-health/mental-health-practitioner-diploma/ |
| `self-belief-emotional-intelligence` | The Self-Belief, Emotional Intelligence and Assertiveness Masterclass | /academy/personal-growth/self-belief-emotional-intelligence/ |
| `authentic-confidence` | Authentic Confidence, Core Identity and Self-Esteem Masterclass | /academy/personal-growth/authentic-confidence/ |
| `emotional-iq-social-skills` | Master Your Emotional IQ and Revolutionise Your Social Skills | /academy/personal-growth/emotional-iq-social-skills/ |
| `clarity-purpose-effectiveness` | The Clarity, Purpose and Personal Effectiveness Masterclass | /academy/personal-growth/clarity-purpose-effectiveness/ |
| `goal-setting-action-planning` | The Strategic Goal Setting and Action Planning Masterclass | /academy/personal-growth/goal-setting-action-planning/ |
| `communication-social-intelligence` | The Communication Skills and Social Intelligence Masterclass | /academy/personal-growth/communication-social-intelligence/ |
| `hyper-focus-productivity` | The Hyper-Focus, Self-Discipline and Productivity Masterclass | /academy/personal-growth/hyper-focus-productivity/ |
| `mental-toughness-resilience` | The Complete Mental Toughness and Inner Resilience Masterclass | /academy/personal-growth/mental-toughness-resilience/ |
| `healthy-marriage-relationships` | An Essential Guide to Healthy Marriage and Long-Term Relationships | /academy/personal-growth/healthy-marriage-relationships/ |
| `entrepreneurship-business` | An Entrepreneurs' Guide to Launching and Growing a New Business | /academy/personal-growth/entrepreneurship-business/ |

**7 plus 28 equals 35, and the row count above is 35.**

## 5. How the pairing was proved rather than eyeballed

The only judgement in this job is which DSRD 5 course each slug refers to, so that is the thing the checks attack. The script holds slug to course **number**; it never holds a course name, because a name typed by me could be wrong and survive. Every name in the tables above is read out of DSRD 5 by number at run time.

Seven checks, all passing:

1. DSRD 5's catalogue holds 28 courses. Found 28.
2. Seven school slugs, no duplicates.
3. Twenty eight course slugs, no duplicates.
4. Every school name claimed appears verbatim in DSRD 5 section 2.
5. Every course number claimed exists in DSRD 5 section 1.
6. **All 28 course numbers are used exactly once.** This is the check that makes a wrong pairing nearly impossible to hide: any slug pointed at the wrong course leaves one course used twice and another unused.
7. **Every course is homed under a school whose DSRD 5 section 3 bundle actually contains it.** This catches a slug matched to the right course but filed under the wrong school.

**The checks were made to fail before they were believed.** Run against a deliberately broken mapping, with one slug pointed at a course number that does not exist and `cbt-toolkit` moved under mindfulness where DSRD 5 does not list it, checks 5, 6 and 7 all went red and named both planted faults. A check that has never been seen to fail is not evidence.

**One thing that looks like a discrepancy and is not.** DSRD 5 section 3 gives the CBP school five courses while the spec homes only three course pages under it. That is correct and expected: nine courses appear in more than one bundle (section 4), DiMAP in all seven, and a page can only live at one address. Each of the 28 gets exactly one canonical home and appears in the other bundles' listings by query. Check 7 is written to allow exactly that, which is why it tests bundle membership rather than exclusive ownership.

## 6. The two templates

Neither exists. The theme currently registers four page templates: Policies Index, Our People, Policy Page and Author Profile. There is no school template and no course template.

Per the spec, the 35 will be created with no template assigned, and switched onto the real ones in one pass when those are signed. **No placeholder template has been created.**

## 7. The second job in that commission, and why it is not started

The two admin menu entries, Courses and Schools, filter the Pages list by template. There is no template to filter on, and no page to filter. The spec itself says to build it when the templates exist. Not started, deliberately.

## 8. The question in that commission about internal linking across the 249

That is a separate answer and it is not in this file. It needs a real count off the live database rather than a recollection of which pass ran, and it travels back on its own so it does not ride on a page creation report.

*No em or en dashes in this file; checked before writing.*
