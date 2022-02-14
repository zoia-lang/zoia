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
"""Implements the classes for parsing the zoia.toml config file."""
import inspect
import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Type, Any

import tomli

import log
from exception import AbstractError
from utils import ps_error

# Internal API begins here
class _AOption:
    """Base class for all options. See its subclasses like _ASrcPathOption for
    more information."""
    option_name: str
    option_value: Any
    option_default: Any
    __slots__ = ('option_name', 'option_value',)

    def __init__(self, opt_name: str, opt_value: Any):
        self.option_name = opt_name
        self.option_value = opt_value

    @classmethod
    def parse_option(cls, option_value: Any, option_name: str,
                     project_folder: Path, /, *, raise_errors: bool):
        """Parses an option with the specified value and name into an
        _AOption-derived instance."""
        # If the option is missing from the config file, use the default
        if option_value is None:
            option_value = cls.option_default
        return cls._do_parse_option(option_value, option_name, project_folder,
                                    raise_errors=raise_errors)

    @classmethod
    def _do_parse_option(cls, option_value: Any, option_name: str,
                         project_folder: Path, /, *, raise_errors: bool):
        """The actual abstract method that does the parsing. This is what you
        have to override to create a new type of option."""
        raise AbstractError(cls.parse_option)

    def __repr__(self):
        return f"Option<{self.option_name} = '{self.option_value}'>"

# TODO Do we need src path options separate from Zoia path options?
class _ASrcPathOption(_AOption):
    """Base class for src path options. A path, specified relative to the 'src'
    folder. Must be entirely lowercase and must exist.

    Do not use this directly. Instead, use the _src_path_option API and pass a
    default value."""
    option_value: Path
    __slots__ = ()

    @classmethod
    def _do_parse_option(cls, option_value: str | None, option_name: str,
                         project_folder: Path, /, *, raise_errors: bool):
        # Slashes or backslashes may be used for paths in the config
        option_value = option_value.replace(
            '\\', os.path.sep).replace('/', os.path.sep)
        # This is a src-relative path, which must be lowercased
        if option_value.lower() != option_value:
            return ps_error(f"Failed to parse option '{option_name}': "
                            f"'{option_value}' is not lowercased",
                            Path('zoia.toml'), raise_errors)
        # Check if the path actually exists
        rel_path = Path('src') / option_value
        final_path = project_folder / rel_path
        try:
            final_path = final_path.resolve(strict=True)
        except FileNotFoundError as e:
            return ps_error(f"Failed to parse option '{option_name}': "
                            f"Specified path '{option_value}' does not exist "
                            f"(resolved to '{rel_path}')",
                            Path('zoia.toml'), raise_errors, orig_error=e)
        return cls(option_name, final_path)

# def _src_path_option(default: str, /): # TODO unused, see above
#     """Internal method for defining a src path option. Pass it a default
#     value to get an appropriate class for the annotation back."""
#     class _SrcPathOption(_ASrcPathOption):
#         """Internal class that holds an appropriate default value for a src
#         path option."""
#         option_default: str = default
#         __slots__ = ()
#     return _SrcPathOption

class _AZoiaPathOption(_ASrcPathOption):
    """Base class for Zoia path options. Similar to _ASrcPathOption, but must
    end in .zoia.

    Do not use this directly. Instead, use the _zoia_path_option API and pass a
    default value."""
    @classmethod
    def _do_parse_option(cls, option_value: str | None, option_name: str,
                         project_folder: Path, /, *, raise_errors: bool):
        # lower() because the check for lowercasing is done in _ASrcPathOption
        if not option_value.lower().endswith('.zoia'):
            return ps_error(f"Failed to parse option '{option_name}': "
                            f"Specified path '{option_value}' does not end in "
                            f"'.zoia'", Path('zoia.toml'), raise_errors)
        return super()._do_parse_option(
            option_value, option_name, project_folder,
            raise_errors=raise_errors)

def _zoia_path_option(default: str, /):
    """Internal method for defining a Zoia path option. Pass it a default value
    to get an appropriate class for the annotation back."""
    class _ZoiaPathOption(_AZoiaPathOption):
        """Internal class that holds an appropriate default value for a Zoia
        path option."""
        option_default: str = default
        __slots__ = ()
    return _ZoiaPathOption

@dataclass(slots=True)
class _ASection:
    """Base class for defining sections. Derive from this class, make yourself
    a dataclass and define options via annotations using the _*_option family
    of methods."""
    @classmethod
    def parse_section(cls, section_contents: defaultdict[str, Any],
                      section_name: str, project_folder: Path, /, *,
                      raise_errors: bool):
        """Parses a section with the specified contents and name."""
        section_ann: dict[str, Type[_AOption]] = inspect.get_annotations(cls)
        init_params = {}
        any_failed = False
        for option_name, option_type in section_ann.items():
            option_value = section_contents[option_name]
            # We're done with this option, mark it as removed
            del section_contents[option_name]
            option_inst = option_type.parse_option(
                option_value, option_name, project_folder,
                raise_errors=raise_errors)
            if option_inst is None:
                any_failed = True
            init_params[option_name] = option_inst
        if any_failed:
            # This is just a cascading effect of a real error
            log.warning(f'Failed to parse section $fWl${section_name}$R$ due '
                        f'to errors when parsing one or more options')
            return None
        # Warn if any unknown options are left in the section
        for unk_option in section_contents:
            log.warning(f'Unknown option $fWl${unk_option}$R$ found in '
                        f'section $fWl${section_name}$R$')
        # For some reason PyCharm bugs out here and thinks this initializer
        # doesn't take any arguments - probably similar to the bug in
        # parse_converter, see there for more info
        # noinspection PyArgumentList
        return cls(**init_params)

# Public API begins here
@dataclass(slots=True)
class SectionAliases(_ASection):
    """Represents the 'aliases' section."""
    src_path: _zoia_path_option('aliases.zoia')

@dataclass(slots=True)
class SectionDict(_ASection):
    """Represents the 'dictionary' section."""
    src_path: _zoia_path_option('dictionary.zoia')

@dataclass(slots=True)
class ZoiaToml:
    """Provides an API for parsing and accessing the contents of the zoia.toml
    config file in a strongly typed way. Every section in the file is a field
    on this class, defined using annotations."""
    aliases: SectionAliases
    dictionary: SectionDict

    @classmethod
    def parse_zoia_toml(cls, toml_path: Path, project_folder: Path, /, *,
                        raise_errors: bool):
        """Parses a zoia.toml file at the specified path. Returns None if
        parsing failed."""
        toml_rel = toml_path.relative_to(project_folder)
        config_ann: dict[str, Type[_ASection]] = inspect.get_annotations(cls)
        try:
            with toml_path.open('rb') as ins:
                parsed_toml = tomli.load(ins)
            log.info(log.arrow(1, f'Parsing config at $fCl${toml_rel}$R$'))
        except FileNotFoundError:
            # Load the default config by behaving as if the file existed and
            # was empty
            parsed_toml = {}
            log.info(log.arrow(1, f'No config found at $fCl${toml_rel}$R$, '
                                  f'using default values'))
        except tomli.TOMLDecodeError as e:
            # The config file has broken TOML syntax, wrap and re-raise error
            return ps_error(f'Invalid TOML syntax: {str(e)}', toml_rel,
                            raise_errors, orig_error=e)
        # Default section contents are an empty dict
        config_contents = defaultdict(dict, parsed_toml.copy())
        init_params = {}
        any_failed = False
        for section_name, section_type in config_ann.items():
            section_contents = defaultdict(
                lambda: None, config_contents[section_name].copy())
            # We're done with this section, mark it as removed
            del config_contents[section_name]
            section_inst = section_type.parse_section(
                section_contents, section_name, project_folder,
                raise_errors=raise_errors)
            if section_inst is None:
                any_failed = True
            init_params[section_name] = section_inst
        if any_failed:
            # This is just a cascading effect of a real error
            log.warning(f'Failed to parse $fCl${toml_rel}$R$ due to errors '
                        f'when parsing one or more sections')
            return None
        # Warn if any unknown sections are left in the config
        for unk_section in config_contents:
            log.warning(f'Unknown section $fWl${unk_section}$R$ found in '
                        f'$fCl${toml_rel}$R$')
        return cls(**init_params)
