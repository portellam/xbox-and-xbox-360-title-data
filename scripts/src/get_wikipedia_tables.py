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

from fetch import (
  fetch_page
)

from extract_wikipedia import (
  extract_headers,
  extract_rows,
  find_tables
)

from config_wikipedia import (
  OUTPUT_FILE_NAME_LIST,
  URL_LIST
)

from write import (
  write_csv,
  write_json
)

def main() -> int:
  for url, output_name in zip(
    URL_LIST,
    OUTPUT_FILE_NAME_LIST
  ):
    page_content = fetch_page(url)

    if not page_content:
      continue

    print("Parsing page.")

    soup = BeautifulSoup(
      page_content,
      "html.parser"
    )

    table_list = find_tables(soup)
    if not table_list:
      continue

    index = 1

    for actual_index, table in enumerate(
      table_list,
      start = 1
    ):
      header_list = extract_headers(table)

      if not header_list:
        continue

      extracted_row_list = extract_rows(
        table,
        header_list
      )
      if not extracted_row_list:
        print("Warning: Could not extract data. No data rows exist.")
        continue

      file_suffix = f"{output_name}_table_{index}"
      index += 1

      if not write_csv(
        header_list,
        extracted_row_list,
        file_suffix
      ):
        continue

      if not write_json(
        header_list,
        extracted_row_list,
        file_suffix
      ):
        continue

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