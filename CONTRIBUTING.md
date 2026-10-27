# Contribution Guidelines

Thanks for helping make this the best reference list for soccer (football) data. Please read this page before opening a pull request.

## What belongs here

- Data sources, APIs, datasets, libraries, tools and learning resources for **soccer/football** (men's and women's, any country).
- Both free and paid products are welcome. Paid and enterprise tools must have a public website that explains what they offer.
- The project must be live and reachable. Archived, abandoned or dead projects are removed.
- Link to the tool's **own site** (or its official repository or docs), not to a news article or a third-party directory.
- No betting tips services, tipster sites or affiliate-only pages.

## How to add an entry

1. Search the list first to avoid duplicates.
2. Add **one** entry per pull request, in the best-fitting section, in **alphabetical order** (case-insensitive).
3. Use this format on a single line:

   ```markdown
   - [Name](https://example.com) - Short, neutral description. `Free` · [Details](https://sportsdatastack.com/tools/slug/)
   ```

4. Description rules:
   - One sentence, starts with a capital letter, ends with a period.
   - Neutral and factual: say what it provides (data types, competitions, format), not how good it is.
   - Do not repeat the tool's name or use words like "best", "powerful" or "revolutionary".
5. Tag rules:
   - `Free` - free to use (including open source and open data).
   - `Freemium` - a free tier plus paid plans or limits.
   - `Paid` - paid only, including contact-sales and enterprise products.
6. The `Details` link is optional. Include it only if the tool has a page on [SportsDataStack](https://sportsdatastack.com), an independent directory of soccer data tools. Please do not add other promotional links.
7. Check that your link works and that you have no trailing whitespace.

## Editing the list

`README.md` is generated from `scripts/entries.json` by `scripts/build_readme.py`, which reads the listings data from a checkout of [3zavalam/sportsdatastack](https://github.com/3zavalam/sportsdatastack) (set `SDS_REPO` to its path). If you are comfortable with that, you can add your entry to `entries.json` instead and run the script. Otherwise edit `README.md` directly and a maintainer will sync the data file.

Run `python3 scripts/check_links.py` to check that all links still resolve.

## Removing or correcting an entry

Open an issue or pull request if a tool has shut down, moved, changed its pricing tag or has an inaccurate description. Include a source link.

## Pull request title

Use `Add <Name>`, `Remove <Name>` or `Update <Name>`.

By contributing you agree that your contribution is released under [CC0 1.0](LICENSE).
