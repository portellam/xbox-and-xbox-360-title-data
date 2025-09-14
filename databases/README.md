# Databases

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](./README.md)
- [References](../REFERENCES.md)
- [Scripts](../scripts/README.md)

## Table of Contents

- [1. This Directory Table](#1-this-directory-table)

- [2. Coverage](#2-coverage)
	- [1. Platforms](#1-platform)
	- [2. Metadata](#2-metadata)
	- [3. Features (General)](#3-features-general)
	- [4. Features (Xbox)](#4-features-xbox)

## Contents

### 1. This Directory Table

| Local Database                                                                          | Reference Database        | Notes                             |
| --------------------------------------------------------------------------------------- | ------------------------- | --------------------------------- |
| **archive.rushhosting.net** <sup>[CSV][201]</sup>                                       | [2](../REFERENCES.md#02)  | Incomplete parse from HTML pages. |
| **ConsoleMods.org Compatibility List** <sup>[JSON][101]</sup>                           | [19](../REFERENCES.md#19) | Columns good, data verified.      |
| **List of Xbox 360 games (A–L)** <sup>[JSON][301]</sup>                                 | [9](../REFERENCES.md#9)   | Columns good, data not verified.  |
| **List of Xbox 360 games (A–L): Cancelled games** <sup>[JSON][302]</sup>                | Same as above.            | Columns good, data not verified.  |
| **List of Xbox 360 games (M–Z)** <sup>[JSON][401]</sup>                                 | [10](../REFERENCES.md#10) | Columns good, data not verified.  |
| **List of Xbox 360 games (M–Z): Cancelled games** <sup>[JSON][402]</sup>                | Same as above.            | Columns good, data not verified.  |
| **List of Xbox 360 System Link games** <sup>[JSON][501]</sup>                           | [11](../REFERENCES.md#11) | Columns good, data not verified.  |
| **List of Xbox games** <sup>[JSON][601]</sup>                                           | [12](../REFERENCES.md#12) | Columns good, data not verified.  |
| **List of Xbox games compatible with Xbox 360** <sup>[JSON][701]</sup>                  | [13](../REFERENCES.md#13) | Columns good, data not verified.  |
| **List of Xbox titles removed from backward compatibility list** <sup>[JSON][702]</sup> | Same as above.            | Columns good, data not verified.  |

[101]: ./json/consolemods.org_xbox_360_original_xbox_games_compatibility_list_table_6.json

[201]: ./csv/archive.rushhosting.net_xbox_360_title_id_list.csv

[301]: ./json/wikipedia.org_xbox_360_games_a-l_table_2.json
[302]: ./json/wikipedia.org_xbox_360_games_a-l_table_4.json

[401]: ./json/wikipedia.org_xbox_360_games_m-z_table_2.json
[402]: ./json/wikipedia.org_xbox_360_games_m-z_table_4.json

[501]: ./json/wikipedia.org_xbox_360_system_link_games_table_1.json

[601]: ./json/wikipedia.org_xbox_games_table_1.json

[701]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_2.json
[702]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_4.json

### 2. Coverage

#### 1. Platforms

| Reference Database        | Xbox                  | Xbox: Xbox 360        | Xbox 360: Retail      | Xbox 360: XBLA        | Xbox 360: Indie       | Xbox 360: Apps        |
| ------------------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [2](./REFERENCES.md/#02)  | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [3](./REFERENCES.md/#03)  | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [4](./REFERENCES.md/#04)  | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [5](./REFERENCES.md/#05)  | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [9](./REFERENCES.md/#09)  | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [12](./REFERENCES.md/#12) | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [13](./REFERENCES.md/#13) | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [14](./REFERENCES.md/#14) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[x]</li></ul> |
| [15](./REFERENCES.md/#15) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [19](./REFERENCES.md/#19) | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [20](./REFERENCES.md/#20) | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [23](./REFERENCES.md/#23) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [24](./REFERENCES.md/#24) | <ul><li>[x]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |

#### 2. Metadata

| Reference Database        | Title ID | Name  | Developer | Publisher | Genre | Release Date | Regions | Rating |
| ------------------------- | :------- | :---: | :-------: | :-------: | :---: | :----------: | :-----: | :----: |
| [2](./REFERENCES.md/#2)   | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [5](./REFERENCES.md/#5)   | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [11](./REFERENCES.md/#11) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [12](./REFERENCES.md/#12) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [13](./REFERENCES.md/#13) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [16](./REFERENCES.md/#16) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [20](./REFERENCES.md/#20) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |

#### 3. Features (General)

| Reference Database        | Player Count: Local   | Player Count: LAN     | Player Count: Online  | 3D Support            | Kinect Supported      | Kinect Required       |
| ------------------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [2](./REFERENCES.md/#2)   | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [5](./REFERENCES.md/#5)   | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [11](./REFERENCES.md/#11) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [12](./REFERENCES.md/#12) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [13](./REFERENCES.md/#13) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [16](./REFERENCES.md/#16) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |
| [20](./REFERENCES.md/#20) | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> | <ul><li>[ ]</li></ul> |

#### 4. Features (Xbox)

**Notice:** includes the following
- Communicator Headset
- Content Download
- Custom Soundtracks
- Dolby Digital Surround
- Friends
- HDTV (Resolutions: 480p, 720p, 1080i)
- Memory Unit Size (Blocks)
- Multiplayer Count: Local
- Multiplayer Count: LAN
- Multiplayer: Online
- Scoreboards
- Voice

| Reference Database        | Features (some or none)                              |
| ------------------------- | :--------------------------------------------------: |
| [2](./REFERENCES.md/#2)   | <ul><li>[x]</li></ul> incomplete: Local, LAN, Online |
| [5](./REFERENCES.md/#5)   | <ul><li>[x]</li></ul> complete                       |
| [11](./REFERENCES.md/#11) | <ul><li>[x]</li></ul> incomplete: LAN                |
| [12](./REFERENCES.md/#12) | <ul><li>[ ]</li></ul>                                |
| [13](./REFERENCES.md/#13) | <ul><li>[ ]</li></ul>                                |
| [16](./REFERENCES.md/#16) | <ul><li>[x]</li></ul> complete                       |
| [20](./REFERENCES.md/#20) | <ul><li>[ ]</li></ul>                                |

##
#### Click [here](#databases) to return to the top of this document.