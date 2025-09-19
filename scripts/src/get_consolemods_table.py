#!/usr/bin/env python

#
# Filename:       get_consolemods_table.py
# Description:    Retrieves table from `www.consolemods.org`, and outputs to file.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import sys

from config_consolemods import (
  URL,
  FILE_NAME,
  HEADER_KEY_LIST,
  HEADER_MAP,
  REQUIRED_HEADER_LIST,
  STATUS_MAP
)

from get_wiki_table import (
  main
)

if __name__ == "__main__":
  try:
    sys.exit(
      main(
        URL,
        FILE_NAME,
        HEADER_KEY_LIST,
        REQUIRED_HEADER_LIST,
        HEADER_MAP,
        STATUS_MAP
      )
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")