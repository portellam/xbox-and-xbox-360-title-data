#!/usr/bin/env python

#
# Filename:       get_consolemods_tables
# Description:    Retrieves table from ConsoleMods.org article, and outputs as
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

from config_consolemods import (
  OUTPUT_FILE_NAME,
  URL
)

from fetch import (
  fetch_page
)

from extract_consolemods import (
  extract_headers,
  extract_rows,
  find_table
 )

from write import (
  write_csv,
  write_json
)

def main() -> int:
  page_content = fetch_page(URL)
  if not page_content:
    return 1

  print("Parsing page.")
  soup = BeautifulSoup(
    page_content,
    "lxml"
  )

  table = find_table(soup)
  if not table:
    return 1

  header_list = extract_headers(table)
  if not header_list:
    return 1

  extracted_row_list = extract_rows(
    table,
    header_list
  )
  if not extracted_row_list:
    print("Warning: Could not extract data. No data rows exist.")
    return 1

  if not write_csv(
    header_list,
    extracted_row_list,
    OUTPUT_FILE_NAME
  ):
    return 1

  if not write_json(
    header_list,
    extracted_row_list,
    OUTPUT_FILE_NAME
  ):
    return 1

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