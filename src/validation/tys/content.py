from dataclasses import dataclass

from validation.tys.any_ty import AnyTy
from validation.tys.none_ty import NoneTy

from ast_nodes import LineElementsNode, CommandNode
from ast_visitor import ACommandVisitor
from commands import get_command_type
from exception import ValidationError

@dataclass(slots=True)
class _ContentValidator(ACommandVisitor):
    parent_ty_name: str

    def visit_command(self, node: CommandNode):
        if isinstance(get_command_type(node).signature.ret_ty, NoneTy):
            raise ValidationError(
                node.src_pos,
                f'Parameters of type {self.parent_ty_name} only accept '
                f'document content, but \\{node.cmd_name} returns '
                f'{get_command_type(node).signature.ret_ty.compact()}')
        super().visit_command(node)

# Any type that will result in something visible in the output
class ContentTy(AnyTy):
    _ty_name = 'Content'
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        _ContentValidator(self._ty_name).visit(cmd_arg)
        return super().validate_arg(cmd_arg)
