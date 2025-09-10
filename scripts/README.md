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

- [ ] cron job to upload latest database files to this repo.
- [ ] individual script files for each resource.
  - [ ] fix `get-xbox-360-games_archive.rushhosting.net.py`
- [ ] master script file
  - [ ] aggregates each resource's database
  - [ ] set priority given trust (or lack of trust) with regards to accuracy of records.
- [ ] add more