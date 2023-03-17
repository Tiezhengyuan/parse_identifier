
import os
from typing import Callable, Iterable

class File:
    def __init__(self, infile:str):
        self.infile = infile
    
    def read_text(self, has_header:bool=True, rows:int=None, \
            sep:str='\t')->Iterable:
        if rows is None: rows = 1e3
        with open(self.infile, 'rt') as f:
            n = 0
            if has_header:
                next(f)
            for line in f:
                n += 1
                items = line.rstrip().split(sep)
                if n > rows:
                    break
                yield items
        