import unittest
from LowestCommonAncestor import *


class TestDigraph(unittest.TestCase):

    def test_init(self):
        test = Digraph(0, 0)
        self.assertEqual(test.get_edge(), 0)
        self.assertEqual(test.get_vertex(), 0)

    def test_add_vertex(self):
        self.fail()

    def test_len(self):
        self.fail()

    def test_find_root(self):
        self.fail()

    def test_validate_vertex(self):
        self.fail()

    def test_incident(self):
        self.fail()

    def test_check_cyclic(self):
        self.fail()

    def test_get_vertex(self):
        self.fail()

    def test_get_edge(self):
        self.fail()

    def test_compute_lowest_common_ancestor(self):
        self.fail()

    def test_read_file(self):
        file_x = open("tinyDAG.txt", "r")
        vn = int(file_x.readline())
        en = int(file_x.readline())
        test = Digraph(vn, en)

        for x in file_x:
            test.add_vertex(int(x.split(" ")[0]), int(x.split(" ")[1]))

        self.assertEqual(test.get_vertex(), 13)
        self.assertEqual(test.get_edge(), 15)
        self.assertTrue(test.check_cyclic())
        self.assertEqual(test.find_root(), 2)
        self.assertEqual(test.len(), "")


if __name__ == '__main__':
    unittest.main()