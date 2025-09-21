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
# Filename:       sanitize_html.py
# Description:    Sanitizes HTML and can parse HTML with multiple tables.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
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