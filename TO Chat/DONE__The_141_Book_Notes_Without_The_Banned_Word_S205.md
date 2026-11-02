**For Chat. What this needs from you:** one mend at source on three held book notes. a-way-of-being, atomic-habits-clear and civilization-and-its-discontents still head their fifth section "What Might Your Next Learning Steps Be?". The ruled fifth heading is "A Question That Deserves an Honest Answer", and with the old one the body tool's book note reader drops that section, its links and everything after it (section 2). Factory session, Code S205.

# DONE: 138 of the 141 book notes without the banned word are on the build site; 3 held (Code, factory S205, a side session of S203, 2 November 2026)

Answers BRIEF__Update_The_141_Book_Notes_Without_The_Banned_Word_S450, on Kain's order of 1 November 2026. Route followed: TO Chat/DONE__54_Book_Notes_Updated_Mended_And_Rescored_S196 (`article_body_update.py book-note:<slug> --apply --with-seo`).

## 1. The import checks

- **Fields complete and signed.** Read against the book-note standard's 25 required fields: 141 of 141 complete. 137 carry the banned word signature. Four (atomic-habits-clear, civilization-and-its-discontents, the-ultimate-life-coaching-handbook, yes-50-scientifically-proven-ways-to-be-persuasive) carry Kain's later signature of 2 November for BRIEF__Update_15_Pages_Resisting_Change_Links_Two_Quote_Articles_Three_Book_Notes_S451, written on top of this batch. So they were sent as they stand, never an earlier copy.
- **Body shape.** `body_guard.py --signed`: 0 working notes. **A new check, added here because the tool would not have caught it:** every link and section heading between each record's Body and End of body lines must reach the converted page. 138 of 141 pass. 3 fail (section 2).
- **Every link resolves.** 66 site addresses: the published ones resolve. The course pages under /academy/ answer 404 (pages not yet built). 16 links point at articles not yet on the build site, for example /learn/psychology/articles/know-thyself/. These links are unchanged by this batch and already on the pages, so they are pages to come. Of 160 outside links, 124 answer below 400. 33 are publisher sites that refuse scripts (HarperCollins, Macmillan, Simon and Schuster, Shambhala, Sage, Bloomsbury and others). One is a host that did not connect (puddledancer.com). **Three Penguin Random House ISBN pages answer 404:** penguinrandomhouse.com/isbn/9781401962128, /9780609809532 and /9780307463630. They are unchanged by this batch; worth a look at source.

## 2. Held: three records on the old fifth heading

a-way-of-being, atomic-habits-clear and civilization-and-its-discontents. Each heads its fifth section "What Might Your Next Learning Steps Be?". The book note reader (`book_note_import.py`, LOCKED_HEADINGS) keeps only the five ruled headings, whose fifth is "A Question That Deserves an Honest Answer". So for these three it silently drops that section, its course link and outside link, and the practice and Sources blocks after it. The tool refused a-way-of-being and civilization-and-its-discontents for the links they lost, but would have sent atomic-habits-clear, which keeps enough links elsewhere. None of the three was sent. Their build site pages are unchanged. Two of them are also in the S451 15 pages brief, so the mend lands both briefs at once. **Needed: the fifth section rewritten to the ruled heading and shape, at source.**

## 3. Landed, 138

- `article_body_update.py book-note:<slug> --apply --with-seo`: 138 of 138 sent, each with its body, excerpt, search title and search description. 0 refused, 0 failed. All stay published.
- **Two tool mends were needed first, both in theme commits with their H9 hash and tests, nothing deployed.**
  - (e2a3e44f) `--with-seo` read only `rm_seo_*`, and 102 of these records carry only `prod_rm_*` (the S196 gap). It now reads `rm_*`, else `prod_rm_*`. The 39 records carrying both carry the same value.
  - (bf809494) 57 records write their search title "X: Summary and Key Ideas \| Achology", and the shared field reader cut the cell at that pipe. The first run sent 29 pages with "| Achology" missing before Code saw it and stopped it (a-guide-to-rational-living to embracing-uncertainty, about two minutes). The tool now reads an escaped pipe's cell whole (proved: 2,479 rows read as before, the 66 rows with an escaped pipe kept whole, 0 otherwise). All 138 were then sent again.
- **Read back.** `--verify`: 138 of 138 clean (6 needed a second read; the first read of those failed to load the page, a passing fault). Every page's rendered `<title>` and meta description were then fetched from inside the host and compared with the record: **138 of 138 match**, "| Achology" included.
- **The banned word.** WordPress's own search across every published book note for "holds" finds four. civilization-and-its-discontents is held (section 2). the-tao-of-fully-feeling, quit and thrift match only "households", which the plan keeps. So no updated book note shows the word.
- **critique-of-practical-reason** carries the corrected fact (1785 to 1788, three years). It went with the rest from its record.
- **Item 7's three, landed here:** free-will-by-sam-harris, best-self-be-you-only-better and identity-youth-and-crisis, with the publisher link carrying the whole title. Each moves from 85 to 88; their line is in the item 5 to 7 DONE.
- No record was changed by the run.

## 4. Scores (bar 86), read by `score_run.py`, nothing saved

**138 of 138 at 86 or more: 136 at 88, 2 at 86** (fierce-self-compassion and mans-search-for-meaning). Failing tests were not read, since none is under the bar. yes-50-scientifically-proven-ways-to-be-persuasive is at 88, up from 81, with the S451 opening link.

| Page (address name) | Post | Focus phrase (as Rank Math reads it) | Score | Against 86 |
|---|---|---|---|---|
| a-guide-to-rational-living | 33788 | a guide to rational living | 88 | pass |
| a-liberated-mind | 33790 | a liberated mind | 88 | pass |
| a-new-guide-to-rational-living | 38527 | a new guide to rational living | 88 | pass |
| a-path-through-the-jungle | 36287 | A Path through the Jungle | 88 | pass |
| a-treatise-of-human-nature | 35932 | a treatise of human nature | 88 | pass |
| as-a-man-thinketh | 35934 | as a man thinketh | 88 | pass |
| awakenings | 33792 | awakenings | 88 | pass |
| before-happiness | 37026 | Before Happiness | 88 | pass |
| best-self-be-you-only-better | 35938 | best self be you only better | 88 | pass |
| bittersweet | 37028 | Bittersweet | 88 | pass |
| born-for-love | 38453 | Born for Love | 88 | pass |
| boundaries-cloud | 35940 | boundaries | 88 | pass |
| brainstorm-the-power-and-purpose-of-the-teenage-brain | 33793 | brainstorm | 88 | pass |
| chasing-the-scream | 33794 | chasing the scream | 88 | pass |
| childhood-and-society | 36533 | childhood and society | 88 | pass |
| coaching-with-the-brain-in-mind | 33795 | coaching with the brain in mind | 88 | pass |
| cognitive-behavior-therapy-second-edition | 35942 | cognitive behavior therapy | 88 | pass |
| come-together | 38455 | Come Together | 88 | pass |
| coming-to-our-senses | 33796 | coming to our senses | 88 | pass |
| counseling-the-culturally-diverse | 36537 | counseling the culturally diverse | 88 | pass |
| creating-minds | 33797 | creating minds | 88 | pass |
| critique-of-practical-reason | 38457 | Critique of Practical Reason | 88 | pass |
| crucial-conversations-mcmillan | 35944 | crucial conversations | 88 | pass |
| daring-to-trust | 36289 | Daring to Trust | 88 | pass |
| decisive | 33798 | decisive | 88 | pass |
| difficult-conversations-patton | 36539 | difficult conversations | 88 | pass |
| discipline-equals-freedom | 35946 | discipline equals freedom | 88 | pass |
| embracing-uncertainty | 37030 | Embracing Uncertainty | 88 | pass |
| emotional-intelligence-goleman | 35948 | emotional intelligence | 88 | pass |
| emotional-leonard-mlodinow | 33799 | Emotional | 88 | pass |
| extreme-ownership-willink | 35950 | extreme ownership | 88 | pass |
| feeling-good-burns | 35952 | feeling good | 88 | pass |
| frames-of-mind | 35954 | frames of mind | 88 | pass |
| free-will-by-sam-harris | 33802 | free will by sam harris | 88 | pass |
| games-people-play | 35956 | games people play | 88 | pass |
| getting-past-no | 33803 | getting past no | 88 | pass |
| have-a-little-faith | 36291 | Have a Little Faith | 88 | pass |
| homage-to-catalonia | 33804 | homage to catalonia | 88 | pass |
| how-the-mighty-fall | 33805 | how the mighty fall | 88 | pass |
| how-to-fix-a-broken-heart | 33806 | how to fix a broken heart | 88 | pass |
| how-to-know-a-person | 33807 | how to know a person | 88 | pass |
| humble-inquiry | 33808 | humble inquiry | 88 | pass |
| identity-youth-and-crisis | 36212 | Identity: Youth and Crisis | 88 | pass |
| internal-family-systems-therapy | 33809 | internal family systems therapy | 88 | pass |
| journey-to-the-heart | 33810 | journey to the heart | 88 | pass |
| keeping-the-love-you-find | 36293 | Keeping the Love You Find | 88 | pass |
| leader-effectiveness-training | 37034 | Leader Effectiveness Training | 88 | pass |
| linchpin | 33811 | linchpin | 88 | pass |
| make-your-bed | 35958 | make your bed | 88 | pass |
| meditations-for-mortals | 38459 | Meditations for Mortals | 88 | pass |
| mental-efficiency | 33813 | mental efficiency | 88 | pass |
| money-master-the-game | 33814 | money: master the game | 88 | pass |
| mothers-who-cant-love | 38461 | Mothers Who Can't Love | 88 | pass |
| multiple-intelligences-new-horizons | 36214 | Multiple Intelligences | 88 | pass |
| nature-emerson | 33815 | Nature | 88 | pass |
| necessary-endings | 37036 | Necessary Endings | 88 | pass |
| noise | 33816 | noise | 88 | pass |
| notes-on-a-nervous-planet | 37038 | Notes on a Nervous Planet | 88 | pass |
| on-the-origin-of-species | 33817 | on the origin of species | 88 | pass |
| on-the-tranquility-of-mind | 38463 | On the Tranquility of Mind | 88 | pass |
| open-when | 36295 | Open When | 88 | pass |
| originals | 38465 | Originals | 88 | pass |
| overcoming-depression | 33818 | overcoming depression | 88 | pass |
| peace-power-and-plenty | 33819 | peace, power and plenty | 88 | pass |
| quit | 37040 | Quit | 88 | pass |
| radical-compassion | 33820 | radical compassion | 88 | pass |
| recovering-from-emotionally-immature-parents | 33821 | recovering from emotionally immature parents | 88 | pass |
| resilient | 36206 | Resilient | 88 | pass |
| running-on-empty-no-more | 37042 | Running on Empty No More | 88 | pass |
| shift | 37044 | Shift | 88 | pass |
| shyness-what-it-is-what-to-do-about-it | 36208 | Shyness | 88 | pass |
| speak-peace-in-a-world-of-conflict | 33822 | speak peace in a world of conflict | 88 | pass |
| stillness-speaks | 33823 | stillness speaks | 88 | pass |
| stoicism-and-the-art-of-happiness | 36541 | stoicism and the art of happiness | 88 | pass |
| surrounded-by-psychopaths | 37046 | Surrounded by Psychopaths | 88 | pass |
| talking-to-crazy | 38451 | Talking to Crazy | 88 | pass |
| teacher-and-child | 36297 | Teacher and Child | 88 | pass |
| the-4-hour-body | 33824 | the 4-hour body | 88 | pass |
| the-8th-habit | 33825 | the 8th habit | 88 | pass |
| the-advantage | 36299 | The Advantage | 88 | pass |
| the-advice-trap | 33826 | the advice trap | 88 | pass |
| the-art-of-the-good-life | 36301 | The Art of the Good Life | 88 | pass |
| the-beck-diet-solution | 36210 | The Beck Diet Solution | 88 | pass |
| the-brains-way-of-healing | 33827 | the brain's way of healing | 88 | pass |
| the-bridge-across-forever | 33828 | the bridge across forever | 88 | pass |
| the-confidence-gap | 33829 | the confidence gap | 88 | pass |
| the-dichotomy-of-leadership | 33830 | the dichotomy of leadership | 88 | pass |
| the-diet-trap-solution | 33831 | the diet trap solution | 88 | pass |
| the-doors-of-perception | 33832 | the doors of perception | 88 | pass |
| the-farther-reaches-of-human-nature | 33833 | the farther reaches of human nature | 88 | pass |
| the-feeling-good-handbook | 33834 | the feeling good handbook | 88 | pass |
| the-happiness-project | 36543 | The Happiness Project | 88 | pass |
| the-high-5-habit | 37048 | The High 5 Habit | 88 | pass |
| the-history-of-philosophy | 35960 | the history of philosophy | 88 | pass |
| the-honest-truth-about-dishonesty | 33836 | the honest truth about dishonesty | 88 | pass |
| the-jealousy-cure | 36303 | The Jealousy Cure | 88 | pass |
| the-life-cycle-completed | 33837 | the life cycle completed | 88 | pass |
| the-maine-woods | 33838 | the maine woods | 88 | pass |
| the-nicomachean-ethics | 35962 | the nicomachean ethics | 88 | pass |
| the-open-society-and-its-enemies | 36545 | the open society and its enemies | 88 | pass |
| the-origins-of-intelligence-in-children | 36216 | The Origins of Intelligence in Children | 88 | pass |
| the-perennial-philosophy | 35964 | the perennial philosophy | 88 | pass |
| the-places-that-scare-you | 33839 | the places that scare you | 88 | pass |
| the-power-of-now | 36547 | the power of now | 88 | pass |
| the-power-of-truth | 33840 | the power of truth | 88 | pass |
| the-prince-machiavelli | 35968 | the prince | 88 | pass |
| the-problems-of-philosophy | 36549 | the problems of philosophy | 88 | pass |
| the-psychology-of-self-esteem | 33841 | the psychology of self-esteem | 88 | pass |
| the-quick-and-easy-way-to-effective-speaking | 38467 | The Quick and Easy Way to Effective Speaking | 88 | pass |
| the-relationship-cure | 33842 | the relationship cure | 88 | pass |
| the-republic-plato | 36551 | the republic | 88 | pass |
| the-road-less-travelled | 36553 | the road less travelled | 88 | pass |
| the-science-of-being-well | 33843 | the science of being well | 88 | pass |
| the-selfish-gene | 35970 | the selfish gene | 88 | pass |
| the-six-pillars-of-self-esteem | 36555 | the six pillars of self-esteem | 88 | pass |
| the-skilled-helper | 35418 | the skilled helper | 88 | pass |
| the-social-animal-aronson | 35972 | the social animal | 88 | pass |
| the-stoic-challenge | 37050 | The Stoic Challenge | 88 | pass |
| the-tao-of-fully-feeling | 38529 | The Tao of Fully Feeling | 88 | pass |
| the-tao-te-ching | 35974 | the tao te ching | 88 | pass |
| the-time-paradox | 36557 | the time paradox | 88 | pass |
| the-ultimate-life-coaching-handbook | 35419 | the ultimate life coaching handbook | 88 | pass |
| the-upside-of-stress | 33844 | the upside of stress | 88 | pass |
| the-way-to-love | 37052 | The Way to Love | 88 | pass |
| thinking-fast-and-slow | 36559 | thinking fast and slow | 88 | pass |
| thrift | 33845 | thrift | 88 | pass |
| time-and-free-will | 33846 | time and free will | 88 | pass |
| toward-a-psychology-of-being | 33847 | toward a psychology of being | 88 | pass |
| truth-and-repair | 33848 | truth and repair | 88 | pass |
| tusculan-disputations | 33849 | tusculan disputations | 88 | pass |
| what-do-you-say-after-you-say-hello | 33850 | what do you say after you say hello | 88 | pass |
| what-life-could-mean-to-you | 33851 | what life could mean to you | 88 | pass |
| why-zebras-dont-get-ulcers | 33852 | why zebras don't get ulcers | 88 | pass |
| words-that-change-minds | 35978 | words that change minds | 88 | pass |
| words-that-work | 35980 | words that work | 88 | pass |
| yes-50-scientifically-proven-ways-to-be-persuasive | 36218 | Yes! 50 Scientifically Proven Ways to Be Persuasive | 88 | pass |
| fierce-self-compassion | 33800 | fierce self-compassion | 86 | pass |
| mans-search-for-meaning | 10901 | man's search for meaning | 86 | pass |

## Commits

Theme: e2a3e44f and bf809494 (the body tool and its H9 hash). Project: none. Channel: this DONE and the brief's disposition line.

OWED BACK: the three records' fifth section at source; then Code sends and rescores them.

*No em or en dashes in this file; checked before writing.*
