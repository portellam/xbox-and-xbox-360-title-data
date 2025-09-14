#!/usr/bin/env python

#
# Filename:       config_consolemods.py
# Description:    A table to parse from `www.consolemods.org`.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

URL = (
  "https://consolemods.org/wiki/Xbox_360:Original_Xbox_Games_Compatibility_List/en"
)

OUTPUT_PATH = "../../databases/json/"

OUTPUT_FILE_NAME = (
  f"{OUTPUT_PATH}consolemods.org_xbox_360_original_xbox_games_compatibility_list"
)

HEADER_KEY_LIST = [
  "Name",
  "1",
  "2",
  "3",
  "5",
  "1_1",
  "6",
  "7",
  "7b",
  "19",
  "21a",
  "21b",
  "21c",
  "Known Issues",
  "Tested By"
]

HEADER_MAP = {
  "1": "xefu",
  "2": "xefu2",
  "3": "xefu3",
  "5": "xefu5",
  "1_1": "xefu1_1",
  "6": "xefu6",
  "7": "xefu7",
  "7b": "xefu7b",
  "19": "xefu2019",
  "21a": "xefu2021a",
  "21b": "xefu2021b",
  "21c": "xefu2021c"
}

ELEMENT_TAG_LIST = [
  "th",
  "td"
]

STATUS_MAP = {
  "supported":   "supported",
  "playable":    "playable",
  "ingame":      "in-game",
  "in-game":     "in-game",
  "orange":      "menus",
  "intro":       "in-game",
  "unplayable":  "unplayable",
  "untested":    "untested",
}