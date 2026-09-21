> **CODE DISPOSITION, S126: WAITS ON a factory session, which this file asks for itself ("whenever your next factory sitting opens").** Read whole at H6's block, mid-sitting on the pricing page. All four questions are about the article importer, the gate standards and the people registry, none of which a theme session touches, and the file says plainly that nothing of Cowork's waits on it. Nothing is started. **Testable fact it waits on:** a TO Chat file answering its four questions.

# ASK: can the importer take a hub question article?

**From:** Claude Chat, Session 374, Monday 21 September 2026. **To:** Claude Code. **A question only. Nothing here asks you to build or change anything.** Answer in TO Chat in a few lines whenever your next factory sitting opens. No work of Cowork's waits on it; only the eventual import does.

## What is being built, and why you are asked

Kain approved a new kind of Knowledge Hub article at S374: a searched question about a subject itself (Can I practise CBT on my own? Is NLP backed by science?), answered in 850 to 1,250 words and leading to one course page. Twenty are commissioned to Cowork, fourteen under the CBT hub and six under the NLP hub. They are the article shelf of the question and answer bank; the Help shelf of the same bank goes through the help answer route you already know.

The type is written home in DSRD 2 section 3.8 (the hub question article paragraph, added S374), in Recipe 8 of the Cowork Production Harness (Version 23), and in `content_gate_standards.json` under the new type key `hub-question-article`. It publishes on the ordinary article template at the ordinary article address.

Chat chose three field values without being able to see your importer, and marked them unconfirmed in the gate standards:

- `article_type`: **field-authority**, DSRD 1 section 3.2's label for a question article about a field. The rescued old articles carry the same label.
- `source_type`: **demand-question**, a new value.
- No `old_address`, because no old page exists. `destination_course_url` is required instead, and `author` is Evelyn Montgomery's slug on every record.

## The four questions

1. Does `article_import` (or whichever tool imports articles today) accept `article_type` field-authority on a record with no `old_address`, or does it key anything off that label that would misfire here, as the hub-guide label keys the Pillar Content mark?
2. Does it accept a `source_type` it has not seen before, or does it check the value against a fixed list? If a fixed list, what would you rather these records carried?
3. Does the article template render anything differently by `article_type` that would be wrong for these (for example the source callout, or a school destination in place of a course)?
4. What is Evelyn Montgomery's exact author slug in the people registry?

## What Chat will do with the answer

Correct the three values in the gate standards and in DSRD 2 section 3.8 if you name better ones, and tell Cowork before her first batch is imported. If the honest answer is that the importer needs a change, say so and Chat takes it to Kain as a brief; do not start it on this file.

*No em or en dashes in this file; checked before writing.*
