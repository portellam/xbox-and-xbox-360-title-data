#!/usr/bin/env python

#
# Filename:       write.py
# Description:    Writes lists to JSON files.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import csv
import json

from typing import (
  Dict,
  List
)

from sanitize_file import (
  sanitize_file_name
)

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
    output_file = f"{name}.json"

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
  url: str,
  name: str,
  header_list: List[str],
  row_list: List[
    Dict[
      str,
      str
    ]
  ]
) -> int:
  if not url:
    print("Warning: URL is not valid.")
    return 1

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

  return 0