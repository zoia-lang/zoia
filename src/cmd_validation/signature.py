from dataclasses import dataclass, field
from io import StringIO
from typing import Any

from cmd_validation.base import CmdValidator
from cmd_validation.tys import Ty, NoneTy
from cmd_validation.varargs import Varargs, VARARGS_EITHER_OR, VARARGS_KWD, \
    VARARGS_STD

from ast_nodes import AArgumentNode, KwdArgumentNode
from exception import ValidationError
from src_pos import SourcePos

_varargs_sentinel = object()

@dataclass(slots=True)
class Signature:
    std_only: dict[str, CmdValidator] = field(default_factory=dict)
    either_or: dict[str, CmdValidator] = field(default_factory=dict)
    kwd_only: dict[str, CmdValidator] = field(default_factory=dict)
    varargs: Varargs = None
    ret_ty: Ty = NoneTy()

    def __post_init__(self):
        # Once we've found a Default, all later validators must be Defaults too
        found_default = False
        def _check_defaults(cv_dict: dict[str, CmdValidator]):
            nonlocal found_default
            for cv in cv_dict.values():
                if cv.has_default:
                    found_default = True
                elif found_default:
                    raise SyntaxError('A Signature may not have non-Default '
                                      'validators after a Default validator')
        _check_defaults(self.std_only)
        _check_defaults(self.either_or)
        _check_defaults(self.kwd_only)
        seen_names = set()
        add_seen_name = seen_names.add
        def _check_duplicates(cv_dict: dict[str, CmdValidator]):
            for cv_name in cv_dict:
                if cv_name in seen_names:
                    raise SyntaxError(f"Duplicate parameter name '{cv_name}'")
                add_seen_name(cv_name)
        _check_duplicates(self.std_only)
        if self.varargs:
            # std-only varargs are only allowed if we have no either-or
            # validators and no kwd-only validators
            if self.varargs.va_type is VARARGS_STD:
                if self.either_or:
                    raise SyntaxError('Std-only varargs are not allowed when '
                                      'either-or validators are present')
                if self.kwd_only:
                    raise SyntaxError('Std-only varargs are not allowed when '
                                      'kwd-only validators are present')
            # either-or varargs are only allowed if we have no kwd-only
            # validators
            elif self.varargs.va_type is VARARGS_EITHER_OR:
                if self.kwd_only:
                    raise SyntaxError('Either-or varargs are not allowed when '
                                      'kwd-only validators are present')

    def _varargs_accept_standards(self):
        return self.varargs and self.varargs.va_type in (VARARGS_STD,
                                                         VARARGS_EITHER_OR)

    def _varargs_accept_keywords(self):
        return self.varargs and self.varargs.va_type in (VARARGS_EITHER_OR,
                                                         VARARGS_KWD)

    def _accepts_standards(self):
        return (self.std_only or self.either_or or
                self._varargs_accept_standards())

    def _accepts_keywords(self):
        if self.either_or or self.kwd_only:
            return True
        return

    def _num_std_params(self):
        if self._varargs_accept_standards():
            return -1 # Infinite
        return len(self.std_only) + len(self.either_or)

    def _num_kwd_params(self):
        if self._varargs_accept_keywords():
            return -1 # Infinite
        return len(self.either_or) + len(self.kwd_only)

    def _next_std_param(self, filled_args: dict[str]) \
            -> tuple[str | object | None, CmdValidator | None]:
        for std_n, std_v in self.std_only.items():
            if std_n not in filled_args:
                return std_n, std_v
        for eo_n, eo_v in self.either_or.items():
            if eo_n not in filled_args:
                return eo_n, eo_v
        if self.varargs and self.varargs.va_type in (VARARGS_STD,
                                                     VARARGS_EITHER_OR):
            return _varargs_sentinel, self.varargs
        # No more std args to fill
        return None, None

    def _next_kwd_param(self, cmd_name: str) \
            -> tuple[str | object | None, CmdValidator | None]:
        kwd_validator = self.either_or.get(cmd_name)
        if kwd_validator is not None:
            return cmd_name, kwd_validator
        kwd_validator = self.kwd_only.get(cmd_name)
        if kwd_validator is not None:
            return cmd_name, kwd_validator
        if self.varargs and self.varargs.va_type in (VARARGS_EITHER_OR,
                                                     VARARGS_KWD):
            return _varargs_sentinel, self.varargs
        # No more kwd args to fill
        return None, None

    def process_args(self, cmd_args: list[AArgumentNode]) \
            -> tuple[dict[str, tuple[Any, SourcePos]],
                     list[tuple[Any, SourcePos]]]:
        filled_args = {}
        varargs_list = []
        append_vararg = varargs_list.append
        found_kwd = False
        next_sp = self._next_std_param
        next_kp = self._next_kwd_param
        accepts_std = self._accepts_standards()
        accepts_kwd = self._accepts_keywords()
        for cmd_arg in cmd_args:
            arg_src_pos = cmd_arg.src_pos
            if isinstance(cmd_arg, KwdArgumentNode):
                if not accepts_kwd:
                    raise ValidationError(
                        arg_src_pos,
                        'This command does not accept keyword arguments')
                found_kwd = True
                cmd_name = cmd_arg.kwd_name
                if cmd_name in filled_args:
                    raise ValidationError(
                        arg_src_pos,
                        f"Keyword argument '{cmd_name}' specified twice")
                next_param_name, next_validator = next_kp(cmd_name)
                if next_param_name is None:
                    raise ValidationError(
                        arg_src_pos,
                        f'All {self._num_kwd_params()} parameters that accept '
                        f'keyword arguments have been filled')
            else:
                if not accepts_std:
                    raise ValidationError(
                        arg_src_pos,
                        'This command does not accept standard arguments')
                if found_kwd:
                    raise ValidationError(
                        arg_src_pos,
                        'Standard arguments may not be placed after keyword '
                        'arguments')
                next_param_name, next_validator = next_sp(filled_args)
                if next_param_name is None:
                    raise ValidationError(
                        arg_src_pos,
                        f'All {self._num_std_params()} parameters that accept '
                        f'standard arguments have been filled')
            processed_arg = next_validator.process_arg(cmd_arg)
            if next_param_name is _varargs_sentinel:
                append_vararg((processed_arg, arg_src_pos))
            else:
                filled_args[next_param_name] = (processed_arg, arg_src_pos)
        # TODO Check unfilled args and fill with defaults if not validate_only
        return filled_args, varargs_list

    def compact(self) -> str:
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

    def __repr__(self):
        return self.compact()
