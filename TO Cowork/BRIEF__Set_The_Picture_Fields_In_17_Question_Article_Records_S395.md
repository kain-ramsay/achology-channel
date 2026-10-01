**Needs from Cowork:** set two picture fields in 17 question article records, so Code can attach their pictures. Do this after the four jobs in `RULING__Four_Small_Jobs_Go_To_The_Front_Of_Your_Tray_S395`, and before the S388 order. Skip and log anything you cannot do.

# BRIEF: set the picture fields in 17 question article records

**From:** Claude Chat, S395, Friday 2 October 2026. **To:** Claude Cowork.
**Same job as** `BRIEF__Set_The_Picture_Fields_In_The_36_Elder_Records_S393`, for a different set. Kain is making these 17 pictures now.

## The 17 records, in `Content Records/hub-question-article/`

being-present-in-the-moment, benefits-of-mindfulness, best-mindfulness-books, can-mindfulness-meditation-be-harmful, can-self-awareness-be-learned, conditions-of-worth, how-to-practice-mindfulness, is-mindfulness-evidence-based, is-self-criticism-good, lack-of-self-awareness, mindfulness-skills, mindfulness-therapy, mindfulness-without-religion, what-is-mindfulness-based-stress-reduction, what-is-self-understanding, what-is-stress-management, zen-vs-mindfulness.

## The job

- Open each record and check whether `featured_image` and `featured_image_alt` are already set. Chat has not checked this, so do not assume they are empty. Where a field already holds a value, leave it and say so in the report.
- Where `featured_image` is empty, set it to the record's own slug followed by `.png` (for example `zen-vs-mindfulness.png`). The full list is in `000__IMAGE_MAP__17_Article_Pictures.csv` in the Article Page's Page Images folder, subfolder `17 Article Pictures To Make (S395)`; copy the `save_as` column exactly.
- Where `featured_image_alt` is empty, set it to a plain description of the picture that carries the record's own focus keyword once, 8 to 15 words, no quotation marks, no dashes. The pictures are not made yet, so describe an idea and never a person, as in the elder brief: for example "A calm, warm abstract image about being present in the moment".
- Change nothing else in any record. Run the real gate on a sample of five and report the result.

## Done when

17 records carry both fields (or you have said why one did not change), a one-line check shows none is empty or doubled, and `REPORT__Seventeen_Picture_Fields_Set_S395` is in FROM Cowork ending in the status line.

*No em or en dashes in this file; checked before writing.*
