from bs4 import BeautifulSoup
import datetime
import pandas as pd
import platform
import re
import requests
import time

try:
  import aiohttp
  import asyncio
  IS_ASYNC_AVAILABLE = True
  PRIMARY_KEY = "Title ID"
  INPUT_FILE_EXTENSION = ".txt"
  INPUT_FILE = f"xbox_360_title_ids{INPUT_FILE_EXTENSION}"
  OUTPUT_FILE_EXTENSION = ".csv"
  OUTPUT_FILE = f"xbox_360_title_data{OUTPUT_FILE_EXTENSION}"
  FAILED_FILE = f"xbox_360_title_ids_failed{INPUT_FILE_EXTENSION}"
  URL = "https://archive.rushhosting.net/"

except ImportError:
  module = "aiohttp"
  command = f"pip install {module}"
  
  print(
    f"Warning: '{module}' not installed."
    + f" Falling back to synchronous mode. Run '{command}' for async support."
  )
  
  IS_ASYNC_AVAILABLE = False

def is_title_id(title_id):
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

def read_title_ids(file_path):
  if not isinstance(
    file_path,
    str
  ):
    type_name = type(file_path).__name__
    print(f"Error: File path must be a string, got {type_name}")
    return []

  title_id_list = []
  
  try:
   
    has_extension = file_path.lower().endswith(OUTPUT_FILE_EXTENSION)
    
    if has_extension:
      df = pd.read_csv(file_path)
      
      if PRIMARY_KEY in df.columns:
        title_id_list = df[PRIMARY_KEY].dropna().astype(str).tolist()
      
      else:
        raise ValueError(
          f"{OUTPUT_FILE_EXTENSION} file must contain a '{PRIMARY_KEY}' column."
        )
    
    else:
      with open(
        file_path,
        'r'
      ) as f:
        title_id_list = [line.strip() for line in f if line.strip()]
    
    valid_title_id_list = [
      title_id for title_id in title_id_list if is_title_id(title_id)
    ]
    
    if len(valid_title_id_list) != len(title_id_list):
      invalid_count = len(title_id_list) - len(valid_title_id_list)
      print(f"Warning: {invalid_count} invalid {PRIMARY_KEY}(s) found.")
    
    return valid_title_id_list
  
  except Exception as e:
    print(f"Error reading {PRIMARY_KEY}(s) from '{file_path}': {e}")
    return []

def log_failed_title_id(title_id):
  with open(FAILED_FILE, 'a') as f:
    f.write(f"{title_id}\n")

def fetch_url_sync(
  prefix,
  url,
  retries = 3,
  delay = 2
):
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

      print(f"{prefix}Error fetching '{url}': {e}")
      title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
      log_failed_title_id(title_id)
      return None

async def fetch_url_async(
  prefix,
  session,
  url,
  retries = 3,
  delay = 2
):
  for attempt in range(retries):
    try:
      async with session.get(
        url,
        timeout = 30
      ) as response:
        response.raise_for_status()
        return await response.text()
    
    except aiohttp.ClientError as e:
      do_backoff = attempt < retries - 1
      backoff_count_in_seconds = delay * (2 ** attempt)

      if do_backoff:
        await asyncio.sleep(backoff_count_in_seconds)
        continue
      
      print(f"{prefix}Error fetching {url}: {e}")
      title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
      log_failed_title_id(title_id)
      return None

def extract_game_data(
  prefix,
  html,
  url
):
  try:
    if not html:
      return None
    
    soup = BeautifulSoup(
      html,
      'html.parser'
    )
    
    regex = '([A-F0-9]+)'

    title_id_match = re.search(
      fr'{URL}{regex}', 
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

    name = name_elem.get_text(strip=True) if name_elem else 'N/A'
    
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
          tag.get_text(strip=True),
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
      description = next_elem.get_text(strip=True) if next_elem else 'N/A'
    
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
        headers = [cell.get_text(strip=True).lower() for cell in tr_list[0].find_all(['th', 'td'])]
        values = [cell.get_text(strip=True) for cell in tr_list[1].find_all(['th', 'td'])]

        for label, value in zip(headers, values):
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
      # 'Description': f'\"{description}\"',
      'Publisher': f'\"{published_by}\"',
      'Developer': f'\"{developed_by}\"',
      'Release date': release_date,
      'Has Local Multiplayer': has_local_multiplayer,
      'Has LAN Multiplayer': has_LAN_multiplayer,
      'Has Online Multiplayer': has_online_multiplayer
    }
  
  except Exception as e:
    print(f"{prefix}Error processing '{url}': {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

async def extract_game_data_async(
  prefix,
  session,
  url
):
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
    print(f"{prefix}Error processing '{url}': {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

def extract_game_data_sync(
  prefix,
  url
):
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
    print(f"{prefix}Error processing '{url}': {e}")
    title_id = re.search(r'[A-F0-9]{8}$', url).group(0) if re.search(r'[A-F0-9]{8}$', url) else 'Unknown'
    log_failed_title_id(title_id)
    return None

def write_to_file(
  data
):
  try:
    df = pd.DataFrame(data)
    
    df.to_csv(
      OUTPUT_FILE,
      index=False
    )

    print(f"Data saved to '{OUTPUT_FILE}' ({len(df)} records).")
  
  except Exception as e:
    print(f"Error writing to file: {e}")
    return None

async def main_async(title_id_list):
  try:
    game_url_list = [URL + title_id for title_id in title_id_list]
    data = []
    index = 0
    max_index = len(title_id_list)    
    connector = aiohttp.TCPConnector(limit = 5)

    async with aiohttp.ClientSession(connector = connector) as session:
      tasks = [
        extract_game_data_async(
          "",
          session,
          url
        ) for url in game_url_list
      ]

      completed_tasks = enumerate(asyncio.as_completed(tasks))

      for i, future in completed_tasks:
        result = await future
        index += 1
        
        if index % 50 == 0:
          print("Waiting 30 seconds...")
          await asyncio.sleep(30)
          
        prefix = f"Record {index} of {max_index}:"
        
        if result:
          print(f"{prefix}\tExtracted game data from {game_url_list[i]}")
          data.append(result)
          write_to_file(data)

  except Exception as e:
    print(f"Async processing failed: {e}")
    return None

def main_sync(title_id_list):
  try:
    game_url_list = [URL + title_id for title_id in title_id_list]
    data = []
    index = 1
    max_index = len(title_id_list)
    
    for url in game_url_list:
      prefix = f"Record {index} of {max_index}:"
      do_wait = index % 50 == 0 and index != 0
      wait_seconds = 30
    
      if do_wait:
        print(f"Waiting {wait_seconds} seconds...")
        time.sleep(wait_seconds)

      print(f"{prefix}\tExtracting game data from {url}")
      
      result = extract_game_data_sync(
        prefix,
        url
      )

      if result:
        data.append(result)
        write_to_file(data)

      index += 1
      time.sleep(0.5)
  
  except Exception as e:
    print(f"Sync processing failed: {e}")
    return None

if __name__ == "__main__":
  try:
    title_id_list = read_title_ids(INPUT_FILE)
    
    if not title_id_list:
      print(f"No valid {PRIMARY_KEY}(s) found. Exiting.")
      exit(1)
    
    has_incompatible_module = platform.system() == "Emscripten"

    if IS_ASYNC_AVAILABLE and not has_incompatible_module:
      asyncio.run(main_async(title_id_list))
    
    else:
      main_sync(title_id_list)
  
  except KeyboardInterrupt:
    print("Script interrupted by user.")
  
  except Exception as e:
    print(f"Script failed: {e}")