# RULING: Kain rules the WordPress author is filled in, and two things stand in the way

**From:** Claude Code, Session 105. **Date:** Monday 7 September 2026. **Session type:** factory.
**Filed under Harness Rule 14:** a ruling Kain gives in a Code session is authority at once, and is filed to TO Chat the same session so Chat writes it into the document that owns it.
**Board card:** the Knowledge Hub article set.
**Answers:** decision 2 of the standing five, "192 of 196 published articles have no WordPress author at all".

---

## 1. What was put to him, and what he said

He was told, in these terms: almost every article on the site has no author recorded in WordPress; readers see the right name because the byline comes from the record's pen name; the hidden record that search engines and AI systems read is empty on 192 of them; the proposal was to fill it in to match the name already printed on each page, with nothing on any page looking different.

**Kain, in this sitting, in his own words: "yes, please go ahead claude"**

**So the ruling is: the WordPress author is filled in to match the name already printed on the page.** It needs writing into the document that owns article authorship.

---

## 2. The ruling cannot be carried out as described, and this is measured rather than argued

Measured off the install this session. **196 published articles carry seven different pen names. The install has three WordPress users.**

| Pen name on the page | Published articles | A WordPress user exists |
|---|---|---|
| charlotte-j-avery | 84 | no |
| benjamin-lockwood | 60 | no |
| declan-fitzpatrick | 12 | no |
| karen-ramsay | 12 | **yes, user 3** |
| evelyn-montgomery | 11 | no |
| gerard-egan | 9 | no |
| kain-ramsay | 8 | **yes, user 2** |

The three users are Achology Admin, Kain Ramsay and Karen Ramsay. **So 176 of the 196 name a person the install has no account for.**

**Making those 176 match would mean creating five new WordPress user accounts, four of them for pen names rather than real people.** That is not what Kain approved, it is not a small thing, and creating accounts is not something Code does. It carries real consequences that are somebody's decision and not mine: author archive pages appearing at new addresses, accounts that can be logged into, an email address needed for each, and four fictional personas becoming user records that read as real people.

**So it goes back to him as its own question rather than riding in on this yes.** Named here so the ruling's record shows what it actually reaches.

**20 articles can be done exactly as he described**, the 8 under his own name and Karen's 12, because both already have an account and the hidden name would then agree with the printed one. Their ids were read off the install this turn and are held in this session's working file.

---

## 3. Even those 20 are refused by our own wall, and I have not gone round it

`H9`, the publishing wall, refuses `wp post update` on ground A, an explicit publishing verb, whatever field the update actually sets. Setting `post_author` on a page that is already published changes no status and publishes nothing, and the wall still refuses it, by design: its own words are "Unknown is a refusal on purpose".

**The route it offers does not fit either.** A clearance is minted by `publish_gate.py --clear` only where every page passes the machine third of DSRD 6 with no failing line. These very pages carry failing lines: chapter 2 fails on all of them on the trial panel's 36 word supporting line, and chapter 1 fails on several on the stray dash. So the gate would refuse to mint, correctly.

**I have not edited H9 and I will not.** Loosening a wall so my own work can pass is the exact failure the project has been burned by, and my standing instruction on this is explicit: where the machinery refuses approved work, record a waiver naming what it waits on, never a silent switch-off. **H9 has no waiver mechanism**, which is why this file is the record instead.

### What I think the answer is, for Chat to rule

**H9 already draws exactly the distinction that is missing here**, one line further down, for the status flag: "`--post_status=publish` is a marker only where it is SETTING a status. On `wp post list --post_status=publish` it is a filter."

The same shape applies to the verb. A `wp post update` that sets no status, on ids that are already published, is not a publish and cannot become one. **My recommendation: ground A stops treating `wp post update` as a publishing verb where the command sets no `post_status` at all, and keeps refusing it in every other case.** That is a narrowing with a test, not a loosening: a command that could change a status is refused exactly as it is today.

**It is not my change to make on my own judgement**, because it is the enforcement layer and because the work it would unblock is mine. It needs your ruling, and Kain validating it, before a line of H9 moves.

---

## 4. What this leaves open

Nothing on the install was changed. The 20 ids are read and held; the moment the wall question is settled they take one command.

---

OWED BACK: this ruling written into the document that owns article authorship; your ruling on the H9 narrowing in section 3; and Kain's own answer, put to him separately, on whether five WordPress accounts are created for the remaining pen names.

*No em or en dashes in this file; checked before writing.*
