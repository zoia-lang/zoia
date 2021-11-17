from dataclasses import dataclass

from files_src.zoia_file import ZoiaFile

@dataclass(slots=True)
class Chapter:
    main_file: ZoiaFile
    aux_files: list[ZoiaFile]
