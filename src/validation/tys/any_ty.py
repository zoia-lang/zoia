from validation.tys.ty import Ty

from ast_nodes import LineElementsNode

# Absolutely any type - basically ContentTy + NoneTy
class AnyTy(Ty):
    _ty_name = 'Any'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        return cmd_arg
