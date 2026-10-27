#!/usr/bin/env python3
"""Check every external link in README.md and write a JSON report {url: status}.

Usage: python3 scripts/check_links.py [--out scripts/link-report.json] [--drop]

Statuses: ok (2xx/3xx after redirects), blocked (401/403/429/999: the site refuses bots, not dead),
dead (404/410, DNS failure, connection refused), error (anything else, e.g. timeouts, 5xx, TLS).
Tool links and sportsdatastack.com "Details" links are checked in separate passes.
--drop removes entries whose tool url is dead from entries.json and records dropped slugs in
scripts/dropped.json (so build_readme.py still accounts for every listing). Exits 1 if any link is dead.
Stdlib only.
"""
import argparse
import json
import pathlib
import re
import socket
import ssl
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ENTRIES = ROOT / "scripts" / "entries.json"
DROPPED = ROOT / "scripts" / "dropped.json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/130.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8", "Accept-Language": "en;q=0.9"}
TIMEOUT = 20
BLOCKED, DEAD = {401, 403, 429, 999}, {404, 410}


def classify_code(code):
    if 200 <= code < 400:
        return "ok"
    if code in BLOCKED:
        return "blocked"
    if code in DEAD:
        return "dead"
    return "error"


def request(url, method):
    """Return an HTTP status code (redirects followed) or raise for network-level failures."""
    req = urllib.request.Request(url, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def network_status(exc):
    """DNS failures and refused connections mean dead; other network errors are inconclusive."""
    reason = getattr(exc, "reason", exc)
    if isinstance(reason, (socket.gaierror, ConnectionRefusedError)):
        return "dead"
    return "error"


def check_once(url):
    try:
        code = request(url, "HEAD")
        if classify_code(code) != "ok":  # many servers mishandle HEAD; confirm with GET
            code = request(url, "GET")
        return classify_code(code)
    except (urllib.error.URLError, OSError, ssl.SSLError, ValueError) as e:
        return network_status(e)


def check(url):
    status = check_once(url)
    if status != "ok":  # retry once to ride out transient failures
        status = check_once(url)
    return url, status


def run_pass(label, urls):
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(pool.map(check, urls))
    counts = {s: sum(v == s for v in results.values()) for s in ("ok", "blocked", "dead", "error")}
    print(f"{label}: {len(urls)} urls, " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    for url, s in sorted(results.items()):
        if s != "ok":
            print(f"  {s:8} {url}")
    return results


def drop_dead(dead_urls):
    """Remove entries whose tool url is dead; remember dropped slugs for build_readme.py."""
    import build_readme  # same directory; gives listing urls for slug entries
    entries = json.loads(ENTRIES.read_text())
    keep, dropped = [], []
    for e in entries:
        (dropped if build_readme.resolve(e)["url"] in dead_urls else keep).append(e)
    if not dropped:
        print("--drop: nothing to drop")
        return
    ENTRIES.write_text(json.dumps(keep, indent=2, ensure_ascii=False) + "\n")
    prev = json.loads(DROPPED.read_text()) if DROPPED.exists() else []
    slugs = sorted(set(prev) | {e["slug"] for e in dropped if e["slug"]})
    DROPPED.write_text(json.dumps(slugs, indent=2) + "\n")
    print("--drop: removed from entries.json:")
    for e in dropped:
        print(f"  {e.get('slug') or e.get('name')}  {build_readme.resolve(e)['url']}")
    print("Re-run scripts/build_readme.py to regenerate README.md.")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(ROOT / "scripts" / "link-report.json"), help="JSON report path")
    ap.add_argument("--drop", action="store_true", help="remove entries with dead tool urls from entries.json")
    args = ap.parse_args()

    urls = sorted(set(re.findall(r"\((https?://[^)\s]+)\)", README.read_text())))
    sds = [u for u in urls if re.match(r"https?://(www\.)?sportsdatastack\.com", u)]
    external = [u for u in urls if u not in sds]

    report = run_pass("External links", external)
    report.update(run_pass("SportsDataStack links", sds))
    pathlib.Path(args.out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"Report written to {args.out}")

    dead = {u for u, s in report.items() if s == "dead"}
    if args.drop:
        drop_dead(dead & set(external))
    raise SystemExit(1 if dead else 0)


if __name__ == "__main__":
    main()
