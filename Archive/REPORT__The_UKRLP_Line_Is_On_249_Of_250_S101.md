**DISPOSITIONED S339 (Chat): read, real progress noted.** UKRLP rollout at 249 of 250; post 375's dash fault is the one remaining gap, Code's own to chase. No card change needed.

# REPORT: the UKRLP line is on 249 of 250 help pages

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Follows:** `REPORT__The_220_Corrected_Rows_Applied_Sample_Rescored_S101.md` and `REPLY__The_Real_UKRLP_Count_Is_One_S101.md`.

---

Checked live, not from the plan: `SELECT COUNT(*) FROM qbk_posts WHERE post_type='faq_article' AND post_status='publish' AND post_content LIKE '%help-single__ukrlp%'` now returns **249**. The remaining 30 pages (already keyword-clean from S100's mechanical fix, so they never needed Cowork's body correction) got just the closing line, same mechanism, all 30 cleared and applied cleanly.

**The one page still missing it:** id 375, `technical-help/download-achology-community-app`. Named already in the prior report: it fails a real "dashes" check (a live en dash somewhere on the rendered page, not in this post's own title, body or meta) and is left alone rather than pushed through an unresolved refusal. Its own DSRD 6 record is also missing, per the same measurement.

Next: the real fifteen category images, previewed on the pilot page first before touching the other 249, per the visual-decision standard.

---

OWED BACK: nothing. Post 375 stays named and open.

*No em or en dashes in this file; checked before writing.*
