#!/usr/bin/env python

#
# Filename:       get_consolemods_tables.py
# Description:    Retrieves table from ConsoleMods.org article, and outputs as
#                 JSON.
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

from extract_consolemods import (
  extract_headers,
  extract_rows
 )

from sanitize_html import (
  retrieve_and_process_tables
)

from write import (
  write_this
)

def write_many(
  url: str,
  base_name: str
) -> int:
  table_list = retrieve_and_process_tables(url)

  if not table_list:
    return 1

  index = 1

  for table_html in table_list:
    print(f"Sanitized HTML for table {index}: {table_html[:100]}...")

    table = BeautifulSoup(
      table_html,
      'lxml'
    )

    header_list = extract_headers(table)

    if not header_list:
      print(f"Note: No headers found for table {index}.")
      index += 1
      continue

    row_list = extract_rows(
      table,
      header_list
    )

    if not row_list:
      print(f"Note: Output for table {index} is empty.")
      index += 1
      continue

    output_file = f"{base_name}_table_{index}"

    if write_this(
      url,
      output_file,
      header_list,
      row_list
    ) != 0:
      return 1

    index += 1

  return 0

def main() -> int:
  write_many(
    URL,
    OUTPUT_FILE_NAME
  )

if __name__ == "__main__":
  try:
    sys.exit(
      main()
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")