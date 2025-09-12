#!/usr/bin/env python

#
# Filename:       get_wikipedia_tables.py
# Description:    Retrieves tables from specified Wikipedia articles, and outputs as
#                 CSV and JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import sys

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

from bs4 import (
  BeautifulSoup
)

from config_wikipedia import (
  OUTPUT_FILE_NAME_LIST,
  URL_LIST
)

from extract_wikipedia import (
  extract_headers,
  extract_rows,
  find_tables
)

from fetch import (
  fetch_page
)

from write import (
  write_this
)

def write_many(
  url,
  name
) -> int:
  page_content = fetch_page(url)

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
    name = f"{name}_{index}"
    header_list = extract_headers(table)
    index += 1

    row_list = extract_rows(
      table,
      header_list
    )

    write_this(
      url,
      name,
      header_list,
      row_list
    )

  return 0

def main() -> int:
  for url, output_name in zip(
    URL_LIST,
    OUTPUT_FILE_NAME_LIST
  ):
    write_many(
      url,
      output_name
    )

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