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
# THIRD PARTY NOTICES:
#
# This software accesses content from www.consolemods.org for personal,
# non-commercial research and archival purposes only. You must comply with the
# ConsoleMods.org Terms of Service
# (https://www.consolemods.org/wiki/Terms_of_Service) and robots.txt file
# (https://www.consolemods.org/robots.txt).
#
# ConsoleMods.org and related trademarks are property of their respective owners.
# This software is not affiliated with, endorsed by, or sponsored by
# ConsoleMods.org.
#
# USAGE RESTRICTIONS:
#
# • Respect rate limits and robots.txt directives.
# • Do not use for commercial purposes without explicit permission.
# • Do not overload or disrupt consolemods.org services.
# • Only access publicly available data.
# • Include appropriate attribution to ConsoleMods.org when redistributing data.
#
# ROBOTS.TXT COMPLIANCE NOTICE:
#
# This script respects the ConsoleMods.org robots.txt file. Certain paths may be
# disallowed. Always check https://www.consolemods.org/robots.txt before use.
#

#
# Filename:       get_consolemods_table.py
# Description:    Retrieves table from `www.consolemods.org`, and outputs to file.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

CONSOLEMODS_HTTP_QUOTA_LIMIT_IN_SECONDS = 5.000   # Unknown value. As a courtesy, set as twelve (12) quotas/minute.

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
        STATUS_MAP,
        CONSOLEMODS_HTTP_QUOTA_LIMIT_IN_SECONDS
      )
    )

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Script failed: {e}")