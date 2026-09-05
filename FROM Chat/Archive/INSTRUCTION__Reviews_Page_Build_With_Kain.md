# INSTRUCTION: build the Reviews page with Kain, S240

**From:** Claude Chat, S240. **Date:** 2026-08-04.
**Read with:** `PLAN__Reviews_Page.md` in this folder, which is the structural plan and is not repeated here.
**Read first:** this file. It tells you how this page is being run, which is different from About.

---

## 1. The change in method, ruled by Kain at S240

**The Reviews page is designed in Claude Code with Kain at the browser, not in Chat.** Chat produced the plan; the design happens with you. Kain will iterate with you on screen, and he is making the graphics and images himself in Canva.

What that means in practice:

- The plan is your instruction for structure, copy, data and standards. Follow it exactly.
- The visual treatment of each block is Kain's to settle by eye, with you, on the rendered page. Section 11 of the plan lists precisely which items those are.
- Standing rule 19 still holds in substance: you build only to what Kain has approved. Here his approval arrives live in your session rather than as a signed spec from Chat. Record what he approves as you go, and return it through TO Chat so Chat can write it into the DSRDs.
- Where the plan is silent and Kain is not present to rule, stop and ask through the channel. Do not fill a gap with judgement.

Chat's job from here is the record: the DSRDs, the board, and the channel. Send the outcomes back and they will be written up.

---

## 2. The review card is DEFINED and LOCKED. Do not redesign it.

**DSRD 8 §14, LOCKED at S239.** Kain approved every value by eye across sixteen rendered rounds, on cards carrying real review data from the live bank. It is the atomic unit of this page and of the future course-page and school-page review blocks. Read §14 in full at the canonical DSRD folder before you write a line of CSS for it.

What §14 covers, so you know it is all there: the card shell (§14.1), the body and its content stack (§14.2), the star row including the half-star mechanism and its accessible label (§14.3), the course signpost footer with the flipped artwork and the baked course URL (§14.4), and the data and production rules (§14.5).

**One change to §14 from S240, and it is a removal.** The featured scaling in §14.5 is withdrawn by Kain: **standout reviews render at normal card size.** Everything else in §14 stands unchanged. Chat updates §14.5 to match once Kain confirms; build to normal size now.

Nothing else about the card is open. If something about it looks wrong on the page, that is a finding to report through TO Chat, not a licence to adjust it.

---

## 3. What you are building, in order

Follow `PLAN__Reviews_Page.md` section 3 for the block order, and its sections 4 to 8 for each block. The short version:

1. **Hero**, built on the About page's `.policy-header--doc` pattern exactly. Same frame, same floated 312px artwork, same title, lead and button anatomy, same responsive behaviour including the 599.98px exception already named in DSRD 7 §4.5. Kain supplies the artwork; use a plain placeholder until it lands.
2. **The global impact block, ONE component.** Kain ruled at S240 that the map and the proof figures are a single component, not two. DSRD 4 §14.2 Variant 1, the V2B Dark Band direction. This page is its first build, and the component is later shared by the homepage and About.
3. **Standout reviews**, the Featured set, in the locked card at normal size.
4. **The archive**: control bar, live count, the full grid, batching your call.
5. **Where next**, DSRD 8 §13 reused as-is.

---

## 4. Two things waiting on you

**The map data file.** `BRIEF__Fetch_World_Map_Data_For_Reviews_Page.md` in this folder asks you to download the Natural Earth 110m TopoJSON to The Review Page assets folder. Kain tried twice from the browser and got a screenshot both times. Do that first; the map block is blocked without it. There is a stray `countries-110m.png` in that folder from the failed attempts, which is a screenshot and not an asset.

**The schema question.** No star rich snippets are available for self-hosted reviews about one's own organisation. You decide what this page emits, state it plainly, and Chat records the answer in DSRD 10. Do not propose a rich result Google will not grant.

---

## 5. Definition of done

DSRD 6, every chapter, with the per-chapter record returned through TO Chat. Plus Kain's approval by eye on every block, which on this page he gives you directly.

Return through TO Chat as you go: what Kain approved and in what terms, any value you had to name that the system does not yet hold, and anything the plan got wrong. Chat writes all of it into the owning documents.

*No em or en dashes in this file; checked before writing.*
