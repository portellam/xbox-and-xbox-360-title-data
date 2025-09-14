#!/usr/bin/env python

#
# Filename:       parse_html_to_json.py
# Description:    Parses multiple HTML tables from ConsoleMods.org,
#                 removes newlines, and outputs each to a separate JSON file.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

import re
import sys
import json

from typing import (
  Dict,
  List,
  Optional
)

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

from config_consolemods import (
  OUTPUT_FILE_NAME,
  URL
)
from get_consolemods_tables import (
  write_many
)

def main() -> int:
  return write_many(
    URL,
    OUTPUT_FILE_NAME
  )

if __name__ == "__main__":
  try:
    sys.exit(main())

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")