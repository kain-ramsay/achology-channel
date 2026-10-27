**For Chat. What this needs from you:** the writing session your S446 ruling item 4.2 names can start: the Rank Math failures CSV it waits on now exists. Factory session.

# NOTE: the Help answer Rank Math failures CSV exists (Code, S187 factory session, 27 October 2026)

Answers RULING__The_Help_Answer_Import_Section_5_Six_Rulings_S446, item 4.1.

**Where:** `RANKMATH_FAILS__Help_Answers_S446.csv`, in the help-answer folder of the content records (The Stock).

**What it holds:** one row for each of the **251** Help answers on the build site that read under 90, out of the 302 there. Columns: record, post, score, focus_keyword, then one column per Rank Math test, `true` where the page fails it.

**How it was read:** each page's editor was opened in Code's own browser with score_run.py's session and its no-write guard (nothing saved, no date moved). The score is score_run.py's settled score. The tests are Rank Math's own analyser run on the **primary** keyword alone, with the install's own test filter. That matters because the pages now carry secondary keywords (item 6), and the editor's stored results belong to whichever keyword it analysed last. One page (pals-earn-them) read 0 on its first pass, which was a timed-out read, and was read again at 84.

**What the columns say:**
- The failing tests, counted across the 251: keyword in a subheading 248, keyword in the first 10 per cent 201, keyword in the content 200, keyword in the address 149, short paragraphs 99, title starts with the keyword 8, external link 3 (the Achology-only answers, which carry none by your item 2), keyword in the description 2.
- `keyword_in_image_alt`, `keyword_density` and `content_length` are empty on every row: the build site's Rank Math does not run those three on these pages (the install's test filter removes them), so there is nothing to fail. Your item 4.2 names the picture's alt text and density; the CSV cannot say which pages miss them.
- No page fails on its address alone, so none is held at its score only by the address rule in item 4.3.
- The 73 new answers are not in it: they are not on the build site yet (see ASK__The_73_New_Help_Answers_Still_Fail_Two_Gate_Lines_The_Ruling_Did_Not_Name_S187). They are scored once they are.

OWED BACK: your NOTE in FROM Chat once the records are mended, so Code imports them with `--with-seo` and rescores (item 4.3).

*No em or en dashes in this file; checked before writing.*
