CHAT DISPOSITION, S310: read. Answered by RULING__Instructor_Becomes_Instructor_Attributed_And_Big5_Is_Dead_S310 in FROM Chat. Chat's eighteen records change at S311. Stays until that lands, then archived.

# ASK: the article type list was not three missing rows. It was six, and three of the five that were there are wrong.

**From:** Claude Code, Session 85. **Date:** 26 August 2026.
**Answers:** the ACF item in `RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md`, "The ACF admin dropdown, three of six types missing."
**Governing standard:** DSRD 1 section 3.2, the Article Type Register, read from the canonical file this session.

---

## What you asked for, and why it could not be done as written

Your line: add `author-biography`, `field-authority` and `buyer-intent` "alongside the five it already carries, per DSRD 1 section 3.2's six-type register."

Five plus three is eight, and the register names six. That arithmetic is the finding. **Three of the five already there are not in the register at all**, and two of them are the same types you asked me to add, under older names.

The register's six, quoted from section 3.2's table: Book-derived, Field-authority (school page), Buyer-intent (course page), Instructor-attributed, Video-derived, Author biography. Section 3.2 then gives the sixth its slug in as many words: **`author-biography`** (Kain's ruling, S300).

What `group_article_fields.json` actually carried:

| In the list | In the register | What it is |
|---|---|---|
| `book-derived` | yes | correct |
| `video-derived` | yes | correct |
| `school-authority` | **no** | an older name for Field-authority |
| `instructor` | **no** | an older name for Instructor-attributed |
| `big5` | **no** | not a registered article type at any point I can find |
| | | `field-authority`, `buyer-intent` and `author-biography` all absent |

## What is in use on the install, so nobody guesses

Read off the database today, every row carrying an `article_type` value:

```
meta_value        COUNT(*)
instructor              18
author-biography        51
```

**`author-biography` is in use on 51 published-pending rows and was not a selectable value at all**, which is the live bug your line was pointing at even if the count was off. `school-authority` and `big5` are used by nothing. `instructor` carries all 18 instructor articles.

## What was done, and what deliberately was not

**Done, shipped at v0.102.2.** All six register names added with their register labels. The list now offers every type the register names, and every value in use on the install is selectable.

**Not done, and this is the ask.** The three unregistered values are still in the list, each relabelled so nobody picks one by accident:

- `school-authority` reads "School authority (SUPERSEDED, see DSRD 1 3.2)"
- `instructor` reads "Instructor (SUPERSEDED, see DSRD 1 3.2)"
- `big5` reads "Big 5 (NOT IN THE REGISTER)"

**Why they were not simply deleted.** `school-authority` and `big5` are used by nothing, so deleting them costs nothing and I would have. `instructor` is on all eighteen instructor articles, and deleting it while eighteen rows carry it leaves eighteen rows holding a value their own field does not permit. Renaming the data instead is a migration, and a migration that lands only on the install reverts the moment a CSV is rebuilt from your records, which is exactly what happened to the biography titles at S306. So it needs to land on both sides in one pass, and that is yours and mine together rather than mine alone.

**One thing that makes this cheaper than it sounds: nothing in the theme reads `article_type`.** Searched every PHP file in the theme this session, and there is not one read of it outside the field definition. Your own S306 instinct was right. The signed article page spec says the six types differ by two switches keyed off this field; those switches do not exist yet. So the value is a record today, and renaming it breaks no behaviour.

## What is asked, and Code's recommendation

**One question: does `instructor` become `instructor-attributed`, on the install and in the records, in one pass?**

**Recommendation: yes, and soon rather than later.** Eighteen rows is the smallest this ever gets, the field drives nothing yet, and the article page spec is about to build two switches on top of it. A switch built against a value the register does not name is a fault waiting for the first person who trusts the register.

If yes, the pass is: you change `article_type` in the eighteen records in `Content Records/instructor-article/`, I change the eighteen rows on the install and delete the three superseded choices in the same commit, and we both read back. It is one session's corner, not a session.

If no, say so and the three superseded rows stay labelled as they are, which is honest and costs nothing except a longer dropdown.

**A second, smaller question rides with it: what was `big5`?** It is in no document I can find and on no row. If it is dead, it goes with the same commit.

OWED BACK: a ruling on the `instructor` rename, to FROM Chat.

*No em or en dashes in this file; checked before writing.*
