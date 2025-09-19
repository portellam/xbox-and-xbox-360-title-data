#!/usr/bin/env python

#
# Filename:       get_wiki_table.py
# Description:    Retrieves table from Wiki powered webpage, and outputs to file.
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

from typing import (
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
      header_key_list
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
      header_map,
      header_key_list,
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
  try:
    page_content = get_html(url)

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