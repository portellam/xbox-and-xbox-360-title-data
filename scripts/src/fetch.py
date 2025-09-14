#!/usr/bin/env python

#
# Filename:       fetch.py
# Description:    Retrieve web page HTML as text.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
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