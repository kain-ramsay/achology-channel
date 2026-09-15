# REPORT: the six AI wisdom articles are drafts, each with its hero attached

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** `NOTE__The_Six_AI_Wisdom_Hero_Image_Names_And_Where_Kain_Saves_Them_S362.md`.

---

Kain's export landed already named to slug, six of six, no remapping needed: `AI Wisdom Hero Template.zip`, unzipped into the Page Images folder as masters (2200x1050, 1.25x scale of the 1760x840 design, same shape). Run through `image_pipeline.py` at the hero slot, 680px display width to match every existing article hero, quality 82: all twelve WebP files land between 11.8KB and 39KB, well under the 200KB 2x budget.

Imported with `import_field_authority_articles.py --type instructor-article`, which reads each record's own `featured_image` field directly rather than a static per-batch map. 6 of 6 pass, 6 of 6 pushed as drafts with their image attached at create, 6 of 6 verified clean back off the install. Confirmed one image live and correctly sized over its real URL.

Drafts only; nothing published. That closes the mechanical half of the six AI wisdom articles card.
