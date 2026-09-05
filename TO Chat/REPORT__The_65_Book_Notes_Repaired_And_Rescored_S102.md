# REPORT: the 65 live book notes repaired and re-scored. 64 read 85, one reads 79, from a median of 20.

**From:** Claude Code, Session 102. **Date:** 5 September 2026, about 15:40 BST.
**On:** `RULING__Kain_Orders_The_Book_Note_Rank_Math_Repair_Now_S102.md`, Kain's order in the sitting. Closes the "what's still needed" section of Cowork's `Batch_Report__65_Live_Book_Notes_Keyword_Fix_S338.md`.
**Board cards:** Book Notes, the psychologist expansion; Page readiness records.
**Every number below was read off the install this afternoon**, before and after, by `score_run.py` in its own driven browser, which saves nothing; the per-test figures by `score_breakdown.py`. The 65 rows are appended to the score table the gate reads (`~/.claude/achology_rank_math_scores.tsv`, note "S102 book note repair").

## What was wrong, measured

The focus keyword stored on every live page was "{book title} book summary" and that phrase appeared nowhere on the page, so every keyword test scored nothing (the one-page breakdown: title 0 of 36, description 0 of 2, address 0 of 5, opening 0 of 3, density 0 of 3, headings 0 of 3, alt 0 of 2, title start 0 of 3). Cowork's S338 pass had corrected all 65 records (keyword trimmed to the book title, the phrase written into the opening, one external link each), and the corrections had never reached the site, for two reasons in Code's own tools: the master's rule that a record never overwrites an approved value kept the master's junk keyword columns; and the importer's field reader kept the markdown escape on a pipe, which is how 18 live titles read "Book Notes \ Achology". 23 titles ran over 60 characters.

## What was done, in order

1. `tools/book_note_import.py`: the field reader now strips the table escape from a pipe; `--slugs FILE` names the pages a run is about (the S310 agreed list mis-names one live page and predates another); `--write --overwrite-columns col,col` lets a run name the master columns a record's value may replace, so the protective default stays. Read in full and re-hashed in the H9 register. Theme commit `bf04047`.
2. 22 record titles brought inside 60 characters by dropping the author clause, the pattern the other 43 already carried (record commit `6b851ea`). Nothing else in any record moved.
3. `--write` over the 65 live slugs with the three Rank Math columns named: master backed up (`Book_Note_Master__pre_S086_ingest_2026-09-05_1.xlsx`), 65 rows updated, upload sheet regenerated (680 rows).
4. The update clearance: all 65 pages measured by `publish_gate.py --update` with Kain's words as the override, **65 cleared, 0 refused**, id `b227e8106dff46f5`; the rows every page carried into the update (breadcrumb geometry, boundary owner, block heading, acronyms) are written on the clearance as its "before".
5. `--push` under that clearance: **65 updated, 0 created, 0 failed**; `--verify`: 65 of 65 on the site, 65 published. Read off the install afterwards: 0 titles over 60, 0 with a backslash, 0 keywords saying "book summary".
6. Re-scored: **64 pages at 85, one at 79.** Before: 61 at 20, one each at 4, 13, 22 and 76.

## The one-page breakdown after the repair (`a-guide-to-rational-living`, 33788)

Every keyword test now earns its full marks: title 36, title start 3, description 2, address 5, opening 3, density 3, headings 3, internal links 5, external links 4, short paragraphs 3. Three tests still earn less than they could, on every page:

| Test | Earns | Could earn | Why, and whose |
|---|---|---|---|
| contentHasAssets | 0 | 6 | the analyser sees no picture in the content it is fed; the cover is drawn by the template outside the reading column, so the theme's analyser feed would have to include it, Code's, a theme edit |
| keywordInImageAlt | 0 | 2 | the cover's alt text on the install does not carry the keyword; the records carry a corrected alt in `prod_cover_image_alt` (Cowork, S338) but the importer carries that field nowhere, Code's, one map entry and a re-push |
| lengthContent | 3 | 8 | Rank Math's 8 wants 2,500 words and a book note's own band is about 1,100; accepted as the type's shape, DSRD 2 |

**The one page at 79**, `the-bridge-across-forever` (33828), also earns 0 of 5 on internal links: its record carries no link to another Achology page. Cowork's, one line in the record.

**On the bar.** DSRD 6 section 5 item 11 asks 90. With the picture tests earned the type would read about 93; without them 85 is the most a book note can show, and that is where 64 of 65 now sit. The two picture fixes above are the whole distance to the bar, and both are Code's tooling and theme work, named here as the next step rather than started under this ruling.

## The titles, and the one thing not done

Every title now reads "{Book}: Book Notes | Achology" or "{Book} by {Author}: Book Notes | Achology" where that fits in 60. Kain called the titles poor as well as the scores; a new pattern is wording, so it was put to him in the sitting as one yes or no ("{Book}: Summary and Key Ideas | Achology", the suffix dropped where the name is long, 57 of 65 fit as is). Not applied. Two wrinkles for when he answers: eight books have names so long that even the bare pattern passes 60 and need a shorter form each; five keywords carry the author's name because the plain title collides (`free will sam harris`, `emotional leonard mlodinow` and three more), so their titles have to open with that exact phrase or lose the 36 points again, which is a keyword decision for the register before it is a title.

## The table

| Page | Keyword now | Before | After |
|---|---|---|---|
| a-guide-to-rational-living | a guide to rational living | 20 | 85 |
| a-liberated-mind | a liberated mind | 20 | 85 |
| a-way-of-being | a way of being | 20 | 85 |
| awakenings | awakenings | 20 | 85 |
| brainstorm-the-power-and-purpose-of-the-teenage-brain | brainstorm | 20 | 85 |
| chasing-the-scream | chasing the scream | 20 | 85 |
| coaching-with-the-brain-in-mind | coaching with the brain in mind | 20 | 85 |
| coming-to-our-senses | coming to our senses | 20 | 85 |
| creating-minds | creating minds | 20 | 85 |
| decisive | decisive | 20 | 85 |
| emotional-leonard-mlodinow | emotional leonard mlodinow | 13 | 85 |
| fierce-self-compassion | fierce self-compassion | 20 | 85 |
| finding-flow | finding flow | 20 | 85 |
| free-will-sam-harris | free will sam harris | 20 | 85 |
| getting-past-no | getting past no | 20 | 85 |
| homage-to-catalonia | homage to catalonia | 20 | 85 |
| how-the-mighty-fall | how the mighty fall | 20 | 85 |
| how-to-fix-a-broken-heart | how to fix a broken heart | 20 | 85 |
| how-to-know-a-person | how to know a person | 20 | 85 |
| humble-inquiry | humble inquiry | 20 | 85 |
| internal-family-systems-therapy | internal family systems therapy | 20 | 85 |
| journey-to-the-heart | journey to the heart | 20 | 85 |
| linchpin | linchpin | 20 | 85 |
| mans-search-for-meaning | search for meaning | 4 | 85 |
| maps-of-meaning | maps of meaning | 20 | 85 |
| mental-efficiency | mental efficiency | 20 | 85 |
| money-master-the-game | money: master the game | 20 | 85 |
| nature-emerson | nature emerson | 20 | 85 |
| noise | noise | 20 | 85 |
| on-the-origin-of-species | on the origin of species | 20 | 85 |
| overcoming-depression | overcoming depression | 20 | 85 |
| peace-power-and-plenty | peace, power and plenty | 20 | 85 |
| radical-compassion | radical compassion | 20 | 85 |
| recovering-from-emotionally-immature-parents | recovering from emotionally immature parents | 20 | 85 |
| speak-peace-in-a-world-of-conflict | speak peace in a world of conflict | 20 | 85 |
| stillness-speaks | stillness speaks | 20 | 85 |
| the-4-hour-body | the 4-hour body | 20 | 85 |
| the-8th-habit | the 8th habit | 20 | 85 |
| the-advice-trap | the advice trap | 20 | 85 |
| the-brains-way-of-healing | the brain's way of healing | 20 | 85 |
| the-bridge-across-forever | the bridge across forever | 76 | 79 |
| the-confidence-gap | the confidence gap | 20 | 85 |
| the-dichotomy-of-leadership | the dichotomy of leadership | 20 | 85 |
| the-diet-trap-solution | the diet trap solution | 20 | 85 |
| the-doors-of-perception | the doors of perception | 20 | 85 |
| the-farther-reaches-of-human-nature | the farther reaches of human nature | 20 | 85 |
| the-feeling-good-handbook | the feeling good handbook | 20 | 85 |
| the-gap-and-the-gain | the gap and the gain | 20 | 85 |
| the-honest-truth-about-dishonesty | the honest truth about dishonesty | 20 | 85 |
| the-life-cycle-completed | the life cycle completed | 20 | 85 |
| the-maine-woods | the maine woods | 20 | 85 |
| the-places-that-scare-you | the places that scare you | 20 | 85 |
| the-power-of-truth | the power of truth | 22 | 85 |
| the-psychology-of-self-esteem | the psychology of self-esteem | 20 | 85 |
| the-relationship-cure | the relationship cure | 20 | 85 |
| the-science-of-being-well | the science of being well | 20 | 85 |
| the-upside-of-stress | the upside of stress | 20 | 85 |
| thrift | thrift | 20 | 85 |
| time-and-free-will | time and free will | 20 | 85 |
| toward-a-psychology-of-being | toward a psychology of being | 20 | 85 |
| truth-and-repair | truth and repair | 20 | 85 |
| tusculan-disputations | tusculan disputations | 20 | 85 |
| what-do-you-say-after-you-say-hello | what do you say after you say hello | 20 | 85 |
| what-life-could-mean-to-you | what life could mean to you | 20 | 85 |
| why-zebras-dont-get-ulcers | why zebras don't get ulcers | 20 | 85 |

OWED BACK: from Kain, the yes or no on the title pattern; from Cowork, the internal link in `the-bridge-across-forever`; from Code, the cover alt carried to the attachment and the analyser feed carrying the cover, both named on the theme queue when the sitting closes.

*No em or en dashes in this file; checked before writing.*
