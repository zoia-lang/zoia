from validation.tys.word import WordTy

from ast_nodes import LineElementsNode
from exception import ValidationError

# WordTy that is restricted to digits
class IntTy(WordTy):
    _ty_name = 'Int'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        try:
            return int(txt_str)
        except ValueError as e:
            raise ValidationError(
                cmd_arg.src_pos,
                f"Parameters of type {self._ty_name} only accept valid "
                f"integers, which {txt_str} is not") from e
