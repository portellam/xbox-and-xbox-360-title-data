#!/usr/bin/env python

#
# Filename:       get-consolemods-database.py
# Description:    Retrieves table from ConsoleMods.org article, and outputs as
#                 CSV and JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import sys
import csv
import json
from typing import Optional, List

try:
  import requests
  from bs4 import BeautifulSoup

except ImportError as e:
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )
  sys.exit(1)

URL = (
  "https://consolemods.org/wiki/Xbox_360:Original_Xbox_Games_Compatibility_List"
)

OUTPUT_FILE_NAME = (
  "consolemods.org_xbox_360_original_xbox_games_compatibility_list"
)

HEADER_KEY_LIST = [
  "Name",
  "Tested By",
  "Known Issues"
]

ELEMENT_TAG_LIST = [
  "th",
  "td"
]

STATUS_MAP = {
  "supported":   "supported",
  "playable":    "playable",
  "ingame":      "in-game",
  "orange":      "menus",
  "menus":       "menus",
  "intro":       "intro",
  "unplayable":  "unplayable",
  "untested":    "untested",
}

def fetch_page(
  url: str
) -> Optional[str]:
  try:
    print(f"Fetching page: '{url}'")

    response = requests.get(
      url,
      headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
      },
      timeout = 10
    )

    response.raise_for_status()
    print("Fetched page.")
    return response.text

  except requests.RequestException as e:
    print(f"Error: {e}")
    return None

def find_table(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  try:
    table = (
      find_by_section_id(soup)
      or find_by_header(soup)
    )

    if table is None:
      print("Could not find table by section.")
      print("Could not find table by header.")
      return None

    print("Found table by section.")
    return table

  except Exception as e:
    print(f"Error: {e}")
    return None

def has_required_headers(
  header_list: List[str]
) -> bool:
  return all(
    h in header_list
    for h in HEADER_KEY_LIST
  )

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

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  try:
    print("Extracting headers.")

    for tr in table.find_all("tr"):
      cell_list = tr.find_all(ELEMENT_TAG_LIST)

      if cell_list:
        return [
          cell.get_text(
            separator=" ",
            strip = True
          )
          for cell in cell_list
        ]

    return []

  except Exception as e:
    print(f"Error: {e}")
    return []

def process_row(
  cell_list: List[BeautifulSoup],
  header_list: List[str]
) -> Optional[List[str]]:
  try:
    if len(cell_list) < len(header_list):
      return None

    row = []

    for i, cell in enumerate(cell_list):
      text = cell.text.strip()

      if 0 < i < len(header_list) - 2:
        a = cell.find("a")

        if a and a.has_attr("href"):
          fragment = a["href"].lstrip("#").strip()
          text = STATUS_MAP.get(
            fragment,
            fragment
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

    for index, tr in enumerate(row_list, start=1):
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

def write_csv(
  header_list: List[str],
  extracted_row_list: List[List[str]],
  name: str
) -> bool:
  try:
    output_file = f"{name}.csv"
    print(f"Writing to file: '{output_file}'")

    with open(
      output_file,
      "w",
      newline = "",
      encoding = "utf-8"
    ) as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(header_list)
      writer.writerows(extracted_row_list)

    print("Wrote to file.")
    return True

  except IOError as e:
    print("Could not write to file.")
    print(f"Error: {e}")
    return False

def write_json(
  header_list: List[str],
  extracted_row_list: List[List[str]],
  name: str
) -> bool:
  try:
    output_file = f"{name}.json"
    print(f"Writing to file: '{output_file}'")

    data = [
      dict(
        zip(header_list, row)
      )
      for row in extracted_row_list
    ]

    with open(
      output_file,
      "w",
      encoding = "utf-8"
    ) as jsonfile:
      json.dump(
        data,
        jsonfile,
        indent = 2
      )

    print("Wrote to file.")
    return True

  except IOError as e:
    print("Could not write to file.")
    print(f"Error: {e}")
    return False

def main() -> int:
  page_content = fetch_page(URL)

  if not page_content:
    return 1

  print("Parsing page.")
  soup = BeautifulSoup(
    page_content,
    "html.parser"
  )

  table = find_table(soup)

  if not table:
    return 1

  header_list = extract_headers(table)

  if not header_list:
    return 1

  extracted_row_list = extract_rows(
    table,
    header_list
  )

  if not extracted_row_list:
    print("Warning: Could not extract data. No data rows exist.")
    return 1

  if not write_csv(
    header_list,
    extracted_row_list,
    OUTPUT_FILE_NAME
  ):
    return 1

  if not write_json(
    header_list,
    extracted_row_list,
    OUTPUT_FILE_NAME
  ):
    return 1

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