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
# Filename:       get_many_databases.py
# Description:    Download and query SQLite database(s) as specified in config.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

import csv
import json
import os
import sqlite3
import sys
import tempfile
import urllib.request

from typing import (
  Dict,
  List
)

from config_databases import (
  DB_QUERY_MAP
)

from get_this_database import (
  download_and_query
)

def main() -> int:
  partial_success = False
  complete_success = True

  for value in DB_QUERY_MAP:
    result = download_and_query(
      value['path'],
      value['name'],
      value['query']
    )

    if result == 0:
      partial_success = True

    else:
      complete_success = False

  if complete_success:
    return 0

  if not partial_success:
    return 1

if __name__ == "__main__":
  try:
    sys.exit(
      main()
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")