#!/usr/bin/env python

#
# Filename:       extract_wiki_table.py
# Description:    Extract an HTML webpage Wiki table as a list.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import re

from typing import (
  Dict,
  List,
  Optional
)

from config import (
  ELEMENT_TAG_LIST
)

try:
  from bs4 import BeautifulSoup

except ImportError as e:
  import sys
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

def extract_cell_value(
  cell: BeautifulSoup,
  is_status_column: bool,
  status_map: Dict[
    str,
    str
  ]
) -> str:
  div = cell.find('div')

  if div and div.has_attr('title') and is_status_column:
    return status_map.get(
      div['title'].lower().strip(),
      div['title'].strip()
    )

  text = cell.get_text(strip = True)

  if not text:
    return ""

  return status_map.get(
    text.lower(),
    text
  ) if is_status_column else text

def extract_table_data(
  table: BeautifulSoup,
  header_key_list: List[str],
  header_map: Dict[
    str,
    str
  ],
  status_map: Dict[
    str,
    str
  ]
) -> tuple[
  List[str],
  List[
    Dict[
      str,
      str
    ]
  ]
]:
  try:
    header_list = []
    thead = table.find("thead")

    if thead:
      header_cells = thead.find_all("th")

    else:
      header_cells = table.find_all(
        "th",
        limit = len(header_key_list)
      )

    inverted_header_map = {
      v: k for
        k,
        v
      in header_map.items()
    }

    for cell in header_cells:
      if cell.has_attr("title"):
        text = cell["title"].strip()

      elif cell.find("abbr") and cell.find("abbr").has_attr("title"):
        text = cell.find("abbr")["title"].strip()

      else:
        text = cell.get_text(strip = True)

      text = text.strip()

      normalized_text = re.sub(
        r'[^a-z0-9_]',
        '',
        text.lower()
      )

      text = inverted_header_map.get(
        normalized_text,
        text
      )

      header_list.append(text)

    if "Name" not in header_list:
      return [], []

    row_list = []
    tr_list = table.find_all("tr")

    if not tr_list:
      return header_list, []

    for tr in tr_list[1:]:
      cell_list = tr.find_all("td")

      if not cell_list or len(cell_list) < len(header_list):
        continue

      row_data = {}

      for header, cell in zip(
        header_list,
        cell_list
      ):
        is_status_column = header in header_map or header in header_map.values()

        value = extract_cell_value(
          cell,
          is_status_column,
          status_map
        )

        if value == header or not value:
          continue

        row_data[header] = value

      if not row_data or "Name" not in row_data:
        continue

      row_list.append(row_data)

    return header_list, row_list

  except Exception as e:
    print("Could not extract table.")
    print(f"Error: {e}")

    return [],
    []

def has_required_headers(
  header_list: List[str],
  required_header_list: List[str]
) -> bool:
  header_set_lower = {
    h.lower()
    for h in header_list
  }

  required_headers = {
    "name",
    "tested by",
    "known issues"
  }

  return all(h in header_set_lower for h in required_headers)