# Scripts

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](../databases/README.md)
- [References](../REFERENCES.md)
- [Scripts](./README.md)

## This Directory Table

| Script File | Functionality | Notes |
| - | - | - |
| [`get-xbox-360-compatible-xbox-games_consolemods.org`](./get-xbox-360-compatible-xbox-games_consolemods.org) | Parses HTML and outputs to CSV, JSON. | Lists the best-known compatibility status of each Xbox game on Xbox 360. |
| [`get-xbox-360-games_archive.rushhosting.net.py`](./get-xbox-360-games_archive.rushhosting.net.py) | Parses HTML and outputs to CSV. | Xbox 360 games. Rate limited. Fails every 50 to 100 web requests. |

## Backlog

Last Updated: 2025-09-11

### 1. Not complete

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
  - comprehensive resource.
  - [ ] use API
  - [ ] acquire API
    - This is more courteous.
    - paid ([link](https://www.mobygames.com/api/subscribe/))
    - free ([link](https://www.mobygames.com/user/login/?next=%2Fsubscription-request-form))
  - [ ] scrape webpages
    - *Xbox* ([link](https://www.mobygames.com/game/platform:xbox/sort:title/page:1/))
      - Action only: ([link](https://www.mobygames.com/game/genre:action/platform:xbox/sort:title/page:1/))
    - *Xbox 360* ([link](https://www.mobygames.com/game/platform:xbox360/sort:title/page:1/))
      - Action only: ([link](https://www.mobygames.com/game/genre:action/platform:xbox360/sort:title/page:1/))
	  - [ ] determine if this is feasible?
    - scraper ([link](https://github.com/P-ogg/Game-details/blob/main/Mobygames_api.py))
  - Retrospective: may do both API and scrape. API because it's the right thing to do, and scrape because I like the challenge.

- [ ] *Xbox DB*
  - [link](https://xboxdb.altervista.org/browse)

### 2. Complete