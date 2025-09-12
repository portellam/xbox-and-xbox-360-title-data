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

OUTPUT_PATH = "../../databases/"

OUTPUT_FILE_NAME = (
  f"{OUTPUT_PATH}consolemods.org_xbox_360_original_xbox_games_compatibility_list"
)

HEADER_KEY_LIST = [
  "Name",
  "xefu",
  "xefu2",
  "xefu3",
  "xefu5",
  "xefu1_1",
  "xefu6",
  "xefu7",
  "xefu7b",
  "xefu2019",
  "xefu2021a",
  "xefu2021b",
  "xefu2021c",
  "Tested By",
  "Known Issues"
]

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
  "intro":       "intro",
  "unplayable":  "unplayable",
  "untested":    "untested",
}