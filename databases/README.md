# Databases
Backups and local copies of title data.

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](./README.md)
- [References](../REFERENCES.md)
- [Scripts](../scripts/README.md)

## Table of Contents

- [1. This Directory Table](#1-this-directory-table)
- [2. Backlog](#2-backlog)
	- [1. Not complete](#2-not-complete)
	- [2. Complete](#2-complete)

## Contents

### 1. This Directory Table

Last Updated: 2025-09-11

| Database File | Functionality | Notes | Credits |
| - | - | - | - |
| **archive.rushhosting.net**<sup>[JSON][201]</sup> | Includes **Capabilities* (*Coop, SystemLink,* and *Xbox Live*). | Incomplete parse from HTML pages. | [2](../REFERENCES.md#2) |
| **ConsoleMods.org Compatibility List**<sup>[JSON][101] [JSON][102]</sup> | Includes which versions of the *Xenon Fusion (XeFu)*[<sup>\[24\]</sup>](../REFERENCES.md#24) emulator have the best compatibility per title. | Successful parse from HTML table. | [19](../REFERENCES.md#19) |
| **List of Xbox 360 games (A–L)**<sup>[JSON][301]</sup> | Includes *Genres* and *Addons* (*3D support Kinect optional/required, Downloadable titles, Indie,* and *XBLA*). | Successful parse from HTML table. | [9](../REFERENCES.md#9) |
| **List of Xbox 360 games (A–L): Cancelled games**<sup>[JSON][302]</sup> | Same as above. | Successful parse from HTML table. | Same as above. |
| **List of Xbox 360 games (M–Z)**<sup>[JSON][401]</sup> | Same as above. | Successful parse from HTML table. | [10](../REFERENCES.md#10) |
| **List of Xbox 360 games (M–Z): Cancelled games**<sup>[JSON][402]</sup> | Same as above. | Successful parse from HTML table. | Same as above. |
| **List of Xbox 360 System Link games**<sup>[JSON][501]</sup> | Includes *Total players, Per console, Versus mode,* and *Co-op mode*. | Successful parse from HTML table. | [11](../REFERENCES.md#11) |
| **List of Xbox games**<sup>[JSON][601]</sup> | - | Successful parse from HTML table. | [12](../REFERENCES.md#12) |
| **List of Xbox games compatible with Xbox 360**<sup>[JSON][701]</sup> | Includes *Technical Issues*. | Successful parse from HTML table. | [13](../REFERENCES.md#13) |
| **List of Xbox titles removed from backward compatibility list**<sup>[JSON][702]</sup> | Includes *Date Available, Date Removed,* and *Technical Issues*. | Successful parse from HTML table. | Same as above. |

[101]: ./json/consolemods.org_xbox_360_original_xbox_games_compatibility_list.json

[201]: ./json/archive.rushhosting.net_xbox_360_title_id_list.json

[301]: ./json/wikipedia.org_xbox_360_games_a-l_table_1.json
[302]: ./json/wikipedia.org_xbox_360_games_a-l_table_2.json

[401]: ./json/wikipedia.org_xbox_360_games_m-z_table_1.json
[402]: ./json/wikipedia.org_xbox_360_games_m-z_table_2.json

[501]: ./json/wikipedia.org_xbox_360_system_link_games_table_1.json

[601]: ./json/wikipedia.org_xbox_games_table_1.json

[701]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_1.json
[702]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_2.json

### 2. Backlog

Last Updated: 2025-09-11

#### 1. Not complete

- [ ] add more?

- [ ] *Xbox* and *Xbox 360:* master database file with following columns:
	1. **Title ID**
	2. **Name**
	3. **Is Xbox**
	4. **Is Xbox 360**
	5. **Is Retail**
	6. **Is XBLA** (Xbox Live Arcade)
	7. **Region** (NTSC/PAL, Americas/Europe/Asia/Australia)

- [ ]  *Xbox* and *Xbox 360:* database file with the following columns:
1. **Title ID**
2. **Developer**
3. **Publisher**
4. **Genre**
5. **Max Player Count** (Local, LAN, or Online)
6. **Has Multiplayer**
	1. **Has Local** (Cooperative or Split-screen)
	2. **Has LAN** (System Link)
	3. **Has Online** (Xbox Live)
7. **Release Date**
8. **Rating** (ESRB, PEGI)

- [ ] *Xbox* only: database file with the following columns:
1. **Title ID**
2. **Xenon Fusion (XeFu)** [<sup>\[25\]</sup>](../REFERENCES.md#25) **Revisions and Status** [<sup>\[19\]</sup>](../REFERENCES.md#19)
	1. **v1**
	2. **v2**
	3. **v3**
	4. **v5**
	5. **v1_1**
	6. **v6**
	7. **v7**
	8. **v7b**
	9. **2019**
	10. **2021a**
	11. **2021b**
	12. **2021c**

  - Status map: [<sup>\[19\]</sup>](../REFERENCES.md#19)

    | Status | Notes |
    | - | - |
    | 1. Supported  | For officially supported games. |
    | 2. Playable   | For games with very minor or no issues. |
    | 3. In-Game    | For games that you can actually play with issues. |
    | 4. Menus      | For games that will not progress past the menus. |
    | 5. Intro      | For games that will not progress past the boot screens. |
    | 6. Unplayable | For games that do not work. |
    | 7. Untested   | For untested games. |

- [ ] *Xbox 360* only: database files:
	1. **Title ID**
	2. **Is Indie** (Xbox 360 only)
	3. **Uses 3D**
	4. **Uses Kinect (required)**
	5. **Uses Kinect (optional)**

#### 2. Complete

- [x] *Xbox* and *Xbox 360:* found one (1) or more database(s) which have the following fields (in one form or another):
	1.  [x] **Title ID**
	2.  [x] **Name**
	3.  [x] **Is Xbox**
	4.  [x] **Is Xbox 360**
	5.  [x] **Is Retail**
	6.  [x] **Is XBLA** (Xbox Live Arcade)
	7.  [x] **Region** (NTSC/PAL, Americas/Europe/Asia/Australia)
	8.  [x] **Developer**
	9.  [x] **Publisher**
	10. [x] **Genre**
	11. [x] **Max Player Count** (Local, LAN, or Online)
	12. [x] **Has Local** (Cooperative or Split-screen)
	13. [x] **Has LAN** (System Link)
	14. [x] **Has Online** (Xbox Live)
	15. [x] **Release Date**
	16. [x] **Rating** (ESRB, PEGI)

- [x] *Xbox* only: found one (1) or more database(s) which have the following fields (in one form or another):
	1.  [x] **XeFu v1**
	2.  [x] **v2**
	3.  [x] **v3**
	4.  [x] **v5**
	5.  [x] **v1_1**
	6.  [x] **v6**
	7.  [x] **v7**
	8.  [x] **v7b**
	9.  [x] **2019**
	10. [x] **2021a**
	11. [x] **2021b**
	12. [x] **2021c**

- [x] *Xbox 360* only: found one (1) or more database(s) which have the following fields (in one form or another):
	1. [x] **Is Indie** (Xbox 360 only)
	2. [x] **Uses 3D**
	3. [x] **Uses Kinect (required)**
	4. [x] **Uses Kinect (optional)**