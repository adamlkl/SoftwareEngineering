import unittest
from LowestCommonAncestor import *


class TestDigraph(unittest.TestCase):

    '''Test initianting the digraph class'''
    def test_init(self):
        test1 = Digraph(0, 0)
        self.assertEqual(test1.get_edge(), 0)
        self.assertEqual(test1.get_vertex(), 0)

    '''test adding vertex to the digraph'''
    def test_add_vertex(self):
        test2 = Digraph(3, 3)
        test2.add_vertex(0, 1)
        test2.add_vertex(1, 2)
        test2.add_vertex(2, 3)
        self.assertEqual(test2.print_digraph(), {0: [1], 1: [2], 2: []})

    '''test finding root in an empty digraph'''
    def test_find_root(self):
        test3 = Digraph(1, 1)
        self.assertEqual(test3.find_root(), [0])

    '''test finding root in an non-empty digraph'''
    def test_find_root2(self):
        test4 = Digraph(3, 2)
        test4.add_vertex(0, 1)
        test4.add_vertex(0, 2)
        self.assertEqual(test4.find_root(), [0])

    '''test if any vertex is available in a filled digraph'''
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

    '''test the incidence of a vertex'''
    def test_incident(self):
        test6 = Digraph(3, 2)
        test6.add_vertex(0, 1)
        test6.add_vertex(0, 2)
        self.assertEqual(test6.incidence(0), [1, 2])

    '''test check cylic on cyclic and acyclic digraph and check if compute lca returns -2 if digraoh is acyclic'''
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
        self.assertEqual(test8.compute_lca2(0, 1, 2), -2)
        test9 = Digraph(4, 3)
        test9.add_vertex(0, 1)
        test9.add_vertex(1, 2)
        test9.add_vertex(2, 3)
        self.assertFalse(test9.check_cyclic())

    '''test digraph in a text file, performs checks on every function on both roots in the digraph'''
    def test_read_file_and_compute_LCA2(self):
        file_x = open("tinyDAG.txt", "r")
        vn = int(file_x.readline())
        en = int(file_x.readline())
        test77 = Digraph(vn, en)

        for x in file_x:
            test77.add_vertex(int(x.split(" ")[0]), int(x.split(" ")[1]))
        file_x.close()
        self.assertEqual(test77.get_vertex(), vn)
        self.assertEqual(test77.get_edge(), en)
        self.assertTrue(test77.validate_vertex(5))
        self.assertFalse(test77.validate_vertex(70))

        self.assertFalse(test77.check_cyclic())

        self.assertEqual(test77.find_root(), [2, 8])

        self.assertEqual(test77.compute_lca2(test77.find_root()[0], 1, 6), [0])
        self.assertEqual(test77.compute_lca2(test77.find_root()[0], 5, 6), [0])
        self.assertEqual(test77.compute_lca2(test77.find_root()[0], 10, 11), [9])
        self.assertEqual(test77.compute_lca2(test77.find_root()[0], 10, 9), [9])
        self.assertEqual(test77.compute_lca2(test77.find_root()[0], 10, 4), [6])

        self.assertFalse(test77.haspathto(8))
        test77.bfs(test77.find_root()[1])
        self.assertTrue(test77.haspathto(8))
        self.assertTrue(test77.haspathto(7))
        self.assertEqual(test77.compute_lca2(8, 4, 12), [6])
        self.assertEqual(test77.compute_lca2(8, 10, 11), [9])
        self.assertEqual(test77.compute_lca2(500, 10, 1), -1)
        self.assertEqual(test77.compute_lca2(8, 10, 700), -1)
        self.assertEqual(test77.compute_lca2(8, 600, 1), -1)
        self.assertEqual(test77.compute_lca2(8, 0, 1), -3)

        self.assertEqual(test77.print_digraph(), {0: [6, 1, 5], 1: [], 2: [3, 0], 3: [5], 4: [], 5: [4],
                                                  6: [4, 9], 7: [6], 8: [7], 9: [12, 10, 11], 10: [],
                                                  11: [12], 12: []})


if __name__ == '__main__':
    unittest.main()
