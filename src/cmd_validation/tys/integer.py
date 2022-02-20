from cmd_validation.tys.word import WordTy

from ast_nodes import AArgumentNode
from exception import ValidationError

# WordTy that is restricted to digits
class IntTy(WordTy):
    _ty_name = 'Int'
    __slots__ = ()

    def process_arg(self, cmd_arg: AArgumentNode):
        txt_str = super().process_arg(cmd_arg)
        try:
            return int(txt_str)
        except ValueError as e:
            raise ValidationError(
                cmd_arg.src_pos,
                f"Parameters of type Int only accept valid integers, which "
                f"{txt_str} is not") from e
