> **CHAT DISPOSITION, S329:** read; board pass run. Progress note written onto the Plugins & Site Configuration card's page body (the six live values, the ACF sync stamp lesson, the four unsynced groups, the lecture-transcript value still owed). Board cards moved: Plugins & Site Configuration (page body). Archived.

# REPORT: the article type choice list is live on the install, and S310 is closed

**From:** Claude Code, Session 092. **Date:** 1 September 2026. **Theme v0.132.1, deployed.**
**Closes:** `RULING__Instructor_Becomes_Instructor_Attributed_And_Big5_Is_Dead_S310.md` and its OWED BACK line.
**Also closes:** the ACF admin dropdown item in `RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md`, which named three of the six types as missing from the choice list.

---

## The count you asked for

| Value | Articles carrying it on the install |
|---|---|
| `instructor-attributed` | 18 |
| `author-biography` | 51 |

Read this turn off the install. Sixty nine articles, all accounted for, nothing carrying `instructor`, `school-authority` or `big5`.

**So the install half of your ruling had already landed** and I did not have to change eighteen rows. All eighteen were already `instructor-attributed` before I touched anything, including the three you are holding on Kain's keyphrase ruling. Their records on disk still read `instructor`, per your own S316 batch note, so that half is still yours and Cowork's.

## The three superseded choices are deleted, and why it needed more than deleting them

The choices are now the six DSRD 1 section 3.2 names, read back off the install after the change:

`book-derived`, `field-authority`, `buyer-intent`, `instructor-attributed`, `video-derived`, `author-biography`.

**The list had already been corrected in the theme, and ACF had never taken it.** The theme's `acf-json/group_article_fields.json` has carried the correct six for some time. The install's own copy of the group carried the old five: book-derived, school-authority, big5, instructor, video-derived.

**Why the theme file was not winning.** ACF prefers the database copy of a field group and offers a sync only when the local JSON's `modified` stamp is newer. Both stamps read `1784000000`, identical to the character. So ACF saw no change, offered no sync, and the correction sat in the theme where nobody could see it fail. Whoever corrected the choices changed them without moving the stamp.

**What was live, and it could have lost a value.** All eighteen instructor articles carried `article_type: instructor-attributed`, a value the live dropdown did not offer, on a field marked required with null not allowed. An editor opening one of those articles in the admin and pressing Update could have blanked the field. Nothing would have said so.

## What I changed, and what I deliberately did not

**Changed: one number.** The JSON's `modified` stamp moved to now, the theme shipped at v0.132.1 with three deploy proofs, and the group was synced to the install with `wp acf json sync --key=group_article_fields`. **No choice value was edited in this change set**, because the list on disk was already right.

**Not changed: the other four field groups.** `wp acf json status` reported five of six groups pending. The other four (about videos, book note, review, workbook) live only in the theme's JSON with no database row, which is a working state rather than a fault, and syncing them would have created database copies of four groups nobody asked me to touch. Scoped the sync to the one key instead.

**Read back after the sync**: the five field rows keep their original IDs, so no key moved, and the eighteen and fifty one counts above were taken after the sync, not before.

## One thing for your eye, and it is the general lesson

**A theme file that has been corrected is not the same as a correction that landed.** This one was correct on disk, in git, and in the register, and wrong on the site, for as long as the stamp sat still. It is the same shape as the S082 biography titles reverting at the next CSV rebuild: the record and the thing the record describes moved apart, and nothing was watching the gap.

Worth knowing when the workbook group is next edited: it has no database row today, so a JSON edit reaches the site immediately. The moment it is ever synced, it acquires the same stamp discipline.

OWED BACK: nothing. This closes S310 on both of its Code items.

*No em or en dashes in this file; checked before writing.*
