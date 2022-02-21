from io import StringIO

from cmd_validation.tys.content import ContentTy

from ast_nodes import AArgumentNode, TextFragmentNode
from exception import ValidationError

# Any number of text fragments in a row
class TextTy(ContentTy):
    _ty_name = 'Text'
    __slots__ = ()

    def process_arg(self, cmd_arg: AArgumentNode):
        cmd_arg_val = super().process_arg(cmd_arg)
        s = StringIO()
        for arg_element in cmd_arg_val.elements:
            if not isinstance(arg_element, TextFragmentNode):
                raise ValidationError(
                    arg_element.src_pos,
                    'Parameters of type Text only accept text fragments')
            s.write(arg_element.text_val)
        return s.getvalue().strip()
