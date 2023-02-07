# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2023 Infernio
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
"""This module implements Signature, which handles most of the validation of
command arguments - e.g. checking if all required arguments are filled, that no
standard arguments come after keyword arguments, etc."""
from dataclasses import dataclass, field
from io import StringIO
from typing import Any

from validation.base import _ACmdValidator
from validation.default import Default
from validation.tys import ATy, NoneTy
from validation.varargs import Varargs, VARARGS_EITHER_OR, VARARGS_KWD, \
    VARARGS_STD

from ast_nodes import CommandNode, KwdArgumentNode
from exception import ValidationError, InternalError
from src_pos import SourcePos
from utils import format_word_list

# Sentinel object used to indicate that the next parsed parameter is not a
# regular parameter, but should be appended to the varargs list instead
_VARARGS_SENTINEL = object()

def _raise_if_unfilled(unfilled_params: list[str],
                       cmd_node: CommandNode) -> None:
    """Raises a ValidationError if the specified list of unfilled required
    parameters is not empty. Also handles formatting and the error position."""
    if unfilled_params:
        fmt_unfilled = format_word_list(unfilled_params)
        if cmd_node.arguments:
            # Show marker at the last arg since that's most likely where
            # the missing args have to be inserted
            error_pos = cmd_node.arguments[-1].src_pos
        else:
            # No arguments, but some are expected - show the error at the
            # command node itself
            error_pos = cmd_node.src_pos
        if len(unfilled_params) == 1:
            raise ValidationError(error_pos, f'The required argument '
                                             f'{fmt_unfilled} is missing')
        raise ValidationError(error_pos, f'The required arguments '
                                         f'{fmt_unfilled} are missing')

@dataclass(slots=True, kw_only=True)
class Signature:
    """The Signature class describes a command's signature, specifying what
    parameters it has, which kinds of arguments those parameters accept and
    what types of arguments those parameters accept. It also specifies the
    return type of a command."""
    std_only: dict[str, _ACmdValidator] = field(default_factory=dict)
    either_or: dict[str, _ACmdValidator] = field(default_factory=dict)
    kwd_only: dict[str, _ACmdValidator] = field(default_factory=dict)
    varargs: Varargs | None = None
    ret_ty: ATy = field(default_factory=NoneTy)

    def __post_init__(self) -> None:
        # Once we've found a Default, all later validators must be Defaults too
        found_default = False
        def _check_defaults(cv_dict: dict[str, _ACmdValidator]) -> None:
            nonlocal found_default
            for cv in cv_dict.values():
                if isinstance(cv, Default):
                    found_default = True
                elif found_default:
                    raise SyntaxError('A Signature may not have non-Default '
                                      'validators after a Default validator')
        _check_defaults(self.std_only)
        _check_defaults(self.either_or)
        _check_defaults(self.kwd_only)
        seen_names = set()
        def _check_duplicates(cv_dict: dict[str, _ACmdValidator]) -> None:
            for cv_name in cv_dict:
                if cv_name in seen_names:
                    raise SyntaxError(f"Duplicate parameter name '{cv_name}'")
                seen_names.add(cv_name)
        _check_duplicates(self.std_only)
        _check_duplicates(self.either_or)
        _check_duplicates(self.kwd_only)
        if self.varargs:
            # This is nonsense type-wise, but Python does not have static
            # typing, so we'll have to do it manually...
            if not isinstance(self.varargs, Varargs):
                raise SyntaxError("'varargs' kwarg must have Varargs type")
            # Std-only varargs are only allowed if we have no either-or
            # validators and no kwd-only validators
            if self.varargs.va_kind is VARARGS_STD:
                if self.either_or:
                    raise SyntaxError('Std-only varargs are not allowed when '
                                      'either-or validators are present')
                if self.kwd_only:
                    raise SyntaxError('Std-only varargs are not allowed when '
                                      'kwd-only validators are present')
            # Either-or varargs are only allowed if we have no kwd-only
            # validators
            elif self.varargs.va_kind is VARARGS_EITHER_OR:
                if self.kwd_only:
                    raise SyntaxError('Either-or varargs are not allowed when '
                                      'kwd-only validators are present')

    # Internal API begins here
    def _varargs_accept_standards(self) -> bool:
        """Returns True if this signature has varargs and those varargs could
        accept standard arguments."""
        return self.varargs and self.varargs.va_kind in (VARARGS_STD,
                                                         VARARGS_EITHER_OR)

    def _varargs_accept_keywords(self) -> bool:
        """Returns True if this signature has varargs and those varargs could
        accept keyword arguments."""
        return self.varargs and self.varargs.va_kind in (VARARGS_EITHER_OR,
                                                         VARARGS_KWD)

    def _accepts_standards(self) -> bool:
        """Returns True if this signature could accept standard arguments."""
        return (self.std_only or self.either_or or
                self._varargs_accept_standards())

    def _accepts_keywords(self) -> bool:
        """Returns True if this signature could accept keyword arguments."""
        return (self.either_or or self.kwd_only or
                self._varargs_accept_keywords())

    def _num_std_params(self) -> int:
        """Returns the number of parameters in this signature that could accept
        a standard argument. Raises an internal error if varargs are present
        and could accept standard arguments, since in that case an infinite
        number of standard arguments could be accepted."""
        if self._varargs_accept_standards():
            raise InternalError('_num_std_params may not be called if '
                                'varargs accept standard arguments')
        return len(self.std_only) + len(self.either_or)

    def _num_kwd_params(self) -> int:
        """Returns the number of parameters in this signature that could accept
        a keyword argument. Raises an internal error if varargs are present
        and could accept keyword arguments, since in that case an infinite
        number of keyword arguments could be accepted"""
        if self._varargs_accept_keywords():
            raise InternalError('_num_kwd_params may not be called if '
                                'varargs accept keyword arguments')
        return len(self.either_or) + len(self.kwd_only)

    def _next_std_param(self, filled_params: dict[str]) \
            -> tuple[str | object | None, _ACmdValidator | None]:
        """Given the specified already filled parameters, returns the name and
        validator for the next parameter that can accept a standard argument.
        Returns _VARARGS_SENTINEL if the next parameter is the varargs and None
        if all parameters that can accept standard arguments have been
        filled."""
        for std_n, std_v in self.std_only.items():
            if std_n not in filled_params:
                return std_n, std_v
        for eo_n, eo_v in self.either_or.items():
            if eo_n not in filled_params:
                return eo_n, eo_v
        if self._varargs_accept_standards():
            return _VARARGS_SENTINEL, self.varargs
        # No more std args to fill
        return None, None

    def _next_kwd_param(self, kwd_arg_name: str) \
            -> tuple[str | object | None, _ACmdValidator | None]:
        """Given the specified keyword argument name, returns the name and
        validator for the next parameter that can accept said keyword argument.
        Returns _VARARGS_SENTINEL if the next parameter is the varargs and None
        if all parameters that can accept said keyword argument have been
        filled."""
        kwd_validator = self.either_or.get(kwd_arg_name)
        if kwd_validator is not None:
            return kwd_arg_name, kwd_validator
        kwd_validator = self.kwd_only.get(kwd_arg_name)
        if kwd_validator is not None:
            return kwd_arg_name, kwd_validator
        if self._varargs_accept_keywords():
            return _VARARGS_SENTINEL, self.varargs
        # No more kwd args to fill
        return None, None

    def _fill_defaults(self, filled_params: dict[str],
                       filled_params_pos: dict[str, SourcePos | None]) \
            -> list[str]:
        """Fills the specified parameters and parameter positions with default
        values for all optional parameters and returns a list of parameter
        names for all unfilled required parameters."""
        unfilled_params = []
        def _fill_from_dict(cv_dict: dict[str, _ACmdValidator]) -> None:
            for cv_n, cv_v in cv_dict.items():
                if cv_n not in filled_params:
                    if isinstance(cv_v, Default):
                        filled_params[cv_n] = cv_v.default
                        # No source position since it was a default argument
                        filled_params_pos[cv_n] = None
                    else:
                        unfilled_params.append(cv_n)
        _fill_from_dict(self.std_only)
        _fill_from_dict(self.either_or)
        _fill_from_dict(self.kwd_only)
        return unfilled_params

    # Public API begins here
    def compact(self) -> str:
        """Returns the compact signature representation of this signature as a
        string."""
        s = StringIO()
        if (not self.std_only and not self.either_or and not self.kwd_only and
                not self.varargs):
            s.write('|')
        else:
            s.write('[\n')
            for std_v_n, std_v_t in self.std_only.items():
                s.write(f'    ~ {std_v_n}: {std_v_t.compact()};\n')
            for eo_v_n, eo_v_t in self.either_or.items():
                s.write(f'    {eo_v_n}: {eo_v_t.compact()};\n')
            for kwd_v_n, kwd_v_t in self.kwd_only.items():
                s.write(f'    $ {kwd_v_n}: {kwd_v_t.compact()};\n')
            if self.varargs:
                s.write(f'    {self.varargs.compact()};\n')
            s.write(']')
        s.write(f' -> {self.ret_ty.compact()}')
        return s.getvalue()

    def init_default_values(self) -> None:
        """Initializes this signature's default values by parsing their string
        representations. Called by finalize_command once all command modules
        have been imported and all command signatures have been created."""
        def _init_defaults(cv_dict: dict[str, _ACmdValidator]) -> None:
            for cv_v in cv_dict.values():
                if isinstance(cv_v, Default):
                    cv_v.init_default_value()
        _init_defaults(self.std_only)
        _init_defaults(self.either_or)
        _init_defaults(self.kwd_only)

    def validate_args(self, cmd_node: CommandNode) \
            -> tuple[dict[str, Any], dict[str, SourcePos | None],
                     list[Any], list[SourcePos]]:
        """Given a CommandNode, processes and validates all its arguments and
        returns them in a tuple containing a dict mapping command names to
        their processed values, a dict mapping command names to their origin
        source positions (or None if it was a default value), a list of
        processed varargs values and a list of varargs source positions."""
        filled_params = {}
        filled_params_pos = {}
        varargs_list = []
        varargs_list_pos = []
        found_kwd = False
        accepts_std = self._accepts_standards()
        accepts_kwd = self._accepts_keywords()
        for cmd_arg in cmd_node.arguments:
            # First extract the next parameter name and validator, which
            # differs between standard and keyword arguments
            if isinstance(cmd_arg, KwdArgumentNode):
                if not accepts_kwd:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        f'\\{cmd_node.cmd_name} does not accept keyword '
                        f'arguments')
                # Once we've found a keyword argument, reject all further
                # standard arguments
                found_kwd = True
                kwd_arg_name = cmd_arg.kwd_name
                if kwd_arg_name in filled_params:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        f"Keyword argument '{kwd_arg_name}' specified twice")
                next_param_name, next_validator = self._next_kwd_param(
                    kwd_arg_name)
                if next_param_name is None:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        f'All {self._num_kwd_params()} parameters that accept '
                        f'keyword arguments have been filled')
            else:
                if not accepts_std:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        f'\\{cmd_node.cmd_name} does not accept standard '
                        f'arguments')
                if found_kwd:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        'Standard arguments may not be placed after keyword '
                        'arguments')
                next_param_name, next_validator = self._next_std_param(
                    filled_params)
                if next_param_name is None:
                    raise ValidationError(
                        cmd_arg.src_pos,
                        f'All {self._num_std_params()} parameters that accept '
                        f'standard arguments have been filled')
            # We have a name and a validator for the next parameter, so process
            # and store, making sure to check if we're going to store to
            # varargs instead of regular parameters
            processed_arg = next_validator.validate_arg(cmd_arg.arg_value)
            if next_param_name is _VARARGS_SENTINEL:
                varargs_list.append(processed_arg)
                varargs_list_pos.append(cmd_arg.src_pos)
            else:
                filled_params[next_param_name] = processed_arg
                filled_params_pos[next_param_name] = cmd_arg.src_pos
        # All arguments processed, fill optional parameters with defaults and
        # raise an error if required arguments are missing
        unfilled_params = self._fill_defaults(filled_params, filled_params_pos)
        _raise_if_unfilled(unfilled_params, cmd_node)
        return filled_params, filled_params_pos, varargs_list, varargs_list_pos

    def __repr__(self) -> str:
        return self.compact()
