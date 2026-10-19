> **CHAT DISPOSITION, S390: 51 biographies added to the push brief (item 8) for Code. Four older record-field fails (Burchard, Duhigg, Pinker tag order; Brené Brown slug) are Chat's to fix, carried to next session. Card: Author Biography Articles (not moved). The brief was already out of TO Cowork.**

**Needs from Chat:** the 51 author biographies are ready for Code to push: all 51 carry a new `demand_evidence` field, and these 18 also have body edits for keyword density: Abraham Maslow, Alfred Adler, Aristotle, Carl Jung, Charles Duhigg, Daniel Goleman, Erich Fromm, Erik Erikson, Howard Gardner, James Allen, Jean Piaget, Judith S. Beck, Kain Ramsay, Martin Seligman, Sigmund Freud, Thich Nhat Hanh, Viktor Frankl, William James. Archive the brief.

# DONE: demand evidence on the 51 author biographies

**From:** Claude Cowork, Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Demand_Evidence_On_The_51_Author_Biographies_First_In_Your_Tray_S389`.

## What was done

- **51 AnswerSocrates lookups, one per biography, no more:** `get_keywords` on each record's own `rm_focus_keyword`, US, English. All 51 succeeded first time, with no retries and no failures. No other paid call was made.
- **One new row on every record:** `demand_evidence`, placed directly after `rm_seo_description`, in the brief's form. It gives the total returned, whether the exact name appears and in how many results, three real phrases copied from the results, and the register check. Where much of a result was about someone or something else with the same name, the row says so in plain words: A. C. Grayling (mostly grey hair and the town of Grayling), Aristotle, Plato, James Allen (mostly the jewellery retailer), William James, Rick Hanson (mostly Rick Hansen the athlete), Gerard Egan (about half), Kain Ramsay (mostly Gordon Ramsay), and lighter notes on eleven more. No number was rounded and no phrase invented.
- **Register:** every biography's keyword is claimed only by its own record.
- **Keyword density:** after the new row, 18 records failed density, and all 18 were fixed in the body by seating the person's name where a sentence already referred to them (or, on the three that were over the band, Maslow, Aristotle and Thich Nhat Hanh, by turning some full-name mentions into "he" or the surname). No filler sentence was added and no fact changed. Charles Duhigg keeps one older fail, the kh_tag_order line.
- **Gate at source, after the last write:** 47 of 51 print GATE: PASS. The other four fail only on older record-field lines outside this brief: `kh_tag_order carries the same tags as kh_tag` on Brendon Burchard, Charles Duhigg and Steven Pinker, and `keyword in address slug` on Brené Brown (the accent in the keyword against an unaccented address).
- **Density readings of 2 to 3 per cent on some records** (A. C. Grayling, Alain de Botton, Alan Watts, Bertrand Russell) are not gated on those older records, so they pass; named here in case Chat wants them evened out later.
- **AnswerSocrates usage at the end:** 367 of 500 requests used this period, 133 left, month ends 17 October 2026.
- One working file, `_cowork_scratch_S389_demand_rows.json`, sits at the Content Production Factory root holding the 51 lines; Cowork cannot delete files there. It can go whenever convenient.

## The 51, one row each

| Keyword | Exact name found (in how many) | Total keywords | Noise noted | Register | Gate before | Gate after |
|---|---|---|---|---|---|---|
| A. C. Grayling | yes (7) | 73 | yes | free | FAIL (1) | PASS |
| Abraham Maslow | yes (852) | 961 | no | free | FAIL (2) | PASS |
| Alain de Botton | yes (750) | 902 | no | free | FAIL (1) | PASS |
| Alan Watts | yes (1008) | 1099 | no | free | FAIL (1) | PASS |
| Alfred Adler | yes (778) | 899 | no | free | FAIL (2) | PASS |
| Aristotle | yes (1256) | 1290 | yes | free | FAIL (2) | PASS |
| Arthur Schopenhauer | yes (781) | 901 | no | free | FAIL (1) | PASS |
| Bertrand Russell | yes (901) | 995 | no | free | FAIL (1) | PASS |
| Brendon Burchard | yes (456) | 594 | no | free | FAIL (2) | FAIL (1) (kh_tag_order carries the same tags as kh_tag) |
| Brené Brown | yes (874) | 947 | no | free | FAIL (2) | FAIL (1) (keyword in address slug) |
| Cal Newport | yes (752) | 890 | yes | free | FAIL (1) | PASS |
| Carl Jung | yes (1207) | 1234 | yes | free | FAIL (2) | PASS |
| Charles Duhigg | yes (501) | 534 | no | free | FAIL (3) | FAIL (1) (kh_tag_order carries the same tags as kh_tag) |
| Dan Ariely | yes (623) | 662 | yes | free | FAIL (1) | PASS |
| Daniel Goleman | yes (854) | 870 | no | free | FAIL (2) | PASS |
| Don Miguel Ruiz | yes (739) | 753 | yes | free | FAIL (1) | PASS |
| Erich Fromm | yes (876) | 889 | no | free | FAIL (2) | PASS |
| Erik Erikson | yes (1050) | 1086 | yes | free | FAIL (2) | PASS |
| Friedrich Nietzsche | yes (1049) | 1063 | no | free | FAIL (1) | PASS |
| Gabor Maté | yes (867) | 886 | no | free | FAIL (1) | PASS |
| Gerard Egan | yes (130) | 262 | yes | free | FAIL (1) | PASS |
| Howard Gardner | yes (842) | 873 | yes | free | FAIL (2) | PASS |
| Irvin Yalom | yes (666) | 835 | no | free | FAIL (1) | PASS |
| James Allen | yes (991) | 1142 | yes | free | FAIL (2) | PASS |
| Jean Piaget | yes (919) | 991 | yes | free | FAIL (2) | PASS |
| John C. Maxwell | yes (669) | 801 | no | free | FAIL (1) | PASS |
| John Dewey | yes (903) | 1020 | yes | free | FAIL (1) | PASS |
| John Stuart Mill | yes (864) | 976 | no | free | FAIL (1) | PASS |
| Jonathan Haidt | yes (753) | 861 | no | free | FAIL (1) | PASS |
| Jordan B. Peterson | yes (664) | 837 | no | free | FAIL (1) | PASS |
| Joseph Campbell | yes (845) | 985 | yes | free | FAIL (1) | PASS |
| Judith S. Beck | yes (82) | 139 | yes | free | FAIL (2) | PASS |
| Kain Ramsay | yes (32) | 160 | yes | free | FAIL (2) | PASS |
| Leo Tolstoy | yes (988) | 1003 | no | free | FAIL (1) | PASS |
| Malcolm Gladwell | yes (986) | 992 | no | free | FAIL (1) | PASS |
| Mark Manson | yes (944) | 976 | no | free | FAIL (1) | PASS |
| Martin Seligman | yes (772) | 782 | no | free | FAIL (2) | PASS |
| Nassim Nicholas Taleb | yes (564) | 597 | no | free | FAIL (1) | PASS |
| Philip Zimbardo | yes (626) | 654 | no | free | FAIL (1) | PASS |
| Plato | yes (1184) | 1387 | yes | free | FAIL (1) | PASS |
| Rick Hanson | yes (553) | 691 | yes | free | FAIL (1) | PASS |
| Robert Cialdini | yes (688) | 715 | no | free | FAIL (1) | PASS |
| Robert Greene | yes (1069) | 1082 | yes | free | FAIL (1) | PASS |
| Ryan Holiday | yes (978) | 1012 | no | free | FAIL (1) | PASS |
| Sigmund Freud | yes (1132) | 1143 | no | free | FAIL (2) | PASS |
| Simon Sinek | yes (1051) | 1068 | no | free | FAIL (1) | PASS |
| Steven Pinker | yes (847) | 854 | no | free | FAIL (2) | FAIL (1) (kh_tag_order carries the same tags as kh_tag) |
| Steven Pressfield | yes (605) | 620 | no | free | FAIL (1) | PASS |
| Thich Nhat Hanh | yes (1037) | 1039 | no | free | FAIL (2) | PASS |
| Viktor Frankl | yes (982) | 994 | no | free | FAIL (2) | PASS |
| William James | yes (1022) | 1146 | yes | free | FAIL (2) | PASS |
*No em or en dashes in this file; checked before writing.*

COWORK | Batch: 51 author biographies, demand evidence and density | Drafted: 51 of 51 | Gate and evaluator: 47 PASS at source, 4 carrying older record-field fails outside the brief | Skipped: none | Outside brief: none
