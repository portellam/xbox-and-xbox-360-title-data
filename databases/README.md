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

- [2. Database Coverage](#2-coverage)
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

| Local Database | Remote Database Reference | Parseable? | Accuracy Verified? |
| -------------- | ------------------------- | :--------: | :----------------: |
| <[201]>        | [2][202]                  | No         | No                 |
| <[211]>        | [19][212]                 | Yes        | Yes                |
| <[221]>        | [9][222]                  | Yes        | No                 |
| <[231]>        | [13][232]                 | Yes        | No                 |
| <[241]>        | [10][242]                 | Yes        | No                 |
| <[251]>        | [13][252]                 | Yes        | No                 |
| <[261]>        | [11][262]                 | Yes        | No                 |
| <[271]>        | [12][272]                 | Yes        | No                 |
| <[281]>        | [13][282]                 | Yes        | No                 |
| <[291]>        | [13][292]                 | Yes        | No                 |


[201]: ./csv/archive.rushhosting.net_xbox_360_title_id_list.csv
[202]: ../REFERENCES.md#2

[211]: ./json/consolemods.org_xbox_360_original_xbox_games_compatibility_list_table_6.json
[212]: ../REFERENCES.md#19

[221]: ./json/wikipedia.org_xbox_360_games_a-l_table_2.json
[222]: ../REFERENCES.md#9

[231]: ./json/wikipedia.org_xbox_360_games_a-l_table_4.json
[232]: ../REFERENCES.md#13

[241]: ./json/wikipedia.org_xbox_360_games_m-z_table_2.json
[242]: ../REFERENCES.md#10

[251]: ./json/wikipedia.org_xbox_360_games_m-z_table_4.json
[252]: ../REFERENCES.md#13

[261]: ./json/wikipedia.org_xbox_360_system_link_games_table_1.json
[262]: ../REFERENCES.md#11

[271]: ./json/wikipedia.org_xbox_games_table_1.json
[272]: ../REFERENCES.md#12

[281]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_2.json
[282]: ../REFERENCES.md#13

[291]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_4.json
[292]: ../REFERENCES.md#13

### 3. Database Coverage

The data and metadata coverage of remote databases.

#### 1. Titles

| Platform         | Total Titles Released                                   | Total Titles Unreleased                   |
| ---------------- | ------------------------------------------------------- | ----------------------------------------- |
| Xbox             | 989 <sup>[101]</sup>, or 998 <sup>[103]</sup>           | 57 <sup>[102], or 566 <sup>[104]</sup>    |
| Xbox: XLBA       | 38 <sup>[111]</sup>                                     | 0 <sup>[111]</sup>                        |
| Xbox 360: Apps	 | 572                                                     | unknown                                   |
| Xbox 360: Retail | 2,155 (1,072 <sup>[131]</sup> + 1,080 <sup>[132]</sup>) | 6 (3 <sup>[131]<sup> + 3<sup>[132]</sup>) |
| Xbox 360: Indie  | ?                                                       | unknown                                   |
| Xbox 360: XBLA   | 724 (362 <sup>[131]</sup> + 362 <sup>[132]</sup>)       | >= 1 (GoldenEye)                          |

[101]: ../REFERENCES.md/#12
[102]: https://en.wikipedia.org/wiki/List_of_cancelled_Xbox_games
[103]: https://xbox.fandom.com/wiki/List_of_Xbox_games
[104]: https://xbox.fandom.com/wiki/List_of_Cancelled_Xbox_games

[111]: https://en.wikipedia.org/wiki/Xbox_Live_Arcade

[121]: https://en.wikipedia.org/wiki/List_of_Xbox_360_applications

[131]: ../REFERENCES.md/#09
[132]: ../REFERENCES.md/#10

[151]: https://goldeneye.fandom.com/wiki/GoldenEye_007_(XBLA)


https://en.wikipedia.org/wiki/List_of_cancelled_Xbox_games
https://xbox.fandom.com/wiki/List_of_Xbox_games
https://xbox.fandom.com/wiki/List_of_Cancelled_Xbox_games
https://en.wikipedia.org/wiki/Xbox_Live_Arcade
https://en.wikipedia.org/wiki/List_of_Xbox_360_applications
https://goldeneye.fandom.com/wiki/GoldenEye_007_(XBLA)
https://old.reddit.com/r/xbox360/comments/meey0w/wip_list_of_all_xbox_live_indie_games_xblig/
https://web.archive.org/web/20250615025844/https://old.reddit.com/r/xbox360/comments/meey0w/wip_list_of_all_xbox_live_indie_games_xblig/
https://www.python.org/downloads/

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