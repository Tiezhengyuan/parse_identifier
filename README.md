# bioID: suck, parse identifiers or accession numbers

## Introduction
bioID is a bioinformatics data structure library optimized for sucking identifiers or 
accession numbers into memory, parse those identifiers accession numbers to each other. 

Identifiers or accession numbers are defined and referenced by various biological databases.
Their number could be million size or even billion level.
Some data operations, such as query or parse, are very common.

bioID employs Data structure "trie" and "ditrie". Trie could suck tremendous identifiers into memory at a time. 
Ditrie could suck a large number of mapping of identifiers. Through the trie and ditrie, 
huge data operations including insert, get, search, delete, scan etc could be quickly called.


## testing

```
pytest -s tests
```


## quick start
Here, I provide two examples on how to suck huge accession numbers in memory.
Retrieve 169,652,527 UniProt Accession numbers from file and feed them into Trie.
Showed as the example below, accession numbers are stored in the object t. 
```
from bioID.data_type.trie import Trie
from bioID.data_type.ditrie import Ditrie

t = Trie()
for acc in UniProt_acc_iterator:
    t.insert(acc)
```

Retrieve 169,652,527 pairs of NCBI protein accession number and 
UniProt Accession numbers from file and feed them into Ditrie.
Showed as the example below, the mapping fo two accession numbers
are stored in the object map_trie, which is ready for query or parsing.
```
from bioID.data_type.trie import Trie
from bioID.data_type.ditrie import Ditrie

uniprotkb_acc_trie = Trie()
ncbi_acc_trie = Trie()
map_trie = Ditrie(uniprotkb_acc_trie, ncbi_acc_trie)
with open('gene_refseq_uniprotkb_collab', 'rt') as f:
    for ncbi_acc, uniprotkb_acc in f:
        map_trie.insert(ncbi_acc, uniprotkb_acc)
```



