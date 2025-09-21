#!/usr/bin/env python

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# THIRD PARTY NOTICES:
#
# This software accesses content from www.consolemods.org for personal,
# non-commercial research and archival purposes only. You must comply with the
# ConsoleMods.org Terms of Service
# (https://www.consolemods.org/wiki/Terms_of_Service) and robots.txt file
# (https://www.consolemods.org/robots.txt).
#
# ConsoleMods.org and related trademarks are property of their respective owners.
# This software is not affiliated with, endorsed by, or sponsored by
# ConsoleMods.org.
#
# USAGE RESTRICTIONS:
#
# • Respect rate limits and robots.txt directives.
# • Do not use for commercial purposes without explicit permission.
# • Do not overload or disrupt consolemods.org services.
# • Only access publicly available data.
# • Include appropriate attribution to ConsoleMods.org when redistributing data.
#
# ROBOTS.TXT COMPLIANCE NOTICE:
#
# This script respects the ConsoleMods.org robots.txt file. Certain paths may be
# disallowed. Always check https://www.consolemods.org/robots.txt before use.
#

#
# Filename:       config_consolemods.py
# Description:    A table to parse from `www.consolemods.org`.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

from config import (
  ELEMENT_TAG_LIST
)

URL = (
  "https://consolemods.org/wiki/Xbox_360:Original_Xbox_Games_Compatibility_List"
)

FILE_NAME = (
  "consolemods.org_xbox_360_original_xbox_games_compatibility_list"
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

REQUIRED_HEADER_LIST = [
  "name",
  "tested by",
  "known issues"
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