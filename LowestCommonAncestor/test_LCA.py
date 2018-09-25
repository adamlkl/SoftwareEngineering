import unittest
from LowestCommonAncestor import *


class TestLCA(unittest.TestCase):
    def test_isEmpty(self):
        test1 = LCA()
        self.assertEqual(test1.isempty(), True, "Testing if LCA is empty")

    def test_findLCA(self):
        test2 = LCA()
        self.assertEqual(test2.__size__(), 0, "Testing if size of empty LCA is 0")

if __name__ == '__main__':
    unittest.main()
