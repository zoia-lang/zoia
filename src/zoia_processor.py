# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021 Infernio
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

from antlr4 import CommonTokenStream, FileStream

from ast_converter import ASTConverter
from grammar import zoiaLexer, zoiaParser
from paths import ZPath

def process_zoia_file(zoia_path: ZPath):
    """Parses the Zoia file at the specified path and converts it into a Zoia
    AST."""
    # UTF-8 required by specification, so this is fine
    ins = FileStream(zoia_path, encoding='utf-8')
    lexer = zoiaLexer(ins)
    parser = zoiaParser(CommonTokenStream(lexer))
    parse_tree = parser.zoiaFile()
    return ASTConverter(ins.fileName).visit(parse_tree)
