#!/usr/bin/env python3
"""Build README.md for awesome-soccer-data from scripts/entries.json + SportsDataStack listings.

Usage: python3 scripts/build_readme.py   (env SDS_REPO, default /workspace/sportsdatastack)
Stdlib only, no network access.
"""
import datetime
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SDS = pathlib.Path(os.environ.get("SDS_REPO", "/workspace/sportsdatastack"))
LISTINGS = json.loads((SDS / "data" / "listings.json").read_text())
TAX = json.loads((SDS / "data" / "taxonomy.json").read_text())
ENTRIES = json.loads((ROOT / "scripts" / "entries.json").read_text())
BY_SLUG = {l["slug"]: l for l in LISTINGS}
TODAY = datetime.date.today().isoformat()

SITE = "https://sportsdatastack.com"
UTM = "?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data"
TAGS = {"free": "Free", "freemium": "Freemium", "paid": "Paid"}
# Listings with coverage.access == null get a hand-checked tag.
TAG_OVERRIDES = {"sofascore": "free", "markstats": "free", "smarterscout-vantage-fc": "paid", "eyeball": "paid"}
MARKETING = re.compile(r"\b(best|leading|powerful|cutting-edge|revolutionary|ultimate|world-class|amazing|seamless)\b|per its own site", re.I)

# (id, title, one-line description)
SECTIONS = [
    ("event-data", "Event Data", "Open and commercial providers of on-ball event data (passes, shots, tackles) with pitch coordinates."),
    ("tracking-data", "Tracking Data", "Player and ball positions over time, from enterprise optical tracking to open samples and DIY camera tools."),
    ("xg-models", "xG & Models", "Expected goals, ratings and action-value models, as websites or libraries."),
    ("stats-sites", "Stats Websites", "Websites and apps for browsing match, player and team statistics."),
    ("apis", "APIs", "Programmatic access to fixtures, live scores, stats and odds."),
    ("python", "Python Libraries", "Python packages for loading, scraping and analysing soccer data."),
    ("r-packages", "R Packages", "R packages for accessing soccer data."),
    ("visualization", "Visualization", "Libraries for drawing pitches, shot maps, radars and animations."),
    ("womens", "Women's Football", "Sources dedicated to women's football."),
    ("datasets", "Datasets", "Downloadable datasets: results, World Cups, transfers, odds and ID mappings."),
    ("scouting", "Scouting & Recruitment Platforms", "Commercial platforms for player scouting, recruitment and performance analysis."),
    ("ai-tools", "AI & MCP Tools", "MCP servers, agent plugins and AI assistants for working with football data."),
    ("learning", "Learning Resources", "Tutorials, courses, handbooks and other curated lists."),
]
SECTION_IDS = [s[0] for s in SECTIONS]
HIGHLIGHT_LEAGUES = ["premier-league", "la-liga", "serie-a", "bundesliga", "ligue-1", "mls", "liga-mx", "brasileirao",
                     "argentina-primera", "champions-league", "world-cup", "nwsl", "wsl", "liga-f", "liga-mx-femenil",
                     "womens-world-cup"]


def anchor(title):
    """GitHub heading anchor: lowercase, drop punctuation, spaces -> hyphens."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def validate():
    """Every listing exactly once, valid categories/tags, blurb rules, no duplicate names or urls."""
    # Slugs removed by `check_links.py --drop` (dead links) still count as accounted for.
    dropped_file = ROOT / "scripts" / "dropped.json"
    dropped = json.loads(dropped_file.read_text()) if dropped_file.exists() else []
    slugs = [e["slug"] for e in ENTRIES if e["slug"]] + dropped
    assert len(slugs) == len(set(slugs)), "duplicate slug in entries.json/dropped.json"
    assert set(slugs) == set(BY_SLUG), f"slug mismatch: missing {set(BY_SLUG) - set(slugs)}, unknown {set(slugs) - set(BY_SLUG)}"
    assert len(slugs) == 85, f"expected 85 listings, got {len(slugs)}"
    for e in ENTRIES:
        assert e["category"] in SECTION_IDS, f"bad category {e}"
        assert e["tag"] in TAGS, f"bad tag {e}"
        b = e["blurb"]
        assert len(b) <= 110 and b[0].isupper() and b.endswith(".") and not MARKETING.search(b), f"bad blurb: {b}"
        if e["slug"]:
            l = BY_SLUG[e["slug"]]
            assert e["tag"] == (l["coverage"]["access"] or TAG_OVERRIDES[e["slug"]]), f"tag mismatch {e['slug']}"
            assert not b.lower().startswith(l["name"].lower()), f"blurb repeats name: {e['slug']}"
        else:
            assert e["name"] and e["url"].startswith("http"), f"extra needs name and url: {e}"
    for key in ("name", "url"):
        vals = [resolve(e)[key].lower() for e in ENTRIES]
        assert len(vals) == len(set(vals)), f"duplicate {key}"


def resolve(e):
    """Entry with name/url filled in from the listing when it has a slug."""
    if e["slug"]:
        l = BY_SLUG[e["slug"]]
        return {**e, "name": l["name"], "url": l["url"]}
    return e


def entry_line(e):
    line = f"- [{e['name']}]({e['url']}) - {e['blurb']} `{TAGS[e['tag']]}`"
    if e["slug"]:
        line += f" · [Details]({SITE}/tools/{e['slug']}/{UTM})"
    return line


def sort_key(e):
    return e["name"].casefold()


# --- League coverage: mirrors src/lib/coverage.js (cellEntries / cell / leagueSources) ---

def cell_entries(league, dtype):
    """Primary and via entries for a (league, type); one per listing, a free cell beats a paid one."""
    primary, via = {}, {}
    for l in LISTINGS:
        for c in (l.get("coverage") or {}).get("cells", []):
            if league not in c["competitions"] or dtype not in c["types"]:
                continue
            m = via if c.get("via") else primary
            prev = m.get(l["slug"])
            if not prev or (prev["access"] != "free" and c["access"] == "free"):
                m[l["slug"]] = {"l": l, "access": c["access"], "via": c.get("via")}
    return list(primary.values()), list(via.values())


def league_sources(league):
    """Direct (non-via) sources for a league with the types they cover, sorted like the site."""
    out = {}
    for t in TAX["types"]:
        primary, via = cell_entries(league, t["id"])
        for e in primary + via:
            o = out.setdefault(e["l"]["slug"], {"l": e["l"], "types": [], "via": e["via"], "free": False})
            o["types"].append(t["id"])
            if e["access"] == "free":
                o["free"] = True
            if not e["via"]:
                o["via"] = None
    srcs = [o for o in out.values() if not o["via"]]
    return sorted(srcs, key=lambda o: (-len(o["types"]), o["l"]["name"].casefold()))


def coverage_table():
    leagues = {l["id"]: l for l in TAX["leagues"]}
    rows = ["| Competition | Free sources | xG sources (free) | Free sources include |", "| --- | --- | --- | --- |"]
    for lid in HIGHLIGHT_LEAGUES:
        srcs = league_sources(lid)
        free = [s for s in srcs if s["free"]]
        xg_primary, _ = cell_entries(lid, "xg")
        xg_free = sum(e["access"] == "free" for e in xg_primary)
        top = ", ".join(f"[{s['l']['name']}]({s['l']['url']})" for s in free[:3]) or "-"
        name = f"[{leagues[lid]['name']}]({SITE}/leagues/{lid}/{UTM})"
        rows.append(f"| {name} | {len(free)} | {len(xg_primary)} ({xg_free} free) | {top} |")
    return rows


def build():
    validate()
    entries = [resolve(e) for e in ENTRIES]
    by_cat = {cid: sorted([e for e in entries if e["category"] == cid], key=sort_key) for cid in SECTION_IDS}
    titles = [s[1] for s in SECTIONS] + ["Leagues Coverage Highlights", "Contributing", "License"]

    out = [
        "# Awesome Soccer Data [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A curated list of soccer (football) data sources, APIs, libraries and tools.",
        "",
        f"This list collects {len(entries)} data sources and tools for soccer analytics: event and tracking data, xG models, "
        "stats websites, APIs, Python and R libraries, datasets and scouting platforms. It covers free and paid options "
        "and men's and women's competitions worldwide.",
        "",
        "Legend: `Free` - free to use. `Freemium` - free tier plus paid plans. `Paid` - paid only, including contact-sales and enterprise products.",
        "",
        f"Every external link was checked on {TODAY}. \"Details\" links go to [SportsDataStack]({SITE}/{UTM}), "
        "an independent directory with pricing and coverage notes for each tool.",
        "",
        "## Contents",
        "",
        *[f"- [{t}](#{anchor(t)})" for t in titles],
    ]
    for cid, title, desc in SECTIONS:
        out += ["", f"## {title}", "", desc, ""]
        out += [entry_line(e) for e in by_cat[cid]]
        if cid == "womens":
            also = sorted([e for e in entries if e["category"] != "womens" and e["slug"] and BY_SLUG[e["slug"]].get("womens")], key=sort_key)
            out += ["", "Also cover women's football: " + ", ".join(f"[{e['name']}]({e['url']})" for e in also) + "."]
    out += [
        "", "## Leagues Coverage Highlights", "",
        "Direct sources with verified coverage for each competition (client libraries and scrapers of another source are not counted).",
        "", *coverage_table(), "",
        f"See the [full league x data-type coverage map]({SITE}/coverage/{UTM}) for every competition and data type.",
        "", "## Contributing", "",
        "Contributions are welcome. Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.",
        "Suggest one tool per pull request, with a link to its own site and a neutral one-sentence description.",
        "", "## License", "",
        "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)",
        "",
        "To the extent possible under law, the contributors have waived all copyright and related rights to this work. See [LICENSE](LICENSE).",
        "",
    ]
    text = "\n".join(out)
    assert not re.search(r"[ \t]+$", text, re.M), "trailing whitespace"
    (ROOT / "README.md").write_text(text)

    print(f"README.md written ({TODAY}): {len(entries)} unique entries")
    for cid, title, _ in SECTIONS:
        print(f"  {title:34} {len(by_cat[cid]):3}")


if __name__ == "__main__":
    build()
