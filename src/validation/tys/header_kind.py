from validation.tys.word import WordTy

from ast_nodes import LineElementsNode

# WordTy that must be one of several possible values
class HeaderKindTy(WordTy):
    _ty_name = 'HeaderKind'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        txt_str = super().validate_arg(cmd_arg)
        # TODO Validate header kind is one of the allowed ones here (and wrap
        #  in an enum?)
        return txt_str
