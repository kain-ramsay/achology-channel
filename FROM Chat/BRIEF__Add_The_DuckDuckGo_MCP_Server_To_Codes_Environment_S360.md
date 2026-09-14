# BRIEF: add the DuckDuckGo MCP server to Code's environment, free, no key

**From:** Claude Chat, Session 360. **Date:** Monday 14 September 2026.
**For:** Claude Code.
**Authority:** Kain, live in chat, evaluating Code's lack of web access after the S359 Amazon-data workaround. Tool evaluation recorded in `tools-and-integrations` (the project's tool registry).
**Read this cold.**

---

## 1. The problem this closes

Code currently has no route to the live web. Last session that meant asking Code to hunt for free GitHub tools just to get real Amazon search data, rather than simply looking it up (`BRIEF__Get_Real_Amazon_Search_Data_For_TULCH_Keywords_And_Categories_S359.md`, still in your tray). This brief gives Code a direct, standing search route so that kind of workaround stops being necessary.

## 2. What to install

`duckduckgo-mcp-server` (GitHub: nickclyde/duckduckgo-mcp-server, MIT licence). No API key, no account, no cost. Two tools: `search` (DuckDuckGo web search, titles/URLs/descriptions, configurable result count and region) and `fetch_content` (fetch a URL, return cleaned page text).

Add it to Code's MCP configuration the normal way for a new server on your machine. Confirm it loads and both tools are callable before reporting back.

## 3. What it is not

This is not a replacement for the harness, the channel, or the signed-spec model. It is a fact-lookup tool: current documentation, a plugin's current version, whether a claim is still true, what a page online actually says right now. It is not licence to make independent design, content, or scope calls from what it finds; those stay Chat and Kain's, per standing rule 19, exactly as before. Use it the way Chat uses its own search: to gather facts, not to decide things.

## 4. Its known limits, so a rough patch isn't mistaken for a broken install

It scrapes DuckDuckGo's own pages rather than calling an official API, so occasional rate-limit errors (HTTP 429) are a known, common behaviour of this server, not necessarily a sign something is wrong. If it starts failing repeatedly on real work, name it plainly rather than working around it silently; that is the signal a paid option (Perplexity's research-grade MCP was the alternative considered and set aside for now) might be worth revisiting for research-heavy tasks specifically.

## 5. Proving it works

Once installed, run one real test: the kind of query the S359 Amazon brief needed (a real search returning current, checkable results), and report what came back. That is the proof this closes the gap, not just that the server loads.

---

OWED BACK: confirmation it is installed and both tools respond, plus the one test query and what it returned.

*No em or en dashes in this file; checked before writing.*
