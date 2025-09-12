#!/usr/bin/env python

#
# Filename:       extract_wiki.py
# Description:    Extract HTML Wiki table as lists.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

from typing import Optional, List
from wiki_config import ELEMENT_TAG_LIST

try:
  from bs4 import BeautifulSoup

except ImportError as e:
  import sys

  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

def find_tables(
  soup: BeautifulSoup
) -> List[BeautifulSoup]:
  try:
    table_list = soup.find_all(
      "table",
      {"class": "wikitable"}
    )

    if not table_list:
      print("No tables found.")
      return []

    print(f"Found {len(table_list)} tables.")
    return table_list

  except Exception as e:
    print("Could not find tables.")
    print(f"Error: {e}")
    return []

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  try:
    print("Extracting headers.")

    for tr in table.find_all("tr"):
      cell_list = tr.find_all(ELEMENT_TAG_LIST)

      if not cell_list:
        continue

      return [
        cell.get_text(
          separator = " ",
          strip = True
        )
        for cell in cell_list
      ]

    return []

  except Exception as e:
    print("Could not extract headers.")
    print(f"Error: {e}")
    return []

def process_row(
  cell_list: List[BeautifulSoup],
  header_list: List[str]
) -> Optional[List[str]]:
  try:
    if len(cell_list) < 1:
      return None

    row = []

    for cell in cell_list:
      text = cell.get_text(
        separator = " ",
        strip = True
      )

      row.append(text)

    return row

  except Exception as e:
    print(f"Error: {e}")
    return None

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