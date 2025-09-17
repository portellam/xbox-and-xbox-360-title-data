#!/usr/bin/env python

#
# Filename:       config_wikipedia.py
# Description:    List of Wikipedia articles to parse.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

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
  "https://en.wikipedia.org/wiki/Xbox_Live_Arcade#Xbox"
]

OUTPUT_PATH = "../../databases/json/"

OUTPUT_FILE_NAME_LIST = [
  f"{OUTPUT_PATH}wikipedia.org_category_xbox_360_live_indie_games",
  f"{OUTPUT_PATH}wikipedia.org_list_of_cancelled_xbox_games",
  f"{OUTPUT_PATH}wikipedia.org_list_of_xbox_360_applications",
  f"{OUTPUT_PATH}wikipedia.org_xbox_360_games_a-l",
  f"{OUTPUT_PATH}wikipedia.org_xbox_360_games_m-z",
  f"{OUTPUT_PATH}wikipedia.org_xbox_360_system_link_games",
  f"{OUTPUT_PATH}wikipedia.org_xbox_games",
  f"{OUTPUT_PATH}wikipedia.org_xbox_games_compatible_with_xbox_360"
  f"{OUTPUT_PATH}xbox.fandom.com_list_of_cancelled_xbox_games",
  f"{OUTPUT_PATH}xbox.fandom.com_list_of_xbox_games",
  f"{OUTPUT_PATH}wikipedia.org_xbox_live_arcade_xbox",
]

ELEMENT_TAG_LIST = [
  "th",
  "td"
]