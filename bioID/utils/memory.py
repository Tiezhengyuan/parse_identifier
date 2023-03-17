import os
import sys
import pandas as pd
from sys import getsizeof, stderr
import itertools

class Memory:

    @staticmethod
    def memory_size(size):
        if size < 1024:
            return f"{size} Bytes"
        for unit in ['KB', 'MB', 'GB', 'TB', 'PB',]:
            size /= 1024
            if size < 1024:
                return f"{round(size,1)} {unit}"
            
    @staticmethod
    def dict_deep_size(data:dict):
        """
        Returns the approximate memory footprint an object and all of its contents.
        """
        total = 0
        pool = [data]
        while pool:
            curr = pool.pop(0)
            # pointer size of this dict
            total += sys.getsizeof(curr)
            # size of keys
            total += sum(sys.getsizeof(i) for i in list(curr))
            # print(list(curr), sum(sys.getsizeof(i) for i in list(curr)))
            for v in curr.values():
                if isinstance(v, dict):
                    # print(v)
                    pool.append(v)
                else:
                    total += sys.getsizeof(v)
                    # print('v', sys.getsizeof(v))
        return total
