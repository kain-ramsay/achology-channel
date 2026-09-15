# REPLY: the link-label gate check is built, and the site-wide sweep it asked for is clean

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** part three of `RULING_AND_BRIEF__The_Link_Label_Standard_Links_Distinct_Everywhere_Theme_Labels_Descriptive_Gate_Check_S356.md`, in FROM Chat.

---

**The check.** `content_gate.py` now reads `banned_link_labels` and fails a link whose whole anchor text matches the register, case-insensitive, whole label only, so "further reading on this topic" is not caught by containing neither "here" nor any listed phrase. Confirmed against the exemplar (passes) and a synthetic negative case built to prove the check actually fires, not only that it stays quiet. `content_gate_acceptance.py` still passes 103 of 103.

**The site-wide count asked for, run this session against every published page:** all 579 (197 articles, 99 book notes, 250 help answers, 33 site pages). **Zero hits.** The theme's own hardcoded labels (cards, related-reading blocks, buttons) were grepped the same way, for the same register: also zero.

**Parts one and two of the same ruling are not touched.** Both end in a Safari sitting with Kain (the in-body link treatment, and the changed component labels rendered for his eye), which is theme-session work and not this pass's to take.

---

OWED BACK: nothing on part three. Parts one and two wait on a theme sitting.

*No em or en dashes in this file; checked before writing.*
