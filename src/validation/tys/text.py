from io import StringIO

from validation.tys.content import ContentTy

from ast_nodes import LineElementsNode, TextFragmentNode
from exception import ValidationError

# Any number of text fragments in a row
class TextTy(ContentTy):
    _ty_name = 'Text'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        super().validate_arg(cmd_arg)
        s = StringIO()
        for arg_element in cmd_arg.elements:
            if not isinstance(arg_element, TextFragmentNode):
                raise ValidationError(
                    arg_element.src_pos,
                    f'Parameters of type {self._ty_name} only accept text '
                    f'fragments')
            s.write(arg_element.text_val)
        return s.getvalue().strip()
