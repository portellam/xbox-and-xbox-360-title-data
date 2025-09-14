#!/usr/bin/env python

#
# Filename:       extract_consolemods.py
# Description:    Extract HTML Wiki table as lists.
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

from config_consolemods import (
  HEADER_KEY_LIST,
  ELEMENT_TAG_LIST,
  STATUS_MAP,
  HEADER_MAP
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
  cell: BeautifulSoup
) -> str:
  text = cell.get_text(strip = True)
  if text:
    return STATUS_MAP.get(
      text.lower(),
      text
    )

  if cell.has_attr("title"):
    return STATUS_MAP.get(
      cell["title"].lower().strip(),
      cell["title"].strip()
    )

  return ""

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  inverted_header_map = {}

  for key, value in HEADER_MAP.items():
    inverted_header_map[value] = key

  try:
    thead = table.find("thead")

    if thead:
      header_cells = thead.find_all("th")

    else:
      header_cells = table.find_all(
        "th",
        limit = len(HEADER_KEY_LIST)
      )

    header_list = []

    for cell in header_cells:
      if cell.has_attr("title"):
        text = cell["title"].strip()

      elif cell.find("abbr") and cell.find("abbr").has_attr("title"):
        text = cell.find("abbr")["title"].strip()

      else:
        text = cell.get_text(strip = True)

      text = text.strip()

      normalized_text = normalize_header(text)

      text = inverted_header_map.get(
        normalized_text,
        text
      )

      header_list.append(text)

    if "Name" not in header_list:
      return []

    return header_list

  except Exception as e:
    print("Could not extract headers")
    print(f"Error: {e}")
    return []

def extract_rows(
  table: BeautifulSoup,
  header_list: List[str]
) -> List[
  Dict[
    str,
    str
  ]
]:
  try:
    rows_list = []
    tr_list = table.find_all("tr")
    print(f"Extracting {len(tr_list)} rows.")

    if not tr_list:
      return []

    for tr in tr_list[1:]:
      cell_list = tr.find_all("td")

      if not cell_list:
        continue

      if len(cell_list) < len(header_list):
        continue

      row_data = {}

      for header, cell in zip(
        header_list,
        cell_list
      ):
        value = extract_cell_value(cell)

        if header in HEADER_MAP or header in HEADER_MAP.values():
          value = STATUS_MAP.get(
            value.lower(),
            value
          )

        if value == header or not value:
          continue

        row_data[header] = value

      if not row_data or "Name" not in row_data or row_data["Name"].startswith("{{"):
        continue

      rows_list.append(row_data)

    return rows_list

  except Exception as e:
    print("Could not extract rows.")
    print(f"Error: {e}")
    return []

def find_by_header(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  for table in soup.find_all("table"):
    header_list = extract_headers(table)

    if has_required_headers(header_list):
      return table

  return None

def find_by_section_id(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  section = soup.find(
    "span",
    id = "Compatibility_List"
  )

  if not section:
    return None

  heading = section.find_parent(
    [
      "h1",
      "h2",
      "h3",
      "h4",
      "h5",
      "h6"
    ]
  )

  if not heading:
    return None

  table = heading.find_next("table")

  if not table:
    return None

  header_list = extract_headers(table)

  if has_required_headers(header_list):
    return table
  return None

def find_table(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  table = find_by_section_id(soup)

  if table:
    return table

  table = find_by_header(soup)

  if table:
    return table

  table = soup.find(
    "table",
    class_ = lambda c: c and "wikitable" in c
  )

  if table:
    header_list = extract_headers(table)

    if has_required_headers(header_list):
      return table

  tables = soup.find_all("table")

  for i, table in enumerate(tables):
    headers = extract_headers(table)

    if has_required_headers(headers):
      return table

  print("DEBUG: No suitable table found")
  return None

def has_required_headers(
  header_list: List[str]
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

def normalize_header(h: str) -> str:
  return re.sub(
    r'[^a-z0-9_]',
    '',
    h.lower()
  )