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
"""Implements an API that can be used to map Zoia AST nodes and leaves."""
from ast_nodes import AASTNode
from ast_visitor import AASTVisitor

class AASTMapper(AASTVisitor):
    """Abstract base class for Zoia AST mappers."""
    __slots__ = ()

    """Base class for Zoia AST mappers. Based on AASTVisitor."""
    def _try_visit_val(self, node_val):
        if isinstance(node_val, AASTNode):
            return node_val.accept(self)
        elif isinstance(node_val, list):
            ret_list = []
            for list_el in node_val:
                ret_list.append(self._try_visit_val(list_el))
            return ret_list
        return self._map_leaf(node_val)

    def _visit_default(self, node: AASTNode):
        for node_attr in node.__slots__:
            if not hasattr(node, node_attr):
                continue # Member descriptor, ignore
            setattr(node, node_attr,
                    self._try_visit_val(getattr(node, node_attr)))
        return node

    # API that is intended for overriding by end users begins here
    # pylint: disable=no-self-use
    def _map_leaf(self, leaf_val):
        """Maps a leaf value (i.e. anything other than a node) to a new
        value. Default behavior is the identity function (i.e. keeping the
        value the same)."""
        return leaf_val
