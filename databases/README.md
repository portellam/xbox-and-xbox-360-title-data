# Databases
Backups and local copies of title data.

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](.README.md)
- [References](../REFERENCES.md)
- [Scripts](../scripts/README.md)

## Table of Contents

- [1. This Directory Table](#1-this-directory-table)
- [2. Backlog](#2-backlog)
- [3. References](#3-references)

## Contents

### 1. This Directory Table

TODO: implement!

| Database File | Functionality | Notes |
| - | - | - |
| | | |

### 2. Backlog

- [ ] add more?

- [ ] (Original) *Xbox* and *Xbox 360:* master database file with following columns:
	1. **Title ID**
	2. **Name**
	3. **Is Xbox**
	4. **Is Xbox 360**
	5. **Is Retail**
	6. **Is XBLA** (Xbox Live Arcade)
	7. **Is Indie** (Xbox 360 only)
  8. **Region** (NTSC/PAL, NA/EU/Asia/AUS)
  8. **Rating** (ESRB, PEGI)

- [ ]  *Xbox* and *Xbox 360:* database file with the following columns:
	1. **Title ID**
	2. **Developer**
	3. **Publisher**
	4. **Genre**
	5. **Max Player Count** (Local, LAN, or Online)
	6. **Has Local Multiplayer** (Cooperative or Split-screen)
	7. **Has LAN Multiplayer** (System Link)
	8. **Has Online Multiplayer** (Xbox Live)
	9. **Release Date** (North America/NTSC-U or main region)

- [ ] *Xbox:* database file with the following columns:
1. **Title ID**
2. **Xenon Fusion (XeFu)** [<sup>\[24\]</sup>](../REFERENCES.md#24) **Revisions and Status** [<sup>\[18\]</sup>](../REFERENCES.md#18)
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

  - Status map: [<sup>\[18\]</sup>](../REFERENCES.md#18)

    | Status | Notes |
    | - | - |
    | 1. Supported  | For officially supported games. |
    | 2. Playable   | For games with very minor or no issues. |
    | 3. In-Game    | For games that you can actually play with issues. |
    | 4. Menus      | For games that will not progress past the menus. |
    | 5. Intro      | For games that will not progress past the boot screens. |
    | 6. Unplayable | For games that do not work. |
    | 7. Untested   | For untested games. |

- [ ] *Xbox 360:* database files:
	1. **Title ID**
	2. **Uses 3D**
	3. **Uses Kinect (required)**
	4. **Uses Kinect (optional)**