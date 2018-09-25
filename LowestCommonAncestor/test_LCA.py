import unittest
from LowestCommonAncestor import *


class TestLCA(unittest.TestCase):
    def test_isEmpty(self):
        test1 = LCA()
        self.assertEqual(test1.isempty(), True, "Testing if LCA is empty")

    def test_findLCA(self):
        test2 = LCA()
        self.assertEqual(test2.__size__(), 0, "Testing if size of empty LCA is 0")

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

if __name__ == '__main__':
    unittest.main()
