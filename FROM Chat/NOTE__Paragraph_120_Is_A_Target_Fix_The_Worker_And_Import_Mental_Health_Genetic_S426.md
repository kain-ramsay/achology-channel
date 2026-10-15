> CODE DISPOSITION, S169: WAITS ON the import factory session for is-mental-health-genetic (part 2); part 1 is DONE, the worker's paragraph line now reads as Chat worded it, and no free check or checker rule fails a paragraph for passing 120 words.

First line of need: Code, factory session: two small things. (1) The API worker's writer rule says paragraphs are "none over 120 words"; the Standard says 120 is a target, never a fail. Fix the line. (2) Lift your import hold on is-mental-health-genetic and import it.

# NOTE: 120 words is a target, so fix the worker and import is-mental-health-genetic (Chat, Session 426, Thursday 15 October 2026)

**The rule, read this turn.** Standard Part 6 rule 2 (Version 22, Kain S424): "Paragraphs of three to six sentences, aiming for about 120 words. 120 words is a target, never a fail." The gate prints a NOTE above 150 or below 45, never a FAIL. PACK_01 file 06 says the same: "a longer paragraph is fine when the thought needs it ... Never clip a thought."

**1. The worker.** `api_worker.py` line 73, in `WRITER_RULES`, says "Paragraphs of 3 to 6 sentences, none over 120 words." That tells the writer to clip, which file 06 forbids. Replace it with: "Paragraphs of 3 to 6 sentences, aiming for about 120 words; longer is fine when the thought needs it, and over 150 is worth a second look. Never clip a thought to hit a number." If the checker or any free check fails a paragraph for passing 120, change it to match. Leave the batch now running alone; Chat reads its 16 for clipped paragraphs and asks for a rerun only if it finds any (the whole batch costs a few dollars).

**2. is-mental-health-genetic.** Kain signed this version on 13 October 2026 ("very, very, very good"). The import was held only because nine paragraphs ran 125 to 141 words. All are under 150, so under the rule above there is nothing to settle. Import it with the next signed records.

OWED BACK: one line in your next DONE: the worker line changed, and the page imported.

*No em or en dashes in this file; checked before writing.*
