# Scripts

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](../databases/README.md)
- [References](../REFERENCES.md)
- [Scripts](./README.md)

## Table of Contents

- [1. This Directory](#1-this-directory)
- [2. Legal & Usage Directives/Notes](#2-legal--usage-directivesnotes)
  - [1. General Best Practices](#1-general-best-practices)
  - [2. Google Sheets API Usage](#2-google-sheets-api-usage)
  - [3. Wikipedia Usage](#3-wikipedia-usage)
  - [4. Generic Wiki Usage](#4-generic-wiki-usage)
  - [5. ConsoleMods.org Usage](#5-consolemodsorg-usage)

## Contents

### 1. This Directory

| Script                                          | Remote Database                 | Status                                                                        |
| ----------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------- |
| [`./src/get_this_database.py`][100A]            | any remote database file        | Working.                                                                      |
| [`./src/get_wiki_table.py`][100B]               | any Wiki powered webpage        | Working.                                                                      |
| -                                               | [1],  [21]                      | -                                                                             |
| [`./src/get_rushhosting.net_database.py`][1002] | [2]                             | Developing. Suffers timeouts. Fails every 50 to 100 web requests.             |
| [`./src/get_many_databases.py`][1003]           | [3],  [5],  [6]                 | Working. For SQL query statement(s), see [`./src/config_databases.py`][1103]. |
| [`./src/get_wikipedia_tables.py`][1009]         | [9],  [10],  [11],  [12],  [13] | Developing. Does not parse sub headers correctly.                             |
| -                                               | [14],  [15]                     | -                                                                             |
| [`./src/get_consolemods_table.py`][1019]        | [19]                            | Working.                                                                      |
| -                                               | [22]                            | -                                                                             |
| -                                               | [23]                            | -                                                                             |
| -                                               | [27]                            | -                                                                             |
| -                                               | [28]                            | -                                                                             |
| -                                               | [29]                            | -                                                                             |
| -                                               | [32]                            | -                                                                             |
| -                                               | [33]                            | -                                                                             |
| [`./src/get_google_sheets.py`][1035]            | [35]                            | Working.                                                                      |
| -                                               | [36]                            | -                                                                             |

[100A]: ./src/get_this_database.py
[100B]: ./src/get_wiki_table.py
[1002]: ./src/get_rushhosting.net_database.py
[1003]: ./src/get_many_databases.py
[1103]: ./src/config_databases.py
[1009]: ./src/get_wikipedia_tables.py
[1019]: ./src/get_consolemods_table.py
[1035]: ./src/get_google_sheets.py

### 2. Legal & Usage Directives/Notes

#### 1. General Best Practices

- Add delays between requests (greater than one ( ≥1 ) second).
- Cache results to minimize server load.
- Document your data sources and usage in publications.
- Handle errors gracefully without retry loops.

#### 2. Google Sheets API Usage

- Do not use for unauthorized data collection.
- Follow Google's [*Terms of Use*][2200].
- Only works with sheets shared publicly ("Anyone with link").
- Rate limited to about thirty ( ~30 ) requests/minute to respect quotas.
- Respect sheet owners' terms and privacy settings.
- Respect the [`robots.txt`][2201].

- The following tools use Google's free public Sheets API:
  - [`./src/get_google_sheets.py`][1035]

[2200]: https://developers.google.com/terms
[2201]: https://google.com/robots.txt

#### 3. Wikipedia Usage

- Content is CC BY-SA 3.0 - attribute Wikipedia as source.
- Follow Wikimedia [*Terms of Use*][2300].
- Include original article links in redistributed data.
- Maximum two-hundred (200) requests/second, six-thousand (6,000) requests/day.
- Respect the [`robots.txt`][2301].

- The following tools apply:
  - [`./src/get_wikipedia_tables.py`][1009]

[2300]: https://foundation.wikimedia.org/wiki/Terms_of_Use
[2301]: https://www.wikipedia.org/robots.txt

#### 4. Generic Wiki Usage

- Always check target wiki's `robots.txt` and *Terms of Service*.
- Use conservative rate limiting (less than one ( ≤1 ) request/second).
- Attribute original sources properly.
- Respect each wiki's specific policies.

- The following tools apply:
  - [`./src/get_wiki_table.py`][100B]

#### 5. ConsoleMods.org Usage

- Include attribution when redistributing data.
- Non-commercial research use only.
- Rate limit to one (1) request/second.
- Respect the [`robots.txt`][2500].

- The following tools apply:
  - [`./src/get_wikipedia_tables.py`][1019]

[2500]: https://www.consolemods.org/robots.txt

##
#### Click [here](#scripts) to return to the top of this document.

[1]: ../REFERENCES.md/#1
[2]: ../REFERENCES.md/#2
[3]: ../REFERENCES.md/#3
[4]: ../REFERENCES.md/#4
[5]: ../REFERENCES.md/#5
[6]: ../REFERENCES.md/#6
[7]: ../REFERENCES.md/#7
[8]: ../REFERENCES.md/#8
[9]: ../REFERENCES.md/#9
[10]: ../REFERENCES.md/#10
[11]: ../REFERENCES.md/#11
[12]: ../REFERENCES.md/#12
[13]: ../REFERENCES.md/#13
[14]: ../REFERENCES.md/#14
[15]: ../REFERENCES.md/#15
[16]: ../REFERENCES.md/#16
[17]: ../REFERENCES.md/#17
[18]: ../REFERENCES.md/#18
[19]: ../REFERENCES.md/#19
[20]: ../REFERENCES.md/#20
[21]: ../REFERENCES.md/#21
[22]: ../REFERENCES.md/#22
[23]: ../REFERENCES.md/#23
[24]: ../REFERENCES.md/#24
[25]: ../REFERENCES.md/#25
[26]: ../REFERENCES.md/#26
[27]: ../REFERENCES.md/#27
[28]: ../REFERENCES.md/#28
[29]: ../REFERENCES.md/#29
[30]: ../REFERENCES.md/#30
[31]: ../REFERENCES.md/#31
[32]: ../REFERENCES.md/#32
[33]: ../REFERENCES.md/#33
[34]: ../REFERENCES.md/#34
[35]: ../REFERENCES.md/#35
[36]: ../REFERENCES.md/#36
[37]: ../REFERENCES.md/#37
[38]: ../REFERENCES.md/#38