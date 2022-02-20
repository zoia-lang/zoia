from cmd_validation.tys.ty import Ty

from ast_nodes import AArgumentNode

# Absolutely any type - basically ContentTy + NoneTy
class AnyTy(Ty):
    _ty_name = 'Any'
    __slots__ = ()

    def process_arg(self, cmd_arg: AArgumentNode):
        return cmd_arg.arg_value # Accept and don't change anything
