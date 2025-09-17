# Databases

## Main Directory

- [README](../README.md)
- [Contributors](../CONTRIBUTORS.md)
- [Databases](./README.md)
- [References](../REFERENCES.md)
- [Scripts](../scripts/README.md)

## Table of Contents

- [1. Disclaimer](#1-disclaimer)
- [2. This Directory](#2-this-directory)

- [3. Database Coverage](#3-database-coverage)
	- [1. Titles](#1-titles)
	- [2. Platforms](#1-platform)
	- [3. Metadata](#2-metadata)
	- [4. Features (General)](#3-features-general)
	- [5. Features (Xbox)](#4-features-xbox)

## Contents

### 1. Disclaimer

The word **"accuracy"** in this context describes as a **ratio** of the presence
of **metadata** for a number of video game titles **relative** to the **total**
number of titles.

The word **"coverage"** in this context describes the **presence** of metadata
attributes (*Name, Developer, Release Date,* and so forth), and **not**
necessarily of the metadata **accuracy.**

### 2. This Directory

| Local Database                                                                        | Remote Database Reference | Parseable? | Accuracy Verified? |
| ------------------------------------------------------------------------------------- | ------------------------- | :--------: | :----------------: |
| <./csv/archive.rushhosting.net_xbox_360_title_id_list.csv>                            | [2][201]                  | No         | No                 |
| <./json/consolemods.org_xbox_360_original_xbox_games_compatibility_list_table_6.json> | [19][202]                 | Yes        | Yes                |
| <./json/wikipedia.org_xbox_360_games_a-l_table_2.json>                                | [9][203]                  | Yes        | No                 |
| <./json/wikipedia.org_xbox_360_games_a-l_table_4.json>                                | [13][204]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_360_games_m-z_table_2.json>                                | [10][205]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_360_games_m-z_table_4.json>                                | [13][206]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_360_system_link_games_table_1.json>                        | [11][207]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_games_table_1.json>                                        | [12][208]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_2.json>               | [13][209]                 | Yes        | No                 |
| <./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_4.json>               | [13][210]                 | Yes        | No                 |

[201]: ../REFERENCES.md#2
[202]: ../REFERENCES.md#19
[203]: ../REFERENCES.md#9
[204]: ../REFERENCES.md#13
[205]: ../REFERENCES.md#10
[206]: ../REFERENCES.md#13
[207]: ../REFERENCES.md#11
[208]: ../REFERENCES.md#12
[209]: ../REFERENCES.md#13
[210]: ../REFERENCES.md#13

### 3. Database Coverage

The data and metadata coverage of remote databases.

#### 1. Titles

| Platform         | Total Titles Released                                     | Total Titles Unreleased                        |
| ---------------- | --------------------------------------------------------- | ---------------------------------------------- |
| Xbox             | 989 <sup>[3101]</sup>, or 998 <sup>[3103]</sup>           | 57 <sup>[3102]</sup>, or 566 <sup>[3104]</sup> |
| Xbox: XLBA       | 38 <sup>[3111]</sup>                                      | 0 <sup>[3111]</sup>                            |
| Xbox 360: Apps	 | 572 <sup>[3121]</sup>                                     | unknown                                        |
| Xbox 360: Retail | 2,155 (1,072 <sup>[3131]</sup> + 1,080 <sup>[3132]</sup>) | 6 (3 <sup>[3131]<sup> + 3<sup>[3132]</sup>)    |
| Xbox 360: Indie  | ?                                                         | unknown                                        |
| Xbox 360: XBLA   | 724 (362 <sup>[3151]</sup> + 362 <sup>[3151]</sup>)       | >= 1 (*GoldenEye 007*) <sup>[3151]<sup>        |

[3101]: ../REFERENCES.md/#12
[3102]: ../REFERENCES.md/#29
[3103]: ../REFERENCES.md/#31
[3104]: ../REFERENCES.md/#32

[3111]: ../REFERENCES.md/#36

[3121]: ../REFERENCES.md/#33

[3131]: ../REFERENCES.md/#09
[3132]: ../REFERENCES.md/#10

[3151]: ../REFERENCES.md/#30

#### 2. Platforms

| Remote Database Reference  | Xbox                  | Xbox on Xbox 360      | Xbox 360: Retail      | Xbox 360: XBLA        | Xbox 360: Indie       | Xbox 360: Apps        |
| -------------------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [1](../REFERENCES.md/#1)  | No                    | No                    | **Yes**               | **Yes**               | ?                     | ?                     |
| [2](../REFERENCES.md/#2)  | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [3](../REFERENCES.md/#3)  | **Yes**               | No                    | No                    | No                    | No                    | No                    |
| [4](../REFERENCES.md/#4)  | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [5](../REFERENCES.md/#5)  | **Yes**               | No                    | No                    | No                    | No                    | No                    |
| [9](../REFERENCES.md/#9)  | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [10](../REFERENCES.md/#10) | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [12](../REFERENCES.md/#12) | **Yes**               | No                    | No                    | No                    | No                    | No                    |
| [13](../REFERENCES.md/#13) | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [14](../REFERENCES.md/#14) | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [15](../REFERENCES.md/#15) | No                    | No                    | No                    | **Yes**               | No                    | No                    |
| [19](../REFERENCES.md/#19) | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [20](../REFERENCES.md/#20) | **Yes**               | No                    | **Yes**               | **Yes**               | No                    | No                    |
| [21](../REFERENCES.md/#21) | No                    | No                    | **Yes**               | **Yes**               | ?                     | ?                     |
| [23](../REFERENCES.md/#23) | No                    | No                    | No                    | **Yes**               | No                    | No                    |
| [24](../REFERENCES.md/#24) | **Yes**               | No                    | No                    | No                    | No                    | No                    |

#### 2. Metadata

 Remote Database Reference   | Title ID              | Name                  | Developer             | Publisher             | Genre                 | Release Date          | Regions               | Rating                |
| -------------------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [1](../REFERENCES.md/#1)  | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [2](../REFERENCES.md/#2)  | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [5](../REFERENCES.md/#5)  | **Yes**               | **Yes**               | No                    | **Yes**               | No                    | No                    | **Yes**               | **Yes**               |
| [11](../REFERENCES.md/#11) | No                    | **Yes**               | No                    | No                    | No                    | No                    | No                    | No                    |
| [12](../REFERENCES.md/#12) | No                    | **Yes**               | **Yes**               | **Yes**               | No                    | **Yes**               | **Yes**               | No                    |
| [13](../REFERENCES.md/#13) | No                    | **Yes**               | No                    | **Yes**               | No                    | No                    | **Yes**               | No                    |
| [14](../REFERENCES.md/#14) | **Yes**               | **Yes**               | No                    | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    |
| [15](../REFERENCES.md/#15) | **Yes**               | **Yes**               | No                    | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    |
| [16](../REFERENCES.md/#16) | **Yes**               | **Yes**               | No                    | **Yes**               | No                    | No                    | **Yes**               | **Yes**               |
| [20](../REFERENCES.md/#20) | **Yes**               | **Yes**               | No                    | No                    | No                    | **Yes**               | No                    | No                    |
| [21](../REFERENCES.md/#21) | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [27](../REFERENCES.md/#27) | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [28](../REFERENCES.md/#28) | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |

#### 3. Features (General)

| Remote Database Reference  | Multiplayer: Local    | Multiplayer: LAN      | Multiplayer: Online   | Player Count: Local   | Player Count: LAN     | Player Count: Online  | 3D Support            | Kinect Supported      | Kinect Required       |
| -------------------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |:--------------------: |:--------------------: |
| [2](../REFERENCES.md/#2)  | **Yes**               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [5](../REFERENCES.md/#5)   | **Yes**               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [9](../REFERENCES.md/#9)  | No                    | No                    | No                    | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [10](../REFERENCES.md/#10) | No                    | No                    | No                    | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [11](../REFERENCES.md/#11) | No                    | **Yes**               | No                    | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [12](../REFERENCES.md/#12) | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [13](../REFERENCES.md/#13) | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [16](../REFERENCES.md/#16) | **Yes**               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [20](../REFERENCES.md/#20) | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [28](../REFERENCES.md/#28) | No                    | **Yes**               | No                    | No                    | No                    | No                    | No                    | No                    | No                    |

#### 4. Features (Xbox)

Xbox features include the following:
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

| Remote Database Reference  | Features (some or none)                 |
| -------------------------- | :-------------------------------------: |
| [2](../REFERENCES.md/#2)  | **Yes**; incomplete: Local, LAN, Online |
| [5](../REFERENCES.md/#5)  | **Yes**; complete                       |
| [11](../REFERENCES.md/#11) | **Yes**; incomplete: LAN                |
| [12](../REFERENCES.md/#12) | No                                      |
| [13](../REFERENCES.md/#13) | No                                      |
| [16](../REFERENCES.md/#16) | **Yes**; complete                       |
| [20](../REFERENCES.md/#20) | No                                      |

##
#### Click [here](#databases) to return to the top of this document.