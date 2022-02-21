from dataclasses import dataclass, field

from validation.base import CmdValidator
from validation.tys import Ty

from ast_nodes import LineElementsNode
from exception import ValidationError
from zoia_processor import process_zoia_arg

@dataclass(slots=True)
class Default(CmdValidator):
    ty: Ty
    _default_str: str = field(repr=False)
    default: LineElementsNode = field(init=False)

    def __post_init__(self):
        try:
            self.default = self.validate_arg(process_zoia_arg(
                self._default_str, '<Signature default>'))
        except ValidationError as e:
            raise SyntaxError('Failed to validate a Signature default '
                              'value') from e

    def validate_arg(self, cmd_arg: LineElementsNode):
        return self.ty.validate_arg(cmd_arg)

    def compact(self) -> str:
        return f'{self.ty.compact()} = {self._default_str}'
