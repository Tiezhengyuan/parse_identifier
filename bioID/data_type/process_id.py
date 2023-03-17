"""
data structure: The di-trie. Here are the features:
Define A trie and B trie:
one leave node of A trie is mapped to one or more leave nodes of B trie
"""
from bioID.utils.file import File
from bioID.utils.utils import Utils
from bioID.utils.constants import *

from .trie import Trie
from .ditrie import Ditrie

class ProcessID:
    
    def uniprotkb_accession(self, infile:str)->Trie:
        """
        source file: gene_refseq_uniprotkb_collab downloaded from NCBI/Entrez
        suck UniProtKB accession numbers
        """
        uniprotkb_acc_trie = Trie()
        n = 0
        for _,acc in File(infile).read_text(True, '\t'):
            uniprotkb_acc_trie.insert(acc)
            n += 1
        print(f"Total number of {n} UniProtKB accession numbers are fed into Trie.")
        return uniprotkb_acc_trie

    def uniprotkb_accession_map(self, infile:str)->Ditrie:
        '''
        source file: gene_refseq_uniprotkb_collab downloaded from NCBI/Entrez
        map: UniProtKB accession number ~ NCBI protein accession number
        '''
        uniprotkb_acc_trie = Trie()
        ncbi_acc_trie = Trie()
        map_trie = Ditrie(uniprotkb_acc_trie, ncbi_acc_trie)

        n = 0
        for ncbi_acc, uniprotkb_acc in File(infile).read_text(True, '\t'):
            map_trie.insert(ncbi_acc, uniprotkb_acc)
            n += 1
        print(f"Total number of {n} pairs of ccession numbers are fed into Ditrie.")
        return map_trie
    

