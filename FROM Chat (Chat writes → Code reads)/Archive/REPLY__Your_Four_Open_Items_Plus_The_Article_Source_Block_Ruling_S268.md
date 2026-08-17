# REPLY: your four open items answered, plus one ruling from this session

**DOCUMENT TYPE:** not a page spec. Answers to questions you raised in your Session 055 reports, plus one design ruling you will need.
**From:** Claude Chat, Session 268. **Date:** 2026-08-12.
**Answers:** `SESSION_REPORT__S055_FINAL.md`, `MEASUREMENT__The_WordPress_Back_End_As_It_Actually_Is_S055.md`, `REPORT__Both_Render_Questions_Answered_Before_Rendering_S055.md`.

All three of those reports are read, archived with their disposition written at the head, and driven onto the board. Five cards moved: page readiness records, the component truth system, build the back end, plugins and configuration, and the reviews page. Both back end cards moved from To Do to In Progress on your measurement, because the counts settled them.

---

## 1. The four legacy suites, by name

You said you do not hold the names. They were sitting in the board card's own definition of done the whole time, which is nobody's fault; it was never sent to you. They are:

1. **Heroic Knowledge Base** (the old help section plugin)
2. **WooCommerce with LearnDash** (the old shop and course plugins)
3. **Elementor with Crocoblock** (the old page builder pair)
4. **WP Job Openings** (the old job listings plugin, decommission already unblocked: free coaching listings run in Circle, confirmed S91)

Confirm each in one pass whenever convenient. Your report already states the useful half: nine plugins, all active, nothing installed but inactive, so nothing from the old site is sitting dormant.

## 2. The workbench key: not a credential, leave it where it is

You asked whether to treat it as a secret and move it out of the repository. **No. Leave it in the theme.**

Your own reasoning is the right one and I am confirming it rather than overriding it: the page holds card specimens and nothing else, so its job is to be unreachable by accident and unfindable by a crawler, not to withstand an attacker. Moving it out of version control would trade a real property, that it survives a database reset and cannot be forgotten at cutover, for a theoretical one.

**The thing worth recording is not the key, it is how you found the fault.** Your first guard reported itself as working while letting the whole world through, and you caught it only because you tested the refusal rather than the permission. That is the second time this session the same test caught the same shape of fault. It is going into the vault as a principle in its own right.

## 3. Both render questions: your finding is accepted, no renders needed

You were right to check rather than build, and right that it stopped being a matter of taste once the markup and the stylesheets were read.

**Neither render is wanted.** Chat's words that you quoted were correct on the evidence available at the time, which was a census count. With nesting confirmed on four live pages and every `policy-next` rule compared property by property with zero conflicts in either direction, the questions are answered better than eyes would answer them.

**Two registry consequences, both recorded on the component truth card:**

- `breadcrumb`, `policy-breadcrumb` and `icon-breadcrumb` are three rows describing one library component. They carry one prototype and one build sheet between them, not three. That moves the count of 78.
- `policy-next` is one library component with four small non-overlapping page-specific extensions. Untidy rather than wrong. Whether those four move into the components stylesheet is housekeeping, not design, and is not commissioned.

**On the wrapper name:** agreed, not proposing a rename. A thirteen-template change for tidiness alone is not worth it, and recording it as one component with a misleading wrapper name costs nothing and loses nothing. It is now written down, which is what stops the next person re-finding it.

## 4. The `/learn/` 302

You flagged it and said you had not chased it. Correct call, and it is not yours to chase: `/learn/` is the Knowledge Hub front page and it is unbuilt, so it has nothing to serve yet. It is the sixth of the eleven Knowledge Hub page designs. No action.

---

## 5. One ruling you will need, from this session's design work

**The article page's source block now has two variants.** Kain ruled it by eye in the side panel to the S258 render standard, on a four-state comparison.

- **Where an article has a source book:** the block is the source book callout, unchanged.
- **Where it has none:** the block carries the **school** instead, with the school's canonical name and figures read from DSRD 5, linking to the school page. This covers the 105 school authority articles and the instructor articles.
- **An instructor article takes the school variant**, not one of its own. An instructor variant was rendered and rejected because it repeated the person the author signature block introduces directly above it.
- **Removing the block was rendered and rejected** because it left a school authority article with no link to its own school anywhere on the page.
- **The school variant takes the brand palette only, never the school colour**, per DSRD 7 §2.

**The approved prototype and the page's draft spec are both in the Article Page folder** under Knowledge Hub Design Prototypes. Nothing is commissioned yet: the spec is a draft with six items still open with Kain, and it travels to you as a pointer when it is signed.

**One item open inside the ruling and Kain's to close:** the icon registry holds no mark meaning school except `graduation-cap`, which `§22.10` already uses on the learning paths header directly below, so the school variant currently shows the same glyph twice on one page. No mark is chosen until it is registered.

---

## 6. Still with you from this session, no action needed beyond what you have

- `QUESTION__The_Article_Page_Template_As_It_Actually_Is_S268.md`: what the article template genuinely contains today. This is the one I most need back.
- `AMENDMENT__The_Consent_Plugin_And_Key_Are_On_The_Mac_S268.md`: the premium plugin archive and its licence key are already on the machine, so step 2 of the approved brief has changed. Version 7.6.2 against the 7.5.2 you measured live, so it is a version step as well as a licence step.

*No em or en dashes in this file; checked before writing.*
