**For Code: do this now, in the session you are in with Kain. Signed by Kain at S405. One field on 51 records, nothing else.**

# BRIEF: push the 51 new author biography descriptions to the build site (S405)

**Why it matters now.** Kain found that the author biographies' search descriptions tied real people to Achology. Taleb's read "Explore his life, his major works, and his influence on Achology"; 31 of the 51 named Achology, 23 with "influence on Achology" or the like. That tells a reader those people worked with or shaped Achology, which is untrue, and the PRD bars overclaiming at launch. Kain is with you on the page templates now, so the pages he looks at should carry the corrected lines. He asked for this to go across straight away.

**What changed.** Cowork rewrote only the `rm_seo_description` field in all 51 records in `Content Records/author-biography/` to one frame Kain ruled at S405: "{Name} is {who they are}. Read about {his/her} life, {his/her} big ideas and the books {he/she} wrote." Her git diff shows 51 files, one line each, nothing else changed. Every line is at most 153 characters; the gate passes every description line. **One line was changed by Chat after Cowork's table, at S405:** Gerard Egan's now reads "Gerard Egan created the Skilled Helper model, a way of helping people through their problems. Read about his life, his big ideas and the books he wrote." (152 characters), because whether he is alive is unknown, so his line is written to be true either way. Push the record as it stands. Her full before and after table is `DONE__The_51_Author_Biography_Descriptions_Rewritten_To_One_Simple_Frame_S405` in FROM Cowork (Chat will archive it once you report).

**Kain's signature.** Kain asked for the push in session (S405), which Chat records as his signature on Cowork's table.

## The job

1. Commit the 51 changed records in the Content Production Factory.
2. Write each record's `rm_seo_description` to the matching post's Rank Math description on the build site. Touch no other field, no body, no status.
3. Read back each of the 51 from the build site and confirm it matches the record word for word.
4. Report in TO Chat: the count written, the count read back matching, and any that failed.

## Also, when you next touch the gate (not now)

Add a check that fails any title, description or excerpt that ties a named person to Achology ("influence on Achology", "draws on", "taught at Achology" and the like) on an author biography, so the pattern cannot pass again. Chat will confirm the wording with the gate brief that follows from S405.

*Signed by Kain Ramsay, S405, Tuesday 6 October 2026.*

*No em or en dashes in this file; checked before writing.*
