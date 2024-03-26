
from typing import Iterable

class File:
    def __init__(self, infile:str):
        self.infile = infile
    
    def read_text(self, has_header:bool=True, sep:str='\t')->Iterable:
        with open(self.infile, 'rt') as f:
            if has_header:
                next(f)
            for line in f:
                items = line.rstrip().split(sep)
                yield items
        