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
# This software accesses content from wiki-powered websites. Different wikis have
# different terms of service and robots.txt policies. You must:
#
# 1. Review and comply with the specific wiki's Terms of Service
# 2. Respect the site's robots.txt file
# 3. Follow rate limiting guidelines (typically 1-2 requests/second)
# 4. Only access publicly available content
#
# COMMON WIKI PLATFORMS:
#
# • MediaWiki (Wikipedia, Fandom): https://www.mediawiki.org/wiki/Robots.txt
# • DokuWiki: Check individual site policies.
# • Other wiki software: Always verify robots.txt and ToS.
#
# ATTRIBUTION REQUIREMENTS:
#
# When redistributing data obtained through this script:
# • Include attribution to the original wiki source.
# • Preserve any existing copyright notices from the source.
# • Do not claim the data as your own creation.
#
# SITE-SPECIFIC COMPLIANCE:
#
# Before using this script with a specific wiki, verify:
# • robots.txt: https://[wiki-domain]/robots.txt
# • Terms of Service: Usually at https://[wiki-domain]/terms or /tos
# • Rate limits: Typically documented in API documentation.
#

#
# Filename:       get_wiki_table.py
# Description:    Retrieves table from Wiki powered webpage, and outputs to file.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

WIKI_HTTP_QUOTA_LIMIT_IN_SECONDS = 1.000  # Set as one (1) quota/second. Actual is 200 quotas/second.

import sys

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

from bs4 import (
  BeautifulSoup
)

from typing import (
  Dict,
  List
)

from extract_wiki_table import (
  extract_table_data,
  has_required_headers
)

from fetch import (
  get_html
)

from sanitize_html import (
  sanitize_html_table
)

from write import (
  write_json
)

def write_many(
  url: str,
  base_name: str,
  table_list: List[BeautifulSoup],
  header_key_list: List[str],
  required_header_list: List[str],
  header_map: Dict[
    str,
    str
  ],
  status_map: Dict[
    str,
    str
  ]
) -> int:
  if not table_list:
    print(f"Could not process tables.")
    return 1

  print(f"Processing tables.")
  print()

  index = 1
  success_count = 0

  for table in table_list:
    header_list, _ = extract_table_data(
      table,
      header_key_list,
      header_map,
      status_map
    )

    if not has_required_headers(
      header_list,
      required_header_list
    ):
      print(f"Skipping table {index}: missing required headers.")
      index += 1
      print()
      continue

    print(f"Processing table {index}.")
    td_list = table.find_all('td')

    for td in td_list:
      div = td.find('div')
      has_title = div and div.has_attr('title')

      if not (has_title and not td.get_text(strip = True)):
        continue

      td.clear()
      td.string = div['title'].strip()

    header_list, row_list = extract_table_data(
      table,
      header_key_list,
      header_map,
      status_map
    )

    file_name = f"{base_name}_table_{index}"
    index += 1

    if not row_list:
      print(f"Could not process table.")
      print(f"Warning: Table is empty.")
      print()
      continue

    print("Processed table.")

    if not write_json(
      header_list,
      row_list,
      file_name
    ):
      print()
      continue

    print()
    success_count += 1

  print(f"Processed {success_count} tables.")
  return 0 if success_count != 0 else 1

def main(
  url: str,
  base_name: str,
  header_key_list: List[str],
  required_header_list: List[str],
  header_map: Dict[
    str,
    str
  ],
  status_map: Dict[
    str,
    str
  ],
  quota_limit_in_seconds: float = WIKI_HTTP_QUOTA_LIMIT_IN_SECONDS
) -> int:
  try:
    page_content = get_html(
      url,
      quota_limit_in_seconds
    )

    if not page_content:
      return 1

    soup = BeautifulSoup(
      page_content,
      "html.parser"
    )

    table_list = soup.find_all("table")

    if not table_list:
      print("No tables found.")
      return 1

    print(f"Found {len(table_list)} tables.")
    print()

    return write_many(
      url,
      base_name,
      table_list,
      header_key_list,
      required_header_list,
      header_map,
      status_map
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")