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
	- [5. Features (*Xbox*)](#4-features-xbox)

## Contents

### 1. Disclaimer

- The word **"entry"** or "record" in this context is a given video game title's
metadata.

- The word **field"** or "attribute" in this context is an individual key and value
of metadata. For example: `Name: "Halo 3"`

- The word **"coverage"** in this context describes the **presence** of all valid
**fields** on a local database from a remote database.

- The word **"parity"** in this context describes the **ratio** of the
**presence** of **entries** on a local database relative to a remote database.

### 2. This Directory

| Local Database                                                                                                                                                                        | Remote           | Has Coverage? | Has Parity? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | :-----------: | :---------: |
| -                                                                                                                                                                                     | [1],  [21]       | -             | -           |
| `archive.rushhosting.net` <sup>[CSV][20002]</sup>                                                                                                                                     | [2]              | **Yes**       | No          |
| -                                                                                                                                                                                     | [3],  [5],  [16] | -             | -           |
| -                                                                                                                                                                                     | [4]              | -             | -           |
| `Wikipedia \| List of Xbox 360 games (A-L)` <sup>[JSON][20109]</sup>                                                                                                                  | [9]              | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox 360 games (A-L): Cancelled games` <sup>[JSON][20119]</sup>                                                                                                 | [9]              | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox 360 games (M-Z)` <sup>[JSON][20110]</sup>                                                                                                                  | [10]             | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox 360 games (M-Z): Cancelled games` <sup>[JSON][20110]</sup>                                                                                                 | [10]             | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox 360 System Link games` <sup>[JSON][20111]</sup>                                                                                                            | [11]             | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox games` <sup>[JSON][20112]</sup>                                                                                                                            | [12]             | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox games compatible with Xbox 360` <sup>[JSON][20113]</sup>                                                                                                   | [13]             | **Yes**       | **Yes**     |
| `Wikipedia \| List of Xbox games compatible with Xbox 360: List of Xbox titles removed from backward compatibility list` <sup>[JSON][21113]</sup>                                     | [13]             | **Yes**       | **Yes**     |
| -                                                                                                                                                                                     | [14]             | -             | -           |
| -                                                                                                                                                                                     | [15]             | -             | -           |
| `consolemods.org \| Original Xbox Games Compatibility List` <sup>[JSON][20119]</sup>                                                                                                  | [19]             | **Yes**       | **Yes**     |
| -                                                                                                                                                                                     | [22]             | -             | -           |
| -                                                                                                                                                                                     | [23]             | -             | -           |
| -                                                                                                                                                                                     | [27]             | -             | -           |
| -                                                                                                                                                                                     | [28]             | -             | -           |
| `Wikipedia \| List of Cancelled Xbox games` <sup>[JSON][20129]</sup>                                                                                                                  | [29]             | -             | -           |
| `xbox.fandom.com \| List of Cancelled Xbox games` <sup>[JSON][20131]</sup>                                                                                                            | [31]             | No            | No          |
| `xbox.fandom.com \| List of Xbox games` <sup>[JSON][20132]</sup>                                                                                                                      | [32]             | No            | No          |
| `Wikipedia \| List of Xbox 360 applications` <sup>[JSON][20133]</sup>                                                                                                                 | [33]             | -             | -           |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: Not XBLIG Games` <sup>[CSV][20035]</sup>                                                                                        | [35]             | **Yes**       | **Yes**     |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: Other XNA Projects` <sup>[CSV][21035]</sup>                                                                                     | [35]             | **Yes**       | **Yes**     |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: Pre-launch titles` <sup>[CSV][22035]</sup>                                                                                      | [35]             | **Yes**       | **Yes**     |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: Unreleased cancelled Games` <sup>[CSV][23035]</sup>                                                                             | [35]             | **Yes**       | **Yes**     |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: XNA Starter Kits & Mini Games` <sup>[CSV][24035]</sup>                                                                          | [35]             | **Yes**       | **Yes**     |
| `Google Sheets \| WIP: List of Xbox Live Indie Games: XNAProjects` <sup>[CSV][25035]</sup>                                                                                            | [35]             | **Yes**       | **Yes**     |
| -                                                                                                                                                                                     | [36]             | -             | -           |

[20002]: ./csv/archive.rushhosting.net_xbox_360_title_id_list.csv
[20109]: ./json/wikipedia.org_xbox_360_games_a-l_table_2.json
[21109]: ./json/wikipedia.org_xbox_360_games_a-l_table_4.json
[20110]: ./json/wikipedia.org_xbox_360_games_m-z_table_2.json
[21110]: ./json/wikipedia.org_xbox_360_games_m-z_table_4.json
[20111]: ./json/wikipedia.org_xbox_360_system_link_games_table_1.json
[20112]: ./json/wikipedia.org_xbox_games_table_1.json
[20113]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_2.json
[21113]: ./json/wikipedia.org_xbox_games_compatible_with_xbox_360_table_4.json
[20119]: ./json/consolemods.org_xbox_360_original_xbox_games_compatibility_list_table_6.json
[20129]: ./json/wikipedia.org_list_of_cancelled_xbox_games_table_1.json
[20131]: ./json/xbox.fandom.com_list_of_cancelled_xbox_games_table_1.json
[20132]: ./json/xbox.fandom.com_list_of_xbox_games_table_1.json
[20133]: ./json/wikipedia.org_list_of_xbox_360_applications_table_1.json
[20035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_Not_XBLIG_Games.csv
[21035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_Other_XNA_Projects.csv
[22035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_Pre-launch_titles.csv
[23035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_Unreleased_cancelled_Games.csv
[24035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_XNA_Starter_Kits_&_Mini_Games.csv
[25035]: ./csv/WIP__List_of_Xbox_Live_Indie_Games_-_XNAProjects.csv

### 3. Database Coverage

The data and metadata coverage of remote databases.

#### 1. Titles

| Platform         | Released                                             | Unreleased                                 | Notes                                                                                                      |
| ---------------- | ---------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Xbox             | 989 <sup>[12]</sup>, or 998 <sup>[29]</sup>          | 57 <sup>[31]</sup>, or 566 <sup>[32]</sup> | -                                                                                                          |
| Xbox: XLBA       | 38 <sup>[36]</sup>                                   | 0 <sup>[36]</sup>                          | -                                                                                                          |
| Xbox 360: Retail | 2,152 (1,072 <sup>[9]</sup> + 1,080 <sup>[10]</sup>) | 6 (3 <sup>[9]</sup> + 3 <sup>[10]</sup>)   | Website reports 2,155, counted 2,152. Viewed HTML and counted `<tr>` tags. <sup>[9]</sup>  <sup>[10]</sup> |
| Xbox 360: XBLA   | 724 (362 <sup>[30]</sup> + 362 <sup>[30]</sup>)      | >= 1                                       | at least one exists: *GoldenEye 007* <sup>[30]</sup>                                                       |
| Xbox 360: Indie  | 3,596 <sup>[35]</sup>                                | 165 <sup>[35]</sup>                        | Pre-launch: 9; XNA Starter Kits: 19; XNA Projects: 28; Other: 20. <sup>[35]</sup>                          |
| Xbox 360: Apps   | 572 <sup>[33]</sup>                                  | unknown                                    | -                                                                                                          |

#### 2. Platforms

| Remote           | Xbox                  | Xbox on Xbox 360      | Xbox 360: Retail      | Xbox 360: XBLA        | Xbox 360: Indie       | Xbox 360: Apps        |
| ---------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [1],  [21]       | No                    | No                    | **Yes**               | **Yes**               | ?                     | ?                     |
| [2]              | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [3],  [5],  [16] | **Yes**               | No                    | No                    | No                    | No                    | No                    |
| [4]              | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [9]              | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [10]             | No                    | No                    | **Yes**               | No                    | No                    | No                    |
| [12]             | **Yes**               | No                    | No                    | No                    | No                    | No                    |
| [13]             | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [14]             | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [15]             | No                    | No                    | No                    | **Yes**               | No                    | No                    |
| [19]             | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [20]             | **Yes**               | No                    | **Yes**               | **Yes**               | No                    | No                    |
| [23]             | No                    | No                    | No                    | **Yes**               | No                    | No                    |
| [24]             | **Yes**               | No                    | No                    | No                    | No                    | No                    |

#### 2. Metadata

 Remote            | Title ID              | Name                  | Developer             | Publisher             | Genre                 | Release Date          | Regions               | Maturity Rating       |
| ---------------- | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |
| [1],  [21]       | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [2]              | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [3],  [5],  [16] | **Yes**               | **Yes**               | No                    | **Yes**               | No                    | No                    | **Yes**               | **Yes**               |
| [11]             | No                    | **Yes**               | No                    | No                    | No                    | No                    | No                    | No                    |
| [12]             | No                    | **Yes**               | **Yes**               | **Yes**               | No                    | **Yes**               | **Yes**               | No                    |
| [13]             | No                    | **Yes**               | No                    | **Yes**               | No                    | No                    | **Yes**               | No                    |
| [14],  [15]      | **Yes**               | **Yes**               | No                    | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    |
| [20]             | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | **Yes**               | No                    | No                    |
| [27]             | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [28]             | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |

#### 3. Features (General)

| Remote            | Multiplayer: Local    | Multiplayer: LAN      | Multiplayer: Online   | Player Count: Local   | Player Count: LAN     | Player Count: Online  | 3D Support            | Kinect Supported      | Kinect Required       |
| ----------------  | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: | :-------------------: |:--------------------: |:--------------------: |
| [2]               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [3],  [5],  [16]  | **Yes**               | **Yes**               | **Yes**               | **Yes**               | **Yes**               | No                    | No                    | No                    | No                    |
| [9]               | No                    | No                    | No                    | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [10]              | No                    | No                    | No                    | No                    | No                    | No                    | **Yes**               | **Yes**               | **Yes**               |
| [11]              | No                    | **Yes**               | No                    | No                    | **Yes**               | No                    | No                    | No                    | No                    |
| [12]              | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [13]              | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [20]              | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    | No                    |
| [28]              | No                    | **Yes**               | No                    | No                    | No                    | No                    | No                    | No                    | No                    |

#### 4. Features (*Xbox*)

*Xbox* features include the following:
- Communicator Headset
- Content Download
- Custom Soundtracks
- Dolby Digital Surround
- Friends
- HDTV (Resolutions: 480p, 720p, 1080i)
- Memory Unit Size (Blocks)
- Multiplayer Count: Local (Coop)
- Multiplayer Count: LAN (System Link)
- Multiplayer: Online (*Xbox Live*)
- Scoreboards
- Voice

| Remote     | Has Features?                            |
| ---------- | :--------------------------------------: |
| [2]        |  **Yes**; incomplete: Local, LAN, Online |
| [5],  [16] | **Yes**; complete                        |
| [11]       | **Yes**; incomplete: LAN                 |
| [12]       | No                                       |
| [13]       | No                                       |
| [20]       | No                                       |

##
#### Click [here](#databases) to return to the top of this document.

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