'''
Test Tree
'''
from tests.helper import *
from data_type.bio_tree import BioTree as c

@ddt
class TestTrie(TestCase):

    @skip
    def test_1(self):
        c().uniprotkb_acc_trie()
    @skip
    def test_2(self):
        c().select_uniprotkb_acc()

    def test_3(self):
        c().cal_time()