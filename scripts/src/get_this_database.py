#
# Filename:       get_database.py
# Description:    Download and query a SQLite database.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import csv
import json
import os
import sqlite3
import tempfile
import urllib.request

from typing import (
  Dict,
  List
)

from config import (
  OUTPUT_DB_PATH
)

from sanitize_file import (
  sanitize_file_name
)

from write import (
  write_this
)

def download_db(
  db_url: str,
  db_file_name: str,
  db_parent_path: str = OUTPUT_DB_PATH
) -> str:
  try:
    print(f"Downloading database: '{db_url}'.")

    os.makedirs(
      os.path.dirname(db_parent_path) or '.',
      exist_ok = True
    )

    if not db_file_name:
      db_file_name = os.path.basename(db_url)

    expected_file_extension = ".db"

    if not db_file_name.endswith(expected_file_extension):
      db_file_name += expected_file_extension

    db_path = db_parent_path + db_file_name

    with urllib.request.urlopen(db_url) as response:
      with open(
        db_path,
        'wb'
      ) as perm_file:
        perm_file.write(response.read())

    print(f"Downloaded database: '{db_path}'")
    return db_path

  except Exception as e:
    print("Could not download database.")
    print(f"Error: {e}")
    raise

def execute_query(
  db_path: str,
  query: str
) -> List[
  Dict[
    str,
    str
  ]
]:
  try:
    print(f"Executing query on '{db_path}'.")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    row_list = cursor.fetchall()

    if not row_list:
      print("No data.")
      raise Exception

    header_list = [
      description[0]
      for description in cursor.description
    ]

    new_row_list = [
      dict(
        zip(
          header_list,
          row
        )
      )
      for row in row_list
    ]

    conn.close()
    print(f"Executed query.")
    return new_row_list

  except Exception as e:
    print("Could not execute query.")
    print(f"Error: {e}")

    if 'conn' in locals():
      conn.close()

    raise

def write_results(
  db_url: str,
  name: str,
  header_list: List[str],
  row_list: List[
    Dict[
      str,
      str
    ]
  ]
) -> int:
  if not db_url:
    print("Warning: database path is not valid.")
    return 1

  if not name:
    print("Warning: file name is not valid.")
    return 1

  if not row_list:
    print("Warning: output is empty.")
    return 2

  if not write_this(
    name,
    header_list,
    row_list
  ):
    return 1

  return 0

def download_and_query(
  db_url: str,
  name: str,
  query: str
) -> int:
  db_path = None

  if type(name) is not str:
    return 2

  try:
    if not db_url:
      print("Warning: database path is not valid.")
      return 1

    if not name:
      print("Warning: file name is not valid.")
      return 1

    name = sanitize_file_name(name)

    db_path = download_db(
      db_url,
      name,
      OUTPUT_DB_PATH
    )

    row_list = execute_query(
      db_path,
      query
    )

    if not row_list:
      print("No results from query.")
      return 2

    header_list = [
      key
      for key in row_list[0].keys()
    ]

    result = write_results(
      db_url = db_url,
      name = name,
      header_list = header_list,
      row_list = row_list
    )

    if result != 0:
      return result

    print("Executed query.")
    return 0

  except Exception as e:
    print(f"Error: {e}")
    return 1