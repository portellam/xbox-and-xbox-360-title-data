#!/usr/bin/env python

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

#
# Filename:       write.py
# Description:    Writes lists to JSON files.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

import csv
import json

from typing import (
  Dict,
  List
)

from config import (
  OUTPUT_BASE_PATH,
  OUTPUT_CSV_PATH,
  OUTPUT_JSON_PATH
)

from sanitize_file import (
  sanitize_file_name
)

def write_csv(
  header_list: List[str],
  text: List[
    Dict[
      str,
      str
    ]
  ],
  name: str
) -> bool:
  try:
    output_file = f"{OUTPUT_CSV_PATH}{name}.csv"

    if not header_list:
      print("No data.")
      raise Exception

    print(f"Writing to file: '{output_file}'")

    with open(
      output_file,
      "w",
      newline = "",
      encoding = "utf-8"
    ) as csvfile:
      writer = csv.DictWriter(
        csvfile,
        fieldnames = header_list
      )
      writer.writeheader()
      writer.writerows(text)

    print("Wrote to file.")
    return True

  except Exception as e:
    print("Could not write to file.")
    print(f"Error: {e}")
    return False

def write_json(
  header_list: List[str],
  text: List[
    Dict[
      str,
      str
    ]
  ],
  name: str
) -> bool:
  try:
    output_file = f"{OUTPUT_JSON_PATH}{name}.json"

    if not header_list:
      print("No data.")
      raise Exception

    print(f"Writing to file: '{output_file}'")

    with open(
      output_file,
      "w",
      encoding = "utf-8"
    ) as jsonfile:
      json.dump(
        text,
        jsonfile,
        indent = 2
      )

    print("Wrote to file.")
    return True

  except Exception as e:
    print("Could not write to file.")
    print(f"Error: {e}")
    return False

def write_this(
  name: str,
  header_list: List[str],
  row_list: List[
    Dict[
      str,
      str
    ]
  ]
) -> int:
  if not name:
    print("Warning: file name is not valid.")
    return 1

  if not row_list:
    print(f"Warning: output is empty.")
    return 2

  try:
    name = sanitize_file_name(name)

  except Exception as e:
    print(f"Error: {e}")
    return 1

  if not write_json(
    header_list,
    row_list,
    name
  ):
    return 1

  if not write_csv(
    header_list,
    row_list,
    name
  ):
    return 1

  return 0