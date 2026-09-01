# THE HARNESS

**Version 3.8, S318. Authority: Kain Ramsay.**

**Read by Claude Code at the open of every Code session, after The Shared Rules and before any work.**
**Checked by Kain by viewing the rendered pages Code returns.**

**The Shared Rules come first.** `000__THE_SHARED_RULES.md` at this root holds every rule binding Chat, Code and Cowork alike. This document holds only Code's own conduct. Where a rule below points at the shared file, the shared file is the rule and this is the pointer; the rule is not written twice.

This document is the complete set of constraints around Claude Code's work on Achology.com. Its purpose, in Kain's words: work and deliver code and pages to the standard that has been defined. Nothing else. No guessing. No made up facts. Where no specification exists, stop and ask.

It has three layers. Layer 1 is the rules: what Code must do. Layer 2 is the hooks: small tripwire scripts on Code's own machine that enforce the key rules mechanically, on every action, whether Code remembers them or not. Layer 3 is the evaluator: a separate, fresh pair of eyes that grades every built page against its signed spec before Kain ever sees it, because an AI grading its own work praises it.

Nothing in this document is open to interpretation. Where a rule seems to have a gap, the gap is a question for Kain, never a judgement call.

## Version history

One line per version. The reasoning behind each change lives in the handovers, the session reports and the vault, which are the records built to hold it.

- **3.8, S318.** H9 widened to cover taking a live page down, built and accepted at Code's S087 on Kain's S317 ruling, and its third ground corrected in the same pass so a read verb in front of an unreadable payload no longer disarms it. Nothing added and nothing removed; a hook was tightened.
- **3.7, S317.** H9, the publishing wall, added to Layer 2, built and accepted at Code's S087 on Kain's ruling given in session. Nothing else changed; the growth governor is met because H9 is a hook, not a rule, and it mechanises Rule 6 and Rule 8 where they already reached publishing in words only.
- **3.6, S311.** H8, the inbox wall, added to Layer 2, built and accepted at Code's S085, and named H8 because H7 was already taken by `h7_no_unanalysable_shell.py` and rule numbers are never reused (recorded S327 on Code's S091 acceptance printout, Kain's approval). Rule 4's component precedence and Rule 5's check-first paragraph moved to The Shared Rules (sections 4 and 3) and kept as pointers. Version history cut to one line per version. Every count of rules removed from prose, since Rule 10 is retired and a number in prose goes stale the moment the thing it counts moves. H6's tidy tax recorded as a named open finding.
- **3.5, S306.** Rule 3 tightened with the derived-artefact check, after a video replacement silently orphaned 923 transcript files.
- **3.4, S294.** Rule 1's opening read scoped to the live stream while a stream ruling stands, with every unopened file named.
- **3.3, S267.** Rule 8's page-creation boundary moved from a prohibition to an enumeration: only the pages a signed specification names, as drafts, counted and listed back.
- **3.2, S267.** Rule 13's session report assembled from the version control log rather than from recall, with hand-added lines marked.
- **3.1, S266.** Rule 13 gained the session report itself, closing the reporting void where finished work never reached the board.
- **3.0, S264.** Rule 6 and hook H5 tightened so a page cannot be called done without its complete DSRD 6 record; the intake refusal of a spec carrying no PAGE GATE line added.
- **2.9, S258.** Rule 14 gained the fold-back: a Safari approval writes the prototype's next version and its build sheet, not only a RULING file.
- **2.8, S257.** Rule 10 retired (the status line nobody read); pushing to origin folded into Rule 9; Rule 4 gained the component case.
- **2.7, S255.** The start-minimal-and-tighten instruction withdrawn; the uncertainty standard homed inside Rule 5; the rule count removed from H1.
- **2.6, S244.** Rule 13 (close the channel) and Rule 14 (a ruling in session is authority, filed the same session) added.
- **2.5, S243.** Rule 8 gained the content boundary: Code drafts no published words.
- **2.4, S242.** Rule 12 added: Code deploys over SSH and Kain never uploads.
- **2.3, S235.** Rule 11 added: look for a maintained public project before building, and outside code is Kain's decision.
- **2.2, S229.** H6 version 2 ruled live. **2.1, S228:** H6 widened to fire on a modified file, not only a new one. **2, S228:** the four install seams closed. **1, S227:** approved and installed.

---

## LAYER 1: THE RULES

Rule numbers are never reused. A retired rule keeps its number with its retirement recorded, so every reference to a rule number anywhere in the project keeps pointing where it did.

### Rule 1. Open every session the same way
First acts, before any work: read The Shared Rules, read every file in FROM Chat, and read this document whole. The first message of the session states all three in its first line. A session that opens without this line is a broken session.

**While a stream ruling is in force, the read is scoped to that stream (ruled by Kain in the S074 sitting).** A stream ruling is Kain naming one body of work as the only work until it is delivered. While one stands: read this document in full, read the FROM Chat files that sit inside the live stream in full, and list every other file by name without opening it. The opening line still states that both the channel and the harness have been read, and it also names the stream and the count of files left unopened.

**Three things this does not weaken.** Nothing is skipped silently, because every unopened file is named, so an omission is visible rather than invisible. A file arriving inside the live stream is read in full, always: the scoping is by stream, never by size or convenience. And the moment a stream ruling lifts, the whole backlog is read at the next open. Parked work is deferred, never dropped, and Rule 13's archiving obligation is untouched.

**Where no stream ruling is in force, this paragraph does not apply** and the rule runs exactly as written above.

**Why it was ruled.** Measured at the S074 open: FROM Chat held 27 files totalling 137KB, of which three files and 14KB were inside the live video stream. The other 123KB was component and chrome work parked under Kain's own video-only ruling, and it had been read in full at every session open since that ruling was given. The read bought nothing while the parked work could not be acted on, and it consumed the context the actual work needed.

### Rule 2. Declare scope before touching anything
Before any change, write the declaration into the session, as its own message sent before any edit begins, in this exact shape:

> SCOPE: {one page or one named job} | FILES: {every file this change may touch, listed as bare paths} | SPEC: {the DSRD sections and the signed spec that govern it}

No declaration, no edit. A file not named in the declaration is out of scope, and touching it is a violation regardless of how useful the touch would be. The declaration must be its own message because the scope wall reads the transcript, and a declaration written in the same message as the edit is invisible to it.

### Rule 3. One page, or one named job, per change set
A change set covers one page, or one named non-page job declared under Rule 2. Work that would touch more than one page is a sweep, and a sweep runs only under a signed sweep brief from Kain, arrived through FROM Chat, naming the pages or bodies of work it covers. There is no other route to a sweep. "While I am in here anyway" is the exact failure this rule exists to stop.

**Before a sweep that bulk-replaces files or content runs:** the brief names everything derived from what is being replaced, checked against it or at minimum listed, before the replacement runs rather than discovered after. A video replacement's derived artefacts include its transcripts and captions; a content-record replacement's include anything that cross-links to it; the brief names the actual derived set for the case at hand. Ruled after the S305 finding that replacing 2,146 course videos silently orphaned 923 transcript files with nothing reporting it, the second time that exact failure has cost a rebuild.

### Rule 4. Quote the spec, never cite it
Any claim about a standard carries the governing sentence copied word for word from the DSRD, read from the canonical file that turn, with its section number. A claim without its quoted sentence is a guess and is treated as one. What counts as a source, and what does not, is The Shared Rules, section 2.

**The component case, and where a component's standard lives, is The Shared Rules, section 4.** Precedence runs prototype, then build sheet, then code, and the lower one is corrected rather than negotiated with. What this rule adds for Code alone: a claim about a component's values carries the row copied from its build sheet, and a claim about what the component looks like is settled against the approved prototype. No value is ever read from the code as though the code were the standard.

### Rule 5. No spec means stop and ask
**The rule itself, including the obligation to look before the question travels, is The Shared Rules, section 3.**

What this rule adds for Code alone: the mechanics. Write the question as a file into TO Chat, mark the item "waiting on ruling", and continue with other declared work. Stopping costs one file. Deciding costs a rebuild.

**What the shared rule does not soften.** A genuine specification gap still stops the work, and a decision that turns on what Kain wants, knows or owns still goes to him whole. The standard governs the questions that were never his, not the ones that are.

### Rule 6. "Done" is banned without proof
The word "done" may only appear with two things attached: the machine gate printout for the work, and a link to the rendered page Kain can open in Safari. **For a page, a third thing: the page's DSRD 6 record, complete, with every chapter line reading pass or recorded exception, and Code's own lines in it limited to the machine chapters.** Work changed but not yet verified is reported as "changed, not verified", in those exact words. Work verified in one place of three is reported as "verified 1 of 3", never as done. A page whose record still carries a fail or a not-run line is reported as "built, gate open: {the open chapters named}", never as done.

### Rule 7. Show pages, never measurements
Every visual result returns to Kain as a rendered page viewed in Safari. Measurements, values, tables and descriptions are never a substitute. If a page cannot be rendered, the work waits until it can.

### Rule 8. The hard boundaries
Code never edits a DSRD (corrections travel to Chat as instruction files). **Code creates a WordPress page only from an enumeration in a signed specification: each page named by its title, its address, its parent and its template, created as a draft, never published, with the count and the full list reported back. A page created that the specification does not name is a harness break, and so is a page the specification names that does not appear. Where the specification's own list is incomplete or ambiguous, that is a stop-and-ask under Rule 5, never a judgement.** Outside that route, pages are Kain's alone. Code never mirrors a DSRD anywhere. Code never critiques work Kain has designed and approved. Code never redesigns what he was asked to reuse. Code never drafts content: page copy, article bodies, blurbs, metadata text, and every other published word arrive written and approved through FROM Chat, and content drafting routes to Chat and Cowork, never to Code. **A canonical name copied from DSRD 5 is not drafting; it is standing rule 1 being obeyed, and the copied value is quoted in the report so it can be checked.** Code never edits this document or The Shared Rules.

### Rule 9. Commit and push before and after every change set
One git commit immediately before a change set begins, one immediately after it passes its gates, and a push to origin with each. The repo is never more than one change set behind the theme on disk, and origin is never behind the local repo. This makes "what changed and when" answerable again, permanently, from a copy that survives the machine.

### Rule 10. Retired, S257: the status line is not read
The fixed status line that ended every Code message is withdrawn. Kain ruled at S052, asked directly whether he reads it: he does not, and told Code to drop it. A receipt nobody reads enforces nothing; it costs a line in every message and detects only its own absence.

What Kain actually reads is the rendered page (Rule 7) and, where the work is not a page, the proof Rule 6 requires. What actually enforces the rules is Layer 2, the hooks, which fire whether or not Code remembers anything, and Layer 3, the independent evaluator. Those are unchanged and unweakened by this retirement.

### Rule 11. Look before you build
Before building anything from scratch that is not specific to Achology, search for a maintained public project that already does it, and report in one line what was found and whether it is being used. Reading an outside project for its approach is always allowed and is encouraged. Putting outside code into the theme is never Code's decision: it travels to Kain as a question through TO Chat first, every time, with no exception for small, obvious or trivially small pieces. The reason is not effort, it is that Achology.com takes card payments, so admitting outside code is a security decision and security decisions are Kain's.

### Rule 12. Code deploys; Kain never uploads
When a change set has passed its gates and its closing commit (Rule 9), Code deploys the theme to the server himself over SSH, purges the cache, and returns the rendered live page link (Rules 6 and 7). Kain never uploads a theme zip, and a message asking him to upload anything is a harness break. Deployment is part of the change set, never a separate step waiting on a human courier. If SSH access to where the theme lives is ever missing or refused, that is a stop-and-ask through TO Chat (Rule 5), never a fallback to a Kain upload.

### Rule 13. Close the channel at session end, and report what the session finished
Before the session's last message, archive every FROM Chat file whose work is fully executed and verified this session or earlier. Only live instructions stay. The last message states how many files remain in FROM Chat and why each one stays. FROM Chat is Code's side of the road to empty, exactly as TO Chat is Chat's: a consumed instruction left sitting live is how a shipped page's spec stayed on the road as a live instruction for weeks, indistinguishable from work still owed. **Since Version 3.6 this is enforced mechanically by H8**, which refuses the close while any file that was in FROM Chat at the open carries no disposition line, and archives by machine every file head-lined DONE.

**The session report.** The same closing act writes one file into TO Chat, `SESSION_REPORT__S{nnn}.md`, listing every piece of work the session finished. One line per piece: what was finished, and the Notion board card it touches, named in words. Work that was started and not finished is listed the same way and marked not finished, in those words, with what remains. Work Kain asked for directly in the sitting is listed exactly like commissioned work, because that is the work most likely to go unrecorded: it never travelled the channel on the way in, so the report is its only route out.

**Where the report's content comes from.** The report is assembled from the version control log for the session, never from recall. Rule 9 already commits before and after every change set and pushes to origin, so the log is a machine written record of what happened and when. Code reads the log for the session, turns each change set into one line, and adds the board card it touches. Work that touched no file in the repository, such as images, spreadsheets, or anything worked by hand with Kain in the sitting, has no machine record: those lines are added by hand and marked as hand added, so a reader can tell which lines rest on the log and which rest on memory. **The test, so this is a rule and not a preference: a finished change set that appears in the log and not in the report is a harness break.** A session that ended without a report is recovered the same way, by reading its log, rather than treated as lost.

**Why this exists.** Chat holds the Notion board, and Chat learns only what the channel carries. At S055 Code and Kain worked the 108 unresolved book covers by hand and the channel said nothing, so the board still showed the job outstanding and Chat was one turn from asking Karen to redo it. A session that finishes work and files no report is a harness break on the same terms as an unfiled ruling: the work is live in the build and absent from the record, which is the drift every harness in this project exists to prevent.

**What it is not.** Not a narrative of the session, not a report of intentions, and not a second copy of anything already filed. A piece of work with its own REPORT or RULING file in TO Chat gets one line naming that file, never a summary of it. The report is an index for the board, and it stays that.

### Rule 14. A ruling from Kain in session is authority, and is filed the same session
When Kain gives a ruling directly in a Code session, Code acts on it: his word is the project's highest authority and waiting for a brief to repeat what he just said serves nobody. The obligation is the record: the ruling is filed to TO Chat as a RULING file in the same session, quoting Kain's words, so Chat writes it into the owning document. A ruling acted on but not filed is a harness break, because a ruling live in the build and absent from its owning document is the drift this project's harnesses exist to prevent.

**The fold-back.** Where the ruling approves how a component looks on the rendered live page, the record is not only the RULING file: whoever rendered the approved artefact writes the signed record, and here that is Code. In the same session, Code exports the approved state into that component's design folder as the prototype's next version, updates the build sheet to match it, and the RULING file names both writes. The Rule 4 chain then always has its top: prototype wins, sheet matches prototype, code matches sheet, whichever surface the ruling happened on. A Safari approval left as a RULING file with no prototype version behind it is the same harness break as an unfiled ruling.

---

## THE STATUS LINE: RETIRED (S257)

Code's messages no longer end with a status line. Kain ruled at S052 that he does not read it, so it was dropped at source; this document records the retirement rather than keeping a format nobody consumes.

What replaces it is what was doing the work all along: the rendered page link Rule 7 requires, the proof Rule 6 requires where there is no page, and the hooks that enforce the rules mechanically. A missing page link or an unproved "done" is still a harness break, on the same terms as before.

---

## LAYER 2: THE HOOKS (mechanical enforcement)

Hooks are a built-in Claude Code feature: scripts that run automatically at fixed points in Code's working cycle. A blocking hook stops the action regardless of what Code intended or believed. They exist because three of Code's own named failure modes cannot be fixed by rules alone: he cannot tell his recall from his invention, long sessions erode rules held in his head, and skipping a check costs him nothing in the moment. A hook fires on action one thousand exactly as on action one, and makes the skipped check fail instantly.

Code builds these hooks himself, in the theme repository, to this specification. Each has an acceptance test: Code deliberately breaks the rule and files the printout of the hook blocking him. H1 to H5 were built and verified at S228.

**H1. Session open (SessionStart hook).** At every session start, automatically prints into Code's context: this document's rules, and the live contents of both channel folders. The rules can no longer fade or be forgotten, because they arrive fresh every session without anyone remembering to load them. It also writes `channel_seen`, the signature of FROM Chat at the open, which H6 and H8 both read.
*Acceptance test: open a session, show the rules and channel list arrived unprompted. Verified S228.*

**H2. Scope wall (PreToolUse hook on every file edit).** Before any file edit, checks the target file against the declared scope list for the session. No declaration on record: the edit is blocked. File not on the declared list: the edit is blocked, with the reason written back to Code. A declaration whose fields still carry braces is the template, not a declaration, and is ignored. This is the mechanical end of Rules 2 and 3: sweeps become physically impossible without a signed brief.
*Acceptance test: attempt one edit with no declaration, and one edit to an undeclared file; show both blocked. Verified S228.*

**H3. Forbidden ground (PreToolUse hook on file paths).** Blocks outright, in every mode, any write to the DSRD folder, any write path that would mirror a DSRD, and any write to this document or The Shared Rules. The Rule 8 boundaries stop depending on Code's restraint. Runs before H2, so a forbidden path is refused before any scope question is asked.
*Acceptance test: attempt a write into the DSRD folder; show it blocked. Verified S228.*

**H4. Automatic gates (PostToolUse hook).** After edits, runs the existing gate scripts against the changed files automatically: css_gate for stylesheets, article_gate for article content, the dash check (U+2014 and U+2013) on the text the edit introduced. Failures are fed straight back to Code as feedback in the moment, not discovered by Kain hours later.
*Acceptance test: introduce one deliberate gate failure; show the hook catching it immediately. Verified S228.*

**H5. The completion gate (Stop hook).** When Code moves to finish a piece of work, checks whether the gates have run clean since the last edit. If not, finishing is blocked with the reason. The word "done" becomes mechanically impossible without the proof Rule 6 requires. **Where the finished work is a page, H5 opens that page's `DSRD6_RECORD.md`. A turn that calls the page finished while the record is missing or open is refused. Every other turn passes, with the open chapters named in Rule 6's own words: "built, gate open: {the open chapters}". The naming is unconditional, so an open record is never passed in silence.** An earlier wording refused the turn rather than the claim, and because a Stop hook fires at the end of every turn, no session could close once a page template had been edited. Kain's words, S055: "Narrow it so it refuses only a page being declared done." Seven acceptance cases pass in both directions, including the one that makes the rest mean anything: a fully closed record allows a page to be called done.
*Acceptance test: edit a file, attempt to finish without running gates; show the finish blocked. Verified S228, and again for the DSRD 6 strengthening.*

**H6. The mid-session message wall (PreToolUse hook).** Before each edit, compares the FROM Chat folder against what was read at session open. If a file is new or has been modified since the open, the edit is blocked until that file is read. This closes the gap that caused the 249 rewrite to outrun its governing instructions: a message from Chat can never again arrive or change unseen while work is moving.
*Acceptance test: add a file to FROM Chat mid-session, attempt an edit; show the edit blocked until the file is read. Built and verified S228; ruled live by Kain, S229.*

**H6's tidy tax, a named open finding (Code's S085, recorded here rather than left to be rediscovered).** H6 cannot tell Code's own write to FROM Chat from Chat's. Head-lining files during a channel tidy makes every one of them look like a mid-session message, so H6 blocks the next edit until each is read again. The tidy is the one job that edits FROM Chat, so this fires on precisely the work Chat commissions. Nothing is lost by it and the re-read is honest, but every tidy pays the tax. The fix is one condition in H6's marking, that a FROM Chat file Code himself just wrote is marked read by that write. **Deliberately not built at S085**, because H6 is a live safety hook and changing one at the end of a long session, outside a declared scope for it, is how a gate quietly stops gating. It is built under its own declared scope, not folded into another job.

**H7. The unanalysable shell guard.** Live, and holds that number. Named here so nobody renumbers it.

**H8. The inbox wall (Stop hook, beside H5). Built and accepted at Code's S085; ruled the same by Kain at S310.** Every file that was sitting in FROM Chat when the session opened must carry a disposition line as its first line. No line, no close, and the offending file is named. A line reading DONE moves the file to Archive by machine, so Rule 13's archiving stops depending on anybody remembering it. **What counts as older than the session is H1's `channel_seen` record, not a timestamp**, so H6 and H8 cannot come to different views of when the session began; a file that arrived mid-session is H6's business and is not held to this wall.

**The owed-line check, and the correction Code made to the brief.** The brief proposed matching an answer to its question by the source file's session number and prefix. That match is not merely loose, it is wrong, and it would have failed on the first healthy case it met: a readback carries Code's session number rather than Chat's, and its prefix is REPLY rather than ASK. A check that goes red on the healthy case teaches everyone to switch it off. **The tighter match, built instead: the disposition line names its answering file, and the hook checks that file exists** in TO Chat or in any archive. The check fires only where the source file's OWED BACK line names something owed back, so a file written before that convention, and a file owing nothing, are not held to it. The brief itself asked for exactly this correction where the proposed match was unreliable, and Code was right to make it.

**It was commissioned as H7 and built as H8** because `h7_no_unanalysable_shell.py` already holds that name and fired eleven times during the same session. Renumbering a live hook to free a name has no upside and a real chance of breaking the launcher.
*Acceptance: ten cases green in `harness/h8_inbox_wall_acceptance.py`, run against a temporary tree rather than the live channel, deliberately, because a regression test that moves real files archives live instructions whenever anyone runs it. Live-fired once on the real channel as well, blocking on a real file with its head line removed (exit code 2), archiving it once head-lined DONE, and reading clear on the restored channel.*

**H9. The publishing wall (PreToolUse hook on the shell, beside H7). Built and accepted at Code's S087; ruled by Kain in the S086 sitting and restated at the S087 open, filed under Rule 14.** Publishing touches no file, so until this hook nothing watched it, and 116 pages went live at S086 unchecked. H9 refuses any command from Code that could put content in front of the public unless the command names a live clearance minted by `publish_gate.py`, and a clearance is minted only where every named page passed the machine third of DSRD 6 and its record carried no failing line. A clearance expires after forty five minutes and is spent by the first command that uses it, so one can never quietly cover a second batch.

**Its governing principle, in Kain's words: "I could not tell" is a fail, never a pass.** The wall refuses on three grounds: an explicit publishing verb; a project script capable of publishing, worked out by reading the scripts rather than from a list somebody keeps; and a command that reaches the install and cannot be statically read. The third is the widest and the one that matters, because a shell command can hide its verb behind a substitution, a pipe or a script.

**It cannot reach Kain, by construction rather than by rule.** It is a hook on Claude Code's own shell. Kain publishes in the WordPress admin in his own browser, and nothing in that path passes through any hook.

**DSRD 6 section 0's volume rule is read, not invented.** A batch clears under `--exemplar`, naming the page type's signed exemplar whose own record carries its human chapters closed; without that flag every page's own record must be closed in full. The five page spot check is drawn and printed with a seed written into the clearance, not enforced, because a human read is a human read.

**The reviewed exception register.** Three measurement scripts reach the install through `wp eval` and are permitted as reads, each recorded in `harness/h9_reviewed_scripts.json` with its reason bound to the sha256 of the exact bytes that were read. Edit one character and the exception dies, and that expiry is itself an acceptance case.

**Taking a live page down is covered on the same terms as publishing (ruled by Kain at S317, built at Code's S087).** The wall refuses any command from Code that would take a live page out of public view: a post deleted or trashed, a post status set to draft, pending, private or trash, the theme's own delete and trash functions, or a delete against the posts table. Same clearance, minted, expiring and spent the same way. Filtering a list by draft status is a read and passes, because the wall reads what a command does rather than the words it contains, exactly as it already does for the publish status.

**The third ground asks only its own question.** Until Code's S087 the unreadable-payload check stood down whenever a read verb appeared anywhere in the command, so a harmless read at the front could carry any payload behind it through the wall. Found by Code hitting the wall in ordinary work rather than by review. Now the ground asks only whether the command reaches the install and can be read; a genuine read has no substitution, no heredoc and no pipe into a shell, so it passes on its own merits and never on an exemption.
*Acceptance: thirty seven cases green in `harness/h9_publishing_wall_acceptance.py`, run against a temporary clearance store rather than the live one, deliberately, because a regression test that spends real clearances damages the thing it tests every time anybody runs it. Seven of the cases exist because the first version of the wall got them wrong, every one by being too wide, and all seven were found within ten minutes of going live. Six more were added for the widening and the corrected third ground, and one proves a reviewed exception dies when its file changes.*

The gate scripts (css_gate, page_gate, article_gate) run themselves through these hooks. What a gate script checks changes only under a commissioned brief from Chat through FROM Chat, never as Code's own idea.

---

## LAYER 3: THE EVALUATOR (independent grading)

Anthropic's own engineering finding, and the reason this layer exists: an AI asked to evaluate its own work confidently praises it, even when the quality is obviously poor to a human. The builder and the grader must therefore never be the same mind that just did the work.

**During the build.** After building a page, Code hands the rendered page and the signed spec, and nothing else, to a fresh evaluator agent that had no part in building. The evaluator grades against the concrete checklist below and returns its findings. Code fixes and resubmits, up to three rounds. Still failing after three: work stops and the failure comes to Chat as a question.

**At intake, before anything is built.** The requirement, stated as an outcome: a signed spec or brief without its PAGE GATE line at its foot (the printed proof Chat's page-design-brief route ran before signing) is mechanically unbuildable, refused before any edit lands, with the refusal returned through TO Chat naming the missing line. The evaluator's intake is one layer of this check and must not be the only one; where the tripwire finally lives in Code's machinery is Code's call, and this document records the placement when his reply names it. Specs signed before S264 predate the line and are exempt by date; non-page jobs carry no spec foot and are out of scope.

**At the return.** When the rendered page travels back through TO Chat, Chat reviews it against the signed spec, chapter by chapter, before Kain views it. Kain's eye stays the final gate, but it is never the first one.

**The evaluator's checklist, graded one by one, never as an overall impression:**
1. Every block the signed spec names is present, in the spec's order, with nothing present the spec does not name.
2. The copy matches the signed spec word for word.
3. Every link resolves, to the exact URL the spec names.
4. The DSRD 6 chapters, each reported pass, fail, or recorded exception, read from the page's `DSRD6_RECORD.md`, never asserted without it.
5. Zero em dashes and zero en dashes anywhere.
6. The page gate printout attached and clean.

---

## SETUP: WHO DOES WHAT (Kain does nothing technical)

1. **Kain:** approved the harness, S227. His ongoing role is viewing the rendered pages Code returns; he never audits code and never needs to.
2. **Chat:** wrote this document to the channel folder root, commissioned the install, and verified the acceptance printouts.
3. **Code:** built the hooks, proved each by breaking its rule, and filed the printouts.
4. **Layer 3** fires on page work.
5. Build work runs only while the harness is live and verified.

---

## WHEN THE HARNESS BREAKS

A hook bypassed, a rule broken, an unproved claim of "done", or a change set returned without its rendered page fires the problem-interrupt: work stops, the break is defined, and the fix is written into this document before work resumes. The harness is never patched in conversation; it is versioned here.

**How a break is closed is decided, never assumed.** The growth governor (The Shared Rules, section 9) governs every harness in this project: a rule enters only as another leaves, only with a test someone else could check, and never to govern the shape of a message. Removing a rule, tightening one that already exists, strengthening a hook, or fixing the thing a rule was compensating for are all closures, and the first three cost nothing to carry. Where nothing can be retired, that is the signal the failure needs a fix somewhere other than a rule.

*The earlier instruction here read "start minimal, and tighten on every miss". It is withdrawn. Across 252 sessions that instruction, sitting in three harnesses at once, produced a one-way accumulation until satisfying the obligations had become the work.*

**This document lives in exactly one place: `000__THE_HARNESS.md` at the channel folder root. It is never mirrored. Changes to it are made by Chat, with Kain's approval, versioned inside the document itself, and delivered whole.**

*No em or en dashes in this file; checked before writing.*

*End of The Harness, Version 3.8.*
