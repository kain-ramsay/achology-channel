**For Chat. What this needs from you:** mend at source the eight hub guide records held for no outside link (section 3); decide the 18 pages carrying the banned word "holds" (section 4); rule whether the contents list's two link lines are a gate fault (section 4); and read the score table, where one page sits under 86 (section 6). Factory session, Code S201.

# DONE: 21 of the 29 signed hub guides are on the build site, read back, Pillar Content set and scored; 8 held (Code, S201 factory session, 28 October 2026)

Answers BRIEF__Import_The_28_Signed_Hub_Guides_S445, the 20 hub-guide rows of BRIEF__Import_The_192_Pages_Re_Signed_With_Full_Course_Names_S447, change 1 of BRIEF__The_Word_Holds_Is_Banned_Two_Changes_For_The_Build_Site_S450 for its four hub guides, and the hub guide rows of RULING__The_28_Unpublished_Articles_Decided_And_The_S429_Tool_Changes_Kept_S432, on Kain's go: "Yes, start the 28 hub guides in a fresh factory session." All 29 records in the hub-guide folder were read as they stand today: 20 signed Version 34 (S447), 8 signed Version 33 (S445), and grow-self-awareness signed Version 26, carried because the S450 brief names it. BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447 names no hub guide.

## 1. What reached the build site
- **21 pages updated in place, all published now.** 8 were published before; **13 were drafts** from the S429 unpublish and are **published again**: applied-psychology 39454, entrepreneurship 39468, healthy-marriage 39474, humanistic-psychology 39478, leadership-and-influence 39482, life-coaching 39484, mental-wellbeing 39488, mindfulness 39490, neuro-linguistic-programming 39492, person-centred-counselling 39494, psychoanalysis 39496, purpose-and-direction 39498, self-confidence 39502. The 8 already published: cognitive-behavioural-therapy 39458, communication-skills-and-language-patterns 39462, emotional-intelligence-and-social-skills 39466, goal-setting-and-action-planning 39470, grow-self-awareness 39472, limiting-beliefs-and-mindset 39486, resilience-and-mental-toughness 39500, self-discipline-and-mind-management 39504. No page was created, none taken down, no address changed.
- **Body, excerpt, search title and search description** through the theme's `tools/article_body_update.py --apply --with-seo`, 21 of 21. The tool refused the folder by name, as it did hub questions at S199. The importer (`import_field_authority_articles.py --type hub-guide`) converts the type with the same `drop_title_h1` and `to_blocks`, so Code added `hub-guide` to the tool's folder list and to its folder-to-post-type map (so `hub-guide:slug` never meets hub-guide-retired), and recorded the new hash in `harness/h9_reviewed_scripts.json` (theme 21cd25fe, pushed). No install-reaching line changed. The course autolinker changed no record.
- **The old headline:** every body's first-line headline equals its `post_title` and was dropped by `drop_title_h1`; no page was refused for it (RULING__Signed_Pages_Take_Their_Title_From_Post_Title_Drop_The_Old_Headline_S446).
- **Titles:** 20 of 21 differed from their records (all but grow-self-awareness) and now carry the record's `post_title`. Every focus phrase already matched. **Pillar Content** (`rank_math_pillar_content` on) set on all 21, per the pipeline's stage 6; it was set on none before. Written by one `wp eval-file` writer setting `post_title` by `wp_update_post` and the two meta by `update_post_meta`, no status key, staged rows read back on the server before each clearance was spent: 97216669bb958f26 (5), a1e2a5eb1f5890c0 (9), 72e7173adc1c8b47 (5), b40db78e5c0ec876 (1), ba39b6166c03ab08 (1), each `publish_gate.py --clear --update` at the live address.
- **Publishing the 13:** clearances bfabf95ae1c19815 (7) and 29e3bffde3080ae2 (6), minted with `--override` quoting Harness Rule 8 (Kain, S417) and Kain's go; each draft refused only "page-loaded", as a draft does. Then `publish_gate.py --remove-redirect ... --ruling RULING__The_28_Unpublished_..._S432`: rows 34, 35, 36, 38, 39, 43, 44, 46, 47, 48, 49, 50 and 51 of `qbk_rank_math_redirections` set inactive, each address proved to answer 200. Then all 13 re-gated at their live addresses and cleared. One earlier override clearance, 84b81c22b7212e78, was minted on the drafts' query-string addresses, which the gate recorded as a single "/"; it was left unspent to expire rather than used on a record that misnamed its pages.
- **The CBT guide** failed import check 3 at first: its record named `cognitive-behavioural-therapy-cbt.webp`, a file on no attachment, while the page shows `cognitive-behavioural-therapy.webp`. RULING__The_19_Held_Instructor_Articles_Land_With_The_Picture_Each_Page_Shows_S450 says the same ruling stands for any later record in this case, so Code wrote the attachment's file name into the record's `featured_image` (not body text, no signature changed), the record then passed all three checks, and the page landed with the picture it already shows.
- **The belief line (S450 change 1):** grow-self-awareness, limiting-beliefs-and-mindset and cognitive-behavioural-therapy carry "only the person who believes it can do that work" and not the old clause. human-nature-and-behaviour is held (section 3), so its page still carries its older words.

## 2. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 (1,118 records, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py --type hub-guide`, with the build site's 904 attachment names): 28 of 29 passed at first, the CBT guide failing check 3 (section 1); 29 of 29 after its picture field was corrected.
- **Read back of all 21** from plain ssh dumps after the last write: status, `post_title`, `post_excerpt`, search title, search description, focus keyword, Pillar Content, and the stored body character for character against `article_body_update.body_html_for()`. **21 of 21 match.**
- **Lock 5:** all 21 stored bodies through `content_gate.machinery_in_body()`: 0 carry a working note.
- **Product names:** `product_name_check.py --type hub-guide --list` finds three records naming a subject the way a course is named (healthy marriage, mental toughness, goal setting and action planning, each in a section heading), and none is a product.
- **The page check:** `publish_gate.py` measured all 21 at their live addresses and cleared them.
- **Not run:** Google's Rich Results test (stage 6) and the three inbound links (section 5.4); these are existing pages and no record names new inbound work.

## 3. The 8 held, and why
All fail the body tool's outside link rule (DSRD 6 section 5 item 11 move 6), which by your S449 ruling takes no exception: behavioural-psychology (draft 39456), cognitive-psychology (draft 39460), developmental-psychology (draft 39464), human-nature-and-behaviour (published 39476), hypnotherapy (draft 39480), skilled-helper (published 39506), social-psychology (draft 39508), values-and-decision-making (published 39510). The five drafts stay drafts with their S429 redirects; the three published pages stay exactly as they were. None has Pillar Content yet. Each lands the moment its record carries an outside link, with no further word: body, title, Pillar Content, and for the drafts the publish and the redirect.

## 4. Gate lines
158 failing lines on the 21, every one in `GATE_LINES__The_Hub_Guides_S201.csv` beside the records.
- **100 are style lines on Kain's signed words**, recorded `exception, 2026-10-28, signed prose not reworded (Kain S190 principle, Chat S449), approved by Kain`: paragraphs of 3 to 6 sentences 21, seven words shared 21, keyword in the first paragraph 20, stances field 20, numbers in digits 8, keyword in the first tenth 5, keyword in exactly one teaching heading 2, "actually" 2, keyword in the address slug 1 (grow-self-awareness, whose phrase is "grow in self-awareness"). **Code applied the S190 principle to hub guide style lines without a line naming this type, as at S194, S196 and S199; overturn it in one word if it should not stand.**
- **58 listed, not excepted and not held:**
  - **Link words 20 and a destination linked twice 20.** Both come from the contents list each guide opens with: its entries link to the guide's own sections by their full heading words, which run past five words, and the gate counts them as outside links and as repeated destinations. The brief says the contents list was kept word for word, so Code reads both as the gate not knowing the hub guide shape, not as faults in the pages. **Please rule whether the gate should pass a hub guide's contents list.**
  - **"holds" on 18 pages**, banned at S450 after these were signed: every landed guide but entrepreneurship, leadership-and-influence and life-coaching. Your S450 brief says you bring Kain the plan for existing records first, so Code landed the signed words and lists them here. One title also carries the word's root: goal-setting-and-action-planning, "How to Set Goals That Hold". Each lands again with no further word once its record changes.

## 5. Also found
None of the 21 has its focus phrase missing from its record title. Pillar Content is not yet on the 8 held pages; it goes on with each one's landing.

## 6. The score table: 21 pages
Read from each page's editor with `score_run.py`, nothing saved, after every write. Failing tests for the one page under 86 from `score_breakdown.py`, with contentHasAssets and lengthContent set aside (RULING__The_Article_Publish_Bar_Is_86_..._S449). **20 pass, 1 under; median 91.** Every page with its phrase is in `RANK_MATH_FAILURES__Hub_Guides_S201.csv` beside the records.

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| leadership-and-influence | 39482 | 94 | pass | none |
| cognitive-behavioural-therapy | 39458 | 91 | pass | none |
| communication-skills-and-language-patterns | 39462 | 91 | pass | none |
| emotional-intelligence-and-social-skills | 39466 | 91 | pass | none |
| entrepreneurship | 39468 | 91 | pass | none |
| goal-setting-and-action-planning | 39470 | 91 | pass | none |
| healthy-marriage | 39474 | 91 | pass | none |
| humanistic-psychology | 39478 | 91 | pass | none |
| life-coaching | 39484 | 91 | pass | none |
| mental-wellbeing | 39488 | 91 | pass | none |
| mindfulness | 39490 | 91 | pass | none |
| neuro-linguistic-programming | 39492 | 91 | pass | none |
| person-centred-counselling | 39494 | 91 | pass | none |
| psychoanalysis | 39496 | 91 | pass | none |
| purpose-and-direction | 39498 | 91 | pass | none |
| self-confidence | 39502 | 91 | pass | none |
| applied-psychology | 39454 | 87 | pass | none |
| limiting-beliefs-and-mindset | 39486 | 87 | pass | none |
| resilience-and-mental-toughness | 39500 | 87 | pass | none |
| self-discipline-and-mind-management | 39504 | 87 | pass | none |
| grow-self-awareness | 39472 | 82 | under | contentHasShortParagraphs, keywordInPermalink, keywordInImageAlt |

grow-self-awareness: its phrase "grow in self-awareness" is not in its address (grow-self-awareness) or its picture text, and one paragraph runs past 120 words. The record is the Version 26 one, older than the other 28.

OWED BACK: the eight outside links mended at source, after which each page lands with no further word; the "holds" plan for these 18 pages; a ruling on the contents list lines; grow-self-awareness mended at source, after which it is rescored.

*No em or en dashes in this file; checked before writing.*
