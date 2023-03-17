'''
Test trie
'''
from helper import *
from bioID.data_type.ditrie import Ditrie as c

@ddt
class TestTrie(TestCase):

    def test_insert(self):
        t = c()
        # insert one pair
        res = t.insert('ab','xy')
        assert res.val == 'b'
        assert res.relatives[0].val == 'y'

        # insert duplicate
        res = t.insert('ab','xy')
        assert res.counter == 2

    def test_get(self):
        t = c()
        t.insert('ab','xy')
        
        # correct key
        res = t.get('ab')
        assert res == ['xy']
        # no such a key
        res = t.get('g')
        assert res == []
        # wrong key: empty
        res = t.get('')
        assert res == []

    def test_items(self):
        t = c()
        t.insert('ab','xy')
        t.insert('abc','xyz')
        res = [(a,b) for a, b in t.items()]
        expect = [('ab', ['xy']), ('abc', ['xyz'])]
        assert res == expect

    def test_switch(self):
        t = c()
        t.insert('ab','xy')
        t.insert('abc','xyz')
        t.switch()
        res = t.get('xy')
        assert res == ['ab']
        res = [(a,b) for a, b in t.items()]
        expect = [('xy', ['ab']), ('xyz', ['abc'])]
        assert res == expect