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
# This software uses the Wikipedia API under the Wikimedia Foundation's
# Terms of Use (https://foundation.wikimedia.org/wiki/Terms_of_Use)
# and API guidelines (https://www.mediawiki.org/wiki/API:Etiquette).
#
# Wikipedia, Wikimedia Foundation, and related trademarks are property of the
# Wikimedia Foundation. This software is not affiliated with, endorsed by, or
# sponsored by the Wikimedia Foundation.
#
# CONTENT LICENSING:
#
# All Wikipedia content retrieved by this script is licensed under the
# Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA 3.0):
# https://creativecommons.org/licenses/by-sa/3.0/
#
# When redistributing Wikipedia data, you must:
# • Attribute Wikipedia as the source.
# • Include a link to the original article.
# • License your derivative work under CC BY-SA 3.0 or compatible terms.
# • Provide a way for users to access the original Wikipedia article.
#
# API USAGE GUIDELINES:
#
# • Maximum 200 requests per second per IP (this script uses conservative limits).
# • Maximum 6,000 requests per day per user (if authenticated).
# • Use User-Agent header identifying your application.
# • Handle rate limiting gracefully with exponential backoff.
# • Do not use Wikipedia data for commercial spam or harassment.
#
# ROBOTS.TXT COMPLIANCE:
#
# This script respects Wikipedia's robots.txt: https://en.wikipedia.org/robots.txt
# Certain paths and high-frequency access patterns are disallowed.
#
# ATTRIBUTION TEMPLATE:
#
# When including Wikipedia data in publications, use:
# "Data from '[Article Title]' by Wikipedia, licensed under CC BY-SA 3.0
# (https://en.wikipedia.org/wiki/[Article_Title])"
#

#
# Filename:       extract_wikipedia.py
# Description:    Extract HTML Wiki table as lists.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

from typing import (
  List,
  Optional
)

from config import (
  ELEMENT_TAG_LIST
)

try:
  from bs4 import (
    BeautifulSoup
  )

except ImportError as e:
  import sys

  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

def find_tables(
  soup: BeautifulSoup
) -> List[BeautifulSoup]:
  try:
    table_list = soup.find_all(
      "table",
      {"class": "wikitable"}
    )

    if not table_list:
      print("No tables found.")
      return []

    print(f"Found {len(table_list)} tables.")
    return table_list

  except Exception as e:
    print("Could not find tables.")
    print(f"Error: {e}")
    return []

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  try:
    if not table:
      return []

    header_list = []

    for tr in table.find_all("tr"):
      cell_list = []

      try:
        cell_list = tr.find_all(ELEMENT_TAG_LIST)

      except:
        continue

      if not cell_list:
        continue

      header_list = [
        cell.get_text(
          separator = " ",
          strip = True
        )
        for cell in cell_list
      ]

      return header_list

    return []

  except Exception as e:
    print("Could not extract headers.")
    print(f"Error: {e}")
    return []

def extract_rows(
  table: BeautifulSoup,
  header_list: List[str]
) -> List[dict]:
  try:
    row_list = table.find_all("tr")[1:]

    if not row_list:
      return []

    print(f"Extracting {len(row_list)} rows.")
    extracted_row_list = []

    for index, tr in enumerate(
      row_list,
      start = 1
    ):
      cell_list = tr.find_all(ELEMENT_TAG_LIST)

      row = process_row(
        cell_list,
        header_list
      )

      if not row:
        print(f"Could not process row: {index}")
        continue

      extracted_row_list.append(row)

    print(f"Extracted {len(extracted_row_list)} rows.")
    return extracted_row_list

  except Exception as e:
    print("Could not extract rows.")
    print(f"Error: {e}")
    return []

def process_row(
  cell_list: List[BeautifulSoup],
  header_list: List[str]
) -> Optional[dict]:
  try:
    row = {}

    for header, cell in zip(
      header_list,
      cell_list
    ):
      text = cell.get_text(
        separator = " ",
        strip = True
      )

      row[header] = text

    return row

  except Exception as e:
    print(f"Error: {e}")
    return None