> CODE DISPOSITION, S208: WAITS ON Kain installing the plugin (the /plugin commands are his to run; a session cannot install a plugin or change settings on a peer's word) and on the factory session for the hook (ASK__A_Gate_So_The_Design_Skill_Is_Always_Loaded_S208 in TO Chat asks the same). Sections 3 and 4 are applied now: the course page design session is redoing block 2's outcome cards through visual-design-craft, each design from a named site, before block 3.
**For Code, theme and design sessions, open first of all. What this needs from you:** set up three things so that every page and block you design is designed, not just assembled, then prove it on one block. Chat, S456, 3 November 2026, on Kain's direct instruction: "I want code to start doing exceptional design work on these pages ... What is the permanent solution for this?"

# BRIEF: make Code design every block, permanently

**Why.** Kain, S456: "all I ever get from him is clunky block work. Clunky and bland block work ... Claude Code refuses to design." The course page record (previews/course-page-s208/PICKS.md) shows it plainly. Picks 36, 37, 72 and 73 were rejected as rearrangements, not design. The one block that worked, pick 74, started from real sites. The rules (type, spacing, change nothing) are being met. The design is not happening. A rule written in a file has not fixed this, so the fix has to load and fire on its own.

## 1. Install Anthropic's design skill, on by default

Install Anthropic's official frontend-design plugin, which lives in `anthropics/claude-plugins-official` (plugins/frontend-design), not in anthropics/claude-code as first written: `/plugin marketplace add anthropics/claude-plugins-official`, then `/plugin install frontend-design@claude-plugins-official`. Also turn on ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill), which is already among the account's skills, and use the Playwright MCP already on this machine to screenshot every design. Enable it in the theme project's own `.claude/settings.json`, so every Code session in the theme loads it without anyone asking. Keep the visual-design-craft skill on beside it.

## 2. A hook that fires on every design file

Add one hook to the theme's harness. Whenever a file under `previews/` is written or edited, it prints into context, once per file: read frontend-design and visual-design-craft; name the real site this block's design is drawn from; take one bold idea for this block, inside the design system; screenshot the result at computer and phone width and judge it against that reference before Kain sees it. The Change Viewer refuses to open a round that has no reference named and no screenshot judged. This is a check that fires on its own, not a rule to remember.

## 3. Design inside the system, not instead of it

DSRD 7 sets the type, spacing and colours, and nothing in this brief loosens it. Within those, every block gets a design idea of its own, drawn from what the block has to say: composition, image, scale, contrast, motion, cream and dark bands, the brand orange used with intent. A block that only places text and images in a grid is not a design and is not shown.

## 4. Prove it on one block

Redesign block 3 of the course page, The Course Contents, with Kain's signed course 001 lesson paragraphs (Course Page Copy, `000__COPY__Course_Lesson_Paragraphs_001_S456.md`; Chat's plain rendering is in `Course Contents Previews S456`). Show Kain four designs in the Change Viewer, each drawn from a named real site, each with its own idea, plus Chat's plain version as the before.

**Done when:** the plugin and hook are live in the theme project, the hook fires on a test edit, and Kain has picked a block 3 design. Report in TO Chat with what was installed, the hook's proof, and his pick.

*No em or en dashes in this file; checked before writing.*
