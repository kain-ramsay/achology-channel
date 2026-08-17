"""Unwrap the three links that repeat the identical anchor words in one article.

Authority: Kain, direct instruction, 28 July 2026: "Yes, tidy up those duplicate
links too please claude!", given again after Chat was unavailable to file the
brief. Recorded verbatim in `REPORT__S229_Rulings_Carried_Out.md` section 5,
together with the harness seam it exposes.

Standard: `BRIEF__Internal_Links_Across_The_249_Help_Articles.md` rule 1: "First
mention only. Each target is linked once per article, at its first appearance.
Never twice."

Scope, and it is deliberately tiny. Of the 242 article-and-target pairs linked
more than once in the section:

  * 232 are the "Related questions" list at the foot of an article linking a page
    the body already mentions. That is what the list is for. Untouched.
  * 7 link the same page from two different phrases, which is ordinary prose
    linking and reads correctly. Untouched.
  * 3 repeat the identical anchor words. Those, and only those, are unwrapped.

The first link stays, the repeat loses its tags, and the words stay exactly as
they are. Nothing is added, removed or reordered.

Usage:
    python3 dedupe_repeats.py report      what would change, nothing written
    python3 dedupe_repeats.py write       write the results into batch/
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(BASE, "closing.json")

ANCHOR = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)
RELATED = "related question"


def body_end(html):
    """Where the Related questions list starts. Everything from there is that
    list's own linking and is out of scope."""
    i = html.lower().find(RELATED)
    return i if i >= 0 else len(html)


def repeats(html):
    """Anchors in the body that repeat both the same target and the same words."""
    cut = body_end(html)
    seen, out = {}, []
    for m in ANCHOR.finditer(html):
        if m.start() >= cut:
            break
        key = (m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip().lower())
        if key in seen:
            out.append(m)
        else:
            seen[key] = m
    return out


def run(write):
    live = json.load(open(LIVE))
    changed = []
    for art in live:
        html = art["content"]
        found = repeats(html)
        if not found:
            continue
        out = html
        for m in reversed(found):
            out = out[:m.start()] + m.group(2) + out[m.end():]
        changed.append((art, out, found))

    print("articles with an identical repeated link: %d" % len(changed))
    for art, out, found in changed:
        for m in found:
            words = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            print('   [%d] %-34s second "%s" unwrapped'
                  % (art["id"], m.group(1), words))
    if write:
        os.makedirs(os.path.join(BASE, "batch"), exist_ok=True)
        for art, out, _ in changed:
            io.open(os.path.join(BASE, "batch", "%d.html" % art["id"]),
                    "w", encoding="utf-8").write(out)
        print("\nwritten to batch/ for gating: %d files" % len(changed))
    return changed


if __name__ == "__main__":
    run(write=(len(sys.argv) > 1 and sys.argv[1] == "write"))
