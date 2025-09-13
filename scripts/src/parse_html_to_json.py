#!/usr/bin/env python

#
# Filename:       parse_html_to_json.py
# Description:    Parses multiple HTML tables from ConsoleMods.org,
#                 removes newlines, and outputs each to a separate JSON file.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import re
import sys
import json

from typing import (
  Dict,
  List,
  Optional
)

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

try:
  import requests

  from bs4 import (
    BeautifulSoup
  )

except ImportError as e:
  print(
    f"Missing required package: {e.name}. Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

URL = "https://consolemods.org/wiki/Xbox_360:Original_Xbox_Games_Compatibility_List"

OUTPUT_PATH = "../../databases/json/"

OUTPUT_FILE_NAME = f"{OUTPUT_PATH}consolemods.org_xbox_360_original_xbox_games_compatibility_list"

HEADER_KEY_LIST = [
  "Name",
  "1",
  "2",
  "3",
  "5",
  "1_1",
  "6",
  "7",
  "7b",
  "19",
  "21a",
  "21b",
  "21c",
  "Known Issues",
  "Tested By"
]

HEADER_MAP = {
  "1": "xefu",
  "2": "xefu2",
  "3": "xefu3",
  "5": "xefu5",
  "1_1": "xefu1_1",
  "6": "xefu6",
  "7": "xefu7",
  "7b": "xefu7b",
  "19": "xefu2019",
  "21a": "xefu2021a",
  "21b": "xefu2021b",
  "21c": "xefu2021c"
}

STATUS_MAP = {
  "supported": "supported",
  "playable": "playable",
  "ingame": "in-game",
  "in-game": "in-game",
  "orange": "menus",
  "intro": "in-game",
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

def sanitize_html(
  table: BeautifulSoup
) -> str:
  td_list = table.find_all('td')

  for td in td_list:
    div = td.find('div')
    has_title = div and div.has_attr('title')

    if has_title and not td.get_text(strip = True):
      td.clear()
      td.string = div['title'].strip()

  return str(table).replace('\n', '')

def extract_cell_value(
  cell: BeautifulSoup,
  is_status_column: bool
) -> str:
  div = cell.find('div')

  if div and div.has_attr('title') and is_status_column:
    return STATUS_MAP.get(div['title'].lower().strip(), div['title'].strip())

  text = cell.get_text(strip = True)

  if text:
    return STATUS_MAP.get(text.lower(), text) if is_status_column else text

  return ""

def extract_table_data(
  table: BeautifulSoup
) -> tuple[List[str], List[Dict[str, str]]]:
  try:
    header_list = []
    thead = table.find("thead")

    if thead:
      header_cells = thead.find_all("th")

    else:
      header_cells = table.find_all(
        "th",
        limit = len(HEADER_KEY_LIST)
      )

    inverted_header_map = {v: k for k, v in HEADER_MAP.items()}

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

    print("Extracting rows.")
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
        is_status_column = header in HEADER_MAP or header in HEADER_MAP.values()

        value = extract_cell_value(
          cell,
          is_status_column
        )

        if value == header or not value:
          continue

        row_data[header] = value

      if not row_data or "Name" not in row_data:
        continue

      row_list.append(row_data)

    return header_list, row_list

  except Exception as e:
    print("Could not extract table data.")
    print(f"Error: {e}")
    return [], []

def find_tables(
  soup: BeautifulSoup
) -> List[BeautifulSoup]:
  table_list = soup.find_all("table")

  if not table_list:
    print("No tables found.")
    return []

  print(f"Found {len(table_list)} tables.")
  return table_list

def write_json(
  header_list: List[str],
  row_list: List[Dict[str, str]],
  output_file: str
) -> bool:
  try:
    if not row_list:
      print(f"Skipped writing to file: '{output_file}'")
      return False

    print(f"Writing to file: '{output_file}'")
    with open(
      output_file,
      "w",
      encoding = "utf-8"
    ) as jsonfile:
      json.dump(
        row_list,
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

  soup = BeautifulSoup(
    page_content,
    "html.parser"
  )

  table_list = find_tables(soup)

  if not table_list:
    return 1

  index = 1
  for table in table_list:
    sanitized_html = sanitize_html(table)
    print(f"Sanitized HTML for table {index}: {sanitized_html[:100]}...")
    header_list, row_list = extract_table_data(table)

    if not row_list:
      print(f"Note: Output for table {index} is empty.")
      index += 1
      continue

    output_file = f"{OUTPUT_FILE_NAME}_table_{index}.json"

    if not write_json(
      header_list,
      row_list,
      output_file
    ):
      return 1

    index += 1

  return 0

if __name__ == "__main__":
  try:
    sys.exit(main())

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")