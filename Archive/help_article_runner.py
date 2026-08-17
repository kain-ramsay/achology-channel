"""One command per batch, instead of six.

  python3 run.py fetch          refresh the local copy of all 249 articles
  python3 run.py list N         show the N thinnest articles still to rebuild
  python3 run.py show ID ...    print the current text of one or more articles
  python3 run.py ship           gate everything in batch/ and, if it all passes, publish it

Written so Kain is not sitting behind an approval prompt for every step.
"""
import json, os, re, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from article_gate import check, known_urls, TAG

HOST = "u3156-zbuugkeqcc2g@ssh.achologytest.com"
SSH = ["ssh", "-i", os.path.expanduser("~/.ssh/achology_siteground"),
       "-p", "18765", "-o", "BatchMode=yes", "-o", "ConnectTimeout=60", HOST]
WP = "cd ~/www/achologytest.com/public_html && "

DUMP = WP + '''wp eval '
$ids=get_posts(["post_type"=>"faq_article","post_status"=>"publish","numberposts"=>-1,"fields"=>"ids"]);
$o=[]; foreach($ids as $i){$p=get_post($i); $o[]=["id"=>$i,"title"=>$p->post_title,"content"=>$p->post_content];}
echo json_encode($o);' 2>/dev/null'''


def run(remote, stdin=None):
    return subprocess.run(SSH + [remote], input=stdin, capture_output=True, text=True)


def fetch():
    r = run(DUMP)
    data = json.loads(r.stdout)
    json.dump(data, open(os.path.join(BASE, "cur249.json"), "w"))
    return data


def load():
    return json.load(open(os.path.join(BASE, "cur249.json")))


def thin(data, urls):
    out = []
    for a in data:
        if a["id"] >= 10000:
            continue
        w, f = check(a["id"], a["content"], urls, a["title"])
        if any("too thin" in x for x in f):
            out.append((w, a["id"], a["title"]))
    return sorted(out)


def ship():
    urls, cur = known_urls(), {a["id"]: a for a in load()}
    files = sorted(f for f in os.listdir(os.path.join(BASE, "batch")) if f.endswith(".html"))
    if not files:
        print("nothing in batch/")
        return
    payload, ok = [], True
    for f in files:
        pid = int(f[:-5])
        html = open(os.path.join(BASE, "batch", f)).read()
        w, fails = check(pid, html, urls, cur[pid]["title"])
        old = len(TAG.sub(" ", cur[pid]["content"]).split())
        print(f'[{pid}] {old:4}w -> {w:4}w  links={html.count("<a "):2}  {cur[pid]["title"][:44]}')
        for x in fails:
            print("      FAIL:", x)
            ok = False
        payload.append({"id": pid, "content": html})
    if not ok:
        print("\nnothing published: fix the failures above first")
        return
    r = run("cat > /tmp/apply.json", stdin=json.dumps(payload))
    if r.returncode:
        print("upload failed:", r.stderr[:300])
        return
    r = run(WP + "wp eval-file /tmp/apply.php && wp cache flush")
    print("\n" + "\n".join(l for l in r.stdout.splitlines() if l.strip())[-400:])
    for f in files:
        os.remove(os.path.join(BASE, "batch", f))
    data = fetch()
    left = len(thin(data, urls))
    print(f"\n{left} articles left to rebuild in the 200")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "fetch":
        print(len(fetch()), "articles fetched")
    elif cmd == "list":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        rows = thin(load(), known_urls())
        print(f"{len(rows)} left to rebuild")
        for w, pid, t in rows[:n]:
            print(f"  {w:4}w [{pid}] {t[:62]}")
    elif cmd == "show":
        d = {a["id"]: a for a in load()}
        for pid in [int(x) for x in sys.argv[2:]]:
            print(f'===== [{pid}] {d[pid]["title"]}')
            print(d[pid]["content"])
            print()
    elif cmd == "ship":
        ship()
