# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021 Infernio
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
"""Implements a simple logging/output system. It works like a simple print
statement, except that it can also colorize output. You do that by using dollar
signs around 'commands'. There are two types of commands: styles and colors.

A style command is one character long. It may be one of the following values:

 - B: bright style
 - D: dim style
 - N: normal style
 - R: reset color and style

A color command is either two or three characters long. In the former case, the
first character is either 'f' or 'b', indicating foreground color or background
color, respectively. The second character specifies the color to use:

 - D: black ('dark', chosen since blue is much more common)
 - R: red
 - G: green
 - Y: yellow
 - B: blue
 - M: magenta
 - C: cyan
 - W: white
 - T: reset color (chosen since red is much more common)

In the latter case, the third letter must be an 'l'. It indicates that the
color is to be chosen as a 'light' color by the terminal. The other two
characters are processed the same way as in the two-character case.
"""
import sys

from colorama import Back, Fore, Style
from colorama.initialise import wrap_stream
from io import StringIO

# TODO This module needs to create an output log in build/, where detailed logs
#  go (including debug messages, timestamps, etc.)

wrapped_stdout = sys.stdout

def init():
    global wrapped_stdout
    wrapped_stdout = wrap_stream(sys.stdout, autoreset=True, convert=None,
                                 strip=None, wrap=True)

def _colorize_line(line: str):
    wip_line = StringIO()
    for i, part in enumerate(line.split('$')):
        # Every second element is a color command
        if i % 2 == 1:
            wip_line.write(_parse_cmd(part))
        else:
            wip_line.write(part)
    return wip_line.getvalue()

_char_to_location = {
    'b': Back,
    'f': Fore,
}
_char_to_color = {
    'D': 'BLACK',
    'R': 'RED',
    'G': 'GREEN',
    'Y': 'YELLOW',
    'B': 'BLUE',
    'M': 'MAGENTA',
    'C': 'CYAN',
    'W': 'WHITE',
    'T': 'RESET',
}
_char_to_style = {
    'B': Style.BRIGHT,
    'D': Style.DIM,
    'N': Style.NORMAL,
    'R': Style.RESET_ALL,
}
def _parse_cmd(cmd: str):
    if len(cmd) == 3:
        if cmd[2] != 'l':
            raise SyntaxError(f"Invalid log command: Last character of "
                              f"three-character command sequence must be an "
                              f"'l'")
        if cmd[1] == 'T':
            raise SyntaxError(f'Invalid log command: There is no light '
                              f'version of the color reset command')
        return _parse_color(cmd[:2], light=True)
    if len(cmd) == 2:
        return _parse_color(cmd)
    elif len(cmd) == 1:
        try:
            return _char_to_style[cmd[0]]
        except KeyError:
            raise SyntaxError(f"Invalid log command: Unknown style code "
                              f"'{cmd[0]}'")
    else:
        raise SyntaxError(f'Invalid log command: must have length 1-3, but '
                          f'has length {len(cmd)}')

def _parse_color(color: str, light: bool = False):
    try:
        target_loc = _char_to_location[color[0]]
    except KeyError:
        raise SyntaxError(f"Invalid log command: Unknown color location "
                          f"'{color[0]}'")
    try:
        color_name = _char_to_color[color[1]]
    except KeyError:
        raise SyntaxError(f"Invalid log command: Unknown color code "
                          f"'{color[1]}'")
    if light:
        color_name = f'LIGHT{color_name}_EX'
    return getattr(target_loc, color_name)

def info(s):
    print(_colorize_line(s), file=wrapped_stdout)

def debug(s):
    # see TODO above
    info(s)
