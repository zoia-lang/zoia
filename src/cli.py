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
"""This module is the main entry point for using Zoia from the command line."""
import sys
import time

import log
from exception import AbstractError
from paths import ZPath
from project import Series

def _print_legal_verbs(*, illegal_verb: str = ''):
    """Helper function for printing all recognized verbs (and optionally
    highlighting an invalid verb provided by the user)."""
    msg = ('Legal verbs are:' if not illegal_verb else
           f"Illegal verb '{illegal_verb}', legal verbs are:")
    print(msg, file=sys.stderr)
    for verb in sorted(_verbs):
        print(f' - {verb}', file=sys.stderr)

def main(args):
    log.init()
    if len(args) < 1:
        print('Usage: zoia <verb>', file=sys.stderr)
        _print_legal_verbs()
        sys.exit(1)
    try:
        verb = _verbs[args[0]]
    except KeyError:
        _print_legal_verbs(illegal_verb=args[0])
        sys.exit(1)
    verb.run(args[1:])

def _log_boot_info():
    """Prints a standard boot message informing the user of what they're using,
    how it's licensed, what version it has"""
    log.info('Zoia - a language for writing fiction.')
    _log_version()
    log.info('Copyright (C) 2021-2022 Infernio')
    log.info('This is free software licensed under the GPLv3. See the LICENSE '
             'file included with this program for more information.')

_zoia_version = '0.1'
def _log_version():
    """Prints the version of this Zoia implementation to the log."""
    log.info(f'Version {_zoia_version}')

class _Verb:
    """Base class for verbs."""
    def run(self, args: list[str]) -> None:
        """Runs this verb on the specified arguments."""
        raise AbstractError(self.run)

class _CommonVerb(_Verb):
    """Base class for verbs that share a simple pattern of behavior: logging
    the standard boot info at startup and printing errors/warnings at exit."""
    def run(self, args: list[str]) -> None:
        _log_boot_info()
        self._run_common(args)
        log.log_stats()

    def _run_common(self, args: list[str]) -> None:
        """Implements the verb-specific behavior (everything besides the
        boot/exit logging)."""
        raise AbstractError(self._run_common)

class _Build(_CommonVerb):
    """Verb that builds a project."""
    def _run_common(self, args: list[str]) -> None:
        log.info(f'Working directory is $fWl${ZPath.cwd()}$R$')
        start_time = time.time()
        Series.parse_series(ZPath.cwd() / 'src')
        duration = time.time() - start_time
        log.info(f'Build took {duration:.1f}s')

class _Version(_Verb):
    """Verb that prints the Zoia version and exits."""
    def run(self, args: list[str]) -> None:
        _log_version()

_verbs = {
    'build': _Build(),
    'version': _Version(),
}

if __name__ == '__main__':
    main(sys.argv[1:])
