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
"""Implements evaluation of Zoia file of type 'aliases' (also named
'aliases.zoia' by default)."""
import log
from ast_nodes import AASTNode, HeaderNode, LineElementsNode
from ast_visitor import ACommandEvaluator
from exception import EvalError, ValidationError
from validation import HeaderKind

class AliasesEvaluator(ACommandEvaluator):
    r"""Evaluates an aliases file to resolve all \def_alias commands in it and
    return them in the form of an easy to process dict."""
    # Override to add return value type
    def visit(self, tree: AASTNode) -> dict[str, LineElementsNode] | None:
        try:
            super().visit(tree)
        except ValidationError as e:
            # TODO Move this to log - duplicate and doing so will make testing
            #  it easier too
            p = e.src_pos
            log.error(f'Failed to validate $fWl${p.src_file}$fT$ at line '
                      f'$fWl${p.src_line}$fT$, column '
                      f'$fWl${p.src_char + 1}$fT$: $fRl${e.orig_msg}$fT$')
            return None
        return self._state_container.alias_dict

    def _visit_default(self, node: AASTNode):
        raise EvalError(
            node.src_pos,
            f"Unexpected node of type {node.__class__.__name__} in an aliases "
            f"file. Only \\def_alias commands are allowed")

    def visit_header(self, node: HeaderNode):
        header_kind = node.proc_cmd.cmd_args['header_kind']
        if header_kind != HeaderKind.ALIASES:
            raise EvalError(
                node.arguments[0].arg_value.elements[0].src_pos,
                f"Aliases files must have header kind 'aliases', but had "
                f"header kind '{header_kind}' instead")
        pass
