#!/usr/bin/env python

#
# Filename:       get-consolemods-database.py
# Description:    Retrieves table from ConsoleMods.org article, and outputs as
#                 CSV/JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import sys
import csv
import json
from typing import Optional, List, Dict

try:
  import requests
  from bs4 import BeautifulSoup
except ImportError as e:
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )
  sys.exit(1)

URL = "https://consolemods.org/wiki/Xbox_360:Original_Xbox_Games_Compatibility_List"
OUTPUT_FILE_NAME = "xbox_360_original_xbox_games_compatibility_list"

STATUS_MAP = {
  "supported": "supported",
  "playable": "playable",
  "ingame": "in-game",
  "orange": "menus",
  "menus": "menus",
  "intro": "intro",
  "unplayable": "unplayable",
  "untested": "untested",
}

def fetch_page(
  url: str
) -> Optional[str]:
  try:
    print(f"Fetching page: '{url}'")

    response = requests.get(
      url,
      headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" },
      timeout=10
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
    table = find_by_section_id(soup)

    if table is not None:
      print("Found table by section.")
      return table

    print("Could not find table by section.")
    table = find_by_header(soup)

    if table is None:
      print("Could not find table by header.")
      return None

    print("Found table by section.")
    return table

  except Exception as e:
    print(f"Error: {e}")
    return None

def find_by_header(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  for table in soup.find_all("table"):
    headers = [
      th.text.strip()
      for th in table.find_all("th")
    ]

    if all(h in headers for h in ["Name", "Tested By", "Known Issues"]):
      return table

def find_by_section_id(
  soup: BeautifulSoup
) -> Optional[BeautifulSoup]:
  section = soup.find("span", id="Compatibility_List")

  if not section:
    return None

  element = section.parent

  while element:
    element = element.find_next_sibling()

    if element and element.name == "table":
      headers = [
        th.get_text(strip=True).lower()
        for th in element.find_all("th")
      ]

      if "name" in headers and "tested by" in headers and "known issues" in headers:
        return element

  return None

def extract_headers(
  table: BeautifulSoup
) -> List[str]:
  try:
    print("Extracting headers.")

    for tr in table.find_all("tr"):
      cells = tr.find_all(["th", "td"])

      if cells:
        return [
          cell.get_text(separator=" ", strip=True)
          for cell in cells
        ]

    return []

  except Exception as e:
    print(f"Error: {e}")
    return []

def process_row(
  cells: List[BeautifulSoup],
  headers: List[str]
) -> Optional[List[str]]:
  try:
    if len(cells) < len(headers):
      return None

    row = []

    for i, cell in enumerate(cells):
      if 0 < i < len(headers) - 2:
        a = cell.find("a")

        if a and a.has_attr("href"):
          fragment = a["href"].lstrip("#").strip()
          status = STATUS_MAP.get(fragment, fragment)
          row.append(status)
        else:
          row.append(cell.text.strip())
      else:
        row.append(cell.text.strip())

    return row

  except Exception as e:
    print(f"Error: {e}")
    return None

def extract_rows(
  table: BeautifulSoup,
  headers: List[str]
) -> List[List[str]]:
  try:
    valid_rows = table.find_all("tr")[1:]
    valid_rows_count = len(valid_rows)
    print(f"Extracting {valid_rows_count} rows...")
    extracted_rows = []
    index = 1

    for tr in valid_rows:
      cells = tr.find_all(["td", "th"])
      row = process_row(cells, headers)
      index += 1

      if not row:
        print(f"Could not process row: {index}")
        valid_rows_count -= 1
        continue

      extracted_rows.append(row)

    print(f"Extracted {valid_rows_count} rows.")
    return extracted_rows

  except Exception as e:
    print("Could not extract rows.")
    print(f"Error: {e}")
    return []

def write_csv(
  headers: List[str],
  extracted_rows: List[List[str]],
  output_file_name: str
) -> bool:
  try:
    output_file = f"{output_file_name}.csv"
    print(f"Writing to file: '{output_file}'")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(headers)
      writer.writerows(extracted_rows)

    print("Wrote to file.")
    return True

  except IOError as e:
    print("Could not write to file.")
    print(f"Error: {e}")
    return False

def write_json(
  headers: List[str],
  extracted_rows: List[List[str]],
  output_file_name: str
) -> bool:
  try:
    output_file = f"{output_file_name}.json"
    print(f"Writing to file: '{output_file}'")

    data = [
      dict(zip(headers, row))
      for row in extracted_rows
    ]

    with open(output_file, "w", encoding="utf-8") as jsonfile:
      json.dump(data, jsonfile, indent=2)

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

  try:
    print("Parsing page.")
    soup = BeautifulSoup(
      page_content,
      "html.parser"
    )

  except Exception as e:
    print("Could not parse page.")
    print(f"Error: {e}")
    return 1

  table = find_table(soup)

  if not table:
    return 1

  headers = extract_headers(table)

  if not headers:
    return 1

  extracted_rows = extract_rows(
    table,
    headers
  )

  if not extracted_rows:
    print("Warning: Could not extract data. No data rows exist.")
    return 1

  if not write_csv(
    headers,
    extracted_rows,
    OUTPUT_FILE_NAME
  ):
    return 1

  if not write_json(
    headers,
    extracted_rows,
    OUTPUT_FILE_NAME
  ):
    return 1

  return 0

if __name__ == "__main__":
  sys.exit(
    main()
  )