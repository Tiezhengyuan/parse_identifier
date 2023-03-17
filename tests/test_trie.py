'''
Test trie
'''
from helper import *
from data_type.trie import Trie as c

@ddt
class TestTrie(TestCase):

    def test_node_size(self):
        t = c()
        res = t.insert(list('word'))
        assert sys.getsizeof(res) == 48
        res = t.insert(list('abc')*100)
        assert sys.getsizeof(res) == 48

    def test_insert(self):
        t = c()
        t.insert(list('wo'))
        t.insert(list('wolf'))
        t.insert(list('w'))
        res = [a for a,_ in t.scan()]
        assert res == ['w', 'wo', 'wolf']

    def test_search(self):
        t = c()
        res = t.search('wo')
        assert res == []

        t.insert(list('word'))
        t.insert(list('words'))
        t.insert(list('fox'))
        t.insert(list('wolf'))
        t.insert(list('wolf'))
        res = t.search('wo')
        expect = [('word', 2), ('wolf', 2), ('words', 1)]
        assert res == expect

        res = t.search('word')
        expect = [('word', 2),('words', 1),]
        assert res == expect


    def test_dump(self):
        t = c()
        t.insert(list('word'))
        t.insert(list('words'))
        t.insert(list('world'))
        t.insert(list('wolf'))
        t.insert(list('wolf'))
        t.insert(list('golf'))
        res = t.dump()
        expect = [('golf', 1), ('wolf', 2), ('word', 2),
                ('words', 1), ('world', 1)]
        assert res == expect

    def test_scan(self):
        t = c()
        res = [a for a,_ in t.scan()]
        assert res == []

        t.insert(list('word'))
        t.insert(list('words'))
        t.insert(list('world'))
        t.insert(list('wolf'))
        t.insert(list('wolf'))
        t.insert(list('golf'))
        res = [a for a,_ in t.scan()]
        expect = ['word', 'words', 'world', 'wolf', 'golf']
        assert res == expect

    def test_get(self):
        t = c()
        res = t.get('wo')
        assert res is None
        t.insert(list('word'))
        t.insert(list('words'))
        res = t.get('wo')
        assert res is None
        res = t.get('')
        assert res is None

        res = t.get('word')
        assert res == 'word'
        res = t.get('words')
        assert res == 'words'

    def test_get_node(self):
        t = c()
        res = t.get_node('wo')
        assert res is None
        t.insert(list('word'))
        t.insert(list('words'))
        res = t.get_node('wo')
        assert res is None
        res = t.get_node('')
        assert res is None

        res = t.get_node('word')
        assert getattr(res, 'val') == 'd'
        res = t.get_node('words')
        assert getattr(res, 'val') == 's'
        res = t.get_node('wordss')
        assert res is None

    def test_delete(self):
        t = c()
        res = t.delete('wo')
        assert res == []
        t.insert(list('word'))
        t.insert(list('words'))
        res = t.delete('wordss')
        assert res == []
        res = t.delete('')
        assert res == []
        res = t.delete('f')
        assert res == []

        t.insert(list('w'))
        t.insert(list('golf'))
        res = t.delete('wo')
        assert res ==  ['word', 'words']
        res = t.dump()
        assert res == [('golf', 1), ('w', 3)]
        res = t.delete('w')
        assert res ==  ['w',]
        res = t.dump()
        assert res == [('golf', 1)]


    def test_retrieve(self):
        t = c()
        res = t.retrieve(t.root)
        assert res == ''
        res = t.retrieve(None)
        assert res == ''
        res = t.retrieve('abc')
        assert res == ''

        last_node = t.insert('word')
        res = t.retrieve(last_node)
        assert res == 'word'

        last_node = t.insert('wo')
        res = t.retrieve(last_node)
        assert res == 'wo'
    
    def test_relative(self):
        t = c()
        node = t.insert(list('word'))
        node_a = t.insert(list('truck'))
        node_b = t.insert(list('car'))
        t.insert_relative(node, node_a)
        t.insert_relative(node, node_b)
        relatives = t.get_relatives(node)
        res = [i.val for i in relatives]
        assert res == ['k', 'r']
        res = [t.retrieve(i) for i in relatives]
        assert res == ['truck', 'car']


    def test_scan(self):
        t = c()
        t.insert(list('word'))
        t.insert(list('words'))
        t.insert(list('world'))
        t.insert(list('wolf'))
        t.insert(list('wolf'))
        t.insert(list('golf'))
        t.insert(list('abc')*100)
        res = t.memory_size()
        assert res == 15072