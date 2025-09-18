#!/usr/bin/env python

#
# Filename:       config_google_sheet.py
# Description:    Various public Google Sheet documents to parse.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

from config import (
  OUTPUT_PATH
)

URL_LIST = [
  "https://docs.google.com/spreadsheets/d/1Vp7YHrX_YEii87_gD7s3pIemmjUjIPd_y0dBcrDXihw/edit?gid=0#gid=0"
]

NAME_LIST = [
  "List of Xbox Live Indie Games"
]

FILE_NAME_LIST = [
  "list_of_xbox_live_indie_games"
]

for key, value in enumerate(
  URL_LIST,
  start = 1
):
  FILE_NAME_LIST[key] = OUTPUT_PATH + FILE_NAME_LIST[key]