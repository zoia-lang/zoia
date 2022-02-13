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
"""High-level interface for parsing a Zoia file and converting it into an
AST."""

from pathlib import Path

from antlr4 import FileStream, InputStream, Token

from parse_converter import ParseConverter
from ast_nodes import ZoiaFileNode
from exception import ParsingError
from grammar import parse, SA_ErrorListener
from src_pos import SourcePos

class _RaiseErrorListener(SA_ErrorListener):
    # No point in pylint complaining about this - it's inherited from generated
    # source code, so we can't fix it
    # pylint: disable=arguments-renamed,too-many-arguments
    def syntaxError(self, input_stream: InputStream, offending_symbol: Token,
                    char_index: int, line: int, column: int, msg: str):
        try:
            origin_file = offending_symbol.source[1].fileName
        except (AttributeError, KeyError, TypeError):
            origin_file = '<unknown file>'
        # 'from None' to hide the pointless, messageless error that we're in
        # the middle of handling while this gets called
        raise ParsingError(SourcePos(origin_file, line, column), msg) from None

_REL_INSTANCE = _RaiseErrorListener()

def process_zoia_file(zoia_path: Path) -> ZoiaFileNode:
    """Parses the Zoia file at the specified path and converts it into a Zoia
    AST."""
    # UTF-8 required by specification, so this is fine
    ins = FileStream(str(zoia_path), encoding='utf-8')
    parse_tree = parse(ins, 'zoiaFile', sa_err_listener=_REL_INSTANCE)
    return ParseConverter(ins.fileName).visit(parse_tree)

def process_zoia_string(zoia_src: str, src_name: str) -> ZoiaFileNode:
    """Parses the specified string representation of a Zoia file and converts
    it into a Zoia AST. src_name specifies the name of the source to use in
    errors etc."""
    ins = InputStream(zoia_src)
    parse_tree = parse(ins, 'zoiaFile', sa_err_listener=_REL_INSTANCE)
    return ParseConverter(src_name).visit(parse_tree)
