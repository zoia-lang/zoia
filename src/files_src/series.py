from dataclasses import dataclass

from files_src.work import Work

@dataclass(slots=True)
class Series:
    works: list[Work]
