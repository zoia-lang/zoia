# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2022 Infernio
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
import os
import sys
from enum import Enum
from io import StringIO

from colorama import Back, Fore, Style
from colorama.initialise import wrap_stream

# NO LOCAL IMPORTS! This has to be importable from any module/package.

# TODO This module needs to create an output log in build/, where detailed logs
#  go (including debug messages, timestamps, etc.)

# Disable some pylint warnings for this file only:
#  - consider-using-with: We're opening os.devnull, no need to worry about
#    closing it.
#  - global-statement: This is a global logging framework that has to
#    explicitly be initialized via init() call to avoid messing with tests etc.
#  - invalid-name: Those aren't constants, they're global variables. Yeah,
#    spooky.
# pylint: disable=consider-using-with,global-statement,invalid-name

# Discard all output until init() is called
_wrapped_stdout = open(os.devnull, 'w', encoding='utf-8')

def init() -> None:
    """Initializes the logging module. Without this method having been called
    beforehand, all functions in this module will discard their output."""
    global _wrapped_stdout
    _wrapped_stdout = wrap_stream(sys.stdout, autoreset=True, convert=None,
                                  strip=None, wrap=True)

def _colorize_line(line: str) -> str:
    """Parses the specified line for color syntax and replaces it with the
    appropriate escape codes."""
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

def _parse_cmd(cmd: str) -> str:
    """Parses a single command and returns it as an escape code."""
    if len(cmd) == 3:
        if cmd[2] != 'l':
            raise SyntaxError(f"Invalid log command: Last character of "
                              f"three-character command sequence must be an "
                              f"'l', not {cmd[2]}")
        if cmd[1] == 'T':
            raise SyntaxError('Invalid log command: There is no light '
                              'version of the color reset command')
        return _parse_color(cmd[:2], light=True)
    if len(cmd) == 2:
        return _parse_color(cmd)
    elif len(cmd) == 1:
        try:
            return _char_to_style[cmd[0]]
        except KeyError:
            raise SyntaxError(f"Invalid log command: Unknown style code "
                              f"'{cmd[0]}'") from None
    else:
        raise SyntaxError(f'Invalid log command: must have length 1-3, but '
                          f'has length {len(cmd)}')

def _parse_color(color: str, /, *, light: bool = False) -> str:
    """Parses a single color and returns it as an escape code."""
    try:
        target_loc = _char_to_location[color[0]]
    except KeyError:
        raise SyntaxError(f"Invalid log command: Unknown color location "
                          f"'{color[0]}'") from None
    try:
        color_name = _char_to_color[color[1]]
    except KeyError:
        raise SyntaxError(f"Invalid log command: Unknown color code "
                          f"'{color[1]}'") from None
    if light:
        color_name = f'LIGHT{color_name}_EX'
    return getattr(target_loc, color_name)

def arrow(n: int, s: str) -> str:
    """Formats a message with a colorized, leading 'arrow' composed of
    n equal signs (=) and a single greater-than sign (>)."""
    return f'$B${"=" * n}>$R$ {s}'

class _Level(Enum):
    """An enum listing the different levels of severity supported by this
    logging system."""
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

_num_warnings = 0
_num_errors = 0

# FIXME Use the severity argument
# pylint: disable=unused-argument
def _do_log(s: str, /, *, severity: _Level) -> None:
    """The method that actually handles parsing and printing of a single log
    line."""
    print(_colorize_line(s), file=_wrapped_stdout)

def debug(s: str) -> None:
    """Logs a message with severity level of DEBUG. This will not print
    anything to stdout and only print to the log, if that is enabled. Intended
    for debugging messages that an end-user usually doesn't need to see."""
    # TODO see other TODO above
    _do_log(s, severity=_Level.DEBUG)

def info(s: str) -> None:
    """Logs a message with severity level of INFO. The most common usage.
    Intended for normal messages that the end-user should see."""
    _do_log(s, severity=_Level.INFO)

def error(s: str, /, *, count_error: bool = True) -> None:
    """Logs a message with severity level of ERROR. Intended for critical
    problems that prevent the program from completing its task. They will be
    highlighted in red and preceded with a '[!]' marker. The number of
    invocations is also tracked, see log_stats and reset_stats."""
    _do_log(f'$fR$[!] Error:$fT$ {s}', severity=_Level.ERROR)
    if count_error:
        global _num_errors
        _num_errors += 1

def warning(s: str, /, *, count_warning: bool = True) -> None:
    """Logs a message with severity level of WARNING. Intended for problems
    that do not prevent the program from completing its task, but are likely to
    be mistakes or could cause errors later down the line. They will be
    highlighted in orange/yellow and preceded with a '[*]' marker."""
    _do_log(f'$fY$[*] Warning:$fT$ {s}', severity=_Level.WARNING)
    if count_warning:
        global _num_warnings
        _num_warnings += 1

def log_stats() -> None:
    """Prints out error/warning statistics based on the internal error/warning
    counters. See error and warning as well as reset_stats."""
    if _num_warnings == _num_errors == 0:
        info('$fGl$No warnings or errors occurred$R$')
    else:
        warning(f'{_num_warnings} total warning(s)', count_warning=False)
        error(f'{_num_errors} total error(s)', count_error=False)

def reset_stats() -> None:
    """Resets the error and warning counters. See log_stats as well as error
    and warning."""
    global _num_errors, _num_warnings
    _num_errors = 0
    _num_warnings = 0
