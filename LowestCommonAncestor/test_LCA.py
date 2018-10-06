import unittest
from LowestCommonAncestor import *


class TestLCA(unittest.TestCase):
    """#TODO test empty"""
    def test_isEmpty(self):

    '#TODO check empty size of tree'
    def test_empty_size(self):

    '#TODO testLCA and other functions on empty tree'
    def test_lca(self):

    def testInsert(self):

    '#TODO test inserting repetitively same data and check size'
    def testInsert2(self):

    '#TODO test inserting non-integer type data'
    def testInsert3(self):

    '#TODO test LCA on a filled tree'
    def testFindLCA(self):

    '#TODO test LCA on unavailable nodes in the tree'
    def testFindLCAfail(self):

    '#TODO test num values and non int type data on LCA'
    def test_nonintegers(self):

    def test_read_file(self):
        file_x = open("tinyDAG.txt", "r")
        vn = file_x.readline()
        en = file_x.readline()
        test = Digraph(vn, en)

        for x in file_x:
            s = x.readline()
            test.add_vertex(s.split(" ")[0], s.split(" ")[1])

        self.assertEqual(test.get_vertex(), vn)
        self.assertEqual(test.get_edge(), en)
        self.assertFalse(test.check_cyclic())


if __name__ == '__main__':
    unittest.main()
