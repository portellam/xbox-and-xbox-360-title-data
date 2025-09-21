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
# Filename:       get_wikipedia_tables.py
# Description:    Retrieves tables from specified Wikipedia articles, and outputs
#                 as JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

WIKIPEDIA_HTTP_QUOTA_LIMIT_IN_SECONDS = 0.500  # Set as two (2) quotas/second. Actual is two-hundred (200) quotas/second.

import sys

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

from bs4 import (
  BeautifulSoup
)

from config_wikipedia import (
  FILE_NAME_LIST,
  URL_LIST
)

from extract_wikipedia import (
  extract_headers,
  extract_rows,
  find_tables
)

from fetch import (
  get_html
)

from write import (
  write_this
)

def write_many(
  url,
  base_name
) -> int:
  page_content = get_html(
    url,
    WIKIPEDIA_HTTP_QUOTA_LIMIT_IN_SECONDS
  )

  if not page_content:
    return 1

  soup = BeautifulSoup(
    page_content,
    "html.parser"
  )

  table_list = find_tables(soup)

  if not table_list:
    return 1

  index = 1

  for table in table_list:
    print(f"Extracting table {index}.")
    name = f"{base_name}_table_{index}"
    index += 1
    header_list = extract_headers(table)

    row_list = extract_rows(
      table,
      header_list
    )

    write_this(
      name,
      header_list,
      row_list
    )

    if index < len(table_list):
      print()

  return 0

def main() -> int:
  index = 0

  for url, name in zip(
    URL_LIST,
    FILE_NAME_LIST
  ):
    index += 1

    write_many(
      url,
      name
    )

    if index < len(URL_LIST):
      print()

  return 0

if __name__ == "__main__":
  try:
    sys.exit(
      main()
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")