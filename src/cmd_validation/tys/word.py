from cmd_validation.tys.text import TextTy

from ast_nodes import AArgumentNode
from exception import ValidationError

# TextTy that is restricted to only one word
class WordTy(TextTy):
    _ty_name = 'Word'
    __slots__ = ()

    def process_arg(self, cmd_arg: AArgumentNode):
        text_str = super().process_arg(cmd_arg)
        split_text = text_str.split()
        if len(split_text) > 1:
            raise ValidationError(
                cmd_arg.src_pos,
                f'Parameters of type Word only accept single words - '
                f'{split_text[1:]!r} are extraneous')
        return text_str
