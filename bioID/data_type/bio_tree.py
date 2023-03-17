"""
data structure: The di-trie. Here are the features:
Define A trie and B trie:
one leave node of A trie is mapped to one or more leave nodes of B trie
"""
import sys
import random
from utils.file import File
from utils.utils import Utils
from utils.memory import Memory
from commons import *
import time

from typing import Iterable
from .trie import TrieNode, Trie
from .ditrie import Ditrie

class BioTree:
    def __init__(self):
        pass

    
    def uniprotkb_acc_trie(self):
        outfile = os.path.join(dir_results, f"uniprotkb_acc_trie.txt")
        with open(outfile, 'wt') as wf:
            wf.write(f"avg_characters/item\tmemory_usage\trecords_number\n")
            for i in range(1, 9):
                i = pow(10, i)
                m, n = 0, 0
                t = Trie()
                print(i)
                for _,r in File(uniprotkb_file).read_text(True, i, '\t'):
                    n += 1
                    m += len(r)
                    t.insert(r)
                avg_len = str(round(m/n,2))
                memory = Memory.memory_size(t.memory_size())
                stat = '\t'.join([avg_len, memory, str(n), '\n'])
                wf.write(stat)

    def select_uniprotkb_acc(self):
        n=0
        pool = [random.randint(1,1e8) for i  in range(100)]
        for _,r in File(uniprotkb_file).read_text(True, 1e8, '\t'):
            n+=1
            if n in pool:
                print(f"\"{r}\"", end= ', ')
    
    def cal_time(self):
        start =  time.time()
        t = Trie()
        for _,r in File(uniprotkb_file).read_text(True, 1e8, '\t'):
            t.insert(r)
        end =  time.time()
        # ~6.29min
        print('min:', (end-start)/60)

        # pool = ["A0A3G5UJ09", "F8XY74", "A0A3U8P868", "A0A4V6KMA5", 
        #         "J8EVX6", "A0A2D2D3B6", "A0A0E2SZF9", "A0A1Q8KHV1", 
        #         "A0A0D0LUL5", "A0A0H3CQR2", "E8U7E3", "G2I0W7", 
        #         "K0M9Y3", "A0A178PLB1", "A0A085HMW2", "A0A0Z8NRX6",
        #         "A0A0G2ZI72", "A0A0Q2M151", "A0A0R1HR88", "A0A2X2S0G1", 
        #         "A0A191V1R6", "A0A1B1EHI8", "A0A1E5LI73", "A0A1X0A724", 
        #         "A0A158F0C8", "A0A977FWM8", "A0A2S9BNK3", "A0A2T0Q134", 
        #         "A0A2V3XXJ6", "A0A3E5EPH4",]
        start =  time.time()
        for _,r in File(uniprotkb_file).read_text(True, 1e8, '\t'):
            t.get_node(r)
        end =  time.time()
        # 157.64
        print('second:', end-start)
