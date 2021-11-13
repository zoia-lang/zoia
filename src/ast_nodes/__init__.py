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
"""This module implements the classes from which the Zoia AST is built. All
imports should come directly from here - *never* import from the actual files
that define the classes. That way they can be moved around easily."""
from .alias import *
from .argument import *
from .base import *
from .command import *
from .header import *
from .kwd_argument import *
from .line import *
from .line_element import *
from .std_argument import *
from .text_fragment import *
from .zoia_file import *

# TODO str -> WordNode? Or is that overkill?
