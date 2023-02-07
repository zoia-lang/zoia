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
"""This package performs validation of command signatures, guarding against
syntax errors, type errors and other mistakes.

Quick notes on terminology:
 - The implementations in the code are internally called 'validators'.
 - When interfacing with a user, validators refer to themselves as
   'parameters', since that's how users will interact with them. Every
   validator validates one (or more, for varargs) parameter on a command.
 - An 'argument' is the same as a parameter, but from the perspective of the
   Zoia code passing said argument.
 - A 'value' is what Zoia code actually passes to a command's parameter. It's
   the object that a validator interacts with."""
from validation.default import *
from validation.tys import *
from validation.signature import *
from validation.varargs import *
