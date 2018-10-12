import unittest
from LowestCommonAncestor import *


class TestDigraph(unittest.TestCase):
    
    def test_init(self):
        test1 = Digraph(0, 0)
        self.assertEqual(test1.get_edge(), 0)
        self.assertEqual(test1.get_vertex(), 0)
    
    def test_add_vertex(self):
        test2 = Digraph(3, 3)
        test2.add_vertex(0, 1)
        test2.add_vertex(1, 2)
        test2.add_vertex(2, 3)
        self.assertEqual(test2.print_digraph(), {0: [1], 1: [2], 2: []})
    
    def test_find_root(self):
        test3 = Digraph(1, 1)
        self.assertEqual(test3.find_root(), [0])
    
    def test_find_root2(self):
        test4 = Digraph(3, 2)
        test4.add_vertex(0, 1)
        test4.add_vertex(0, 2)
        self.assertEqual(test4.find_root(), [0])
    
    def test_validate_vertex(self):
        test5 = Digraph(3, 3)
        test5.add_vertex(0, 1)
        test5.add_vertex(1, 2)
        test5.add_vertex(2, 3)
        self.assertTrue(test5.validate_vertex(0))
        self.assertTrue(test5.validate_vertex(1))
        self.assertTrue(test5.validate_vertex(2))
        self.assertFalse(test5.validate_vertex(7))
        self.assertFalse(test5.validate_vertex(-1))
    
    def test_incident(self):
        test6 = Digraph(3, 2)
        test6.add_vertex(0, 1)
        test6.add_vertex(0, 2)
        self.assertEqual(test6.incidence(0), [1, 2])
    
    def test_check_cyclic(self):
        test7 = Digraph(3, 2)
        test7.add_vertex(0, 1)
        test7.add_vertex(0, 2)
        self.assertFalse(test7.check_cyclic())
        test8 = Digraph(3, 3)
        test8.add_vertex(0, 1)
        test8.add_vertex(1, 2)
        test8.add_vertex(2, 0)
        self.assertTrue(test8.check_cyclic())
        test9 = Digraph(4, 3)
        test9.add_vertex(0, 1)
        test9.add_vertex(1, 2)
        test9.add_vertex(2, 3)
        self.assertFalse(test9.check_cyclic())
    
    def test_compute_lowest_common_ancestor(self):
        test10 = Digraph(3, 2)
        test10.add_vertex(0, 1)
        test10.add_vertex(0, 2)
        self.assertEqual(test10.compute_lowest_common_ancestor(1, 2, 0), 0)
    
    def test_read_file_and_compute_LCA(self):
        file_x = open("tinyDAG.txt", "r")
        vn = int(file_x.readline())
        en = int(file_x.readline())
        test77 = Digraph(vn, en)
        
        for x in file_x:
            test77.add_vertex(int(x.split(" ")[0]), int(x.split(" ")[1]))
        file_x.close()
        self.assertFalse(test77.check_cyclic())


if __name__ == '__main__':
    unittest.main()
