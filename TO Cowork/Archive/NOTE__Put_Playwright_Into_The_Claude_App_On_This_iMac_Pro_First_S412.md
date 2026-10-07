# NOTE: put Playwright into the Claude app on this iMac Pro, before anything else (S412)

**From:** Claude Chat, S412, Wednesday 7 October 2026, on Kain's word: nothing else happens until this is done. **For:** Cowork, who runs on this iMac Pro, the same computer as Chat. **Run this first, before the diagram list and every other note in your tray.**

## Why

Chat needs its own browser on this computer so it can open pages on the build site by itself. Microsoft's Playwright MCP gives it one. Node.js v24.21.0 is installed on this Mac (Kain checked at S412; `/usr/local/bin/npx` should exist). Kain is not technical and must not be asked to edit anything.

## The job

1. Back up `~/Library/Application Support/Claude/claude_desktop_config.json` to the same folder as `claude_desktop_config.backup_S412.json`. If you cannot reach that folder, ask Kain for access to it in one plain line (he only clicks Allow), and nothing more.
2. Confirm `/usr/local/bin/npx` exists. If not, find where `npx` is and use that full path.
3. Add one top-level entry to the file, leaving every existing setting exactly as it is:

```
"mcpServers": {
  "playwright": {
    "command": "/usr/local/bin/npx",
    "args": ["-y", "@playwright/mcp@latest"]
  }
}
```

If an `mcpServers` entry already exists, add `playwright` inside it instead.

4. Check the file is still valid JSON. Read it back. If anything is wrong, restore the backup.
5. Tell Kain, in one line: "Done. Quit the Claude app with Command Q and open it again."
6. File a short DONE in FROM Cowork saying what you did and whether the file reads back valid. Then hold.

If you cannot do this at all from where you run, say so in one line in a DONE and stop. Do not ask Kain to do it.

*No em or en dashes in this file; checked before writing.*
