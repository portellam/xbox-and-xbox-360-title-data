#!/usr/bin/env python3

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
# THIRD PARTY NOTICES:
#
# This software uses the Google Sheets API under the Google APIs Terms of Service
# (https://developers.google.com/terms). You must comply with these terms when
# using this script, including rate limits and data usage restrictions.
#
# Google and Google Sheets are trademarks of Google LLC. This software is not
# affiliated with, endorsed by, or sponsored by Google LLC.
#
# DATA USAGE NOTICE:
#
# This script only accesses publicly available Google Sheets. Users are
# responsible for ensuring they have permission to access and process the data
# retrieved. Respect the privacy and terms of service of the original sheet
# creators.
#
# USAGE WARNING:
#
#   - Only use with sheets marked "Anyone with the link can view".
#   - Respect sheet owners' terms of use.
#   - Do not scrape private or restricted content.
#   - Comply with robots.txt and rate limits.
#

#
# Filename:       get_google_sheets.py
# Description:    Retrieves data from public Google Sheet(s) and outputs as JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

GOOGLE_API_QUOTA_LIMIT_IN_SECONDS = 2.000  # Set as thirty (30) quotas/minute. Actual is sixty (60) quotas/minute.

import sys
import time

from typing import (
  Dict,
  List,
  Optional
)

from config_google_sheet import (
  URL_LIST,
  NAME_LIST,
  FILE_NAME_LIST
)

try:
  from gspread import (
    Spread
  )

  import pandas

  module = "gspread"
  actual_version = pkg_resources.get_distribution("gspread").version
  expected_version = "5.0.0"

  if actual_version < expected_version:
    print(
      f"{module} version is too old."
      + f" Required: >={expected_version}, Installed: " + actual_version
    )

    command = f"pip install --upgrade {module}>={expected_version}"
    print(f"Please update using '{command}'")
    sys.exit(1)

except ImportError as e:
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )

  sys.exit(1)

from write import (
  write_json
)

def parse_this(
  sheet_url: str,
  sheet_name: str,
  output_name: str
) -> int:
  try:
    if sheet_url is None:
      print("URL is not valid.")
      raise TypeError

    if sheet_name is None:
      print("Google Sheet name is not valid.")
      raise TypeError

    if output_name is None:
      print("Output name is not valid.")
      raise TypeError

    print(f"Found Google Sheet: '{sheet_url}'")

    gc = gspread.url()

    quota_limit_in_seconds_str = str(GOOGLE_API_QUOTA_LIMIT_IN_SECONDS).rstrip('0')
    quota_limit_in_seconds_str = quota_limit_in_seconds_str.rstrip('.')
    print(f"Waiting {quota_limit_in_seconds_str} second(s).")
    time.sleep(GOOGLE_API_QUOTA_LIMIT_IN_SECONDS)

    print(f"Fetching Google Sheet.")
    spreadsheet = gc.open_by_url(sheet_url)
    worksheet = spreadsheet.worksheet(sheet_name)
    data_list = worksheet.get_all_values()

    if not data_list:
      print("No data found in sheet.")
      return 1

    header_list = data_list[0]
    row_list = data_list[1:]

    if not header_list or not row_list:
      print("No valid data found in sheet.")
      return 1

    dataframe = pandas.DataFrame(
      row_list,
      columns=header_list
    )

    print(f"Found {len(header_list)} header(s).")
    row_list = dataframe.to_dict('records')
    print(f"Extracted {len(row_list)} row(s).")

    if not write_json(
      header_list,
      row_list,
      output_name
    ):
      return 1

    return 0

  except Exception as e:
    print("Could not process Google Sheet.")
    print(f"Error: {e}")
    return 1

def main() -> int:
  partial_success = False
  complete_success = True

  for index, value in enumerate(
    URL_LIST,
    start = 0
  ):
    sheet_name = NAME_LIST[index]
    output_name = FILE_NAME_LIST[index]

    result = parse_this(
      value,
      sheet_name,
      output_name
    )

    if result == 0:
      partial_success = True

    else:
      complete_success = False

  if complete_success:
    return 0

  if not partial_success:
    return 1

  return 2

if __name__ == "__main__":
  try:
    sys.exit(
      main()
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")