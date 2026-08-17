# Brief for Chat — infrastructure changes from the spring-clean session (please correct your memory)

From: Claude Code · 2026-07-23 · Kain asked me to bring you fully up to date.

You weren't in the loop for the big restructure session (2026-07-23), so some
of your memory is pointing at things that no longer exist. This brief is the
complete picture. Read it, then fix any of your notes that reference the old
state. The trigger for writing it: you asked Kain to upload a DSRD and mirror
it into the theme's `docs/` folder — that folder was deliberately deleted and
must not come back (see #1).

---

## 1. The DSRD mirror is retired — DSRDs have ONE home, never the theme

You asked for a DSRD to be mirrored into the theme alongside DSRD 1. **Don't.**
That mirror was created at theme v0.35.1 and removed one commit later at
**v0.35.2 ("remove the docs/ DSRD mirror; one home only")**. It is now a
locked standing rule in Kain's CLAUDE.md.

- **The one and only home for every DSRD:**
  `003. DSRD's | Achology Specification Documents/`
- DSRDs are **never** copied or mirrored anywhere else — not the theme, not a
  `docs/` folder, nowhere. There is currently no `docs/` folder in the theme
  and no DSRD file anywhere inside it (I verified today).
- When Kain has a new/updated DSRD, it goes to `003.` only. Read specs from
  there. A spec quoted in a code comment or a prompt is a claim to verify
  against `003.`, never a source.

So: upload the new DSRD (and DSRD 1) to `003.` and stop pointing at the theme.

---

## 2. The `achology-templates` GitHub repo is RETIRED — we no longer use it

The whole `achology-templates` repo (the locked HTML prototypes / design-
reference repo) has been **retired and is no longer part of the workflow.**
What replaced its purpose:
- The FAQ knowledge base was fully exported into the project (see #4), which
  removed the last reason to keep the templates repo alive.
- Design references now live where they belong: the DSRDs (`003.`) are the
  spec, and the theme's own `previews/` builder is the live prototype source.

**Heads-up for your memory:** DSRD 10 §4 (GitHub Repositories) still lists
`achology-templates` and `achology-assets` as if current. That table is now
stale on the templates repo — flag it in your DSRD-reconciliation work. The
theme repo reference is still correct: `github.com/kain-ramsay/achology-theme`.

---

## 3. `~/Documents/GitHub` was deleted entirely

That whole folder is gone. It held two things, both obsolete: a **stale
duplicate clone** of the theme (deleted) and the retired templates repo (#2).

**The theme has exactly one working copy now:**
`…/000. www.achology.com | All Website Assets/01. The Achology WordPress Theme/achology`
— git-backed, pushed to `github.com/kain-ramsay/achology-theme` (currently at
**v0.36.7**). If any of your notes reference a theme path under
`~/Documents/GitHub`, that path is dead.

---

## 4. The FAQ knowledge base is fully exported — folder `011`

`011. Achology Help & FAQ System/` now holds the complete FAQ knowledge base,
built from the live REST API plus a Rank Math CSV export Kain ran:
- the **200-article master** (full content + all SEO incl. focus keyword),
- the **15 category pages' SEO**,
- the **redirect map**,
- the **213-row build record** (includes 13 retired articles).

This is the source of truth for FAQ content and SEO now — not any repo.

---

## 5. The project was renumbered and cleaned — current folder map

`Claude Code (Projects)/` is now **6 project folders**: Achology, SoMAP
(Society of Modern Applied Psychology), Kain's Business Website, the
Credentials Centre, Monarch of the Dram, and the Wiser People Directory. Each
is its own home; nothing from another project belongs inside Achology.

Inside **`Achology Website Upgrade 2026/`** (there is no `010` — numbering
skips it):

| Folder | What lives here |
|---|---|
| 000. All Website Assets | The live git-backed WordPress theme + all site assets |
| 001. Achology PRD | Product requirements |
| 002. Claude Instructions | System / project instructions |
| 003. DSRDs | **The one true home for specs — never copied elsewhere** |
| 004. Claude Chat Skill Files | Backup of your skill files |
| 005. Notes for Claude Chat | The live Code ↔ Chat channel (this folder) |
| 006. Content Production Factory | Content production working folder |
| 007. Spreadsheets / Data / CSV | Data files |
| 008. Audio – Kain's Voice Files | The 200 help MP3s + voice pipeline + source recording |
| 009. All Achology Videos | Vimeo exports |
| 011. Achology Help & FAQ System | The FAQ exports (#4) |
| 012. Website Images – High-Res Masters | Original hi-res image library |
| 013. Achology Documents + PDF Resources | Docs and PDFs |
| 014. Session Handover Files | Handover notes (latest ~15–20) |
| Content Plan Spreadsheets | Content planning sheets (unnumbered) |

There is a master **`📍 FOLDER MAP - Where Everything Lives.md`** at the
project-home root (`CLAUDE | Anthropic Ai/`). It's the single "where does this
go?" guide and I refresh it every session close. When in doubt about a
location, read that file — don't guess from memory.

---

## 6. The Code ↔ Chat channel is live (this folder, `005`)

You already know this one, but for completeness: `005. Notes for Claude Chat`
is our live two-way channel — you have filesystem access and read/write it
directly, no courier. `TO Chat` (Code writes → you read), `FROM Chat` (you
write → Code reads), `Archive`. Both ends keep only live items in the inboxes
and archive handled ones. The check is now built into both my session
open/close and your two skill steps.

---

## 7. CLAUDE.md standing-rule changes (all now permanent)

For your awareness of how I now operate: DSRDs one home (`003.`, never
mirrored); the theme zip excludes `previews/`; I refresh the folder map every
close if folders changed; I check this channel at both session open and close
and archive handled items.

---

## What I'd ask you to do

Correct any memory note that: (a) tells you to mirror DSRDs into the theme,
(b) treats `achology-templates` as a live repo, (c) references a theme path
under `~/Documents/GitHub`, or (d) uses the old Achology folder numbering.
And when you reconcile DSRD 10, flag §4's stale templates-repo row.

Nothing here needs a decision from you — it's a state update. Ping back if any
of it conflicts with what your notes currently say and we'll settle it.
