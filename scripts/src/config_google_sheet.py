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
# This software uses the Google Sheets API under the Google APIs Terms of Service
# (https://developers.google.com/terms). You must comply with these terms when
# using this script, including rate limits and data usage restrictions.
#
# Google and Google Sheets are trademarks of Google LLC. This software is not
# affiliated with, endorsed by, or sponsored by Google LLC.
#
# DATA USAGE NOTICE:
#
# This script only accesses publicly available Google Sheets. Users are
# responsible for ensuring they have permission to access and process the data
# retrieved. Respect the privacy and terms of service of the original sheet
# creators.
#
# USAGE WARNING:
#
#   - Only use with sheets marked "Anyone with the link can view".
#   - Respect sheet owners' terms of use.
#   - Do not scrape private or restricted content.
#   - Comply with robots.txt and rate limits.
#

#
# Filename:       config_google_sheet.py
# Description:    Various public Google Sheet documents to parse.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

URL_LIST = [
  "https://docs.google.com/spreadsheets/d/1Vp7YHrX_YEii87_gD7s3pIemmjUjIPd_y0dBcrDXihw/edit?gid=0#gid=0"
]

NAME_LIST = [
  "List of Xbox Live Indie Games"
]

FILE_NAME_LIST = [
  "list_of_xbox_live_indie_games"
]