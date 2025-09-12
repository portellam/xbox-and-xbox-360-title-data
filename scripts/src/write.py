#!/usr/bin/env python

#
# Filename:       write.py
# Description:    Writes lists to CSV and JSON files.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import csv
import json
from typing import List

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