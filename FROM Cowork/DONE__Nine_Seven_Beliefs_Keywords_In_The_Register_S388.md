**Needs from Chat:** nothing to decide. Archive the brief. One finding for whoever owns the register builder is at the end.

# DONE: the nine Seven Beliefs keywords are in the keyword register

**From:** Claude Cowork, Monday 28 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Nine_Seven_Beliefs_Keywords_Into_The_Register_S388`.

## The result

- **Register rows before:** 1,403. **After:** 1,412. Nine rows added, one per part, at the end of the file, dated 2026-09-28, session S388. The 1,403 rows already there were checked line by line after the write and are untouched.
- **Read from the records:** every keyword was read from its part's `rm_focus_keyword` field, and all nine match Chat's table word for word: standing on the shoulders of giants, can people change, know thyself, thinking errors, managing emotions, emotional responsibility, change your life, sense of purpose, philosophy of life.
- **Clashes:** none. No keyword was already in the register, and no other record or claims file on disk claims any of the nine.
- **No word in any part was changed.**

## The route, and why it was by hand

`build_keyword_register.py` can read the series folder, and a dry run of it (written to a scratch file, never over the register) produced the nine rows cleanly. But the builder rewrites the whole register from scratch, and on today's disk that would also have changed about 90 other rows: 58 help-answer and hub-guide rows would appear or change their keyword, 33 rows now in the register would be replaced, and every row's date would reset. That goes well past this brief, so the nine rows were added by hand, by a short script copying each from its record's page fields.

## One finding, for the register's owner

The same dry run reports **21 keyword clashes already on disk**, none involving the Seven Beliefs. Most pair a quote page with another quote page (for example "there are no experts on life" on both `no-experts-on-life` and `there-are-no-experts-on-life`, and "ready to change" on `ready-to-change` and `wanting-is-not-readiness`). The register as it stands does not show them, because it was last rebuilt before those records existed. Nobody has briefed Cowork on this, so it is named here and not acted on.

*No em or en dashes in this file; checked before writing.*

COWORK | Batch: nine Seven Beliefs register rows | Drafted: 9 of 9 | Gate and evaluator: not applicable, register rows only, read back clean | Skipped: none | Outside brief: none
