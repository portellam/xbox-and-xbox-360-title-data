# Scripts

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Coverage](../COVERAGE.md)
- [Databases](../databases/README.md)
- [References](../REFERENCES.md)
- [Scripts](./README.md)

## Table of Contents

- [1. This Directory Table](#1-this-directory-table)
- [2. Backlog](#2-backlog)
  - [1. Not complete](#2-not-complete)
  - [2. Complete](#2-complete)

## Contents

### 1. This Directory Table

| Script                                                                         | Function                                     | Status                                                        |
| ------------------------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------- |
| [`./src/get_consolemods_tables.py`](./src/get_consolemods_tables.py)           | Parses HTML, converts to JSON.               | Working.                                                      |
| [`./get_rushhosting_data.py`](./get-xbox-360-games_archive.rushhosting.net.py) | Queries URL, aggregates HTML, converts JSON. | Developing. Rate limited. Fails every 50 to 100 web requests. |
| [`./src/get_wikipedia_tables.py`](./src/get_wikipedia_tables.py)               | Parses HTML, converts to JSON.               | Working.                                                      |

### 2. Backlog

#### 1. Not complete

- [ ] add more

- [ ] cron job to upload latest database files to this repo.

- [ ] individual script files for each resource.
  - [ ] fix `get-xbox-360-games_archive.rushhosting.net.py`

- [ ] master script file
  - [ ] aggregates each resource's database
  - [ ] set priority given trust (or lack of trust) with regards to accuracy of records.

- [ ] *Mobcat*[<sup>[15]</sup>](../REFERENCES.md#15)
  - has API.

- [ ] *Moby Games*
  - [ ] Use API.
    - Note: this is more courteous.
    - API scraper ([link](https://github.com/P-ogg/Game-details/blob/main/Mobygames_api.py))
  - [ ] Acquire API.
    - Paid API ([link](https://www.mobygames.com/api/subscribe/))
    - Free API ([link](https://www.mobygames.com/user/login/?next=%2Fsubscription-request-form))
  - [ ] scrape webpages
    - *Xbox* ([link](https://www.mobygames.com/game/platform:xbox/sort:title/page:1/))
      - Action only: ([link](https://www.mobygames.com/game/genre:action/platform:xbox/sort:title/page:1/))
    - *Xbox 360* ([link](https://www.mobygames.com/game/platform:xbox360/sort:title/page:1/))
      - Action only: ([link](https://www.mobygames.com/game/genre:action/platform:xbox360/sort:title/page:1/))
  - Review: Comprehensive resource.
  - Retrospective: may do both API and scrape. API because it's the right thing to do, and scrape because I like the challenge.

- [ ] *Xbox DB*[<sup>[20]</sup>](../REFERENCES.md#20)
  - Free API [<sup>[1]</sup>](../REFERENCES.md#1)
  - [ ] Use API.

#### 2. Complete

N/A

##
#### Click [here](#scripts) to return to the top of this document.