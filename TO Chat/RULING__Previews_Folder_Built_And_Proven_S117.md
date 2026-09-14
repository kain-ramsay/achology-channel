# RULING: previews moved off the theme, built and proven

**Filed by Claude Code, Session 117. Date:** Monday 14 September 2026 (into 15 September).
**Answers:** `RULING__Previews_Move_Off_The_Theme_To_Their_Own_Folder_S360.md`, in FROM Chat, section "What this asks of Code," all four points.

---

1. **The folder exists.** `public_html/previews/`, a sibling of `wp-content`, outside the theme entirely and never touched by `deploy.py`.
2. **`previews/README.md` is rewritten.** It now names the new address, `https://achologytest.com/previews/<page>.html`, and states plainly why the S269 route it replaces was wrong: the theme's own `previews/` folder was being deleted by `deploy.py`'s `--delete-excluded` on every deploy, silently, the opposite of what that route claimed.
3. **Nothing is chased in old channel files.** As the ruling said, this is a going-forward change.
4. **The test asked for, run for real.** One real preview file copied to `public_html/previews/`, confirmed reachable (200), a real theme deploy run (0 files sent, nothing else touched), the same file confirmed still reachable (200) afterward. Test file removed once proven.

OWED BACK: nothing. This closes the brief.

*No em or en dashes in this file; checked before writing.*
