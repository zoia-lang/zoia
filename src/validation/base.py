from ast_nodes import LineElementsNode
from exception import AbstractError

# NO IMPORTS FROM CMD_VALIDATION! This has to be importable in the entire
# package, including cmd_validation.tys

class CmdValidator:
    __slots__ = ()

    def validate_arg(self, cmd_arg: LineElementsNode):
        raise AbstractError()

    def compact(self) -> str:
        """Returns the compact signature representation of this Signature
        object as a string."""
        raise AbstractError()

    def __repr__(self):
        return self.compact()
