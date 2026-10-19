> Code: Kain's ruling on banned words, written into the Standard as Version 27. Needs from you: the gate change, the writer's rules, and the slips fixed in the staged pages, then one DONE.

# BRIEF: ban the steady family, and make every banned word catch all its forms (Chat, S429, Monday 19 October 2026)

**Kain's ruling (S429, his yes at 10:16).** Reading the rewritten quote page CQ001-098-1, Kain said no human being uses "steady" or "steadier"; it is an AI word. Then he asked that every banned word's family be banned too. The Achology Content Standard is now **Version 27**, Part 16 rule 5 (Version 26 is in the factory Archive):
1. **Always banned:** steady, steadier, steadily, steadiness (moved out of `flag_in_context`).
2. **Every form of a listed word counts,** for every list in Part 16 rules 5 to 9: empower catches empowered, empowering, empowers; holistic catches holistically; steady catches steadied, steadying, steadies. The two exceptions stand: a real title, and a verbatim quote on a quote page.

**What done looks like.**
1. `content_gate_standards.json`: steady and its forms in `banned_always`; "steady" out of `flag_in_context`.
2. `content_gate.py`, the `found()` matcher: match every inflected form, not only plain and plural (today it adds `(?:e?s)?` only). A rule, not a longer list: for example the word's stem plus any word ending (`ed`, `ing`, `ly`, `ness`, `ier`, `iest`, `ies`, `ied`, `ying`, `s`, `es`), with a test per list showing a family form fails or notes as its plain word does. Watch the false hits a loose stem would make (for example "steadfast" must not match "steady"; "realm" must not catch "realms" wrongly, which is a correct catch; "fix" in the stance list must not catch "fixture"). List any word where you had to keep the match narrow.
3. The API worker's writer rules carry the ban, with the forms.
4. **The staged pages:** Chat's count on 19 October found 188 of the 1,147 newest staged pages using a steady word (336 uses; steadier 38, steadiness 33, steadily 19 among them), plus empowered (5), empowering (4) and holistically (3). Replace each with plain words a person would say, in the sentence's own meaning, by the cheapest route that passes (a script with a small writer call per sentence is fine). Never inside a verbatim quote or a real title. Re-run the six-word check and the stance step on every page changed.
5. **Count afterwards:** the same scan across every newest staged page reads 0 for every banned word and its forms, outside quotes and titles.

**Report:** one DONE in TO Chat: the gate change and its tests, the pages changed and uses replaced, any sentence you could not fix cleanly (with its slug), and the zero count. Pick five changed pages for Chat to read.

*No em or en dashes in this file; checked before writing.*

**WITHDRAWN by Chat, S429 11:13, on Kain's ruling: no patching. Folded into one complete instruction set per content type, shown to Kain before anything goes to Code.**
