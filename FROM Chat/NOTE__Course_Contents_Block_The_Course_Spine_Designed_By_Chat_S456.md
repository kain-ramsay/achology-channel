**For Code, the course page design session. What this needs from you:** build block 3, The Course Contents, to Chat's design The Course Spine with Kain's side panel pick, option 4, How far you will be. Chat, S456, 3 November 2026.

# NOTE: the course contents block, The Course Spine, with the progress ring

**Kain's words (S456):** on the direction, "somewhere between A and B, plus we want to use that strip"; on the side panel options, "option 4 is really, really nice ... really strong."

**The design file.** In the Course Page folder: `000__DESIGN__Course_Contents_Spine_Side_Panel_Options_S456.html`, which is self-contained with every lesson of course 001. Choose "4. How far you will be" in its bar. The same design without the options bar is `000__DESIGN__Course_Contents_The_Course_Spine_S456.html`.

**What it is.**
- **Block head:** the heading "What the Course Covers, Section by Section" (Como 24/600), one supporting line, and the four figures on the right (8 sections, 175 lessons, 51+ hours of video, certificate on completion). These figures move here from What You Will Learn, as Kain asked.
- **The spine, which replaces your section strip:** the whole course is drawn to scale as one continuous bar. Each section's length is its share of the lessons (flex by lesson count, a minimum of 4 so the one-lesson Summary can still be clicked), with 3px gaps and rounded ends. At rest a segment is brand orange at 22 per cent, and 45 per cent on hover. The chosen segment takes an orange gradient, scales up 1.45 on the vertical and casts a soft orange shadow. Labels under it read "N Name" in Como 14/600 and "N lessons" in Mulish 13; a narrow segment shows its label only when chosen, and on a phone only the chosen label shows. The bar is a tablist, and the arrow keys move between sections.
- **The thread:** a 2px orange line, 30 tall, with a 12px action orange dot, drops from the chosen segment into the panel and travels when the section changes (0.45s).
- **The panel:** white, a 24 radius, with two columns at computer width (300 and the rest). The side column holds a large faint section number (Como 120/700 at 14 per cent orange), "Section N of 8", the section name (Como 21/600), "Lessons X to Y of 175", the Next button (action orange disc), and at its foot **the progress ring, Kain's pick:** a 76px ring, 8 stroke, brand orange on the hairline, with the percentage in Como 24/700 and "of the course covered by the end of this section". The lesson column holds the lessons numbered through the whole course (001 to 175), each showing its name (Como 18/600) and guiding question (Mulish 16, soft grey), with the ring-to-fire plus and minus toggle (pick 15). Each opens to its signed 60 to 80 word paragraph, and the open title turns action orange. Seven show at first, then "Show all N lessons in this section".
- **Phone and tablet:** the spine stays one strip, the side column folds into a header row above the lessons, and nothing scrolls sideways at 375.

**How the design skills were used:** frontend-design was loaded first. The one bold idea is the course drawn to scale, because it carries real information (the shape of the course). Everything else stays quiet. There is one orchestrated motion, the thread travelling and the panel settling. No all-caps labels. Numbering is used only where the content is a real sequence. Checked in the browser at 1280 and 375 before Kain saw it, and one fault fixed: the first pointer was white on the grey band and could not be seen, so it became the orange thread.

**Content.** Each course's lessons, questions and paragraphs come from its copy file, `Course Page Copy/000__COPY__Course_Lesson_Paragraphs_NNN_S456.md` (001 to 021 written, the rest landing tonight). The short section names under the spine (Foundations, Behavioural and so on) are Chat's for 001. Chat writes a short name for every section in the other 27 courses once the build is agreed.

Keep DSRD 7's type and spacing, and run your two screenshot passes.

*No em or en dashes in this file; checked before writing.*
