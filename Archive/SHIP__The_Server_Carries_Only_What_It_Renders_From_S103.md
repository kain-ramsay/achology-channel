# SHIP: the server carries only what it renders from, and the reviews export has left it

**From:** Claude Code, Session 103, theme session. **Date:** 5 September 2026.
**Shipped:** theme v0.167.28, deployed with its three proofs.
**Closes:** two theme queue lines, both from the Codex audit: the runtime-only deploy, and the reviews dataset out of the theme. They shipped together because the second cannot be done without the first.
**Board card:** the Codex theme audit.

---

## What was actually on the server, measured before the change

Seven files that a web server has no use for, and one of them matters:

`data/reviews.csv.php`, 2.1MB, about 4,500 real students' reviews with their names, sitting inside the public web root behind a PHP exit guard and an `.htaccess`. Not exposed today, because SiteGround honours the `.htaccess`. Two thin defences on personal data, on a theme whose next home takes card payments.

The other six: `README.md`, `DESIGN-RULES.md`, `component_gate_waivers.md`, two folder readmes and `.gitignore`.

## What changed

**The exclude list is an allowlist now.** It was a denylist, which is why the audit found anything at all: a denylist only ever names the wrongs somebody already noticed, and it says nothing about the next file type nobody thought of. The question is turned around. Nothing reaches the server unless it is a template, a stylesheet, a script, a picture, a font, an ACF group definition, the course data the templates read, or an `.htaccess`. 609 of 701 files.

**The rsync filter is generated from the allowlist rather than written beside it.** One function answers "does this belong on a web server", and the filter, the proof and the test all call it. That is deliberate: at S093 the filter and the proof disagreed and the proof printed "identical, nothing left to send" while every file the change was about sat untouched on the server.

**The reviews export reads from above the web root.** `dirname( ABSPATH ) . '/achology-data/'`, with `ACHOLOGY_REVIEW_CSV` in wp-config.php as an override for a host laid out differently. It was copied there before the deploy removed it, and the copy was read back at its absolute path. The theme copy stays as the fallback, which is what keeps a local build working with no setup; on a deployed site there is nothing to fall back to.

The export is still in the theme folder, in git and in the zip. That was never the exposure and the file's own header explains why the working copy stays.

**There is a test, `deploy_runtime_acceptance.py`.** It goes red on a `.py`, `.md`, `.sh`, a `harness/` or `tools/` path and on the reviews export, and it also asserts that real templates are still accepted, so a function that simply refused everything would fail it too. With `--server` it reads the deployed theme rather than the local filter.

**Run against the server before this deploy, it failed and named all seven strays. Run after, it passes on 609 files.** That is the proof it can go red, which this project has learned to ask for.

## One correction to my own S102 assessment

That assessment said the zip should be built from the runtime set too. **It should not, and I have not.** CLAUDE.md makes the zip the working copy that exists outside git on a machine with no backup, and the zip never reaches a web server. Stripping the tooling out of the one off-git copy would trade a real safeguard for nothing. The line in the assessment was wrong; this is the correction, and the queue line is struck on that basis.

## Proofs

Deploy: three proofs green, local and server and zip agreeing, server reporting 0.167.28.
Acceptance test with `--server`: 609 files read, nothing refused present.
The site answers: home, /reviews/ and a book note all 200. The export's address returns 403.

---

OWED BACK: nothing, unless you want the zip decision recorded differently, in which case say so and it becomes a queue line of its own.

*No em or en dashes in this file; checked before writing.*
