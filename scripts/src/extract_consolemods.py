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
  if cell.has_attr("title"):
    return cell["title"].strip()

  inner_with_title = cell.find(attrs = {"title": True})

  if inner_with_title:
    return inner_with_title["title"].strip()

  abbr = cell.find("abbr")

  if abbr and abbr.has_attr("title"):
    return abbr["title"].strip()

  img = cell.find("img")

  if img and img.has_attr("alt"):
    return img["alt"].strip()

  if cell.has_attr("class"):
    for cls in cell["class"]:
      cls_lower = cls.lower()

      if cls_lower in [
        "in-game",
        "intro",
        "issues",
        "menus",
        # "orange",
        "playable",
        "supported",
        "unplayable",
        "untested",
      ]:
        return cls_lower

  return cell.get_text(strip = True)

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  inverted_header_map = {}

  for key, value in HEADER_MAP.items():
    inverted_header_map[value] = key

  try:
    print("Extracting headers.")

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
      print(f"DEBUG: raw header text: '{text}'")

      text = inverted_header_map.get(
        text,
        text
      )

      header_list.append(text)

    print("DEBUG: Extracted headers:", header_list)
    return header_list

  except Exception as e:
    print(f"Error extracting headers: {e}")
    return []

def extract_rows(
  table: BeautifulSoup,
  header_list: List[str]
) -> List[Dict[str, str]]:
  try:
    print("Extracting rows.")
    rows_list = []

    tr_list = table.find_all("tr")

    for tr in tr_list[1:]:
      cell_list = tr.find_all("td")

      if not cell_list:
        continue

      row_data = {}

      for header, cell in zip(
        header_list,
        cell_list
      ):
        row_data[header] = extract_cell_value(cell)

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
    header_list = [
      th.text.strip()
      for th in table.find_all("th")
    ]

    if has_required_headers(header_list):
      return table

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

  header_list = [th.get_text(strip=True).lower() for th in table.find_all("th")]
  print("DEBUG: header_list from table:", header_list)
  print("DEBUG: required headers:", HEADER_KEY_LIST)

  if has_required_headers(header_list):
      return table

  return None

def find_table(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  id = "Compatibility_List"

  section_span = soup.find(
    "span",
    id = id
  )

  if not section_span:
    print("DEBUG: No span with id=Compatibility_List found.")
    return None

  heading = section_span.find_parent(
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
    print("DEBUG: No heading parent found for Compatibility_List span.")
    return None

  table = heading.find_next(
    "table",
    class_ = lambda c: c and "wikitable" in c
  )

  if not table:
    print("DEBUG: No wikitable found after heading.")
    return None

  print("DEBUG: Found table classes:", table.get("class"))

  thead = table.find("thead")

  header_list = extract_headers(table)

  print("DEBUG: header_list from table:", header_list)

  if has_required_headers(header_list):
    return table

  else:
    print("DEBUG: Table found but headers did not match required list.")
    return None

def has_required_headers(
  header_list: List[str]
) -> bool:
  header_set_lower = {
    h.lower()
    for h in header_list
  }

  required_set_lower = {
    h.lower()
    for h in HEADER_KEY_LIST
  }

  return required_set_lower.issubset(header_set_lower)

def normalize_header(h: str) -> str:
  return re.sub(
    r'[^a-z0-9_]',
    '',
    h.lower()
  )

def process_row(
  cell_list,
  header_list
):
  row = []
  status_headers = set(HEADER_MAP.values())

  for i, header in enumerate(header_list):
    cell = cell_list[i]
    header_lower = header.lower()

    canonical_header = HEADER_MAP.get(header_lower, header_lower)

    if canonical_header in status_headers:
      div = cell.find(
        'div',
        class_ = 'visible'
      )
      title = div.get(
        'title',
        ''
      ).strip().lower() if div else ''
      status_token = STATUS_MAP.get(
        title,
        'untested'
      )
      row.append(status_token)

    elif header_lower == "tested by":
      row.append(cell.get_text(strip = True))

    elif header_lower == "known issues":
      row.append(cell.get_text(strip = True))

    else:
      row.append(cell.get_text(strip = True))

  return row