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
from ast_nodes import AASTNode, ZoiaFileNode, HeaderNode, LineNode, \
    LineElementsNode, CommandNode, TextFragmentNode
from ast_visitor import AASTVisitor
from cmd_validation import Signature, WordTy, ContentTy
from exception import EvalError, ValidationError
from src_pos import SourcePos

_def_alias_sig = Signature(
    std_only={
        'key': WordTy(),
        'val': ContentTy(),
    },
)

class AliasesEvaluator(AASTVisitor):
    r"""Evaluates an aliases file to resolve all \def_alias commands in it and
    return them in the form of an easy to process dict."""
    # Override to add return value type
    def visit(self, tree: AASTNode) -> dict[str, LineElementsNode] | None:
        # pylint: disable=useless-super-delegation
        try:
            return super().visit(tree)
        except ValidationError as e:
            # TODO Move this to log - duplicate and doing so will make testing
            #  it easier too
            p = e.src_pos
            log.error(f'Failed to validate $fWl${p.src_file}$fT$ at line '
                      f'$fWl${p.src_line}$fT$, column $fWl${p.src_char}$fT$: '
                      f'$fRl${e.orig_msg}$fT$')
            return None

    def _visit_default(self, node: AASTNode):
        raise EvalError(
            node.src_pos,
            f"Unexpected node of type {node.__class__.__name__} in an aliases "
            f"file. Only \\def_alias commands are allowed")

    def visit_zoia_file(self, node: ZoiaFileNode) \
            -> dict[str, LineElementsNode]:
        self.visit_header(node.header)
        final_aliases = []
        extend_aliases = final_aliases.extend
        visit_ln = self.visit_line
        for l in node.lines:
            extend_aliases(visit_ln(l))
        ret_dict = {}
        seen_alias_keys = set()
        add_alias_key = seen_alias_keys.add
        for alias_key_tup, alias_val_tup in final_aliases:
            alias_key = alias_key_tup[0]
            if alias_key in seen_alias_keys:
                raise EvalError(alias_key_tup[1], f"Duplicate alias key "
                                                  f"'{alias_key}'")
            else:
                add_alias_key(alias_key)
                ret_dict[alias_key] = alias_val_tup[0]
        return ret_dict

    def visit_header(self, node: HeaderNode):
        if node.header_type != 'aliases':
            raise EvalError(
                node.arguments[0].arg_value.elements[0].src_pos,
                f"Aliases files must have header type 'aliases', but had "
                f"header type '{node.header_type}' instead")

    def visit_line(self, node: LineNode) \
            -> list[tuple[TextFragmentNode, LineElementsNode]]:
        if n_elements := node.elements:
            return self.visit_line_elements(n_elements)
        return []

    def visit_line_elements(self, node: LineElementsNode) \
            -> list[tuple[TextFragmentNode, LineElementsNode]]:
        ret_aliases = []
        append_alias = ret_aliases.append
        visit_cmd = self.visit_command
        for line_el in node.elements:
            if isinstance(line_el, CommandNode):
                append_alias(visit_cmd(line_el))
            else:
                # Only \def_alias commands are OK, raise an error
                self._visit_default(line_el)
        return ret_aliases

    def visit_command(self, node: CommandNode) \
            -> tuple[tuple[str, SourcePos],
                     tuple[LineElementsNode, SourcePos]]:
        if node.cmd_name != 'def_alias':
            raise EvalError(
                node.src_pos,
                f"Unexpected '\\{node.cmd_name}' command in an aliases file. "
                f"Only \\def_alias commands are allowed")
        proc_args = _def_alias_sig.process_args(node.arguments)[0]
        return proc_args['key'], proc_args['val']
