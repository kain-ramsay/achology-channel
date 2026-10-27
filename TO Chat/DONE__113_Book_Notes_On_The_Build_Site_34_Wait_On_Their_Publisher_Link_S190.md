**For Chat. What this needs from you:** read the score table and the findings in section 4; mend the 34 records at source (already your job by RULING__Gate_Lines_On_Signed_Words_..._S449); rule on the three pages in section 3. Factory session.

# DONE: 113 of the 147 signed book notes are on the build site; the 34 wait on their publisher link (Code, S190 factory session, 27 October 2026)

Answers BRIEF__Import_The_147_Signed_Book_Notes_S446 for 113 pages, with RULING__Kain_Lands_The_147_Book_Notes_S190 (Kain, in the sitting: "yes, please go ahead and do this claude") and RULING__Gate_Lines_On_Signed_Words_The_73_Help_Answers_The_147_Book_Notes_And_The_Five_Anxiety_Articles_S449, which confirms that reading. Every record was read as it stands today.

## 1. What reached the build site
- **113 book notes updated in place**, all still published; none created, none unpublished. Through the theme's `article_body_update.py --apply --with-seo`, after the theme deployed the S440 template at 0.707.637 (contents list and badge on "A Question That Deserves an Honest Answer"; the S190 theme queue line struck by that session).
- Body for all 113. Excerpt for all 113. Search title and description for the 33 records that carry `rm_seo_title` and `rm_seo_description`; the other 80 carry only `prod_rm_*` and the tool reads `rm_*`, so their stored search title and description were left as they were. The read back below found them already equal to the record's `prod_rm_*` values.
- No course link was written into any record by the autolinker this run; no record changed.

## 2. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 before the dry run and again before the landing (1,014 records, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py` with the build site's attachment file names): 146 of 147 pass all three. fierce-self-compassion fails check 3: its record names `fierce-self-compassion.jpg`, on no attachment; its page keeps the `self-compassion.jpg` cover it already shows, as your S449 ruling says.
- **The page check:** `article_body_update.py --verify` (publish_gate.rendered_faults) on a-liberated-mind: clean. Its served page carries the five headings, the practice block and Sources (as a list), and all five contents links resolve to an id in the body.
- **Read back of all 113** against their records (post_title, post_excerpt, search title, search description, focus keyword, the five headings in order, no old headline): **110 match.** Three do not, in section 3.
- **Content gate:** each page's lines that judge Kain's signed words are recorded as `exception, 2026-10-27, signed prose not reworded (Kain S190 sitting), approved by Kain`. Every line by record is in `GATE_LINES__The_147_Book_Notes_S190.csv` beside the records.
- **Lock 5:** LOCK5_PENDING

## 3. Three pages whose title or keyword on the build site is older than the record
The body tool writes neither, and the publishing wall refuses a hand `wp post update` without a clearance, so Code left them:
- free-will-sam-harris (33802): title "Free Will: Summary and Key Ideas" against the record's "Free Will by Sam Harris: Summary and Key Ideas"; focus keyword "Free Will" against "free will by sam harris".
- thinking-fast-and-slow (36559): title "Thinking Fast and Slow: Summary and Key Ideas" against "Thinking, Fast and Slow: Summary and Key Ideas".
- mans-search-for-meaning (10901): focus keyword "search for meaning" against "man's search for meaning".
**Ask:** may Code write these three through `publish_gate.py --clear` and the cleared update, or does a theme or Kain route take them?

## 4. Findings for Chat
- **71 records link their course to the full address `https://achology.com/academy/...`** rather than `/academy/...`. On the build site Rank Math counts that as an outside link, so 56 pages fail "internal link" and lose points they would keep on achology.com. A record mend (the address without the host) or nothing until go-live; your call.
- **Three records link their course to a checkout address** (`community.achology.com/checkout/...`), boundaries-cloud among them.
- **The book note ceiling is 88**, as the theme queue's S103 line says (`contentHasAssets` scores 1 of 6 for a body with no picture): 34 pages reach it with no test failing.
- `rank_math_title` on the pages stores the title without " | Achology", as it did before this import; the served title is the same.

## 5. The title ruling (owed line)
On every book note landed this session the body's first-line headline was dropped and the page title is `post_title`; no page was refused for it.

## 6. The 34 not landed
Refused by the body tool, before any write, for no outside link (DSRD 6 section 5 item 11 move 6); have-a-little-faith also has no internal link. They land the moment their records change, with no further word: a-guide-to-rational-living, a-new-guide-to-rational-living, a-path-through-the-jungle, bittersweet, brainstorm-the-power-and-purpose-of-the-teenage-brain, coming-to-our-senses, creating-minds, critique-of-practical-reason, crucial-conversations-mcmillan, emotional-leonard-mlodinow, finding-flow, getting-past-no, have-a-little-faith, keeping-the-love-you-find, linchpin, maps-of-meaning, money-master-the-game, multiple-intelligences-new-horizons, nature-emerson, noise, originals, quit, shyness-what-it-is-what-to-do-about-it, stillness-speaks, talking-to-crazy, teacher-and-child, the-brains-way-of-healing, the-happiness-project, the-maine-woods, the-origins-of-intelligence-in-children, the-republic-plato, the-way-to-love, time-and-free-will, toward-a-psychology-of-being. Until then their pages keep the S150 bodies, whose fifth contents link now points at nothing on the new template.

## 7. Tools changed (committed and pushed; no rule loosened)
- Theme d8eaf70e: `tools/book_note_import.py` repointed and reading the S440 shape; its H9 entry re-hashed after reading the whole diff.
- Project aa0dfaa9 (Kain's S190 yes): `content_gate_standards.json` book note shape to S440; `content_gate_acceptance.py` change 2 turned to the S440 fifth (the same four cases fail as before); `stage5_import_checks.py` reads a book note's cover and leaves the foot out of the body shape.

## 8. The score table: 113 pages
Read from each page's editor with score_run.py's session under `block_every_write`, nothing saved, by Rank Math's own analyser on the primary keyword (its result manager's score). 0 at 90 or above (the ceiling is 88), 34 at 88, 79 under; median 82. Every page under 90, with its failing tests and primary keyword, is in `RANK_MATH_FAILURES__Book_Notes_S190.csv` beside the records, keyed by post id. Tests failing: internal link 56 (section 4), short paragraphs 38, keyword in subheadings 4, title starts with keyword 2, keyword in title 2, keyword in first 10% 2, keyword in image alt 1, keyword in content 1.

| Page (address name) | Post | Score |
|---|---|---|
| a-treatise-of-human-nature | 35932 | 88 |
| as-a-man-thinketh | 35934 | 88 |
| authentic-happiness-seligman | 36529 | 88 |
| awaken-the-giant-within | 36531 | 88 |
| awakenings | 33792 | 88 |
| before-happiness | 37026 | 88 |
| born-for-love | 38453 | 88 |
| chasing-the-scream | 33794 | 88 |
| coaching-with-the-brain-in-mind | 33795 | 88 |
| counseling-the-culturally-diverse | 36537 | 88 |
| daring-to-trust | 36289 | 88 |
| discipline-equals-freedom | 35946 | 88 |
| embracing-uncertainty | 37030 | 88 |
| emotional-intelligence-goleman | 35948 | 88 |
| feeling-good-burns | 35952 | 88 |
| free-will-sam-harris | 33802 | 88 |
| games-people-play | 35956 | 88 |
| how-to-know-a-person | 33807 | 88 |
| humble-inquiry | 33808 | 88 |
| internal-family-systems-therapy | 33809 | 88 |
| journey-to-the-heart | 33810 | 88 |
| leader-effectiveness-training | 37034 | 88 |
| make-your-bed | 35958 | 88 |
| mans-search-for-meaning | 10901 | 88 |
| mothers-who-cant-love | 38461 | 88 |
| necessary-endings | 37036 | 88 |
| on-the-origin-of-species | 33817 | 88 |
| open-when | 36295 | 88 |
| overcoming-depression | 33818 | 88 |
| radical-compassion | 33820 | 88 |
| recovering-from-emotionally-immature-parents | 33821 | 88 |
| the-diet-trap-solution | 33831 | 88 |
| the-farther-reaches-of-human-nature | 33833 | 88 |
| words-that-work | 35980 | 88 |
| fierce-self-compassion | 33800 | 86 |
| a-liberated-mind | 33790 | 85 |
| best-self-be-you-only-better | 35938 | 85 |
| childhood-and-society | 36533 | 85 |
| cognitive-behavior-therapy-second-edition | 35942 | 85 |
| come-together | 38455 | 85 |
| decisive | 33798 | 85 |
| difficult-conversations-patton | 36539 | 85 |
| extreme-ownership-willink | 35950 | 85 |
| frames-of-mind | 35954 | 85 |
| further-along-the-road-less-travelled | 37032 | 85 |
| homage-to-catalonia | 33804 | 85 |
| how-the-mighty-fall | 33805 | 85 |
| how-to-fix-a-broken-heart | 33806 | 85 |
| identity-youth-and-crisis | 36212 | 85 |
| meditations-for-mortals | 38459 | 85 |
| mental-efficiency | 33813 | 85 |
| notes-on-a-nervous-planet | 37038 | 85 |
| on-the-tranquility-of-mind | 38463 | 85 |
| peace-power-and-plenty | 33819 | 85 |
| the-beck-diet-solution | 36210 | 85 |
| the-honest-truth-about-dishonesty | 33836 | 85 |
| boundaries-cloud | 35940 | 82 |
| resilient | 36206 | 82 |
| running-on-empty-no-more | 37042 | 82 |
| speak-peace-in-a-world-of-conflict | 33822 | 82 |
| stoicism-and-the-art-of-happiness | 36541 | 82 |
| the-advantage | 36299 | 82 |
| the-advice-trap | 33826 | 82 |
| the-bridge-across-forever | 33828 | 82 |
| the-confidence-gap | 33829 | 82 |
| the-dichotomy-of-leadership | 33830 | 82 |
| the-high-5-habit | 37048 | 82 |
| the-history-of-philosophy | 35960 | 82 |
| the-jealousy-cure | 36303 | 82 |
| the-life-cycle-completed | 33837 | 82 |
| the-nicomachean-ethics | 35962 | 82 |
| the-open-society-and-its-enemies | 36545 | 82 |
| the-philosophy-of-freedom | 35966 | 82 |
| the-places-that-scare-you | 33839 | 82 |
| the-power-of-now | 36547 | 82 |
| the-power-of-truth | 33840 | 82 |
| the-prince-machiavelli | 35968 | 82 |
| the-problems-of-philosophy | 36549 | 82 |
| the-psychology-of-self-esteem | 33841 | 82 |
| the-road-less-travelled | 36553 | 82 |
| the-science-of-being-well | 33843 | 82 |
| the-selfish-gene | 35970 | 82 |
| the-stoic-challenge | 37050 | 82 |
| the-time-paradox | 36557 | 82 |
| the-upside-of-stress | 33844 | 82 |
| thinking-fast-and-slow | 36559 | 82 |
| thus-spoke-zarathustra | 35976 | 82 |
| truth-and-repair | 33848 | 82 |
| utilitarianism | 36561 | 82 |
| why-zebras-dont-get-ulcers | 33852 | 82 |
| words-that-change-minds | 35978 | 82 |
| yes-50-scientifically-proven-ways-to-be-persuasive | 36218 | 81 |
| shift | 37044 | 79 |
| surrounded-by-psychopaths | 37046 | 79 |
| the-8th-habit | 33825 | 79 |
| the-art-of-the-good-life | 36301 | 79 |
| the-doors-of-perception | 33832 | 79 |
| the-feeling-good-handbook | 33834 | 79 |
| the-gap-and-the-gain | 33835 | 79 |
| the-perennial-philosophy | 35964 | 79 |
| the-quick-and-easy-way-to-effective-speaking | 38467 | 79 |
| the-relationship-cure | 33842 | 79 |
| the-six-pillars-of-self-esteem | 36555 | 79 |
| the-skilled-helper | 35418 | 79 |
| the-tao-of-fully-feeling | 38529 | 79 |
| the-tao-te-ching | 35974 | 79 |
| the-ultimate-life-coaching-handbook | 35419 | 79 |
| thrift | 33845 | 79 |
| what-do-you-say-after-you-say-hello | 33850 | 79 |
| what-life-could-mean-to-you | 33851 | 79 |
| the-social-animal-aronson | 35972 | 72 |
| the-4-hour-body | 33824 | 36 |
| tusculan-disputations | 33849 | 33 |

OWED BACK: the ask in section 3; the 34 mended at source; your word on section 4's course address.

*No em or en dashes in this file; checked before writing.*
