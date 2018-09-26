import unittest
from LowestCommonAncestor import *


class TestLCA(unittest.TestCase):
    def test_isEmpty(self):
        test1 = LCA()
        self.assertEqual(test1.isempty(), True, "Testing if LCA is empty")

    def test_empty_size(self):
        test2 = LCA()
        self.assertEqual(test2.__size__(), 0, "Testing if size of empty LCA is 0")

    '#TODO testLCA and other functions on empty tree'
    def test_lca(self):
        test = LCA()
        self.assertFalse(test.findlca(4, 5))

    def testInsert(self):
        test3 = LCA()
        self.assertEqual(test3.isempty(), True, "Testing if LCA is empty")
        self.assertEqual(test3.__size__(), 0, "Testing if size of empty LCA is 0")
        test3.insert(5)
        self.assertEqual(test3.isempty(), False, "Testing if LCA is no longer empty")
        self.assertEqual(test3.__size__(), 1, "Testing if size of empty LCA is 1")
        test3.insert(1)
        test3.insert(4)
        test3.insert(6)
        self.assertEqual(test3.__size__(), 4, "Testing if size of empty LCA is 1")

    '#TODO test inserting repetitively same data and check size'
    def testInsert2(self):
        test = LCA()
        test.insert(4)
        test.insert(5)
        test.insert(6)
        test.insert(4)
        test.insert(4)
        self.assertEqual(test.__size__(), 3, "Testing final size of LCA if it is 3")

    def testFindLCA(self):
        test4 = LCA()
        test4.insert(7)
        test4.insert(4)
        test4.insert(1)
        test4.insert(5)
        test4.insert(6)
        test4.insert(9)
        test4.insert(10)
        test4.insert(8)
        self.assertEqual(test4.findlca(7, 7), 7, "Find LCA if it is 7")
        self.assertEqual(test4.findlca(6, 1), 4, "Find LCA if it is 4")
        self.assertEqual(test4.findlca(1, 8), 7, "Find LCA if it is 7")
        self.assertEqual(test4.findlca(10, 8), 9, "Find LCA if it is 9")

    '#TODO test LCA on unavailable nodes in the tree'
    def testFindLCAfail(self):
        test5 = LCA()
        test5.insert(7)
        test5.insert(4)
        test5.insert(1)
        test5.insert(5)
        test5.insert(6)
        test5.insert(9)
        test5.insert(10)
        test5.insert(8)
        self.assertEqual(test5.findlca(4, 11), -1, "Find unavailable nodes in LCA")
        self.assertEqual(test5.findlca(13, 11), -1, "Find unavailable nodes in LCA")
        self.assertEqual(test5.findlca(13, 8), -1, "Find unavailable nodes in LCA")

    '#TODO test num values'
    def test_nonintegers(self):
        test6 = LCA()
        test6.insert(7)
        test6.insert(4)
        test6.insert(1)
        test6.insert(5)
        test6.insert(6)
        self.assertFalse(test6.findlca("RR", 6.798))
        self.assertFalse(test6.findlca(7, "6"))
        self.assertFalse(test6.findlca("r", 6))
        self.assertFalse(test6.findlca(None, None))


if __name__ == '__main__':
    unittest.main()
