#!/usr/bin/env python

from typing import Optional, List
from config_consolemods import HEADER_KEY_LIST, ELEMENT_TAG_LIST, STATUS_MAP

try:
  from bs4 import BeautifulSoup

except ImportError as e:
  import sys
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

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

  element = section.parent

  while element:
    element = element.find_next_sibling()

    if element and element.name == "table":
      header_list = [
        th.get_text(
          strip = True
        ).lower()
        for th in element.find_all("th")
      ]

      if has_required_headers(header_list):
        return element

  return None

def find_table(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  try:
    table = find_by_section_id(soup)

    if table:
      print("Found table by section ID 'Compatibility_List'.")
      print(f"Debug: Table headers: {[th.get_text(strip=True) for th in table.find_all('th')]}")
      return table

    table = find_by_header(soup)

    if table:
      print("Found table by header match.")
      print(f"Debug: Table headers: {[th.get_text(strip=True) for th in table.find_all('th')]}")
      return table

    print("Could not find table by section.")
    print("Could not find table by header.")
    return None

  except Exception as e:
    print(f"Error: {e}")
    return None

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  try:
    print("Extracting headers.")

    for tr in table.find_all("tr"):
      cell_list = tr.find_all(ELEMENT_TAG_LIST)

      if cell_list:
        header_list = [
          cell.get_text(
            separator = " ",
            strip = True
          )
          for cell in cell_list
        ]

        print(f"Debug: Extracted headers: {header_list}")
        return header_list
    return []

  except Exception as e:
    print(f"Error: {e}")
    return []

def process_row(
  cell_list,
  header_list
):
  row = []

  for i, header in enumerate(header_list):
    cell = cell_list[i]

    if 1 <= i <= 12:
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
    elif i == 13:

      row.append(cell.get_text(strip = True))

    elif i == 14:
      row.append(cell.get_text(strip = True))

    else:
      row.append(cell.get_text(strip = True))
  return row

def extract_rows(
  table: BeautifulSoup,
  header_list: List[str]
) -> List[List[str]]:
  try:
    row_list = table.find_all("tr")[1:]
    print(f"Extracting {len(row_list)} rows...")
    extracted_row_list = []

    for index, tr in enumerate(
      row_list,
      start = 1
    ):
      cell_list = tr.find_all(ELEMENT_TAG_LIST)

      if len(cell_list) != 15:
        print(f"Warning: Row {index} has {len(cell_list)} columns, expected 15")
        continue

      row = process_row(
        cell_list,
        header_list
      )

      if not row:
        print(f"Could not process row: {index}")
        continue

      extracted_row_list.append(row)

    print(f"Extracted {len(extracted_row_list)} rows.")
    return extracted_row_list

  except Exception as e:
    print("Could not extract rows.")
    print(f"Error: {e}")
    return []