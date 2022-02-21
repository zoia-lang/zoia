from validation.tys.text import TextTy

from ast_nodes import LineElementsNode
from exception import ValidationError
from utils import format_word_list

# TextTy that is restricted to only one word
class WordTy(TextTy):
    _ty_name = 'Word'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        text_str = super().validate_arg(cmd_arg)
        split_text = text_str.split()
        if len(split_text) > 1:
            fmt_extra = format_word_list(split_text[1:])
            if len(split_text) == 2:
                # Fix the grammar for a single extraneous word
                raise ValidationError(
                    cmd_arg.src_pos,
                    f'Parameters of type {self._ty_name} only accept single '
                    f'words - {fmt_extra} is extraneous')
            raise ValidationError(
                cmd_arg.src_pos,
                f'Parameters of type {self._ty_name} only accept single '
                f'words - {fmt_extra} are extraneous')
        return text_str
