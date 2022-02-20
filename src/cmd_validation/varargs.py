from dataclasses import dataclass
from enum import Enum

from cmd_validation.base import CmdValidator
from cmd_validation.tys import Ty

from ast_nodes import AArgumentNode

class _VarArgsType(Enum):
    VA_STD = 0
    VA_EITHER_OR = 1
    VA_KWD = 2

VARARGS_STD = _VarArgsType.VA_STD
VARARGS_EITHER_OR = _VarArgsType.VA_EITHER_OR
VARARGS_KWD = _VarArgsType.VA_KWD

@dataclass(slots=True)
class Varargs(CmdValidator):
    va_type: _VarArgsType
    ty: Ty

    def process_arg(self, cmd_arg: AArgumentNode):
        return self.ty.process_arg(cmd_arg)

    def compact(self) -> str:
        if self.va_type is VARARGS_STD:
            return f'~ {self.ty.compact()}*'
        if self.va_type is VARARGS_EITHER_OR:
            return f'{self.ty.compact()}*'
        if self.va_type is VARARGS_KWD:
            return f'$ {self.ty.compact()}*'
