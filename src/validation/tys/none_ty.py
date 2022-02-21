from validation.tys.any_ty import AnyTy

from ast_nodes import LineElementsNode
from exception import ValidationError

# Special type - only to be used as a return type for commands
class NoneTy(AnyTy):
    _ty_name = 'None'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        # TODO Maybe add some detection to log to make it recognize internal
        #  errors and crash everything?
        raise ValidationError(
            cmd_arg.src_pos,
            f'[INTERNAL ERROR]: {self._ty_name} does not accept any kinds of '
            f'values. It should only be specified as a return type')
