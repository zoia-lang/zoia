# TODO This should maybe be elsewhere?
from dataclasses import dataclass
from enum import Enum

class FileType(Enum):
    ALIASES = 0


@dataclass(slots=True)
class ZoiaFile:
    pass
