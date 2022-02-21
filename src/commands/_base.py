from typing import Any

from ast_nodes import CommandNode
from exception import AbstractError
from src_pos import SourcePos
from validation import Signature

class _ACommand:
    signature: Signature
    cmd_args: dict[str, Any]
    cmd_args_pos: dict[str, SourcePos]
    cmd_varargs: list[Any]
    cmd_varargs_pos: list[SourcePos]
    __slots__ = ('cmd_args', 'cmd_args_pos', 'cmd_varargs', 'cmd_varargs_pos')

    def __init__(self, node: CommandNode):
        c_a, c_ap, c_v, c_vp = self.signature.validate_args(node.arguments)
        self.cmd_args = c_a
        self.cmd_args_pos = c_ap
        self.cmd_varargs = c_v
        self.cmd_varargs_pos = c_vp

    def exec_command(self, ctx):
        raise AbstractError()
