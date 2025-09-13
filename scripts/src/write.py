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
      print(f"Skipped writing to file: '{output_file}'")
      return False

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

  except IOError as e:
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
    print()
    return 1

  if not name:
    print("Warning: File name is not valid.")
    print()
    return 1

  if not row_list:
    print(f"Note: Output is empty.")
    print()
    return 2

  if not write_json(
    header_list,
    row_list,
    name
  ):
    print()
    return 1

  print()
  return 0