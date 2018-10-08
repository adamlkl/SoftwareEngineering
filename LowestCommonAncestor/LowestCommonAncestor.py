from collections import defaultdict


class Digraph:

    def __init__(self, vertices, edges):
        self.V = int(vertices)
        self.E = int(edges)
        self.digraph = defaultdict(list)
        self.indegree = [0] * self.V