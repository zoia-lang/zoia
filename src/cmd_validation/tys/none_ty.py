from cmd_validation.tys.any_ty import AnyTy

# Special type - only to be used as a return type for commands
class NoneTy(AnyTy):
    _ty_name = 'None'
    __slots__ = ()
