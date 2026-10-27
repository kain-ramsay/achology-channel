**For Chat. What this needs:** write three of Kain's Safari afternoon rulings (Code S189, theme side session, 27 October 2026) into their homes: the course card in DSRD 8, the All Tags quilt in DSRD 9 section 35, and the category strip in DSRD 8 or 9 wherever the strip lives. Then mark R5 and R10 of BRIEF__Page_Readiness_Reader_Halves_Fixes_For_Code_S448, and item 2 of NOTE__Tag_Page_Reader_Halves_Run_One_List_For_Code_S449, as answered.

# RULING (theme, S189): course card stats balanced, topic names on a phone, the strip's soft fade

## 1. R5, the course card's student count: no word is ever added
Code showed four ways of adding a word to the count ("Students", "Enrolled", "Learners", a small label). **Kain's words:** "Claude, no more words are going onto these course cards ... Add by adding an additional word, onto that strip, it throws the design of the entire card. Nothing else goes onto it at all." **Instead:** "balance out those three social proof numbers ... the star stays as it is ... to the left ... the word video with the clock ... sits on the inside of the right-hand container, and then the student number is just kind of centralized." Shown in the Change Viewer, then **Kain:** "Yes, that's right. Build the balanced stats line."
**Built** (cards.css, theme commit 1808e1b7): from 360 wide up, the three stats sit on a three-column grid, with the stars at the left edge, the students centred and the hours at the right edge. Below 360 the row keeps T11's wrap. R5 part (a) is built too: a visually hidden " students" after the number (courses-setup.php), so a screen reader says what the number counts. Nothing visible is added.
**For DSRD 8's course card:** the stats line is balanced as above, and no word is ever added to it (Kain S189). This replaces the R5(b) idea of a visible word.

## 2. R10, the All Tags topic grid on a phone
Four options, shown at phone width. **Kain's words:** "Yes, option 1, names beside the icons on a phone."
**Built** (learn-tags.php and kh-subject.css, commit 46b05b91): below 768, the quilt is two columns. Each topic is a row with its coloured icon tile and its own name beside it, so nobody taps blind. The name is the topic's existing title, so no new word is written. From 768 up the quilt is unchanged.

## 3. The category strip's All Categories label on a phone (tag page record, chapter 8)
Four options, shown at phone width. **Kain's words:** "Yes, option 1, the soft fade on the category strip."
**Built** (kh-subject.css, commit 4e79bf3a): below 768, the subjects fade softly as they slide towards the label, so none is cut by the strip's edge. The label and the computer strip are unchanged. Code's WebKit could not reproduce a subject passing *under* the label; it saw a subject cut at the row's edge, and the fade covers both.

**Deploy:** branch safari-afternoon, handed to the founder-review session to merge and deploy. The version and the live read-back follow in SESSION_REPORT__S189.

OWED BACK: the dated lines in DSRD 8 and DSRD 9 named above.

*No em or en dashes in this file; checked before writing.*
