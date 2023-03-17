'''
Test Tree
'''
from helper import *
from bioID.data_type.process_id import ProcessID as c

@ddt
class TestTrie(TestCase):

    # @skip
    def test_1(self):
        infile = os.path.join(DIR_DATA, 'gene_refseq_uniprotkb_collab')
        c().uniprotkb_accession(infile)


    @skip
    def test_2(self):
        infile = os.path.join(DIR_DATA, 'gene_refseq_uniprotkb_collab')
        c().uniprotkb_accession_map(infile)

