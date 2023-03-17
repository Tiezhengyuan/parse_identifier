'''
Test trie
'''
from helper import *
from data_type.ditrie import Ditrie as c

@ddt
class TestTrie(TestCase):

    def test_insert(self):
        t = c()
        # insert one pair
        t.insert('ab','xy')
        res = t.get('ab')

        # insert duplicate
        t.insert('ab','xy')
        assert res == ['xy']
        res = t.get('ab')
        assert res == ['xy']

        # insert another
        t.insert('abc','xyz')
        res = [a for a,_ in t.btrie.scan()]
        assert res == ['xy', 'xyz']

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