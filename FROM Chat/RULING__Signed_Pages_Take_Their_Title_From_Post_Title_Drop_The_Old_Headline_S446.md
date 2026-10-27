> CODE DISPOSITION, S187: WAITS ON the S445 field authority, author biography, hub guide and hub question imports; the Help half is done, its owed line is in TO Chat/DONE__The_302_Help_Answers_Updated_The_73_Wait_On_One_Ruling_S187, section 4.

> CODE DISPOSITION, S183: WAITS ON a factory session (read in full by the theme main session; it touches no theme file, and the Help answers factory session was archived after delivering 286).

**For Code, factory session. What this needs from you:** when you import the S445 signed batches, drop the body's first-line headline on every page, because post_title is the title Kain approved and the old headline would make your importer refuse the page.

# RULING: signed pages take their title from post_title; drop the old body headline (Chat, S446, 26 October 2026)

Read from the vault first: the ruling "Every Article Is Checked Once and, Where It Fails, Rewritten Whole in Kain's Tone by a Session on His Plan", section "Titles are researched, never padded".

**What Chat found.** Each signed record carries its title twice: the `post_title` field, which Kain approved, and a `# ` headline at the top of the body. When titles were researched and changed at S445, Chat's step that restored titles wrote only `post_title`. Checked today in the batch folders, the body headline differs from `post_title` on: field authority 100 of 105, author biographies 30 of 30, hub guides 28 of 28, hub questions 54 of 55 and Help answers 32 of 374 (these two differ in capital letters only), workbooks 43 of 52. Your `drop_title_h1` (in `import_field_authority_articles.py` and the importers built on it) drops a first-line headline only when it matches the title, and refuses any other, so most of these pages would be refused.

**The ruling (Chat's call, technical, overturnable by Kain).** For BRIEF__Import_The_105_Signed_Field_Authority_Articles_S445, BRIEF__Import_The_Thirty_Signed_Author_Biographies_S445, BRIEF__Import_The_28_Signed_Hub_Guides_S445, BRIEF__Import_The_55_Signed_Hub_Question_Articles_S445 and BRIEF__Import_The_374_Signed_Help_Answers_S445: the page title is `post_title`, always. Drop the body's first-line `# ` headline on every page whatever its words, never show it, and never refuse a page for it. Workbook documents are different: their body headline is the workbook's own name by design (Kain named them at S445), so leave BRIEF__Build_The_52_Signed_Workbook_Documents_S445 as briefed. The 102 instructor articles coming next already have the two lines matching.

**Chat's own fix, done today:** the step that sets titles now writes both lines, and the instructor batch was corrected and checked (102 of 102 matching).

OWED BACK: one line in your import DONEs saying the headline was dropped and no page was refused for it.

*No em or en dashes in this file; checked before writing.*
