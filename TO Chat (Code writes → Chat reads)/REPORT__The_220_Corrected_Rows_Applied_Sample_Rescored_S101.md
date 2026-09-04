# REPORT: the 220 corrected help answers are applied, 219 of them, sample re-scored

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `RULING_AND_ASK__Apply_The_220_Corrected_Help_Answers_S338.md`'s OWED BACK line.

---

## The update mechanism, named

`publish_gate.py`'s `--clear <urls> --update` route, exactly as proved on the pilot page this session. At 220-page scale the browser-driven measurement proved unreliable under concurrency: three attempts at 6 and then 3 workers each produced a different, spurious ~10-25 page refusal set (mostly a load-timing check), confirmed spurious by rechecking several of those exact pages alone and having them pass clean. A fourth run, concurrent first pass then a reliable one-at-a-time recheck of only what the first pass missed, cleared 219 of 220 pages. One page, `download-achology-community-app` (id 375), failed twice running and was left untouched.

## Applied

All 219 cleared rows: new keyword, SEO title, SEO description, corrected body, plus the ruled UKRLP line appended. Post 218 (the pilot) kept its hero image; the CSV's `new_body_html` for that one row was captured before the image landed, so the image was re-prepended rather than applied verbatim.

**One mistake, caught and fixed the same session:** Kain reworded the UKRLP line mid-session ("UK Provider Number UKRLP 10099815" instead of the S100 wording). The 219-row apply script still carried the old wording when it ran. Caught on the first post I read back to verify, fixed with a second, targeted pass across all 219, re-verified after.

## Sample re-score, read from the install

- 218 (pilot, keyword-corrected earlier, hero image, both UKRLP wordings tried): 73
- 222: 72
- 10057: 72
- 375 (the one left untouched): 9, unchanged, as expected

## The one page not applied, and why it is a real refusal, not noise

375 failed the same "dashes" check twice under completely different conditions (once mid-batch, once alone with nothing else running), which every other spurious refusal this session did not survive. Investigated properly: `wp post get 375` and its title carry no em or en dash anywhere, checked by direct character scan, not a pattern guess. The checker's own row says "0 em, 1 en", so the character is real and live on the rendered page, just not in this post's own fields; the page also fails `block-heading` on two section captions that are template chrome shared by every help page, which points at a related-post title or shared block rather than this post's own content. Not chased further, it is out of this batch's scope: 375 never had Cowork's correction applied and was correctly left alone rather than guessed at.

## Where the site stands now

219 of 250 help answers carry the corrected keyword, SEO fields, body and the UKRLP line. 30 were already keyword-clean from the mechanical fix and still need the UKRLP line, same as the 219 did before today. 375 needs its dash investigated before it can join either batch. The real category images are checked and ready, not yet placed on any page; that plus the remaining UKRLP rollout is this session's next job.

---

OWED BACK: nothing further on this batch. 375's dash and the 30-page UKRLP gap are named rather than silently carried.

*No em or en dashes in this file; checked before writing.*
