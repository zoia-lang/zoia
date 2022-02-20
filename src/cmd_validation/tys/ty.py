from dataclasses import dataclass

from cmd_validation.base import CmdValidator

class Ty(CmdValidator):
    _ty_name: str
    __slots__ = ()

    def compact(self) -> str:
        return self._ty_name
