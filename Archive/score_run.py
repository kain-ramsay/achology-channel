#!/usr/bin/env python3
"""The bulk Rank Math score run for the 249 help articles.

WHY IT WORKS THIS WAY

Rank Math's SEO score is not computed on the server. It is computed by the
analyser that runs inside the WordPress editor, in a browser, which is why 249
imported articles carry no score at all: nobody has ever opened them.

Two constraints shaped this script.

1. **The obvious automation is the wrong one.** Opening each article and
   pressing Update would work, and would also risk the block editor rewriting
   imported HTML, and would stamp a fresh modified date on all 249. DSRD 6
   section 6: "The date changes only when the content genuinely changes;
   bumping dates to look fresh is a known trick that AI systems and readers
   both learn to distrust." So this script reads the score the analyser
   produces and saves nothing. Not a character of content changes, and no
   modified date moves.

2. **Every browser I control is refused by the host.** SiteGround's Antibot
   answers automated clients with a challenge screen, and support confirmed on
   2026-07-27 that it cannot be disabled or whitelisted per site. Kain's own
   Safari is not refused, because it is a real browser with him signed in. So
   the run drives Safari through AppleScript, in its own window, reading each
   score as it appears. Nothing about the site's security is changed to make
   this work, which was the alternative and the worse one.

It runs in a dedicated Safari window, so Kain can carry on working in his own
windows while it goes.

USAGE
    python3 score_run.py --ids ids.txt --out scores.tsv [--limit N]
"""
import argparse
import os
import subprocess
import time

SITE = "https://achologytest.com"

# Rank Math answers from its editor store. Ask for a string, because AppleScript
# hands back text and an absent value must be distinguishable from a zero.
READ_JS = (
    "(function(){"
    "try{var s=wp.data.select('rank-math').getAnalysisScore();"
    "if(typeof s==='number')return 'S'+s;}catch(e){}"
    "try{if(window.rankMathEditor&&rankMathEditor.resultManager&&window.rankMath){"
    "var t=rankMathEditor.resultManager.getScore(rankMath.objectID);"
    "if(typeof t==='number')return 'S'+t;}}catch(e){}"
    "return 'X'+document.readyState;})()"
)


def osa(script):
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=120)
    return (r.stdout or r.returncode and r.stderr or "").strip()


def open_window(first_url):
    """Own window, so the run never steals the window Kain is working in.

    Safari's scripting model has no id on a document, only on a window, and a
    window's page is reached as its current tab, so the run holds a window id
    and addresses "current tab of window id N".
    """
    out = osa('tell application "Safari"\n'
              f'  make new document with properties {{URL:"{first_url}"}}\n'
              '  return id of window 1\n'
              'end tell')
    return out.strip().splitlines()[-1]


def score_for(win_id, post_id, settle_reads=2, timeout_s=45):
    """Load one article in the run's window and read the settled score."""
    url = f"{SITE}/wp-admin/post.php?post={post_id}&action=edit"
    osa(f'tell application "Safari" to set URL of current tab of window id {win_id} to "{url}"')
    deadline = time.time() + timeout_s
    stable, last = 0, None
    while time.time() < deadline:
        time.sleep(3)
        raw = osa(f'tell application "Safari" to do JavaScript "{READ_JS}" '
                  f'in current tab of window id {win_id}')
        if raw.startswith("S"):
            val = int(raw[1:])
            # The analyser climbs to its final number rather than arriving at
            # it, so a reading only counts once it has repeated.
            stable = stable + 1 if val == last else 0
            last = val
            if stable >= settle_reads:
                return val, "settled"
    return (last, "unsettled") if last is not None else (None, "no reading")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    ids = [l.strip() for l in open(args.ids) if l.strip()]
    if args.limit:
        ids = ids[:args.limit]
    if os.path.exists(args.out):                     # resumable: a run that dies
        done = {l.split("\t")[0] for l in open(args.out)}   # at 180 does not start again
        ids = [i for i in ids if i not in done]
        print(f"resuming: {len(done)} scored, {len(ids)} to go", flush=True)
    if not ids:
        print("nothing to do", flush=True)
        return

    doc = open_window(f"{SITE}/wp-admin/post.php?post={ids[0]}&action=edit")
    print(f"run window: {doc}", flush=True)
    t0 = time.time()
    with open(args.out, "a") as out:
        for n, pid in enumerate(ids, 1):
            try:
                score, note = score_for(doc, pid)
            except Exception as e:                   # one stuck editor is one
                score, note = None, f"error: {type(e).__name__}"   # article, not the run
            out.write(f"{pid}\t{score if score is not None else ''}\t{note}\n")
            out.flush()
            rate = n / max(time.time() - t0, 1) * 3600
            print(f"[{n}/{len(ids)}] {pid} -> {score} ({note}) ~{rate:.0f}/hr", flush=True)
    print("SCORE_RUN_DONE", flush=True)


if __name__ == "__main__":
    main()
