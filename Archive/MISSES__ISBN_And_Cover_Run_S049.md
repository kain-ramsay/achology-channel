# MISSES: the ISBN, Amazon URL and cover run

**From:** Claude Code, S050. **Date:** 2026-08-06.
**Answers:** `COMMISSION__ISBN_Amazon_URL_And_Cover_Collection_Run_S250.md` section 5 item 1.
**Read with:** `RECORD__ISBN_And_Cover_Run_S049.md`, which carries the summary.

Every row below is a row where `cover_status` is not `ok`. It is a work list, in four parts, hardest first. The first three parts are the 64 books that **cannot publish** until somebody finds a cover by hand, because a missing cover blocks the Book Note page with no fallback. The fourth part is 44 books that can publish today but would look better with a bigger picture.

Each book gives its title, its author, its slug (the filename to save a cover under, plus `.jpg`), and the ISBN where one was found.

---

## No ISBN found (41 books)

**What failed:** Step 1, the ISBN lookup. Neither Open Library nor Google Books returned an ISBN for this title and author, so no Amazon URL and no cover could be derived.

**The hand work:** find the book on Amazon or Google Books, copy the 10 digit ISBN into the master's `isbn` column, and the rest follows mechanically. Several of these are classics under a title or a translation the free catalogues index differently.

| Book | Author | Slug | ISBN |
|---|---|---|---|
| Breaking Free of Compulsive Eating | Geneen Roth | `breaking-free-of-compulsive-eating` | not found |
| Chuang Tzu (Zhuangzi) | Zhuangzi | `chuang-tzu` | not found |
| Co-Active Coaching | Henry Kimsey-House, Karen Kimsey-House, Phillip Sandahl | `co-active-coaching` | not found |
| Cognitive Behavioural Therapy with Couples and Families | Frank Dattilio | `cognitive-behavioural-therapy-with-couples-and-families` | not found |
| Counseling the Culturally Diverse | Derald Wing Sue and David Sue | `counseling-the-culturally-diverse` | not found |
| Emotional Intelligence 2.0 | Travis Bradberry and Jean Greaves | `emotional-intelligence-2-0` | not found |
| Getting to Yes | Roger Fisher and William Ury | `getting-to-yes` | not found |
| Great by Choice | Jim Collins and Morten T. Hansen. | `great-by-choice` | not found |
| Intentional Interviewing and Counseling in a Multicultural Society | Allen E. Ivey and Mary Bradford Ivey | `intentional-interviewing-and-counseling-in-a-multicultural-society` | not found |
| Jonathan Livingston Seagull | Richard Bach | `jonathan-livingston-seagull` | not found |
| Make Your Bed | Admiral William H. McRaven | `make-your-bed` | not found |
| No Excuses! The Power of Self-Discipline | Brian Tracy | `no-excuses-the-power-of-self-discipline` | not found |
| Phantoms in the Brain | V.S. Ramachandran | `phantoms-in-the-brain` | not found |
| Psychology from the Standpoint of a Behaviorist | John B. Watson | `psychology-from-standpoint-behaviorist` | not found |
| Psychology: The Briefer Course | William James | `psychology-briefer-course` | not found |
| Set Boundaries, Find Peace | Nedra Glennon Tawwab | `set-boundaries-find-peace` | not found |
| The 4-Hour Work Week | Tim Ferriss | `the-4-hour-work-week` | not found |
| The Aladdin Factor | Jack Canfield and Mark Victor Hansen | `the-aladdin-factor` | not found |
| The Art of Living | Epictetus (Sharon Lebell interpretation) | `the-art-of-living` | not found |
| The Art of Possibility | Rosamund Stone Zander and Benjamin Zander | `the-art-of-possibility` | not found |
| The Bhagavad Gita | Eknath Easwaran (translator) | `the-bhagavad-gita` | not found |
| The Book of Joy | Dalai Lama XIV and Desmond Tutu | `the-book-of-joy` | not found |
| The CBT Toolbox | J Riggenbach | `the-cbt-toolbox` | not found |
| The Courage to Be Disliked | Ichiro Kishimi | `the-courage-to-be-disliked` | not found |
| The Decision Book | Michael Krogerus | `the-decision-book` | not found |
| The Design of Everyday Things | Don Norman | `the-design-of-everyday-things` | not found |
| The Dhammapada | Buddha (trans. Eknath Easwaran) | `the-dhammapada-easwaran` | not found |
| The Frontiers of Knowledge | A.C. Grayling | `the-frontiers-of-knowledge` | not found |
| The History of Philosophy | A.C. Grayling | `the-history-of-philosophy` | not found |
| The Inside-Out Revolution | Micheal Neill | `the-inside-out-revolution` | not found |
| The Joyful Wisdom (The Gay Science) | Friedrich Nietzsche | `joyful-wisdom` | not found |
| The Knowledge Illusion | Steven Sloman and Philip Fernbach | `the-knowledge-illusion` | not found |
| The Little Book of Big Change | Amy Johnson | `the-little-book-of-big-change` | not found |
| The Mindfulness and Acceptance Workbook for Anxiety | John Forsyth | `the-mindfulness-and-acceptance-workbook-for-anxiety` | not found |
| The Narcissism Epidemic | Dr. Jean Twenge | `the-narcissism-epidemic` | not found |
| The Power of Ambition | Jim Rohn | `the-power-of-ambition` | not found |
| The Stranger | Albert Camus | `the-stranger` | not found |
| The Ultimate Life Coaching Handbook | Kain Ramsay | `the-ultimate-life-coaching-handbook` | not found |
| To Have or to Be? | Erich Fromm | `to-have-or-to-be` | not found |
| Tools of Titans | Tim Ferriss | `tools-of-titans` | not found |
| Why Has Nobody Told Me This Before? | Dr Julie Smith | `why-has-nobody-told-me-this-before` | not found |

---

## ISBN found, no cover held anywhere (18 books)

**What failed:** Step 4, the cover download. The ISBN resolved, but no cover image was held for it by Apple Books or Open Library.

**The hand work:** the identification is right, so this is a picture hunt only. The publisher's own page and the Amazon product page both carry a usable cover.

| Book | Author | Slug | ISBN |
|---|---|---|---|
| Built to Last | Jim Collins | `built-to-last` | 1844135845 |
| Cognitive Behaviour Therapy | Judith Beck | `cognitive-behaviour-therapy` | 1009090941 |
| Compassion and Self-Hate | Theodore Rubin | `compassion-and-self-hate` | 0345248856 |
| Getting the Love You Want | Harville Hendrix | `getting-the-love-you-want` | 9570805803 |
| How We Decide | Jonah Lehrer | `how-we-decide` | 1299880886 |
| On Being a Therapist | Jeffrey Kottler | `on-being-a-therapist` | 1555422136 |
| On Old Age and On Friendship | Cicero | `old-age-friendship` | 1797020587 |
| Peace Is Every Step | Thich Nhat Hanh | `peace-is-every-step` | 0938051393 |
| The Archetypes and The Collective Unconscious | Carl Jung | `the-archetypes-and-the-collective-unconscious` | 1317534603 |
| The Attention Merchants | Tim Wu | `the-attention-merchants` | 1782394842 |
| The Deepest Well | Nadine Burke Harris | `the-deepest-well` | 1508254176 |
| The Demon-Haunted World | Carl Sagan | `the-demon-haunted-world` | 0747215545 |
| The Moral Animal | Robert Wright | `the-moral-animal` | 0679407731 |
| The Perennial Philosophy | Aldous Huxley | `the-perennial-philosophy` | 0701108126 |
| The Power of Full Engagement | Jim Loehr and Tony Schwartz | `the-power-of-full-engagement` | 0743271513 |
| The Psychology of Intelligence | Jean Piaget | `the-psychology-of-intelligence` | 0822602229 |
| The Social Animal | Elliot Aronson | `the-social-animal-aronson` | 071672166X |
| What Happened to You? | Bruce Perry | `what-happened-to-you` | 1529068479 |

---

## Cover found but rejected as unusable (5 books)

**What failed:** Step 5, the cover quality check. An image existed but was a placeholder, a blank, or under 400px on its long edge, so it was rejected rather than saved.

**The hand work:** same as above. What was on offer was too small or was a placeholder, so it was refused rather than saved and forgotten about.

| Book | Author | Slug | ISBN |
|---|---|---|---|
| Existentialism is a Humanism | Jean-Paul Sartre | `existentialism-is-a-humanism` | 0300115466 |
| Mind Over Mood | Dennis Greenberger | `mind-over-mood` | 1462520421 |
| People Skills | Robert Bolton | `people-skills-bolton` | 0136557619 |
| The Nature of Prejudice | Gordon W. Allport | `the-nature-of-prejudice` | 0201001780 |
| The Wisdom Books | Robert Alter | `the-wisdom-books` | 0393068129 |

---

## Cover saved, but low resolution (44 books)

**What failed:** Nothing failed. A usable cover was saved, but from Open Library at roughly 400 to 899px rather than from Apple Books at 900px and above.

**The hand work:** none is required. These are safe to publish. If a better cover is wanted later, the ISBN is already there to look it up with. Worth knowing why they are here: Apple Books either held no edition or the edition it held did not match the expected title and author, and a wrong cover is worse than a small one, so the check sent them back to Open Library.

| Book | Author | Slug | ISBN |
|---|---|---|---|
| A Game Free Life | Stephen Karpman | `a-game-free-life` | 0990586707 |
| ACT Made Simple | Russ Harris | `act-made-simple` | 1572247053 |
| Adult Children of Emotionally Immature Parents | Lindsay Gibson | `adult-children-of-emotionally-immature-parents` | 1648370357 |
| Anger | Thich Nhat Hanh | `anger` | 0712611819 |
| Anything You Want | Derek Sivers | `anything-you-want` | 1936719118 |
| Be Here Now | Ram Dass | `be-here-now` | 0517543052 |
| Becoming a Helper | Marianne Schneider Corey | `becoming-a-helper` | 0357366271 |
| Between Parent and Child | Haim Ginott | `between-parent-and-child` | 0380008211 |
| Bowling Alone | Robert Putnam | `bowling-alone-putnam` | 1508230595 |
| Buddha's Brain | Rick Hanson | `buddhas-brain-hanson` | 036932367X |
| Complex PTSD | Pete Walker | `complex-ptsd-walker` | 1492871842 |
| Doing CBT | David F. Tolin | `doing-cbt-david-tolin` | 1462527078 |
| Driven to Distraction | Edward Hallowell | `driven-to-distraction` | 0679421777 |
| Frames of Mind | Howard Gardner | `frames-of-mind` | 0465025080 |
| Get Out of Your Own Way | Mark Goulston | `get-out-of-your-own-way` | 0399519904 |
| Helping Skills | Clara E. Hill | `helping-skills` | 1433831376 |
| How to Live | Derek Sivers | `how-to-live` | 1991152302 |
| I Hear You | Michael S. Sorensen | `i-hear-you` | 0999104012 |
| It’s Not How Good You Are, It’s How Good You Want to Be | Paul Arden | `it-s-not-how-good-you-are-it-s-how-good-you-want-to-be` | 0714843377 |
| Memory Observed | Ulric Neisser | `memory-observed-neisser` | 0716713713 |
| Motivation and Personality | Abraham Maslow | `motivation-and-personality` | 0060442417 |
| My Voice Will Go With You | Sidney Rosen | `my-voice-will-go-with-you` | 0393301354 |
| On Duties (De Officiis) | Cicero | `duties` | 0674990331 |
| Parent Effectiveness Training | Thomas Gordon | `parent-effectiveness-training` | 0609806939 |
| Person-Centered Psychotherapies | David J. Cain | `person-centered-psychotherapies` | 1433807211 |
| Skills in Person-Centred Counselling | Janet Tolan | `skills-in-person-centred-counselling` | 1848600941 |
| Skills in Person-Centred Counselling & Psychotherapy | Janet Tolan | `skills-in-person-centred-counselling-psychotherapy` | 1848600941 |
| Still the Mind | Alan Watts | `still-the-mind` | 1577311183 |
| The Anxiety and Phobia Workbook | Edmund Bourne | `the-anxiety-and-phobia-workbook` | 1974810062 |
| The Art of War | Sun Tzu | `the-art-of-war` | 8476518072 |
| The Consolations of Philosophy | Alain de Botton | `the-consolations-of-philosophy` | 0786146400 |
| The Miracle of Mindfulness | Thich Nhat Hanh | `the-miracle-of-mindfulness` | 0807012394 |
| The Nurture Assumption | Judith Rich Harris | `the-nurture-assumption` | 0747548943 |
| The Paradox of Choice | Barry Schwartz | `the-paradox-of-choice` | 0060005688 |
| The Power of Vulnerability | Brené Brown | `the-power-of-vulnerability` | 1604078588 |
| The Skilled Helper | Gerard Egan | `the-skilled-helper` | 081850479X |
| The Slight Edge | Jeff Olson | `the-slight-edge-olson` | 0967285550 |
| The Stress-Proof Brain | Melanie Greenberg | `the-stress-proof-brain` | 1626252661 |
| The Tao Te Ching | Lao Tzu | `the-tao-te-ching` | 1250209064 |
| The Undiscovered Self | Carl Gustav Jung | `the-undiscovered-self` | 0415278392 |
| The Upward Spiral | Alex Korb | `the-upward-spiral` | 1626251207 |
| The Willpower Instinct | Kelly McGonigal | `the-willpower-instinct` | 1469000431 |
| Words That Work | Frank Luntz | `words-that-work` | 1401384889 |
| Working the Shadow Side | Gerard Egan | `working-the-shadow-side` | 0787900117 |

---

## The two dead Amazon URLs (2 books)

These two resolved to an ISBN, but the derived `amazon.com/dp/` address did not answer as a product page, so the cell was left blank rather than filled with a link that goes nowhere. Every other derived URL is either verified live or was unverifiable because Amazon refuses scripted requests; that is set out in the record.

| Book | Author | Slug | ISBN |
|---|---|---|---|
| Pushing to the Front | Orison Swett Marden | `pushing-front` | 1775413845 |
| The Light We Carry | Michelle Obama | `the-light-we-carry` | 0241998085 |

---

## One thing waiting on a ruling from you

The commission's column contract gives `cover_status` four permitted values: `ok`, `missing`, `low_quality`, `no_isbn`. The run wrote a fifth, `low_res`, on 44 rows, to mark a cover that is saved and usable but came from the smaller source. It is a real distinction and it is useful, but it is not in the contract and it is not mine to add, so it is recorded here rather than resolved. Either fold those 44 into `ok`, or register `low_res` as a fifth value in DSRD 2. One line back either way and the master is corrected in a minute.

*No em or en dashes in this file; checked before writing.*
