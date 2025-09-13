#!/usr/bin/env python

#
# Filename:       sanitize_html.py
# Description:    Sanitizes HTML and can parse HTML with multiple tables.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# Version:        1.0.0
#

# Must come before `bs4`
import collections
import collections.abc
collections.Callable = collections.abc.Callable

import requests

from bs4 import (
  BeautifulSoup
)

from fetch import (
  fetch_page
)

def sanitize_table(
  table
):
  td_list = table.find_all('td')

  for td in td_list:
    is_empty = not td.get_text(strip = True)

    if not is_empty:
      continue

    div = td.find('div')
    has_title = div and div.has_attr('title')

    if not has_title:
      continue

    td.append(div['title'])

  return table

def format_html(
  element,
  level = 0
):
  indent = '  ' * level

  if isinstance(
    element,
    str
  ):
    return indent + element.strip()

  if not hasattr(
    element,
    'contents'
  ) or not element.contents:
    return indent + str(element)

  has_nested = any(child.name for child in element.contents)

  if not has_nested:
    text = ''.join(str(c).strip() for c in element.contents)
    return f"{indent}<{element.name}{format_attrs(element)}>{text}</{element.name}>"

  inner = []
  trailing_text = ''

  for child in element.contents:
    if isinstance(
      child,
      str
    ):
      stripped = child.strip()

      if stripped:
        trailing_text += stripped

      continue

    inner.append(
      format_html(
        child,
        level + 1
      )
    )

  inner_text = '\n'.join(inner)
  trailing = trailing_text if trailing_text else ''

  return f"{indent}<{element.name}{format_attrs(element)}>"
  + f"\n{inner_text}{trailing and trailing}\n{indent}</{element.name}>"

def format_attrs(
  tag
):
  if not tag.attrs:
    return ''

  attributes = " ".join(v) if isinstance(
    v,
    list
  ) else v for k,
  v in tag.attrs.items()

  return ' '
  + ' '.join(f'{k}="{attributes}"')

def retrieve_and_process_tables(
  url
):
  text = fetch_page(url)

  if not text:
    return []

  soup = BeautifulSoup(
    text,
    'lxml'
  )

  table_list = soup.find_all('table')
  sanitized_list = []

  for table in table_list:
    sanitized_table = sanitize_table(table)
    sanitized_list.append(sanitized_table)

  return sanitized_list

def export_html(
  html_content,
  output_file
):
  with open(
    output_file,
    'w',
    encoding='utf-8'
  ) as f:
    f.write(html_content)