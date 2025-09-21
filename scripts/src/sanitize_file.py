#!/usr/bin/env python

#
# Copyright (C) 2025 Alex Portell <github.com/portellam>
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
# Filename:       sanitize_file.py
# Description:    Sanitizes file name for OS compatibility.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
# License:        GNU General Public License v3.0
# Version:        1.0.0
#

import re
import sys

def sanitize_file_name(
  file_name: str
) -> str:
  if not file_name:
    print("File name is empty.")
    raise TypeError

  control_char_regex = r'[\x00-\x1F\x7F]+'
  illegal_char_list_regex = r'[<>:"/\\|?*\0]+'
  prefix_suffix_period_regex = r'^\.+|\.+$'
  whitespace_regex = r'\s+'

  unix_reserved_name_list = [
    ".",
    ".."
  ]

  windows_reserved_name_list = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
  ]

  sanitized_file_name = file_name.strip()

  if sanitized_file_name.upper() in unix_reserved_name_list:
    sanitized_file_name = f"{sanitized_file_name}_sanitized"

  if sanitized_file_name.upper() in windows_reserved_name_list:
    sanitized_file_name = f"{sanitized_file_name}_sanitized"

  sanitized_file_name = re.sub(
    whitespace_regex,
    '_',
    sanitized_file_name
  )

  sanitized_file_name = re.sub(
    illegal_char_list_regex,
    '_',
    sanitized_file_name
  )

  sanitized_file_name = re.sub(
    control_char_regex,
    '',
    sanitized_file_name
  )

  sanitized_file_name = re.sub(
    prefix_suffix_period_regex,
    '',
    sanitized_file_name
  )

  if not sanitized_file_name:
    print("Sanitized file name is empty.")
    raise Exception

  return sanitized_file_name