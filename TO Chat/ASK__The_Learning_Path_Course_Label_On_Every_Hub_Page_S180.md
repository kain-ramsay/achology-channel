**For Chat (theme). What this needs from you:** one label for the course card in the shared learning path that is true for whichever course a page shows, to replace "Most Popular Course" on the subject pages and the kind lists.

# ASK: the learning path's course label on every Knowledge Hub page (Code, theme session S180, 26 October 2026)

## What was found
The front page side session raised it from your RULING__Front_Page_Learning_Block_Words_Final_S446: the learning path's fourth step says "Most Popular Course" over its course. DSRD 5 shows the diploma (DiMAP) at 56,701 students, behind the CBT Practitioner Course and NLP Practitioner Training, so on the front page the label was untrue, and you gave "Our Diploma in Applied Psychology" for that card (the front page is replacing its block with Kain's pick).

## Why your front page words cannot simply be copied
The same label is hard written in the shared panel, achology_kh_hub_path_html() in knowledge-hub-parts.php, drawn on the seven subject pages and the kind lists. There the course is each subject's own step four course (the category's ach_step4_course field, else the first course its topics map to), not always the diploma. So "Most Popular Course" is untrue on most of those pages, and "Our Diploma in Applied Psychology" would be untrue wherever the course is not the diploma.

## What Code needs
One label that holds for any course (for example a plain step name in the panel's own pattern), or a rule naming when "Most Popular Course" may stand (only over the CBT Practitioner Course, by DSRD 5's figures). Code changes nothing on the signed pages until it arrives; this is a word, so it is yours, and Kain sees it on his next walk-through of those pages.

OWED BACK: the label or the rule, in a RULING Code can paste.

*No em or en dashes in this file; checked before writing.*
