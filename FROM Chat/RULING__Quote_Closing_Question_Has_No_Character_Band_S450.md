> CODE DISPOSITION, S194: WAITS ON a factory session (read in full by the T7 AI crawler theme side session, which edits no gate script).

**For Code (factory session). What this needs:** two small changes to `content_gate.py` for gate type quote-page, then one line in TO Chat with the commit.

# RULING: the quote article's closing question has no character band, and its question paragraph is outside the paragraph rule (Kain, S450, 28 October 2026)

Kain lifted the S356 band of 79 to 89 characters on the closing question ("Yes, lift the cap"), after giving his own model close. The close is now two paragraphs under "A Question That Deserves an Honest Answer": a context paragraph in plain spoken words (three to six sentences), then one paragraph that invites the reader to be honest and asks a question naming both sides of their real choice, as long as it needs to be. His model, on the helping article Q06984, ends: "As we wrap up this article, be honest with yourself for a moment: when someone opens up to you about a problem they're facing, is your first response to listen, or are you typically more interested in getting your turn to talk at them or offer advice?" Each page words its own invitation (Kain: "Yes, vary it"). The rule is written in the vault's quote shape note (field 5), the Took note, the quote pack and the writer desk's checklist; `content_gate_standards.json`'s `_closing_question_chars_note` is marked lifted.

**The two changes:**
1. Remove the "closing question within 79 to 89 characters" check (line about 3331) for quote-page; build no length check in its place.
2. In "paragraphs of 3 to 6 sentences", treat the last paragraph under heading 5 (the invitation and question, which ends with a question mark) as the closing question line, outside the rule, as the fix note already says of the closing question line. The context paragraph above it stays inside the rule.

No vault note bears on this beyond the four named above.

OWED BACK: the commit, and one gate run on `vault_gate/briefs/quotes_r1_helping/rewrite/hand/Q06984__helping-is-about-the-person.md` showing neither line fails.

*No em or en dashes in this file; checked before writing.*
