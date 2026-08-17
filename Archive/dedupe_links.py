"""Remove the duplicate links the S226 link map pass created on 28 July 2026.

The defect, stated plainly. The brief's rule 1: "First mention only. Each target
is linked once per article, at its first appearance. Never twice." Its rule 7:
"Leave existing links alone. This pass adds; it does not re-point."

`linkmap_pass.py` honoured rule 7 by masking the links already in an article, so
none was re-pointed. It then broke rule 1 by not counting them: where an article
already linked to a target, the pass added a second link to the same target. That
put 87 duplicate links across 65 articles.

The repair, and why this way round. Rule 7 protects the link that was already
there, so the original stays wherever it sits, and the one this session added is
unwrapped: the anchor tags come off and the words stay exactly as they were. The
pre-session snapshot decides which is which, so nothing is guessed.

Usage:
    python3 dedupe_links.py report      what would be unwrapped, nothing written
    python3 dedupe_links.py write       write the repaired bodies into batch/
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(BASE, "verify.json")
SNAPSHOT = os.environ.get(
    "PRE_SESSION_SNAPSHOT",
    "/private/tmp/claude-501/-Users-kainramsay-Documents-CLAUDE---Anthropic-Ai/"
    "991f1b49-7d86-454c-865d-63d552cd483d/scratchpad/cur249.json")

ANCHOR = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)


def counts(html):
    out = {}
    for m in ANCHOR.finditer(html):
        out[m.group(1)] = out.get(m.group(1), 0) + 1
    return out


def repair(html, pre_html, log):
    """Unwrap the surplus links this session added, target by target."""
    was, now = counts(pre_html), counts(html)
    surplus = {t: n - was.get(t, 0) for t, n in now.items()
               if n > 1 and was.get(t, 0) >= 1 and n > was.get(t, 0)}
    if not surplus:
        return html
    for target, extra in surplus.items():
        for _ in range(extra):
            spans = [m for m in ANCHOR.finditer(html) if m.group(1) == target]
            if len(spans) < 2:
                break
            # Prefer unwrapping an anchor whose exact HTML is not in the
            # pre-session body: that one is demonstrably this session's.
            pick = next((m for m in spans if m.group(0) not in pre_html), spans[-1])
            html = html[:pick.start()] + pick.group(2) + html[pick.end():]
            log.append("unwrapped a second link to " + target)
    return html


def run(write):
    live = json.load(open(LIVE))
    pre = {a["id"]: a["content"] for a in json.load(open(SNAPSHOT))}
    changed, logs = [], {}
    for art in live:
        log = []
        out = repair(art["content"], pre.get(art["id"], ""), log)
        if out != art["content"]:
            changed.append((art, out))
            logs[art["id"]] = log

    total = sum(len(v) for v in logs.values())
    print("articles repaired : %d" % len(changed))
    print("links unwrapped   : %d" % total)
    per = {}
    for v in logs.values():
        for line in v:
            t = line.rsplit(" ", 1)[-1]
            per[t] = per.get(t, 0) + 1
    for t, n in sorted(per.items(), key=lambda x: -x[1]):
        print("   %-34s %d" % (t, n))

    if write:
        os.makedirs(os.path.join(BASE, "batch"), exist_ok=True)
        for art, out in changed:
            io.open(os.path.join(BASE, "batch", "%d.html" % art["id"]),
                    "w", encoding="utf-8").write(out)
        print("\nwritten to batch/ for gating: %d files" % len(changed))
    return changed


if __name__ == "__main__":
    run(write=(len(sys.argv) > 1 and sys.argv[1] == "write"))
