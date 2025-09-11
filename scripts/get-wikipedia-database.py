#!/usr/bin/env python

#
# Filename:       get-wikipedia-database.py
# Description:    Retrieves tables from specified Wikipedia articles, and outputs as
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

URL_LIST = [
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(A%E2%80%93L)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(M%E2%80%93Z)",
  "https://en.wikipedia.org/wiki/List_of_Xbox_360_System_Link_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games",
  "https://en.wikipedia.org/wiki/List_of_Xbox_games_compatible_with_Xbox_360"
]

OUTPUT_FILE_NAME_LIST = [
  "wikipedia.org_xbox_360_games_a-l",
  "wikipedia.org_xbox_360_games_m-z",
  "wikipedia.org_xbox_360_system_link_games",
  "wikipedia.org_xbox_games",
  "wikipedia.org_xbox_games_compatible_with_xbox_360"
]

ELEMENT_TAG_LIST = [
  "th",
  "td"
]

def fetch_page(
  url: str
) -> Optional[str]:
  try:
    print(f"Fetching page: '{url}'")

    response = requests.get(
      url,
      headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
      },
      timeout = 10
    )

    response.raise_for_status()
    print("Fetched page.")
    return response.text

  except requests.RequestException as e:
    print("Could not fetch page.")
    print(f"Error: {e}")
    return None

def find_tables(
  soup: BeautifulSoup
) -> List[BeautifulSoup]:
  try:
    table_list = soup.find_all("table", {"class": "wikitable"})

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
        zip(
          header_list,
          row
        )
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
  for url, output_name in zip(
    URL_LIST,
    OUTPUT_FILE_NAME_LIST
  ):
    page_content = fetch_page(url)

    if not page_content:
      continue

    print("Parsing page.")

    soup = BeautifulSoup(
      page_content,
      "html.parser"
    )

    table_list = find_tables(soup)

    if not table_list:
      continue

    index = 1

    for actual_index, table in enumerate(
      table_list,
      start = 1
    ):
      header_list = extract_headers(table)

      if not header_list:
        continue

      extracted_row_list = extract_rows(
        table,
        header_list
      )

      if not extracted_row_list:
        print("Warning: Could not extract data. No data rows exist.")
        continue

      file_suffix = f"{output_name}_table_{index}"
      index += 1

      if not write_csv(
        header_list,
        extracted_row_list,
        file_suffix
      ):
        continue

      if not write_json(
        header_list,
        extracted_row_list,
        file_suffix
      ):
        continue

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