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
from antlr4.tree.Tree import ParseTree

from ast_nodes import ZoiaFileNode, LineElementsNode
from ast_validator import ASTValidator
from exception import ParsingError
from grammar import parse, SA_ErrorListener
from parse_converter import ParseConverter
from src_pos import SourcePos

class _RaiseErrorListener(SA_ErrorListener):
    """Error listener that reports parsing errors to our logging framework."""
    __slots__ = ()

    def __init__(self, project_folder: Path = None) -> None:
        self._project_folder = project_folder

    # No point in pylint complaining about this - it's inherited from generated
    # source code, so we can't fix it
    # pylint: disable=arguments-renamed,too-many-arguments
    def syntaxError(self, input_stream: InputStream, offending_symbol: Token,
                    char_index: int, line: int, column: int, msg: str):
        try:
            origin_path = Path(offending_symbol.source[1].fileName)
            if (self._project_folder is not None and
                    origin_path.is_relative_to(self._project_folder)):
                origin_path = origin_path.relative_to(self._project_folder)
            origin_file = str(origin_path)
        except (AttributeError, KeyError, IndexError, TypeError):
            origin_file = '<unknown file>'
        # 'from None' to hide the pointless, messageless error that we're in
        # the middle of handling while this gets called
        raise ParsingError(SourcePos(origin_file, line, column), msg) from None

_validate_ast = ASTValidator().visit

def _process_shared(parse_tree: ParseTree, src_name: str,
                    skip_validation: bool):
    """Shared code of process_zoia_file and process_zoia_string."""
    ret_ast = ParseConverter(src_name).visit(parse_tree)
    if not skip_validation:
        _validate_ast(ret_ast)
    return ret_ast

def process_zoia_file(zoia_path: Path, project_folder: Path, *,
                        skip_validation: bool = False) -> ZoiaFileNode:
    """Parses the Zoia file at the specified path and converts it into a Zoia
    AST. Also performs validation on the resulting AST."""
    origin_path = str(zoia_path)
    # UTF-8 required by specification, so this is fine
    ins = FileStream(origin_path, encoding='utf-8')
    if zoia_path.is_relative_to(project_folder):
        origin_path = str(zoia_path.relative_to(project_folder))
    parse_tree = parse(ins, 'zoiaFile',
                       sa_err_listener=_RaiseErrorListener(project_folder))
    return _process_shared(parse_tree, origin_path, skip_validation)

def process_zoia_string(zoia_src: str, src_name: str, *,
                        skip_validation: bool = False) -> ZoiaFileNode:
    """Parses the specified string representation of a Zoia file and converts
    it into a Zoia AST. src_name specifies the name of the source to use in
    errors etc. Also performs validation on the resulting AST."""
    ins = InputStream(zoia_src)
    parse_tree = parse(ins, 'zoiaFile', sa_err_listener=_RaiseErrorListener())
    return _process_shared(parse_tree, src_name, skip_validation)

def process_zoia_arg(zoia_line: str, src_name: str, *,
                        skip_validation: bool = False) -> LineElementsNode:
    """Parses the specified string representation of a Zoia command argument
    value and converts it into a Zoia AST. src_name specifies the name of the
    source to use in errors etc. Also performs validation on the resulting
    AST."""
    ins = InputStream(zoia_line)
    parse_tree = parse(ins, 'lineElementsArg',
                       sa_err_listener=_RaiseErrorListener())
    return _process_shared(parse_tree, src_name, skip_validation)
