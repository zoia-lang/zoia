from dataclasses import dataclass

from files_src.chapter import Chapter

@dataclass(slots=True)
class Work:
    chapters: list[Chapter]
