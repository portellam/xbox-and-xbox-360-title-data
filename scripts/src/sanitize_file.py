#!/usr/bin/env python

#
# Filename:       sanitize_file.py
# Description:    Sanitizes file name for OS compatibility.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
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