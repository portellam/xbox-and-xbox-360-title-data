#!/usr/bin/env python

#
# Filename:       config_databases.py
# Description:    Various SQLite database file(s) to parse and query.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
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