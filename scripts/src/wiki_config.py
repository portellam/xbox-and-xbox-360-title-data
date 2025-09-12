#!/usr/bin/env python

#
# Filename:       wiki_config.py
# Description:    List of Wikipedia articles to parse.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

URL_LIST = [
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(A%E2%80%93L)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(M%E2%80%93Z)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_System_Link_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games_compatible_with_Xbox_360"
]

OUTPUT_FILE_NAME_LIST = [
  "wikipedia.org_xbox_360_games_a-l",
  "wikipedia.org_xbox_360_games_m-z",
  "wikipedia.org_xbox_360_system_link_games",
  "wikipedia.org_xbox_games",
  "wikipedia.org_xbox_games_compatible_with_xbox_360"
]

ELEMENT_TAG_LIST = [
  "th",
  "td"
]