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
from commands._base import _ACommand

from validation import Signature, HeaderKindTy, AnyTy, Varargs, \
    VARARGS_EITHER_OR

class HeaderCmd(_ACommand):
    cmd_name = 'header'
    signature = Signature(
        std_only={
            'header_kind': HeaderKindTy(),
        },
        # TODO Do we have a use case for >1 argument passed to the header? If
        #  not, drop the varargs
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    __slots__ = ()

CMD_TYPE = HeaderCmd
