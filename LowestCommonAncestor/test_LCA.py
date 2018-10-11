import unittest
from LowestCommonAncestorDAG import *


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
        self.assertEqual(test.print_digraph(), "")
    
    def test_find_root(self):
        test3 = Digraph(1, 1)
        self.assertEqual(test3.find_root(), 1)
    
    def test_find_root2(self):
        test4 = Digraph(3, 2)
        test4.add_vertex(0, 1)
        test4.add_vertex(0, 2)
        self.assertEqual(test4.find_root(), 0)
    
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
        self.assertEqual(test6.incidence(0), {1, 2})
    
    def test_check_cyclic(self):
        test7 = Digraph(3, 2)
        test7.add_vertex(0, 1)
        test7.add_vertex(0, 2)
        self.assertFalse(test7.check_cyclic())
        test8 = Digraph(3, 3)
        test8.add_vertex(0, 1)
        test8.add_vertex(1, 2)
        test8.add_vertex(2, 3)
        self.assertTrue(test8.check_cyclic())
    
    def test_compute_lowest_common_ancestor(self):
        self.fail()
    
    def test_read_file(self):
        file_xx = open("tinyDAG.txt", "r")
        vt = int(file_xx.readline())
        ed = int(file_xx.readline())
        test77 = Digraph(vt, ed)
        
        for y in file_xx:
            test77.add_vertex(int(y.split(" ")[0]), int(y.split(" ")[1]))
        file_x.close()


if __name__ == '__main__':
    unittest.main()
