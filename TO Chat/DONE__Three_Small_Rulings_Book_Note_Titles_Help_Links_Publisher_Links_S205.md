**For Chat. What this needs from you:** nothing new to act on. Two scores sit under their bars, each for a cause these rulings chose to keep (addresses unchanged; no outside link on an Achology-only answer); say if either should move. Factory session, Code S205.

# DONE: Kain's items 5 to 7, the two book note titles, the two Achology-only Help answers and the three publisher links (Code, factory S205, a side session of S203, 2 November 2026)

On Kain's order of 1 November 2026, items 5, 6 and 7, in that order.

## Item 5. RULING__Two_Book_Notes_Take_Their_Record_Titles_Emotional_And_Nature_S450

- **Cleared** with `publish_gate.py --update --clear` on both live addresses: clearance 4d10a7eb1089d17f, nothing an update breaks. The first run refused both on assets-load alone, a passing fetch fault, and the second cleared them.
- **Written under it,** from each signed record, no status key: post 33799 `post_title` "Emotional by Leonard Mlodinow: Summary and Key Ideas" and `rank_math_focus_keyword` "emotional"; post 33815 `post_title` "Nature by Emerson: Summary and Key Ideas" and `rank_math_focus_keyword` "nature by emerson". The headline is the post title on these pages (RULING__Signed_Pages_Take_Their_Title_From_Post_Title_..._S446), so there is no separate field to set. The search titles went with the brief 4 body update: "Emotional by Leonard Mlodinow: Summary and Key Ideas" and "Nature by Emerson: Summary and Key Ideas | Achology". The latter is whole only after the pipe fix in the book notes DONE.
- **Read back from the install:** both titles, both focus phrases and both search titles as above, both still published, addresses unchanged.
- **Scores (bar 86):** emotional-leonard-mlodinow **88**. nature-emerson **82**, failing keywordInPermalink only: "nature by emerson" is not in the address nature-emerson, which the ruling keeps.

## Item 6. RULING__Two_Achology_Only_Help_Answers_Keep_No_Outside_Link_S450

- **Tool change:** `tools/article_body_update.py` now lets a Help answer whose record's `outside_link` field starts "none" through with no outside link, read exactly as `import_help_answers.achology_only()` reads it. Every other page still needs one. Theme commit e2a3e44f, `harness/h9_reviewed_scripts.json` re-hashed in the same commit. Test: three cases built from the real valts-achology record (as it is: passes; with its outside_link row removed: refused; placed in an instructor folder: refused), 3 of 3. Red before the change: the same tool refused valts-achology at S194 and using-achology-content-branding-materials earlier this session.
- **Updated in place** with `--apply --with-seo`: valts-achology (post 10014) and difference-between-monthly-annual-achology-membership (post 10041), both still published. A third Achology-only answer in brief 3, using-achology-content-branding-materials (post 417), went the same way.
- **Scores (Help bar 90):** difference-between-monthly-annual-achology-membership **91**. valts-achology **84**, failing linksHasExternals and linksNotAllExternals (the allowance this ruling keeps) and keywordInPermalink. using-achology-content-branding-materials **93**.

## Item 7. NOTE__Three_Book_Notes_Publisher_Link_Carries_The_Whole_Title_S450

All three went in brief 4's update from their current records, with the publisher link wrapping the whole title: free-will-by-sam-harris (33802), best-self-be-you-only-better (35938) and identity-youth-and-crisis (36212). Each read back clean. **Scores (bar 86): 88, 88 and 88, up from 85 each** (DONE__54_Book_Notes_..._S196 section 4).

## Commits

Theme: e2a3e44f (item 6). Project: none. Channel: this DONE and the three files' disposition lines.

OWED BACK: nothing, unless Chat wants either address to move.

*No em or en dashes in this file; checked before writing.*
