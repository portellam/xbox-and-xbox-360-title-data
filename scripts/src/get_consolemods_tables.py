#!/usr/bin/env python

#
# Filename:       get_consolemods_tables
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
  url,
  base_name
) -> int:
  table_list = retrieve_and_process_tables(url)

  if not table_list:
    return 1

  index = 1

  for table in table_list:
    print(f"Extracting table {index}.")
    name = f"{base_name}_table_{index}"
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