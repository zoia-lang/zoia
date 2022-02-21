from validation.tys.text import TextTy

from ast_nodes import LineElementsNode
from exception import ValidationError

# TextTy that may not contain commas
class TagTy(TextTy):
    _ty_name = 'Tag'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        if ',' in txt_str:
            raise ValidationError(
                cmd_arg.src_pos,
                f'Parameters of type {self._ty_name} may not include commas')
        return txt_str
