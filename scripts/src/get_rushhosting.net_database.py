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
# Filename:       get_rushhosting.net_database.py
# Description:    Retrieves data from archive.rushhosting.net pages, and outputs
#                 as JSON.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

import datetime
import re
import sys
import time

from typing import (
  List,
  Optional
)

try:
  import aiohttp
  import asyncio
  import pandas

  from bs4 import (
    BeautifulSoup
  )

except ImportError as e:
  print(f"Missing required package: {e.name}. Please install using 'pip install {e.name}'")
  sys.exit(1)

PRIMARY_KEY = "Title ID"
INPUT_FILE_EXTENSION = ".txt"
INPUT_FILE = f"xbox_360_title_ids{INPUT_FILE_EXTENSION}"
OUTPUT_FILE_EXTENSION = ".csv"
OUTPUT_FILE = f"archive.rushhosting.net_xbox_360_title_id_list{OUTPUT_FILE_EXTENSION}"
FAILED_FILE = f"xbox_360_title_ids_failed{INPUT_FILE_EXTENSION}"
BASE_URL = "https://archive.rushhosting.net/"

def is_title_id(
  title_id: str
) -> bool:
  if not isinstance(
    title_id,
    str
  ):
    return False

  regex = r'^[A-F0-9]{8}$'

  is_match = re.match(
    regex,
    title_id
  ) is not None

  return is_match

def read_title_list(
  file_path: str
) -> List[str]:
  if not isinstance(
    file_path,
    str
  ):
    type_name = type(file_path).__name__
    print(f"Error: File path must be a string, got {type_name}")
    return []

  title_list = []

  try:
    has_extension = file_path.lower().endswith(OUTPUT_FILE_EXTENSION)

    if has_extension:
      df = pandas.read_csv(file_path)

      if PRIMARY_KEY in df.columns:
        title_list = df[PRIMARY_KEY].dropna().astype(str).tolist()

      else:
        raise ValueError(f"{OUTPUT_FILE_EXTENSION} file must contain a '{PRIMARY_KEY}' column.")

    else:
      with open(
        file_path,
        'r'
      ) as f:
        title_list = [line.strip() for line in f if line.strip()]

    valid_title_list = [
      title_id for title_id in title_list if is_title_id(title_id)
    ]

    if len(valid_title_list) != len(title_list):
      invalid_count = len(title_list) - len(valid_title_list)
      print(f"Warning: {invalid_count} invalid {PRIMARY_KEY}(s) found.")

    return valid_title_list

  except Exception as e:
    print(f"Error: {e}")
    return []

def log_failed_title_id(
  title_id: str
) -> None:
  with open(FAILED_FILE, 'a') as f:
    f.write(f"{title_id}\n")

def fetch_url_sync(
  prefix: str,
  url: str,
  retries: int = 3,
  delay: int = 2
) -> Optional[str]:
  for attempt in range(retries):
    try:
      response = requests.get(
        url,
        timeout = 30
      )

      response.raise_for_status()
      return response.text

    except requests.RequestException as e:
      do_backoff = attempt < retries - 1
      backoff_count_in_seconds = delay * (2 ** attempt)

      if do_backoff:
        time.sleep(backoff_count_in_seconds)
        continue

      print(f"Error: {e}")
      title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
      log_failed_title_id(title_id)
      return None

async def fetch_url_async(
  prefix: str,
  session: aiohttp.ClientSession,
  url: str,
  retries: int = 3,
  delay: int = 2
) -> Optional[str]:
  for attempt in range(retries):
    try:
      async with session.get(
        url,
        timeout = 30
      ) as response:
        response.raise_for_status()
        return await response.text()

    except aiohttp.ClientError as e:
      if attempt < retries - 1:
        await asyncio.sleep(delay * (2 ** attempt))
        continue

      print(f"Error: {e}")
      title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
      log_failed_title_id(title_id)
      return None

def extract_game_data(
  prefix: str,
  html: Optional[str],
  url: str
) -> Optional[dict]:
  try:
    if not html:
      return None

    soup = BeautifulSoup(
      html,
      'html.parser'
    )

    regex = '([A-F0-9]+)'

    title_id_match = re.search(
      fr'{BASE_URL}{regex}',
      url
    )

    title_id = title_id_match.group(1) if title_id_match else 'N/A'

    name_elem = (
      soup.select_one('head title')
      or soup.find('h1')
      or soup.find('h2')
      or soup.select_one('div.game-title h2, h3, div.title')
      or soup.find(
        'div',
        class_ = re.compile(
            r'title|game|name|header',
            re.I
          )
      )
    )

    name = name_elem.get_text(strip = True) if name_elem else 'N/A'

    description = 'N/A'

    desc_elem = (
      soup.find(
        'div',
        class_ = re.compile(
          r'description|summary|overview|info|about',
          re.I
        )
      )
      or soup.find(
        'section',
        class_ = re.compile(
          r'description|summary|overview|info',
          re.I
        )
      )
      or soup.find(
        lambda tag: tag.name in ['h2', 'h3', 'div']
        and re.search(
          r'description|summary|overview|about',
          tag.get_text(strip = True),
          re.I
        )
      )
    )

    if desc_elem:
      next_elem = (
        desc_elem.find_next_sibling('p')
        or desc_elem.find_next('p')
        or desc_elem.find_parent().select_one('p, div.description-text, div.summary')
      )
      description = next_elem.get_text(strip = True) if next_elem else 'N/A'

    published_by = developed_by = release_date = 'N/A'

    table = (
      soup.find(
        'table',
        class_ = re.compile(
            r'info|details|metadata|gameinfo', 
            re.I
          )
      )
      or soup.find('table')
    )

    if table:
      tbody = table.find('tbody') or table
      tr_list = tbody.find_all('tr')

      if len(tr_list) >= 2:
        header_list = [cell.get_text(strip = True).lower() for cell in tr_list[0].find_all(['th', 'td'])]
        value_list = [cell.get_text(strip = True) for cell in tr_list[1].find_all(['th', 'td'])]

        for label, value in zip(header_list, value_list):
          if 'published by' in label or 'publisher' in label:
            published_by = value

          elif 'developed by' in label or 'developer' in label:
            developed_by = value

          elif 'release date' in label or 'released' in label or 'launch' in label:
            release_date = value

            if release_date != 'N/A':
              release_date = datetime.datetime.strptime(release_date, "%m/%d/%Y").strftime("%Y/%m/%d")

            else:
              release_date = f'\"{release_date}\"'

    cap_section = (
      soup.find(
        'div',
        class_ = re.compile(
          r'capabilities|features|multiplayer|support',
          re.I
        )
      )
      or soup.find(
        'section',
        class_ = re.compile(
          r'capabilities|features|multiplayer',
          re.I
        )
      )
    )

    text = cap_section.get_text().lower() if cap_section else html.lower()

    has_local_multiplayer = False
    has_LAN_multiplayer = False
    has_online_multiplayer = False

    if 'coop' in text or 'co-op' in text:
      has_local_multiplayer = True

    if 'system link' in text:
      has_LAN_multiplayer = True

    if 'xbox live' in text:
      has_online_multiplayer = True

    return {
      f'{PRIMARY_KEY}': f'\'{title_id}',
      'Name': f'\"{name}\"',
      'Publisher': f'\"{published_by}\"',
      'Developer': f'\"{developed_by}\"',
      'Release date': release_date,
      'Has Local Multiplayer': has_local_multiplayer,
      'Has LAN Multiplayer': has_LAN_multiplayer,
      'Has Online Multiplayer': has_online_multiplayer
    }

  except Exception as e:
    print(f"Error: {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

async def extract_game_data_async(
  prefix: str,
  session: aiohttp.ClientSession,
  url: str
) -> Optional[dict]:
  try:
    html = await fetch_url_async(
      prefix,
      session,
      url
    )

    return extract_game_data(
      prefix,
      html,
      url
    )

  except Exception as e:
    print(f"Error: {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

def extract_game_data_sync(
  prefix: str,
  url: str
) -> Optional[dict]:
  try:
    html = fetch_url_sync(
      prefix,
      url
    )

    return extract_game_data(
      prefix,
      html,
      url
    )

  except Exception as e:
    print(f"Error: {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

def write_csv(
  data: List[dict]
) -> None:
  try:
    df = pandas.DataFrame(data)

    df.to_csv(
      OUTPUT_FILE,
      index=False
    )

    print(f"Wrote to file: '{OUTPUT_FILE}' ({len(df)} records).")

  except Exception as e:
    print(f"Error: {e}")

async def main_async(
  title_list: List[str]
) -> int:
  try:
    game_url_list = [BASE_URL + title_id for title_id in title_list]
    data = []
    index = 0
    max_index = len(title_list)
    connector = aiohttp.TCPConnector(limit = 5)

    async with aiohttp.ClientSession(connector = connector) as session:
      task_list = [
        extract_game_data_async(
          "",
          session,
          url
        ) for url in game_url_list
      ]

      completed_tasks = enumerate(asyncio.as_completed(task_list))

      for i, future in completed_tasks:
        result = await future
        index += 1
        do_wait = index % 50 == 0 and index != 0
        wait_seconds = 30

        if do_wait:
          print(f"Waiting {wait_seconds} seconds...")
          await asyncio.sleep(wait_seconds)

        prefix = f"Record {index} of {max_index}:"

        if result:
          print(f"{prefix}\tExtracted game data from {game_url_list[i]}")
          data.append(result)
          write_csv(data)

    return 0

  except Exception as e:
    print(f"Error: {e}")
    return 1

def main_sync(
  title_list: List[str]
) -> int:
  try:
    game_url_list = [BASE_URL + title_id for title_id in title_list]
    data = []
    index = 1
    max_index = len(title_list)

    for url in game_url_list:
      prefix = f"Record {index} of {max_index}:"

      if index % 50 == 0 and index != 0:
        print(f"Waiting 30 seconds...")
        time.sleep(30)

      print(f"{prefix}\tExtracting game data from {url}")

      result = extract_game_data_sync(
        prefix,
        url
      )

      if result:
        data.append(result)
        write_csv(data)

      index += 1
      time.sleep(0.5)

    return 0

  except Exception as e:
    print(f"Error: {e}")
    return 1

def main() -> int:
  title_list = read_title_list(INPUT_FILE)

  if not title_list:
    print(f"No valid {PRIMARY_KEY}(s) found.")
    return 1

  try:
    import platform
    has_incompatible_module = platform.system() == "Emscripten"

    if not has_incompatible_module:
      return asyncio.run(main_async(title_list))

    return main_sync(title_list)

  except Exception as e:
    print(f"Error: {e}")
    return 1

if __name__ == "__main__":
  try:
    sys.exit(main())

  except KeyboardInterrupt:
    print("Script interrupted by user.")

  except Exception as e:
    print(f"Error: {e}")