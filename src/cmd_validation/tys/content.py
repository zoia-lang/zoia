from cmd_validation.tys.any_ty import AnyTy

from ast_nodes import AArgumentNode

# Any type that will result in something visible in the output
class ContentTy(AnyTy):
    _ty_name = 'Content'
    __slots__ = ()

    # TODO This needs to check commands for return value None in the future
