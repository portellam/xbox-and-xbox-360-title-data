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

#
# Filename:       config_wikipedia.py
# Description:    List of Wikipedia articles to parse.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

from config import (
  ELEMENT_TAG_LIST
)

URL_LIST = [
  "https://en.wikipedia.org/wiki/Category:Xbox_360_Live_Indie_games",
  "https://en.wikipedia.org/wiki/List_of_cancelled_Xbox_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_applications",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(A%E2%80%93L)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(M%E2%80%93Z)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_System_Link_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games_compatible_with_Xbox_360",
  "https://xbox.fandom.com/wiki/List_of_Cancelled_Xbox_games",
  "https://xbox.fandom.com/wiki/List_of_Xbox_games",
  "https://en.wikipedia.org/wiki/Xbox_Live_Arcade",
  "https://en.wikipedia.org/wiki/Xbox_Live_Arcade#Xbox",
]

FILE_NAME_LIST = [
  "wikipedia.org_category_xbox_360_live_indie_games",
  "wikipedia.org_list_of_cancelled_xbox_games",
  "wikipedia.org_list_of_xbox_360_applications",
  "wikipedia.org_xbox_360_games_a-l",
  "wikipedia.org_xbox_360_games_m-z",
  "wikipedia.org_xbox_360_system_link_games",
  "wikipedia.org_xbox_games",
  "wikipedia.org_xbox_games_compatible_with_xbox_360",
  "xbox.fandom.com_list_of_cancelled_xbox_games",
  "xbox.fandom.com_list_of_xbox_games",
  "wikipedia.org_xbox_live_arcade",
  "wikipedia.org_xbox_live_arcade_xbox",
]