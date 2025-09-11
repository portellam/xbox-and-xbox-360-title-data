# Xbox 360 Title README

## Files
- `Parse Xbox 360 Title ID.py`
  - see [#idea-1].

- `xbox_360_title_data_archive.rushhosting.net.csv`
  - no XBLA games
  - incomplete
  - see [#idea-1].

- `xbox_360_title_ids.txt`
  - see [#reference-1].

## References
### Reference 1
source of title IDs:
  - Xbox 360: https://www.gamesdatabase.org/xbox_360_games_list_with_title_ids
    - not complete: has 1,068 titles.
  - XBLA: https://www.gamesdatabase.org/xbox_live_arcade_games_list_with_title_ids
  - original Xbox: N/A
  - has the following:
    - Title ID
    - Game (Name)
    - Developer
    - Category (Genre)
    - (Release) Year (North America?)
### Reference 2
more comprehensive list:
  - https://archive.rushhosting.net/page/1?filter=all
    - for all Xbox 360 titles
  - Indie only: https://archive.rushhosting.net/page/1?filter=37
  - XBLA only: https://archive.rushhosting.net/page/1?filter=23
  - Xbox LIVE only: https://archive.rushhosting.net/page/1?filter=1
  - unknown: https://archive.rushhosting.net/page/1?filter=0
### Reference 3
different list: https://gist.github.com/albertofustinoni/51f2ea0537130f4820a3f5ed49d69042
  - not complete: 2,722
### Reference 4
https://dbox.tools/api/docs
 - has API
 - original Xbox
 - Xbox 360 (physical and digital)
 - Xbox One and later

## Backlog
- [x] attempt #1: get title ID information. [#idea-1]
- [ ] create a method to retrieve title IDs from a website. [#idea-3]
- [ ] local lists for the following platforms:
  1. Original Xbox
  2. Xbox 360
  3. XBLA
  4. Indie
- [ ] local lists for the following parameters:
  1. **Title ID**
	2. **Name**
	3. **Developer**
	4. **Publisher**
	5. **Genre**
	6. **Max Player Count**
	7. **Has Local Multiplayer**
	8. **Has LAN Multiplayer**
	9. **Has Online Multiplayer**
	10. **Uses 3D**
	11. **Uses Kinect (required)**
	12. **Uses Kinect (optional)**
	13. **Release Date (NA/NTSC-U)**
	14. **Release Year**
- [ ] original Xbox list parameters
  1. **Xenon Fusion Emulator Version Compatibility**
    - which version of the backwards compatiblity emulator.
    - emulator for Xbox 360/One/Series
    - best experience possible (at least playable).

## Ideas
### Idea 1
- used python script.
- copy a list from a webpage directly. [#reference-1]
- parsed these title IDs agains [#reference-2].

### Idea 2
- copy parse each new page of a website, saving each hyperlink which contains a Title ID. [#reference-2]

### Idea 3
- parse a JSON. [#reference-4]