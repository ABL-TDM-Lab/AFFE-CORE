# coding=utf-8
"""
Provide Finder classes to help find files of certain name or pattern in target directory
"""
import os
from abc import ABC, abstractmethod
from typing import List, Optional, final


class Finder(ABC):
    @final
    def find_first_in(self, target_dir: str) -> Optional[str]:
        for (cur_dir, dirs, files) in os.walk(target_dir):
            for file in files:
                if self._match(file):
                    return os.path.abspath(os.path.join(cur_dir, file))

    @final
    def find_all_in(self, target_dir: str) -> List[str]:
        paths = []
        for (dir_name, dirs_here, files_here) in os.walk(target_dir):
            for file in files_here:
                if self._match(file):
                    paths.append(os.path.abspath(os.path.join(dir_name, file)))
        return paths

    @abstractmethod
    def _match(self, file) -> bool:
        pass


class PatternFinder(Finder):
    def __init__(self, *, init: str = "", ext=""):
        self._init = init
        self._ext = ext

    def _match(self, file) -> bool:
        return file.startswith(self._init) and file.endswith(self._ext)


class FileNameFinder(Finder):
    def __init__(self, file_name: str):
        self._file_name = file_name

    def _match(self, file) -> bool:
        return file is self._file_name
