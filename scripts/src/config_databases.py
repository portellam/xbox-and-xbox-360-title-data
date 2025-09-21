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
# Filename:       config_databases.py
# Description:    Various SQLite database file(s) to parse and query.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

DB_QUERY_MAP = [
  # {
  #   'path': "http://website.com/database.db",   # URL goes here.
  #   'name': "Database Name",                    # Name of output file goes here.
  #   'query': "SELECT *",                        # SQL query goes here.
  # },
  {
    'path': 'https://www.mobcat.zip/XboxIDs/titleIDs.db',
    'name': 'MobCat\'s Original Xbox Title ID Database',
    'query': 'SELECT * FROM TitleIDs ORDER BY TitleIDs.Title_ID'
  }
]