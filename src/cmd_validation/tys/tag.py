from cmd_validation.tys.text import TextTy

from ast_nodes import AArgumentNode
from exception import ValidationError

# TextTy that may not contain commas
class TagTy(TextTy):
    _ty_name = 'Tag'
    __slots__ = ()

    def process_arg(self, cmd_arg: AArgumentNode):
        txt_str = super().process_arg(cmd_arg)
        if ',' in txt_str:
            raise ValidationError(
                cmd_arg.src_pos,
                'Parameters of type Tag may not include commas')
        return txt_str
