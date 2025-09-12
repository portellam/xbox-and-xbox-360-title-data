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
  text = cell.get_text(strip=True)
  if text:
    return STATUS_MAP.get(text.lower(), text)

  if cell.has_attr("title"):
    return STATUS_MAP.get(cell["title"].lower().strip(), cell["title"].strip())

  return ""

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

      normalized_text = normalize_header(text)
      text = inverted_header_map.get(
        normalized_text,
        text
      )

      if text not in HEADER_KEY_LIST:
        print(f"DEBUG: Header '{text}' not in HEADER_KEY_LIST, using raw text")

      header_list.append(text)

    print("DEBUG: Extracted headers:", header_list)
    if "Name" not in header_list:
      print("DEBUG: 'Name' header missing, returning empty list")
      return []
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

    if not tr_list:
      print("DEBUG: No rows found in table")
      return []

    for tr in tr_list[1:]:
      cell_list = tr.find_all("td")

      if not cell_list:
        print("DEBUG: Skipping empty row")
        continue

      if len(cell_list) < len(header_list):
        print(f"DEBUG: Skipping row with insufficient cells: {len(cell_list)} cells, expected {len(header_list)}")
        continue

      row_data = {}

      for header, cell in zip(
        header_list,
        cell_list
      ):
        value = extract_cell_value(cell)

        if header in HEADER_MAP or header in HEADER_MAP.values():
          value = STATUS_MAP.get(value.lower(), value)

        if value == header or not value:
          print(f"DEBUG: Skipping placeholder or empty value for header '{header}'")
          continue

        row_data[header] = value

      if not row_data or "Name" not in row_data or row_data["Name"].startswith("{{"):
        print("DEBUG: Skipping row with invalid or placeholder Name")
        continue

      rows_list.append(row_data)

    if not rows_list:
      print("DEBUG: No valid rows extracted")

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
      print("DEBUG: Table found by header matching with required headers")
      return table
  print("DEBUG: No table found by header matching")
  return None

def find_by_section_id(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  section = soup.find(
    "span",
    id = "Compatibility_List"
  )

  if not section:
    print("DEBUG: No span with id=Compatibility_List found")
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
    print("DEBUG: No heading parent found for Compatibility_List span")
    return None

  table = heading.find_next("table")

  if not table:
    print("DEBUG: No table found after heading")
    return None

  header_list = extract_headers(table)
  if has_required_headers(header_list):
    print("DEBUG: Table found by section ID with required headers")
    return table
  print("DEBUG: Table found but missing required headers")
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

  table = soup.find("table", class_=lambda c: c and "wikitable" in c)
  if table:
    header_list = extract_headers(table)
    if has_required_headers(header_list):
      print("DEBUG: Table found by wikitable class with required headers")
      return table
    print("DEBUG: Wikitable found but missing required headers")

  tables = soup.find_all("table")
  print(f"DEBUG: Found {len(tables)} tables")
  for i, table in enumerate(tables):
    headers = extract_headers(table)
    print(f"DEBUG: Table {i+1} headers: {headers}")
    if has_required_headers(headers):
      print(f"DEBUG: Table {i+1} selected as fallback")
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
  required_headers = {"name", "tested by", "known issues"}
  return all(h in header_set_lower for h in required_headers)

def normalize_header(h: str) -> str:
  return re.sub(
    r'[^a-z0-9_]',
    '',
    h.lower()
  )