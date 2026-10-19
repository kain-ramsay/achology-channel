**Needs from Cowork:** set the picture fields and the tag fields in the nine Seven Beliefs records, so Code can attach their pictures and tags. Small and mechanical. Run it end to end; skip and log anything you cannot do.

# BRIEF: the picture fields and tags in the nine Seven Beliefs records

**From:** Claude Chat, S394, Thursday 1 October 2026. **To:** Claude Cowork.
**Tray order:** first in the tray, before everything else (Kain wants the nine ready to publish). Do not start anything bigger until it is reported.
**Board card:** What Achology Believes.

## The job

In each of the nine records in `Content Records/seven-beliefs-series/` (PART_01 to PART_09), add these rows to the Page fields table, in this order after `post_excerpt`: `kh_tag`, `kh_tag_order`, `lead_tag`, `featured_image`, `featured_image_alt`. Change nothing else in any record: no body text, no other field.

**featured_image:** the record's own `post_name` followed by `.webp` (for example `can-people-change.webp`). Part 1's `post_name` is `standing-on-the-shoulders-of-giants`, so its value is `standing-on-the-shoulders-of-giants.webp`, even though its picture file in Kain's folder carries a different name; Code handles that.

**featured_image_alt:** a plain description of the picture, 8 to 20 words, carrying the record's own `rm_focus_keyword` exactly once, no quotation marks, no dashes, never describing a person. Look at each picture in the Article Page's Page Images folder (Kain made nine, named for the slugs; Part 1's is named for the old title, `the-seven-beliefs-achology-is-built-on`). Describe what the picture shows, then tie it to the keyword the way the published records do, for example "Two armchairs facing each other in a quiet room beside a notebook and pencil, standing for the choice between counselling vs CBT". If a picture cannot be found, write the alt from the part's idea, and list that part in your report.

**Tags (Chat's decision, from the locked outcome list).** Write exactly these. `kh_tag_order` repeats `kh_tag` in the same order. Separate with a comma and a space.

| Part | post_name | kh_tag | lead_tag |
|---|---|---|---|
| 1 | standing-on-the-shoulders-of-giants | understand-your-mind, unlock-personal-growth | understand-your-mind |
| 2 | can-people-change | unlock-personal-growth, master-your-mindset, overcome-feeling-stuck | unlock-personal-growth |
| 3 | know-thyself | grow-self-awareness, understand-your-mind | grow-self-awareness |
| 4 | thinking-errors | break-negative-thinking, master-your-mindset, understand-your-mind | break-negative-thinking |
| 5 | understanding-and-managing-emotions | develop-emotional-intelligence, manage-stress-and-anxiety, understand-your-mind | develop-emotional-intelligence |
| 6 | emotional-responsibility | develop-emotional-intelligence, master-your-mindset, build-mental-resilience | master-your-mindset |
| 7 | change-your-life-from-the-inside-out | unlock-personal-growth, navigate-life-changes, master-your-mindset | navigate-life-changes |
| 8 | sense-of-purpose | find-purpose-and-direction, achieve-your-goals | find-purpose-and-direction |
| 9 | philosophy-of-life | find-purpose-and-direction, understand-your-mind, unlock-personal-growth | unlock-personal-growth |

## Then check

Run the real gate on all nine. Expect failures on paragraph length and keyword density (Kain ruled those two lines exempt for this series; Code is typing the exemption now), and on Part 1 reading ease, words and long paragraphs. Report any other failure by line, but do not fix any text. If a tag slug is refused by the gate, report it and change nothing.

## Done when

Nine records carry all five fields, a one-line check shows none is empty or doubled, and `REPORT__Seven_Beliefs_Picture_And_Tag_Fields_Set_S394` is in FROM Cowork ending in the status line.

*No em or en dashes in this file; checked before writing.*
