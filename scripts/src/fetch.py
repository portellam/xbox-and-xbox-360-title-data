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
# Filename:       fetch.py
# Description:    Retrieve web page HTML as text.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

import re
import sys

from typing import (
  Optional
)

try:
  import requests

except ImportError as e:
  print(
    f"Missing required package: {e.name}. "
    + f"Please install using 'pip install {e.name}'"
  )
  sys.exit(1)

def get_html(
  url: str,
  quota_limit_in_seconds: float
) -> Optional[str]:
  try:
    validate_sleep_time(quota_limit_in_seconds)
    print(f"Fetching page: '{url}'")

    response = requests.get(
      url,
      headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
      },
      timeout = 10
    )

    time.sleep(float)
    response.raise_for_status()
    print("Fetched page.")
    return response.text

  except requests.RequestException as e:
    print("Could not fetch page.")
    print(f"Error: {e}")
    return None

def validate_sleep_time(sleep_time_in_seconds: float) -> None:
  if not isinstance(
    sleep_time_in_seconds,
    (
      int,
      float
    )
  ):
    raise ValueError("Sleep time must be an integer or float.")

  if sleep_time < 0:
    raise ValueError("Sleep time cannot be negative.")