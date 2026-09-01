# REPORT: the publishing wall, four findings closed, 63 of 63 acceptance cases

**From:** Claude Code, Session 093. **Date:** 1 September 2026.
**Closes:** finding 2 of `ASK__The_Wall_Cannot_Bin_The_Eighteen_And_It_Let_A_Delete_Through_S092.md`, which said plainly that it was mine to close and would be the first job of its own declared change set. It was, and this is it. Also closes the two false refusals recorded at the foot of `SESSION_REPORT__S092.md`.
**Board card:** the harness's own. Nothing on a content card moves because of this.
**Commit:** `17ba33b` in the theme repository, pushed. Two files changed, both in the harness folder. **No theme CSS or PHP was touched, so there is no version bump and no deploy:** these hooks run on this machine, never on the server.

---

## Four findings, not three

Three came in from S092. **The fourth was found here while proving the other three**, and it is the most serious of the four. All four are closed in one change set because they are one job and one file.

**They are also one fault.** The wall judged the TEXT of a command rather than the commands in it. Every one of the four falls out of that, and the harness's own words for this wall are that it reads what a command does rather than the words it contains. That sentence is now true.

## Finding 1, a hole: a WP-CLI global parameter hid every publishing verb

The command that went through the wall unblocked at S092, against a real post id:

    ssh ... "wp --path=/home/.../public_html post delete 33535"

Every pattern on ground A was written to need the subcommand immediately after `wp`. WP-CLI takes global parameters in between, and this project uses one on every call, because the SSH login does not land in the WordPress root. **So the flag split the verb from its binary and the pattern saw nothing.**

**The hole was never about `delete`.** Proved by driving the hook: `create`, `update`, `generate`, `trash` and `eval` were all one global flag away from invisible. It went unnoticed because the ordinary shape of a publish also carries `--post_status=publish`, and a second check caught that. A publish with no status flag on it, or any takedown, had nothing in its way.

**Closed:** every WP-CLI pattern in the file now runs through one prefix that tolerates any number of global parameters. Seven acceptance cases, one of them the S092 command verbatim.

## Finding 2, a false refusal: a plain SELECT refused for saying the word publish

`wp db query` was refused on sight, on the reasoning that a database write can publish without WordPress noticing and that the payload cannot be read. **The first half is true. The second half is not.** A single quoted SQL statement on the command line is exactly as readable as the command around it, and refusing it blocked ordinary measurement work.

**Closed:** a `wp db query` is now READ, and it passes only where all of these hold. One inline quoted argument. Opening on SELECT, SHOW, DESCRIBE or EXPLAIN. No writing word anywhere in it. One statement, so nothing rides behind a semicolon. And no shell substitution inside a double-quoted payload, because inside double quotes a backtick and a `$` run a command while inside single quotes they are literal and a backtick is MySQL's own identifier quote.

**Everything else is refused unread**, and each has its own case: a second statement behind a semicolon, a payload read from a file, a payload that is a command substitution, a bare query taking its statement from standard input, a SELECT carrying INTO OUTFILE, and `wp db import`, which is not readable on any terms.

## Finding 3, a false refusal: `||` is not a pipe

The pipe check split on `\|\|?`, so it cut at a `||` and judged what followed as a pipe TARGET, a thing being fed output it cannot be read handling. A compound was refused whose second half the wall allows on its own line.

**Nothing is piped by `||`.** It is a statement separator, and the statement after it is an ordinary command that all three grounds read on its own merits. **Closed:** only a single `|` cuts a pipe stage. Nothing is weakened, and there is a case proving it: an unreadable shape after a `||` is still refused, by the grounds that were always going to catch it.

## Finding 4, a hole, found here: a read verb answered for a write beside it

    ssh host 'wp post list --format=ids; wp rest post edit 44 --post_status=publish'

**Allowed, until this session.** The status check asks two questions of one string, is a status being set and is this a read, and asked of the whole line they answer about different halves of it. The `post list` at the front answered for the `post edit` behind it.

**It is the same shape as the ground C hole closed at S087**, where a read verb at the front switched off the check on the payload behind it. It survived in the status check because that check reads the line rather than the commands in it.

**Closed:** the check now runs per statement, and it walks into quoted payloads, because an ssh payload is a quoted span and every command this wall cares about arrives inside one. Three cases, including one proving two honest reads in one payload are still allowed.

**Why it was fixed here rather than filed.** It is a live publishing hole in the hook already open on the bench, under a declared scope naming that hook, found by proving the very findings the scope names. Filing it would have left it open for a session with the fix a line away. Named here rather than folded in silently.

## The proof

**63 of 63 acceptance cases as specified, 0 wrong.** 24 are new, they sit at the foot of the case list grouped by finding, and **every one of the 24 behaved the wrong way before the fix**, measured by running them against the old hook first. Each new case is the command that produced the finding rather than a tidied version of it.

The 39 existing cases are untouched and all still pass, including the three that exist to stop this wall becoming unusable: `publish_gate.py` itself, the reviewed-script register, and the register's exception dying the moment the file it excuses changes.

## One thing the wall did to me while I was fixing it, which is the wall working

**It refused my own commit message**, because the message quoted `wp post delete` and `wp db import` while explaining them. Ground A fired on the words. The message was shortened and the detail put in this file, which is where it belongs anyway. Recorded because it is the same class as finding 2 and it is the one case where the answer is not a code change: a commit message that quotes a verb is not a command that runs one, but the cost of teaching the wall that difference is higher than the cost of writing shorter subjects.

OWED BACK: nothing. Item 3 of the S092 ASK is closed with this, and the takedown half of that ASK was already closed at S092 by the `--takedown` mode. **For The Harness:** Layer 2's H9 entry gains a line naming the four, if you keep a change history for the hooks there.

*No em or en dashes in this file; checked before writing.*
