# Awesome Soccer Data [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of soccer (football) data sources, APIs, libraries and tools.

This list collects 88 data sources and tools for soccer analytics: event and tracking data, xG models, stats websites, APIs, Python and R libraries, datasets and scouting platforms. It covers free and paid options and men's and women's competitions worldwide.

Legend: `Free` - free to use. `Freemium` - free tier plus paid plans. `Paid` - paid only, including contact-sales and enterprise products.

Every external link was checked on 2026-10-27. "Details" links go to [SportsDataStack](https://sportsdatastack.com/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data), an independent directory with pricing and coverage notes for each tool.

## Contents

- [Event Data](#event-data)
- [Tracking Data](#tracking-data)
- [xG & Models](#xg--models)
- [Stats Websites](#stats-websites)
- [APIs](#apis)
- [Python Libraries](#python-libraries)
- [R Packages](#r-packages)
- [Visualization](#visualization)
- [Women's Football](#womens-football)
- [Datasets](#datasets)
- [Scouting & Recruitment Platforms](#scouting--recruitment-platforms)
- [AI & MCP Tools](#ai--mcp-tools)
- [Learning Resources](#learning-resources)
- [Leagues Coverage Highlights](#leagues-coverage-highlights)
- [Contributing](#contributing)
- [License](#license)

## Event Data

Open and commercial providers of on-ball event data (passes, shots, tackles) with pitch coordinates.

- [Hudl StatsBomb](https://www.hudl.com/products/statsbomb) - Professional event data with 360 player locations and broadcast-tracking physical data for 300+ competitions. `Paid` · [Details](https://sportsdatastack.com/tools/hudl-statsbomb/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Hudl Wyscout](https://www.hudl.com/products/wyscout) - Video and data scouting platform with match footage and performance stats from 1,000+ competitions. `Paid` · [Details](https://sportsdatastack.com/tools/hudl-wyscout/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [IMPECT (Catapult)](https://www.catapult.com/solutions/impect) - Event data and scouting platform known for Packing metrics, now part of Catapult. `Paid` · [Details](https://sportsdatastack.com/tools/impect-catapult/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Opta (Stats Perform)](https://www.statsperform.com/opta/) - Enterprise event, tracking and xG data feeds covering 3,900+ competitions for media, teams and betting. `Paid` · [Details](https://sportsdatastack.com/tools/opta-stats-perform/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [StatsBomb Open Data](https://github.com/hudl/open-data) - Free JSON event data for selected men's and women's competitions, released by Hudl StatsBomb. `Free` · [Details](https://sportsdatastack.com/tools/statsbomb-open-data/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Tracking Data

Player and ball positions over time, from enterprise optical tracking to open samples and DIY camera tools.

- [Fut Traffic](https://github.com/danrublop/futtraffic) - Local app that tracks players from a panoramic camera and reports distance and speed per player. `Free` · [Details](https://sportsdatastack.com/tools/fut-traffic/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Metrica Sports](https://www.metrica-sports.com/) - Video analysis software for coaches and analysts with tracking and data integration. `Paid` · [Details](https://sportsdatastack.com/tools/metrica-sports/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Metrica Sports Sample Data](https://github.com/metrica-sports/sample-data) - Three anonymised sample games of synchronised tracking and event data. `Free` · [Details](https://sportsdatastack.com/tools/metrica-sports-sample-data/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Second Spectrum (Genius Sports)](https://www.geniussports.com/) - Optical tracking and performance analytics, now part of Genius Sports. `Paid` · [Details](https://sportsdatastack.com/tools/second-spectrum-genius-sports/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [SkillCorner](https://skillcorner.com/) - Broadcast-tracking provider of physical and off-ball data across 150+ competitions. `Paid` · [Details](https://sportsdatastack.com/tools/skillcorner/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [SkillCorner Open Data](https://github.com/SkillCorner/opendata) - Broadcast tracking data for 10 A-League 2024/25 matches plus season-level physical aggregates. `Free` · [Details](https://sportsdatastack.com/tools/skillcorner-open-data/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [TouchLine](https://github.com/allwayso/TouchLine) - Open-source tool that turns single-camera amateur match footage into player tracking data on a CPU. `Free` · [Details](https://sportsdatastack.com/tools/touchline/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## xG & Models

Expected goals, ratings and action-value models, as websites or libraries.

- [American Soccer Analysis](https://www.americansocceranalysis.com/) - Public xG, xPass and Goals Added models with interactive tables and an API for North American leagues. `Free` · [Details](https://sportsdatastack.com/tools/american-soccer-analysis/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [ClubElo](https://clubelo.com/) - Elo ratings and fixture probabilities for club teams worldwide. `Free` · [Details](https://sportsdatastack.com/tools/clubelo/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Scout Lab (Streamlit app)](https://scoutlab.streamlit.app/) - Web app with player percentiles, radars, similarity scores and VAEP metrics for Big-5 leagues. `Free` · [Details](https://sportsdatastack.com/tools/scout-lab-streamlit-app/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [socceraction](https://socceraction.readthedocs.io/) - Python library that converts event data to SPADL and values actions with VAEP or xT. `Free` · [Details](https://sportsdatastack.com/tools/socceraction/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Understat](https://understat.com/) - Team and player xG for six European leagues, with tables exportable as CSV, JSON or XLSX. `Free` · [Details](https://sportsdatastack.com/tools/understat/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [xG Lab](https://xglab.io/) - Match analytics with win-probability replays, xG timelines, shot maps and explained predictions. `Free` · [Details](https://sportsdatastack.com/tools/xg-lab/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [xG Stat](https://www.xgstat.com/) - Player xG-per-90 rankings, percentiles, match reports and shot maps for six leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/xg-stat/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Stats Websites

Websites and apps for browsing match, player and team statistics.

- [DataMB](https://datamb.football/) - Player and team comparison radars and visual tools for the Big-5 and other European leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/datamb/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [FBref](https://fbref.com/en/) - Stats reference site from Sports Reference; basic and historical data only since January 2026. `Freemium` · [Details](https://sportsdatastack.com/tools/fbref/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [FootyStats](https://footystats.org/) - Stats tables for 1,500+ leagues (goals, corners, cards, xG) with a betting-oriented focus. `Freemium` · [Details](https://sportsdatastack.com/tools/footystats/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [FotMob](https://www.fotmob.com/) - Live scores app and website with league stat leaderboards, including xG for many competitions. `Free` · [Details](https://sportsdatastack.com/tools/fotmob/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [LIGA MX (official site)](https://ligamx.net/) - Official Liga MX site with fixtures, results, standings and historical statistics, in Spanish. `Free` · [Details](https://sportsdatastack.com/tools/liga-mx-official-site/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [MarkStats](https://markstats.club/) - Statistics and analytics portal for major European leagues. `Free` · [Details](https://sportsdatastack.com/tools/markstats/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Opta Analyst](https://theanalyst.com/) - Editorial site from Stats Perform with Opta stats, predictions and power rankings. `Free` · [Details](https://sportsdatastack.com/tools/opta-analyst/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [SofaScore](https://www.sofascore.com/) - Live scores and match statistics website and app. `Free` · [Details](https://sportsdatastack.com/tools/sofascore/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Tifolab](https://www.tifolab.com/) - Player and team comparison with radars, percentiles and shortlists across 74 competitions. `Free` · [Details](https://sportsdatastack.com/tools/tifolab/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Transfermarkt](https://www.transfermarkt.com/) - Football database of market values, transfers, contracts and squads for 1,300+ leagues. `Free` · [Details](https://sportsdatastack.com/tools/transfermarkt/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [WhoScored](https://www.whoscored.com/) - Match and player statistics with player ratings and per-game leaderboards for major leagues. `Free` · [Details](https://sportsdatastack.com/tools/whoscored/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## APIs

Programmatic access to fixtures, live scores, stats and odds.

- [API-Football](https://www.api-football.com/) - REST API for fixtures, live scores, events, lineups, players, transfers, statistics and odds. `Freemium` · [Details](https://sportsdatastack.com/tools/api-football/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Dribble](https://dribble360.com/) - Match stats and xG for 23 leagues delivered as CSV downloads, REST API or BigQuery. `Paid` · [Details](https://sportsdatastack.com/tools/dribble/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [football-data.org](https://www.football-data.org/) - REST API for fixtures, results, standings, lineups and squads with a free tier of 12 competitions. `Freemium` · [Details](https://sportsdatastack.com/tools/football-data-org/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [FootyStats API](https://footystats.org/api/) - JSON API with league, team, player and match stats (goals, BTTS, corners, cards) for 1,500+ leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/footystats-api/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [GOAL API](https://goal-api.com/) - REST and WebSocket API with live scores, fixtures, standings and lineups for 1,000+ competitions. `Freemium` · [Details](https://sportsdatastack.com/tools/goal-api/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [KickoffAPI](https://kickoffapi.com/) - API with live scores, fixtures, lineups, odds, player stats and model xG for 1,245 leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/kickoffapi/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Sportmonks Football API](https://www.sportmonks.com/football-api/) - Football API covering 2,200+ leagues with fixtures, live scores, stats and paid xG add-ons. `Freemium` · [Details](https://sportsdatastack.com/tools/sportmonks-football-api/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [SportsDataIO Soccer API](https://sportsdata.io/soccer-api) - Soccer data feeds with schedules, scores, standings and rosters for many international leagues. `Paid` · [Details](https://sportsdatastack.com/tools/sportsdataio-soccer-api/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Statorium](https://statorium.com/) - Multi-sport data API and HTML widgets with football coverage and WordPress integration. `Paid` · [Details](https://sportsdatastack.com/tools/statorium/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [StrikerAPI](https://strikerapi.com/) - API and MCP server with results, lineups, events, shot xG, Elo and odds for 17 competitions. `Freemium` · [Details](https://sportsdatastack.com/tools/strikerapi/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [TheSportsDB](https://www.thesportsdb.com/) - Crowd-sourced multi-sport database and JSON API of teams, players, events and artwork. `Freemium` · [Details](https://sportsdatastack.com/tools/thesportsdb/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [TheStatsAPI](https://www.thestatsapi.com/) - Football stats API with fixtures, live scores, player stats, xG and odds for 150 competitions. `Paid` · [Details](https://sportsdatastack.com/tools/thestatsapi/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [zerozero API](https://api.zerozero.pt/) - API from the Portuguese site zerozero with competitions, clubs, players, fixtures and statistics. `Freemium` · [Details](https://sportsdatastack.com/tools/zerozero-api/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Python Libraries

Python packages for loading, scraping and analysing soccer data.

- [databallpy](https://github.com/Alek050/databallpy) - Python package to read, preprocess, visualise and synchronise event and tracking data. `Free` · [Details](https://sportsdatastack.com/tools/databallpy/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [floodlight](https://github.com/floodlight-sports/floodlight) - Python package for streamlined analysis of sports tracking and event data. `Free` · [Details](https://sportsdatastack.com/tools/floodlight/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [itscalledsoccer](https://github.com/American-Soccer-Analysis/itscalledsoccer) - Python wrapper for the American Soccer Analysis API (MLS, NWSL, USL, MLS Next Pro). `Free` · [Details](https://sportsdatastack.com/tools/itscalledsoccer/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [kloppy](https://kloppy.pysport.org/) - Python library that standardises tracking and event data from many providers into one model. `Free` · [Details](https://sportsdatastack.com/tools/kloppy/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [LanusStats](https://github.com/federicorabanos/LanusStats) - Spanish-language Python scraper for FBref, FotMob, SofaScore, 365Scores and Transfermarkt. `Free` · [Details](https://sportsdatastack.com/tools/lanusstats/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [ScraperFC](https://github.com/oseymour/ScraperFC) - Python package for scraping ClubElo, FBref, Sofascore, Transfermarkt, Understat and Capology. `Free` · [Details](https://sportsdatastack.com/tools/scraperfc/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [soccerdata](https://soccerdata.readthedocs.io/) - Python scrapers for FBref, Understat, WhoScored, Sofascore and more, returning pandas DataFrames. `Free` · [Details](https://sportsdatastack.com/tools/soccerdata/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [statsbombpy](https://github.com/hudl/statsbombpy) - Official Python client for StatsBomb open data and API data. `Free` · [Details](https://sportsdatastack.com/tools/statsbombpy/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [understatAPI](https://github.com/collinb9/understatAPI) - Python package for scraping data from understat.com. `Free` · [Details](https://sportsdatastack.com/tools/understatapi/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [unravelsports](https://github.com/UnravelSports/unravelsports) - Python package that turns raw tracking data into analysis-ready formats, including graph neural networks. `Free` · [Details](https://sportsdatastack.com/tools/unravelsports/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## R Packages

R packages for accessing soccer data.

- [StatsBombR](https://github.com/hudl/StatsBombR) - Official R package for StatsBomb API data and the open-data repository. `Free` · [Details](https://sportsdatastack.com/tools/statsbombr/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [worldfootballR](https://github.com/JaseZiv/worldfootballR) - R package for extracting data from FBref, Transfermarkt and Understat. `Free` · [Details](https://sportsdatastack.com/tools/worldfootballr/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Visualization

Libraries for drawing pitches, shot maps, radars and animations.

- [d3-soccer](https://github.com/probberechts/d3-soccer) - D3.js plugin for visualising event-stream soccer data in the browser. `Free` · [Details](https://sportsdatastack.com/tools/d3-soccer/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [ggsoccer](https://github.com/Torvaney/ggsoccer) - R package for plotting event data on pitches with ggplot2. `Free` · [Details](https://sportsdatastack.com/tools/ggsoccer/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [matplotsoccer](https://github.com/TomDecroos/matplotsoccer) - Python package to visualise soccer event data. `Free` · [Details](https://sportsdatastack.com/tools/matplotsoccer/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [mplsoccer](https://mplsoccer.readthedocs.io/) - Python library for pitches, shot maps, radars and pizza charts with matplotlib. `Free` · [Details](https://sportsdatastack.com/tools/mplsoccer/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [soccerAnimate (Dato-Futbol)](https://github.com/Dato-Futbol/soccerAnimate) - R package from the Spanish-language Dato Fútbol project for animating tracking data. `Free` · [Details](https://sportsdatastack.com/tools/socceranimate-dato-futbol/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Women's Football

Sources dedicated to women's football.

- [LIGA Femenil (official site)](https://ligafemenil.mx/) - Official Liga MX Femenil site with calendar, results, standings and statistics, in Spanish. `Free` · [Details](https://sportsdatastack.com/tools/liga-femenil-official-site/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Soccerdonna](https://www.soccerdonna.de/) - German-language women's football database of players, clubs, transfers and competitions. `Free` · [Details](https://sportsdatastack.com/tools/soccerdonna/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

Also cover women's football: [American Soccer Analysis](https://www.americansocceranalysis.com/), [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup), [FootyStats](https://footystats.org/), [FootyStats API](https://footystats.org/api/), [FotMob](https://www.fotmob.com/), [itscalledsoccer](https://github.com/American-Soccer-Analysis/itscalledsoccer), [LIGA MX (official site)](https://ligamx.net/), [Opta Analyst](https://theanalyst.com/), [Sportmonks Football API](https://www.sportmonks.com/football-api/), [StatsBomb Open Data](https://github.com/hudl/open-data), [statsbombpy](https://github.com/hudl/statsbombpy), [StatsBombR](https://github.com/hudl/StatsBombR), [StrikerAPI](https://strikerapi.com/).

## Datasets

Downloadable datasets: results, World Cups, transfers, odds and ID mappings.

- [European Soccer Database (Kaggle)](https://www.kaggle.com/datasets/hugomathien/soccer) - SQLite dataset of 25k+ European matches, players and odds from 2008 to 2016. `Free`
- [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) - Collection of 27 datasets on every men's (1930-2022) and women's (1991-2019) FIFA World Cup. `Free` · [Details](https://sportsdatastack.com/tools/fjelstul-world-cup-database/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [football-data.co.uk](https://football-data.co.uk/data.php) - Historical CSV results, match stats and odds for 25+ leagues going back decades. `Free` · [Details](https://sportsdatastack.com/tools/football-data-co-uk/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [openfootball football.json](https://github.com/openfootball/football.json) - Public-domain JSON fixtures and results for the Premier League, Bundesliga, La Liga and more. `Free` · [Details](https://sportsdatastack.com/tools/openfootball-football-json/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [openfootball worldcup.json](https://github.com/openfootball/worldcup.json) - Public-domain JSON data for World Cups, including Canada/USA/Mexico 2026. `Free` · [Details](https://sportsdatastack.com/tools/openfootball-worldcup-json/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Reep](https://reep.football/) - Identity register mapping players, teams and matches to IDs from Transfermarkt, FBref, Opta and 50+ others. `Freemium` · [Details](https://sportsdatastack.com/tools/reep/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [transfermarkt-datasets](https://github.com/dcaribou/transfermarkt-datasets) - Pipeline publishing cleaned Transfermarkt data on players, clubs, games and valuations. `Free` · [Details](https://sportsdatastack.com/tools/transfermarkt-datasets/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Scouting & Recruitment Platforms

Commercial platforms for player scouting, recruitment and performance analysis.

- [Analytics FC](https://analyticsfc.co.uk/) - Data-driven football consultancy and analytics provider. `Paid` · [Details](https://sportsdatastack.com/tools/analytics-fc/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Eyeball](https://www.eyeball.club/) - Youth football scouting and video platform. `Paid` · [Details](https://sportsdatastack.com/tools/eyeball/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [SciSports](https://www.scisports.com/) - Football analysis and recruitment software for clubs and youth programmes. `Paid` · [Details](https://sportsdatastack.com/tools/scisports/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Scout Lab AI](https://scoutlab.ai/) - AI tool that turns uploaded match video into player-evaluation reports. `Paid` · [Details](https://sportsdatastack.com/tools/scout-lab-ai/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [ScoutingStats.AI](https://scoutingstats.ai/) - Scouting platform with player comparisons, advanced search, radars and match models for 20 leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/scoutingstats-ai/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [smarterscout (Vantage FC)](https://vantagefc.com/) - Player analytics for evaluating style, quality and comparable profiles, now part of Vantage FC. `Paid` · [Details](https://sportsdatastack.com/tools/smarterscout-vantage-fc/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [TransferRoom](https://www.transferroom.com/) - Transfer marketplace and market intelligence network for clubs, agents and players. `Paid` · [Details](https://sportsdatastack.com/tools/transferroom/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [TruMedia](https://www.trumedianetworks.com/) - Sports analytics and data-visualisation software for teams and media. `Paid` · [Details](https://sportsdatastack.com/tools/trumedia/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Twelve / Earpiece](https://twelve.football/) - AI assistant for scouting and opposition analysis via web and WhatsApp, covering 300+ leagues. `Freemium` · [Details](https://sportsdatastack.com/tools/twelve-earpiece/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## AI & MCP Tools

MCP servers, agent plugins and AI assistants for working with football data.

- [Football Data MCP](https://www.kupsas.com/football-data-mcp) - MCP server that lets AI assistants query player stats, xG and shot maps for 10 leagues. `Free` · [Details](https://sportsdatastack.com/tools/football-data-mcp/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [football-blueprints](https://github.com/opengoalapp/football-blueprints) - Catalogue of football analytics project ideas written as prompts for AI coding agents. `Free` · [Details](https://sportsdatastack.com/tools/football-blueprints/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [football-docs](https://nutmeg.withqwerty.com/football-docs/) - MCP server with searchable docs for 31 football data providers and libraries, plus metric definitions. `Free` · [Details](https://sportsdatastack.com/tools/football-docs/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [nutmeg](https://nutmeg.withqwerty.com/) - Claude Code plugin with skills and agents for acquiring, analysing and visualising football data. `Free` · [Details](https://sportsdatastack.com/tools/nutmeg/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)

## Learning Resources

Tutorials, courses, handbooks and other curated lists.

- [awesome-soccer-analytics](https://github.com/matiasmascioto/awesome-soccer-analytics) - Curated list of soccer analytics resources (not actively updated). `Free` · [Details](https://sportsdatastack.com/tools/awesome-soccer-analytics/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Edd Webster football_analytics](https://github.com/eddwebster/football_analytics) - Collection of football analytics projects and a curated list of public resources. `Free` · [Details](https://sportsdatastack.com/tools/edd-webster-football-analytics/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Friends of Tracking (YouTube)](https://www.youtube.com/@friendsoftracking755) - Video lectures and tutorials on analysing football tracking data. `Free`
- [LaurieOnTracking](https://github.com/Friends-of-Tracking-Data-FoTD/LaurieOnTracking) - Friends of Tracking tutorial code for working with Metrica tracking data in Python. `Free` · [Details](https://sportsdatastack.com/tools/laurieontracking/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Soccer Analytics Handbook](https://github.com/devinpleuler/analytics-handbook) - Getting-started guide and notebooks for soccer analytics. `Free` · [Details](https://sportsdatastack.com/tools/soccer-analytics-handbook/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data)
- [Soccermatics](https://soccermatics.readthedocs.io/) - Python course material on football analytics by David Sumpter. `Free`

## Leagues Coverage Highlights

Direct sources with verified coverage for each competition (client libraries and scrapers of another source are not counted).

| Competition | Free sources | xG sources (free) | Free sources include |
| --- | --- | --- | --- |
| [Premier League](https://sportsdatastack.com/leagues/premier-league/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 19 | 7 (7 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [La Liga](https://sportsdatastack.com/leagues/la-liga/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 18 | 7 (7 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [Serie A](https://sportsdatastack.com/leagues/serie-a/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 18 | 7 (7 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [Bundesliga](https://sportsdatastack.com/leagues/bundesliga/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 18 | 7 (7 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [Ligue 1](https://sportsdatastack.com/leagues/ligue-1/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 18 | 7 (7 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [MLS (Major League Soccer)](https://sportsdatastack.com/leagues/mls/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 12 | 6 (6 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [American Soccer Analysis](https://www.americansocceranalysis.com/) |
| [Liga MX](https://sportsdatastack.com/leagues/liga-mx/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 8 | 3 (3 free) | [StrikerAPI](https://strikerapi.com/), [FotMob](https://www.fotmob.com/), [football-data.co.uk](https://football-data.co.uk/data.php) |
| [Brasileirão Série A](https://sportsdatastack.com/leagues/brasileirao/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 7 | 2 (2 free) | [StrikerAPI](https://strikerapi.com/), [FotMob](https://www.fotmob.com/), [football-data.co.uk](https://football-data.co.uk/data.php) |
| [Argentine Liga Profesional](https://sportsdatastack.com/leagues/argentina-primera/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 7 | 3 (3 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [UEFA Champions League](https://sportsdatastack.com/leagues/champions-league/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 7 | 4 (4 free) | [StrikerAPI](https://strikerapi.com/), [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/) |
| [FIFA World Cup](https://sportsdatastack.com/leagues/world-cup/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 8 | 3 (3 free) | [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/), [xG Lab](https://xglab.io/) |
| [NWSL](https://sportsdatastack.com/leagues/nwsl/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 6 | 5 (5 free) | [StatsBomb Open Data](https://github.com/hudl/open-data), [StrikerAPI](https://strikerapi.com/), [American Soccer Analysis](https://www.americansocceranalysis.com/) |
| [Women's Super League (WSL)](https://sportsdatastack.com/leagues/wsl/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 5 | 3 (3 free) | [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/), [FootyStats](https://footystats.org/) |
| [Liga F](https://sportsdatastack.com/leagues/liga-f/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 3 | 1 (1 free) | [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/), [API-Football](https://www.api-football.com/) |
| [Liga MX Femenil](https://sportsdatastack.com/leagues/liga-mx-femenil/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 4 | 0 (0 free) | [FotMob](https://www.fotmob.com/), [LIGA Femenil (official site)](https://ligafemenil.mx/), [API-Football](https://www.api-football.com/) |
| [FIFA Women's World Cup](https://sportsdatastack.com/leagues/womens-world-cup/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) | 4 | 1 (1 free) | [StatsBomb Open Data](https://github.com/hudl/open-data), [FotMob](https://www.fotmob.com/), [API-Football](https://www.api-football.com/) |

See the [full league x data-type coverage map](https://sportsdatastack.com/coverage/?utm_source=github&utm_medium=awesome-list&utm_campaign=awesome-soccer-data) for every competition and data type.

## Contributing

Contributions are welcome. Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
Suggest one tool per pull request, with a link to its own site and a neutral one-sentence description.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and related rights to this work. See [LICENSE](LICENSE).
