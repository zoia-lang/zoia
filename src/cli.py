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
from pathlib import Path

import build_supervisor
import log
from exception import AbstractError
from project import Project

def _print_legal_verbs(*, illegal_verb: str = ''):
    """Helper function for printing all recognized verbs (and optionally
    highlighting an invalid verb provided by the user)."""
    msg = ('Legal verbs are:' if not illegal_verb else
           f"Illegal verb '{illegal_verb}', legal verbs are:")
    print(msg, file=sys.stderr)
    for verb in sorted(_verbs):
        print(f' - {verb}', file=sys.stderr)

def main(args):
    """The main method. Starts the Zoia CLI."""
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
    log.info('This is free software licensed under the GPLv3.')
    log.info('See the LICENSE file included with this program for more '
             'information.')
    log.info('')

_ZOIA_VERSION = '0.1'
def _log_version():
    """Prints the version of this Zoia implementation to the log."""
    log.info(f'Version {_ZOIA_VERSION}')

class _Verb:
    """Base class for verbs."""
    def run(self, args: list[str]) -> None:
        """Runs this verb on the specified arguments."""
        raise AbstractError()

class _CommonVerb(_Verb):
    """Base class for verbs that share a pattern of behavior: logging the
    standard boot info at startup and printing errors/warnings at exit."""
    def run(self, args: list[str]) -> None:
        _log_boot_info()
        self._run_common(args)
        log.log_stats()

    def _run_common(self, args: list[str]) -> None:
        """Implements the verb-specific behavior (everything besides the
        boot/exit logging)."""
        raise AbstractError()

class _ProjectVerb(_CommonVerb):
    """Base class for common verbs that share an additional pattern of
    behavior: parsing a project from the first argument or CWD, while keeping
    track of time elapsed."""
    _time_msg: str

    def _run_common(self, args: list[str]) -> None:
        start_time = time.time()
        match len(args):
            case 0:
                final_path = Path.cwd()
            case 1:
                final_path = Path(args[0])
            case _:
                print('Usage: zoia build [path]', file=sys.stderr)
                sys.exit(1)
        project = Project.parse_project(final_path)
        if project is not None:
            self._run_on_project(project)
        else:
            log.warning('Aborting build due to errors while parsing project')
        duration = time.time() - start_time
        log.info(self._time_msg % f'{duration:.1f}')

    def _run_on_project(self, project: Project) -> None:
        """Implements the verb-specific behavior using the project."""
        raise AbstractError()

class _Build(_ProjectVerb):
    """Verb that builds a project."""
    _time_msg = 'Build took %ss'

    def _run_on_project(self, project: Project) -> None:
        build_supervisor.build(project)

class _Check(_ProjectVerb):
    """Verb that checks a project for spelling, grammar, style, etc.
    errors."""
    _time_msg = 'Check took %ss'

    def _run_on_project(self, project: Path) -> None:
        pass # TODO implement checking

class _Version(_Verb):
    """Verb that prints the Zoia version and exits."""
    def run(self, args: list[str]) -> None:
        _log_version()

_verbs = {
    'build': _Build(),
    'check': _Check(),
    'version': _Version(),
}

if __name__ == '__main__':
    main(sys.argv[1:])
