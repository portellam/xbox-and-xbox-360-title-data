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
  get_html
)

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
    text = ''.join(
      str(c).strip() for c in element.contents
    )

    return format_html_element(
      indent,
      element,
      text
    )

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

  return format_html_element(
    indent,
    element,
    f"\n{inner_text}{trailing and trailing}\n{indent}"
  )

def format_html_attributes(
  tag
):
  if not tag.attrs:
    return ''

  return ' '
  + ' '.join(
    f'{k}="{ " ".join(v) if isinstance(v, list) else v }"'
    for k, v in tag.attrs.items()
  )

def format_html_element(
  indent: str,
  element,
  text: str
):
  if not element:
    return ""

  attributes = format_html_attributes(element)

  return f"{indent}"
  + f"<{element.name}{attributes}>{text}</{element.name}>"

def get_html_tables(
  url
):
  text = get_html(url)

  if not text:
    return []

  soup = BeautifulSoup(
    text,
    'lxml'
  )

  table_list = soup.find_all('table')
  sanitized_list = []

  for table in table_list:
    sanitized_html = sanitize_html_table(table)
    sanitized_list.append(sanitized_html)

  return sanitized_list

def sanitize_html_table(
  table
) -> str:
  if not table:
    return ""

  td_list = table.find_all('td')

  for td in td_list:
    div = td.find('div')
    has_title = div and div.has_attr('title')

    if not (has_title and not td.get_text(strip = True)):
      continue

    td.clear()
    td.string = div['title'].strip()

  return str(table).replace(
    '\n',
    ''
  )