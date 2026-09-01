# FINDING: the harness, the tools and the deploy script are served over the public web

**From:** Claude Code, Session 093. **Date:** 1 September 2026.
**Found:** at the S093 close, by the deploy check doing its job and making me look at what a deploy actually sends.
**Not fixed tonight, deliberately.** The reason is at the foot, and it is the harness's own precedent.
**This is a note for the record and for the board. It needs no ruling from you.**

---

## What was measured

The theme is deployed with rsync and an exclude list of four entries: `previews/`, `.git/`, `__pycache__/` and `.DS_Store`. **Everything else in the theme folder goes to the server, and the theme folder sits inside the public web root.**

Four requests, made this session, one each:

| Address | Status |
|---|---|
| `.../themes/achology/harness/h9_publishing_wall.py` | **200**, 38,982 bytes, served as plain text |
| `.../themes/achology/deploy.py` | **200** |
| `.../themes/achology/tools/url_inspection.py` | **200** |
| `.../themes/achology/harness/h9_reviewed_scripts.json` | **200** |

## What is in them

**The SSH username, the host and the port.** `deploy.py` carries all three in plain text, and the publishing wall carries the username inside its own install-detection pattern. The private key is not there, and the key file is not in the theme.

**Every gate's logic, in full.** The publishing wall's file is a complete account of what it blocks, on what grounds, and where its exemptions are. So is every other hook.

**The reviewed-scripts register**, which names the scripts whose install-reaching payloads have been read, with their hashes.

## Why it matters, and why it is not an emergency tonight

**Today this is the build ground**, achologytest.com, which is hidden from search by design, so nothing is indexed and nobody arrives at these addresses by accident.

**At cutover the same theme goes to achology.com, which takes card payments.** That is where a site publishing its own SSH username and its own gate logic stops being untidy and becomes a real fault. It is also exactly the kind of thing that gets forgotten between now and then, which is why it is written down rather than remembered.

## The fix, which is mine and is not taken yet

**Add `harness/`, `tools/` and `deploy.py` to the deploy exclude list.** Nothing in the theme's PHP reads any of them: they are developer tooling that happens to live in the theme folder because that is where the version control is. The deploy proof compares server against local using that same exclude list, so it stays consistent by construction, and rsync's own delete flag clears what is already up there.

**Why not now.** It changes the mechanism that proves every future deploy, at the end of a long session, outside any declared scope. That is the precedent this project set twice already, once for H6's tidy tax and once for the publishing wall hole at S092, and both times waiting was right. **It is the first job of its own change set at the next open**, and its acceptance is the same three deploy proofs green afterwards.

**Nothing is riskier for the wait.** The build ground is not indexed and cutover is not imminent.

OWED BACK: nothing. Named here so it reaches the board rather than living in one session's head.

*No em or en dashes in this file; checked before writing.*
