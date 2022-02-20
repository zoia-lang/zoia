from dataclasses import dataclass

from cmd_validation.base import CmdValidator
from cmd_validation.tys import Ty


@dataclass(slots=True)
class Default(CmdValidator):
    ty: Ty
    default: str
    has_default = True

    def compact(self) -> str:
        return f'{self.ty.compact()} = {self.default}'
