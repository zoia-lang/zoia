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
"""This module is the main entry point for using Zoia from the command line."""
import sys
from antlr4 import CommonTokenStream, FileStream

from grammar import zoiaLexer, zoiaParser
from ast_converter import ASTConverter

def main(args):
    ins = FileStream('tmp_test/test.zoia', encoding='utf-8')
    lexer = zoiaLexer(ins)
    tokens = CommonTokenStream(lexer)
    parser = zoiaParser(tokens)
    tree = parser.zoiaFile()
    ast = ASTConverter().visit(tree)
    print(ast.canonical())

if __name__ == '__main__':
    main(sys.argv[1:])
